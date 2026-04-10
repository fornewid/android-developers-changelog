---
title: https://developer.android.com/develop/ui/compose/performance/stability/diagnose
url: https://developer.android.com/develop/ui/compose/performance/stability/diagnose
source: md.txt
---

If you are experiencing performance issues that result from unnecessary or
excessive recomposition, you should debug the stability of your app. This guide
outlines several methods for doing so.
| **Important:** You should aim to resist unnecessary or premature optimization. Before optimizing for stability, verify you are following our [best practices
| for Compose performance](http://goo.gle/compose-performance).
| **Note:** If you would like more information about how to measure performance properly, see the [Macrobenchmark guide](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview).

## Layout Inspector

The Layout Inspector in Android Studio lets you see which composables are
recomposing in your app. It displays counts of how many times Compose has
recomposed or skipped a component.

![Recomposition and skips counts in the Layout Inspector](https://developer.android.com/static/develop/ui/compose/images/performance/stability/layout-inspector.png)

## Compose compiler reports

The Compose compiler can output the results of its stability inference for
inspection. Using this output, you can determine which of your composables are
skippable, and which are not. The follow subsections summarize how to use these
reports, but for more detailed information see the [technical
documentation](https://github.com/JetBrains/kotlin/blob/master/plugins/compose/design/compiler-metrics.md).
| **Warning:** You should only use this technique if you are actually experiencing performance issues related to stability. Trying to make your entire UI skippable is a premature optimization that could lead to maintenance difficulties in the future.

### Setup

Compose compiler reports are not enabled by default. You can activate them with
a compiler flag. The [exact setup](https://github.com/JetBrains/kotlin/blob/master/plugins/compose/design/compiler-metrics.md#enabling-metrics) varies depending on your
project, but for projects using the [Compose compiler gradle plugin](https://developer.android.com/develop/ui/compose/compiler) you can
add the following in each module's `build.gradle` file.  

      android { ... }

      composeCompiler {
        reportsDestination = layout.buildDirectory.dir("compose_compiler")
        metricsDestination = layout.buildDirectory.dir("compose_compiler")
      }

Compose compiler reports will now be generated when building your project.
| **Important:** Make sure to always run this on a release build to ensure accurate results.

#### Example output

The `reportsDestination` outputs three files. The following are example outputs
from [JetSnack](https://github.com/android/compose-samples/tree/master/Jetsnack).

- **`<modulename>-classes.txt`:** A report on the stability of classes in this module. [Sample](https://gist.github.com/bentrengrove/9b823045a160d8a5d986bb4b31106245).
- **`<modulename>-composables.txt`:** A report on how restartable and skippable the composables are in the module. [Sample](https://gist.github.com/bentrengrove/a8ee3716a7df136144041134575f5fcb).
- **`<modulename>-composables.csv`:** A `CSV` version of the composables report that you can import into a spreadsheet or processing using a script. [Sample](https://gist.github.com/bentrengrove/2beb1b2993f68f61a7ba3ed91a1c75c9)

| **Note:** The `metricsDestination` configuration produces overall statistics on the number of composables in your project and other similar info.
| **Note:** These reports make use of the compiler tags described in the [Compose
| stability](https://developer.android.com/develop/ui/compose/performance/stability) guide.

#### Composables report

The `composables.txt` file details each composable functions for the given
module, including the stability of their parameters, and whether they are
restartable or skippable. The following is a hypothetical example from
[JetSnack](https://github.com/android/compose-samples/tree/master/Jetsnack):  

    restartable skippable scheme("[androidx.compose.ui.UiComposable]") fun SnackCollection(
      stable snackCollection: SnackCollection
      stable onSnackClick: Function1<Long, Unit>
      stable modifier: Modifier? = @static Companion
      stable index: Int = @static 0
      stable highlight: Boolean = @static true
    )

This `SnackCollection` composable is completely restartable, skippable, and
stable. This is generally preferable, although certainly not mandatory.

On the other hand, let's take a look at another example.  

    restartable scheme("[androidx.compose.ui.UiComposable]") fun HighlightedSnacks(
      stable index: Int
      unstable snacks: List<Snack>
      stable onSnackClick: Function1<Long, Unit>
      stable modifier: Modifier? = @static Companion
    )

The `HighlightedSnacks` composable is not skippable. Compose never skips it
during recomposition. This occurs even if none of its parameters have changed.
The reason for this is the `unstable` parameter, `snacks`.

#### Classes report

The file `classes.txt` contains a similar report on the classes in the given
module. The following snippet is the output for the class `Snack`:  

    unstable class Snack {
      stable val id: Long
      stable val name: String
      stable val imageUrl: String
      stable val price: Long
      stable val tagline: String
      unstable val tags: Set<String>
      <runtime stability> = Unstable
    }

For reference, the following is the definition of `Snack`:  

    data class Snack(
        val id: Long,
        val name: String,
        val imageUrl: String,
        val price: Long,
        val tagline: String = "",
        val tags: Set<String> = emptySet()
    )

The Compose compiler has marked `Snack` as unstable. This is because the type of
the `tags` parameter is `Set<String>`. This is an immutable type, given that it
is not a `MutableSet`. However, standard collection classes such as `Set`,
`List`, and `Map` are ultimately interfaces. As such, the underlying
implementation may still be mutable.

For example, you could write `val set: Set<String> = mutableSetOf("foo")`. The
variable is constant and its declared type is not mutable, but its
implementation is *still* mutable. The Compose compiler cannot be sure of the
immutability of this class as it only sees the declared type. It therefore marks
`tags` as unstable.
| **Important:** For information about how to bring stability to an unstable class such as this, see the [Fix stability issues](https://developer.android.com/develop/ui/compose/performance/stability/fix) guide.