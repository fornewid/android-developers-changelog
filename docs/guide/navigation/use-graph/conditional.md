---
title: https://developer.android.com/guide/navigation/use-graph/conditional
url: https://developer.android.com/guide/navigation/use-graph/conditional
source: md.txt
---

# Conditional navigation

When designing navigation for your app, you might want to navigate to one destination versus another based on conditional logic. For example, a user might follow a deep link to a destination that requires the user to be logged in, or you might have different destinations in a game for when the player wins or loses.

## User login

In this example, a user attempts to navigate to a profile screen that requires authentication. Because this action requires authentication, the user should be redirected to a login screen if they are not already authenticated.

The navigation graph for this example might look something like this:
![a login flow is handled independently from the app's main navigation flow.](https://developer.android.com/static/images/guide/navigation/navigation-conditional-login.png)**Figure 1.**A login flow is handled independently from the app's main navigation flow.

To authenticate, the app must navigate to the`login_fragment`, where the user can enter a username and password to authenticate. If accepted, the user is sent back to the`profile_fragment`screen. If not accepted, the user is informed that their credentials are invalid using a[`Snackbar`](https://developer.android.com/reference/com/google/android/material/snackbar/Snackbar). If the user navigates back to the profile screen without logging in, they are sent to the`main_fragment`screen.
| **Note:** The architecture of this app follows the pattern described in the[Guide to App Architecture](https://developer.android.com/jetpack/docs/guide). It uses a[`ViewModel`](https://developer.android.com/topic/libraries/architecture/viewmodel)and[`LiveData`](https://developer.android.com/topic/libraries/architecture/livedata)and follows a single-activity structure. Be sure that you're familiar with these classes before proceeding.

Here's the navigation graph for this app:  

    <navigation xmlns:android="http://schemas.android.com/apk/res/android"
            xmlns:app="http://schemas.android.com/apk/res-auto"
            xmlns:tools="http://schemas.android.com/tools"
            android:id="@+id/nav_graph"
            app:startDestination="@id/main_fragment">
        <fragment
                android:id="@+id/main_fragment"
                android:name="com.google.android.conditionalnav.MainFragment"
                android:label="fragment_main"
                tools:layout="@layout/fragment_main">
            <action
                    android:id="@+id/navigate_to_profile_fragment"
                    app:destination="@id/profile_fragment"/>
        </fragment>
        <fragment
                android:id="@+id/login_fragment"
                android:name="com.google.android.conditionalnav.LoginFragment"
                android:label="login_fragment"
                tools:layout="@layout/login_fragment"/>
        <fragment
                android:id="@+id/profile_fragment"
                android:name="com.google.android.conditionalnav.ProfileFragment"
                android:label="fragment_profile"
                tools:layout="@layout/fragment_profile"/>
    </navigation>

`MainFragment`contains a button that the user can click to view their profile. If the user wants to see the profile screen, they must first authenticate. This interaction is modeled using two separate fragments, but it depends on shared user state. This state information is not the responsibility of either of these two fragments and is more appropriately held in a shared`UserViewModel`. This`ViewModel`is shared between the fragments by scoping it to the activity, which implements`ViewModelStoreOwner`. In the following example,`requireActivity()`resolves to`MainActivity`, because`MainActivity`hosts`ProfileFragment`:  

### Kotlin

```kotlin
class ProfileFragment : Fragment() {
    private val userViewModel: UserViewModel by activityViewModels()
    ...
}
```

### Java

```java
public class ProfileFragment extends Fragment {
    private UserViewModel userViewModel;
    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        userViewModel = new ViewModelProvider(requireActivity()).get(UserViewModel.class);
        ...
    }
    ...
}
```

The user data in`UserViewModel`is exposed via`LiveData`, so to decide where to navigate, you should observe this data. Upon navigating to`ProfileFragment`, the app shows a welcome message if the user data is present. If the user data is`null`, you then navigate to`LoginFragment`, since the user needs to authenticate before seeing their profile. Define the deciding logic in your`ProfileFragment`, as shown in the following example:  

### Kotlin

```kotlin
class ProfileFragment : Fragment() {
    private val userViewModel: UserViewModel by activityViewModels()

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        val navController = findNavController()
        userViewModel.user.observe(viewLifecycleOwner, Observer { user ->
            if (user != null) {
                showWelcomeMessage()
            } else {
                navController.navigate(R.id.login_fragment)
            }
        })
    }

    private fun showWelcomeMessage() {
        ...
    }
}
```

### Java

```java
public class ProfileFragment extends Fragment {
    private UserViewModel userViewModel;

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        userViewModel = new ViewModelProvider(requireActivity()).get(UserViewModel.class);
        final NavController navController = Navigation.findNavController(view);
        userViewModel.user.observe(getViewLifecycleOwner(), (Observer<User>) user -> {
            if (user != null) {
                showWelcomeMessage();
            } else {
                navController.navigate(R.id.login_fragment);
            }
        });
    }

    private void showWelcomeMessage() {
        ...
    }
}
```

If the user data is`null`when they reach the`ProfileFragment`, they are redirected to the`LoginFragment`.

You can use[`NavController.getPreviousBackStackEntry()`](https://developer.android.com/reference/androidx/navigation/NavController#getPreviousBackStackEntry())to retrieve the[`NavBackStackEntry`](https://developer.android.com/reference/androidx/navigation/NavBackStackEntry)for the previous destination, which encapsulates the`NavController`-specific state for the destination.`LoginFragment`uses the[`SavedStateHandle`](https://developer.android.com/reference/androidx/lifecycle/SavedStateHandle)of the previous`NavBackStackEntry`to set an initial value indicating whether the user has successfully logged in. This is the state we would want to return if the user were to immediately press the system back button. Setting this state using`SavedStateHandle`ensures that the state persists through process death.  

### Kotlin

```kotlin
class LoginFragment : Fragment() {
    companion object {
        const val LOGIN_SUCCESSFUL: String = "LOGIN_SUCCESSFUL"
    }

    private val userViewModel: UserViewModel by activityViewModels()
    private lateinit var savedStateHandle: SavedStateHandle

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        savedStateHandle = findNavController().previousBackStackEntry!!.savedStateHandle
        savedStateHandle.set(LOGIN_SUCCESSFUL, false)
    }
}
```

### Java

```java
public class LoginFragment extends Fragment {
    public static String LOGIN_SUCCESSFUL = "LOGIN_SUCCESSFUL"

    private UserViewModel userViewModel;
    private SavedStateHandle savedStateHandle;

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        userViewModel = new ViewModelProvider(requireActivity()).get(UserViewModel.class);

        savedStateHandle = Navigation.findNavController(view)
                .getPreviousBackStackEntry()
                .getSavedStateHandle();
        savedStateHandle.set(LOGIN_SUCCESSFUL, false);
    }
}
```

Once the user enters a username and password, they are passed to the`UserViewModel`for authentication. If authentication is successful, the`UserViewModel`stores the user data. The`LoginFragment`then updates the`LOGIN_SUCCESSFUL`value on the`SavedStateHandle`and pops itself off of the back stack.  

### Kotlin

```kotlin
class LoginFragment : Fragment() {
    companion object {
        const val LOGIN_SUCCESSFUL: String = "LOGIN_SUCCESSFUL"
    }

    private val userViewModel: UserViewModel by activityViewModels()
    private lateinit var savedStateHandle: SavedStateHandle

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        savedStateHandle = findNavController().previousBackStackEntry!!.savedStateHandle
        savedStateHandle.set(LOGIN_SUCCESSFUL, false)

        val usernameEditText = view.findViewById(R.id.username_edit_text)
        val passwordEditText = view.findViewById(R.id.password_edit_text)
        val loginButton = view.findViewById(R.id.login_button)

        loginButton.setOnClickListener {
            val username = usernameEditText.text.toString()
            val password = passwordEditText.text.toString()
            login(username, password)
        }
    }

    fun login(username: String, password: String) {
        userViewModel.login(username, password).observe(viewLifecycleOwner, Observer { result ->
            if (result.success) {
                savedStateHandle.set(LOGIN_SUCCESSFUL, true)
                findNavController().popBackStack()
            } else {
                showErrorMessage()
            }
        })
    }

    fun showErrorMessage() {
        // Display a snackbar error message
    }
}
```

### Java

```java
public class LoginFragment extends Fragment {
    public static String LOGIN_SUCCESSFUL = "LOGIN_SUCCESSFUL"

    private UserViewModel userViewModel;
    private SavedStateHandle savedStateHandle;

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        userViewModel = new ViewModelProvider(requireActivity()).get(UserViewModel.class);

        savedStateHandle = Navigation.findNavController(view)
                .getPreviousBackStackEntry()
                .getSavedStateHandle();
        savedStateHandle.set(LOGIN_SUCCESSFUL, false);

        EditText usernameEditText = view.findViewById(R.id.username_edit_text);
        EditText passwordEditText = view.findViewById(R.id.password_edit_text);
        Button loginButton = view.findViewById(R.id.login_button);

        loginButton.setOnClickListener(v -> {
            String username = usernameEditText.getText().toString();
            String password = passwordEditText.getText().toString();
            login(username, password);
        });
    }

    private void login(String username, String password) {
        userViewModel.login(username, password).observe(viewLifecycleOwner, (Observer<LoginResult>) result -> {
            if (result.success) {
                savedStateHandle.set(LOGIN_SUCCESSFUL, true);
                NavHostFragment.findNavController(this).popBackStack();
            } else {
                showErrorMessage();
            }
        });
    }

    private void showErrorMessage() {
        // Display a snackbar error message
    }
}
```

Note that all logic pertaining to authentication is held within`UserViewModel`. This is important, as it is not the responsibility of either`LoginFragment`or`ProfileFragment`to determine how users are authenticated. Encapsulating your logic in a`ViewModel`makes it not only easier to share but also easier to test. If your navigation logic is complex, you should especially verify this logic through testing. See the[Guide to app architecture](https://developer.android.com/jetpack/docs/guide)for more information on structuring your app's architecture around testable components.

Back in the`ProfileFragment`, the`LOGIN_SUCCESSFUL`value stored in the`SavedStateHandle`can be observed in the[`onCreate()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onCreate(android.os.Bundle))method. When the user returns to the`ProfileFragment`, the`LOGIN_SUCCESSFUL`value will be checked. If the value is`false`, the user can be redirected back to the`MainFragment`.  

### Kotlin

```kotlin
class ProfileFragment : Fragment() {
    ...

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val navController = findNavController()

        val currentBackStackEntry = navController.currentBackStackEntry!!
        val savedStateHandle = currentBackStackEntry.savedStateHandle
        savedStateHandle.getLiveData<Boolean>(LoginFragment.LOGIN_SUCCESSFUL)
                .observe(currentBackStackEntry, Observer { success ->
                    if (!success) {
                        val startDestination = navController.graph.startDestination
                        val navOptions = NavOptions.Builder()
                                .setPopUpTo(startDestination, true)
                                .build()
                        navController.navigate(startDestination, null, navOptions)
                    }
                })
    }

    ...
}
```

### Java

```java
public class ProfileFragment extends Fragment {
    ...

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        NavController navController = NavHostFragment.findNavController(this);

        NavBackStackEntry navBackStackEntry = navController.getCurrentBackStackEntry();
        SavedStateHandle savedStateHandle = navBackStackEntry.getSavedStateHandle();
        savedStateHandle.getLiveData(LoginFragment.LOGIN_SUCCESSFUL)
                .observe(navBackStackEntry, (Observer<Boolean>) success -> {
                    if (!success) {
                        int startDestination = navController.getGraph().getStartDestination();
                        NavOptions navOptions = new NavOptions.Builder()
                                .setPopUpTo(startDestination, true)
                                .build();
                        navController.navigate(startDestination, null, navOptions);
                    }
                });
    }

    ...
}
```

If the user successfully logged in, the`ProfileFragment`displays a welcome message.

The technique used here of checking the result allows you to distinguish between two different cases:

- The initial case, where the user is not logged in and should be asked to login.
- The user is not logged in because**they chose not to login** (a result of`false`).

By distinguishing these use cases, you can avoid repeatedly asking the user to login. The business logic for handling failure cases is left to you and might include displaying an overlay that explains why the user needs to login, finishing the entire activity, or redirecting the user to a destination that does not require login, as was the case in the previous code example.