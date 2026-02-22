---
title: https://developer.android.com/develop/ui/compose/components/navigation-rail
url: https://developer.android.com/develop/ui/compose/components/navigation-rail
source: md.txt
---

Rails provide access to destinations in apps that run on devices with large
screens. You should use navigation rails for:

- Top-level destinations that need to be accessible anywhere in an app
- Three to seven main destinations
- Tablet or desktop layouts

![A vertical navigation rail on the left side of a screen with four destinations (All Files, Recent, Photos, and Library), each with an associated icon, and a floating action button.](https://developer.android.com/static/develop/ui/compose/images/components/navigation-rail.png) **Figure 1.** A navigation rail with four destinations and a floating action button.

This page shows you how to display rails in your app with related screens and
basic navigation.

## API surface

Use the [`NavigationRail`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#NavigationRail(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)) composable with [`NavigationRailItem`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#NavigationRailItem(kotlin.Boolean,kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,kotlin.Boolean,androidx.compose.material3.NavigationRailItemColors,androidx.compose.foundation.interaction.MutableInteractionSource)) to
implement a rail in your application. The `NavigationRailItem` represents a
single rail item in the rail column.

`NavigationRailItem` includes the following key parameters:

- `selected`: Determines whether the current rail item is visually highlighted.
- `onClick()`: A required lambda function that defines the action to be performed when the user clicks on the rail item. This is where you typically handle navigation events, update the selected rail item state, or load corresponding content.
- `label`: Displays text within the rail item. Optional.
- `icon`: Displays an icon within the rail item. Optional.

## Example: Rail-based navigation

The following snippet implements a navigation rail so users can navigate between
different screens in an app:

> [!NOTE]
> **Note:** The [full source code](https://github.com/android/snippets/blob/main/compose/snippets/src/main/java/com/example/compose/snippets/components/Navigation.kt) includes the code that establishes the basic navigation structure for the following example.


```kotlin
@Composable
fun NavigationRailExample(modifier: Modifier = Modifier) {
    val navController = rememberNavController()
    val startDestination = Destination.SONGS
    var selectedDestination by rememberSaveable { mutableIntStateOf(startDestination.ordinal) }

    Scaffold(modifier = modifier) { contentPadding ->
        NavigationRail(modifier = Modifier.padding(contentPadding)) {
            Destination.entries.forEachIndexed { index, destination ->
                NavigationRailItem(
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
        AppNavHost(navController, startDestination)
    }
}
```

<br />

### Key points

- `NavigationRail` displays a vertical column of rail items, with each item corresponding to a `Destination`.
- `val navController = rememberNavController()` creates and remembers an instance of [`NavHostController`](https://developer.android.com/reference/androidx/navigation/NavHostController), which manages the navigation within a [`NavHost`](https://developer.android.com/reference/androidx/navigation/NavHost).
- `var selectedDestination by rememberSaveable {
  mutableIntStateOf(startDestination.ordinal) }` manages the state of the currently selected rail item.
  - `startDestination.ordinal` gets the numerical index (position) of the `Destination.SONGS` enum entry.
- When a rail item is clicked, `navController.navigate(route =
  destination.route)` is called to navigate to the corresponding screen.
- The `onClick` lambda of the `NavigationRailItem` updates the `selectedDestination` state to visually highlight the clicked rail item.
- It calls the `AppNavHost` composable, passing the `navController` and `startDestination`, to display the actual content of the selected screen.

### Result

The following image shows the result of the previous snippet:
![A vertical navigation rail with 3 destinations with associated icons: Songs, Album, and Playlist. Icons visually indicate the purpose of each navigation button in the rail. Each destination has a relevant icon paired with it (e.g., a music note for](https://developer.android.com/static/develop/ui/compose/images/components/navigation-rail-result.png) **Figure 2.** A navigation rail that contains 3 destinations with associated icons: Songs, Album, and Playlist.

## Additional resources

- [Material 3 - Navigation rail](https://m3.material.io/components/navigation-rail/overview)
- [Navigation with Compose](https://developer.android.com/develop/ui/compose/navigation)