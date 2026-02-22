---
title: https://developer.android.com/develop/ui/compose/components/radio-button
url: https://developer.android.com/develop/ui/compose/components/radio-button
source: md.txt
---

A [radio button](https://m3.material.io/components/radio-button/overview) lets a user select an option from a set of
options. You use a radio button when only one item can be selected from a
list. If users need to select more than one item, use a [switch](https://m3.material.io/components/switch/overview)
instead.
![Two radio buttons with no labels. The left button is selected, and the circle is filled in to indicate its selected state. The right button is not filled in](https://developer.android.com/static/develop/ui/compose/images/components/radio-button.svg) **Figure 1.** A pair of radio buttons with one option selected.

## API surface

Use the [`RadioButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#RadioButton(kotlin.Boolean,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.material3.RadioButtonColors,androidx.compose.foundation.interaction.MutableInteractionSource)) composable to list the available options. Wrap each
`RadioButton` option and its label inside a `Row` component to group them
together.

`RadioButton` includes the following key parameters:

- `selected`: Indicates whether the radio button is selected.
- `onClick`: A lambda function that your app executes when the user clicks the radio button. If this is `null`, the user can't interact directly with the radio button.
- `enabled`: Controls whether the radio button is enabled or disabled. Users can't interact with disabled radio buttons.
- `interactionSource`: Lets you observe the interaction state of the button, for example, whether it's pressed, hovered, or focused.

## Create a basic radio button

The following code snippet renders a list of radio buttons within a `Column`:


```kotlin
@Composable
fun RadioButtonSingleSelection(modifier: Modifier = Modifier) {
    val radioOptions = listOf("Calls", "Missed", "Friends")
    val (selectedOption, onOptionSelected) = remember { mutableStateOf(radioOptions[0]) }
    // Note that Modifier.selectableGroup() is essential to ensure correct accessibility behavior
    Column(modifier.selectableGroup()) {
        radioOptions.forEach { text ->
            Row(
                Modifier
                    .fillMaxWidth()
                    .height(56.dp)
                    .selectable(
                        selected = (text == selectedOption),
                        onClick = { onOptionSelected(text) },
                        role = Role.RadioButton
                    )
                    .padding(horizontal = 16.dp),
                verticalAlignment = Alignment.CenterVertically
            ) {
                RadioButton(
                    selected = (text == selectedOption),
                    onClick = null // null recommended for accessibility with screen readers
                )
                Text(
                    text = text,
                    style = MaterialTheme.typography.bodyLarge,
                    modifier = Modifier.padding(start = 16.dp)
                )
            }
        }
    }
}
```

<br />

### Key points about the code

- `radioOptions` represents the labels for the radio buttons.
- The `remember` composable function creates a state variable `selectedOption` and a function to update that state called `onOptionSelected`. This state holds the selected radio button option.
  - `mutableStateOf(radioOptions[0])` initializes the state to the first item in the list. "Calls" is the first item, so it's the radio button selected by default.
- [`Modifier.selectableGroup()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).selectableGroup()) ensures proper accessibility behavior for screen readers. It informs the system that the elements within this `Column` are part of a selectable group, which enables proper screen reader support.
- [`Modifier.selectable()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).selectable(kotlin.Boolean,kotlin.Boolean,androidx.compose.ui.semantics.Role,kotlin.Function0)) makes the entire `Row` act as a single selectable item.
  - `selected` indicates whether the current `Row` is selected based on the `selectedOption` state.
  - The `onClick` lambda function updates the `selectedOption` state to the clicked option when the `Row` is clicked.
  - `role = Role.RadioButton` informs accessibility services that the `Row` functions as a radio button.
- `RadioButton(...)` creates the `RadioButton` composable.
  - `onClick = null` on the `RadioButton` improves accessibility. This prevents the radio button from handling the click event directly, and allows the `Row`'s `selectable` modifier to manage the selection state and accessibility behavior.

### Result

![A list of three radio buttons labeled Calls, Missed, and Friends. The Friends radio button is selected.](https://developer.android.com/static/develop/ui/compose/images/components/radiobutton2.png) **Figure 2.** Three radio buttons with the "Friends" option selected.

## Additional resources

- Material Design: [Buttons](https://m3.material.io/components/buttons/overview)