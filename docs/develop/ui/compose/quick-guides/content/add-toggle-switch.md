---
title: Add a switch that users can toggle  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/add-toggle-switch
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Add a switch that users can toggle Stay organized with collections Save and categorize content based on your preferences.




The [`Switch`](/reference/kotlin/androidx/compose/material3/Switch.composable#Switch(kotlin.Boolean,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Boolean,androidx.compose.material3.SwitchColors,androidx.compose.foundation.interaction.MutableInteractionSource)) component lets users toggle between two states: checked
and unchecked. Use a switch to let the user to do one of the
following:

* Toggle a setting on or off.
* Enable or disable a feature.
* Select an option.

The component has two parts: the thumb and the track. The thumb is the draggable
part of the switch, and the track is the background. The user can drag the thumb
to the left or right to change the state of the switch. They can also tap the
switch to check and clear it.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

## Implement a switch

The following example is a minimal implementation of the `Switch` composable:

### Results

![A basic switch that is unchecked.](/static/develop/ui/compose/images/components/switch-deactivated.png)


**Figure 1.** An unchecked switch.


![A basic Switch that is checked.](/static/develop/ui/compose/images/components/switch.png)


**Figure 2.** A checked switch.

## Create a custom thumb

You can pass any composable for the `thumbContent` parameter to create a custom
thumb. The following is an example of a switch that uses a custom icon for its
thumb:

### Results

The unchecked appearance is the same as the example in
the preceding section. However, when checked, this implementation appears as
follows:

![A switch that uses the thumbContent parameter to display a custom icon when checked.](/static/develop/ui/compose/images/components/switch-icon.png)


**Figure 3.** A switch with a custom checked icon.

## Use custom colors

Use the `colors` parameter to
change the color of a switch's thumb and track, taking into account whether the
switch is checked.

### Results

![A switch that uses the colors parameter to display a switch with custom colors for both the thumb and tack.](/static/develop/ui/compose/images/components/switch-colors.png)


**Figure 4.** A switch with custom colors.

## Key points

* Basic parameters:

  + **`checked`**: The initial state of the switch.
  + **`onCheckedChange`**: A callback that is called when the state of the
    switch changes.
  + **`enabled`**: Whether the switch is enabled or disabled.
  + **`colors`**: The colors used for the switch.
* Advanced parameters

  + **`thumbContent`**: Use this to customize the appearance of the thumb when
    it is checked.
  + **`colors`**: Use this to customize the color of the track and thumb.

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