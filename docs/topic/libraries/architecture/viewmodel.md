---
title: https://developer.android.com/topic/libraries/architecture/viewmodel
url: https://developer.android.com/topic/libraries/architecture/viewmodel
source: md.txt
---

# ViewModel overview

# ViewModel overviewPart of[Android Jetpack](https://developer.android.com/jetpack).

<br />

Try with Kotlin Multiplatform  
Kotlin Multiplatform allows sharing the business logic with other platforms. Learn how to set up and work with ViewModel in KMP  
[Set up ViewModel for KMP →](https://developer.android.com/kotlin/multiplatform/viewmodel)  
![](https://developer.android.com/static/images/android-kmp-logo.png)

<br />

The[`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel)class is a[business logic or screen level state holder](https://developer.android.com/topic/architecture/ui-layer/stateholders). It exposes state to the UI and encapsulates related business logic. Its principal advantage is that it caches state and persists it through configuration changes. This means that your UI doesn't have to fetch data again when navigating between activities, or following configuration changes, such as when rotating the screen.
| **Objective:** This guide explains the basics of ViewModels, how they fit into[Modern Android Development](https://developer.android.com/modern-android-development), and how you can implement them in your app.

For more information on state holders, see the[state holders](https://developer.android.com/topic/architecture/ui-layer/stateholders)guidance. Similarly, for more information on the UI layer generally, see the[UI layer](https://developer.android.com/topic/architecture/ui-layer)guidance.

## ViewModel benefits

The alternative to a ViewModel is a plain class that holds the data you display in your UI. This can become a problem when navigating between activities or Navigation destinations. Doing so destroys that data if you don't store it using the[saving instance state mechanism](https://developer.android.com/topic/libraries/architecture/saving-states#onsaveinstancestate). ViewModel provides a convenient API for data persistence that resolves this issue.

The key benefits of the ViewModel class are essentially two:

- It allows you to persist UI state.
- It provides access to business logic.

| **Note:** ViewModel fully supports integration with key Jetpack libraries such as[Hilt](https://developer.android.com/training/dependency-injection/hilt-android)and[Navigation](https://developer.android.com/guide/navigation), as well as[Compose](https://developer.android.com/jetpack/compose).

### Persistence

ViewModel allows persistence through both the state that a ViewModel holds, and the operations that a ViewModel triggers. This caching means that you don't have to fetch data again through common configuration changes, such as a screen rotation.

#### Scope

When you instantiate a ViewModel, you pass it an object that implements the[`ViewModelStoreOwner`](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelStoreOwner)interface. This may be a Navigation destination, Navigation graph, activity, fragment, or any other type that implements the interface. Your ViewModel is then scoped to the[Lifecycle](https://developer.android.com/reference/androidx/lifecycle/Lifecycle)of the`ViewModelStoreOwner`. It remains in memory until its`ViewModelStoreOwner`goes away permanently.

A range of classes are either direct or indirect subclasses of the`ViewModelStoreOwner`interface. The direct subclasses are[`ComponentActivity`](https://developer.android.com/reference/androidx/activity/ComponentActivity),[`Fragment`](https://developer.android.com/reference/androidx/fragment/app/Fragment), and[`NavBackStackEntry`](https://developer.android.com/reference/androidx/navigation/NavBackStackEntry). For a full list of indirect subclasses, see the[`ViewModelStoreOwner`reference](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelStoreOwner).

When the fragment or activity to which the ViewModel is scoped is destroyed, asynchronous work continues in the ViewModel that is scoped to it. This is the key to persistence.

For more information, see the section below on[ViewModel lifecycle](https://developer.android.com/topic/libraries/architecture/viewmodel#lifecycle).

#### SavedStateHandle

[SavedStateHandle](https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-savedstate)allows you to persist data not just through configuration changes, but across process recreation. That is, it enables you to keep the UI state intact even when the user closes the app and opens it at a later time.

### Access to business logic

Even though the vast majority of[business logic](https://developer.android.com/topic/architecture/ui-layer/stateholders#business-logic)is present in the data layer, the UI layer can also contain business logic. This can be the case when combining data from multiple repositories to create the screen UI state, or when a particular type of data doesn't require a data layer.

ViewModel is the right place to handle business logic in the UI layer. The ViewModel is also in charge of handling events and delegating them to other layers of the hierarchy when business logic needs to be applied to modify application data.

## Jetpack Compose

When using Jetpack Compose, ViewModel is the primary means of exposing screen UI state to your composables. In a hybrid app, activities and fragments simply host your composable functions. This is a shift from past approaches, where it wasn't that simple and intuitive to create reusable pieces of UI with activities and fragments, which caused them to be much more active as UI controllers.

The most important thing to keep in mind when using ViewModel with Compose is that you cannot scope a ViewModel to a composable. This is because a composable is not a`ViewModelStoreOwner`. Two instances of the same composable in the Composition, or two different composables accessing the same ViewModel type under the same`ViewModelStoreOwner`would receive the*same*instance of the ViewModel, which often is not the expected behavior.

To get the[benefits](https://developer.android.com/topic/libraries/architecture/viewmodel#viewmodel-benefits)of ViewModel in Compose, host each screen in a Fragment or Activity, or use Compose Navigation and use ViewModels in composable functions as close as possible to the Navigation destination. That is because you can scope a ViewModel to Navigation destinations, Navigation graphs, Activities, and Fragments.

For more information, see the guide on[state hoisting](https://developer.android.com/jetpack/compose/state-hoisting#viewmodels-as-state-owner)for Jetpack Compose.

## Implement a ViewModel

The following is an example implementation of a ViewModel for a screen that allows the user to roll dice.
**Important:** In this example, the responsibility of acquiring and holding the list of users sits with the ViewModel, not an Activity or Fragment directly.  

### Kotlin

    data class DiceUiState(
        val firstDieValue: Int? = null,
        val secondDieValue: Int? = null,
        val numberOfRolls: Int = 0,
    )

    class DiceRollViewModel : ViewModel() {

        // Expose screen UI state
        private val _uiState = MutableStateFlow(DiceUiState())
        val uiState: StateFlow<DiceUiState> = _uiState.asStateFlow()

        // Handle business logic
        fun rollDice() {
            _uiState.update { currentState ->
                currentState.copy(
                    firstDieValue = Random.nextInt(from = 1, until = 7),
                    secondDieValue = Random.nextInt(from = 1, until = 7),
                    numberOfRolls = currentState.numberOfRolls + 1,
                )
            }
        }
    }

### Java

    public class DiceUiState {
        private final Integer firstDieValue;
        private final Integer secondDieValue;
        private final int numberOfRolls;

        // ...
    }

    public class DiceRollViewModel extends ViewModel {

        private final MutableLiveData<DiceUiState> uiState =
            new MutableLiveData(new DiceUiState(null, null, 0));
        public LiveData<DiceUiState> getUiState() {
            return uiState;
        }

        public void rollDice() {
            Random random = new Random();
            uiState.setValue(
                new DiceUiState(
                    random.nextInt(7) + 1,
                    random.nextInt(7) + 1,
                    uiState.getValue().getNumberOfRolls() + 1
                )
            );
        }
    }

You can then access the ViewModel from an activity as follows:  

### Kotlin

    import androidx.activity.viewModels

    class DiceRollActivity : AppCompatActivity() {

        override fun onCreate(savedInstanceState: Bundle?) {
            // Create a ViewModel the first time the system calls an activity's onCreate() method.
            // Re-created activities receive the same DiceRollViewModel instance created by the first activity.

            // Use the 'by viewModels()' Kotlin property delegate
            // from the activity-ktx artifact
            val viewModel: DiceRollViewModel by viewModels()
            lifecycleScope.launch {
                repeatOnLifecycle(Lifecycle.State.STARTED) {
                    viewModel.uiState.collect {
                        // Update UI elements
                    }
                }
            }
        }
    }

### Java

    public class MyActivity extends AppCompatActivity {
        public void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);

            // Create a ViewModel the first time the system calls an activity's onCreate() method.
            // Re-created activities receive the same MyViewModel instance created by the first activity.
            DiceRollViewModel model = new ViewModelProvider(this).get(DiceRollViewModel.class);
            model.getUiState().observe(this, uiState -> {
                // update UI
            });
        }
    }

### Jetpack Compose

    import androidx.lifecycle.viewmodel.compose.viewModel

    // Use the 'viewModel()' function from the lifecycle-viewmodel-compose artifact
    @Composable
    fun DiceRollScreen(
        viewModel: DiceRollViewModel = viewModel()
    ) {
        val uiState by viewModel.uiState.collectAsStateWithLifecycle()
        // Update UI elements
    }

| **Caution:** A[`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel)usually shouldn't reference a view,[`Lifecycle`](https://developer.android.com/reference/androidx/lifecycle/Lifecycle), or any class that may hold a reference to the activity context. Because the ViewModel lifecycle is larger than the UI's, holding a lifecycle-related API in the ViewModel could cause memory leaks.
| **Note:** To import[`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel)into your Android project, see the instructions for declaring dependencies in the[Lifecycle release notes](https://developer.android.com/jetpack/androidx/releases/lifecycle#declaring_dependencies).

### Use coroutines with ViewModel

`ViewModel`includes support for Kotlin coroutines. It is able to persist asynchronous work in the same manner as it persists UI state.

For more information, see[Use Kotlin coroutines with Android Architecture Components](https://developer.android.com/topic/libraries/architecture/coroutines).

## The lifecycle of a ViewModel

The lifecycle of a[`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel)is tied directly to its scope. A`ViewModel`remains in memory until the[`ViewModelStoreOwner`](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelStoreOwner)to which it is scoped disappears. This may occur in the following contexts:

- In the case of an activity, when it finishes.
- In the case of a fragment, when it detaches.
- In the case of a Navigation entry, when it's removed from the back stack.

This makes ViewModels a great solution for storing data that survives configuration changes.

Figure 1 illustrates the various lifecycle states of an activity as it undergoes a rotation and then is finished. The illustration also shows the lifetime of the[`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel)next to the associated activity lifecycle. This particular diagram illustrates the states of an activity. The same basic states apply to the lifecycle of a fragment.

![Illustrates the lifecycle of a ViewModel as an activity changes state.](https://developer.android.com/static/images/topic/libraries/architecture/viewmodel-lifecycle.png)

You usually request a[`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel)the first time the system calls an activity object's[`onCreate()`](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle))method. The system may call[`onCreate()`](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle))several times throughout the existence of an activity, such as when a device screen is rotated. The[`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel)exists from when you first request a[`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel)until the activity is finished and destroyed.

### Clearing ViewModel dependencies

The ViewModel calls the[`onCleared`](https://developer.android.com/reference/androidx/lifecycle/ViewModel#onCleared())method when the`ViewModelStoreOwner`destroys it in the course of its lifecycle. This allows you to clean up any work or dependencies that follows the ViewModel's lifecycle.

The following example shows an alternative to[`viewModelScope`](https://developer.android.com/topic/libraries/architecture/coroutines#viewmodelscope).`viewModelScope`is a built-in[`CoroutineScope`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/)that automatically follows the ViewModel's lifecycle. The ViewModel uses it to trigger business-related operations. If you want to use a custom scope instead of`viewModelScope`for[easier testing](https://developer.android.com/kotlin/coroutines/test), the ViewModel can receive a`CoroutineScope`as a dependency in its constructor. When the`ViewModelStoreOwner`clears the ViewModel at the end of its lifecycle, the ViewModel also cancels the`CoroutineScope`.  

    class MyViewModel(
        private val coroutineScope: CoroutineScope =
            CoroutineScope(SupervisorJob() + Dispatchers.Main.immediate)
    ) : ViewModel() {

        // Other ViewModel logic ...

        override fun onCleared() {
            coroutineScope.cancel()
        }
    }

From lifecycle[version 2.5](https://developer.android.com/jetpack/androidx/releases/lifecycle#version_25_2)and above, you can pass one or more`Closeable`objects to the ViewModel's constructor that automatically closes when the ViewModel instance is cleared.  

    class CloseableCoroutineScope(
        context: CoroutineContext = SupervisorJob() + Dispatchers.Main.immediate
    ) : Closeable, CoroutineScope {
        override val coroutineContext: CoroutineContext = context
        override fun close() {
            coroutineContext.cancel()
       }
    }

    class MyViewModel(
        private val coroutineScope: CoroutineScope = CloseableCoroutineScope()
    ) : ViewModel(coroutineScope) {
        // Other ViewModel logic ...
    }

## Best practices

The following are several key best practices you should follow when implementing ViewModel:

- Because of[their scoping](https://developer.android.com/topic/libraries/architecture/viewmodel#lifecycle), use ViewModels as implementation details of a screen level state holder. Don't use them as state holders of reusable UI components such as chip groups or forms. Otherwise, you'd get the same ViewModel instance in different usages of the same UI component under the same ViewModelStoreOwner unless you use an explicit view model key per chip.
- ViewModels shouldn't know about the UI implementation details. Keep the names of the methods the ViewModel API exposes and those of the UI state fields as generic as possible. In this way, your ViewModel can accommodate any type of UI: a mobile phone, foldable, tablet, or even a Chromebook!
- As they can potentially live longer than the`ViewModelStoreOwner`, ViewModels shouldn't hold any references of lifecycle-related APIs such as the`Context`or`Resources`to prevent memory leaks.
- Don't pass ViewModels to other classes, functions or other UI components. Because the platform manages them, you should keep them as close to it as you can. Close to your Activity, fragment, or screen level composable function. This prevents lower level components from accessing more data and logic than they need.

## Further information

As your data grows more complex, you might choose to have a separate class just to load the data. The purpose of[`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel)is to encapsulate the data for a UI controller to let the data survive configuration changes. For information about how to load, persist, and manage data across configuration changes, see[Saved UI States](https://developer.android.com/topic/libraries/architecture/saving-states).

The[Guide to Android App Architecture](https://developer.android.com/topic/libraries/architecture/guide#fetching_data)suggests building a repository class to handle these functions.

## Additional resources

For further information about the`ViewModel`class, consult the following resources.

### Documentation

- [UI layer](https://developer.android.com/topic/architecture/ui-layer)
- [UI Events](https://developer.android.com/topic/architecture/ui-layer/events)
- [State holders and UI State](https://developer.android.com/topic/architecture/ui-layer/stateholders)
- [State production](https://developer.android.com/topic/architecture/ui-layer/state-production)
- [Data layer](https://developer.android.com/topic/architecture/data-layer)

### Samples

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Use Kotlin coroutines with lifecycle-aware components](https://developer.android.com/topic/libraries/architecture/coroutines)
- [Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states)
- [Load and display paged data](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data)