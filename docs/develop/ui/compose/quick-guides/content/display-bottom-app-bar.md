---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/display-bottom-app-bar
url: https://developer.android.com/develop/ui/compose/quick-guides/content/display-bottom-app-bar
source: md.txt
---

<br />

Create a bottom app bar to help users navigate and access functions in your app.
Follow this guidance to add a bottom app bar to your app by using the
[`BottomAppBar`](https://developer.android.com/reference/com/google/android/material/bottomappbar/BottomAppBar) composable.

## Results

![An example of a bottom app bar](https://developer.android.com/static/develop/ui/compose/quick-guides/content/bottom-app-bar.png) **Figure 1.** An example of a bottom app bar.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/display-bottom-app-bar_3a2b552451c600770ced3cf232b4eae6bfd7c5a087c97f6847de20396400e5b5.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Create a bottom app bar

Use the following code to create a bottom app bar containing four icon buttons,
and a floating action button:


```kotlin
@Composable
fun BottomAppBarExample() {
    Scaffold(
        bottomBar = {
            BottomAppBar(
                actions = {
                    IconButton(onClick = { /* do something */ }) {
                        Icon(Icons.Filled.Check, contentDescription = "Localized description")
                    }
                    IconButton(onClick = { /* do something */ }) {
                        Icon(
                            Icons.Filled.Edit,
                            contentDescription = "Localized description",
                        )
                    }
                    IconButton(onClick = { /* do something */ }) {
                        Icon(
                            Icons.Filled.Mic,
                            contentDescription = "Localized description",
                        )
                    }
                    IconButton(onClick = { /* do something */ }) {
                        Icon(
                            Icons.Filled.Image,
                            contentDescription = "Localized description",
                        )
                    }
                },
                floatingActionButton = {
                    FloatingActionButton(
                        onClick = { /* do something */ },
                        containerColor = BottomAppBarDefaults.bottomAppBarFabColor,
                        elevation = FloatingActionButtonDefaults.bottomAppBarFabElevation()
                    ) {
                        Icon(Icons.Filled.Add, "Localized description")
                    }
                }
            )
        },
    ) { innerPadding ->
        Text(
            modifier = Modifier.padding(innerPadding),
            text = "Example of a scaffold with a bottom app bar."
        )
    }
}
```

<br />

### Key points about the code

- An outer [`Scaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Scaffold(androidx.compose.foundation.layout.WindowInsets,androidx.compose.ui.Modifier,androidx.compose.material.ScaffoldState,kotlin.Function0,kotlin.Function0,kotlin.Function1,kotlin.Function0,androidx.compose.material.FabPosition,kotlin.Boolean,kotlin.Function1,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1)) that has a `bottomBar` set.
- A `bottomBar` implementation that contains a list of actions.
- Actions that are implementations of [`IconButton`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#IconButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)) that contain [`Icon`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Icon(androidx.compose.ui.graphics.ImageBitmap,kotlin.String,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color)) for image and content description text, each with an `onClick` lambda to perform these actions.

You can pass composables for the following key parameters:

- `actions`: a series of icons that appear on the left side of the bar. These are commonly either key actions for the given screen, or navigation items.
- [`floatingActionButton`](https://developer.android.com/reference/com/google/android/material/floatingactionbutton/FloatingActionButton): the floating action button that appears on the right side of the bar.

> [!NOTE]
> **Note:** After you add the bottom app bar, you can customize it with content as you do with other containers by filling the `BottomAppBar` composable with other content. You can also use `BottomAppBar` without passing a value for `actions` or `floatingActionButton`.

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