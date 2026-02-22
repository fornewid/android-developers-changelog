---
title: https://developer.android.com/develop/ui/compose/components/tabs
url: https://developer.android.com/develop/ui/compose/components/tabs
source: md.txt
---

Tabs allow you to organize groups of related content. There are two types of
tabs:

- **Primary tabs**: Placed at the top of the content pane under a top app bar. They display the main content destinations, and should be used when just one set of tabs are needed.
- **Secondary tabs**: Used within a content area to further separate related content and establish hierarchy. They are necessary when a screen requires more than one level of tabs.

![3 primary tabs are shown with associated icons (Flights, Trips, and Explore). 2 secondary tabs are shown (Overview, Specifications) without associated icons.](https://developer.android.com/static/develop/ui/compose/images/primary-secondary-tab.png) **Figure 1.** Primary tabs (1) and secondary tabs (2).

This page shows how to display primary tabs in your app with related screens and
basic navigation.

## API surface

Use the [`Tab`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Tab(kotlin.Boolean,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.interaction.MutableInteractionSource)), [`PrimaryTabRow`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#PrimaryTabRow(kotlin.Int,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1,kotlin.Function0,kotlin.Function0)), and [`SecondaryTabRow`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#SecondaryTabRow(kotlin.Int,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1,kotlin.Function0,kotlin.Function0)) composables
to implement tabs. The `Tab` composable represents an individual tab within the
row, and is typically used inside of a `PrimaryTabRow` (for primary indicator
tabs) or `SecondaryTabRow` (for secondary indicator tabs).

`Tab` includes the following key parameters:

- `selected`: Determines whether the current tab is visually highlighted.
- `onClick()`: A required lambda function that defines the action to be performed when the user clicks on the tab. This is where you typically handle navigation events, update the selected tab state, or load corresponding content.
- `text`: Displays text within the tab. Optional.
- `icon`: Displays an icon within the tab. Optional.
- `enabled`: Controls whether the tab is enabled and can be interacted with. If set to false, the tab appears in a disabled state and won't respond to clicks.

## Example: Tab-based navigation

The following snippet implements a top navigation bar with tabs to navigate
between different screens in an app:

> [!NOTE]
> **Note:** The [full source code](https://github.com/android/snippets/blob/main/compose/snippets/src/main/java/com/example/compose/snippets/components/Navigation.kt) includes the code that establishes the basic navigation structure for the following example.


```kotlin
@Composable
fun NavigationTabExample(modifier: Modifier = Modifier) {
    val navController = rememberNavController()
    val startDestination = Destination.SONGS
    var selectedDestination by rememberSaveable { mutableIntStateOf(startDestination.ordinal) }

    Scaffold(modifier = modifier) { contentPadding ->
        PrimaryTabRow(selectedTabIndex = selectedDestination, modifier = Modifier.padding(contentPadding)) {
            Destination.entries.forEachIndexed { index, destination ->
                Tab(
                    selected = selectedDestination == index,
                    onClick = {
                        navController.navigate(route = destination.route)
                        selectedDestination = index
                    },
                    text = {
                        Text(
                            text = destination.label,
                            maxLines = 2,
                            overflow = TextOverflow.Ellipsis
                        )
                    }
                )
            }
        }
        AppNavHost(navController, startDestination)
    }
}
```

<br />

### Key points

- `PrimaryTabRow` displays a horizontal row of tabs, with each tab corresponding to a `Destination`.
- `val navController = rememberNavController()` creates and remembers an instance of [`NavHostController`](https://developer.android.com/reference/androidx/navigation/NavHostController), which manages the navigation within a [`NavHost`](https://developer.android.com/reference/androidx/navigation/NavHost).
- `var selectedDestination by rememberSaveable {
  mutableIntStateOf(startDestination.ordinal) }` manages the state of the selected tab.
  - `startDestination.ordinal` gets the numerical index (position) of the `Destination.SONGS` enum entry.
- When you click a tab, the `onClick` lambda calls `navController.navigate(route = destination.route)` to navigate to the corresponding screen.
- The `onClick` lambda of the `Tab` updates the `selectedDestination` state to visually highlight the clicked tab.
- It calls the `AppNavHost` composable, passing the `navController` and `startDestination`, to display the actual content of the selected screen.

### Result

The following image shows the result of the previous snippet:
![3 tabs arranged horizontally across the top of the app screen. The tabs are Songs, Album, and Playlist, with the Songs tab selected and underlined.](https://developer.android.com/static/develop/ui/compose/images/Tabs (1).png)**Figure 2.** 3 tabs--- Songs, Album, and Playlist--- arranged horizontally.

## Additional resources

- [Material 3 - Tabs](https://m3.material.io/components/tabs/guidelines)
- [Navigation with Compose](https://developer.android.com/develop/ui/compose/navigation)