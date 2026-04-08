---
title: Create a dynamic top app bar  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/components/app-bars-dynamic
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Create a dynamic top app bar Stay organized with collections Save and categorize content based on your preferences.




This guide explains how to create a dynamic top app bar in Compose that changes
its options when items are selected from the list. You can modify the top app
bar's title and actions based on the selection state.

## Implement dynamic top app bar behavior

This code defines a composable function for the top app bar that changes based
on item selection:

```
@Composable
fun AppBarSelectionActions(
    selectedItems: Set<Int>,
    modifier: Modifier = Modifier,
) {
    val hasSelection = selectedItems.isNotEmpty()
    val topBarText = if (hasSelection) {
        "Selected ${selectedItems.size} items"
    } else {
        "List of items"
    }

    TopAppBar(
        title = {
            Text(topBarText)
        },
        colors = TopAppBarDefaults.topAppBarColors(
            containerColor = MaterialTheme.colorScheme.primaryContainer,
            titleContentColor = MaterialTheme.colorScheme.primary,
        ),
        actions = {
            if (hasSelection) {
                IconButton(onClick = {
                    /* click action */
                }) {
                    Icon(
                        imageVector = Icons.Filled.Share,
                        contentDescription = "Share items"
                    )
                }
            }
        },
        modifier = modifier
    )
}

AppBar.kt
```

### Key points about the code

* `AppBarSelectionActions` accepts a `Set` of selected item indexes.
* The `topBarText` changes depending on whether you select any items.
  + When you select items, text describing the number of items selected
    appears in the [`TopAppBar`](/reference/kotlin/androidx/compose/material3/TopAppBar.composable).
  + If you don't select any items, the `topBarText` is "List of items".
* The `actions` block defines the actions you display in the top app bar. If
  `hasSelection` is true, a share icon appears after the text.
* The `onClick` lambda of the [`IconButton`](/reference/kotlin/androidx/compose/material3/IconButton.composable#IconButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.material3.IconButtonColors,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Shape,kotlin.Function0)) handles the share action when
  you click the icon.

### Result

![A dynamic top app bar displays the text Selected 3 items with a share icon. This text and the icon only appear when items are selected](/static/develop/ui/compose/images/components/AppBarSelectionActions.png)


**Figure 1.** A dynamic top app bar with text and a share icon that only appear when items are selected.

## Integrate selectable list into dynamic top app bar

This example demonstrates how to add a selectable list to a dynamic top app bar:

```
@Composable
private fun AppBarMultiSelectionExample(
    modifier: Modifier = Modifier,
) {
    val listItems by remember { mutableStateOf(listOf(1, 2, 3, 4, 5, 6)) }
    var selectedItems by rememberSaveable { mutableStateOf(setOf<Int>()) }

    Scaffold(
        modifier = modifier,
        topBar = { AppBarSelectionActions(selectedItems) }
    ) { innerPadding ->
        LazyColumn(contentPadding = innerPadding) {
            itemsIndexed(listItems) { _, index ->
                val isItemSelected = selectedItems.contains(index)
                ListItemSelectable(
                    selected = isItemSelected,
                    Modifier
                        .combinedClickable(
                            interactionSource = remember { MutableInteractionSource() },
                            indication = null,
                            onClick = {
                                /* click action */
                            },
                            onLongClick = {
                                if (isItemSelected) selectedItems -= index else selectedItems += index
                            }
                        )
                )
            }
        }
    }
}

AppBar.kt
```

### Key points about the code

* The top bar updates based on how many list items you select.
* `selectedItems` holds the set of selected item indexes.
* `AppBarMultiSelectionExample` uses a [`Scaffold`](/reference/kotlin/androidx/compose/material/Scaffold.composable#Scaffold(androidx.compose.foundation.layout.WindowInsets,androidx.compose.ui.Modifier,androidx.compose.material.ScaffoldState,kotlin.Function0,kotlin.Function0,kotlin.Function1,kotlin.Function0,androidx.compose.material.FabPosition,kotlin.Boolean,kotlin.Function1,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1)) to structure the
  screen.
  + `topBar = { AppBarSelectionActions(selectedItems) }` sets the
    `AppBarSelectionActions` composable as the top app bar.
    `AppBarSelectionActions` receives the `selectedItems` state.
* [`LazyColumn`](/reference/kotlin/androidx/compose/foundation/lazy/LazyColumn.composable#LazyColumn(androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.LazyListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.compose.foundation.OverscrollEffect,kotlin.Function1)) displays the items in a vertical list, rendering only the
  items visible on the screen.
* `ListItemSelectable` represents a selectable list item.
  + [`combinedClickable`](/reference/kotlin/androidx/compose/foundation/combinedClickable.modifier#(androidx.compose.ui.Modifier).combinedClickable(androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.foundation.Indication,kotlin.Boolean,kotlin.String,androidx.compose.ui.semantics.Role,kotlin.String,kotlin.Function0,kotlin.Function0,kotlin.Boolean,kotlin.Function0)) allows both click and long-click handling for
    item selection. A click performs an action, while long-clicking an item
    toggles its selection state.

### Result

![A dynamic top app bar displays the text Selected 3 items, followed by a share icon. Below, a list shows several items, with checkmarks next to the three that are selected](/static/develop/ui/compose/images/components/AppBarMultiSelectionExample.png)


**Figure 2.** A list integrated into a dynamic top app bar with specific items selected.

## Additional resources

* [`TopAppBar`](/reference/kotlin/androidx/compose/material3/TopAppBar.composable)
* [`LazyColumn`](/reference/kotlin/androidx/compose/foundation/lazy/LazyColumn.composable#LazyColumn(androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.LazyListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.compose.foundation.OverscrollEffect,kotlin.Function1))
* [`Scaffold`](/reference/kotlin/androidx/compose/material/Scaffold.composable#Scaffold(androidx.compose.ui.Modifier,androidx.compose.material.ScaffoldState,kotlin.Function0,kotlin.Function0,kotlin.Function1,kotlin.Function0,androidx.compose.material.FabPosition,kotlin.Boolean,kotlin.Function1,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1))