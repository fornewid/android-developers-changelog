---
title: https://developer.android.com/develop/ui/compose/components/fab-menu
url: https://developer.android.com/develop/ui/compose/components/fab-menu
source: md.txt
---

> Documentation index: https://developer.android.com/develop/ui/compose/components/llms.txt

A [floating action button (FAB) menu](https://developer.android.com/reference/kotlin/androidx/compose/material3/FloatingActionButtonMenu.composable.md.txt) opens from a FAB to display multiple
related actions in Material 3.

This keeps key actions accessible while keeping the UI clean by concealing
secondary actions when they aren't needed, replacing speed dials and stacked
small FABs.

## Using the FAB menu

- Opens from a FAB to show two to six related actions floating on screen.
- Uses one FAB menu size across all FAB sizes.
- Isn't used with extended FABs.
- Supports primary, secondary, and tertiary color sets.

![Three FAB menu color sets: primary, secondary, and tertiary.](https://developer.android.com/static/develop/ui/compose/images/components/fab_menu_color_sets.png) **Figure 1.** FAB menu color sets: primary, secondary, and tertiary.

## Examples

### FAB menu sample

Pair [`FloatingActionButtonMenu`](https://developer.android.com/reference/kotlin/androidx/compose/material3/FloatingActionButtonMenu.composable.md.txt) with [`ToggleFloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/ToggleFloatingActionButton.composable.md.txt) to
expand and collapse a list of [`FloatingActionButtonMenuItem`](https://developer.android.com/reference/kotlin/androidx/compose/material3/FloatingActionButtonMenuItem.composable.md.txt) actions. The
following snippet hides the toggle FAB when scrolling down a list and expands
the menu when tapped:


```kotlin
@Composable
fun FloatingActionButtonMenuSample() {
    val listState = rememberLazyListState()
    val fabVisible by remember { derivedStateOf { listState.firstVisibleItemIndex == 0 } }

    Box {
        LazyColumn(state = listState, modifier = Modifier.fillMaxSize()) {
            for (index in 0 until 100) {
                item { Text(text = "List item - $index", modifier = Modifier.padding(24.dp)) }
            }
        }

        val items =
            listOf(
                AppIcons.Message to "Reply",
                AppIcons.People to "Reply all",
                AppIcons.Contacts to "Forward",
                AppIcons.Snooze to "Snooze",
                AppIcons.Archive to "Archive",
                AppIcons.Label to "Label",
            )

        var fabMenuExpanded by rememberSaveable { mutableStateOf(false) }

        FloatingActionButtonMenu(
            modifier = Modifier.align(Alignment.BottomEnd),
            expanded = fabMenuExpanded,
            button = {
                ToggleFloatingActionButton(
                    modifier =
                        Modifier.semantics {
                            traversalIndex = -1f
                            stateDescription = if (fabMenuExpanded) "Expanded" else "Collapsed"
                            contentDescription = "Toggle menu"
                        }
                            .animateFloatingActionButton(
                                visible = fabVisible || fabMenuExpanded,
                                alignment = Alignment.BottomEnd,
                            ),
                    checked = fabMenuExpanded,
                    onCheckedChange = { fabMenuExpanded = !fabMenuExpanded },
                ) {
                    val imageVector by remember {
                        derivedStateOf { if (checkedProgress > 0.5f) AppIcons.Close else AppIcons.Add }
                    }
                    Icon(
                        painter = rememberVectorPainter(imageVector),
                        contentDescription = null,
                        modifier = Modifier.animateIcon({ checkedProgress }),
                    )
                }
            },
        ) {
            items.forEach { item ->
                FloatingActionButtonMenuItem(
                    onClick = { fabMenuExpanded = false },
                    icon = { Icon(painter = rememberVectorPainter(item.first), contentDescription = null) },
                    text = { Text(text = item.second) },
                )
            }
        }
    }
}
```
![A scrollable list of items with an expanded floating action button menu in the bottom-right corner showing 'Reply', 'Reply all', 'Forward', 'Snooze', 'Archive', and 'Label' actions above a close button.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_expressive_components_floatingactionbuttonmenu.png) An expanded floating action button (FAB) menu.

<br />