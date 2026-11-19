---
title: https://developer.android.com/develop/ui/compose/components/menu
url: https://developer.android.com/develop/ui/compose/components/menu
source: md.txt
---

> Documentation index: https://developer.android.com/develop/ui/compose/components/llms.txt

Drop-down [menus](https://m3.material.io/components/menus/guidelines#4d2ca9a5-906c-43fe-95e2-c02871619f19) let users click an icon, text field, or other component,
and then select from a list of options on a temporary surface. This guide
describes how to create both basic menus and more complex menus with dividers
and icons.
![A dropdown menu with two options displayed. An icon with three vertical dots indicates that clicking it opens the menu.](https://developer.android.com/static/develop/ui/compose/images/components/basicmenu1.png) **Figure 1.** A basic drop-down menu with two items listed.

## API surface

Use [`DropdownMenu`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary.md.txt#DropdownMenu(kotlin.Boolean,kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.unit.DpOffset,androidx.compose.foundation.ScrollState,androidx.compose.ui.window.PopupProperties,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.foundation.BorderStroke,kotlin.Function1)), [`DropdownMenuItem`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary.md.txt#DropdownMenuItem(kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.material3.MenuItemColors,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource)), [`IconButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary.md.txt#IconButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.material3.IconButtonColors,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Shape,kotlin.Function0)), and
[`ExposedDropdownMenuBox`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary.md.txt#ExposedDropdownMenuBox(kotlin.Boolean,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1)) components to implement drop-down menus. The
`DropdownMenu` and `DropdownMenuItem` components are used to display the menu
items, while `IconButton` or other components can trigger the menu display.
`ExposedDropdownMenuBox` is used to create a menu attached to a text field.

The key parameters for the `DropdownMenu` component include the following:

- `expanded`: Indicates whether the menu is visible.
- `onDismissRequest`: Used to handle menu dismissal.
- `content`: The composable content of the menu, typically containing `DropdownMenuItem` composables.

The key parameters for `DropdownMenuItem` include the following:

- `text`: Defines the content displayed in the menu item.
- `onClick`: Callback to handle interaction with the item in the menu.

## Create a basic drop-down menu

The following snippet demonstrates a minimal `DropdownMenu` implementation:


```kotlin
@Composable
fun MinimalDropdownMenu() {
    var expanded by remember { mutableStateOf(false) }
    Box(
        modifier = Modifier
            .padding(16.dp)
    ) {
        IconButton(onClick = { expanded = !expanded }) {
            Icon(painter = rememberVectorPainter(AppIcons.MoreVert), contentDescription = "More options")
        }
        DropdownMenu(
            expanded = expanded,
            onDismissRequest = { expanded = false }
        ) {
            DropdownMenuItem(
                text = { Text("Option 1") },
                onClick = { /* Do something... */ }
            )
            DropdownMenuItem(
                text = { Text("Option 2") },
                onClick = { /* Do something... */ }
            )
        }
    }
}
```

<br />

### Key points about the code

- Defines a basic `DropdownMenu` containing two menu items.
- The `expanded` parameter controls the menu's visibility as expanded or collapsed.
- The `onDismissRequest` parameter defines a callback that executes when the user closes the menu.
- The `DropdownMenuItem` composable represents selectable items in the drop-down menu.
- An `IconButton` triggers the expansion and collapse of the menu.

### Result

![An open drop-down menu with two items, 'Option 1' and 'Option 2'.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_components_minimaldropdownmenu.png) **Figure 2.** A minimal drop-down menu with only two options.

## Create a longer drop-down menu

`DropdownMenu` is scrollable by default if all the menu items can't be displayed
at once. The following snippet creates a longer, scrollable drop-down menu:


```kotlin
@Composable
fun LongBasicDropdownMenu() {
    var expanded by remember { mutableStateOf(false) }
    // Placeholder list of 100 strings for demonstration
    val menuItemData = List(100) { "Option ${it + 1}" }

    Box(
        modifier = Modifier
            .padding(16.dp)
    ) {
        IconButton(onClick = { expanded = !expanded }) {
            Icon(painter = rememberVectorPainter(AppIcons.MoreVert), contentDescription = "More options")
        }
        DropdownMenu(
            expanded = expanded,
            onDismissRequest = { expanded = false }
        ) {
            menuItemData.forEach { option ->
                DropdownMenuItem(
                    text = { Text(option) },
                    onClick = { /* Do something... */ }
                )
            }
        }
    }
}
```

<br />

### Key points about the code

- The `DropdownMenu` is scrollable when the total height of its content exceeds the available space. This code creates a scrollable `DropdownMenu` that displays 100 placeholder items.
- The `forEach` loop dynamically generates `DropdownMenuItem` composables. The items are not lazily created, which means that all 100 drop-down items are created and exist in the composition.
- The `IconButton` triggers the expansion and collapse of the `DropdownMenu` when clicked.
- The `onClick` lambda within each `DropdownMenuItem` lets you define the action performed when the user selects a menu item.

### Result

The preceding code snippet produces the following scrollable menu:
![An open, scrollable drop-down menu that lists items from 'Option 1' to 'Option 6', with more below.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_components_longbasicdropdownmenu.png) **Figure 3.** A long, scrollable drop-down menu.

## Create a longer drop-down menu with dividers

The following snippet shows a more advanced implementation of a drop-down menu.
In this snippet, leading and trailing icons are added to menu items, and
dividers separate groups of menu items.


```kotlin
@Composable
fun DropdownMenuWithDetails() {
    var expanded by remember { mutableStateOf(false) }

    Box(
        modifier = Modifier
            .fillMaxWidth()
            .padding(16.dp)
    ) {
        IconButton(onClick = { expanded = !expanded }) {
            Icon(painter = rememberVectorPainter(AppIcons.MoreVert), contentDescription = "More options")
        }
        DropdownMenu(
            expanded = expanded,
            onDismissRequest = { expanded = false }
        ) {
            // First section
            DropdownMenuItem(
                text = { Text("Profile") },
                leadingIcon = { Icon(painter = rememberVectorPainter(AppIcons.Person), contentDescription = null) },
                onClick = { /* Do something... */ }
            )
            DropdownMenuItem(
                text = { Text("Settings") },
                leadingIcon = { Icon(painter = rememberVectorPainter(AppIcons.Settings), contentDescription = null) },
                onClick = { /* Do something... */ }
            )

            HorizontalDivider()

            // Second section
            DropdownMenuItem(
                text = { Text("Send Feedback") },
                leadingIcon = { Icon(painter = rememberVectorPainter(AppIcons.Feedback), contentDescription = null) },
                trailingIcon = { Icon(painter = rememberVectorPainter(AppIcons.Send), contentDescription = null) },
                onClick = { /* Do something... */ }
            )

            HorizontalDivider()

            // Third section
            DropdownMenuItem(
                text = { Text("About") },
                leadingIcon = { Icon(painter = rememberVectorPainter(AppIcons.Info), contentDescription = null) },
                onClick = { /* Do something... */ }
            )
            DropdownMenuItem(
                text = { Text("Help") },
                leadingIcon = { Icon(painter = rememberVectorPainter(AppIcons.Help), contentDescription = null) },
                trailingIcon = { Icon(painter = rememberVectorPainter(AppIcons.OpenInNew), contentDescription = null) },
                onClick = { /* Do something... */ }
            )
        }
    }
}
```

<br />

This code defines a `DropdownMenu` within a `Box`.

### Key points about the code

- The `leadingIcon` and `trailingIcon` parameters add icons to the start and end of a `DropdownMenuItem`.
- An `IconButton` triggers the menu's expansion.
- The `DropdownMenu` contains several `DropdownMenuItem` composables, each representing a selectable action.
- [`HorizontalDivider`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary.md.txt#HorizontalDivider(androidx.compose.ui.Modifier,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color)) composables insert a horizontal line to separate groups of menu items.

### Result

The preceding snippet produces a drop-down menu with icons and dividers:
![An open drop-down menu with leading icons, divided into three sections: 'Profile' and 'Settings'; 'Send Feedback' with a trailing send icon; and 'About' and 'Help' with a trailing open-in-new icon.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_components_dropdownmenuwithdetails.png) **Figure 4.** A drop-down menu divided into sections with leading and trailing icons.

## M3 Expressive update

Material 3 Expressive introduces `DropdownMenuPopup`, `DropdownMenuGroup`, and
`CheckableDropdownMenuItem` as additional options alongside `DropdownMenu` and
`DropdownMenuItem` to create segmented menus with grouped items, gaps, and
checkable states.
![M3 expressive menu examples.](https://developer.android.com/static/develop/ui/compose/images/components/expressive_menu.png) **Figure 5.** Material 3 Expressive vertical menu variations with gaps (1, left) and dividers (2, right).

For more information about the M3 Expressive updates for menus, see the
[Material Design 3 menus guidelines](https://m3.material.io/components/menus/guidelines#4d2ca9a5-906c-43fe-95e2-c02871619f19).

### Segmented menus

Segmented menus group related actions into distinct visual sections separated by
gaps or dividers. The following snippet demonstrates how to implement a
segmented drop-down menu with `DropdownMenuPopup`, `DropdownMenuGroup`, and
`CheckableDropdownMenuItem`:


```kotlin
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun GroupedMenuSample() {
    val groupInteractionSource = remember { MutableInteractionSource() }
    var expanded by remember { mutableStateOf(false) }
    val groupLabels = listOf("Modification", "Navigation")
    val groupItemLabels = listOf(listOf("Edit", "Settings"), listOf("Home", "More Options"))
    val groupItemLeadingIcons =
        listOf(listOf(AppIcons.Edit, AppIcons.Settings), listOf(null, AppIcons.Info))
    val groupItemCheckedLeadingIcons =
        listOf(
            listOf(AppIcons.EditFilled, AppIcons.SettingsFilled),
            listOf(AppIcons.Check, AppIcons.InfoFilled),
        )
    val groupItemTrailingIcons: List<List<ImageVector?>> =
        listOf(listOf(null, null), listOf(AppIcons.Home, AppIcons.MoreVert))
    val groupItemCheckedTrailingIcons: List<List<ImageVector?>> =
        listOf(listOf(null, null), listOf(AppIcons.HomeFilled, AppIcons.MoreVert))
    val groupItemSupportingText: List<List<String?>> =
        listOf(listOf("Edit mode", null), listOf(null, "Opens menu"))
    val checked = remember {
        listOf(mutableStateListOf(false, false), mutableStateListOf(false, false))
    }

    Box(modifier = Modifier.fillMaxSize().wrapContentSize(Alignment.TopStart)) {
        // Icon button should have a tooltip associated with it for a11y.
        TooltipBox(
            positionProvider =
                TooltipDefaults.rememberTooltipPositionProvider(TooltipAnchorPosition.Above),
            tooltip = { PlainTooltip { Text("Localized description") } },
            state = rememberTooltipState(),
        ) {
            IconButton(onClick = { expanded = true }) {
                Icon(painter = rememberVectorPainter(AppIcons.MoreVert), contentDescription = "Localized description")
            }
        }
        DropdownMenuPopup(expanded = expanded, onDismissRequest = { expanded = false }) {
            val groupCount = groupLabels.size
            groupLabels.fastForEachIndexed { groupIndex, label ->
                DropdownMenuGroup(
                    shapes = MenuDefaults.groupShape(groupIndex, groupCount),
                    interactionSource = groupInteractionSource,
                ) {
                    MenuDefaults.DropdownMenuGroupLabel { Text(label) }
                    HorizontalDivider(modifier = Modifier.padding(MenuDefaults.HorizontalDividerPadding))
                    val groupItemCount = groupItemLabels[groupIndex].size
                    groupItemLabels[groupIndex].fastForEachIndexed { itemIndex, itemLabel ->
                        CheckableDropdownMenuItem(
                            text = { Text(itemLabel) },
                            supportingText =
                                groupItemSupportingText[groupIndex][itemIndex]?.let { supportingText ->
                                    { Text(supportingText) }
                                },
                            shapes = MenuDefaults.itemShape(itemIndex, groupItemCount),
                            leadingIcon =
                                groupItemLeadingIcons[groupIndex][itemIndex]?.let { iconData ->
                                    {
                                        Icon(
                                            painter = rememberVectorPainter(iconData),
                                            modifier = Modifier.size(MenuDefaults.LeadingIconSize),
                                            contentDescription = null,
                                        )
                                    }
                                },
                            checkedLeadingIcon = {
                                Icon(
                                    painter = rememberVectorPainter(groupItemCheckedLeadingIcons[groupIndex][itemIndex]),
                                    modifier = Modifier.size(MenuDefaults.LeadingIconSize),
                                    contentDescription = null,
                                )
                            },
                            trailingContent =
                                if (checked[groupIndex][itemIndex]) {
                                    groupItemCheckedTrailingIcons[groupIndex][itemIndex]?.let { iconData ->
                                        {
                                            Icon(
                                                painter = rememberVectorPainter(iconData),
                                                modifier = Modifier.size(MenuDefaults.TrailingIconSize),
                                                contentDescription = null,
                                            )
                                        }
                                    }
                                } else {
                                    groupItemTrailingIcons[groupIndex][itemIndex]?.let { iconData ->
                                        {
                                            Icon(
                                                painter = rememberVectorPainter(iconData),
                                                modifier = Modifier.size(MenuDefaults.TrailingIconSize),
                                                contentDescription = null,
                                            )
                                        }
                                    }
                                },
                            checked = checked[groupIndex][itemIndex],
                            onCheckedChange = { checked[groupIndex][itemIndex] = it },
                        )
                    }
                }

                if (groupIndex != groupCount - 1) {
                    Spacer(Modifier.height(MenuDefaults.GroupSpacing))
                }
            }
            if (checked.last().last()) {
                DropdownMenuButtonGroup()
            }
        }
    }
}

@Composable
private fun DropdownMenuButtonGroup() {
    ButtonGroup(
        overflowIndicator = { menuState -> ButtonGroupDefaults.OverflowIndicator(menuState) },
        modifier = Modifier.fillMaxWidth(),
        horizontalArrangement = Arrangement.spacedBy(2.dp, Alignment.CenterHorizontally),
    ) {
        customItem(
            buttonGroupContent = {
                FilledIconButton(
                    onClick = {},
                    colors =
                        IconButtonDefaults.filledIconButtonColors(
                            containerColor = MenuDefaults.groupStandardContainerColor
                        ),
                ) {
                    Icon(painter = rememberVectorPainter(AppIcons.ThumbUp), contentDescription = "Localized description")
                }
            },
            menuContent = {
                DropdownMenuItem(
                    leadingIcon = {
                        Icon(painter = rememberVectorPainter(AppIcons.ThumbUp), contentDescription = null)
                    },
                    text = { Text("Thumbs up") },
                    onClick = {},
                )
            },
        )

        customItem(
            buttonGroupContent = {
                FilledIconButton(
                    onClick = {},
                    colors =
                        IconButtonDefaults.filledIconButtonColors(
                            containerColor = MenuDefaults.groupStandardContainerColor
                        ),
                ) {
                    Icon(painter = rememberVectorPainter(AppIcons.ThumbDown), contentDescription = "Localized description")
                }
            },
            menuContent = {
                DropdownMenuItem(
                    leadingIcon = {
                        Icon(painter = rememberVectorPainter(AppIcons.ThumbDown), contentDescription = null)
                    },
                    text = { Text("Thumbs down") },
                    onClick = {},
                )
            },
        )

        customItem(
            buttonGroupContent = {
                FilledIconButton(
                    onClick = {},
                    colors =
                        IconButtonDefaults.filledIconButtonColors(
                            containerColor = MenuDefaults.groupStandardContainerColor
                        ),
                ) {
                    Icon(painter = rememberVectorPainter(AppIcons.TagFaces), contentDescription = "Localized description")
                }
            },
            menuContent = {
                DropdownMenuItem(
                    leadingIcon = {
                        Icon(painter = rememberVectorPainter(AppIcons.TagFaces), contentDescription = null)
                    },
                    text = { Text("Emotes") },
                    onClick = {},
                )
            },
        )
    }
}
```
![An open segmented drop-down menu with two rounded groups: 'Modification' with 'Edit' and 'Settings', and 'Navigation' with 'Home' and 'More Options'.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_expressive_components_groupedmenusample.png) A segmented drop-down menu.

<br />

## Additional resources

- Material Design: [Menus](https://m3.material.io/components/menus)