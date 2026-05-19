---
title: https://developer.android.com/topic/architecture/views/ui-layer/events-views
url: https://developer.android.com/topic/architecture/views/ui-layer/events-views
source: md.txt
---

[Concepts and Jetpack Compose implementation](https://developer.android.com/topic/architecture/ui-layer/events)

*UI events* are actions that should be handled in the UI layer, either by the UI
or by the ViewModel. The most common type of events are *user events* . The user
produces user events by interacting with the app---for example, by tapping the
screen or by generating gestures. The UI then consumes these events using
callbacks such as `onClick()` listeners.

> [!IMPORTANT]
> **Key terms:**
>
> - **UI:** Code that handles the user interface.
> - **UI events:** Actions that should be handled in the UI layer.
> - **User events:** Events that the user produces when interacting with the app.

The ViewModel is normally responsible for handling the business logic of a
particular user event---for example, the user clicking on a button to refresh some
data. Usually, the ViewModel handles this by exposing functions that the UI can
call. User events might also have UI behavior logic that the UI can handle
directly---for example, navigating to a different screen or showing a
[`Snackbar`](https://developer.android.com/reference/com/google/android/material/snackbar/Snackbar).

While the *business logic* remains the same for the same app on different mobile
platforms or form factors, the *UI behavior logic* is an implementation detail
that might differ between those cases. The [UI layer
page](https://developer.android.com/jetpack/guide/ui-layer#logic-types) defines these types of logic as
follows:

- **Business logic** refers to *what to do* with state changes---for example, making a payment or storing user preferences. The domain and data layers usually handle this logic. Throughout this guide, the [Architecture Components
  ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel) class is used as an opinionated solution for classes that handle business logic.
- **UI behavior logic** or **UI logic** refers to *how to display* state changes---for example, navigation logic or how to show messages to the user. The UI handles this logic.

## Handle user events

The UI can handle user events directly if those events relate to modifying the
state of a UI element---for example, the state of an expandable item. If the event
requires performing business logic, such as refreshing the data on the screen,
it should be processed by the ViewModel.

The following example shows how different buttons are used to expand a UI
element (UI logic) and to refresh the data on the screen (business logic):

    class LatestNewsActivity : AppCompatActivity() {

        private lateinit var binding: ActivityLatestNewsBinding
        private val viewModel: LatestNewsViewModel by viewModels()

        override fun onCreate(savedInstanceState: Bundle?) {
            /* ... */

            // The expand details event is processed by the UI that
            // modifies a View's internal state.
            binding.expandButton.setOnClickListener {
                binding.expandedSection.visibility = View.VISIBLE
            }

            // The refresh event is processed by the ViewModel that is in charge
            // of the business logic.
            binding.refreshButton.setOnClickListener {
                viewModel.refreshNews()
            }
        }
    }

### User events in RecyclerViews

If the action is produced further down the UI tree, like in a `RecyclerView`
item or a custom `View`, the `ViewModel` should still be the one handling user
events.

For example, suppose that all news items from `NewsActivity` contain a bookmark
button. The `ViewModel` needs to know the ID of the bookmarked news item. When
the user bookmarks a news item, the `RecyclerView` adapter does not call the
exposed `addBookmark(newsId)` function from the `ViewModel`, which would require
a dependency on the `ViewModel`. Instead, the `ViewModel` exposes a state object
called `NewsItemUiState` which contains the implementation for handling the
event:

    data class NewsItemUiState(
        val title: String,
        val body: String,
        val bookmarked: Boolean = false,
        val publicationDate: String,
        val onBookmark: () -> Unit
    )

    class LatestNewsViewModel(
        private val formatDateUseCase: FormatDateUseCase,
        private val repository: NewsRepository
    )
        val newsListUiItems = repository.latestNews.map { news ->
            NewsItemUiState(
                title = news.title,
                body = news.body,
                bookmarked = news.bookmarked,
                publicationDate = formatDateUseCase(news.publicationDate),
                // Business logic is passed as a lambda function that the
                // UI calls on click events.
                onBookmark = {
                    repository.addBookmark(news.id)
                }
            )
        }
    }

This way, the `RecyclerView` adapter only works with the data that it needs: the
list of `NewsItemUiState` objects. The adapter doesn't have access to the entire
ViewModel, making it less likely to abuse the functionality exposed by the
ViewModel. When you allow only the activity class to work with the ViewModel,
you separate responsibilities. This ensures that UI-specific objects like views
or `RecyclerView` adapters don't interact directly with the ViewModel.

> [!WARNING]
> **Warning:** It's bad practice to pass the ViewModel into the `RecyclerView` adapter because that tightly couples the adapter with the ViewModel class.

> [!NOTE]
> **Note:** Another common pattern is for the `RecyclerView` adapter to have a `Callback` interface for user actions. In that case, the activity or fragment can handle the binding and call the ViewModel functions directly from the callback interface.

### Naming conventions for user event functions

In this guide, the ViewModel functions that handle user events are named with a
verb based on the action that they handle---for example: `addBookmark(id)` or
`logIn(username, password)`.

## Handle ViewModel events

**UI actions that originate from the ViewModel---ViewModel events---should always
result in a [UI state](https://developer.android.com/jetpack/guide/ui-layer#expose-ui-state) update.** This
complies with the principles of [Unidirectional Data
Flow](https://developer.android.com/jetpack/guide/ui-layer#udf). It makes events reproducible after
configuration changes and guarantees that UI actions won't be lost. Optionally,
you can also make events reproducible after process death if you use the [saved
state module](https://developer.android.com/topic/libraries/architecture/viewmodel-savedstate).

Mapping UI actions to UI state is not always a simple process, but it does lead
to simpler logic. Your thought process shouldn't end with determining how to
make the UI navigate to a particular screen, for example. You need to think
further and consider how to represent that user flow in your UI state. **In
other words: don't think about what actions the UI needs to make; think about
how those actions affect the UI state.**

> [!IMPORTANT]
> **Key Point:** ViewModel events should always result in a UI state update.

For example, consider the case of navigating to the home screen when the user is
logged in on the login screen. You could model this in the UI state as follows:

    data class LoginUiState(
        val isLoading: Boolean = false,
        val errorMessage: String? = null,
        val isUserLoggedIn: Boolean = false
    )

This UI reacts to changes to the `isUserLoggedIn` state and navigates to the
correct destination as needed:

    class LoginViewModel : ViewModel() {
        private val _uiState = MutableStateFlow(LoginUiState())
        val uiState: StateFlow<LoginUiState> = _uiState.asStateFlow()
        /* ... */
    }

    class LoginActivity : AppCompatActivity() {
        private val viewModel: LoginViewModel by viewModels()

        override fun onCreate(savedInstanceState: Bundle?) {
            /* ... */

            lifecycleScope.launch {
                repeatOnLifecycle(Lifecycle.State.STARTED) {
                    viewModel.uiState.collect { uiState ->
                        if (uiState.isUserLoggedIn) {
                            // Navigate to the Home screen.
                        }
                        ...
                    }
                }
            }
        }
    }

> [!NOTE]
> **Note:** The code examples in this section require an understanding of [coroutines](https://developer.android.com/kotlin/coroutines) and [how to use them with lifecycle-aware
> components](https://developer.android.com/topic/libraries/architecture/coroutines).

### Consuming events can trigger state updates

Consuming certain ViewModel events in the UI might result in other UI state
updates. For example, when showing transient messages on the screen to let the
user know that something happened, the UI needs to notify the ViewModel to
trigger another state update when the message has been shown on the screen. The
event that happens when the user has consumed the message (by dismissing it or
after a timeout) can be treated as "user input" and as such, the
ViewModel should be aware of that. In this situation, the UI state can be
modeled as follows:

    // Models the UI state for the Latest news screen.
    data class LatestNewsUiState(
        val news: List<News> = emptyList(),
        val isLoading: Boolean = false,
        val userMessage: String? = null
    )

The ViewModel would update the UI state as follows when the business logic
requires showing a new transient message to the user:

    class LatestNewsViewModel(/* ... */) : ViewModel() {

        private val _uiState = MutableStateFlow(LatestNewsUiState(isLoading = true))
        val uiState: StateFlow<LatestNewsUiState> = _uiState

        fun refreshNews() {
            viewModelScope.launch {
                // If there isn't internet connection, show a new message on the screen.
                if (!internetConnection()) {
                    _uiState.update { currentUiState ->
                        currentUiState.copy(userMessage = "No Internet connection")
                    }
                    return@launch
                }

                // Do something else.
            }
        }

        fun userMessageShown() {
            _uiState.update { currentUiState ->
                currentUiState.copy(userMessage = null)
            }
        }
    }

The ViewModel doesn't need to know how the UI is showing the message on the
screen; it just knows that there's a user message that needs to be shown. Once
the transient message has been shown, the UI needs to notify the ViewModel of
that, causing another UI state update to clear the `userMessage` property:

    class LatestNewsActivity : AppCompatActivity() {
        private val viewModel: LatestNewsViewModel by viewModels()

        override fun onCreate(savedInstanceState: Bundle?) {
            /* ... */

            lifecycleScope.launch {
                repeatOnLifecycle(Lifecycle.State.STARTED) {
                    viewModel.uiState.collect { uiState ->
                        uiState.userMessage?.let {
                            // TODO: Show Snackbar with userMessage.

                            // Once the message is displayed and
                            // dismissed, notify the ViewModel.
                            viewModel.userMessageShown()
                        }
                        ...
                    }
                }
            }
        }
    }

Even though the message is transient, the UI state is a
faithful representation of what's displayed on the screen at every single
point in time. Either the user message is displayed, or it isn't.

## Navigation events

The [Consuming events can trigger state updates](https://developer.android.com/topic/architecture/views/ui-layer/events-views#consuming-trigger-updates)
section details how you use UI state to display user messages on the
screen. Navigation events are also a common type of event in an Android app.

If the event is triggered in the UI because the user tapped on a button, the UI
takes care of that by calling the navigation controller.

    class LoginActivity : AppCompatActivity() {

        private lateinit var binding: ActivityLoginBinding
        private val viewModel: LoginViewModel by viewModels()

        override fun onCreate(savedInstanceState: Bundle?) {
            /* ... */

            binding.helpButton.setOnClickListener {
                navController.navigate(...) // Open help screen
            }
        }
    }

If the data input requires some business logic validation before navigating, the
ViewModel would need to expose that state to the UI. The UI would react
to that state change and navigate accordingly. The [Handle ViewModel events
section](https://developer.android.com/topic/architecture/ui-layer/events#handle-viewmodel-events) covers
this use case. Here's similar code:

    class LoginActivity : AppCompatActivity() {
        private val viewModel: LoginViewModel by viewModels()

        override fun onCreate(savedInstanceState: Bundle?) {
            /* ... */

            lifecycleScope.launch {
                repeatOnLifecycle(Lifecycle.State.STARTED) {
                    viewModel.uiState.collect { uiState ->
                        if (uiState.isUserLoggedIn) {
                            // Navigate to the Home screen.
                        }
                        ...
                    }
                }
            }
        }
    }

In the example above, the app works as expected because the current destination,
Login, wouldn't be kept in the back stack. Users cannot go back to it if they
press back. However, in cases where that might happen, the solution would
require additional logic.

### Navigation events when the destination is kept in the back stack

When a ViewModel sets some state that produces a navigation event from screen
A to screen B and screen A is kept in the navigation back stack, you might need
additional logic to not keep advancing automatically to B. To implement this,
it's required to have additional state that indicates whether or not the UI
should consider navigating to the other screen. Normally, that state is held in
the UI because Navigation logic is a concern of the UI, not the ViewModel.
To illustrate this, let's consider the following use case.

Let's say that you are in the registration flow of your app. In the *date of
birth* validation screen, when the user inputs a date, the date is validated by
the ViewModel when the user taps on the "Continue" button. The ViewModel
delegates the validation logic to the data layer. If the date is valid, the
user goes to the next screen. As an additional feature, users can go back and
forth between the different registration screens in case they want to change
some data. Therefore, all the destinations in the registration flow are kept in
the same back stack. Given these requirements, you could implement this screen
as follows:

    // Key that identifies the `validationInProgress` state in the Bundle
    private const val DOB_VALIDATION_KEY = "dobValidationKey"

    class DobValidationFragment : Fragment() {

        private var validationInProgress: Boolean = false
        private val viewModel: DobValidationViewModel by viewModels()

        override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
            super.onViewCreated(view, savedInstanceState)
            val binding = // ...
            validationInProgress = savedInstanceState?.getBoolean(DOB_VALIDATION_KEY) ?: false

            binding.continueButton.setOnClickListener {
                viewModel.validateDob()
                validationInProgress = true
            }

            viewLifecycleOwner.lifecycleScope.launch {
                viewModel.uiState
                    .flowWithLifecycle(viewLifecycleOwner.lifecycle)
                    .collect { uiState ->
                        // Update other parts of the UI ...

                        // If the input is valid and the user wants
                        // to navigate, navigate to the next screen
                        // and reset `validationInProgress` flag
                        if (uiState.isDobValid && validationInProgress) {
                            validationInProgress = false
                            navController.navigate(...) // Navigate to next screen
                        }
                    }
            }

            return binding
        }

        override fun onSaveInstanceState(outState: Bundle) {
            super.onSaveInstanceState(outState)
            outState.putBoolean(DOB_VALIDATION_KEY, validationInProgress)
        }
    }

The date of birth validation is *business logic* that the ViewModel is
responsible for. Most of the time, the ViewModel would delegate that logic to
the data layer. The logic to navigate the user to the next screen
is *UI logic* because these requirements could change depending on the UI
configuration. For example, you might not want to automatically advance to
another screen in a tablet if you're showing multiple registration steps at the
same time. The `validationInProgress` variable in the code above implements
this functionality and handles whether or not the UI should navigate
automatically whenever the date of birth is valid and the user wanted
to continue to the following registration step.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [UI layer](https://developer.android.com/topic/architecture/ui-layer)
- [State holders and UI State {:#mad-arch}](https://developer.android.com/topic/architecture/ui-layer/stateholders)
- [Guide to app architecture](https://developer.android.com/topic/architecture)