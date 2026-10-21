---
title: https://developer.android.com/develop/ui/compose/performance/stability/fix
url: https://developer.android.com/develop/ui/compose/performance/stability/fix
source: md.txt
---

When faced with an [unstable class](https://developer.android.com/develop/ui/compose/performance/stability/diagnose) that causes performance issues, you
should optimize how Compose compares or instantiates it. This document outlines
several techniques you can use to do so.

> [!IMPORTANT]
> **Important:** Before you fix stability issues, you should learn to properly diagnose them and verify with benchmarks that recomposition is actually causing a performance bottleneck. For information, see the [Diagnose stability issues](https://developer.android.com/develop/ui/compose/performance/stability/diagnose) guide.

## Enable strong skipping

[Strong skipping mode](https://developer.android.com/develop/ui/compose/performance/stability/strongskipping) is enabled by default starting in Kotlin 2.0.20.
Strong skipping mode allows composables with unstable parameters to be skipped
by comparing unstable parameters using instance equality (`===`), while stable
parameters continue to be compared using structural equality
(`Object.equals()`).

If you are using a Kotlin version lower than 2.0.20, enable strong skipping mode
first. If strong skipping mode is already enabled and a composable is still
recomposing unnecessarily, check whether new instances of unstable parameters
are being allocated on every recomposition pass.

See [Strong skipping](https://developer.android.com/develop/ui/compose/performance/stability/strongskipping) for more information.

## Make the class immutable

You can also make an unstable class completely immutable so the compiler can
infer its stability automatically.

- **Immutable** : Indicates a type where the value of any properties can never change after an instance of that type is constructed, and all methods are referentially transparent.
  - Make sure all the class's properties are both `val` rather than `var`, and of immutable types.
  - Primitive types such as `String`, `Int`, and `Float` are always immutable.
  - Flat `data class` types with `val` primitive or `String` properties in modules built with the Compose compiler are already inferred as stable and compared with `.equals()` automatically---you don't need to annotate them with `@Immutable`.
  - If immutability is impossible, then you must use Compose state for any mutable properties.
- **Stable**: Indicates a type that is mutable. The Compose runtime does not become aware if and when any of the type's public properties or method behavior would yield different results from a previous invocation.

> [!IMPORTANT]
> **Important:** In practice, this means you should use Compose state for any mutable property. For example, `mutableStateOf(...)`.

## Collections and stability

A common reason why Compose considers a class unstable is collections. As noted
in the [Diagnose stability issues](https://developer.android.com/develop/ui/compose/performance/stability/diagnose) page, the Compose compiler cannot be
completely sure that collection interfaces such as `List`, `Map`, and `Set` are
truly immutable and therefore marks them as unstable.

Consider this class from the [Diagnose stability issues](https://developer.android.com/develop/ui/compose/performance/stability/diagnose) guide:

    unstable class Snack {
      ...
      unstable val tags: Set<String>
      ...
    }

> [!NOTE]
> **Note:** This snippet is the output from the Compose compiler, not the class definition. For more information, see the [stability guide](https://developer.android.com/develop/ui/compose/performance/stability).

With [Strong skipping mode](https://developer.android.com/develop/ui/compose/performance/stability/strongskipping) enabled (the default in Kotlin 2.0.20 and
higher), **unstable collections and classes containing collections already skip
recomposition** using instance equality (`===`) whenever the same reference is
passed.

Be cautious before replacing `kotlin.collections.List`, `Set`, or `Map` with
Kotlinx Immutable Collections (`ImmutableList`, `ImmutableSet`, `ImmutableMap`),
or adding `@Immutable`, `@Stable`, or `stability_config.conf` rules to
collection-holding models. Under strong skipping mode, standard `List` skips
using reference equality (`===`), whereas `ImmutableList` and annotated
collection models run element-by-element `.equals()` comparisons on every
recomposition pass.

For large collections or lazy layouts (`LazyColumn`, `LazyRow`, `LazyGrid`),
checking `.equals()` on every item can take longer than recomposing. This cost
doubles if you pass an `ImmutableList` property from a `data class` to a child
composable:

    data class SnackCategory(
        val name: String,
        val snacks: ImmutableList<Snack>
    )

    @Composable
    fun CategorySection(category: SnackCategory) {
        Text(category.name)
        // Compose compares category.snacks twice: once in SnackCategory.equals()
        // for CategorySection, and again for HighlightedSnacks.
        HighlightedSnacks(snacks = category.snacks)
    }

Instead of forcing structural equality on collections, preserve the collection's
instance reference across emissions (for example, by caching transformations in
your `ViewModel` or with `remember`) so Compose can skip using instance equality
(`===`). Consider `ImmutableList` or stability annotations on collection-holding
models only when you can't preserve the collection's instance reference and
benchmarks confirm that structural equality checks are faster than recomposing.
If you're using a Kotlin version lower than 2.0.20, enable [Strong skipping
mode](https://developer.android.com/develop/ui/compose/performance/stability/strongskipping) first.

## Annotate with `Stable` or `Immutable`

A possible path to resolving stability issues for small classes with inexpensive
`.equals()` checks is to annotate unstable classes with either `@Stable` or
`@Immutable`.

> [!WARNING]
> **Warning:** These annotations don't make a class immutable or stable on its own. Instead, by using these annotations you are opting in to a contract with the compiler. Incorrectly annotating a class could cause recomposition to break or degrade performance.

Annotating a class is overriding what the compiler would otherwise [infer](https://developer.android.com/develop/ui/compose/performance/stability)
about your class. It is similar to the [`!!`](https://kotlinlang.org/docs/null-safety.html#the-operator) [operator in Kotlin](https://kotlinlang.org/docs/null-safety.html#the-operator). You
should be very careful about how you use these annotations. Overriding the
compiler behavior could lead you to unforeseen bugs, such as your composable not
recomposing when you expect it to.

With [Strong skipping mode](https://developer.android.com/develop/ui/compose/performance/stability/strongskipping) enabled, follow these guidelines when deciding
whether to add `@Stable` or `@Immutable`:

- **Don't annotate classes that are already inferred as stable** : Classes with `val` properties of stable types in modules built with the Compose compiler are already inferred as stable.
- **Only annotate classes with cheap `.equals()` checks when instances are
  recreated** : Add `@Stable` or `@Immutable` when the compiler can't infer stability (for example, interfaces or classes from non-Compose modules) **and** a data source allocates new object instances for unchanged items on every emission, provided the class is small and has an inexpensive `.equals()` check.
- **Be cautious with models containing collections** : Avoid adding `@Stable` or `@Immutable` to data models that hold large collections (`List`, `Set`, `Map`), especially for models used in lazy layouts (`LazyColumn`, `LazyRow`, `LazyGrid`, `Pager`). Leaving those models unannotated lets Compose compare them using instance equality (`===`) instead of running structural `.equals()` checks across every element.

The following snippet provides a minimal example of a flat data class (without
collection properties) annotated as immutable when defined in a module where the
compiler cannot infer stability:

    @Immutable
    data class SnackSummary(
        val id: Long,
        val name: String,
        val price: Long
    )

Whether you use the `@Immutable` or `@Stable` annotation, the Compose compiler
marks the `SnackSummary` class as stable and compares it using
`Object.equals()`.

### Annotated classes in collections

Consider a composable that includes a parameter of type `List<Snack>`:

    restartable skippable scheme("[androidx.compose.ui.UiComposable]") fun HighlightedSnacks(
      stable index: Int
      unstable snacks: List<Snack>
      stable onSnackClick: Function1<Long, Unit>
      stable modifier: Modifier? = @static Companion
    )

Even if `Snack` is stable or annotated with `@Immutable`, the Compose compiler
still marks the `snacks` parameter in `HighlightedSnacks` as `unstable` because
`List` is an interface.

With [Strong skipping mode](https://developer.android.com/develop/ui/compose/performance/stability/strongskipping) enabled, `HighlightedSnacks` is still marked
`skippable` and skips recomposition using instance equality (`===`) when the
same `List` instance is passed. You can make the `snacks` parameter `stable` by
wrapping `List<Snack>` in an `@Immutable` wrapper class, replacing `List<Snack>`
with `ImmutableList<Snack>`, or adding `kotlin.collections.*` to your [stability
configuration file](https://developer.android.com/develop/ui/compose/performance/stability/fix#configuration-file).

However, doing so causes Compose to run an element-by-element `.equals()`
comparison on every recomposition pass. Only use these approaches when you
can't preserve the list's instance reference and benchmarks show a benefit.

## Stability configuration file

Beginning with Compose Compiler 1.5.5, a configuration file of classes to
consider stable can be provided at compile time. This allows for considering
classes you don't control, such as standard library classes like
`LocalDateTime`, as stable.

> [!WARNING]
> **Warning:** These configurations don't make a class stable on its own. Instead, by using these configurations, you opt in to a contract with the compiler. Incorrectly configuring a class could cause recomposition to break.

The configuration file is a plain text file with one class per row. Comments,
single, and double wildcards are supported.

> [!NOTE]
> **Note:** Unlike proguard configuration, wildcards can only indicate full symbol name (package, class name, etc). Partial matches, such as `*ClassName` or `*Model*`, are not supported.

An example configuration:

    // Consider LocalDateTime stable
    java.time.LocalDateTime
    // Consider my datalayer stable
    com.datalayer.*
    // Consider my datalayer and all submodules stable
    com.datalayer.**
    // Consider my generic type stable based off it's first type parameter only
    com.example.GenericClass<*,_>

To enable this feature, pass the path of the configuration file to the
`composeCompiler` options block of the [Compose compiler Gradle plugin](https://developer.android.com/develop/ui/compose/compiler)
configuration.

    composeCompiler {
      stabilityConfigurationFile = rootProject.layout.projectDirectory.file("stability_config.conf")
    }

As the Compose compiler runs on each module in your project separately, you can
provide different configurations to different modules if needed. Alternatively,
have one configuration at the root level of your project and pass that path to
each module.

## Multiple modules

Another common issue involves multi-module architecture. The Compose compiler
can only infer whether a class is stable if all of the non-primitive types that
it references are either explicitly marked as stable or in a module that was
also built with the Compose compiler.

If your data layer is in a separate module to your UI layer, which is the
recommended approach, this may be an issue you encounter. Under [Strong skipping
mode](https://developer.android.com/develop/ui/compose/performance/stability/strongskipping), classes from non-Compose modules are treated as unstable and still
skip recomposition using instance equality (`===`) when the same instance is
passed. However, if your data layer frequently allocates new instances of small,
flat models with identical values on every emission, you can opt in to
structural equality (`Object.equals()`).

### Solution

To solve this issue you can take one of the following approaches:

1. Add small, flat classes with cheap `.equals()` checks to your [Compiler
   configuration file](https://developer.android.com/develop/ui/compose/performance/stability/fix#configuration-file).
2. Enable the Compose compiler on your data layer modules, or tag your classes with `@Stable` or `@Immutable` where appropriate.
   - This involves adding a Compose dependency to your data layer. However, it is just the dependency for the Compose runtime and not for `Compose-UI`.
3. Within your UI module, wrap your data layer classes in UI-specific wrapper classes.

The same issue also occurs when using external libraries if they don't use the
Compose compiler.

## Not every composable should be skippable

When working to fix issues with stability, you shouldn't attempt to make every
composable skippable or force structural equality on every parameter. Skipping a
composable isn't free: every parameter of a skippable composable is stored by
the Compose runtime as if it was remembered, and Compose must compare each
parameter against its previous value each time the function recomposes to
determine whether it should be skipped. Attempting to force skipping everywhere
can lead to premature optimization that introduces more overhead than it saves.

There are many situations where forcing structural stability doesn't have any
real benefit and can degrade performance or maintainability. For example:

- A composable that is not recomposed often, or at all.
- A composable that in itself just calls skippable composables.
- A composable with a large number of parameters or collection models with expensive `.equals()` implementations. In this case, the cost of checking if any parameter has changed can outweigh the cost of a cheap recomposition.

Don't over-index on recomposition counts alone. Focus on making composables
lightweight to execute, deferring rapidly changing state reads to the Layout or
Draw phases, and verifying changes with benchmarks. When a composable is
skippable, it adds a small overhead which may not be worth it. You can even
annotate your composable to be [non-restartable](https://developer.android.com/reference/kotlin/androidx/compose/runtime/NonRestartableComposable) or [non-skippable](https://developer.android.com/reference/kotlin/androidx/compose/runtime/NonSkippableComposable) in
cases where you determine that being restartable or skippable is more overhead
than it's worth.