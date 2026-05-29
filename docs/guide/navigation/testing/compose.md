---
title: https://developer.android.com/guide/navigation/testing/compose
url: https://developer.android.com/guide/navigation/testing/compose
source: md.txt
---

Decouple the navigation code from your composable destinations to enable testing
each composable in isolation, separate from the `NavHost` composable.

Don't pass the `NavController` directly into any composable. Instead, pass
navigation callbacks (lambdas) as parameters. This allows all your composables
to be individually testable, as they don't require an instance of
`NavController` in tests.

The `composable` lambda in your `NavHost` acts as a bridge between the
Navigation APIs and your composable:

    @Composable
    fun ProfileScreen(
        userId: String,
        navigateToFriendProfile: (friendUserId: String) -> Unit
    ) {
     // ...
    }

    // In your NavHost
    composable<Profile> { backStackEntry ->
        val profile = backStackEntry.toRoute<Profile>()
        ProfileScreen(userId = profile.id) { friendUserId ->
            navController.navigate(route = Profile(id = friendUserId))
        }
    }

This way, `ProfileScreen` can be tested independently of Navigation by passing
mock values and callbacks.

It is recommended to write tests that cover your app navigation requirements by
testing the `NavHost`, navigation actions passed to your composables, and your
individual screen composables.

## Test the NavHost

To begin testing your `NavHost`, add the following navigation-testing
dependency to your app module's `build.gradle` file:

    dependencies {
      androidTestImplementation "androidx.navigation:navigation-testing:$navigationVersion"
    }

Wrap your app's `NavHost` in a composable which accepts a
[`NavHostController`](https://developer.android.com/reference/androidx/navigation/NavHostController) as a parameter:

    @Composable
    fun AppNavHost(navController: NavHostController){
      NavHost(navController = navController, startDestination = Home){
          composable<Home> { /*...*/ }
          composable<Profile> { /*...*/ }
      }
    }

Now you can test `AppNavHost` and the navigation logic defined inside `NavHost`
by passing an instance of the navigation testing artifact
[`TestNavHostController`](https://developer.android.com/reference/kotlin/androidx/navigation/testing/TestNavHostController).

A UI test that verifies the start destination of your app and `NavHost` would
look like this:

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

        @Test
        fun appNavHost_verifyStartDestination() {
            composeTestRule
                .onNodeWithContentDescription("Start Screen")
                .assertIsDisplayed()
        }
    }

## Test navigation actions

You can test your navigation implementation in multiple ways, by performing
clicks on the UI elements and then either verifying the displayed destination or
by comparing the expected route against the current route.

As you want to test your concrete app's implementation, clicks on the UI are
preferable. To learn how to test this alongside individual composable functions
in isolation, see the [Testing in Jetpack Compose](https://developer.android.com/codelabs/jetpack-compose-testing)
codelab.

You can also use the `navController` to check navigation assertions by comparing
the current route to the expected one, using the `currentBackStackEntry`:

    @Test
    fun appNavHost_clickProfile_navigatesToProfile() {
        composeTestRule.onNodeWithContentDescription("Go to Profile")
            .performClick()

        assertTrue(navController.currentBackStackEntry?.destination?.hasRoute<Profile>() ?: false)
    }

For more guidance on Compose testing basics, see the
[Testing your Compose layout](https://developer.android.com/develop/ui/compose/testing) guide.