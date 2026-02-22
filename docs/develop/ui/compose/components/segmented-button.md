---
title: https://developer.android.com/develop/ui/compose/components/segmented-button
url: https://developer.android.com/develop/ui/compose/components/segmented-button
source: md.txt
---

Use a segmented button to let users choose from a set of options, side-by-side.
There are two types of segmented buttons:

- **Single-select button**: Lets users choose one option.
- **Multi-select button** : Lets users choose between two and five items. For more complex choices, or more than five items, use [chips](https://developer.android.com/develop/ui/compose/components/chip).

![A segmented button component is shown. The first button allows a single selection, while the second button allows multiple selections.](https://developer.android.com/static/develop/ui/compose/images/components/segmentedbutton.png) **Figure 1.** A single-select button (1) and a multi-select button (2).

## API surface

Use the [`SingleChoiceSegmentedButtonRow`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#SingleChoiceSegmentedButtonRow(androidx.compose.ui.Modifier,androidx.compose.ui.unit.Dp,kotlin.Function1)) and
[`MultiChoiceSegmentedButtonRow`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#MultiChoiceSegmentedButtonRow(androidx.compose.ui.Modifier,androidx.compose.ui.unit.Dp,kotlin.Function1)) layouts to create segmented buttons. These
layouts position and size [`SegmentedButton`s](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#(androidx.compose.material3.MultiChoiceSegmentedButtonRowScope).SegmentedButton(kotlin.Boolean,kotlin.Function1,androidx.compose.ui.graphics.Shape,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.material3.SegmentedButtonColors,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0,kotlin.Function0)) correctly,
and share the following key parameters:

- `space`: Adjusts the overlap between the buttons.
- `content`: Contains the content of the segmented button row, which is typically a sequence of `SegmentedButton`s.

## Create a single-select segmented button

This example shows how to create a single-select segmented button:


```kotlin
@Composable
fun SingleChoiceSegmentedButton(modifier: Modifier = Modifier) {
    var selectedIndex by remember { mutableIntStateOf(0) }
    val options = listOf("Day", "Month", "Week")

    SingleChoiceSegmentedButtonRow {
        options.forEachIndexed { index, label ->
            SegmentedButton(
                shape = SegmentedButtonDefaults.itemShape(
                    index = index,
                    count = options.size
                ),
                onClick = { selectedIndex = index },
                selected = index == selectedIndex,
                label = { Text(label) }
            )
        }
    }
}
```

<br />

### Key points about the code

- Initializes a `selectedIndex` variable using `remember` and `mutableIntStateOf` to track the selected button index.
- Defines a list of `options` representing the button labels.
- `SingleChoiceSegmentedButtonRow` lets you select only one button.
- Creates a `SegmentedButton` for each option, inside the `forEachIndexed` loop:
  - `shape` defines the button's shape based on its index and the total count of options using `SegmentedButtonDefaults.itemShape`.
  - `onClick` updates `selectedIndex` with the clicked button's index.
  - `selected` sets the button's selection state based on `selectedIndex`.
  - `label` displays the button label using the `Text` composable.

### Result

![A segmented button component with the options Day, Month, and Week is displayed. The Day option is currently selected.](https://developer.android.com/static/develop/ui/compose/images/components/SingleChoiceSegmentedButton.png) **Figure 2.** A single-select button with one option picked.

## Create a multi-select segmented button

This example shows how to create a multi-choice segmented button with icons that
lets users select multiple options:


```kotlin
@Composable
fun MultiChoiceSegmentedButton(modifier: Modifier = Modifier) {
    val selectedOptions = remember {
        mutableStateListOf(false, false, false)
    }
    val options = listOf("Walk", "Ride", "Drive")

    MultiChoiceSegmentedButtonRow {
        options.forEachIndexed { index, label ->
            SegmentedButton(
                shape = SegmentedButtonDefaults.itemShape(
                    index = index,
                    count = options.size
                ),
                checked = selectedOptions[index],
                onCheckedChange = {
                    selectedOptions[index] = !selectedOptions[index]
                },
                icon = { SegmentedButtonDefaults.Icon(selectedOptions[index]) },
                label = {
                    when (label) {
                        "Walk" -> Icon(
                            imageVector =
                            Icons.AutoMirrored.Filled.DirectionsWalk,
                            contentDescription = "Directions Walk"
                        )
                        "Ride" -> Icon(
                            imageVector =
                            Icons.Default.DirectionsBus,
                            contentDescription = "Directions Bus"
                        )
                        "Drive" -> Icon(
                            imageVector =
                            Icons.Default.DirectionsCar,
                            contentDescription = "Directions Car"
                        )
                    }
                }
            )
        }
    }
}
```

<br />

### Key points about the code

- The code initializes the `selectedOptions` variable using `remember` and `mutableStateListOf`. This tracks the selected state of each button.
- The code uses `MultiChoiceSegmentedButtonRow` to contain the buttons.
- Inside the `forEachIndexed` loop, the code creates a `SegmentedButton` for each option:
  - `shape` defines the button's shape based on its index and the total count of options.
  - `checked` sets the button's checked state based on the corresponding value in `selectedOptions`.
  - `onCheckedChange` toggles the selected state of the corresponding item in `selectedOptions` when the button is clicked.
  - `icon` displays an icon based on `SegmentedButtonDefaults.Icon` and the button's checked state.
  - `label` displays an icon corresponding to the label, using `Icon` composables with appropriate image vectors and content descriptions.

### Result

![A segmented button component with the options Walk, Ride, and Drive is shown. The Walk and Ride options are currently selected.](https://developer.android.com/static/develop/ui/compose/images/components/Multi-Choice-Segmented-Button.png) **Figure 3.** A multi-select segmented button with two options picked.

## Additional resources

- Material 3: [Segmented buttons](https://m3.material.io/components/segmented-buttons/overview)