---
title: Create a scaffold component to hold the UI together  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/create-scaffold
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Create a scaffold component to hold the UI together Stay organized with collections Save and categorize content based on your preferences.



In Material Design, a scaffold is a fundamental structure that provides a
standardized platform for complex user interfaces. It holds together different
parts of the UI, such as app bars and floating action buttons, giving apps a
coherent look and feel.

## Results

![An implementation of scaffold that contains simple top and bottom app bars, as well as a floating action button that iterates a counter. The inner content of the scaffold is simple text that explains the component.](/static/develop/ui/compose/images/components/scaffold.png)


**Figure 1.** An implementation of scaffold.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21
or higher.

### Dependencies

## Create a scaffold

The following example provides a full example of how you might implement
[`Scaffold`](/reference/kotlin/androidx/compose/material/Scaffold.composable#Scaffold(androidx.compose.foundation.layout.WindowInsets,androidx.compose.ui.Modifier,androidx.compose.material.ScaffoldState,kotlin.Function0,kotlin.Function0,kotlin.Function1,kotlin.Function0,androidx.compose.material.FabPosition,kotlin.Boolean,kotlin.Function1,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1)). It contains a top app bar, bottom app bar, and a floating action
button that interacts with `Scaffold`'s internal state.

## Key points

The [`Scaffold`](/reference/kotlin/androidx/compose/material/ScaffoldState) composable provides a straightforward API you can use to
quickly assemble your app's structure according to Material Design guidelines.
`Scaffold` accepts several composables as parameters. Among these are the
following:

* `topBar`: The app bar across the top of the screen.
* `bottomBar`: The app bar across the bottom of the screen.
* `floatingActionButton`: A button that hovers over the bottom-right corner of
  the screen that you can use to expose key actions.

For more detailed examples on how you can implement both top and bottom
app bars, see the app bars page.

You can also pass `Scaffold` content as you would to other containers. It passes
an `innerPadding` value to the `content` lambda that you can then use in child
composables.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Create a home screen scaffold

Find out how to use a standardized platform to build
complex user interfaces. The scaffold holds together different parts of
the UI, giving apps a coherent look and feel.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/create-a-home-screen-scaffold)

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