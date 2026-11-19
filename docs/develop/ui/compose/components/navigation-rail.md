---
title: https://developer.android.com/develop/ui/compose/components/navigation-rail
url: https://developer.android.com/develop/ui/compose/components/navigation-rail
source: md.txt
---

> Documentation index: https://developer.android.com/develop/ui/compose/components/llms.txt

[Navigation rails](https://m3.material.io/components/navigation-rail/guidelines#b51e4558-351f-4368-af8d-bbf1f63f68b4) provide access to destinations in apps that run on devices
with large screens. You should use navigation rails for:

- Top-level destinations that need to be accessible anywhere in an app
- Three to seven main destinations
- Tablet or desktop layouts

![A vertical navigation rail on the left side of a screen with four destinations (All Files, Recent, Photos, and Library), each with an associated icon, and a floating action button.](https://developer.android.com/static/develop/ui/compose/images/components/navigation-rail.png) **Figure 1.** A navigation rail with four destinations and a floating action button.

This page shows you how to display rails in your app with related screens and
basic navigation.

## API surface

Use the [`NavigationRail`](https://developer.android.com/reference/kotlin/androidx/compose/material3/NavigationRail.composable.md.txt#NavigationRail(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)) composable with [`NavigationRailItem`](https://developer.android.com/reference/kotlin/androidx/compose/material3/NavigationRailItem.composable.md.txt#NavigationRailItem(kotlin.Boolean,kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,kotlin.Boolean,androidx.compose.material3.NavigationRailItemColors,androidx.compose.foundation.interaction.MutableInteractionSource)) to
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
- `val navController = rememberNavController()` creates and remembers an instance of [`NavHostController`](https://developer.android.com/reference/androidx/navigation/NavHostController.md.txt), which manages the navigation within a [`NavHost`](https://developer.android.com/reference/androidx/navigation/NavHost.md.txt).
- `var selectedDestination by rememberSaveable {
  mutableIntStateOf(startDestination.ordinal) }` manages the state of the selected rail item.
  - `startDestination.ordinal` gets the numerical index (position) of the `Destination.SONGS` enum entry.
- When a rail item is clicked, `navController.navigate(route =
  destination.route)` is called to navigate to the corresponding screen.
- The `onClick` lambda of the `NavigationRailItem` updates the `selectedDestination` state to visually highlight the clicked rail item.
- It calls the `AppNavHost` composable, passing the `navController` and `startDestination`, to display the actual content of the selected screen.

### Result

The following image shows the result of the previous snippet:
![A navigation rail with Songs, Album and Playlist destinations next to a screen that reads 'Songs Screen'; Songs is selected.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_components_navigationrailexample.png) **Figure 2.** A navigation rail that contains 3 destinations with associated icons: Songs, Album, and Playlist.

## M3 Expressive update

Material 3 Expressive introduces `WideNavigationRail` and
`ModalWideNavigationRail`, which support collapsed and expanded states as
additional options alongside the standard `NavigationRail`.
![Image showing two navigation rails: one collapsed showing only icons, and one expanded showing icons and labels.](https://developer.android.com/static/develop/ui/compose/images/components/navigation_rail_expressive.png) **Figure 3.** Collapsed and expanded navigation rails.

For more information about the M3 Expressive updates for navigation rails, see
the [Material Design 3 navigation rail guidelines](https://m3.material.io/components/navigation-rail/guidelines#b51e4558-351f-4368-af8d-bbf1f63f68b4).

### Collapsed and expanded wide navigation rail

A wide navigation rail has two states, collapsed and expanded, which can
transform into each other when the user selects the menu button. The following
snippet demonstrates how to implement a `WideNavigationRail` that animates
between collapsed and expanded states:


```kotlin
@Composable
fun WideNavigationRailResponsiveSample() {
    var selectedItem by remember { mutableIntStateOf(0) }
    val items = listOf("Home", "Search", "Settings")
    val selectedIcons = listOf(AppIcons.HomeFilled, AppIcons.Search, AppIcons.SettingsFilled)
    val unselectedIcons = listOf(AppIcons.Home, AppIcons.Search, AppIcons.Settings)
    val state = rememberWideNavigationRailState()
    val scope = rememberCoroutineScope()

    Row(Modifier.fillMaxWidth()) {
        WideNavigationRail(
            state = state,
            header = {
                IconButton(
                    modifier =
                        Modifier
                            .padding(start = 24.dp)
                            .semantics {
                                // The button must announce the expanded or collapsed state of the rail
                                // for accessibility.
                                stateDescription =
                                    if (state.currentValue == WideNavigationRailValue.Expanded) "Expanded"
                                    else "Collapsed"
                            },
                    onClick = {
                        scope.launch {
                            if (state.targetValue == WideNavigationRailValue.Expanded) state.collapse()
                            else state.expand()
                        }
                    },
                ) {
                    if (state.targetValue == WideNavigationRailValue.Expanded) {
                        Icon(painter = rememberVectorPainter(AppIcons.MenuOpen), "Collapse rail")
                    } else {
                        Icon(painter = rememberVectorPainter(AppIcons.Menu), "Expand rail")
                    }
                }
            },
        ) {
            items.forEachIndexed { index, item ->
                WideNavigationRailItem(
                    railExpanded = state.targetValue == WideNavigationRailValue.Expanded,
                    icon = {
                        val imageVector =
                            if (selectedItem == index) {
                                selectedIcons[index]
                            } else {
                                unselectedIcons[index]
                            }
                        Icon(
                            painter = rememberVectorPainter(imageVector),
                            contentDescription = null
                        )
                    },
                    label = { Text(item) },
                    selected = selectedItem == index,
                    onClick = { selectedItem = index },
                )
            }
        }

        val textString =
            if (state.currentValue == WideNavigationRailValue.Expanded) "expanded" else "collapsed"
        Column {
            Text(modifier = Modifier.padding(16.dp), text = "The rail is $textString.")
        }
    }
}
```
![A collapsed wide navigation rail on the left with a menu button and 'Home' (selected), 'Search', and 'Settings' items, beside the text 'The rail is collapsed.'.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_expressive_components_widenavigationrailexample.png) A wide navigation rail that toggles between collapsed and expanded states.

<br />

### Modal wide navigation rail

The expanded navigation rail can be standard or modal. The modal configuration
overlaps the body content and opens from a menu icon. The following snippet
demonstrates how to implement a `ModalWideNavigationRail`:


```kotlin
@Composable
fun ModalWideNavigationRailSample() {
    var selectedItem by remember { mutableIntStateOf(0) }
    val items = listOf("Home", "Search", "Settings")
    val selectedIcons = listOf(AppIcons.HomeFilled, AppIcons.Search, AppIcons.SettingsFilled)
    val unselectedIcons = listOf(AppIcons.Home, AppIcons.Search, AppIcons.Settings)
    val state = rememberWideNavigationRailState()
    val scope = rememberCoroutineScope()

    Row(Modifier.fillMaxWidth()) {
        ModalWideNavigationRail(
            state = state,
            // Note: the value of expandedHeaderTopPadding depends on the layout of your screen in
            // order to achieve the best alignment.
            expandedHeaderTopPadding = 64.dp,
            header = {
                IconButton(
                    modifier =
                        Modifier
                            .padding(start = 24.dp)
                            .semantics {
                                // The button must announce the expanded or collapsed state of the rail
                                // for accessibility.
                                stateDescription =
                                    if (state.currentValue == WideNavigationRailValue.Expanded) "Expanded"
                                    else "Collapsed"
                            },
                    onClick = {
                        scope.launch {
                            if (state.targetValue == WideNavigationRailValue.Expanded) state.collapse()
                            else state.expand()
                        }
                    },
                ) {
                    if (state.targetValue == WideNavigationRailValue.Expanded)
                        Icon(painter = rememberVectorPainter(AppIcons.MenuOpen), "Collapse rail")
                    else Icon(painter = rememberVectorPainter(AppIcons.Menu), "Expand rail")
                }
            },
        ) {
            items.forEachIndexed { index, item ->
                WideNavigationRailItem(
                    railExpanded = state.targetValue == WideNavigationRailValue.Expanded,
                    icon = {
                        Icon(
                            painter = rememberVectorPainter(if (selectedItem == index) selectedIcons[index] else unselectedIcons[index]),
                            contentDescription = null,
                        )
                    },
                    label = { Text(item) },
                    selected = selectedItem == index,
                    onClick = { selectedItem = index },
                )
            }
        }

        val textString =
            if (state.currentValue == WideNavigationRailValue.Expanded) "expanded" else "collapsed"
        Column {
            Text(modifier = Modifier.padding(16.dp), text = "The rail is $textString.")
        }
    }
}
```
![A collapsed modal wide navigation rail on the left with a menu button and 'Home' (selected), 'Search', and 'Settings' items, beside the text 'The rail is collapsed.'.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_expressive_components_modalwidenavigationrailexample.png) A modal wide navigation rail.

<br />

> [!NOTE]
> **Note:** If there are more than four destinations, consider using a [modal expanded
> navigation rail](https://developer.android.com/reference/kotlin/androidx/compose/material3/ModalWideNavigationRail.composable) instead.

### Dismissible modal wide navigation rail

On Android, predictive back gestures let users swipe left or right on the screen
to go back or dismiss modal components. The following snippet demonstrates how
to implement a dismissible `ModalWideNavigationRail` by setting
`hideOnCollapse = true`:


```kotlin
@Composable
fun DismissibleModalWideNavigationRailSample() {
    var selectedItem by remember { mutableIntStateOf(0) }
    val items = listOf("Home", "Search", "Settings")
    val selectedIcons = listOf(AppIcons.HomeFilled, AppIcons.Search, AppIcons.SettingsFilled)
    val unselectedIcons = listOf(AppIcons.Home, AppIcons.Search, AppIcons.Settings)
    val state = rememberWideNavigationRailState()
    val scope = rememberCoroutineScope()

    Row(Modifier.fillMaxSize()) {
        ModalWideNavigationRail(state = state, hideOnCollapse = true) {
            items.forEachIndexed { index, item ->
                WideNavigationRailItem(
                    railExpanded = true,
                    icon = {
                        Icon(
                            painter = rememberVectorPainter(if (selectedItem == index) selectedIcons[index] else unselectedIcons[index]),
                            contentDescription = null,
                        )
                    },
                    label = { Text(item) },
                    selected = selectedItem == index,
                    onClick = {
                        selectedItem = index
                        scope.launch { state.collapse() }
                    },
                )
            }
        }

        Column(Modifier.fillMaxWidth(), horizontalAlignment = Alignment.CenterHorizontally) {
            val currentPage = items.get(selectedItem)
            Button(onClick = { scope.launch { state.expand() } }, Modifier.padding(32.dp)) {
                Text(text = "$currentPage Page\nOpen modal rail", textAlign = TextAlign.Center)
            }
        }
    }
}
```
![An expanded dismissible modal wide navigation rail with 'Home' (selected), 'Search', and 'Settings' items overlapping a dimmed screen with a button reading 'Home Page Open modal rail'.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_expressive_components_dismissiblemodalwidenavigationrailexample.png) A dismissible modal wide navigation rail.

<br />

## Additional resources

- [Material 3 - Navigation rail](https://m3.material.io/components/navigation-rail/overview)
- [Navigation with Compose](https://developer.android.com/guide/navigation.md.txt#framework-options)