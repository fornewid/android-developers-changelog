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

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/add-toggle-switch_cb70818c4f770db4ba7b096843507e1aa7f55b8dcefed0a2bcdea873b78c9077.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Implement a switch

The following example is a minimal implementation of the `Switch` composable:
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/add-toggle-switch_333ff92302bc9405b0686c55c593d9c62f5bbcddc3a690b7b57dab8f4ff35f9b.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Results

![A basic switch that is unchecked.](https://developer.android.com/static/develop/ui/compose/images/components/switch-deactivated.png) **Figure 1.** An unchecked switch. ![A basic Switch that is checked.](https://developer.android.com/static/develop/ui/compose/images/components/switch.png) **Figure 2.** A checked switch.

## Create a custom thumb

You can pass any composable for the `thumbContent` parameter to create a custom
thumb. The following is an example of a switch that uses a custom icon for its
thumb:
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/add-toggle-switch_8f613acd41d560398b2b9b428ba69b2b8ca7defd0e237cd6a5882b864d2ea5ad.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Results

The unchecked appearance is the same as the example in
the preceding section. However, when checked, this implementation appears as
follows:
![A switch that uses the thumbContent parameter to display a custom icon when checked.](https://developer.android.com/static/develop/ui/compose/images/components/switch-icon.png) **Figure 3.** A switch with a custom checked icon.

## Use custom colors

Use the `colors` parameter to
change the color of a switch's thumb and track, taking into account whether the
switch is checked.
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/add-toggle-switch_aee2125ccaae01301f0d66a1c32b80f8def363a96f579ee23edf4927c97b1fa9.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

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