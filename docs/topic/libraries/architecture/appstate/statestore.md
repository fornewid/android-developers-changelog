---
title: https://developer.android.com/topic/libraries/architecture/appstate/statestore
url: https://developer.android.com/topic/libraries/architecture/appstate/statestore
source: md.txt
---

# StateStore
Part of [Android Jetpack](https://developer.android.com/jetpack).

> [!WARNING]
> **Experimental:** AppState is in alpha. Its APIs are subject to change. File bugs and feedback using the [Transform issue tracker](https://issuetracker.google.com/issues/new?component=2302904&template=2430547) or [StateStore issue tracker](https://issuetracker.google.com/issues/new?component=2302751&template=2430521).

StateStore is a type-safe container that stores and exposes shared application
state as Compose `State` across your app.

## Use cases

By creating an application-scoped `StateStore`, you can share state between
application components within the same process:

- **Multiple activities** : If your app displays multiple activities simultaneously (such as an inbox activity and an editor activity in an email client) or has an activity that supports [multi-instance](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode#multi-instance) (such as a document viewer activity), you can use `StateStore` to share information between them.
- **Activity and service** : Synchronize state between an activity and a background [`CarAppService`](https://developer.android.com/training/cars/apps/library) or [AppFunction](https://developer.android.com/ai/appfunctions).
- **Activity and content provider or widget**: Share state between an activity and a home screen widget.

If a singleton only needs in-memory `State<T>` without keyed lookup or
DataStore-backed process-death restoration, you can expose `mutableStateOf`
properties directly on the singleton instead. For a comparison of state APIs
across your app, see [Choose the right state API across your
architecture](https://developer.android.com/topic/libraries/architecture/appstate/state-beyond-ui#choose-state-api).

> [!CAUTION]
> **Caution:** Because `StateStore` lives in memory, you can only access it from the same process in which it's instantiated. If you need to share state across processes, use [interprocess communication (IPC) methods](https://developer.android.com/guide/components/processes-and-threads#IPC).

## API overview

The `androidx.appstate.statestore` package provides the `StateStore` and
`StateStoreKey` classes:

    package androidx.appstate.statestore

    import androidx.compose.runtime.State
    import kotlinx.serialization.Serializable

    public class StateStore {
        public val keys: Set<StateStoreKey<*>>
        public fun <T> getState(
            stateKey: StateStoreKey<T>,
            defaultValue: T = stateKey.defaultValue,
        ): State<T>
        public fun <T> setState(stateKey: StateStoreKey<T>, value: T)
        public inline fun <T> updateState(
            stateKey: StateStoreKey<T>,
            defaultValue: T = stateKey.defaultValue,
            update: (T) -> T,
        )
    }

    @Serializable
    public open class StateStoreKey<T>(
        public val defaultValue: T,
    )

### Define your state

To ensure type safety when storing and retrieving values, `StateStore` uses the
`StateStoreKey` class to define the keys used to read and write values. Keep
`StateStoreKey` definitions `private` or `internal` to the manager, repository,
or module that owns that slice of state:


```kotlin
@Serializable
sealed interface FocusSession {
    @Serializable
    data object Idle : FocusSession

    @Serializable
    data class Running(
        val taskId: String,
        val endTimeMillis: Long,
    ) : FocusSession

    @Serializable
    data class Paused(
        val taskId: String,
        val remainingMillis: Long,
    ) : FocusSession
}

@Serializable
private data object FocusSessionKey :
    StateStoreKey<FocusSession>(defaultValue = FocusSession.Idle)
```

<br />

### Create and inject `StateStore` instances

`StateStore` is a regular class that you instantiate once at the application or
module scope (for example, in your `Application` class or a dependency injection
module) and inject into the managers or repositories that read and write state,
rather than exposing `StateStore` directly to UI classes:


```kotlin
// Instantiate at the application or DI module level
val stateStore = StateStore()

// Inject into managers or repositories that encapsulate their own keys
class FocusSessionManager(
    private val stateStore: StateStore,
)
```

<br />

### Read and write state

Inside your manager or repository, read, write, and update values in the
injected `StateStore` using your private `StateStoreKey` definitions, and expose
read-only `State<T>` properties and mutation functions to callers.

#### Read state

Use `getState(stateKey, defaultValue)` to retrieve a [`State<T>`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/State)
object. If the key isn't initialized yet, `StateStore` populates it with the
`defaultValue` parameter, which defaults to `stateKey.defaultValue` (or you can
pass a custom `defaultValue` when initializing an unpopulated key). Because
`getState` returns a `State<T>`, ViewModels, UI composables, widgets, and
[`transform`](https://developer.android.com/topic/libraries/architecture/appstate/transform) blocks can read the manager's property
reactively:


```kotlin
class FocusSessionManager(
    private val stateStore: StateStore,
) {
    val session: State<FocusSession> = stateStore.getState(FocusSessionKey)
}

class FocusTimerViewModel(
    focusSessionManager: FocusSessionManager,
) : ViewModel() {
    val session: State<FocusSession> = focusSessionManager.session
}

@Composable
fun FocusBanner(viewModel: FocusTimerViewModel = viewModel()) {
    // Reads state reactively; recomposes when FocusSessionKey updates
    when (val session = viewModel.session.value) {
        FocusSession.Idle -> Text(text = "No active focus session")
        is FocusSession.Running -> Text(text = "Focusing on ${session.taskId}")
        is FocusSession.Paused -> Text(text = "Paused: ${session.taskId}")
    }
}
```

<br />

#### Write state

Use `setState(stateKey, value)` inside your manager to initialize or replace the
value associated with a key:


```kotlin
class FocusSessionManager(
    private val stateStore: StateStore,
) {
    val session: State<FocusSession> = stateStore.getState(FocusSessionKey)

    fun startFocus(taskId: String, endTimeMillis: Long) {
        stateStore.setState(
            FocusSessionKey,
            FocusSession.Running(
                taskId = taskId,
                endTimeMillis = endTimeMillis,
            ),
        )
    }

    fun endFocus() {
        stateStore.setState(FocusSessionKey, FocusSession.Idle)
    }
}
```

<br />

#### Update state

If you need to update a state based on its current value, use `updateState`.
This retrieves the current value (or uses the default if not set) and applies
your update lambda:


```kotlin
class FocusSessionManager(
    private val stateStore: StateStore,
) {
    val session: State<FocusSession> = stateStore.getState(FocusSessionKey)

    fun pauseFocus(nowMillis: Long) {
        stateStore.updateState(FocusSessionKey) { current ->
            if (current is FocusSession.Running) {
                FocusSession.Paused(
                    taskId = current.taskId,
                    remainingMillis = (current.endTimeMillis - nowMillis)
                        .coerceAtLeast(0L),
                )
            } else {
                current
            }
        }
    }

    fun resumeFocus(nowMillis: Long) {
        stateStore.updateState(FocusSessionKey) { current ->
            if (current is FocusSession.Paused) {
                FocusSession.Running(
                    taskId = current.taskId,
                    endTimeMillis = nowMillis + current.remainingMillis,
                )
            } else {
                current
            }
        }
    }
}
```

<br />

## Integrations

`StateStore` integrates with Jetpack [DataStore](https://developer.android.com/topic/libraries/architecture/datastore) to persist and
restore state across process death and app restarts.

### DataStore

The `androidx.appstate.statestore:statestore-datastore` artifact lets you
configure persistence once on your shared `StateStore` instance so any
manager's persisted keys automatically save and restore from disk using
DataStore.

The `androidx.appstate.datastore` package provides the following APIs:

    package androidx.appstate.datastore

    import androidx.appstate.statestore.StateStore
    import androidx.datastore.core.DataStore
    import kotlinx.coroutines.CoroutineScope

    public interface PersistToDataStore

    public suspend fun StateStore.syncToDataStore(
        path: String,
        coroutineScope: CoroutineScope,
    )

    public suspend fun StateStore.syncToDataStore(
        dataStore: DataStore<StateStorePreferences>,
    )

1. **Implement `PersistToDataStore`** : Mark any `StateStoreKey` that should be persisted by implementing the `PersistToDataStore` interface:


```kotlin
@Serializable
private data object FocusSessionKey :
    StateStoreKey<FocusSession>(defaultValue = FocusSession.Idle),
    PersistToDataStore
```

<br />

1. **Bind `StateStore` to DataStore** : Call `syncToDataStore` once when setting up your shared `StateStore` instance (for example, in your `Application` class or dependency injection module). Because `syncToDataStore` is a `suspend` function that suspends indefinitely to restore saved values from disk and continue saving future changes in the provided `coroutineScope`, call it inside `launch` and pass your application-level `CoroutineScope`. On startup, `getState` initially returns `defaultValue` in memory and updates the `State` once DataStore finishes reading from disk:


```kotlin
class ProductivityApplication : Application() {
    val applicationScope = CoroutineScope(SupervisorJob() + Dispatchers.Default)

    val stateStore = StateStore().also { store ->
        // Restore saved values and automatically persist future changes
        // for all PersistToDataStore keys across managers
        applicationScope.launch {
            store.syncToDataStore(
                path = dataStoreFile("statestore.json").absolutePath,
                coroutineScope = applicationScope,
            )
        }
    }

    val focusSessionManager = FocusSessionManager(stateStore)
}
```

<br />

#### DataStore persistence guidelines

Because `syncToDataStore` serializes and writes to disk whenever a
`PersistToDataStore` key's value changes, follow these guidelines when choosing
what and when to persist:

- **Save start or end timestamps instead of every timer tick** : For timers or playback progress, persist a stable reference value (such as `endTimeMillis` or `startedAtMillis`) rather than updating a `PersistToDataStore` key every second or frame, and compute the live elapsed or remaining display in the UI.
- **Debounce rapid user input before updating a persisted key** : For text drafts, search queries, or sliders, hold the immediate input in an in-memory `MutableState` (or a `StateStoreKey` that doesn't implement `PersistToDataStore`) and only call `setState` on the persisted `StateStoreKey` after the input settles.
- **Keep persisted keys lightweight** : All `PersistToDataStore` keys in a `StateStore` are serialized together into a single file on each update. Persist compact session state---such as active IDs, filter selections, or in-progress form drafts---and keep large collections or queryable datasets in [Room](https://developer.android.com/training/data-storage/room).