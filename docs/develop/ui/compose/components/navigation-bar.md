---
title: https://developer.android.com/develop/ui/compose/components/navigation-bar
url: https://developer.android.com/develop/ui/compose/components/navigation-bar
source: md.txt
---

The [navigation bar](https://m3.material.io/components/navigation-bar/overview) allows users to switch between destinations in an app. You
should use navigation bars for:

- Three to five destinations of equal importance
- Compact window sizes
- Consistent destinations across app screens

![A navigation bar with 4 destinations. Each destination has a placeholder name called "Label", with the selected destination appearing with a circle icon, and the rest of the destinations as triangles.](https://developer.android.com/static/develop/ui/compose/images/navigation-bar.png) **Figure 1.** A navigation bar with 4 destinations.

This page shows you how to display a navigation bar in your app with related
screens and basic navigation.

## API surface

Use the [`NavigationBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#NavigationBar(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)) and [`NavigationBarItem`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#(androidx.compose.foundation.layout.RowScope).NavigationBarItem(kotlin.Boolean,kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,kotlin.Boolean,androidx.compose.material3.NavigationBarItemColors,androidx.compose.foundation.interaction.MutableInteractionSource)) composables to
implement destination switching logic. Each `NavigationBarItem` represents a
singular destination.

`NavigationBarItem` includes the following key parameters:

- `selected`: Determines whether the current item is visually highlighted.
- `onClick()`: Defines the action to be performed when the user clicks on the item. Logic for handling navigation events, updating the selected item state, or loading corresponding content belongs here.
- `label`: Displays text within the item. Optional.
- `icon`: Displays an icon within the item. Optional.

## Example: Bottom navigation bar

The following snippet implements a bottom navigation bar with items so users can
navigate between different screens in an app:

> [!NOTE]
> **Note:** The [full source code](https://github.com/android/snippets/blob/main/compose/snippets/src/main/java/com/example/compose/snippets/components/Navigation.kt) includes the code that establishes the basic navigation structure for the following example.


```kotlin
@Composable
fun NavigationBarExample(modifier: Modifier = Modifier) {
    val navController = rememberNavController()
    val startDestination = Destination.SONGS
    var selectedDestination by rememberSaveable { mutableIntStateOf(startDestination.ordinal) }

    Scaffold(
        modifier = modifier,
        bottomBar = {
            NavigationBar(windowInsets = NavigationBarDefaults.windowInsets) {
                Destination.entries.forEachIndexed { index, destination ->
                    NavigationBarItem(
                        selected = selectedDestination == index,
                        onClick = {
                            navController.navigate(route = destination.route)
                            selectedDestination = index
                        },
                        icon = {
                            Icon(
                                destination.icon,
                                contentDescription = destination.contentDescription
                            )
                        },
                        label = { Text(destination.label) }
                    )
                }
            }
        }
    ) { contentPadding ->
        AppNavHost(navController, startDestination, modifier = Modifier.padding(contentPadding))
    }
}
```

<br />

### Key points

- `NavigationBar` displays a collection of items, with each item corresponding to a `Destination`.
- `val navController = rememberNavController()` creates and remembers an instance of [`NavHostController`](https://developer.android.com/reference/androidx/navigation/NavHostController), which manages the navigation within a [`NavHost`](https://developer.android.com/reference/androidx/navigation/NavHost).
- `var selectedDestination by rememberSaveable {
  mutableIntStateOf(startDestination.ordinal) }` manages the state of the selected item.
  - `startDestination.ordinal` gets the numerical index (position) of the `Destination.SONGS` enum entry.
- When an item is clicked, `navController.navigate(route = destination.route)` is called to navigate to the corresponding screen.
- The `onClick` lambda of the `NavigationBarItem` updates the `selectedDestination` state to visually highlight the clicked item.
- The navigation logic calls the `AppNavHost` composable, passing the `navController` and `startDestination`, to display the actual content of the selected screen.

### Result

The following image shows the navigation bar resulting from the previous
snippet:
![An app screen with 3 destinations listed horizontally in a bottom navigation bar: Songs, Album, and Playlist. Each destination has a relevant icon paired with it (e.g., a music note for "Songs").](https://developer.android.com/static/develop/ui/compose/images/NavigationBar.png) **Figure 2.** A navigation bar that contains 3 destinations with associated icons: Songs, Album, and Playlist.

## Additional resources

- [Material 3 - Navigation Bar](https://m3.material.io/components/navigation-bar/overview)
- [Navigation with Compose](https://developer.android.com/develop/ui/compose/navigation)