---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/display-top-app-bar
url: https://developer.android.com/develop/ui/compose/quick-guides/content/display-top-app-bar
source: md.txt
---

<br />

Create a top app bar to help users navigate and access functions in your app,
using the [`TopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#TopAppBar(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,androidx.compose.material3.TopAppBarColors,androidx.compose.material3.TopAppBarScrollBehavior)) composable.

## Results

<br />

**Figure 1.** A medium top app bar.

<br />

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/display-top-app-bar_a1e19bb9399af83328f4f119460605b05ca7b024e7aa299476e2a91b55b09539.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Create a composable for top app bar

Create a top app bar using the [`MediumTopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#MediumTopAppBar(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,androidx.compose.material3.TopAppBarColors,androidx.compose.material3.TopAppBarScrollBehavior)) composable that collapses
when the user scrolls down the content area, and expands when the user scrolls
back to the top of the content:
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/display-top-app-bar_f181865a67462f64192b72452285e4fda3d5b005ed72fb0705febb98d502b316.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Key points about the code

- An outer [`Scaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Scaffold(androidx.compose.foundation.layout.WindowInsets,androidx.compose.ui.Modifier,androidx.compose.material.ScaffoldState,kotlin.Function0,kotlin.Function0,kotlin.Function1,kotlin.Function0,androidx.compose.material.FabPosition,kotlin.Boolean,kotlin.Function1,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1)) with a `TopBar` set.
- A title consisting of a single `Text` element.
- A top bar with a single action defined.
- An [`IconButton`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#IconButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)) action with an `onClick` lambda to perform the action.
- An `IconButton` containing an [`Icon`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Icon(androidx.compose.ui.graphics.ImageBitmap,kotlin.String,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color)) that has an icon image and a content description text.
- The scroll behavior for the Scaffold's inner content is defined as `enterAlwaysScrollBehavior()`. This collapses the app bar when the user pulls up the inner content, and expands the app bar when the user pulls down the inner content.
- In addition to `MediumTopBar`, which contains the title, you can also use:
  - `TopAppBar`: use for screens that don't require a lot of navigation or actions.
  - [`CenterAlignedTopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#CenterAlignedTopAppBar(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,androidx.compose.material3.TopAppBarColors,androidx.compose.material3.TopAppBarScrollBehavior)): use for screens that have a single primary action.Title is centered within the component.
  - `MediumTopAppBar`: use for screens that require a moderate amount of navigation and actions.
  - [`LargeTopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#LargeTopAppBar(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,androidx.compose.material3.TopAppBarColors,androidx.compose.material3.TopAppBarScrollBehavior)): use for screens that require a lot of navigation and actions. Uses more padding than `MediumTopAppBar` and places the title beneath any additional icons.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Create a home screen scaffold

Find out how to use a standardized platform to build complex user interfaces. The scaffold holds together different parts of the UI, giving apps a coherent look and feel. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/create-a-home-screen-scaffold) ![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Display interactive components

Learn how composable functions can enable you to easily create beautiful UI components based on the Material Design design system. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-interactive-components) ![](https://developer.android.com/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts. [Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)