---
title: https://developer.android.com/develop/ui/compose/performance/stability
url: https://developer.android.com/develop/ui/compose/performance/stability
source: md.txt
---

Compose considers types to be either stable or unstable. A type is stable if it
is immutable, or if it is possible for Compose to know whether its value has
changed between recompositions. A type is unstable if Compose can't know whether
its value has changed between recompositions.

Compose uses the stability of a composable's parameters to determine how to
compare inputs and decide whether it can skip the composable during
[recomposition](https://developer.android.com/develop/ui/compose/mental-model#recomposition) (with [Strong skipping mode](https://developer.android.com/develop/ui/compose/performance/stability/strongskipping) enabled by default starting
in Kotlin 2.0.20):

- **Stable parameters:** Compose compares stable parameters using structural equality (`Object.equals()`). If a composable's stable parameters are equal to their previous values, Compose skips it.
- **Unstable parameters:** With [Strong skipping mode](https://developer.android.com/develop/ui/compose/performance/stability/strongskipping) enabled (the default in Kotlin 2.0.20 and higher), Compose compares unstable parameters using instance equality (`===`) and skips the composable if the same object instances are passed. In versions prior to Kotlin 2.0.20 (or when Strong skipping mode is disabled), Compose always recomposes a composable with unstable parameters when its parent recomposes.

If your app frequently allocates new instances of unstable parameters---or forces
expensive `.equals()` checks on large collections by over-annotating models---you
might observe unnecessary recompositions or comparison overhead.

This document details how Compose determines stability and how you can optimize
it to improve performance and overall user experience.

## Immutable objects

The following snippets demonstrates the general principles behind stability and
recomposition.

The `Contact` class is an immutable data class. This is because all its
parameters are primitives defined with the `val` keyword. Once you create an
instance of `Contact`, you cannot change the value of the object's properties.
If you attempted to do so, you would create a new object.

    data class Contact(val name: String, val number: String)

The `ContactRow` composable has a parameter of type `Contact`.

    @Composable
    fun ContactRow(contact: Contact, modifier: Modifier = Modifier) {
       var selected by remember { mutableStateOf(false) }

       Row(modifier) {
          ContactDetails(contact)
          ToggleButton(selected, onToggled = { selected = !selected })
       }
    }

Consider what happens when the user clicks the toggle button and the
`selected` state changes:

1. Compose evaluates if it should recompose the code inside `ContactRow`.
2. It sees that the only argument for `ContactDetails` is of type `Contact`.
3. Because `Contact` is an immutable data class, Compose is sure that none of the arguments for `ContactDetails` have changed.
4. As such, Compose skips `ContactDetails` and does not recompose it.
5. On the other hand, the arguments for `ToggleButton` have changed, and Compose recomposes that component.

### Mutable objects

While the preceding example uses an immutable object, it is possible to create a
mutable object. Consider the following snippet:

    data class Contact(var name: String, var number: String)

As each parameter of `Contact` is now a `var`, the class is no longer immutable.
If its properties changed, Compose wouldn't become aware. This is because
Compose only tracks changes to Compose [State objects](https://developer.android.com/reference/kotlin/androidx/compose/runtime/MutableState).

Compose considers such a class unstable. With [Strong skipping mode](https://developer.android.com/develop/ui/compose/performance/stability/strongskipping)
(Kotlin 2.0.20+), Compose compares `Contact` using instance equality (`===`):
mutating `contact.name` in place won't trigger recomposition, while passing a
newly allocated `Contact` instance with identical values will still force
`ContactDetails` to recompose (and without Strong skipping mode,
`ContactDetails` recomposes every time `selected` changes).

## Implementation in Compose

It can be helpful, though not crucial, to consider how exactly Compose
determines which functions to skip during recomposition.

When the Compose compiler runs on your code, it marks each function and type
with one of several tags. These tags reflect how Compose handles the function or
type during recomposition.

> [!NOTE]
> **Note:** These tags aren't strictly necessary to understand recomposition and stability as described in the preceding sections of this document. However, they are broadly useful when [debugging](https://developer.android.com/develop/ui/compose/performance/stability/diagnose) stability issues.

### Functions

Compose can mark functions as `skippable` or `restartable`. Note that it may
mark a function as one, both, or neither of these:

- **Skippable** : If the compiler marks a composable as skippable, Compose can skip it during recomposition if all its arguments are equal with their previous values. (With [Strong skipping mode](https://developer.android.com/develop/ui/compose/performance/stability/strongskipping) in Kotlin 2.0.20+, all restartable composables are automatically skippable.)
- **Restartable**: A composable that is restartable serves as a "scope" where recomposition can start. In other words, the function can be a point of entry for where Compose can start re-executing code for recomposition after state changes.

### Types

Compose marks types as either immutable or stable. Each type is one or the
other:

- **Immutable** : Compose marks a type as immutable if the value of its properties can never change and all methods are referentially transparent.
  - Note that all primitive types are marked as immutable. These include `String`, `Int`, and `Float`.
- **Stable**: Indicates a type whose properties can change after construction. If and when those properties change during runtime, Compose becomes aware of those changes.

> [!NOTE]
> **Note:** A composable's parameters don't have to be immutable for Compose to consider it skippable. They can be mutable as long as the Compose runtime is notified of all changes. For most types this would be an impractical contract to uphold. However, Compose provides mutable classes that do uphold this contract for you, such as `MutableState`, `SnapshotStateMap`, and `SnapshotStateList`.

## Debug stability

If your app is recomposing a composable whose parameters have not changed, first
check whether new instances of unstable types are being allocated on every
recomposition (or, if Strong skipping mode is disabled, whether the composable
has parameters with `var` properties or `val` properties of an unstable type).

For detailed information about how to diagnose complex issues with stability in
Compose, see the [Debug stability](https://developer.android.com/develop/ui/compose/performance/stability/diagnose) guide.

## Fix stability issues

For information about how to bring stability to your Compose implementation, see
the [Fix stability issues](https://developer.android.com/develop/ui/compose/performance/stability/fix) guide.

## Summary

Overall, you should note the following points:

- **Parameters** : Compose determines the stability of each parameter of your composables to decide whether to compare them using structural equality (`.equals()`) or instance equality (`===`) during recomposition.
- **Immediate fixes** : If you notice your composable isn't being skipped *and
  it is causing a performance issue* , check whether new instances of unstable parameters are being recreated on each pass or if `var` properties are being used instead of `State`.
- **Compiler reports** : You can use the [compiler reports](https://developer.android.com/develop/ui/compose/performance/stability/diagnose) to determine what stability is being inferred about your classes.
- **Collections** : Compose considers standard collection interfaces (`List`, `Set`, and `Map`) unstable because their underlying implementations may be mutable. With [Strong skipping mode](https://developer.android.com/develop/ui/compose/performance/stability/strongskipping) (enabled by default in Kotlin 2.0.20+), unstable collections still skip recomposition using fast `O(1)` instance equality (`===`) when the collection reference does not change. Avoid converting large collections to [Kotlinx immutable collections](https://developer.android.com/develop/ui/compose/performance/stability/fix#immutable-collections) or annotating collection-holding classes with `@Immutable` or `@Stable` unless structural equality (`O(N)` `.equals()`) is specifically required, as comparing every element on each recomposition can be more expensive than recomposition itself.
- **Other modules** : Compose considers classes from modules where the Compose compiler does not run to be unstable (compared using `===` under Strong skipping mode). If a data source frequently re-instantiates small, flat models from non-Compose modules with identical values, you can configure a stability configuration file or use `@Stable` or `@Immutable` where `.equals()` is cheap.

## Further reading

- **Performance** : For more debugging tips on Compose performance, check out our [best practices guide](http://goo.gle/compose-performance) and [I/O talk](https://www.youtube.com/watch?v=EOQB8PTLkpY).