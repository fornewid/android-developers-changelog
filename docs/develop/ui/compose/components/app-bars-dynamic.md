---
title: https://developer.android.com/develop/ui/compose/components/app-bars-dynamic
url: https://developer.android.com/develop/ui/compose/components/app-bars-dynamic
source: md.txt
---

This guide explains how to create a dynamic top app bar in Compose that changes
its options when items are selected from the list. You can modify the top app
bar's title and actions based on the selection state.

## Implement dynamic top app bar behavior

This code defines a composable function for the top app bar that changes based
on item selection:


```kotlin
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
```

<br />

### Key points about the code

- `AppBarSelectionActions` accepts a `Set` of selected item indexes.
- The `topBarText` changes depending on whether you select any items.
  - When you select items, text describing the number of items selected appears in the [`TopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#TopAppBar(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,androidx.compose.material3.TopAppBarColors,androidx.compose.material3.TopAppBarScrollBehavior)).
  - If you don't select any items, the `topBarText` is "List of items".
- The `actions` block defines the actions you display in the top app bar. If `hasSelection` is true, a share icon appears after the text.
- The `onClick` lambda of the [`IconButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#IconButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.material3.IconButtonColors,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Shape,kotlin.Function0)) handles the share action when you click the icon.

### Result

![A dynamic top app bar displays the text Selected 3 items with a share icon. This text and the icon only appear when items are selected](https://developer.android.com/static/develop/ui/compose/images/components/AppBarSelectionActions.png) **Figure 1.** A dynamic top app bar with text and a share icon that only appear when items are selected.

## Integrate selectable list into dynamic top app bar

This example demonstrates how to add a selectable list to a dynamic top app bar:


```kotlin
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
```

<br />

### Key points about the code

- The top bar updates based on how many list items you select.
- `selectedItems` holds the set of selected item indexes.
- `AppBarMultiSelectionExample` uses a [`Scaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Scaffold(androidx.compose.foundation.layout.WindowInsets,androidx.compose.ui.Modifier,androidx.compose.material.ScaffoldState,kotlin.Function0,kotlin.Function0,kotlin.Function1,kotlin.Function0,androidx.compose.material.FabPosition,kotlin.Boolean,kotlin.Function1,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1)) to structure the screen.
  - `topBar = { AppBarSelectionActions(selectedItems) }` sets the `AppBarSelectionActions` composable as the top app bar. `AppBarSelectionActions` receives the `selectedItems` state.
- [`LazyColumn`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/package-summary#LazyColumn(androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.LazyListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.compose.foundation.OverscrollEffect,kotlin.Function1)) displays the items in a vertical list, rendering only the items visible on the screen.
- `ListItemSelectable` represents a selectable list item.
  - [`combinedClickable`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).combinedClickable(androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.foundation.Indication,kotlin.Boolean,kotlin.String,androidx.compose.ui.semantics.Role,kotlin.String,kotlin.Function0,kotlin.Function0,kotlin.Boolean,kotlin.Function0)) allows both click and long-click handling for item selection. A click performs an action, while long-clicking an item toggles its selection state.

### Result

![A dynamic top app bar displays the text Selected 3 items, followed by a share icon. Below, a list shows several items, with checkmarks next to the three that are selected](https://developer.android.com/static/develop/ui/compose/images/components/AppBarMultiSelectionExample.png) **Figure 2.** A list integrated into a dynamic top app bar with specific items selected.

## Additional resources

- [`TopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#TopAppBar(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,androidx.compose.material3.TopAppBarColors,androidx.compose.material3.TopAppBarScrollBehavior))
- [`LazyColumn`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/package-summary#LazyColumn(androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.LazyListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.compose.foundation.OverscrollEffect,kotlin.Function1))
- [`Scaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Scaffold(androidx.compose.ui.Modifier,androidx.compose.material.ScaffoldState,kotlin.Function0,kotlin.Function0,kotlin.Function1,kotlin.Function0,androidx.compose.material.FabPosition,kotlin.Boolean,kotlin.Function1,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1))