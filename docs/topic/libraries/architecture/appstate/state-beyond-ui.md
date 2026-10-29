---
title: https://developer.android.com/topic/libraries/architecture/appstate/state-beyond-ui
url: https://developer.android.com/topic/libraries/architecture/appstate/state-beyond-ui
source: md.txt
---

> [!WARNING]
> **Experimental:** AppState is in alpha. Its APIs are subject to change. File bugs and feedback using the [Transform issue tracker](https://issuetracker.google.com/issues/new?component=2302904&template=2430547) or [StateStore issue tracker](https://issuetracker.google.com/issues/new?component=2302751&template=2430521).

Jetpack Compose [`State<T>`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/State) and
[`MutableState<T>`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/MutableState) are general-purpose value holders backed by
the Compose snapshot system. Although they're most commonly used to drive UI
recomposition, the snapshot system itself isn't tied to UI rendering.

With the [AppState](https://developer.android.com/topic/libraries/architecture/appstate) libraries---[Transform](https://developer.android.com/topic/libraries/architecture/appstate/transform)
and [StateStore](https://developer.android.com/topic/libraries/architecture/appstate/statestore)---you can hold, derive, observe, and persist
Compose `State` across ViewModels, managers, repositories, and background
services.

## Why use Compose State beyond the UI?

When you read Compose `State` inside a state-observing block---such as a UI
composable, [`transform`](https://developer.android.com/topic/libraries/architecture/appstate/transform), or
[`derivedStateOf`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/package-summary#derivedStateOf(kotlin.Function0))---the Compose runtime provides two key
benefits across any layer of your architecture:

- **Automatic and dynamic dependency tracking** : Reading a state's `.value` (or using `by` property delegation) automatically registers that state as a dependency of the block. Because tracking is *dynamic* , dependencies are determined at runtime by which code paths execute. If a conditional branch isn't taken (for example, after an `if` check or early `return`), states inside that branch aren't read and changes to them don't trigger unnecessary recomputations.
- **Consistency and granularity** : You can declare separate, fine-grained `MutableState` properties and wrap multi-property writes in [`Snapshot.withMutableSnapshot`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/snapshots/Snapshot.Companion#withMutableSnapshot(kotlin.Function0)). Intermediate updates are isolated to the mutable snapshot and applied atomically when the block completes, so observers reading inside a snapshot never see inconsistent intermediate state and only recompute when the specific properties they read change. Unlike `StateFlow`, you don't have to choose between a single monolithic `StateFlow<UiState>` (which invalidates every collector when any field changes) and separate `StateFlow` properties (which can't update together in a single atomic transaction).

## Choose the right state API across your architecture

Choose how to hold and persist Compose `State` based on how long a piece of
state should live and which components need to access it:

| State category | Lifetime and scope | Examples | Recommended Compose `State` APIs |
|---|---|---|---|
| **Live state** | Always stored in memory; queried fresh on startup and not persisted across process death. | Network connection status, Bluetooth connection status, temporary UI state such as item selection. | - [`mutableStateOf`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/package-summary#mutableStateOf(kotlin.Any,androidx.compose.runtime.SnapshotMutationPolicy)) in a [`ViewModel`](https://developer.android.com/topic/libraries/architecture/viewmodel) or DI-scoped `@Singleton` manager - [`transform`](https://developer.android.com/topic/libraries/architecture/appstate/transform) to derive state - [`listener`](https://developer.android.com/topic/libraries/architecture/appstate/transform#listener) to observe state |
| **Transient UI state** | Survives configuration changes and system-initiated process death, not stored indefinitely; scoped to a single screen or activity. | Expanded or collapsed UI elements, scroll position, screen search query or filter toggles. | - [`rememberSaveable`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/saveable/rememberSaveable.composable#rememberSaveable(kotlin.Array,kotlin.Function0)) and [`rememberSerializable`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/saveable/rememberSerializable.composable) in composables - [`SavedStateHandle.saveable`](https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-savedstate#savedstate-compose-state) in a `ViewModel` |
| **Transient session state** | Survives background process death, not stored indefinitely; shared across activities, services, or widgets. | Active focus timer, multi-step checkout cart, or in-progress form draft. | - [`StateStore`](https://developer.android.com/topic/libraries/architecture/appstate/statestore) encapsulated in a manager or repository - Keys implementing [`PersistToDataStore`](https://developer.android.com/topic/libraries/architecture/appstate/statestore#datastore) and synced using `syncToDataStore` |
| **Permanent state** | Kept on disk indefinitely. | User preferences and settings ([DataStore](https://developer.android.com/topic/libraries/architecture/datastore)), structured app data and media libraries ([Room](https://developer.android.com/training/data-storage/room)). | DataStore or Room flows collected inside `transform` using [`collectAsState`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/collectAsState.composable#(kotlinx.coroutines.flow.Flow).collectAsState(kotlin.Any,kotlin.coroutines.CoroutineContext,androidx.compose.runtime.SnapshotMutationPolicy)) |

> [!NOTE]
> **Note:** Bridging streams and asynchronous APIs into `State` isn't limited to a single category. Depending on the input type and where your Composition runs, you can use `collectAsState`, [`collectAsStateWithLifecycle`](https://developer.android.com/reference/kotlin/androidx/lifecycle/compose/collectAsStateWithLifecycle.composable), [`observeAsState`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/livedata/observeAsState.composable#(androidx.lifecycle.LiveData).observeAsState(kotlin.Any)), and [`produceState`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/produceState.composable#produceState(kotlin.Any,kotlin.coroutines.SuspendFunction1)) to bridge other asynchronous sources into Compose `State`.

## Use Compose State in a ViewModel

Inside a [`ViewModel`](https://developer.android.com/topic/libraries/architecture/viewmodel), you can declare independent screen
inputs as granular `MutableState` properties, persist them across process death
with [`SavedStateHandle.saveable`](https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-savedstate#savedstate-compose-state), update multiple
properties atomically with
[`Snapshot.withMutableSnapshot`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/snapshots/Snapshot.Companion#withMutableSnapshot(kotlin.Function0)), and combine them with
repository `Flow` streams inside a [`transform`](https://developer.android.com/topic/libraries/architecture/appstate/transform):


```kotlin
sealed interface TaskListState {
    data object Loading : TaskListState
    data class Success(
        val tasks: List<Task>,
        val selectedTaskIds: Set<String>,
        val isOnline: Boolean = true,
    ) : TaskListState
}

@HiltViewModel
class TaskListViewModel @Inject constructor(
    private val tasksRepository: TasksRepository,
    savedStateHandle: SavedStateHandle,
) : ViewModel() {

    var selectedTaskIds by mutableStateOf(emptySet<String>())
        private set

    var searchQuery by savedStateHandle.saveable { mutableStateOf("") }
        private set

    fun updateSearchQuery(query: String) {
        Snapshot.withMutableSnapshot {
            searchQuery = query
            selectedTaskIds = emptySet()
        }
    }

    val tasksState: State<TaskListState> = transform<TaskListState>(
        initialValue = TaskListState.Loading,
        scope = viewModelScope,
    ) {
        val tasks = remember(searchQuery) {
            tasksRepository.getTasks(searchQuery)
        }.collectAsState(initial = null).value
            ?: return@transform TaskListState.Loading

        TaskListState.Success(
            tasks = tasks,
            selectedTaskIds = selectedTaskIds,
        )
    }
}
```

<br />

Key patterns in this `ViewModel`:

- **Use `SavedStateHandle.saveable` for reactive saved state** : Delegating `searchQuery` to `SavedStateHandle.saveable` with `mutableStateOf` (from `androidx.lifecycle:lifecycle-viewmodel-compose`) persists the value across process death as a `MutableState`, so `transform` tracks reads automatically. Avoid bare `SavedStateHandle.saved`, which returns a plain Kotlin property rather than Compose `State` and doesn't trigger recomposition when changed.
- **Atomic multi-property writes with `Snapshot.withMutableSnapshot`** : Updating `searchQuery` and `selectedTaskIds` inside `Snapshot.withMutableSnapshot` isolates the writes and commits both changes in a single atomic snapshot transaction, so observers (including `transform`) see both updates together in one recomposition pass rather than observing the new `searchQuery` paired with stale `selectedTaskIds`.
- **Reuse flows across recompositions with `remember(key)`** : Wrapping `tasksRepository.getTasks(searchQuery)` in [`remember`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/remember.composable#remember(kotlin.Function0)) with `searchQuery` as a key ensures that when `selectedTaskIds` changes and recomposes the `transform` block, Compose reuses the existing database `Flow` rather than restarting the query.

## Share live system state across your app

For live system state shared across multiple ViewModels, activities, or
services---such as network or Bluetooth connection status---you don't want to
persist stale status to disk across process death. Instead, query the current
system state on startup, hold it in a private `mutableStateOf` property inside
an application-scoped singleton, and expose a read-only `State<T>`:


```kotlin
interface NetworkMonitor {
    val isOnline: State<Boolean>
}

@Singleton
class LiveNetworkMonitor @Inject constructor(
    @ApplicationContext context: Context,
) : NetworkMonitor {
    private val connectivityManager =
        context.getSystemService(ConnectivityManager::class.java)

    private val _isOnline = mutableStateOf(checkCurrentConnectivity())
    override val isOnline: State<Boolean> = _isOnline

    private val callback = object : ConnectivityManager.NetworkCallback() {
        override fun onCapabilitiesChanged(
            network: Network,
            networkCapabilities: NetworkCapabilities,
        ) {
            _isOnline.value = networkCapabilities.hasCapability(
                NetworkCapabilities.NET_CAPABILITY_INTERNET
            )
        }

        override fun onLost(network: Network) {
            _isOnline.value = false
        }
    }

    init {
        connectivityManager.registerDefaultNetworkCallback(callback)
    }

    private fun checkCurrentConnectivity(): Boolean {
        val network = connectivityManager.activeNetwork ?: return false
        val capabilities =
            connectivityManager.getNetworkCapabilities(network) ?: return false
        return capabilities.hasCapability(
            NetworkCapabilities.NET_CAPABILITY_INTERNET
        )
    }
}
```

<br />

`MutableState` supports consistent reads and updates from any thread, so
`NetworkCallback` can update `_isOnline.value` directly from its background
callback thread. If a background callback updates multiple `MutableState`
properties together, wrap the writes in
[`Snapshot.withMutableSnapshot`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/snapshots/Snapshot.Companion#withMutableSnapshot(kotlin.Function0)) so they're applied
atomically.

Any component in your app can read `networkMonitor.isOnline.value`---whether as a
one-off check, inside a UI composable, or inside a state-observing block such as
[`listener`](https://developer.android.com/topic/libraries/architecture/appstate/transform#listener), [`derivedStateOf`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/package-summary#derivedStateOf(kotlin.Function0)), or
[`transform`](https://developer.android.com/topic/libraries/architecture/appstate/transform). For example, `TaskListViewModel` can read
`networkMonitor.isOnline.value` inside its `transform` block:


```kotlin
val tasksState: State<TaskListState> = transform<TaskListState>(
    initialValue = TaskListState.Loading,
    scope = viewModelScope,
) {
    val tasks = remember(searchQuery) {
        tasksRepository.getTasks(searchQuery)
    }.collectAsState(initial = null).value
        ?: return@transform TaskListState.Loading

    TaskListState.Success(
        tasks = tasks,
        selectedTaskIds = selectedTaskIds,
        isOnline = networkMonitor.isOnline.value,
    )
}
```

<br />

Because `transform` tracks `networkMonitor.isOnline.value` alongside
`searchQuery`, `selectedTaskIds`, and the repository `Flow`, any change to
connectivity automatically recomputes `TaskListState.Success` without
re-querying the database.