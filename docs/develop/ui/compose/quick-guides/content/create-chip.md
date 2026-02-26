---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/create-chip
url: https://developer.android.com/develop/ui/compose/quick-guides/content/create-chip
source: md.txt
---

<br />

The `Chip` component is a compact, interactive UI element. It represents complex
entities like a contact or tag, often with an icon and label. It can be
checkable, dismissible, or clickable.

The five types of chips and where you might use them are as follows:

- [Assist](https://developer.android.com/develop/ui/compose/quick-guides/content/create-chip#assist): Guides the user during a task. Often appears as a temporary UI element in response to user input.
- [Filter](https://developer.android.com/develop/ui/compose/quick-guides/content/create-chip#filter): Lets users refine content from a set of options. They can be selected or deselected, and may include a checkmark icon when selected.
- [Input](https://developer.android.com/develop/ui/compose/quick-guides/content/create-chip#input): Represents user-provided information, such as selections in a menu. They can contain an icon and text, and provide an 'X' for removal.
- [Suggestion](https://developer.android.com/develop/ui/compose/quick-guides/content/create-chip#suggestion): Provides recommendations to the user based on their recent activity or input. Typically appear beneath an input field to prompt user actions.
- [Elevated](https://developer.android.com/develop/ui/compose/quick-guides/content/create-chip#elevated): Has an elevated appearance instead of looking flat.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-chip_cb4c7009a37ca03bc38c7d51d0fd6bae5e3b84d0d59469b89f93ca70b3b96ba1.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Create an assist chip

The [`AssistChip`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#AssistChip(kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ChipColors,androidx.compose.material3.ChipElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.interaction.MutableInteractionSource)) composable provides a straightforward way to create an
assist chip that nudges the user in a particular direction. One distinguishing
feature is its `leadingIcon` parameter that lets you display an icon on the left
side of the chip, as shown in figure 1. The following example demonstrates how
you can implement it:
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-chip_fb15d51175d0f6375ab7ed26347379ef04857ee8ff1457b727b058eee36de2c5.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe> ![A simple assist chip.](https://developer.android.com/static/develop/ui/compose/images/components/chip-assist.png) **Figure 1.** Assist chip.

## Create a filter chip

The [`FilterChip`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#FilterChip(kotlin.Boolean,kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.material3.SelectableChipColors,androidx.compose.material3.SelectableChipElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.interaction.MutableInteractionSource)) composable requires you to track whether or not the chip
is selected. The following example demonstrates how you can show a leading
checked icon only when the user has selected the chip:
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-chip_39af5df311f0dd67e38d418c8b95bb5a1075c464b31b436dbea60756841b2d03.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Results

![An unselected filter chip, with no check and a plan background.](https://developer.android.com/static/develop/ui/compose/images/components/chip-filter.png) **Figure 2.** Unselected filter chip. ![Selected filter chip, with a check and a coloured background.](https://developer.android.com/static/develop/ui/compose/images/components/chip-filter-active.png) **Figure 3.** Selected filter chip.

## Create an input chip

You can use the [`InputChip`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#InputChip(kotlin.Boolean,kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.material3.SelectableChipColors,androidx.compose.material3.SelectableChipElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.interaction.MutableInteractionSource)) composable to create chips that result from
user interaction. For example, in an email client, when the user is writing an
email, an input chip might represent a person whose address the user has entered
into the "to:" field.

The following implementation demonstrates an input chip that is in a selected
state. The user dismisses the chip when they press it.

> [!NOTE]
> **Note:** Consider how you might use a chip like this in the preceding email use case, with a name passed in for the `text` parameter, and a function that performs the necessary network calls for `onDismiss`.

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-chip_1d34f1d7cabf735fe08d34226e8a01ecb3ee29bca360e66729f4a8d23013c36b.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Results

![An input chip with an avatar and a trailing icon.](https://developer.android.com/static/develop/ui/compose/images/components/chip-input.png) **Figure 4.** Input chip.

## Create a suggestion chip

The [`SuggestionChip`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#SuggestionChip(kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ChipColors,androidx.compose.material3.ChipElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.interaction.MutableInteractionSource)) composable is the most basic of the composables listed
on this page, both in its API definition and its common use cases. Suggestion
chips present dynamically generated hints. For example, in an AI chat app, you
might use suggestion chips to present possible responses to the most recent
message.

Consider this implementation of `SuggestionChip`:
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-chip_e7579ac903dc72b4c5fcdac31fc3d74754b632d683f33f9ff9ae1d922c4e17d3.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Results

![A simple assist chip.](https://developer.android.com/static/develop/ui/compose/images/components/chip-suggestion.png) **Figure 5.** Assist chip.

> [!NOTE]
> **Note:** Although the suggestion chip component is intended for informational purposes, it does still take an `onClick` lambda that you can use to create interactivity.

## Create an elevated chip

All the examples in this document use the base composables that take a flat
appearance. If you want a chip that has an elevated appearance, use one of the
three following composables:

- [`ElevatedAssistChip`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ElevatedAssistChip(kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ChipColors,androidx.compose.material3.ChipElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.interaction.MutableInteractionSource))
- [`ElevatedFilterChip`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ElevatedFilterChip(kotlin.Boolean,kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.material3.SelectableChipColors,androidx.compose.material3.SelectableChipElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.interaction.MutableInteractionSource))
- [`ElevatedSuggestionChip`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ElevatedSuggestionChip(kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ChipColors,androidx.compose.material3.ChipElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.interaction.MutableInteractionSource))

## Key points

Four composables correspond to the four types of chips, and they share the
following parameters:

- **`label`**: The string that appears on the chip.
- **`icon`** : The icon displayed at the start of the chip. Some composables have a separate `leadingIcon` and `trailingIcon` parameter.
- **`onClick`**: The lambda that the chip calls when the user clicks it.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Display interactive components

Learn how composable functions can enable you to easily create beautiful UI components based on the Material Design design system. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-interactive-components) ![](https://developer.android.com/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts. [Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)