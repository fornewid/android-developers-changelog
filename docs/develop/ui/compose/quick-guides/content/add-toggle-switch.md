---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/add-toggle-switch
url: https://developer.android.com/develop/ui/compose/quick-guides/content/add-toggle-switch
source: md.txt
---

<br />

The [`Switch`](https://developer.android.com/reference/kotlin/androidx/compose/material3/Switch.composable#Switch(kotlin.Boolean,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Boolean,androidx.compose.material3.SwitchColors,androidx.compose.foundation.interaction.MutableInteractionSource)) component lets users toggle between two states: checked
and unchecked. Use a switch to let the user to do one of the
following:

- Toggle a setting on or off.
- Enable or disable a feature.
- Select an option.

The component has two parts: the thumb and the track. The thumb is the draggable
part of the switch, and the track is the background. The user can drag the thumb
to the left or right to change the state of the switch. They can also tap the
switch to check and clear it.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/add-toggle-switch_fe30e5b1b3bf57635bdc2152f1499c7d7bf124e4909c22a4e51155c557d1cd7f.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Implement a switch

The following example is a minimal implementation of the `Switch` composable:
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/add-toggle-switch_7a716c6426df7f7cbd0d9adb06c28c88eb1b8a3aca0a65b25d211efc1088a889.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Results

![A basic switch that is unchecked.](https://developer.android.com/static/develop/ui/compose/images/components/switch-deactivated.png) **Figure 1.** An unchecked switch. ![A basic Switch that is checked.](https://developer.android.com/static/develop/ui/compose/images/components/switch.png) **Figure 2.** A checked switch.

## Create a custom thumb

You can pass any composable for the `thumbContent` parameter to create a custom
thumb. The following is an example of a switch that uses a custom icon for its
thumb:
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/add-toggle-switch_7d8cebe28a6f231657da7094629feb1d6bfb57a43b3f39ff571c9177e609d3dc.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Results

The unchecked appearance is the same as the example in
the preceding section. However, when checked, this implementation appears as
follows:
![A switch that uses the thumbContent parameter to display a custom icon when checked.](https://developer.android.com/static/develop/ui/compose/images/components/switch-icon.png) **Figure 3.** A switch with a custom checked icon.

## Use custom colors

Use the `colors` parameter to
change the color of a switch's thumb and track, taking into account whether the
switch is checked.
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/add-toggle-switch_0e2d2be24695abc1f8eb3e04fb59306b5d0994cea83a2ac5f36641bb867238c6.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Results

![A switch that uses the colors parameter to display a switch with custom colors for both the thumb and tack.](https://developer.android.com/static/develop/ui/compose/images/components/switch-colors.png) **Figure 4.** A switch with custom colors.

## Key points

- Basic parameters:

  - **`checked`**: The initial state of the switch.
  - **`onCheckedChange`**: A callback that is called when the state of the switch changes.
  - **`enabled`**: Whether the switch is enabled or disabled.
  - **`colors`**: The colors used for the switch.
- Advanced parameters

  - **`thumbContent`**: Use this to customize the appearance of the thumb when it is checked.
  - **`colors`**: Use this to customize the color of the track and thumb.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Display interactive components

Learn how composable functions can enable you to easily create beautiful UI components based on the Material Design design system. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-interactive-components) ![](https://developer.android.com/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts. [Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)