---
title: Navigate from top app bar  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/components/app-bars-navigate
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Navigate from top app bar Stay organized with collections Save and categorize content based on your preferences.



This guide demonstrates how you can make the navigation icon in a [top app
bar](https://m3.material.io/components/top-app-bar/overview) perform navigation actions.

**Note:** The example on this page uses `CenterAlignedTopAppBar`, but this is
applicable to any app bar component with a `NavigationIcon` parameter.

## Example

The following snippet is a minimal example of how you can implement a top app
bar with a functional navigation icon. In this case, the icon takes the user to
their previous destination in the app:

```
@Composable
fun TopBarNavigationExample(
    navigateBack: () -> Unit,
) {
    Scaffold(
        topBar = {
            CenterAlignedTopAppBar(
                title = {
                    Text(
                        "Navigation example",
                    )
                },
                navigationIcon = {
                    IconButton(onClick = navigateBack) {
                        Icon(
                            imageVector = Icons.AutoMirrored.Filled.ArrowBack,
                            contentDescription = "Localized description"
                        )
                    }
                },
            )
        },
    ) { innerPadding ->
        Text(
            "Click the back button to pop from the back stack.",
            modifier = Modifier.padding(innerPadding),
        )
    }
}

AppBar.kt
```

### Key points about the code

Note the following in this example:

* The composable `TopBarNavigationExample` defines a parameter `navigateBack`
  of type `() -> Unit`.
* It passes `navigateBack` for the `navigationIcon` parameter of
  `CenterAlignedTopAppBar`.

As such, whenever the user clicks the navigation icon in the top app back, it
calls `navigateBack()`.

### Pass a function

This example uses a back arrow for the icon. As such, the argument for
`navigateBack()` should take the user to the previous destination.

To do so, pass `TopBarNavigationExample` a call to
[`NavController.popBackStack()`](/guide/navigation/backstack). You do this where you [build your
navigation](/guide/navigation/design#compose) graph. For example:

```
NavHost(navController, startDestination = "home") {
    composable("topBarNavigationExample") {
        TopBarNavigationExample{ navController.popBackStack() }
    }
    // Other destinations...
```

**Note:** Using the same approach, you could implement a different action for the
navigation icon. For example, you could use a house icon and pass a call to
`navController.navigate("home")`.

## Additional resources

For more information on how to implement navigation in your app, see the
following series of guides:

* [Navigation with Compose](/develop/ui/compose/navigation)
* [Create a NavController](/develop/ui/compose/navigation#navcontroller)
* [Design your navigation graph](/guide/navigation/design#compose)
* [Navigate to a composable](/develop/ui/compose/navigation#nav-to-composable)