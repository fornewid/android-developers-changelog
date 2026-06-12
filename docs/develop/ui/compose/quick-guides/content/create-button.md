---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/create-button
url: https://developer.android.com/develop/ui/compose/quick-guides/content/create-button
source: md.txt
---

<br />

Buttons let the user trigger a defined action. There are five types of
button:

| Type | Appearance | Purpose |
|---|---|---|
| [Filled](https://developer.android.com/develop/ui/compose/quick-guides/content/create-button#create-filled) | Solid background with contrasting text. | For primary actions, such as "Submit" and "Save." The shadow effect emphasizes the button's importance. |
| [Tonal](https://developer.android.com/develop/ui/compose/quick-guides/content/create-button#create-filled-tonal) | Background color varies to match the surface. | For primary or significant actions. Filled buttons provide visual weight and are appropriate for actions like "Add to cart" and "Sign in." |
| [Elevated](https://developer.android.com/develop/ui/compose/quick-guides/content/create-button#create-elevated) | Shadow makes it stand out. | For primary or significant actions. Increase elevation to make the button more prominent. |
| [Outlined](https://developer.android.com/develop/ui/compose/quick-guides/content/create-button#create-outlined) | Features a border with no fill. | For actions that are important but not primary. Outlined buttons pair well with other buttons to indicate alternative, secondary actions like "Cancel" or "Back." |
| [Text](https://developer.android.com/develop/ui/compose/quick-guides/content/create-button#create-text) | Text with no background or border. | For less critical actions such as navigational links, or secondary actions like "Learn more" or "View details." |

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-button_cb70818c4f770db4ba7b096843507e1aa7f55b8dcefed0a2bcdea873b78c9077.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Create a filled button

The filled button component uses the basic [`Button`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Button(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) composable. It is
filled with a solid color by default.
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-button_32f3c607ca55b9eb5c17a5ab9593bde80235913bed1cc79f4f5484cb12a0a5e3.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Results

![A filled button with a purple background that reads, 'filled'.](https://developer.android.com/static/develop/ui/compose/images/components/button-filled.png) **Figure 1.** A filled button.

## Create a filled tonal button

The filled tonal button component uses the [`FilledTonalButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/FilledTonalButton.composable#FilledTonalButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) composable.
It is filled with a tonal color by default.
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-button_7d5a00b910441ab399dd738ed422b4f6e7fb2e9498b2984385aaf7b1d463f26a.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Results

![A tonal button with a light purple background that reads, 'filled'.](https://developer.android.com/static/develop/ui/compose/images/components/button-tonal.png) **Figure 2.** A tonal button.

## Create an outlined button

The outlined button component uses the [`OutlinedButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/OutlinedButton.composable#OutlinedButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) composable. It
appears with an outline by default.
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-button_f9164ffd95975e166a093d015d7a163e64f56d43c622f648f5d9aefdad431130.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Results

![A transparent outlined button with a dark border that reads, 'Outlined'.](https://developer.android.com/static/develop/ui/compose/images/components/button-outlined.png) **Figure 3.** An outlined button.

## Create an elevated button

The elevated button component uses the [`ElevatedButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/ElevatedButton.composable#ElevatedButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) composable. It has
a shadow that represents the elevation effect by default and appears as
an outlined button with a shadow.
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-button_44262b172ea40b6b06578ea4f0a4c68aaf88a65e7d6165998543e70f6bec2f43.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Results

![An elevated button with a gray background that reads, 'Elevated'.](https://developer.android.com/static/develop/ui/compose/images/components/button-elevated.png) **Figure 4.** An elevated button.

## Create a text button

The text button component uses the [`TextButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/TextButton.composable#TextButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) composable. Until clicked,
it appears only as text. It does not have a solid fill or outline by default.
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-button_0c85404eff4e6a44ac217b6a8aec747018126a7298cff12492168030a9b2433a.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Results

![A text button that reads 'Text Button'](https://developer.android.com/static/develop/ui/compose/images/components/button-text.png) **Figure 5.** A text button.

## Key points

- `onClick`: The function called when the user presses the button.
- `enabled`: When false, this parameter causes the button to appear unavailable and inactive.
- `colors`: An instance of `ButtonColors` that determines the colors used in the button.
- `contentPadding`: The padding within the button.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Display interactive components

Learn how composable functions can enable you to easily create beautiful UI components based on the Material Design design system. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-interactive-components) ![](https://developer.android.com/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts. [Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)