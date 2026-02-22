---
title: https://developer.android.com/develop/ui/compose/navigation
url: https://developer.android.com/develop/ui/compose/navigation
source: md.txt
---

The [Navigation component](https://developer.android.com/guide/navigation) provides support for Jetpack Compose applications.
You can navigate between composables while taking advantage of the Navigation
component's infrastructure and features.

For the latest prerelease navigation library built specifically for Compose, see
the [Navigation 3 documentation](https://developer.android.com/guide/navigation/navigation-3).
| **Note:** If you are not familiar with Compose, review the [Jetpack Compose](https://developer.android.com/jetpack/compose) resources before continuing.

## Setup

To support Compose, use the following dependency in your app module's
`build.gradle` file:

### Groovy

```groovy
dependencies {
    def nav_version = "2.9.7"

    implementation "androidx.navigation:navigation-compose:$nav_version"
}
```

### Kotlin

```kotlin
dependencies {
    val nav_version = "2.9.7"

    implementation("androidx.navigation:navigation-compose:$nav_version")
}
```

## Get started

When implementing navigation in an app, implement a navigation host, graph, and
controller. For more information, see the [Navigation](https://developer.android.com/guide/navigation/get-started) overview.

## Create a NavController

For information on how to create a `NavController` in Compose, see the Compose
section of [Create a navigation controller](https://developer.android.com/guide/navigation/navcontroller).

## Create a NavHost

For information on how to create a `NavHost` in Compose, see the Compose section
of [Design your navigation graph](https://developer.android.com/guide/navigation/design#compose).
| **Note:** When designing your navigation graph, consider how navigation flows will adapt to different display sizes and form factors.

## Navigate to a composable

For information on navigating to a Composable, see
[Navigate to a destination](https://developer.android.com/guide/navigation/use-graph/navigate) in the architecture documentation.

## Navigate with arguments

For information on passing arguments between composable destinations, see the
Compose section of [Design your navigation graph](https://developer.android.com/guide/navigation/design#compose-arguments).

### Retrieve complex data when navigating

It is strongly advised not to pass around complex data objects when navigating,
but instead pass the minimum necessary information, such as a unique identifier
or other form of ID, as arguments when performing navigation actions:

    // Pass only the user ID when navigating to a new destination as argument
    navController.navigate(Profile(id = "user1234"))

Complex objects should be stored as data in a single source of truth, such as
the data layer. Once you land on your destination after navigating, you can then
load the required information from the single source of truth by using the
passed ID. To retrieve the arguments in your `ViewModel` that's responsible for
accessing the data layer, use the [`SavedStateHandle`](https://developer.android.com/topic/libraries/architecture/viewmodel-savedstate#savedstatehandle) of the `ViewModel`:

    class UserViewModel(
        savedStateHandle: SavedStateHandle,
        private val userInfoRepository: UserInfoRepository
    ) : ViewModel() {

        private val profile = savedStateHandle.toRoute<Profile>()

        // Fetch the relevant user information from the data layer,
        // ie. userInfoRepository, based on the passed userId argument
        private val userInfo: Flow<UserInfo> = userInfoRepository.getUserInfo(profile.id)

    // ...

    }

This approach helps prevent data loss during configuration changes and any
inconsistencies when the object in question is being updated or mutated.

For a more in depth explanation on why you should avoid passing complex data as
arguments, as well as a list of supported argument types, see [Pass data between
destinations](https://developer.android.com/guide/navigation/navigation-pass-data#supported_argument_types).

## Deep links

Navigation Compose supports deep links that can be defined as part of the
`composable()` function as well. Its `deepLinks` parameter accepts a list of
[`NavDeepLink`](https://developer.android.com/reference/androidx/navigation/NavDeepLink) objects which can be created using the [`navDeepLink()`](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#navDeepLink(kotlin.Function1))
method:

    @Serializable data class Profile(val id: String)
    val uri = "https://www.example.com"

    composable<Profile>(
      deepLinks = listOf(
        navDeepLink<Profile>(basePath = "$uri/profile")
      )
    ) { backStackEntry ->
      ProfileScreen(id = backStackEntry.toRoute<Profile>().id)
    }

These deep links let you associate a specific URL, action or mime type with a
composable. By default, these deep links are not exposed to external apps. To
make these deep links externally available you must add the appropriate
`<intent-filter>` elements to your app's `manifest.xml` file. To enable the deep
link in the preceding example, you should add the following inside of the
`<activity>` element of the manifest:

    <activity ...>
      <intent-filter>
        ...
        <data android:scheme="https" android:host="www.example.com" />
      </intent-filter>
    </activity>

Navigation automatically deep links into that composable when the deep link is
triggered by another app.

These same deep links can also be used to build a `PendingIntent` with the
appropriate deep link from a composable:

    val id = "exampleId"
    val context = LocalContext.current
    val deepLinkIntent = Intent(
        Intent.ACTION_VIEW,
        "https://www.example.com/profile/$id".toUri(),
        context,
        MyActivity::class.java
    )

    val deepLinkPendingIntent: PendingIntent? = TaskStackBuilder.create(context).run {
        addNextIntentWithParentStack(deepLinkIntent)
        getPendingIntent(0, PendingIntent.FLAG_UPDATE_CURRENT)
    }

You can then use this `deepLinkPendingIntent` like any other `PendingIntent` to
open your app at the deep link destination.

## Nested Navigation

For information on how to create nested navigation graphs, see
[Nested graphs](https://developer.android.com/guide/navigation/design/nested-graphs).

## Build an adaptive navigation bar and navigation rail

The [`NavigationSuiteScaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/navigationsuite/package-summary#NavigationSuiteScaffold(kotlin.Function1,androidx.compose.ui.Modifier,androidx.compose.material3.adaptive.navigationsuite.NavigationSuiteType,androidx.compose.material3.adaptive.navigationsuite.NavigationSuiteColors,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function0)) displays the appropriate top-level
navigation UI for your app based on the current [`WindowSizeClass`](https://developer.android.com/reference/kotlin/androidx/window/core/layout/WindowSizeClass). For
compact screens, the scaffold shows a bottom navigation bar; for medium and
expanded screens, a navigation rail.

`NavigationSuiteScaffold` handles primary navigation; however, adaptive layouts
often involve other specialized composables. For the list-detail and supporting
pane canonical layouts, which are common in adaptive designs, use
[`ListDetailPaneScaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/package-summary#ListDetailPaneScaffold(androidx.compose.material3.adaptive.layout.PaneScaffoldDirective,androidx.compose.material3.adaptive.layout.ThreePaneScaffoldState,kotlin.Function1,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function2,androidx.compose.material3.adaptive.layout.PaneExpansionState)) and [`SupportingPaneScaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/package-summary#SupportingPaneScaffold(androidx.compose.material3.adaptive.layout.PaneScaffoldDirective,androidx.compose.material3.adaptive.layout.ThreePaneScaffoldState,kotlin.Function1,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1,kotlin.Function2,androidx.compose.material3.adaptive.layout.PaneExpansionState)), respectively.
For more information, see [Build adaptive layouts](https://developer.android.com/develop/ui/compose/layouts/adaptive).

## Interoperability

If you want to use the Navigation component with Compose, you have two options:

- Define a navigation graph with the Navigation component for fragments.
- Define a navigation graph with a `NavHost` in Compose using Compose destinations. This is possible only if all of the screens in the navigation graph are composables.

Therefore, the recommendation for mixed Compose and Views apps is to use the
Fragment-based Navigation component. Fragments will then hold View-based
screens, Compose screens, and screens that use both Views and Compose. Once each
Fragment's contents are in Compose, the next step is to tie all of those screens
together with Navigation Compose and remove all of the Fragments.

### Navigate from Compose with Navigation for fragments

In order to change destinations inside Compose code, you expose events that can
be passed to and triggered by any composable in the hierarchy:

    @Composable
    fun MyScreen(onNavigate: (Int) -> Unit) {
        Button(onClick = { onNavigate(R.id.nav_profile) } { /* ... */ }
    }

In your fragment, you make the bridge between Compose and the fragment-based
Navigation component by finding the `NavController` and navigating to the
destination:

    override fun onCreateView( /* ... */ ) {
        setContent {
            MyScreen(onNavigate = { dest -> findNavController().navigate(dest) })
        }
    }

Alternatively, you can pass the `NavController` down your Compose hierarchy.
However, exposing functions is much more reusable and testable.

## Testing

Decouple the navigation code from your composable destinations to enable testing
each composable in isolation, separate from the `NavHost` composable.

This means that you shouldn't pass the `navController` [directly into any
composable](https://developer.android.com/guide/navigation/design) and instead pass navigation callbacks as parameters. This allows
all your composables to be individually testable, as they don't require an
instance of `navController` in tests.

The level of indirection provided by the `composable` lambda is what lets you
separate your Navigation code from the composable itself. This works in two
directions:

- Pass only parsed arguments into your composable
- Pass lambdas that should be triggered by the composable to navigate, rather than the `NavController` itself.

For example, a `ProfileScreen` composable that takes in a `userId` as input and
allows users to navigate to a friend's profile page might have the signature of:

    @Composable
    fun ProfileScreen(
        userId: String,
        navigateToFriendProfile: (friendUserId: String) -> Unit
    ) {
     ...
    }

This way, the `ProfileScreen` composable works independently from Navigation,
allowing it to be tested independently. The `composable` lambda would
encapsulate the minimal logic needed to bridge the gap between the Navigation
APIs and your composable:

    @Serializable data class Profile(id: String)

    composable<Profile> { backStackEntry ->
        val profile = backStackEntry.toRoute<Profile>()
        ProfileScreen(userId = profile.id) { friendUserId ->
            navController.navigate(route = Profile(id = friendUserId))
        }
    }

It is recommended to write tests that cover your app navigation requirements by
testing the `NavHost`, navigation actions passed to your composables as well as
your individual screen composables.

### Testing the `NavHost`

To begin testing your `NavHost` , add the following navigation-testing
dependency:

    dependencies {
    // ...
      androidTestImplementation "androidx.navigation:navigation-testing:$navigationVersion"
      // ...
    }

Wrap your app's `NavHost` in a composable which accepts a `NavHostController` as
a parameter.

    @Composable
    fun AppNavHost(navController: NavHostController){
      NavHost(navController = navController){ ... }
    }

Now you can test `AppNavHost` and all the navigation logic defined inside
`NavHost` by passing an instance of the navigation testing artifact
[`TestNavHostController`](https://developer.android.com/reference/kotlin/androidx/navigation/testing/TestNavHostController). A UI test that verifies the start destination of
your app and `NavHost` would look like this:

    class NavigationTest {

        @get:Rule
        val composeTestRule = createComposeRule()
        lateinit var navController: TestNavHostController

        @Before
        fun setupAppNavHost() {
            composeTestRule.setContent {
                navController = TestNavHostController(LocalContext.current)
                navController.navigatorProvider.addNavigator(ComposeNavigator())
                AppNavHost(navController = navController)
            }
        }

        // Unit test
        @Test
        fun appNavHost_verifyStartDestination() {
            composeTestRule
                .onNodeWithContentDescription("Start Screen")
                .assertIsDisplayed()
        }
    }

### Testing navigation actions

You can test your navigation implementation in multiple ways, by performing
clicks on the UI elements and then either verifying the displayed destination or
by comparing the expected route against the current route.

As you want to test your concrete app's implementation, clicks on the UI are
preferable. To learn how to test this alongside individual composable functions
in isolation, make sure to check out the [Testing in Jetpack Compose](https://developer.android.com/codelabs/jetpack-compose-testing)
codelab.

You also can use the `navController` to check your assertions by comparing the
current route to the expected one, using `navController`'s
`currentBackStackEntry`:

    @Test
    fun appNavHost_clickAllProfiles_navigateToProfiles() {
        composeTestRule.onNodeWithContentDescription("All Profiles")
            .performScrollTo()
            .performClick()

        assertTrue(navController.currentBackStackEntry?.destination?.hasRoute<Profile>() ?: false)
    }

For more guidance on Compose testing basics, see
[Testing your Compose layout](https://developer.android.com/develop/ui/compose/testing) and the [Testing in Jetpack Compose](https://developer.android.com/codelabs/jetpack-compose-testing)
codelab. To learn more about advanced testing of navigation code, visit the
[Test Navigation](https://developer.android.com/guide/navigation/navigation-testing) guide.

## Learn more

To learn more about Jetpack Navigation, see [Get started with the Navigation
component](https://developer.android.com/guide/navigation/navigation-getting-started) or take the [Jetpack Compose Navigation codelab](https://developer.android.com/codelabs/jetpack-compose-navigation).

To learn how to design your app's navigation so it adapts to different screen
sizes, orientations, and form factors, see [Navigation for responsive UIs](https://developer.android.com/guide/topics/large-screens/navigation-for-responsive-uis).

To learn about a more advanced Compose navigation implementation in a
modularized app, including concepts like nested graphs and bottom navigation bar
integration, take a look at the [Now in Android](https://github.com/android/nowinandroid) app on GitHub.

### Samples

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Material Design 2 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material)
- [Migrate Jetpack Navigation to Navigation Compose](https://developer.android.com/develop/ui/compose/migrate/migration-scenarios/navigation)
- [Where to hoist
  state](https://developer.android.com/develop/ui/compose/state-hoisting)