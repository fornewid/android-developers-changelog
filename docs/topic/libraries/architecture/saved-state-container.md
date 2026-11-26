---
title: https://developer.android.com/topic/libraries/architecture/saved-state-container
url: https://developer.android.com/topic/libraries/architecture/saved-state-container
source: md.txt
---

# SavedStateContainer
Part of [Android Jetpack](https://developer.android.com/jetpack).

[`SavedStateContainer`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateContainer.md.txt) is a thread-safe container that
manages [`SavedStateValue<T>`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateValue.md.txt) instances to coordinate state
saving and restoration across hierarchical and key-value components.

In AndroidX, `SavedStateContainer` serves as the common backing container for
[`SavedStateRegistry`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateRegistry.md.txt),
[`SavedStateHandle`](https://developer.android.com/reference/kotlin/androidx/lifecycle/SavedStateHandle.md.txt), and Compose's
[`SaveableStateRegistry`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/saveable/SaveableStateRegistry.md.txt). Because containers can be
nested inside one another using string keys, you can isolate saved state for
child state holders, custom components, and headless
[`transform`](https://developer.android.com/topic/libraries/architecture/appstate/transform.md.txt) compositions without key collisions.

> [!NOTE]
> **Note:** `SavedStateContainer` and its integrations require `androidx.savedstate:savedstate:1.6.0-alpha05` or higher and `androidx.lifecycle:lifecycle-viewmodel-savedstate:2.12.0-alpha05` or higher.

## Manage hierarchical state with `SavedStateContainer`

As an app or screen grows in complexity, multiple child state holders, custom
components, or reactive transformations often share a single saved-state owner,
such as a `ViewModel` or `Activity`. Storing all of their state in a single
flat map of string keys forces independent components to coordinate key names or
manually prefix keys to avoid overwriting each other's state.

`SavedStateContainer` solves this by organizing saved state into a hierarchy of
isolated containers that can be nested, saved, and restored as a single unit:

- **Isolate state with [`getOrCreateContainer(key)`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateContainer.md.txt#getOrCreateContainer(kotlin.String))** : Retrieves an existing child `SavedStateContainer` associated with `key`, or creates and registers a new child container if none exists. You can pass this child container to a feature component, a Compose [`SaveableStateRegistry`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/saveable/SaveableStateRegistry.md.txt), or [`TransformScope.launchTransform`](https://developer.android.com/reference/kotlin/androidx/appstate/transform/TransformScope.md.txt#launchTransform(kotlin.Any,kotlin.Function1)) so each component gets its own isolated namespace without risking key collisions.
- **Snapshot the hierarchy with [`saveState`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateContainer.md.txt#saveState())** : Captures the current state of every entry and nested child container registered in the container and returns a single [`SavedState`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedState.md.txt).
- **Restore state with [`restoreState(savedState)`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateContainer.md.txt#restoreState(androidx.savedstate.SavedState))** : Restores a previously saved `SavedState` across the container and its nested children.

### Deferred restoration of unconsumed state

In many architectures, child components or transformations are initialized
lazily---often after the parent owner has already restored its saved state.
`SavedStateContainer` handles both eager and lazy initialization automatically:

- **Registered before `restoreState`** : If a child container or value is registered before `container.restoreState(savedState)` is called, the container immediately passes the restored state to each registered entry during `restoreState`.
- **Registered after `restoreState`** : If `container.restoreState(savedState)` runs first, the container holds the incoming state for unclaimed keys in memory. When you later call `getOrCreateContainer(key)` or register a `SavedStateValue` for `key`, the container consumes the pending state for that key and restores the entry immediately. Any unconsumed state that is never claimed is still preserved on subsequent calls to `saveState`.

### Store custom state with `SavedStateValue<T>`

Most app code interacts with `SavedStateContainer` by creating nested containers
with `getOrCreateContainer(key)` and passing them to Jetpack APIs. When you're
building a custom stateful primitive or state holder that needs to plug directly
into a `SavedStateContainer`, you can implement
[`SavedStateValue<T>`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateValue.md.txt):

```kotlin
package androidx.savedstate

import androidx.savedstate.SavedStateRegistry.SavedStateProvider
import androidx.savedstate.SavedStateRegistry.SavedStateRestorer

public interface SavedStateValue<T> : SavedStateProvider, SavedStateRestorer {
    public val value: T
}
```

`SavedStateValue<T>` combines an in-memory value with automatic save and restore
callbacks:

- **[`value: T`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateValue.md.txt#value())**: Exposes the current in-memory value held by the component.
- **[`SavedStateRegistry.SavedStateProvider`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateRegistry.SavedStateProvider.md.txt)** : Defines [`saveState`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateRegistry.SavedStateProvider.md.txt#saveState()), which returns a [`SavedState`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedState.md.txt) snapshot of the component's current state when the container saves its state.
- **[`SavedStateRegistry.SavedStateRestorer`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateRegistry.SavedStateRestorer.md.txt)** : Defines [`restoreState(savedState)`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateRegistry.SavedStateRestorer.md.txt#restoreState(androidx.savedstate.SavedState)), which receives the previously saved `SavedState`, or `null` if no state was saved for its key, when the container restores state---or immediately when the entry is registered if the container has already restored its state.

You can register and retrieve custom `SavedStateValue` instances in a container
using [`getOrPutSavedStateValue(key, defaultValue)`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateContainer.md.txt#getOrPutSavedStateValue(kotlin.String,kotlin.Function0)),
[`putSavedStateValue(key, savedStateValue)`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateContainer.md.txt#putSavedStateValue(kotlin.String,androidx.savedstate.SavedStateValue)),
[`getSavedStateValue(key)`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateContainer.md.txt#getSavedStateValue(kotlin.String)), and
[`removeSavedStateValue(key)`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateContainer.md.txt#removeSavedStateValue(kotlin.String)).

The following example implements a custom `CounterSavedStateValue` and shows how
a parent container and a nested child container save and lazily restore their
state:

```kotlin
import androidx.savedstate.SavedState
import androidx.savedstate.SavedStateContainer
import androidx.savedstate.SavedStateValue
import androidx.savedstate.read
import androidx.savedstate.savedState

class CounterSavedStateValue(
    initialCount: Int = 0,
) : SavedStateValue<Int> {

    override var value: Int = initialCount

    override fun saveState(): SavedState = savedState {
        putInt(COUNT_KEY, value)
    }

    override fun restoreState(savedState: SavedState?) {
        if (savedState != null) {
            value = savedState.read { getIntOrNull(COUNT_KEY) ?: 0 }
        }
    }

    private companion object {
        const val COUNT_KEY = "count"
    }
}

// 1. Populate a parent container and a nested child container
val parentContainer = SavedStateContainer()
val rootCounter = parentContainer.getOrPutSavedStateValue("rootCounter") {
    CounterSavedStateValue(initialCount = 3)
}

val childContainer = parentContainer.getOrCreateContainer("featureA")
val childCounter = childContainer.getOrPutSavedStateValue("stepCounter") {
    CounterSavedStateValue(initialCount = 10)
}

// 2. Save the entire container hierarchy into a single SavedState
val snapshot: SavedState = parentContainer.saveState()

// 3. Restore into a new parent container
val restoredParent = SavedStateContainer()
restoredParent.restoreState(snapshot)

// Entries and child containers created after restoreState automatically
// receive their saved state
val restoredRootCounter = restoredParent.getOrPutSavedStateValue("rootCounter") {
    CounterSavedStateValue()
}
val restoredChild = restoredParent.getOrCreateContainer("featureA")
val restoredChildCounter = restoredChild.getOrPutSavedStateValue("stepCounter") {
    CounterSavedStateValue()
}

// restoredRootCounter.value == 3
// restoredChildCounter.value == 10
```

## Integrations with Jetpack saved state APIs

`SavedStateContainer` integrates directly with
[`SavedStateRegistry`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateRegistry.md.txt),
[`SavedStateHandle`](https://developer.android.com/reference/kotlin/androidx/lifecycle/SavedStateHandle.md.txt), and
[`SaveableStateRegistry`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/saveable/SaveableStateRegistry.md.txt) so you can share and nest
saved state across UI components, ViewModels, and Compose runtime registries.

### Share and nest saved states with `SavedStateRegistry`

In `androidx.savedstate`, [`SavedStateRegistry`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateRegistry.md.txt) is now
backed by a `SavedStateContainer` and exposes two methods for working with
containers directly:

- **[`asContainer`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateRegistry.md.txt#asContainer())** : Returns the underlying `SavedStateContainer` that manages the registry.
- **[`getOrCreateContainer(key)`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateRegistry.md.txt#getOrCreateContainer(kotlin.String))** : Retrieves an existing nested `SavedStateContainer` associated with `key`, or creates and registers a new child container inside the registry.

In addition, `SavedStateRegistry` supports push-based restoration through
[`SavedStateRegistry.SavedStateRestorer`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateRegistry.SavedStateRestorer.md.txt). When a
[`SavedStateProvider`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateRegistry.SavedStateProvider.md.txt) passed to
[`registerSavedStateProvider(key, provider)`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateRegistry.md.txt#registerSavedStateProvider(kotlin.String,androidx.savedstate.SavedStateRegistry.SavedStateProvider)) also
implements `SavedStateRestorer`, the registry automatically invokes
`restoreState(savedState)` during the state restoration phase---or immediately
upon registration if the registry has already been restored. You don't need to
manually call [`consumeRestoredStateForKey(key)`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateRegistry.md.txt#consumeRestoredStateForKey(kotlin.String)):

```kotlin
import androidx.savedstate.SavedState
import androidx.savedstate.SavedStateRegistry
import androidx.savedstate.SavedStateRegistryOwner
import androidx.savedstate.read
import androidx.savedstate.savedState

class SearchHistoryTracker(
    registryOwner: SavedStateRegistryOwner,
) : SavedStateRegistry.SavedStateProvider, SavedStateRegistry.SavedStateRestorer {

    var recentQueries: List<String> = emptyList()
        private set

    init {
        // Because SearchHistoryTracker implements SavedStateRestorer,
        // restoreState() is called automatically without consumeRestoredStateForKey().
        registryOwner.savedStateRegistry.registerSavedStateProvider(
            key = PROVIDER_KEY,
            provider = this,
        )
    }

    override fun saveState(): SavedState = savedState {
        putStringList(QUERIES_KEY, recentQueries)
    }

    override fun restoreState(savedState: SavedState?) {
        recentQueries = savedState?.read {
            getStringListOrNull(QUERIES_KEY)
        } ?: emptyList()
    }

    private companion object {
        const val PROVIDER_KEY = "search_history_tracker"
        const val QUERIES_KEY = "recent_queries"
    }
}
```

### Scope ViewModel state with `SavedStateHandle`

In `androidx.lifecycle`, [`SavedStateHandle`](https://developer.android.com/reference/kotlin/androidx/lifecycle/SavedStateHandle.md.txt) is backed by a
`SavedStateContainer`. Every entry stored in a `SavedStateHandle`---including
regular values accessed with [`get`](https://developer.android.com/reference/kotlin/androidx/lifecycle/SavedStateHandle.md.txt#get(kotlin.String)) and [`set`](https://developer.android.com/reference/kotlin/androidx/lifecycle/SavedStateHandle.md.txt#set(kotlin.String,kotlin.Any)),
[`StateFlow`](https://developer.android.com/reference/kotlin/androidx/lifecycle/SavedStateHandle.md.txt#getStateFlow(kotlin.String,kotlin.Any)) and
[`MutableStateFlow`](https://developer.android.com/reference/kotlin/androidx/lifecycle/SavedStateHandle.md.txt#getMutableStateFlow(kotlin.String,kotlin.Any)) instances, `LiveData`
instances, and [`SavedStateProvider`](https://developer.android.com/reference/kotlin/androidx/lifecycle/SavedStateHandle.md.txt#setSavedStateProvider(kotlin.String,androidx.savedstate.SavedStateRegistry.SavedStateProvider)) callbacks---is stored
as a `SavedStateValue` in the underlying container.

`SavedStateHandle` provides three methods to access or nest containers and
child handles:

- **[`asContainer`](https://developer.android.com/reference/kotlin/androidx/lifecycle/SavedStateHandle.md.txt#asContainer())** : Returns the underlying `SavedStateContainer` managing the `SavedStateHandle`.
- **[`getOrCreateContainer(key)`](https://developer.android.com/reference/kotlin/androidx/lifecycle/SavedStateHandle.md.txt#getOrCreateContainer(kotlin.String))** : Retrieves an existing nested `SavedStateContainer` for `key`, or creates and registers a new child `SavedStateContainer`.
- **[`getOrCreateSavedStateHandle(key)`](https://developer.android.com/reference/kotlin/androidx/lifecycle/SavedStateHandle.md.txt#getOrCreateSavedStateHandle(kotlin.String))** : Retrieves an existing nested `SavedStateHandle` for `key`, or creates and registers a new child `SavedStateHandle` backed by a child container.

Use `getOrCreateSavedStateHandle(key)` when a `ViewModel` delegates state
management to reusable child state holders that each read and write keys in
their own `SavedStateHandle`:

```kotlin
import androidx.lifecycle.SavedStateHandle
import androidx.lifecycle.ViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow

class FilterStateHolder(private val savedStateHandle: SavedStateHandle) {
    // Uses the key "selectedCategory" inside its own scoped SavedStateHandle
    private val _selectedCategory =
        savedStateHandle.getMutableStateFlow("selectedCategory", "All")
    val selectedCategory: StateFlow<String> = _selectedCategory.asStateFlow()

    fun selectCategory(category: String) {
        _selectedCategory.value = category
    }
}

class CatalogViewModel(savedStateHandle: SavedStateHandle) : ViewModel() {
    // Each FilterStateHolder gets an isolated child SavedStateHandle, so both
    // can safely use the "selectedCategory" key without colliding.
    val primaryFilter = FilterStateHolder(
        savedStateHandle.getOrCreateSavedStateHandle("primaryFilter")
    )
    val secondaryFilter = FilterStateHolder(
        savedStateHandle.getOrCreateSavedStateHandle("secondaryFilter")
    )
}
```

### Persist Compose state with `SaveableStateRegistry`

In `androidx.compose.runtime.saveable`,
[`SaveableStateRegistry`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/saveable/SaveableStateRegistry.md.txt) provides a factory overload
that accepts a `SavedStateContainer`:

```kotlin
package androidx.compose.runtime.saveable

import androidx.savedstate.SavedStateContainer

public fun SaveableStateRegistry(
    container: SavedStateContainer,
    canBeSaved: (Any) -> Boolean,
): SaveableStateRegistry
```

When created with a `SavedStateContainer`, `SaveableStateRegistry` saves its
registered value providers into `container` whenever `container.saveState` is
called and restores them whenever `container.restoreState(savedState)` is
called. This allows [`rememberSaveable`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/saveable/rememberSaveable.composable.md.txt#rememberSaveable(kotlin.Array,kotlin.Function0)) and
[`rememberSerializable`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/saveable/rememberSerializable.composable.md.txt) to persist and restore state
even in compositions that run outside a traditional Compose UI hierarchy.

## Use `SavedStateContainer` with Transform

The [Transform](https://developer.android.com/topic/libraries/architecture/appstate/transform.md.txt) library in `androidx.appstate.transform` runs a
headless `@Composable` block outside the UI to combine and transform reactive
inputs into a Compose [`State<T>`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/State.md.txt). By passing a
`SavedStateContainer` to [`TransformScope.launchTransform`](https://developer.android.com/reference/kotlin/androidx/appstate/transform/TransformScope.md.txt#launchTransform(kotlin.Any,kotlin.Function1)),
you can use `@Composable` `remember*` state-saving primitives---such as
[`rememberSaveable`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/saveable/rememberSaveable.composable.md.txt#rememberSaveable(kotlin.Array,kotlin.Function0)) and
[`rememberSerializable`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/saveable/rememberSerializable.composable.md.txt)---directly inside your
transformation block.

### Save state in `launchTransform`

`TransformScope.launchTransform` accepts a `container: SavedStateContainer`
parameter:

```kotlin
package androidx.appstate.transform

import androidx.compose.runtime.Composable
import androidx.savedstate.SavedStateContainer

public interface TransformScope {
    public fun <T> launchTransform(
        container: SavedStateContainer = SavedStateContainer(),
        onUpdate: @Composable (T?) -> T,
    ): DisposableState<T>
}
```

> [!NOTE]
> **Note:** Passing a `SavedStateContainer` to `launchTransform` requires `androidx.appstate.transform:transform:1.0.0-alpha03` or higher.

Providing a `SavedStateContainer` to `launchTransform` connects the
transformation's `@Composable` block to that container so calls to
`rememberSaveable` and `rememberSerializable` save their values when the
container saves state and restore them when the container restores state.

> [!IMPORTANT]
> **Important:** By default, `launchTransform` uses a new, unattached `SavedStateContainer`. An unattached container holds state only in memory for that container instance and doesn't persist state across configuration changes or system-initiated process death. For `rememberSaveable` and `rememberSerializable` to survive recreation and process death, pass a `SavedStateContainer` connected to a saved-state owner---such as `savedStateHandle.getOrCreateContainer(key)` or `savedStateRegistry.getOrCreateContainer(key)`.

### Persist `launchTransform` state with `SavedStateHandle`

Inside a [`ViewModel`](https://developer.android.com/topic/libraries/architecture/viewmodel.md.txt), pass a child container from
`savedStateHandle.getOrCreateContainer(key)` to
`transformScope.launchTransform`. Any state created with `rememberSaveable` or
`rememberSerializable` inside the transformation block is automatically saved
when the host activity stops and restored if the `ViewModel` is recreated after
process death:

```kotlin
import androidx.appstate.transform.DisposableState
import androidx.appstate.transform.TransformScope
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.saveable.rememberSerializable
import androidx.compose.runtime.setValue
import androidx.lifecycle.SavedStateHandle
import androidx.lifecycle.ViewModel
import kotlinx.serialization.Serializable

@Serializable
data class SortConfig(
    val field: String = "date",
    val ascending: Boolean = false,
)

data class FeedUiState(
    val items: List<String> = emptyList(),
    val sortConfig: SortConfig = SortConfig(),
    val expandedSectionId: String? = null,
)

class FeedViewModel(
    savedStateHandle: SavedStateHandle,
    transformScope: TransformScope,
    private val repository: FeedRepository,
) : ViewModel() {

    val uiState: DisposableState<FeedUiState> = transformScope.launchTransform(
        container = savedStateHandle.getOrCreateContainer("feedTransform"),
    ) {
        // Persisted across process death using KotlinX Serialization
        var sortConfig by rememberSerializable {
            mutableStateOf(SortConfig())
        }
        // Persisted across process death using standard Bundle/Saver support
        var expandedSectionId by rememberSaveable {
            mutableStateOf<String?>(null)
        }

        val items by repository
            .getFeedItems(sortConfig.field, sortConfig.ascending)
            .collectAsState(initial = emptyList())

        FeedUiState(
            items = items,
            sortConfig = sortConfig,
            expandedSectionId = expandedSectionId,
        )
    }
}
```

### Isolate multiple transforms with nested containers

When a `ViewModel` or state holder launches more than one transformation on a
`TransformScope`---or combines transformations with `SavedStateHandle` properties
and child state holders---give each `launchTransform` call its own nested
container using `getOrCreateContainer(key)` with a distinct key.

#### Why nested containers matter

If two `launchTransform` blocks share the same `SavedStateContainer` instance---
for example, if both receive `savedStateHandle.asContainer`---the `remember*`
state saved by one transformation can collide with or overwrite the state saved
by the other.

Calling `savedStateHandle.getOrCreateContainer(key)` creates a dedicated child
`SavedStateContainer` nested under `key` in the parent `SavedStateHandle`:

- Each `launchTransform` call receives its own isolated `SavedStateContainer` for its `rememberSaveable` and `rememberSerializable` values.
- Top-level `SavedStateHandle` entries, such as `getMutableStateFlow` or `SavedStateHandle.saveable`, child `SavedStateHandle` instances created with `getOrCreateSavedStateHandle`, and nested `SavedStateContainer` instances created with `getOrCreateContainer` all coexist cleanly in the same hierarchical `SavedStateContainer` tree.
- When `SavedStateHandle` saves or restores state, it traverses the entire tree automatically.

The following example shows a `ViewModel` that launches three independent
transformations in a shared `TransformScope`, isolating each one with its own
nested container from `SavedStateHandle`:

```kotlin
import androidx.appstate.transform.DisposableState
import androidx.appstate.transform.TransformScope
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.lifecycle.SavedStateHandle
import androidx.lifecycle.ViewModel

class WorkspaceViewModel(
    savedStateHandle: SavedStateHandle,
    transformScope: TransformScope,
    private val searchRepository: SearchRepository,
) : ViewModel() {

    // 1. First transformation isolated in the "searchTransform" child container
    val searchState: DisposableState<List<String>> = transformScope.launchTransform(
        container = savedStateHandle.getOrCreateContainer("searchTransform"),
    ) {
        var lastSubmittedQuery by rememberSaveable { mutableStateOf("") }
        val results by searchRepository
            .search(lastSubmittedQuery)
            .collectAsState(initial = emptyList())
        results
    }

    // 2. Second transformation isolated in the "draftTransform" child container
    val draftPageCount: DisposableState<Int> = transformScope.launchTransform(
        container = savedStateHandle.getOrCreateContainer("draftTransform"),
    ) {
        var pageCount by rememberSaveable { mutableIntStateOf(1) }
        pageCount
    }

    // 3. Third transformation isolated in the "bannerTransform" child container
    val bannerDismissed: DisposableState<Boolean> = transformScope.launchTransform(
        container = savedStateHandle.getOrCreateContainer("bannerTransform"),
    ) {
        var isDismissed by rememberSaveable { mutableStateOf(false) }
        isDismissed
    }
}
```

## Additional resources

To learn more about saving state and transforming Compose `State` across your
app, see the following guides:

- [Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states.md.txt)
- [Saved State module for ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-savedstate.md.txt)
- [Transform](https://developer.android.com/topic/libraries/architecture/appstate/transform.md.txt)
- [Use Compose State outside the UI](https://developer.android.com/topic/libraries/architecture/appstate/state-beyond-ui.md.txt)