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

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-button_504265100ae01120c9f8aa6e5287923881f65f7e4bc6b06f0aa1c8888205eb6f.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Create a filled button

The filled button component uses the basic [`Button`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Button(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) composable. It is
filled with a solid color by default.
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-button_77447966b02cd04f139184b53ac4cc2a7ef223fa3cf6186853c993b9640aa570.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Results

![A filled button with a purple background that reads, 'filled'.](https://developer.android.com/static/develop/ui/compose/images/components/button-filled.png) **Figure 1.** A filled button.

## Create a filled tonal button

The filled tonal button component uses the [`FilledTonalButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#FilledTonalButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) composable.
It is filled with a tonal color by default.
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-button_49a080651a3e630b64488439970d810cc160306fea2d9b04288ec010b8d07393.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Results

![A tonal button with a light purple background that reads, 'filled'.](https://developer.android.com/static/develop/ui/compose/images/components/button-tonal.png) **Figure 2.** A tonal button.

## Create an outlined button

The outlined button component uses the [`OutlinedButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#OutlinedButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) composable. It
appears with an outline by default.
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-button_722a18b4b45e165cc2ee46fd69799c3b863e8dafb8ec6f2d9f2f2b71ef9e222b.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Results

![A transparent outlined button with a dark border that reads, 'Outlined'.](https://developer.android.com/static/develop/ui/compose/images/components/button-outlined.png) **Figure 3.** An outlined button.

## Create an elevated button

The elevated button component uses the [`ElevatedButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ElevatedButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) composable. It has
a shadow that represents the elevation effect by default and appears as
an outlined button with a shadow.
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-button_9ddc52af92736fabbaf32e52263a870abc6b1a0460afb5a467f04a2bf509a3ba.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Results

![An elevated button with a gray background that reads, 'Elevated'.](https://developer.android.com/static/develop/ui/compose/images/components/button-elevated.png) **Figure 4.** An elevated button.

## Create a text button

The text button component uses the [`TextButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#TextButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) composable. Until clicked,
it appears only as text. It does not have a solid fill or outline by default.
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-button_ee4bde5819595812c8396c711569ff705f15952398a5cba0989c52404fcebea5.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

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