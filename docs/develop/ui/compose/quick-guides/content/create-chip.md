---
title: Create a chip to represent complex entities  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/create-chip
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Create a chip to represent complex entities Stay organized with collections Save and categorize content based on your preferences.




The `Chip` component is a compact, interactive UI element. It represents complex
entities like a contact or tag, often with an icon and label. It can be
checkable, dismissible, or clickable.

The five types of chips and where you might use them are as follows:

* [Assist](#assist): Guides the user during a task. Often appears as a temporary UI
  element in response to user input.
* [Filter](#filter): Lets users refine content from a set of options. They can be
  selected or deselected, and may include a checkmark icon when selected.
* [Input](#input): Represents user-provided information, such as selections in a
  menu. They can contain an icon and text, and provide an 'X' for removal.
* [Suggestion](#suggestion): Provides recommendations to the user based on their recent
  activity or input. Typically appear beneath an input field to prompt user
  actions.
* [Elevated](#elevated): Has an elevated appearance instead of looking flat.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

## Create an assist chip

The [`AssistChip`](/reference/kotlin/androidx/compose/material3/AssistChip.composable) composable provides a straightforward way to create an
assist chip that nudges the user in a particular direction. One distinguishing
feature is its `leadingIcon` parameter that lets you display an icon on the left
side of the chip, as shown in figure 1. The following example demonstrates how
you can implement it:


![A simple assist chip.](/static/develop/ui/compose/images/components/chip-assist.png)


**Figure 1.** Assist chip.

## Create a filter chip

The [`FilterChip`](/reference/kotlin/androidx/compose/material3/FilterChip.composable) composable requires you to track whether or not the chip
is selected. The following example demonstrates how you can show a leading
checked icon only when the user has selected the chip:

### Results

![An unselected filter chip, with no check and a plan background.](/static/develop/ui/compose/images/components/chip-filter.png)


**Figure 2.** Unselected filter chip.


![Selected filter chip, with a check and a coloured background.](/static/develop/ui/compose/images/components/chip-filter-active.png)


**Figure 3.** Selected filter chip.

## Create an input chip

You can use the [`InputChip`](/reference/kotlin/androidx/compose/material3/InputChip.composable) composable to create chips that result from
user interaction. For example, in an email client, when the user is writing an
email, an input chip might represent a person whose address the user has entered
into the "to:" field.

The following implementation demonstrates an input chip that is in a selected
state. The user dismisses the chip when they press it.

**Note:** Consider how you might use a chip like this in the preceding email use
case, with a name passed in for the `text` parameter, and a function that
performs the necessary network calls for `onDismiss`.


### Results

![An input chip with an avatar and a trailing icon.](/static/develop/ui/compose/images/components/chip-input.png)


**Figure 4.** Input chip.

## Create a suggestion chip

The [`SuggestionChip`](/reference/kotlin/androidx/compose/material3/SuggestionChip.composable) composable is the most basic of the composables listed
on this page, both in its API definition and its common use cases. Suggestion
chips present dynamically generated hints. For example, in an AI chat app, you
might use suggestion chips to present possible responses to the most recent
message.

Consider this implementation of `SuggestionChip`:

### Results

![A simple assist chip.](/static/develop/ui/compose/images/components/chip-suggestion.png)


**Figure 5.** Assist chip.

**Note:** Although the suggestion chip component is intended for informational
purposes, it does still take an `onClick` lambda that you can use to create
interactivity.

## Create an elevated chip

All the examples in this document use the base composables that take a flat
appearance. If you want a chip that has an elevated appearance, use one of the
three following composables:

* [`ElevatedAssistChip`](/reference/kotlin/androidx/compose/material3/ElevatedAssistChip.composable)
* [`ElevatedFilterChip`](/reference/kotlin/androidx/compose/material3/ElevatedFilterChip.composable)
* [`ElevatedSuggestionChip`](/reference/kotlin/androidx/compose/material3/ElevatedSuggestionChip.composable)

## Key points

Four composables correspond to the four types of chips, and they share the
following parameters:

* **`label`**: The string that appears on the chip.
* **`icon`**: The icon displayed at the start of the chip. Some composables
  have a separate `leadingIcon` and `trailingIcon` parameter.
* **`onClick`**: The lambda that the chip calls when the user clicks it.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Display interactive components

Learn how composable functions can enable you to easily
create beautiful UI components based on the Material Design design
system.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/display-interactive-components)

![](/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.

[Go to FAQ](/quick-guides/faq)
[Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)