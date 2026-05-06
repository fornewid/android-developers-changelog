---
title: ViewModel overview (Views)  |  Android Developers
url: https://developer.android.com/topic/libraries/architecture/views/viewmodel
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)
* [Guides](https://developer.android.com/topic/architecture/views/recommendations-views)

Stay organized with collections

Save and categorize content based on your preferences.





# ViewModel overview (Views)

[Concepts and Jetpack Compose implementationarrow\_forward](/topic/libraries/architecture/viewmodel)

The [`ViewModel`](/reference/androidx/lifecycle/ViewModel) class is a [business logic or screen level state
holder](/topic/architecture/ui-layer/stateholders). It exposes state to the UI and encapsulates related business logic.
Its principal advantage is that it caches state and persists it through
configuration changes. This means that your UI doesn't have to fetch data again
when navigating between activities, or following configuration changes, such as
when rotating the screen.

## ViewModel benefits

The alternative to a ViewModel is a plain class that holds the data you display
in your UI. This can become a problem when navigating between activities or
Navigation destinations. Doing so destroys that data if you don't store it
using the [saved instance state mechanism](/topic/libraries/architecture/saving-states#onsaveinstancestate). ViewModel provides a convenient
API for data persistence that resolves this issue.

The key benefits of the ViewModel class are essentially two:

* It lets you persist UI state.
* It provides access to business logic.

### Scope

When you instantiate a ViewModel, you pass it an object that implements the
[`ViewModelStoreOwner`](/reference/kotlin/androidx/lifecycle/ViewModelStoreOwner) interface. This may be a Navigation destination,
Navigation graph, activity, fragment, or any other type that implements the
interface. Your ViewModel is then scoped to the [`Lifecycle`](/reference/androidx/lifecycle/Lifecycle) of the
`ViewModelStoreOwner`. It remains in memory until its `ViewModelStoreOwner`
goes away permanently.

A range of classes are either direct or indirect subclasses of the
`ViewModelStoreOwner` interface. The direct subclasses are
[`ComponentActivity`](/reference/androidx/activity/ComponentActivity), [`Fragment`](/reference/androidx/fragment/app/Fragment), and [`NavBackStackEntry`](/reference/androidx/navigation/NavBackStackEntry).
For a full list of indirect subclasses, see the
[`ViewModelStoreOwner` reference](/reference/kotlin/androidx/lifecycle/ViewModelStoreOwner).

## Implement a ViewModel

The following is an example implementation of a ViewModel for a screen that
allows the user to roll dice.

**Important:** In this example, the responsibility of acquiring and holding the list
of users sits with the ViewModel, not an Activity or Fragment directly.

### Kotlin

```
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
```

### Java

```
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
```

You can then access the ViewModel from an activity as follows:

### Kotlin

```
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
```

### Java

```
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
```

**Caution:** A [`ViewModel`](/reference/androidx/lifecycle/ViewModel) usually shouldn't reference a view,
[`Lifecycle`](/reference/androidx/lifecycle/Lifecycle), or any class that may hold a reference to the activity
context. Because the ViewModel lifecycle is larger than the UI's, holding a
lifecycle-related API in the ViewModel could cause memory leaks.**Note:** To import [`ViewModel`](/reference/androidx/lifecycle/ViewModel) into your Android project, see the instructions
for declaring dependencies in the [Lifecycle release notes](/jetpack/androidx/releases/lifecycle#declaring_dependencies).


## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Use Kotlin coroutines with lifecycle-aware components](/topic/libraries/architecture/coroutines)
* [Save UI states](/topic/libraries/architecture/saving-states)
* [Load and display paged data](/topic/libraries/architecture/paging/v3-paged-data)