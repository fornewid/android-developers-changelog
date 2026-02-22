---
title: https://developer.android.com/kotlin/flow/stateflow-and-sharedflow
url: https://developer.android.com/kotlin/flow/stateflow-and-sharedflow
source: md.txt
---

# StateFlow and SharedFlow

`StateFlow`and`SharedFlow`are[Flow APIs](https://developer.android.com/kotlin/flow)that enable flows to optimally emit state updates and emit values to multiple consumers.

## `StateFlow`

[`StateFlow`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-state-flow/)is a state-holder observable flow that emits the current and new state updates to its collectors. The current state value can also be read through its[`value`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-state-flow/value.html)property. To update state and send it to the flow, assign a new value to the`value`property of the[`MutableStateFlow`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-mutable-state-flow/index.html)class.

In Android,`StateFlow`is a great fit for classes that need to maintain an observable mutable state.

Following the examples from[Kotlin flows](https://developer.android.com/kotlin/flow), a`StateFlow`can be exposed from the`LatestNewsViewModel`so that the`View`can listen for UI state updates and inherently make the screen state survive configuration changes.  

    class LatestNewsViewModel(
        private val newsRepository: NewsRepository
    ) : ViewModel() {

        // Backing property to avoid state updates from other classes
        private val _uiState = MutableStateFlow(LatestNewsUiState.Success(emptyList()))
        // The UI collects from this StateFlow to get its state updates
        val uiState: StateFlow<LatestNewsUiState> = _uiState

        init {
            viewModelScope.launch {
                newsRepository.favoriteLatestNews
                    // Update View with the latest favorite news
                    // Writes to the value property of MutableStateFlow,
                    // adding a new element to the flow and updating all
                    // of its collectors
                    .collect { favoriteNews ->
                        _uiState.value = LatestNewsUiState.Success(favoriteNews)
                    }
            }
        }
    }

    // Represents different states for the LatestNews screen
    sealed class LatestNewsUiState {
        data class Success(val news: List<ArticleHeadline>): LatestNewsUiState()
        data class Error(val exception: Throwable): LatestNewsUiState()
    }

The class responsible for updating a`MutableStateFlow`is the producer, and all classes collecting from the`StateFlow`are the consumers. Unlike a*cold* flow built using the`flow`builder, a`StateFlow`is*hot* : collecting from the flow doesn't trigger any producer code. A`StateFlow`is always active and in memory, and it becomes eligible for garbage collection only when there are no other references to it from a garbage collection root.

When a new consumer starts collecting from the flow, it receives the last state in the stream and any subsequent states. You can find this behavior in other observable classes like[`LiveData`](https://developer.android.com/topic/libraries/architecture/livedata).

The`View`listens for`StateFlow`as with any other flow:  

    class LatestNewsActivity : AppCompatActivity() {
        private val latestNewsViewModel = // getViewModel()

        override fun onCreate(savedInstanceState: Bundle?) {
            ...
            // Start a coroutine in the lifecycle scope
            lifecycleScope.launch {
                // repeatOnLifecycle launches the block in a new coroutine every time the
                // lifecycle is in the STARTED state (or above) and cancels it when it's STOPPED.
                repeatOnLifecycle(Lifecycle.State.STARTED) {
                    // Trigger the flow and start listening for values.
                    // Note that this happens when lifecycle is STARTED and stops
                    // collecting when the lifecycle is STOPPED
                    latestNewsViewModel.uiState.collect { uiState ->
                        // New value received
                        when (uiState) {
                            is LatestNewsUiState.Success -> showFavoriteNews(uiState.news)
                            is LatestNewsUiState.Error -> showError(uiState.exception)
                        }
                    }
                }
            }
        }
    }

| **Warning:** Never collect a flow from the UI directly from`launch`or the`launchIn`extension function if the UI needs to be updated. These functions process events even when the view is not visible. This behavior can lead to app crashes. To avoid that, use the`repeatOnLifecycle`API as shown above.
| **Note:** The`repeatOnLifecycle`API is available only in versions of the`androidx.lifecycle:lifecycle-runtime-ktx:2.4.0`library and higher.

To convert any flow to a`StateFlow`, use the[`stateIn`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/state-in.html)intermediate operator.
| **Note:** Testing`StateFlows`, especially when they're created with`stateIn`, can require some extra attention. For details, see the[Testing Kotlin flows on Android](https://developer.android.com/kotlin/flow/test#stateflows)page.

### StateFlow, Flow, and LiveData

`StateFlow`and[`LiveData`](https://developer.android.com/topic/libraries/architecture/livedata)have similarities. Both are observable data holder classes, and both follow a similar pattern when used in your app architecture.

Note, however, that`StateFlow`and[`LiveData`](https://developer.android.com/topic/libraries/architecture/livedata)do behave differently:

- `StateFlow`requires an initial state to be passed in to the constructor, while`LiveData`does not.
- `LiveData.observe()`automatically unregisters the consumer when the view goes to the`STOPPED`state, whereas collecting from a`StateFlow`or any other flow does not stop collecting automatically. To achieve the same behavior, you need to collect the flow from a`Lifecycle.repeatOnLifecycle`block.

## Making cold flows hot using`shareIn`

`StateFlow`is a*hot* flow---it remains in memory as long as the flow is collected or while any other references to it exist from a garbage collection root. You can turn cold flows hot by using the[`shareIn`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/share-in.html)operator.

Using the`callbackFlow`created in[Kotlin flows](https://developer.android.com/kotlin/flow)as an example, instead of having each collector create a new flow, you can share the data retrieved from Firestore between collectors by using`shareIn`. You need to pass in the following:

- A`CoroutineScope`that is used to share the flow. This scope should live longer than any consumer to keep the shared flow alive as long as needed.
- The number of items to replay to each new collector.
- The start behavior policy.

    class NewsRemoteDataSource(...,
        private val externalScope: CoroutineScope,
    ) {
        val latestNews: Flow<List<ArticleHeadline>> = flow {
            ...
        }.shareIn(
            externalScope,
            replay = 1,
            started = SharingStarted.WhileSubscribed()
        )
    }

In this example, the`latestNews`flow replays the last emitted item to a new collector and remains active as long as`externalScope`is alive and there are active collectors. The`SharingStarted.WhileSubscribed()`start policy keeps the upstream producer active while there are active subscribers. Other start policies are available, such as`SharingStarted.Eagerly`to start the producer immediately or`SharingStarted.Lazily`to start sharing after the first subscriber appears and keep the flow active forever.
| **Note:** To learn more about patterns for`externalScope`, check out this[article](https://medium.com/androiddevelopers/coroutines-patterns-for-work-that-shouldnt-be-cancelled-e26c40f142ad).

## SharedFlow

The`shareIn`function returns a`SharedFlow`, a hot flow that emits values to all consumers that collect from it. A`SharedFlow`is a highly-configurable generalization of`StateFlow`.

You can create a`SharedFlow`without using`shareIn`. As an example, you could use a`SharedFlow`to send ticks to the rest of the app so that all the content refreshes periodically at the same time. Apart from fetching the latest news, you might also want to refresh the user information section with its favorite topics collection. In the following code snippet, a`TickHandler`exposes a`SharedFlow`so that other classes know when to refresh its content. As with`StateFlow`, use a backing property of type`MutableSharedFlow`in a class to send items to the flow:  

    // Class that centralizes when the content of the app needs to be refreshed
    class TickHandler(
        private val externalScope: CoroutineScope,
        private val tickIntervalMs: Long = 5000
    ) {
        // Backing property to avoid flow emissions from other classes
        private val _tickFlow = MutableSharedFlow<Unit>(replay = 0)
        val tickFlow: SharedFlow<Unit> = _tickFlow

        init {
            externalScope.launch {
                while(true) {
                    _tickFlow.emit(Unit)
                    delay(tickIntervalMs)
                }
            }
        }
    }

    class NewsRepository(
        ...,
        private val tickHandler: TickHandler,
        private val externalScope: CoroutineScope
    ) {
        init {
            externalScope.launch {
                // Listen for tick updates
                tickHandler.tickFlow.collect {
                    refreshLatestNews()
                }
            }
        }

        suspend fun refreshLatestNews() { ... }
        ...
    }

You can customize the`SharedFlow`behavior in the following ways:

- `replay`lets you resend a number of previously-emitted values for new subscribers.
- `onBufferOverflow`lets you specify a policy for when the buffer is full of items to be sent. The default value is`BufferOverflow.SUSPEND`, which makes the caller suspend. Other options are`DROP_LATEST`or`DROP_OLDEST`.

`MutableSharedFlow`also has a`subscriptionCount`property that contains the number of active collectors so that you can optimize your business logic accordingly.`MutableSharedFlow`also contains a`resetReplayCache`function if you don't want to replay the latest information sent to the flow.

## Additional flow resources

- [Kotlin flows on Android](https://developer.android.com/kotlin/flow)
- [Testing Kotlin flows on Android](https://developer.android.com/kotlin/flow/test)
- [Things to know about Flow's shareIn and stateIn operators](https://medium.com/androiddevelopers/things-to-know-about-flows-sharein-and-statein-operators-20e6ccb2bc74)
- [Migrating from LiveData to Kotlin Flow](https://medium.com/androiddevelopers/migrating-from-livedata-to-kotlins-flow-379292f419fb)
- [Additional resources for Kotlin coroutines and flow](https://developer.android.com/kotlin/coroutines/additional-resources)