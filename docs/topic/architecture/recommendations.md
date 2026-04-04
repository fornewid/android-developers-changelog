---
title: https://developer.android.com/topic/architecture/recommendations
url: https://developer.android.com/topic/architecture/recommendations
source: md.txt
---

This page presents several [Architecture](https://developer.android.com/topic/architecture) best practices and recommendations.
Adopt them to improve your app's quality, robustness, and scalability. They also
make it easier to maintain and test your app.

> [!NOTE]
> **Note:** Treat the recommendations in the document as recommendations and not strict requirements. Adapt them to your app as needed.

The best practices below are grouped by topic. Each has a priority that reflects
how strong the recommendation is. The list of priorities is as follows:

- **Strongly recommended:** Implement this practice unless it clashes fundamentally with your approach.
- **Recommended:** This practice is likely to improve your app.
- **Optional:** This practice can improve your app in certain circumstances.

> [!NOTE]
> **Note:** To understand these recommendations, make sure you are familiar with the [Architecture guidance](https://developer.android.com/topic/architecture).

## Layered architecture

Our recommended [layered architecture](https://developer.android.com/topic/architecture?gclid=CjwKCAjw6raYBhB7EiwABge5Klm_5PN8nJF0Jrb_ymrPP0JAEsbmemmGv_nsn0nBQKQtQMCBuvjehRoC7qcQAvD_BwE&gclsrc=aw.ds#recommended-app-arch) favors separation of concerns. It
drives UI from data models, complies with the single source of truth principle,
and follows [unidirectional data flow](https://developer.android.com/topic/architecture?gclid=CjwKCAjw6raYBhB7EiwABge5Klm_5PN8nJF0Jrb_ymrPP0JAEsbmemmGv_nsn0nBQKQtQMCBuvjehRoC7qcQAvD_BwE&gclsrc=aw.ds#unidirectional-data-flow) principles. Here are some best
practices for layered architecture:

| Recommendation | Description |
|---|---|
| Use a clearly defined [data layer](https://developer.android.com/jetpack/guide/data-layer). **Strongly recommended** | The [data layer](https://developer.android.com/jetpack/guide/data-layer) exposes application data to the rest of the app and contains the vast majority of your app's business logic. - Create [repositories](https://developer.android.com/topic/architecture/data-layer#architecture) even if they contain only a single data source. - In small apps, you can choose to place data layer types in a `data` package or module. |
| Use a clearly defined [UI layer](https://developer.android.com/jetpack/guide/ui-layer). **Strongly recommended** | The [UI layer](https://developer.android.com/jetpack/guide/ui-layer) displays the application data on the screen and serves as the primary point of user interaction. [Jetpack Compose](https://developer.android.com/develop/ui/compose/documentation) is the recommended modern toolkit for building your app's UI. - In small apps, you can choose to place data layer types in a `ui` package or module. For more information on UI layer best practices, see [UI layer](https://developer.android.com/topic/architecture/recommendations#ui-layer). |
| Expose application data from the [data layer](https://developer.android.com/jetpack/guide/data-layer) using a repository. **Strongly recommended** | Make sure components in the UI layer such as composables or ViewModels don't interact directly with a data source. Examples of data sources include: - Databases, DataStore, SharedPreferences, Firebase APIs. - GPS location providers. - Bluetooth data providers. - Network connectivity status providers. |
| Use [coroutines and flows](https://developer.android.com/kotlin/coroutines?gclid=CjwKCAjwhNWZBhB_EiwAPzlhNtReVIBfrUFBUt6SqZz3YLezP9YEiGuBube4YSTrOF-0ovxzpNGNaRoCiYsQAvD_BwE&gclsrc=aw.ds). **Strongly recommended** | Use [coroutines and flows](https://developer.android.com/kotlin/coroutines?gclid=CjwKCAjwhNWZBhB_EiwAPzlhNtReVIBfrUFBUt6SqZz3YLezP9YEiGuBube4YSTrOF-0ovxzpNGNaRoCiYsQAvD_BwE&gclsrc=aw.ds) to communicate between layers. For more information on coroutines best practices, see [Best practices for coroutines in Android](https://developer.android.com/kotlin/coroutines/coroutines-best-practices). |
| Use a [domain layer](https://developer.android.com/jetpack/guide/domain-layer). **Recommended in big apps** | Use a [domain layer](https://developer.android.com/jetpack/guide/domain-layer) with use cases if you need to reuse business logic that interacts with the data layer across multiple ViewModels, or you want to simplify the business logic complexity of a particular ViewModel |

## UI layer

The role of the [UI layer](https://developer.android.com/topic/architecture/ui-layer) is to display the application data on the screen
and serve as the primary point of user interaction. Here are some best practices
for the UI layer:

| Recommendation | Description |
|---|---|
| Follow [Unidirectional Data Flow (UDF)](https://developer.android.com/jetpack/compose/architecture#udf). **Strongly recommended** | Follow [Unidirectional Data Flow (UDF)](https://developer.android.com/jetpack/compose/architecture#udf) principles, where ViewModels expose UI state using the observer pattern and receive actions from the UI through method calls. |
| Use [AAC ViewModels](https://developer.android.com/topic/libraries/architecture/viewmodel) if their benefits apply to your app. **Strongly recommended** | Use [AAC ViewModels](https://developer.android.com/topic/libraries/architecture/viewmodel) to [handle business logic](https://developer.android.com/jetpack/guide/ui-layer#logic-types), and fetch application data to expose UI state to the UI. For more information on ViewModel best practices, see [Architecture recommendations.](https://developer.android.com/topic/architecture/recommendations#viewmodel) For more information on the benefits of ViewModels, see [The ViewModel as a business logic state holder.](https://developer.android.com/topic/architecture/ui-layer/stateholders#viewmodel-as) |
| Use lifecycle-aware UI state collection. **Strongly recommended** | Collect UI state from the UI using the appropriate lifecycle-aware coroutine builder, [`collectAsStateWithLifecycle`](https://developer.android.com/reference/kotlin/androidx/lifecycle/compose/collectAsStateWithLifecycle.composable#(kotlinx.coroutines.flow.StateFlow).collectAsStateWithLifecycle(androidx.lifecycle.LifecycleOwner,androidx.lifecycle.Lifecycle.State,kotlin.coroutines.CoroutineContext)). Read more about [`collectAsStateWithLifecycle`](https://medium.com/androiddevelopers/consuming-flows-safely-in-jetpack-compose-cde014d0d5a3). |
| Do not send events from the ViewModel to the UI. **Strongly recommended** | Process the event immediately in the ViewModel and cause a state update with the result of handling the event. For more information about UI events, see [Handle ViewModel events](https://developer.android.com/topic/architecture/ui-layer/events#handle-viewmodel-events). |
| Use a single-activity application. **Strongly recommended** | Use [Navigation 3](https://developer.android.com/guide/navigation/navigation-3) to navigate between screens and deep link to your app if your app has more than one screen. |
| Use [Jetpack Compose](https://developer.android.com/jetpack/compose). **Strongly recommended** | Use [Jetpack Compose](https://developer.android.com/jetpack/compose) to build new apps for phones, tablets, foldables, and Wear OS. |

The following snippet outlines how to collect the UI state in a lifecycle-aware
manner:

      @Composable
      fun MyScreen(
          viewModel: MyViewModel = viewModel()
      ) {
          val uiState by viewModel.uiState.collectAsStateWithLifecycle()
      }

## ViewModel

[ViewModels](https://developer.android.com/topic/architecture/ui-layer/stateholders#business-logic) are responsible for providing the UI state and accessing the
data layer. Here are some best practices for ViewModels:

| Recommendation | Description |
|---|---|
| Keep ViewModels independent of the Android lifecycle. **Strongly recommended** | In ViewModels, don't hold a reference to any lifecycle-related type. Don't pass `Activity`, `Context` or `Resources` as a dependency. If something needs a `Context` in the ViewModel, carefully evaluate if that is in the right layer. |
| Use [coroutines and flows](https://developer.android.com/kotlin/coroutines?gclid=CjwKCAjwhNWZBhB_EiwAPzlhNtReVIBfrUFBUt6SqZz3YLezP9YEiGuBube4YSTrOF-0ovxzpNGNaRoCiYsQAvD_BwE&gclsrc=aw.ds). **Strongly recommended** | The ViewModel interacts with the data or domain layers using the following: - Kotlin flows for receiving application data - `suspend` functions for performing actions using [`viewModelScope`](https://developer.android.com/topic/libraries/architecture/coroutines#viewmodelscope) |
| Use ViewModels at screen level. **Strongly recommended** | Do not use ViewModels in reusable pieces of UI. You should use ViewModels in: - Screen-level composables, - Activities/Fragments in Views, - Destinations or graphs when using [Jetpack Navigation](https://developer.android.com/guide/navigation). |
| Use [plain state holder classes](https://developer.android.com/topic/architecture/ui-layer/stateholders#ui-logic) in reusable UI components. **Strongly recommended** | Use [plain state holder classes](https://developer.android.com/topic/architecture/ui-layer/stateholders#ui-logic) for handling complexity in reusable UI components. When you do this, the state can be hoisted and controlled externally. |
| Do not use [`AndroidViewModel`](https://developer.android.com/reference/androidx/lifecycle/AndroidViewModel). **Recommended** | Use the [`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel) class, not [`AndroidViewModel`](https://developer.android.com/reference/androidx/lifecycle/AndroidViewModel). Don't use the `Application` class in the ViewModel. Instead, move the dependency to the UI or the data layer. |
| Expose a UI state. **Recommended** | Make your ViewModels expose data to the UI through a single property called `uiState`. If the UI shows multiple, unrelated pieces of data, the VM can [expose multiple UI state properties](https://developer.android.com/jetpack/guide/ui-layer#additional-considerations). - Make `uiState` a `StateFlow`. - Create the `uiState` using the [`stateIn`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/state-in.html) operator with the [`WhileSubscribed(5000)`](https://medium.com/androiddevelopers/migrating-from-livedata-to-kotlins-flow-379292f419fb) policy if the data comes as a stream of data from other layers of the hierarchy. (See [this code example](https://github.com/android/compose-samples/blob/main/JetNews/app/src/main/java/com/example/jetnews/ui/interests/InterestsViewModel.kt#L56).) - For simpler cases with no streams of data coming from the data layer, it's acceptable to use a `MutableStateFlow` exposed as an immutable `StateFlow`. - You can choose to have the `${Screen}UiState` as a data class that can contain data, errors, and loading signals. This class can also be a sealed class if the different states are exclusive. |

The following snippet outlines how to expose UI state from a ViewModel:

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

## Lifecycle

Follow best practices for working with the [Activity
lifecycle](https://developer.android.com/guide/components/activities/activity-lifecycle):

| Recommendation | Description |
|---|---|
| Use lifecycle-aware effects in composables instead of overriding `Activity` lifecycle callbacks. **Strongly recommended** | Don't override `Activity` lifecycle methods, such as `onResume`, to run UI-related tasks. Instead, use Compose's [LifecycleEffects](https://developer.android.com/topic/libraries/architecture/compose)or lifecycle-aware coroutine scopes: - Use `https://developer.android.com/topic/libraries/architecture/compose#lifecyclestarteffect` to perform synchronous work when your activity starts and stops. - Use `https://developer.android.com/topic/libraries/architecture/compose#lifecycleresumeeffect` to perform synchronous work when your activity resumes and pauses. - Use `https://developer.android.com/topic/libraries/architecture/coroutines#restart` to perform asynchronous work in response to lifecycle events. - Collect asynchronous data from Flows using `https://developer.android.com/reference/kotlin/androidx/lifecycle/compose/package-summary#extension-functions`. |

The following snippet outlines how to perform operations given a certain
Lifecycle state:

      @Composable
      fun LocationChangedEffect(
        locationManager: LocationManager,
        onLocationChanged: (Location) -> Unit
      ) {
        val currentOnLocationChanged by rememberUpdatedState(onLocationChanged)

        LifecycleStartEffect(locationManager) {
            val listener = LocationListener { newLocation ->
                currentOnLocationChanged(newLocation)
            }

            try {
                locationManager.requestLocationUpdates(
                    LocationManager.GPS_PROVIDER,
                    1000L,
                    1f,
                    listener,
                )
            } catch (e: SecurityException) {
                // TODO: Handle missing permissions
            }

            onStopOrDispose {
                locationManager.removeUpdates(listener)
            }
        }
      }

## Handle dependencies

Follow best practices when managing dependencies
between components:

| Recommendation | Description |
|---|---|
| Use [dependency injection](https://developer.android.com/training/dependency-injection). **Strongly recommended** | Use [dependency injection](https://developer.android.com/training/dependency-injection) best practices, mainly [constructor injection](https://developer.android.com/training/dependency-injection#what-is-di) when possible. |
| Scope to a component when necessary. **Strongly recommended** | Scope to a [dependency container](https://developer.android.com/training/dependency-injection/manual#dependencies-container) when the type contains mutable data that needs to be shared or the type is expensive to initialize and is widely used in the app. |
| Use [Hilt](https://developer.android.com/training/dependency-injection/hilt-android). **Recommended** | Use [Hilt](https://developer.android.com/training/dependency-injection/hilt-android) or [manual dependency injection](https://developer.android.com/training/dependency-injection/manual) in simple apps. Use [Hilt](https://developer.android.com/training/dependency-injection/hilt-android) if your project is complex enough-for example, if it includes any of the following: - Multiple screens with ViewModels - Uses WorkManager - Has ViewModels scoped to the navigation back stack |

## Testing

The following are some best practices for [testing](https://developer.android.com/training/testing/fundamentals):

| Recommendation | Description |
|---|---|
| [Know what to test](https://developer.android.com/training/testing/fundamentals/what-to-test). **Strongly recommended** | Unless the project is as simple as a "hello world" app, test it. At minimum, include the following: - Unit tests for ViewModels, including Flows - Unit tests for data layer entities-that is, repositories and data sources - UI navigation tests that are useful as regression tests in CI |
| Prefer fakes to mocks. **Strongly recommended** | For more information on using fakes, see [Use test doubles in Android](https://developer.android.com/training/testing/fundamentals/test-doubles). |
| Test StateFlows. **Strongly recommended** | When testing `StateFlow`, do the following: - [Assert on the `value` property](https://developer.android.com/kotlin/flow/test#stateflows) whenever possible. - Use [`WhileSubscribed`](https://developer.android.com/kotlin/flow/test#statein). |

For more information, see [What to test in Android](https://developer.android.com/training/testing/fundamentals/what-to-test) and [Test your Compose layout](https://developer.android.com/develop/ui/compose/testing).

## Models

Observe these best practices when developing models in your apps:

| Recommendation | Description |
|---|---|
| Create a model per layer in complex apps. **Recommended** | In complex apps, create new models in different layers or components when it makes sense. Consider the following examples: - A remote data source can map the model that it receives through the network to a simpler class with only the data the app needs. - Repositories can map DAO models to simpler data classes with just the information the UI layer needs. - ViewModel can include data layer models in `UiState` classes. |

## Naming conventions

When naming your codebase, you should be aware of the following best practices:

| Recommendation | Description |
|---|---|
| Naming methods. **Optional** | Use verb phrases to name methods-for example, `makePayment()`. |
| Naming properties. **Optional** | Use noun phrases to name properties-for example, `inProgressTopicSelection`. |
| Naming streams of data. **Optional** | When a class exposes a Flow stream or any other stream, the naming convention is `get{model}Stream`. For example, `getAuthorStream(): Flow<Author>`. If the function returns a list of models, use the plural model name: `getAuthorsStream(): Flow<List<Author>>`. |
| Naming interfaces implementations. **Optional** | Use meaningful names for the implementations of interfaces. Use `Default` as the prefix if a better name cannot be found. For example, for a `NewsRepository` interface, you might have an `OfflineFirstNewsRepository`, or `InMemoryNewsRepository`. If you cannot find a good name, use `DefaultNewsRepository`. Prefix fake implementations with `Fake`, as in `FakeAuthorsRepository`. |

## Additional resources

For more information about Android architecture, see the following additional
resources:

### Documentation

- [Compose UI Architecture](https://developer.android.com/develop/ui/compose/architecture)
- [Jetpack Compose architectural layering](https://developer.android.com/develop/ui/compose/layering)

### Views content

- [Recommendations for Android architecture (Views)](https://developer.android.com/topic/architecture/views/recommendations-views)