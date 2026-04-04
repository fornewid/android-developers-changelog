---
title: Recommendations for Android architecture (Views)  |  Android Developers
url: https://developer.android.com/topic/architecture/views/recommendations-views
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)
* [Guides](https://developer.android.com/topic/architecture/views/recommendations-views)

# Recommendations for Android architecture (Views) Stay organized with collections Save and categorize content based on your preferences.




[Concepts and Jetpack Compose implementationarrow\_forward](/topic/architecture/recommendations)

This page presents several architecture best practices and recommendations.
Adopt them to improve your app's quality, robustness, and scalability. They also
make it easier to maintain and test your app.

**Note:** You should treat the recommendations in the document as
recommendations and not strict requirements. Adapt them to your app as needed.

## UI layer

The role of the [UI layer](/topic/architecture/ui-layer) is to display the application data on the screen
and serve as the primary point of user interaction. Here are some best practices
for the UI layer:

|  |  |
| --- | --- |
| **Recommendation** | **Description** |
| Follow [Unidirectional Data Flow (UDF)](/jetpack/compose/architecture#udf).  Strongly recommended | Follow [Unidirectional Data Flow (UDF)](/jetpack/compose/architecture#udf) principles, where ViewModels expose UI state using the observer pattern and receive actions from the UI through method calls. |

* You should create [repositories](/topic/architecture/data-layer#architecture) even if they only contain a single data source.
* In small apps, you can choose to place data layer types in a `data` package or module.

| Use [AAC ViewModels](/topic/libraries/architecture/viewmodel) if their benefits apply to your app.  Strongly recommended | Use [AAC ViewModels](/topic/libraries/architecture/viewmodel) to [handle business logic](/jetpack/guide/ui-layer#logic-types), and fetch application data to expose UI state to the UI.  See more [ViewModel best practices here](/topic/architecture/recommendations#viewmodel).  See the [benefits of ViewModels here](/topic/architecture/ui-layer/stateholders#viewmodel-as). |
| Use lifecycle-aware UI state collection.  Strongly recommended | Collect UI state from the UI using the appropriate lifecycle-aware coroutine builder, [`repeatOnLifecycle`](/reference/kotlin/androidx/lifecycle/package-summary#(androidx.lifecycle.Lifecycle).repeatOnLifecycle(androidx.lifecycle.Lifecycle.State,kotlin.coroutines.SuspendFunction1)).  Read more about [`repeatOnLifecycle`](https://medium.com/androiddevelopers/a-safer-way-to-collect-flows-from-android-uis-23080b1f8bda). |
| Do not send events from the ViewModel to the UI.  Strongly recommended | Process the event immediately in the ViewModel and cause a state update with the result of handling the event. More about [UI events here](/topic/architecture/ui-layer/events#handle-viewmodel-events). |
| Use a single-activity application.  Recommended | Use [Navigation Fragments](/guide/navigation) to navigate between screens and deep link to your app if your app has more than one screen. |

The following snippet outlines how to collect the UI state in a lifecycle-aware
manner:

```
class MyFragment : Fragment() {

    private val viewModel: MyViewModel by viewModel()

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        viewLifecycleOwner.lifecycleScope.launch {
            viewLifecycleOwner.repeatOnLifecycle(Lifecycle.State.STARTED) {
                viewModel.uiState.collect {
                    // Process item
                }
            }
        }
    }
}
```

## ViewModel

[ViewModels](/topic/architecture/ui-layer/stateholders#business-logic) are responsible for providing the UI state and access to the
data layer. Here are some best practices for ViewModels:

|  |  |
| --- | --- |
| **Recommendation** | **Description** |
| ViewModels should be agnostic of the Android lifecycle.  Strongly recommended | ViewModels shouldn't hold a reference to any Lifecycle-related type. Don't pass `Activity`, `Fragment`, `Context`, or `Resources` as a dependency. If something needs a `Context` in the ViewModel, you should strongly evaluate if that is in the right layer. |
| Use [coroutines and flows](/kotlin/coroutines?gclid=CjwKCAjwhNWZBhB_EiwAPzlhNtReVIBfrUFBUt6SqZz3YLezP9YEiGuBube4YSTrOF-0ovxzpNGNaRoCiYsQAvD_BwE&gclsrc=aw.ds).  Strongly recommended | The ViewModel interacts with the data or domain layers using:   * Kotlin flows for receiving application data, * `suspend` functions to perform actions using [`viewModelScope`](/topic/libraries/architecture/coroutines#viewmodelscope). |
| Use ViewModels at screen level.  Strongly recommended | Do not use ViewModels in reusable pieces of UI. You should use ViewModels in:   * Activities/Fragments in Views * Destinations or graphs when using [Jetpack Navigation](/guide/navigation). |
| Do not use [`AndroidViewModel`](/reference/androidx/lifecycle/AndroidViewModel).  Strongly recommended | Use the [`ViewModel`](/reference/androidx/lifecycle/ViewModel) class, not [`AndroidViewModel`](/reference/androidx/lifecycle/AndroidViewModel). The `Application` class shouldn't be used in the ViewModel. Instead, move the dependency to the UI or the data layer. |
| Expose a UI state.  Recommended | ViewModels should expose data to the UI through a single property called `uiState`. If the UI shows multiple, unrelated pieces of data, the ViewModel can [expose multiple UI state properties](/jetpack/guide/ui-layer#additional-considerations).   * You should make `uiState` a `StateFlow`. * You should create the `uiState` using the [`stateIn`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/state-in.html) operator with the [`WhileSubscribed(5000)`](https://medium.com/androiddevelopers/migrating-from-livedata-to-kotlins-flow-379292f419fb) policy ([example](https://github.com/android/compose-samples/blob/main/JetNews/app/src/main/java/com/example/jetnews/ui/interests/InterestsViewModel.kt#L56)) if the data comes as a stream of data from other layers of the hierarchy. * For simpler cases with no streams of data coming from the data layer, it's acceptable to use a `MutableStateFlow` exposed as an immutable `StateFlow`. * You can choose to have the `${Screen}UiState` as a data class that can contain data, errors and loading signals. This class could also be a sealed class if the different states are exclusive. |

The following snippet outlines how to expose UI state from a ViewModel:

```
@HiltViewModel
class BookmarksViewModel @Inject constructor(
    newsRepository: NewsRepository
) : ViewModel() {

    val feedState: StateFlow<NewsFeedUiState> =
        newsRepository
            .getNewsResourcesStream()
            .mapToFeedState(savedNewsResourcesState)
            .stateIn(
                scope = viewModelScope,
                started = SharingStarted.WhileSubscribed(5_000),
                initialValue = NewsFeedUiState.Loading
            )

    // ...
}
```

## Lifecycle

The following are some best practices for working with the [Android
lifecycle](/guide/components/activities/activity-lifecycle):

|  |  |
| --- | --- |
| Recommendation | Description |
| Do not override lifecycle methods in Activities or Fragments.  Strongly recommended | Do not override lifecycle methods such as `onResume` in Activities or Fragments. Use [`LifecycleObserver`](/reference/androidx/lifecycle/LifecycleObserver) instead. If the app needs to perform work when the lifecycle reaches a certain `Lifecycle.State`, use the [`repeatOnLifecycle`](/reference/kotlin/androidx/lifecycle/package-summary#(androidx.lifecycle.Lifecycle).repeatOnLifecycle(androidx.lifecycle.Lifecycle.State,kotlin.coroutines.SuspendFunction1)) API. |

The following snippet outlines how to perform operations given a certain
Lifecycle state:

```
class MyFragment: Fragment() {
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        viewLifecycleOwner.lifecycle.addObserver(object : DefaultLifecycleObserver {
            override fun onResume(owner: LifecycleOwner) {
                // ...
            }
            override fun onPause(owner: LifecycleOwner) {
                // ...
            }
        }
    }
}
```