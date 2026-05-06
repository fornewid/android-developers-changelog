---
title: UI layer (Views)  |  Android Developers
url: https://developer.android.com/topic/architecture/views/ui-layer
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)
* [Guides](https://developer.android.com/topic/architecture/views/recommendations-views)

# UI layer (Views) Stay organized with collections Save and categorize content based on your preferences.





[Concepts and Jetpack Compose implementationarrow\_forward](/topic/architecture/ui-layer)

The role of the UI is to display the application data on the screen and also to
serve as the primary point of user interaction. Whenever the data changes,
either due to user interaction (like pressing a button) or external input (like
a network response), the UI should update to reflect those changes.
*Effectively, the UI is a visual representation of the application state as
retrieved from the data layer.*

However, the application data you get from the data layer is usually in a
different format than the information you need to display. For example, you
might only need part of the data for the UI, or you might need to merge two
different data sources to present information that is relevant to the user.
Regardless of the logic you apply, you need to pass the UI all the information
it needs to render fully. *The UI layer is the pipeline that converts
application data changes to a form that the UI can present and then displays
it.*

## Expose UI state

After you define your UI state and determine how you will manage the production
of that state, the next step is to present the produced state to the UI. Because
you're using UDF to manage the production of state, you can consider the
produced state to be a stream—in other words, multiple versions of the state
will be produced over time. As a result, you should expose the UI state in an
observable data holder like `LiveData` or `StateFlow`. The reason for this is so
that the UI can react to any changes made in the state without having to
manually pull data directly from the ViewModel. These types also have the
benefit of always having the latest version of the UI state cached, which is
useful for quick state restoration after configuration changes.

```
class NewsViewModel(...) : ViewModel() {

    val uiState: StateFlow<NewsUiState> = …
}
```

A common way of creating a stream of `UiState` is by exposing a backing mutable
stream as an immutable stream from the ViewModel—for example, exposing a
`MutableStateFlow<UiState>` as a `StateFlow<UiState>`.

```
class NewsViewModel(...) : ViewModel() {

    private val _uiState = MutableStateFlow(NewsUiState())
    val uiState: StateFlow<NewsUiState> = _uiState.asStateFlow()

    ...

}
```

The ViewModel can then expose methods that internally mutate the state,
publishing updates for the UI to consume. Take, for example, the case where an
asynchronous action needs to be performed; a coroutine can be launched using the
[`viewModelScope`](/topic/libraries/architecture/coroutines#viewmodelscope), and
the mutable state can be updated upon completion.

```
class NewsViewModel(
    private val repository: NewsRepository,
    ...
) : ViewModel() {

    private val _uiState = MutableStateFlow(NewsUiState())
    val uiState: StateFlow<NewsUiState> = _uiState.asStateFlow()

    private var fetchJob: Job? = null

    fun fetchArticles(category: String) {
        fetchJob?.cancel()
        fetchJob = viewModelScope.launch {
            try {
                val newsItems = repository.newsItemsForCategory(category)
                _uiState.update {
                    it.copy(newsItems = newsItems)
                }
            } catch (ioe: IOException) {
                // Handle the error and notify the UI when appropriate.
                _uiState.update {
                    val messages = getMessagesFromThrowable(ioe)
                    it.copy(userMessages = messages)
                }
            }
        }
    }
}
```

## Consume UI state

When consuming observable data holders in the UI, make sure you take the
lifecycle of the UI into consideration. This is important because the UI
shouldn't be observing the UI state when the view isn't being displayed to the
user. To learn more about this topic, see [this blog
post](https://medium.com/androiddevelopers/a-safer-way-to-collect-flows-from-android-uis-23080b1f8bda).
When using `LiveData`, the `LifecycleOwner` implicitly takes care of lifecycle
concerns. When using flows, it's best to handle this with the appropriate
coroutine scope and the `repeatOnLifecycle` API:

```
class NewsActivity : AppCompatActivity() {

    private val viewModel: NewsViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        ...

        lifecycleScope.launch {
            repeatOnLifecycle(Lifecycle.State.STARTED) {
                viewModel.uiState.collect {
                    // Update UI elements
                }
            }
        }
    }
}
```

**Note:** The specific `StateFlow` objects used in this example don't stop
performing work when they have no active collectors, but when you're working
with flows you might not know how they're implemented. Using lifecycle-aware
flow collection lets you make these kinds of changes to the ViewModel flows
later without revisiting downstream collector code.

### Show in-progress operations

A simple way to represent loading states in a `UiState` class is with a
boolean field:

```
data class NewsUiState(
    val isFetchingArticles: Boolean = false,
    ...
)
```

This flag's value represents the presence or absence of a progress bar in the
UI.

```
class NewsActivity : AppCompatActivity() {

    private val viewModel: NewsViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        ...

        lifecycleScope.launch {
            repeatOnLifecycle(Lifecycle.State.STARTED) {
                // Bind the visibility of the progressBar to the state
                // of isFetchingArticles.
                viewModel.uiState
                    .map { it.isFetchingArticles }
                    .distinctUntilChanged()
                    .collect { progressBar.isVisible = it }
            }
        }
    }
}
```

## Animations

In order to provide fluid and smooth top-level navigation transitions, you might
want to wait for the second screen to load data before starting the animation.
The Android view framework provides hooks to delay transitions between fragment
destinations with the
[`postponeEnterTransition()`](/reference/androidx/fragment/app/Fragment#postponeEnterTransition())
and
[`startPostponedEnterTransition()`](/reference/androidx/fragment/app/Fragment#startPostponedEnterTransition())
APIs. These APIs provide a way to ensure that the UI elements on the second
screen (typically an image fetched from the network) are ready to be displayed
before the UI animates the transition to that screen.

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [UI State production](/topic/architecture/ui-layer/state-production)
* [State holders and UI State {:#mad-arch}](/topic/architecture/ui-layer/stateholders)
* [Guide to app architecture](/topic/architecture)