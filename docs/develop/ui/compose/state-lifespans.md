---
title: https://developer.android.com/develop/ui/compose/state-lifespans
url: https://developer.android.com/develop/ui/compose/state-lifespans
source: md.txt
---

In Jetpack Compose, composable functions often hold state using the `remember`
function. Values that are remembered can be reused across recompositions, as
explained in [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state).

While `remember` serves as a tool to persist values across recompositions, state
often needs to live beyond the lifetime of a composition. This page explains the
difference between the [`remember`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/package-summary#remember(kotlin.Function0)), [`retain`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/retain/package-summary#retain(kotlin.Function0)), [`rememberSaveable`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/saveable/package-summary#rememberSaveable(kotlin.Array,kotlin.Function0)),
and [`rememberSerializable`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/saveable/package-summary#rememberSerializable(kotlin.Array,androidx.savedstate.serialization.SavedStateConfiguration,kotlin.Function0)) APIs, when to choose which API, and what the
best practices are for managing remembered and retained values in Compose.

## Choose the correct lifespan

In Compose, there are several functions you can use to persist state across
compositions and beyond: `remember`, `retain`, `rememberSaveable`, and
`rememberSerializable`. These functions differ in their lifespan and semantics,
and are each suited for storing specific kinds of state. The differences are
outlined in the following table:

|   | `remember` | `retain` | `rememberSaveable`, `rememberSerializable` |
|---|---|---|---|
| Values survive recompositions? | ✅ | ✅ | ✅ |
| Values survive activity recreations? | ❌ | ✅ The same (`===`) instance will always be returned | ✅ An equivalent (`==`) object will be returned, possibly a deserialized copy |
| Values survive process death? | ❌ | ❌ | ✅ |
| Supported data types | All | Must not reference any objects that would be leaked if the activity is destroyed | Must be serializable (either with a custom `Saver` or with `kotlinx.serialization`) |
| Use cases | - Objects that are scoped to the composition - Configuration objects for composables - State that could be recreated without losing UI fidelity | - Caches - Long-lived or "manager" objects | - User input - State that can't be recreated by the app, including text field input, scroll state, toggles, etc. |

### `remember`

`remember` is the most common way to store state in Compose. When `remember` is
called for the first time, the given calculation is executed and is
*remembered* , meaning that it is stored by Compose for future reuse by the
composable. When a composable recomposes, it executes its code again, but any
calls to `remember` return their values from the previous composition instead of
executing the calculation again.

Each instance of a composable function has its own set of remembered values,
referred to as *positional memoization*. When remembered values are memoized for
use across recompositions, they are tied to their position in the composition
hierarchy. If a composable is used in different locations, each instance in the
composition hierarchy has its own set of remembered values.

When a remembered value is no longer used, it is *forgotten* and its record is
discarded. Remembered values are forgotten when they are removed from the
composition hierarchy (Including when a value is removed and re-added to move to
a different location without the use of the `key` composable or
`MovableContent`), or called with different `key` parameters.

Of the choices available, `remember` has the shortest lifespan and forgets
values the earliest of the four memoization functions described in this page.
This makes it best-suited for:

- Creating internal state objects, such as scroll position or animation state
- Avoiding expensive object recreation on each recomposition

However, you should avoid:

- Storing any user input with `remember`, because remembered objects are forgotten across Activity configuration changes and system-initiated process death.

### `rememberSaveable` and `rememberSerializable`

`rememberSaveable` and `rememberSerializable` build on top of `remember`. They
have the longest lifespan of the memoization functions discussed in this guide.
In addition to positionally memoizing objects across recompositions, it can also
*save* values so that they can be restored across activity recreations,
including from configuration changes and process death (when the system kills
your app's process while it is in the background, usually either to free memory
for foreground apps or if the user revokes permissions from your app while it is
running).

`rememberSerializable` works in the same way as `rememberSaveable`, but
automatically supports persisting complex types that are serializable with the
`kotlinx.serialization` library. Choose `rememberSerializable` if your type is
(or can be) marked with `@Serializable`, and `rememberSaveable` in all other
cases.

This makes both `rememberSaveable` and `rememberSerializable` perfect candidates
for storing state associated with user input, including text field entry, scroll
position, toggle states, etc. You should save this state to ensure that the user
never loses their place. In general, you should use `rememberSaveable` or
`rememberSerializable` to memoize any state that your app isn't able to retrieve
from another persistent data source, such as a database.

Note that `rememberSaveable` and `rememberSerializable` save their memoized
values by serializing them into a `Bundle`. This has two consequences:

- Values you memoize must be representable by one or more of the following data types: Primitives (including `Int`, `Long`, `Float`, `Double`), `String`, or arrays of any of these types.
- When a saved value is restored, it will be a new instance that is equal to (`==`), but not the same reference (`===`) that the composition used before.

To store more complicated data types without using `kotlinx.serialization`, you
can implement a custom `Saver` to serialize and deserialize your object into
supported data types. Note that Compose understands common data types like
`State`, `List`, `Map`, `Set`, etc. out-of-the-box, and automatically converts
these into supported types on your behalf. The following is an example of a
`Saver` for a `Size` class. It's implemented by packing all of `Size`'s
properties into a list using `listSaver`.


```kotlin
data class Size(val x: Int, val y: Int) {
    object Saver : androidx.compose.runtime.saveable.Saver<Size, Any> by listSaver(
        save = { listOf(it.x, it.y) },
        restore = { Size(it[0], it[1]) }
    )
}

@Composable
fun rememberSize(x: Int, y: Int) {
    rememberSaveable(x, y, saver = Size.Saver) {
        Size(x, y)
    }
}
```

<br />

### `retain`

The `retain` API exists between `remember` and
`rememberSaveable`/`rememberSerializable` in terms of how long it memoizes its
values. It is named differently because retained values also experience a
different lifecycle than their remembered counterparts.

When a value is *retained* , it is both positionally memoized and saved in a
secondary data structure that has a separate lifespan that is tied to the app's
lifespan. A retained value is able to survive configuration changes without
being serialized, but cannot survive process death. If a value is not used after
the composition hierarchy is recreated, the retained value is *retired* (which
is `retain`'s equivalent of being forgotten).

In exchange for this shorter-than-`rememberSaveable` lifecycle, retain is able
to persist values that can't be serialized, like lambda expressions, flows, and
large objects like bitmaps. For example, you can use `retain` to manage a media
player (such as ExoPlayer) to prevent interruptions to media playback during
a configuration change.


```kotlin
@Composable
fun MediaPlayer() {
    // Use the application context to avoid a memory leak
    val applicationContext = LocalContext.current.applicationContext
    val exoPlayer = retain { ExoPlayer.Builder(applicationContext).apply { /* ... */ }.build() }
    // ...
}
```

<br />

> [!CAUTION]
> **Caution:** `retain` shouldn't be used with objects that have a lifespan that is shorter than the lifespan given by retain, because this can cause memory leaks. This also applies to the key inputs of `retain`, which are referenced for as long as the value is retained.
>
>
> Avoid retaining objects that are created and managed outside of your control,
> including `Activity`, `View`, `Fragment`,
> `ViewModel`, `Context`, `Lifecycle`,
> and any object that references one of these types. Generally speaking, if you
> wouldn't store an object in a `ViewModel`, you shouldn't retain it
> either.
>
>
> To mark a class in your code as a type that shouldn't be retained, you can
> annotate it with `@DoNotRetain`.

> [!NOTE]
> **Note:** The `retain` API is available in the `androidx.compose.runtime:runtime-retain` artifact starting in Compose 1.10. Support for retaining values across configuration changes is provided in `androidx.compose.ui:ui:1.10.0`.
>
>
> We are also working on adding retain support to
> `androidx.navigation` and
> `androidx.navigation3`, which will be available in future releases
> of the libraries.

#### `retain` versus `ViewModel`

At their cores, both `retain` and `ViewModel` offer similar functionality in
their most commonly used ability to persist object instances across
configuration changes. The choice to reach for `retain` or `ViewModel` lies in
the type of value you're persisting, how it should be scoped, and whether you
need additional functionality.

`ViewModel`s are objects that typically encapsulate the communication between
your app's UI and data layers. They allow you to move logic out of your
composable functions, which improves testability. `ViewModel`s are managed as
singletons within a `ViewModelStore` and have a different lifespan from retained
values. While a `ViewModel` will remain active until its `ViewModelStore` is
destroyed, retained values are retired when the content is permanently removed
from the composition (for a configuration change, as an example, this means that
a retained value is retired if the UI hierarchy is recreated and the retained
value wasn't consumed after the composition is recreated).

`ViewModel` also includes out-of-the-box integrations for dependency injection
with Dagger and Hilt, integration with `SavedState`, and built-in coroutine
support for launching background tasks. This makes `ViewModel` an ideal place to
launch background tasks and network requests, interact with other data sources
in your project, and optionally capture and persist mission-critical UI state
that should be both retained across configuration changes in the `ViewModel` and
survive process death.

`retain` is best suited for objects that are scoped to specific composable
instances and don't require reuse or sharing between sibling composables. Where
`ViewModel` acts as a good place to store UI state and perform background tasks,
`retain` is a good candidate for storing objects for UI plumbing like caches,
impression tracking and analytics, dependencies on `AndroidView`s, and other
objects that interact with the Android OS or manage third party libraries like
payment processors or advertising.

For advanced users designing custom app architecture patterns outside of the
Modern Android app architecture recommendations: `retain` can also be used to
build an in-house "`ViewModel`-like" API. Although support for coroutines and
saved-state is not offered out-of-the-box, `retain` can serve as the building
block for the lifecycle of such `ViewModel`-look-alikes with these features
built on top. The specifics of how to design such a component are outside the
scope of this guide.

|   | `retain` | `ViewModel` |
|---|---|---|
| **Scoping** | No shared values; each value is retained at and associated with a specific point in the composition hierarchy. Retaining the same type in a different location always acts on a new instance. | `ViewModel`s are singletons within a `ViewModelStore` |
| **Destruction** | When permanently leaving the composition hierarchy | When the `ViewModelStore` is cleared or destroyed |
| **Additional functionality** | Can receive callbacks when the object is in the composition hierarchy or not | Built-in `coroutineScope`, support for `SavedStateHandle`, can be injected using Hilt |
| **Owned by** | `RetainedValuesStore` | `ViewModelStore` |
| **Use cases** | - Persisting UI-specific values local to individual composable instances - Impression tracking, possibly through `RetainedEffect` - Building block for defining a custom "ViewModel-like" architecture component | - Extracting interactions between UI and data layers into a separate class, both for code organization and testing - Transforming `Flow`s into `State` objects and calling suspend functions that shouldn't be interrupted by configuration changes - Sharing states over large UI areas, like entire screens - Interoperability with `View` |

### Combine `retain` and `rememberSaveable` or `rememberSerializable`

Sometimes, an object needs to have a hybrid lifespan of both `retained` and
`rememberSaveable` or `rememberSerializable`. This may be an indicator that your
object should be a `ViewModel`, which can support saved state as described in
the [Saved State module for ViewModel guide](https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-savedstate).

it is possible to use `retain` and `rememberSaveable` or `rememberSerializable`
simultaneously. Correctly combining both lifecycles adds significant complexity.
We recommend employing this pattern as part of more advanced and custom
architecture patterns, and only when all of the following are true:

- You are defining an object comprised of a mix of values that must be retained or saved (e.g. an object that tracks a user input and an in-memory cache that can't be written to disk)
- Your state is scoped to a composable and isn't suitable for the singleton scoping or lifespan of `ViewModel`

When all of these are the case, we recommend splitting your class into three
parts: The saved data, the retained data, and a "mediator" object that has no
state of its own and delegates onto the retained and saved objects to update
state accordingly. This pattern takes the following shape:


```kotlin
@Composable
fun rememberAndRetain(): CombinedRememberRetained {
    val saveData = rememberSerializable(serializer = serializer<ExtractedSaveData>()) {
        ExtractedSaveData()
    }
    val retainData = retain { ExtractedRetainData() }
    return remember(saveData, retainData) {
        CombinedRememberRetained(saveData, retainData)
    }
}

@Serializable
data class ExtractedSaveData(
    // All values that should persist process death should be managed by this class.
    var savedData: AnotherSerializableType = defaultValue()
)

class ExtractedRetainData {
    // All values that should be retained should appear in this class.
    // It's possible to manage a CoroutineScope using RetainObserver.
    // See the full sample for details.
    var retainedData = Any()
}

class CombinedRememberRetained(
    private val saveData: ExtractedSaveData,
    private val retainData: ExtractedRetainData,
) {
    fun doAction() {
        // Manipulate the retained and saved state as needed.
    }
}
```

<br />

By separating the state by lifespan, the separation of responsibilities and
storage becomes very explicit. It is intentional that save data cannot be
manipulated by retain data, as this prevents a scenario where a save data update
is attempted when the `savedInstanceState` bundle has already been captured and
cannot be updated. It also allows for testing recreation scenarios by testing
your constructors without calling into Compose or simulating an Activity
recreation.

See the full sample ([`RetainAndSaveSample.kt`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/runtime/runtime-retain/samples/src/main/kotlin/androidx/compose/runtime/retain/samples/RetainAndSaveSample.kt)) for a complete example of
how this pattern may be implemented.

> [!NOTE]
> **Note:** Don't `retain` an object that was created by `remember`, `rememberSaveable`, or `rememberSerializable`. Retaining and remembering the same object is an antipattern and violates two broader recommendations:
>
> - Don't retain an object that has a shorter lifespan from retain
> - Don't remember an object twice
>
>
> Retaining an object that has already been remembered does not properly retain
> and save the object, can cause the object to receive duplicate callbacks, and
> leads to unexpected bugs.

## Positional memoization and adaptive layouts

Android applications can support many form factors including phones, foldables,
tablets, and desktops. Applications frequently need to transition between these
form factors by using adaptive layouts. For example, an app running on a tablet
may be able to show a two-column list-detail view, but may navigate between a
list and detail page when presented on a smaller phone screen.

Because remembered and retained values are memoized positionally, they are only
reused if they appear in the same point in the composition hierarchy. As your
layouts adapt to different form factors, they may alter the structure of your
composition hierarchy and lead to forgotten values.

For out-of-the-box components like `ListDetailPaneScaffold` and `NavDisplay`
(from Jetpack Navigation 3), this is not an issue and your state will persist
throughout layout changes. For custom components that adapt to form factors,
ensure that state is unaffected by layout changes by doing one of the following:

- Ensure that stateful composables are always called in the same place in the composition hierarchy. Implement adaptive layouts by altering the layout logic instead of relocating objects in the composition hierarchy.
- Use `MovableContent` to relocate stateful composables gracefully. Instances of `MovableContent` are able to move remembered and retained values from their old to new locations.

## Remember factory functions

Although Compose UIs are made up of composable functions, many objects go into
the creation and organization of a composition. The most common example of this
is complex composable objects that define their own state, like `LazyList`,
which accepts a `LazyListState`.

When defining Compose-focused objects, we recommend creating a `remember`
function to define the intended remembering behavior, including both lifespan
and key inputs. This allows consumers of your state to confidently create
instances in the composition hierarchy that will survive and be invalidated as
expected. When defining a composable factory function, follow these guidelines:

- Prefix the function name with `remember`. Optionally, if the function implementation depends on the object being `retained` and the API will never evolve to rely on a different variation of `remember`, use the `retain` prefix instead.
- Use `rememberSaveable` or `rememberSerializable` if state persistence is chosen and it's possible to write a correct `Saver` implementation.
- Avoid side effects or initializing values based on `CompositionLocal`s that might not be relevant to the usage. Remember, the place your state is created might not be where it is consumed.


```kotlin
@Composable
fun rememberImageState(
    imageUri: String,
    initialZoom: Float = 1f,
    initialPanX: Int = 0,
    initialPanY: Int = 0
): ImageState {
    return rememberSaveable(imageUri, saver = ImageState.Saver) {
        ImageState(
            imageUri, initialZoom, initialPanX, initialPanY
        )
    }
}

data class ImageState(
    val imageUri: String,
    val zoom: Float,
    val panX: Int,
    val panY: Int
) {
    object Saver : androidx.compose.runtime.saveable.Saver<ImageState, Any> by listSaver(
        save = { listOf(it.imageUri, it.zoom, it.panX, it.panY) },
        restore = { ImageState(it[0] as String, it[1] as Float, it[2] as Int, it[3] as Int) }
    )
}
```

<br />

> [!NOTE]
> **Note:** We recommend defining `remember` factory functions **in addition** to standard constructors and non-composable factory functions for a given type.
>
>
> Allowing instances to be created outside of composition has numerous benefits
> for consumers of your class, including testing, more flexibility in app
> architecture, and customization of the default behavior.
>
>
> Verify that consumers of your state work correctly regardless of where the
> object originates.