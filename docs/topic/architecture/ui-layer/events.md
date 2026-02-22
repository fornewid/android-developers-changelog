---
title: https://developer.android.com/topic/architecture/ui-layer/events
url: https://developer.android.com/topic/architecture/ui-layer/events
source: md.txt
---

# UI events

*UI events* are actions that should be handled in the UI layer, either by the UI or by the ViewModel. The most common type of events are*user events* . The user produces user events by interacting with the app---for example, by tapping the screen or by generating gestures. The UI then consumes these events using callbacks such as`onClick()`listeners.
| **Key terms:**
|
| - **UI:**View-based or Compose code that handles the user interface.
| - **UI events:**Actions that should be handled in the UI layer.
| - **User events:**Events that the user produces when interacting with the app.

The ViewModel is normally responsible for handling the business logic of a particular user event---for example, the user clicking on a button to refresh some data. Usually, the ViewModel handles this by exposing functions that the UI can call. User events might also have UI behavior logic that the UI can handle directly---for example, navigating to a different screen or showing a[`Snackbar`](https://developer.android.com/reference/com/google/android/material/snackbar/Snackbar).

While the*business logic* remains the same for the same app on different mobile platforms or form factors, the*UI behavior logic* is an implementation detail that might differ between those cases. The[UI layer page](https://developer.android.com/jetpack/guide/ui-layer#logic-types)defines these types of logic as follows:

- **Business logic** refers to*what to do* with state changes---for example, making a payment or storing user preferences. The domain and data layers usually handle this logic. Throughout this guide, the[Architecture Components ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel)class is used as an opinionated solution for classes that handle business logic.
- **UI behavior logic** or**UI logic** refers to*how to display*state changes---for example, navigation logic or how to show messages to the user. The UI handles this logic.

**Note:** The recommendations and best practices present in this page can be applied to a broad spectrum of apps to allow them to scale, improve quality and robustness, and make them easier to test. However, you should treat them as guidelines and adapt them to your requirements as needed.  

## UI event decision tree

The following diagram shows a decision tree to find the best approach for handling a particular event use case. The rest of this guide explains these approaches in detail.
![If the event originated in the ViewModel, then update the UI state. If the event originated in the UI and requires business logic, then delegate the business logic to the ViewModel. If the event originated in the UI and requires UI behavior logic, then modify the UI element state directly in the UI.](https://developer.android.com/static/topic/libraries/architecture/images/mad-arch-uievents-tree.png)**Figure 1.**Decision tree for handling events.

## Handle user events

The UI can handle user events directly if those events relate to modifying the state of a UI element---for example, the state of an expandable item. If the event requires performing business logic, such as refreshing the data on the screen, it should be processed by the ViewModel.

The following example shows how different buttons are used to expand a UI element (UI logic) and to refresh the data on the screen (business logic):  

### Views

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

### Compose

    @Composable
    fun LatestNewsScreen(viewModel: LatestNewsViewModel = viewModel()) {

        // State of whether more details should be shown
        var expanded by remember { mutableStateOf(false) }

        Column {
            Text("Some text")
            if (expanded) {
                Text("More details")
            }

            Button(
              // The expand details event is processed by the UI that
              // modifies this composable's internal state.
              onClick = { expanded = !expanded }
            ) {
              val expandText = if (expanded) "Collapse" else "Expand"
              Text("$expandText details")
            }

            // The refresh event is processed by the ViewModel that is in charge
            // of the UI's business logic.
            Button(onClick = { viewModel.refreshNews() }) {
                Text("Refresh data")
            }
        }
    }

### User events in RecyclerViews

If the action is produced further down the UI tree, like in a`RecyclerView`item or a custom`View`, the`ViewModel`should still be the one handling user events.

For example, suppose that all news items from`NewsActivity`contain a bookmark button. The`ViewModel`needs to know the ID of the bookmarked news item. When the user bookmarks a news item, the`RecyclerView`adapter does not call the exposed`addBookmark(newsId)`function from the`ViewModel`, which would require a dependency on the`ViewModel`. Instead, the`ViewModel`exposes a state object called`NewsItemUiState`which contains the implementation for handling the event:  

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

This way, the`RecyclerView`adapter only works with the data that it needs: the list of`NewsItemUiState`objects. The adapter doesn't have access to the entire ViewModel, making it less likely to abuse the functionality exposed by the ViewModel. When you allow only the activity class to work with the ViewModel, you separate responsibilities. This ensures that UI-specific objects like views or`RecyclerView`adapters don't interact directly with the ViewModel.
| **Warning:** It's bad practice to pass the ViewModel into the`RecyclerView`adapter because that tightly couples the adapter with the ViewModel class.
| **Note:** Another common pattern is for the`RecyclerView`adapter to have a`Callback`interface for user actions. In that case, the activity or fragment can handle the binding and call the ViewModel functions directly from the callback interface.

### Naming conventions for user event functions

In this guide, the ViewModel functions that handle user events are named with a verb based on the action that they handle---for example:`addBookmark(id)`or`logIn(username, password)`.

## Handle ViewModel events

**UI actions that originate from the ViewModel---ViewModel events---should always result in a[UI state](https://developer.android.com/jetpack/guide/ui-layer#expose-ui-state)update.** This complies with the principles of[Unidirectional Data Flow](https://developer.android.com/jetpack/guide/ui-layer#udf). It makes events reproducible after configuration changes and guarantees that UI actions won't be lost. Optionally, you can also make events reproducible after process death if you use the[saved state module](https://developer.android.com/topic/libraries/architecture/viewmodel-savedstate).

Mapping UI actions to UI state is not always a simple process, but it does lead to simpler logic. Your thought process shouldn't end with determining how to make the UI navigate to a particular screen, for example. You need to think further and consider how to represent that user flow in your UI state.**In other words: don't think about what actions the UI needs to make; think about how those actions affect the UI state.**
| **Key Point:** ViewModel events should always result in a UI state update.

For example, consider the case of navigating to the home screen when the user is logged in on the login screen. You could model this in the UI state as follows:  

    data class LoginUiState(
        val isLoading: Boolean = false,
        val errorMessage: String? = null,
        val isUserLoggedIn: Boolean = false
    )

This UI reacts to changes to the`isUserLoggedIn`state and navigates to the correct destination as needed:  

### Views

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

### Compose

    class LoginViewModel : ViewModel() {
        var uiState by mutableStateOf(LoginUiState())
            private set
        /* ... */
    }

    @Composable
    fun LoginScreen(
        viewModel: LoginViewModel = viewModel(),
        onUserLogIn: () -> Unit
    ) {
        val currentOnUserLogIn by rememberUpdatedState(onUserLogIn)

        // Whenever the uiState changes, check if the user is logged in.
        LaunchedEffect(viewModel.uiState)  {
            if (viewModel.uiState.isUserLoggedIn) {
                currentOnUserLogIn()
            }
        }

        // Rest of the UI for the login screen.
    }

| **Note:** The code examples in this section require an understanding of[coroutines](https://developer.android.com/kotlin/coroutines)and[how to use them with lifecycle-aware components](https://developer.android.com/topic/libraries/architecture/coroutines).

### Consuming events can trigger state updates

Consuming certain ViewModel events in the UI might result in other UI state updates. For example, when showing transient messages on the screen to let the user know that something happened, the UI needs to notify the ViewModel to trigger another state update when the message has been shown on the screen. The event that happens when the user has consumed the message (by dismissing it or after a timeout) can be treated as "user input" and as such, the ViewModel should be aware of that. In this situation, the UI state can be modeled as follows:  

    // Models the UI state for the Latest news screen.
    data class LatestNewsUiState(
        val news: List<News> = emptyList(),
        val isLoading: Boolean = false,
        val userMessage: String? = null
    )

The ViewModel would update the UI state as follows when the business logic requires showing a new transient message to the user:  

### Views

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

### Compose

    class LatestNewsViewModel(/* ... */) : ViewModel() {

        var uiState by mutableStateOf(LatestNewsUiState())
            private set

        fun refreshNews() {
            viewModelScope.launch {
                // If there isn't internet connection, show a new message on the screen.
                if (!internetConnection()) {
                    uiState = uiState.copy(userMessage = "No Internet connection")
                    return@launch
                }

                // Do something else.
            }
        }

        fun userMessageShown() {
            uiState = uiState.copy(userMessage = null)
        }
    }

The ViewModel doesn't need to know how the UI is showing the message on the screen; it just knows that there's a user message that needs to be shown. Once the transient message has been shown, the UI needs to notify the ViewModel of that, causing another UI state update to clear the`userMessage`property:  

### Views

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

### Compose

    @Composable
    fun LatestNewsScreen(
        snackbarHostState: SnackbarHostState,
        viewModel: LatestNewsViewModel = viewModel(),
    ) {
        // Rest of the UI content.

        // If there are user messages to show on the screen,
        // show it and notify the ViewModel.
        viewModel.uiState.userMessage?.let { userMessage ->
            LaunchedEffect(userMessage) {
                snackbarHostState.showSnackbar(userMessage)
                // Once the message is displayed and dismissed, notify the ViewModel.
                viewModel.userMessageShown()
            }
        }
    }

Even though the message is transient, the UI state is a faithful representation of what's displayed on the screen at every single point in time. Either the user message is displayed, or it isn't.
| **Note:** For a more advanced use case with a list of user messages to show on the screen, check out the[Jetsnack Compose sample](https://github.com/android/compose-samples/blob/main/Jetsnack/app/src/main/java/com/example/jetsnack/model/SnackbarManager.kt).

## Navigation events

The[Consuming events can trigger state updates](https://developer.android.com/topic/architecture/ui-layer/events#consuming-trigger-updates)section details how you use UI state to display user messages on the screen. Navigation events are also a common type of events in an Android app.

If the event is triggered in the UI because the user tapped on a button, the UI takes care of that by calling the navigation controller or exposing the event to the caller composable as appropriate.  

### Views

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

### Compose

    @Composable
    fun LoginScreen(
        onHelp: () -> Unit, // Caller navigates to the right screen
        viewModel: LoginViewModel = viewModel()
    ) {
        // Rest of the UI

        Button(onClick = onHelp) {
            Text("Get help")
        }
    }

If the data input requires some business logic validation before navigating, the ViewModel would need to expose that state to the UI. The UI would react to that state change and navigate accordingly. The[Handle ViewModel events section](https://developer.android.com/topic/architecture/ui-layer/events#handle-viewmodel-events)covers this use case. Here's a similar code:  

### Views

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

### Compose

    @Composable
    fun LoginScreen(
        onUserLogIn: () -> Unit, // Caller navigates to the right screen
        viewModel: LoginViewModel = viewModel()
    ) {
        Button(
            onClick = {
                // ViewModel validation is triggered
                viewModel.login()
            }
        ) {
            Text("Log in")
        }
        // Rest of the UI

        val lifecycle = LocalLifecycleOwner.current.lifecycle
        val currentOnUserLogIn by rememberUpdatedState(onUserLogIn)
        LaunchedEffect(viewModel, lifecycle)  {
            // Whenever the uiState changes, check if the user is logged in and
            // call the `onUserLogin` event when `lifecycle` is at least STARTED
            snapshotFlow { viewModel.uiState }
                .filter { it.isUserLoggedIn }
                .flowWithLifecycle(lifecycle)
                .collect {
                    currentOnUserLogIn()
                }
        }
    }

In the example above, the app works as expected because the current destination, Login, wouldn't be kept in the back stack. Users cannot go back to it if they press back. However, in cases where that might happen, the solution would require additional logic.

### Navigation events when the destination is kept in the back stack

When a ViewModel sets some state that produces a navigation event from screen A to screen B and screen A is kept in the navigation back stack, you might need additional logic to not keep advancing automatically to B. To implement this, it's required to have additional state that indicates whether or not the UI should consider navigating to the other screen. Normally, that state is held in the UI because Navigation logic is a concern of the UI, not the ViewModel. To illustrate this, let's consider the following use case.

Let's say that you are in the registration flow of your app. In the*date of birth*validation screen, when the user inputs a date, the date is validated by the ViewModel when the user taps on the "Continue" button. The ViewModel delegates the validation logic to the data layer. If the date is valid, the user goes to the next screen. As an additional feature, users can go back and forth between the different registration screens in case they want to change some data. Therefore, all the destinations in the registration flow are kept in the same back stack. Given these requirements, you could implement this screen as follows:  

### Views

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

### Compose

    class DobValidationViewModel(/* ... */) : ViewModel() {
        var uiState by mutableStateOf(DobValidationUiState())
            private set
    }

    @Composable
    fun DobValidationScreen(
        onNavigateToNextScreen: () -> Unit, // Caller navigates to the right screen
        viewModel: DobValidationViewModel = viewModel()
    ) {
        // TextField that updates the ViewModel when a date of birth is selected

        var validationInProgress by rememberSaveable { mutableStateOf(false) }

        Button(
            onClick = {
                viewModel.validateInput()
                validationInProgress = true
            }
        ) {
            Text("Continue")
        }
        // Rest of the UI

        /*
         * The following code implements the requirement of advancing automatically
         * to the next screen when a valid date of birth has been introduced
         * and the user wanted to continue with the registration process.
         */

        if (validationInProgress) {
            val lifecycle = LocalLifecycleOwner.current.lifecycle
            val currentNavigateToNextScreen by rememberUpdatedState(onNavigateToNextScreen)
            LaunchedEffect(viewModel, lifecycle) {
                // If the date of birth is valid and the validation is in progress,
                // navigate to the next screen when `lifecycle` is at least STARTED,
                // which is the default Lifecycle.State for the `flowWithLifecycle` operator.
                snapshotFlow { viewModel.uiState }
                    .filter { it.isDobValid }
                    .flowWithLifecycle(lifecycle)
                    .collect {
                        validationInProgress = false
                        currentNavigateToNextScreen()
                    }
            }
        }
    }

The date of birth validation is*business logic* that the ViewModel is responsible for. Most of the time, the ViewModel would delegate that logic to the data layer. The logic to navigate the user to the next screen is*UI logic* because these requirements could change depending on the UI configuration. For example, you might not want to automatically advance to another screen in a tablet if you're showing multiple registration steps at the same time. The`validationInProgress`variable in the code above implements this functionality and handles whether or not the UI should navigate automatically whenever the date of birth is valid and the user wanted to continue to the following registration step.

## Other use cases

If you think your UI event use case cannot be solved with UI state updates, you might need to reconsider how data flows in your app. Consider the following principles:

- **Each class should do what they're responsible for, not more.**The UI is in charge of screen-specific behavior logic such as navigation calls, click events, and obtaining permission requests. The ViewModel contains business logic and converts the results from lower layers of the hierarchy into UI state.
- **Think about where the event originates.** Follow the[decision tree](https://developer.android.com/topic/architecture/ui-layer/events#decision-tree)presented at the beginning of this guide, and make each class handle what they're responsible for. For example, if the event originates from the UI and it results in a navigation event, then that event has to be handled in the UI. Some logic might be delegated to the ViewModel, but handling the event can't be entirely delegated to the ViewModel.
- **If you have multiple consumers and you're worried about the event being consumed multiple times, you might need to reconsider your app architecture.** Having multiple concurrent consumers results in the*delivered exactly once*contract becoming extremely difficult to guarantee, so the amount of complexity and subtle behavior explodes. If you're having this problem, consider pushing those concerns upwards in your UI tree; you might need a different entity scoped higher up in the hierarchy.
- **Think about when the state needs to be consumed.** In certain situations, you might not want to keep consuming state when the app is in the background---for example, showing a`Toast`. In those cases, consider consuming the state when the UI is in the foreground.

| **Note:** In some apps, you might have seen ViewModel events being exposed to the UI using[Kotlin Channels](https://kotlinlang.org/docs/channels.html)or other reactive streams. When the producer (the ViewModel) outlives the consumer (UI---Compose or Views), these solutions don't guarantee the delivery and processing of those events. This can result in future problems for the developer, and it's also an unacceptable user experience for most apps because this could leave the app in an inconsistent state, it could introduce bugs, or the user might miss critical information.
|
| If you're in one of these situations, reconsider what that one-off ViewModel event actually means for your UI. Handle them immediately and reduce them to UI state. UI state better represents the UI at a given point in time, it gives you more delivery and processing guarantees, it's usually easier to test, and it integrates consistently with the rest of your app.
|
| To learn more about why you shouldn't use the aforementioned APIs with some code examples, read the[ViewModel: One-off event antipatterns](https://medium.com/androiddevelopers/viewmodel-one-off-event-antipatterns-16a1da869b95)blog post.

## Samples

The following Google samples demonstrate the UI events in the UI layer. Go explore them to see this guidance in practice:

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [UI layer](https://developer.android.com/topic/architecture/ui-layer)
- [State holders and UI State {:#mad-arch}](https://developer.android.com/topic/architecture/ui-layer/stateholders)
- [Guide to app architecture](https://developer.android.com/topic/architecture)