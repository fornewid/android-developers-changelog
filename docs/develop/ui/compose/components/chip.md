---
title: https://developer.android.com/develop/ui/compose/components/chip
url: https://developer.android.com/develop/ui/compose/components/chip
source: md.txt
---

The `Chip` component is a compact, interactive UI element. It represents complex
entities like a contact or tag, often with an icon and label. It can be
checkable, dismissible, or clickable.

The four types of chips and where you might use them are as follows:

- **Assist**: Guides the user during a task. Often appears as a temporary UI element in response to user input.
- **Filter**: Allows users to refine content from a set of options. They can be selected or deselected, and may include a checkmark icon when selected.
- **Input** : Represents user-provided information, such as selections in a menu. They can contain an icon and text, and provide an **X** for removal.
- **Suggestion**: Provides recommendations to the user based on their recent activity or input. Typically appear beneath an input field to prompt user actions.

![An example of each of the four chip components, with their unique characteristics highlighted.](https://developer.android.com/static/develop/ui/compose/images/components/chips.svg) **Figure 1.** The four chip components.

## API surface

There are four composables that correspond to the four types of chips. The
following sections outline these composables and their differences in detail.
However, they share the following parameters:

- **`label`**: The string that appears on the chip.
- **`icon`** : The icon displayed at the start of the chip. Some of the specific composables have a separate `leadingIcon` and `trailingIcon` parameter.
- **`onClick`**: The lambda that the chip calls when the user presses it.

## Assist chip

The [`AssistChip`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#AssistChip(kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ChipColors,androidx.compose.material3.ChipElevation,androidx.compose.material3.ChipBorder,androidx.compose.foundation.interaction.MutableInteractionSource)) composable provides a straightforward way to create an
assist chip that nudges the user in a particular direction. One distinguishing
feature is its `leadingIcon` parameter that lets you display an icon on the left
side of the chip. The following example demonstrates how you can implement it:


```kotlin
@Composable
fun AssistChipExample() {
    AssistChip(
        onClick = { Log.d("Assist chip", "hello world") },
        label = { Text("Assist chip") },
        leadingIcon = {
            Icon(
                Icons.Filled.Settings,
                contentDescription = "Localized description",
                Modifier.size(AssistChipDefaults.IconSize)
            )
        }
    )
}
```

<br />

This implementation appears as follows.
![A simple assist chip displaying a leading icon and text label.](https://developer.android.com/static/develop/ui/compose/images/components/chip-assist.png) **Figure 2.** Assist chip.

## Filter chip

The [`FilterChip`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#FilterChip(kotlin.Boolean,kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.material3.SelectableChipColors,androidx.compose.material3.SelectableChipElevation,androidx.compose.material3.SelectableChipBorder,androidx.compose.foundation.interaction.MutableInteractionSource)) composable requires you to track whether or not the chip
is selected. The following example demonstrates how you can show a leading
checked icon only when the user has selected the chip:


```kotlin
@Composable
fun FilterChipExample() {
    var selected by remember { mutableStateOf(false) }

    FilterChip(
        onClick = { selected = !selected },
        label = {
            Text("Filter chip")
        },
        selected = selected,
        leadingIcon = if (selected) {
            {
                Icon(
                    imageVector = Icons.Filled.Done,
                    contentDescription = "Done icon",
                    modifier = Modifier.size(FilterChipDefaults.IconSize)
                )
            }
        } else {
            null
        },
    )
}
```

<br />

This implementation appears as follows when unselected:
![An unselected filter chip, with no check and a plain background.](https://developer.android.com/static/develop/ui/compose/images/components/chip-filter.png) **Figure 3.** Unselected filter chip.

And appears as follows when selected:
![Selected filter chip, with a check and a colored background.](https://developer.android.com/static/develop/ui/compose/images/components/chip-filter-active.png) **Figure 4.** Selected filter chip.

## Input chip

You can use the [`InputChip`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#InputChip(kotlin.Boolean,kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.material3.SelectableChipColors,androidx.compose.material3.SelectableChipElevation,androidx.compose.material3.SelectableChipBorder,androidx.compose.foundation.interaction.MutableInteractionSource)) composable to create chips that result from
user interaction. For example, in an email client, when the user is writing an
email, an input chip might represent a contact the user has added to the "To:"
field.

The following implementation demonstrates an input chip that is already in a
selected state. The user dismisses the chip when they press it.

> [!NOTE]
> **Note:** Consider how you might use a chip like this in the preceding email use case, with a name passed in for the `label` parameter, and a function that performs the necessary network calls for `onDismiss`.


```kotlin
@Composable
fun InputChipExample(
    text: String,
    onDismiss: () -> Unit,
) {
    var enabled by remember { mutableStateOf(true) }
    if (!enabled) return

    InputChip(
        onClick = {
            onDismiss()
            enabled = !enabled
        },
        label = { Text(text) },
        selected = enabled,
        avatar = {
            Icon(
                Icons.Filled.Person,
                contentDescription = "Localized description",
                Modifier.size(InputChipDefaults.AvatarSize)
            )
        },
        trailingIcon = {
            Icon(
                Icons.Default.Close,
                contentDescription = "Localized description",
                Modifier.size(InputChipDefaults.AvatarSize)
            )
        },
    )
}
```

<br />

This implementation appears as follows.
![An input chip with an avatar and a trailing icon.](https://developer.android.com/static/develop/ui/compose/images/components/chip-input.png) **Figure 5.** Input chip.

## Suggestion chip

The [`SuggestionChip`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#SuggestionChip(kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ChipColors,androidx.compose.material3.ChipElevation,androidx.compose.material3.ChipBorder,androidx.compose.foundation.interaction.MutableInteractionSource)) composable is the most basic of the composables listed
on this page, both in its API definition and its common use cases. Suggestion
chips present dynamically generated hints. For example, in an AI chat app, you
might use suggestion chips to present possible responses to the most recent
message.

Consider this implementation of `SuggestionChip`:


```kotlin
@Composable
fun SuggestionChipExample() {
    SuggestionChip(
        onClick = { Log.d("Suggestion chip", "hello world") },
        label = { Text("Suggestion chip") }
    )
}
```

<br />

This implementation appears as follows:
![A simple suggestion chip.](https://developer.android.com/static/develop/ui/compose/images/components/chip-suggestion.png) **Figure 6.** Suggestion chip.

> [!NOTE]
> **Note:** Although the suggestion chip component is intended for informational purposes, it does still take an `onClick` lambda that you can use to create interactivity.

## Elevated chip

All the examples in this document use the base composables that take a flat
appearance. If you want a chip that has an elevated appearance, use one of the
three following composables:

- [`ElevatedAssistChip`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ElevatedAssistChip(kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ChipColors,androidx.compose.material3.ChipElevation,androidx.compose.material3.ChipBorder,androidx.compose.foundation.interaction.MutableInteractionSource))
- [`ElevatedFilterChip`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ElevatedFilterChip(kotlin.Boolean,kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.material3.SelectableChipColors,androidx.compose.material3.SelectableChipElevation,androidx.compose.material3.SelectableChipBorder,androidx.compose.foundation.interaction.MutableInteractionSource))
- [`ElevatedSuggestionChip`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ElevatedSuggestionChip(kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ChipColors,androidx.compose.material3.ChipElevation,androidx.compose.material3.ChipBorder,androidx.compose.foundation.interaction.MutableInteractionSource))

## Additional resources

- [Material UI docs](https://m3.material.io/components/chips/overview)