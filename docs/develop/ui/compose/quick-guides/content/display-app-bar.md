---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/display-app-bar
url: https://developer.android.com/develop/ui/compose/quick-guides/content/display-app-bar
source: md.txt
---

<br />

App bars are containers at the top or the bottom of the screen that give your
users access to key features and navigation items:

| Type | Appearance | Purpose |
|---|---|---|
| [Top app bar](https://developer.android.com/develop/ui/compose/quick-guides/content/display-app-bar#top) | Across the top of the screen. | Provides access to key tasks and information. Typically hosts a title, core action items, and certain navigation items. |
| [Bottom app bar](https://developer.android.com/develop/ui/compose/quick-guides/content/display-app-bar#bottom) | Across the bottom of the screen. | Typically includes core navigation items. Might give access to other actions, for example, by using a floating action button. |

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/display-app-bar_a1e19bb9399af83328f4f119460605b05ca7b024e7aa299476e2a91b55b09539.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Implement a top app bar

The following code shows implementations for the four types of top app bars,
including varying examples of how you can control scroll behavior.

- [Small top app bar](https://developer.android.com/develop/ui/compose/quick-guides/content/display-app-bar#small)
- [Center-aligned top app bar](https://developer.android.com/develop/ui/compose/quick-guides/content/display-app-bar#center)
- [Medium top app bar](https://developer.android.com/develop/ui/compose/quick-guides/content/display-app-bar#medium)
- [Large top app bar](https://developer.android.com/develop/ui/compose/quick-guides/content/display-app-bar#large)

### Small top app bar

To create a small top app bar, use the [`TopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#TopAppBar(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1,androidx.compose.foundation.layout.WindowInsets,androidx.compose.material3.TopAppBarColors,androidx.compose.material3.TopAppBarScrollBehavior)) composable. This is the
simplest possible top app bar and in this example just contains a title.

#### Result

![An example of a small top app bar.](https://developer.android.com/static/develop/ui/compose/images/components/appbar-small.png) **Figure 1.** A small top app bar.

#### Implement a small top app bar

The following example does not pass `TopAppBar` a value for
`scrollBehavior`, so the top app bar does not react to scrolling of the inner
content.
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/display-app-bar_56b05ec808cd9ff6d0f8edb2ea8fe22e38c1c493abb77eeacc3c4121e8d09dd0.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Center-aligned top app bar

The center-aligned top app bar is the same as the small app bar,
except the title is centered within the component. To implement it, use the
dedicated [`CenterAlignedTopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Scaffold(androidx.compose.foundation.layout.WindowInsets,androidx.compose.ui.Modifier,androidx.compose.material.ScaffoldState,kotlin.Function0,kotlin.Function0,kotlin.Function1,kotlin.Function0,androidx.compose.material.FabPosition,kotlin.Boolean,kotlin.Function1,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1)) composable.

#### Result

![Write your alt text here](https://developer.android.com/static/develop/ui/compose/images/components/appbar-centered.png) **Figure 2.** A center-aligned top app bar.

#### Implement a center-aligned top app bar

This example uses `enterAlwaysScrollBehavior()` to get the value that it passes
for `scrollBehavior`. The bar collapses when the user scrolls the
scaffold's inner content.
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/display-app-bar_e1be9a6d611b759a87c9a70c43615d93459590e5be3a52d1c7db7ad6cec8951d.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Medium top app bar

The medium top app bar places the title beneath any additional icons. To create
one, use the [`MediumTopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#MediumTopAppBar(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,androidx.compose.material3.TopAppBarColors,androidx.compose.material3.TopAppBarScrollBehavior)) composable.

#### Result

<br />

**Figure 3.** A medium top app bar demonstrating the scroll behavior from `enterAlwaysScrollBehavior`.

<br />

#### Implement a medium top app bar

Like the previous code, this example uses `enterAlwaysScrollBehavior()` to
get the value that it passes for `scrollBehavior`.
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/display-app-bar_f181865a67462f64192b72452285e4fda3d5b005ed72fb0705febb98d502b316.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

### Large top app bar

A large top app bar is similar to the medium, though the padding between the
title and the icons is greater and it occupies more space on screen overall. To
create one, use the [`LargeTopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#LargeTopAppBar(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,androidx.compose.material3.TopAppBarColors,androidx.compose.material3.TopAppBarScrollBehavior) ) composable.

#### Result

![A screen in an app with a bottom app bar that holds for action icons on the left side, and a floating action button on the right.](https://developer.android.com/static/develop/ui/compose/images/components/appbar-large.png) **Figure 4.** An example implementation of a large top app bar.

#### Implement a large top app bar

This example uses
`exitUntilCollapsedScrollBehavior()` to get the value that it passes for
`scrollBehavior`. The bar collapses when the user scrolls the
scaffold's inner content, but then expands when the user scrolls to the end of
the inner content.
<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/display-app-bar_8111f66166d990547e0b98aae349df53f63bfb4eeb3b0dafde09d43c17f4b658.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Implement a bottom app bar

To create a bottom app bar, use the [`BottomAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#BottomAppBar(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)) composable, which is
similar to the top app bar composable.

### Result

![A screen in an app with a bottom app bar that holds for action icons on the left side, and a floating action button on the right.](https://developer.android.com/static/develop/ui/compose/images/components/appbar-bottom.png) **Figure 5.** An example implementation of a bottom app bar.

#### Implement a bottom app bar

You pass composables for the following key
parameters:

- `actions`: A series of icons that appear on the left side of the bar. These are commonly either key actions for the given screen, or navigation items.
- `floatingActionButton`: The floating action button that appears on the right side of the bar.

> [!NOTE]
> **Note:** You can also use `BottomAppBar` without passing a value for `actions` and `floatingActionButton`. You create a custom bottom app bar by filling `BottomAppBar` with content as you would other containers.

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/display-app-bar_2472de1f6de57ff2e318e3d1ae20a7d39d62d28b37be75e0d6ed27976b8f19bd.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Key points

- You generally pass app bars to the `Scaffold` composable, which has specific parameters to receive them.
- The composables that you use to implement top app
  bars share key parameters:

  - `title`: The text that appears across the app bar.
  - `navigationIcon`: The primary icon for navigation, which appears on the left of the app bar.
  - `actions`: Icons that provide the user access to key actions, which appear on the right of the app bar.
  - `scrollBehavior`: Determines how the top app bar responds to scrolling of the scaffold's inner content.
  - `colors`: Determines how the app bar appears.
- You can control how the app bar responds when the user scrolls the
  scaffold's inner content. To do so, create an instance of
  [`TopAppBarScrollBehavior`](https://developer.android.com/reference/kotlin/androidx/compose/material3/TopAppBarScrollBehavior) and pass it to your top app bar for the
  `scrollBehavior` parameter. There are three types of `TopAppBarScrollBehavior`:

  - `enterAlwaysScrollBehavior`: When the user pulls up the scaffold's inner content, the top app bar collapses. The app bar expands when the user pulls down the inner content.
  - `exitUntilCollapsedScrollBehavior`: Similar to `enterAlwaysScrollBehavior`, though the app bar also expands when the user reaches the end of the scaffold's inner content.
  - `pinnedScrollBehavior`: The app bar remains in place and does not react to scrolling.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Display interactive components

Learn how composable functions can enable you to easily create beautiful UI components based on the Material Design design system. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-interactive-components) ![](https://developer.android.com/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts. [Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)