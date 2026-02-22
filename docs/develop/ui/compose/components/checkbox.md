---
title: https://developer.android.com/develop/ui/compose/components/checkbox
url: https://developer.android.com/develop/ui/compose/components/checkbox
source: md.txt
---

Checkboxes let users select one or more items from a list. You might use a
checkbox to let the user do the following:

- Turn an item on or off.
- Select from multiple options in a list.
- Indicate agreement or acceptance.

> [!NOTE]
> **Note:** Use checkboxes instead of [switches](https://developer.android.com/develop/ui/compose/components/switch) or [radio buttons](https://m3.material.io/components/radio-button) if the user can select multiple options in a list.

## Anatomy

A checkbox consists of the following elements:

- **Box**: This is the container for the checkbox.
- **Check**: This is the visual indicator that shows whether the checkbox is selected or not.
- **Label**: This is the text that describes the checkbox.

## States

A checkbox can be in one of three states:

- **Unselected**: The checkbox is not selected. The box is empty.
- **Indeterminate**: The checkbox is in an indeterminate state. The box contains a dash.
- **Selected**: The checkbox is selected. The box contains a checkmark.

The following image demonstrates the three states of a checkbox.
![An example of a checkbox component in each of its three states: unselected, selected, and indeterminate.](https://developer.android.com/static/develop/ui/compose/images/components/checkboxes.svg) **Figure 1.** The three states of a checkbox. Unselected, indeterminate, and selected.

## Implementation

You can use the [`Checkbox`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Checkbox(kotlin.Boolean,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.material3.CheckboxColors,androidx.compose.foundation.interaction.MutableInteractionSource)) composable to create a checkbox in your app.
There are just a few key parameters to keep in mind:

- `checked`: The boolean that captures whether the checkbox is checked or unchecked.
- `onCheckedChange()`: The function that the app calls when the user taps the checkbox.

The following snippet demonstrates how to use the `Checkbox` composable:


```kotlin
@Composable
fun CheckboxMinimalExample() {
    var checked by remember { mutableStateOf(true) }

    Row(
        verticalAlignment = Alignment.CenterVertically,
    ) {
        Text(
            "Minimal checkbox"
        )
        Checkbox(
            checked = checked,
            onCheckedChange = { checked = it }
        )
    }

    Text(
        if (checked) "Checkbox is checked" else "Checkbox is unchecked"
    )
}
```

<br />

### Explanation

This code creates a checkbox that is initially unchecked. When the user clicks
on the checkbox, the `onCheckedChange` lambda updates the `checked` state.

### Result

This example produces the following component when unchecked:
![An unchecked checkbox with a label. The text beneath it reads 'Checkbox is unchecked'](https://developer.android.com/static/develop/ui/compose/images/components/checkbox-minimal-unchecked.png) **Figure 2.** Unchecked checkbox

And this is how the same checkbox appears when checked:
![A checked checkbox with a label. The text beneath it reads 'Checkbox is checked'](https://developer.android.com/static/develop/ui/compose/images/components/checkbox-minimal-checked.png) **Figure 3.** Checked checkbox

## Advanced example

The following is a more complex example of how you can implement checkboxes in
your app. In this snippet, there is a parent checkbox and a series of child
checkboxes. When the user taps the parent checkbox, the app checks all child
checkboxes.


```kotlin
@Composable
fun CheckboxParentExample() {
    // Initialize states for the child checkboxes
    val childCheckedStates = remember { mutableStateListOf(false, false, false) }

    // Compute the parent state based on children's states
    val parentState = when {
        childCheckedStates.all { it } -> ToggleableState.On
        childCheckedStates.none { it } -> ToggleableState.Off
        else -> ToggleableState.Indeterminate
    }

    Column {
        // Parent TriStateCheckbox
        Row(
            verticalAlignment = Alignment.CenterVertically,
        ) {
            Text("Select all")
            TriStateCheckbox(
                state = parentState,
                onClick = {
                    // Determine new state based on current state
                    val newState = parentState != ToggleableState.On
                    childCheckedStates.forEachIndexed { index, _ ->
                        childCheckedStates[index] = newState
                    }
                }
            )
        }

        // Child Checkboxes
        childCheckedStates.forEachIndexed { index, checked ->
            Row(
                verticalAlignment = Alignment.CenterVertically,
            ) {
                Text("Option ${index + 1}")
                Checkbox(
                    checked = checked,
                    onCheckedChange = { isChecked ->
                        // Update the individual child state
                        childCheckedStates[index] = isChecked
                    }
                )
            }
        }
    }

    if (childCheckedStates.all { it }) {
        Text("All options selected")
    }
}
```

<br />

### Explanation

The following are several points you should note from this example:

- **State management** :
  - `childCheckedStates`: A list of booleans using `mutableStateOf()` to track the checked state of each child checkbox.
  - `parentState`: A [`ToggleableState`](https://developer.android.com/reference/kotlin/androidx/compose/ui/state/ToggleableState?_gl=1*1nllj9c*_up*MQ..*_ga*MTQ4MjE3NjI1Ny4xNzE1MzM1Nzc0*_ga_6HH9YJMN9M*MTcxNTMzNTc3NC4xLjAuMTcxNTMzNTc3NC4wLjAuMA..) whose value derives from the child checkboxes' states.
- **UI components** :
  - [`TriStateCheckbox`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#TriStateCheckbox(androidx.compose.ui.state.ToggleableState,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.material3.CheckboxColors,androidx.compose.foundation.interaction.MutableInteractionSource)): Is necessary for the parent checkbox as it has a `state` param that lets you set it to indeterminate.
  - [`Checkbox`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Checkbox(kotlin.Boolean,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.material3.CheckboxColors,androidx.compose.foundation.interaction.MutableInteractionSource)): Used for each child checkbox with its state linked to the corresponding element in `childCheckedStates`.
  - `Text`: Displays labels and messages ("Select all", "Option X", "All options selected").
- **Logic** :
  - The parent checkbox's `onClick` updates all child checkboxes to the opposite of the current parent state.
  - Each child checkbox's `onCheckedChange` updates its corresponding state in the `childCheckedStates` list.
  - The code displays "`All options selected`" when all child checkboxes are checked.

> [!NOTE]
> **Note:** If you want to have a checkbox with an indeterminate state, you must use `TriStateCheckbox`. This is because it has a `state` parameter of type `ToggleableState`, whereas `Checkbox` does not.

### Result

This example produces the following component when all checkboxes are unchecked.
![A series of unchecked labeled checkboxes with a label.](https://developer.android.com/static/develop/ui/compose/images/components/checkbox-parent-unchecked.png) **Figure 4.** Unchecked checkboxes

Likewise, this is how the component appears when all options are checked, as
when the user taps select all:
![A series of checked labeled checkboxes checkbox with a label. The first is marked 'select all'. There is a text component beneath them that reads 'all options selected.'](https://developer.android.com/static/develop/ui/compose/images/components/checkbox-parent-checked.png) **Figure 5.** Checked checkboxes

When only one option is checked the parent checkbox display the indeterminate
state:
![A series of unchecked labeled checkboxes checkbox with a label. All but one is unchecked. The checkbox labeled 'select all' is indeterminate, displaying a dash.](https://developer.android.com/static/develop/ui/compose/images/components/checkbox-parent-indeterminate.png) **Figure 6.** Indeterminate checkbox

### Additional resources

- [Material Design Checkboxes](https://m3.material.io/components/checkbox/overview)