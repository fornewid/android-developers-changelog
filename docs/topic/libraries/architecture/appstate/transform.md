---
title: https://developer.android.com/topic/libraries/architecture/appstate/transform
url: https://developer.android.com/topic/libraries/architecture/appstate/transform
source: md.txt
---

# Transform
Part of [Android Jetpack](https://developer.android.com/jetpack).

> [!WARNING]
> **Experimental:** AppState is in alpha. Its APIs are subject to change. File bugs and feedback using the [Transform issue tracker](https://issuetracker.google.com/issues/new?component=2302904&template=2430547) or [StateStore issue tracker](https://issuetracker.google.com/issues/new?component=2302751&template=2430521).

Transform is a library built on the Compose runtime that runs a `@Composable`
block without a UI to transform inputs into Compose [`State`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/State).
Whenever any `State` read inside the block changes, the block automatically
recomposes and updates the returned `State`---letting you use Compose's
dependency tracking and recomposition model in ViewModels, repositories, or
background services.

## Use cases

- **Reactive data transformation**: Convert raw data streams (such as network responses or database queries) into UI-ready state.
- **Combine multiple inputs** : Merge multiple independent state sources (such as user input, settings, and network status) into a single cohesive state without complex `Flow` operators.
- **Debouncing and throttling** : Implement time-based behavior (such as debouncing search queries) using standard Compose [side-effects](https://developer.android.com/develop/ui/compose/side-effects) like [`LaunchedEffect`](https://developer.android.com/develop/ui/compose/side-effects#launchedeffect).
- **Conditional operations** : Run different state-gathering logic based on current conditions using standard `if`-`else` or `when` expressions.

## API overview

The `androidx.appstate.transform` package provides the following functions:

    package androidx.appstate.transform

    import androidx.compose.runtime.Composable
    import androidx.compose.runtime.State
    import kotlinx.coroutines.CoroutineDispatcher
    import kotlinx.coroutines.CoroutineScope
    import kotlinx.coroutines.Dispatchers

    public fun <R> transform(
        initialValue: R,
        scope: CoroutineScope,
        dispatcher: CoroutineDispatcher = Dispatchers.Default,
        onUpdate: @Composable (R) -> R,
    ): State<R>

    @Composable
    public fun <R> transform(
        initialValue: R,
        dispatcher: CoroutineDispatcher = Dispatchers.Default,
        onUpdate: @Composable (R) -> R,
    ): State<R>

    public suspend fun listener(
        dispatcher: CoroutineDispatcher = Dispatchers.Default,
        onUpdate: @Composable () -> Unit,
    )

> [!NOTE]
> **Note:** Because `transform` and `listener` take `@Composable` blocks, you must enable Compose build features (`buildFeatures { compose = true }`) and the [Compose Compiler Gradle plugin](https://developer.android.com/develop/ui/compose/setup-compose-dependencies-and-compiler) in any module that uses them, including non-UI modules. For setup details, see [Project
> setup](https://developer.android.com/topic/libraries/architecture/appstate#project-setup).

## Create a transform

You can create transforms either on their own (using a provided
`CoroutineScope`) or within an existing Composition. The key parameters for any
transform are `initialValue` and `onUpdate`. The `onUpdate` lambda receives the
previous output value `R` as its parameter (initialized to `initialValue` on the
first composition). You can return this parameter to keep the last emitted state
instead of resetting to a loading state, such as
`{ previous -> flow.collectAsState(initial = null).value ?: previous }`.

For example, you can use `transform` to observe changes to a search query string
and debounce expensive computations like network calls:


```kotlin
var query: String by mutableStateOf("")
val searchResults: List<String> by transform<List<String>>(
    initialValue = emptyList(),
    scope = coroutineScope,
) {
    var results by remember { mutableStateOf(emptyList<String>()) }
    LaunchedEffect(query) {
        if (query.isBlank()) {
            results = emptyList()
            return@LaunchedEffect
        }
        delay(300.milliseconds)
        results = api.search(query)
    }
    results
}
```

<br />

In this snippet:

- `query` is backed by a `MutableState`, which a search bar UI composable can read and update.
- `transform` takes an `initialValue` of an empty list, a `CoroutineScope`, and `onUpdate` as a trailing lambda.
- Inside the `onUpdate` block, [`remember`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/remember.composable#remember(kotlin.Function0)) keeps the `results` state across recompositions while `LaunchedEffect` runs.
- `LaunchedEffect` takes `query` as a key. Because `query` is backed by a `MutableState`, the effect is cancelled and relaunched every time `query` changes.
- To avoid calling the API on every keystroke, the effect body waits 300 ms. If the query changes before that delay completes, the effect is cancelled and no network call is made.

Inside a `@Composable` function, you can also use the `@Composable transform`
overload, which remembers a `CoroutineScope` internally and runs `onUpdate` on
`Dispatchers.Default` by default. This is useful when you want to offload an
expensive state derivation (such as filtering or searching a large list) off the
main UI thread:


```kotlin
@Composable
fun LogViewerScreen(
    entriesState: State<List<LogEntry>>,
    filterQueryState: State<String>,
) {
    // Calls rememberCoroutineScope() internally and runs onUpdate on
    // Dispatchers.Default so main-thread UI recomposition isn't blocked
    val matchingEntries by transform<List<LogEntry>>(
        initialValue = emptyList(),
        dispatcher = Dispatchers.Default,
    ) {
        val entries by entriesState
        val filterQuery by filterQueryState
        if (filterQuery.isBlank()) {
            entries
        } else {
            entries.filter { entry ->
                entry.matchesQuery(filterQuery)
            }
        }
    }
    // Render matchingEntries...
}
```

<br />

## Observe state with `listener`

When you want to react to Compose `State` changes in a non-UI component (such as
a state manager, repository, or background service) without producing a derived
`State<R>`, use `listener`.

`listener` is a `suspend` function that runs a `@Composable () -> Unit` block
until the calling coroutine is cancelled, automatically recomposing whenever any
state read inside `onUpdate` changes:


```kotlin
class FocusSessionManager(
    private val stateStore: StateStore,
    private val notificationManager: NotificationManager,
    scope: CoroutineScope,
) {
    val session: State<FocusSession> = stateStore.getState(FocusSessionKey)

    init {
        scope.launch {
            listener {
                when (val current = session.value) {
                    is FocusSession.Running -> {
                        LaunchedEffect(current.endTimeMillis) {
                            val remainingMillis =
                                current.endTimeMillis - System.currentTimeMillis()
                            if (remainingMillis > 0) {
                                delay(remainingMillis)
                            }
                            stateStore.setState(FocusSessionKey, FocusSession.Idle)
                            notificationManager.notify(
                                NOTIFICATION_ID,
                                buildSessionCompleteNotification(current.taskId),
                            )
                        }
                    }
                    FocusSession.Idle,
                    is FocusSession.Paused -> Unit
                }
            }
        }
    }
    // startFocus, pauseFocus, resumeFocus, endFocus...
}
```

<br />

In this example, `listener` observes `session.value`. When the session is
`FocusSession.Running`, `LaunchedEffect` waits until `endTimeMillis` before
resetting the session to `FocusSession.Idle` and posting a completion
notification. If the user pauses or ends the session early, the `Running` branch
leaves composition and cancels the timer automatically. When `scope` is
cancelled, `listener` stops observing.

## Common patterns

The following patterns show how to use `transform` for conditional logic,
combining multiple streams, and producing UI state in a `ViewModel`.

### Conditional state production

Use standard Kotlin `if`-`else` or `when` expressions inside `transform` to
switch between upstream state sources based on current conditions. Because read
tracking is dynamic, `transform` only observes the branch that runs on the
current recomposition:


```kotlin
var searchQuery by mutableStateOf("")

val displayedTasks: State<List<Task>> = transform(
    initialValue = emptyList(),
    scope = coroutineScope,
) {
    if (searchQuery.isBlank()) {
        val recentTasks by tasksRepository.recentTasks.collectAsState(
            initial = emptyList(),
        )
        recentTasks
    } else {
        val matchingTasks by remember(searchQuery) {
            tasksRepository.searchTasks(searchQuery)
        }.collectAsState(initial = emptyList())
        matchingTasks
    }
}
```

<br />

### Combine multiple state sources

Because Compose automatically tracks state reads, you can combine any number of
`State<T>` properties and `Flow` streams in a single `transform` block. Unlike
[`Flow.combine`](https://developer.android.com/kotlin/flow), which only provides typed overloads for up to
five flows before falling back to an untyped `Array<Any?>`, adding another input
in `transform` is always a single type-safe read:


```kotlin
var showCompleted by mutableStateOf(false)
var selectedCategory by mutableStateOf<Category?>(null)

val dashboardState: State<DashboardUiState> = transform(
    initialValue = DashboardUiState(),
    scope = coroutineScope,
) {
    val tasks by tasksRepository.tasksFlow.collectAsState(initial = emptyList())
    val sortOrder by userPrefsRepository.sortOrderFlow.collectAsState(
        initial = SortOrder.BY_DEADLINE,
    )
    val focusSession by focusSessionManager.session
    val isOnline by networkMonitor.isOnline

    val visibleTasks = tasks
        .filter { task ->
            (showCompleted || !task.isCompleted) &&
                (selectedCategory == null || task.category == selectedCategory)
        }
        .sortedWith(sortOrder.comparator)

    DashboardUiState(
        tasks = visibleTasks,
        selectedCategory = selectedCategory,
        focusSession = focusSession,
        isOnline = isOnline,
    )
}
```

<br />

### Use `transform` in a ViewModel

The non-composable `transform` overload runs reactive logic in non-UI layers
(such as ViewModels or repositories) while using Compose's state model. It runs
as long as the provided `CoroutineScope` is active, so you can tie it to a
component's lifecycle by passing `viewModelScope` inside a
[`ViewModel`](https://developer.android.com/topic/libraries/architecture/viewmodel):


```kotlin
class HomeViewModel(
    private val mediaRepository: MediaRepository,
    private val networkMonitor: NetworkMonitor,
) : ViewModel() {
    val uiState: State<HomeUiState> = transform<HomeUiState>(
        initialValue = HomeUiState.Loading,
        scope = viewModelScope,
    ) {
        val isOnline by networkMonitor.isOnline
        val tracks = if (isOnline) {
            mediaRepository.allTracksFlow.collectAsState(initial = null).value
        } else {
            mediaRepository.downloadedTracksFlow
                .collectAsState(initial = null).value
        } ?: return@transform HomeUiState.Loading

        HomeUiState.Success(
            tracks = tracks,
            isOnline = isOnline,
        )
    }
}
```

<br />

In this `ViewModel`, `uiState` reads `networkMonitor.isOnline` and dynamically
switches between collecting `mediaRepository.downloadedTracksFlow` when offline
and `mediaRepository.allTracksFlow` when online, exposing a single
`State<HomeUiState>` that UI composables can read directly. For more details on
combining `transform` with `MutableState` and `SavedStateHandle.saveable`, see
[Use Compose State in a ViewModel](https://developer.android.com/topic/libraries/architecture/appstate/state-beyond-ui#state-in-viewmodel).

> [!NOTE]
> **Note:** A `transform` scoped to `viewModelScope` remains active for the entire lifetime of `viewModelScope` (including while the UI is in the background), whereas the `@Composable transform` overload follows the lifecycle of the UI composition that calls it.

## Choose between `transform`, `derivedStateOf`, and `Flow`

Use the following guidelines to choose between `transform`, `derivedStateOf`,
and Kotlin `Flow`:

### `derivedStateOf` versus `transform`

Both [`derivedStateOf`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/package-summary#derivedStateOf(kotlin.Function0)) and `transform` produce a derived
`State<T>` that automatically tracks the Compose states read inside its block.
Choose between them based on whether you're computing a value directly from
existing `State<T>` objects or need `@Composable` features such as
`collectAsState`, [`produceState`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/produceState.composable#produceState(kotlin.Any,kotlin.coroutines.SuspendFunction1)), and `LaunchedEffect`:

| Capability | `derivedStateOf` | `transform` |
|---|---|---|
| **Lambda type** | Standard Kotlin lambda (`() -> T`) | `@Composable` lambda (`@Composable (R) -> R`) |
| **Supported inputs** | Synchronous `State<T>` reads only | `State<T>`, Kotlin `Flow` (using [`collectAsState`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/collectAsState.composable#(kotlinx.coroutines.flow.Flow).collectAsState(kotlin.Any,kotlin.coroutines.CoroutineContext,androidx.compose.runtime.SnapshotMutationPolicy))), `suspend` functions, and callback APIs (using [`produceState`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/produceState.composable#produceState(kotlin.Any,kotlin.coroutines.SuspendFunction1))) |
| **Execution and consistency** | Lazy and synchronous when `.value` is read; updates atomically within the same snapshot without an `initialValue` or `CoroutineScope` | Runs an active Composition in a `CoroutineScope` and recomposes asynchronously after a snapshot commits; requires an `initialValue` |
| **State and side-effects** | Can't call `remember` or side-effect APIs | Supports `remember`, `LaunchedEffect`, `produceState`, and reusable `@Composable` functions |

Use **`derivedStateOf`** when all inputs are already `State<T>` objects and you
don't need `@Composable` APIs:

- **Synchronous, same-snapshot derivations** : Computing a value or filtered list from existing `State<T>` properties without managing a `CoroutineScope` or providing a placeholder `initialValue`. Because `derivedStateOf` evaluates synchronously when `.value` is read, callers reading `.value` immediately after updating an input state always observe the updated result in the same snapshot.
- **Reducing how often observers update** : Computing a value that changes less often than its source `State<T>` (such as checking whether a scroll offset exceeds a threshold). For more details, see the [`derivedStateOf`
  documentation](https://developer.android.com/develop/ui/compose/side-effects#derivedstateof).

Use **`transform`** when your derivation requires the Compose runtime:

- **Combining `State<T>` with asynchronous streams** : Collecting a Kotlin `Flow` from a repository or database using `collectAsState` alongside `State<T>` inputs.
- **Restarting upstream work when inputs change** : Using `remember(key)` inside the block to recreate a parameterized `Flow` only when a specific `State<T>` input updates.
- **Running side-effects or remembering intermediate state** : Using `LaunchedEffect` (for example, to debounce inputs or run timers), `produceState` (to load data from a `suspend` function or wrap a callback with `awaitDispose`), or `remember` to keep state across recompositions.

> [!NOTE]
> **Note:** Inside a `@Composable` function (including `transform`), use [`produceState`](https://developer.android.com/develop/ui/compose/side-effects#producestate) when converting a single `suspend` call or callback-based API into `State<T>` keyed on explicit inputs (`produceState(init, key1)`). Unlike `transform`, `produceState` runs a `suspend` coroutine rather than a Composition, so it doesn't automatically track `State<T>` reads inside its producer block unless you pass those values as keys. Use `transform` when you want automatic, dynamic `State<T>` read tracking or need to call `@Composable` functions such as `collectAsState` and `remember`.

The following example compares `derivedStateOf` with a `transform` block that
combines `State<T>` and a repository `Flow`:


```kotlin
class TaskListViewModel(
    private val tasksRepository: TasksRepository,
    private val preferencesManager: TaskPreferencesManager,
) : ViewModel() {
    var searchQuery by mutableStateOf("")
        private set

    // Computing a value from existing State<T>: use derivedStateOf
    val hasSearchQuery: State<Boolean> = derivedStateOf {
        searchQuery.isNotBlank()
    }

    // Combining State<T> with a Flow and remember(key): use transform
    val uiState: State<TaskListUiState> = transform<TaskListUiState>(
        initialValue = TaskListUiState.Loading,
        scope = viewModelScope,
    ) {
        val showCompleted by preferencesManager.showCompleted
        val tasks by remember(showCompleted) {
            tasksRepository.observeTasks(showCompleted)
        }.collectAsState(initial = null)

        val currentTasks = tasks ?: return@transform TaskListUiState.Loading
        val filteredTasks = currentTasks.filter { task ->
            task.title.contains(searchQuery, ignoreCase = true)
        }
        TaskListUiState.Success(filteredTasks)
    }
}
```

<br />

In this example, `hasSearchQuery` only inspects the `searchQuery` state, so
`derivedStateOf` computes it lazily without a `CoroutineScope`. By contrast,
`uiState` combines `preferencesManager.showCompleted` and `searchQuery` with an
asynchronous `Flow` from `tasksRepository` and uses `remember(showCompleted)` to
avoid recreating the `Flow` when only `searchQuery` changes.

### When to use `Flow` instead of `transform`

`transform` is designed to represent the **current value** of state, not a
stream of events. If a state changes multiple times before the next
recomposition, Compose only uses the latest value, and it skips updates when the
new value equals (`==`) the previous value. Use Kotlin [`Flow`](https://developer.android.com/kotlin/flow)
instead when your logic must process every value in order:

- **Running totals and averages** : Calculations like moving averages, cumulative sums, or undo history (`runningFold` or `scan`) need every value to be counted once. In a `transform` block, rapid updates before recomposition are skipped, two identical readings in a row (such as a sensor emitting `10.0` twice) don't trigger recomposition, and recompositions triggered by other states in the same block can count the current value twice. Compute the running value in a `Flow` first, then collect the result in `transform` if you need to combine it with other state.
- **Event logging and queues** : Pipelines that log user interactions, process queued network requests, or record transactions where every intermediate change (`A -> B -> C` or `A -> B -> A`) must be recorded.
- **One-time events** : Actions like playing a sound or sending a hardware command, where sending the same command twice in a row must run twice. `transform` requires an `initialValue` and skips consecutive equal outputs.
- **Backpressure-sensitive streams**: Streams (such as file or socket reads) where a fast producer must suspend when a consumer falls behind. Compose state writes don't suspend and overwrite previous values instead.

## Test transforms

Because transforms rely on the Compose runtime and Kotlin Coroutines, testing
them requires coordinating asynchronous execution and state recomposition. Use
the `androidx.appstate.transform:transform-testing` artifact to control the
coroutine scheduler and trigger recompositions in unit tests.

The `androidx.appstate.transform.testing` package provides the following APIs:

    package androidx.appstate.transform.testing

    import kotlin.coroutines.CoroutineContext
    import kotlin.coroutines.EmptyCoroutineContext
    import kotlin.time.Duration
    import kotlinx.coroutines.CoroutineScope
    import kotlinx.coroutines.test.TestCoroutineScheduler
    import kotlinx.coroutines.test.TestDispatcher
    import kotlinx.coroutines.test.TestResult

    public fun transformTest(
        context: CoroutineContext = EmptyCoroutineContext,
        block: suspend TransformTestScope.() -> Unit,
    ): TestResult

    public sealed interface TransformTestScope : CoroutineScope {
        public val testCoroutineScheduler: TestCoroutineScheduler
        public val testDispatcher: TestDispatcher
        public val backgroundScope: CoroutineScope
        public fun advance()
        public fun advanceTimeBy(duration: Duration)
        public fun advanceUntilIdle()
    }

`transformTest` wraps [`runTest`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-test/kotlinx.coroutines.test/run-test.html) and executes your test
block with a `TransformTestScope` receiver:

- **`backgroundScope`** : A `CoroutineScope` for running transforms that shouldn't block test completion. It's automatically cancelled when the test finishes, which stops the transform.
- **`testDispatcher`** : A `TestDispatcher` linked to `testCoroutineScheduler`. Pass this to `transform`'s `dispatcher` parameter so recomposition runs on the test scheduler instead of defaulting to `Dispatchers.Default`.
- **`advance`** : Runs pending coroutines on the test scheduler, sends Compose snapshot apply notifications (`Snapshot.sendApplyNotifications`), and recomposes the `transform` so the output `State` updates.
- **`advanceTimeBy(duration)` and `advanceUntilIdle`** : Advance the virtual clock on `testCoroutineScheduler` for time-dependent operations.

### Test state updates

To test a `transform`, pass `backgroundScope` and `testDispatcher` from
`TransformTestScope`, then call `advance` after updating an input state or
`Flow`:


```kotlin
@Test
fun testStateUpdate() = transformTest {
    var sourceState by mutableStateOf(0)

    val state = transform(
        initialValue = 0,
        scope = backgroundScope,
        dispatcher = testDispatcher,
    ) {
        sourceState
    }
    assertThat(state.value).isEqualTo(0)

    // Modify the source state and advance to trigger recomposition.
    sourceState = 1
    advance()

    assertThat(state.value).isEqualTo(1)
}
```

<br />

### Test time-based operations

When a `transform` uses time-based side-effects like `LaunchedEffect` and
`delay` (such as debouncing search queries), combine `advanceTimeBy(duration)`
with `advance`:

1. After modifying an input state, call `advance` so the `transform` block recomposes and starts the `LaunchedEffect`.
2. Call `advanceTimeBy(duration)` to move the virtual clock forward, and then call `advance` to run tasks scheduled at that timestamp and recompose the `transform`.


```kotlin
@Test
fun testDebouncedSearch() = transformTest {
    var query by mutableStateOf("")

    val searchResults = transform<List<String>>(
        initialValue = emptyList(),
        scope = backgroundScope,
        dispatcher = testDispatcher,
    ) {
        var results by remember { mutableStateOf(emptyList<String>()) }
        LaunchedEffect(query) {
            if (query.isBlank()) {
                results = emptyList()
                return@LaunchedEffect
            }
            delay(300.milliseconds)
            results = api.search(query)
        }
        results
    }

    query = "compose"
    // Recompose to start the LaunchedEffect for the new query.
    advance()

    // Results don't update before the 300ms debounce delay completes.
    advanceTimeBy(200.milliseconds)
    advance()
    assertThat(searchResults.value).isEmpty()

    // Advance past the remaining 100ms and trigger recomposition.
    advanceTimeBy(100.milliseconds)
    advance()
    assertThat(searchResults.value).containsExactly("Compose State", "Compose UI")
}
```

<br />

### Test a ViewModel or state holder

Because `transform` runs its Composition in the provided `scope` and defaults
its `dispatcher` parameter to `Dispatchers.Default`, classes that create a
`transform` should accept a `CoroutineScope` and a `CoroutineDispatcher` as
constructor parameters. In a [`ViewModel`](https://developer.android.com/topic/libraries/architecture/viewmodel), pass the injected
`CoroutineScope` to the `ViewModel(coroutineScope)` constructor and forward the
`CoroutineDispatcher` to `transform`:


```kotlin
class HomeViewModel(
    private val mediaRepository: MediaRepository,
    private val networkMonitor: NetworkMonitor,
    coroutineScope: CoroutineScope =
        CoroutineScope(SupervisorJob() + Dispatchers.Main.immediate),
    dispatcher: CoroutineDispatcher = Dispatchers.Default,
) : ViewModel(coroutineScope) {
    val uiState: State<HomeUiState> = transform<HomeUiState>(
        initialValue = HomeUiState.Loading,
        scope = viewModelScope,
        dispatcher = dispatcher,
    ) {
        val isOnline by networkMonitor.isOnline
        val tracks = if (isOnline) {
            mediaRepository.allTracksFlow.collectAsState(initial = null).value
        } else {
            mediaRepository.downloadedTracksFlow
                .collectAsState(initial = null).value
        } ?: return@transform HomeUiState.Loading

        HomeUiState.Success(
            tracks = tracks,
            isOnline = isOnline,
        )
    }
}

@Test
fun testHomeViewModelOfflineState() = transformTest {
    val mediaRepository = FakeMediaRepository()
    val networkMonitor = FakeNetworkMonitor()
    val viewModel = HomeViewModel(
        mediaRepository = mediaRepository,
        networkMonitor = networkMonitor,
        coroutineScope = backgroundScope,
        dispatcher = testDispatcher,
    )

    val downloadedTrack = Track(id = "1", isDownloaded = true)
    val streamingTrack = Track(id = "2", isDownloaded = false)
    mediaRepository.emitAllTracks(listOf(downloadedTrack, streamingTrack))
    mediaRepository.emitDownloadedTracks(listOf(downloadedTrack))
    advance()
    assertThat(viewModel.uiState.value).isEqualTo(
        HomeUiState.Success(
            tracks = listOf(downloadedTrack, streamingTrack),
            isOnline = true,
        )
    )

    // Switch offline and verify it switches to downloadedTracksFlow.
    networkMonitor.setOnline(false)
    // First advance() recomposes into the offline branch (where collectAsState
    // initially returns null -> Loading) and starts collecting downloadedTracksFlow.
    advance()
    // Second advance() applies the collected downloadedTracksFlow value and
    // recomposes uiState with the offline Success state.
    advance()
    assertThat(viewModel.uiState.value).isEqualTo(
        HomeUiState.Success(
            tracks = listOf(downloadedTrack),
            isOnline = false,
        )
    )
}
```

<br />

In this test, passing `backgroundScope` and `testDispatcher` into
`HomeViewModel` binds its `viewModelScope` and `transform` Composition to the
test scheduler, so each `advance` call deterministically processes emissions
from `FakeMediaRepository` and `FakeNetworkMonitor`. For more patterns on using
`SavedStateHandle.saveable` and `Snapshot.withMutableSnapshot` in a `ViewModel`,
see [Use Compose State in a ViewModel](https://developer.android.com/topic/libraries/architecture/appstate/state-beyond-ui#state-in-viewmodel).