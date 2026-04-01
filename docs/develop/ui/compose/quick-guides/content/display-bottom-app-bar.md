---
title: Display a bottom app bar  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/display-bottom-app-bar
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Display a bottom app bar Stay organized with collections Save and categorize content based on your preferences.



Create a bottom app bar to help users navigate and access functions in your app.
Follow this guidance to add a bottom app bar to your app by using the
[`BottomAppBar`](/reference/com/google/android/material/bottomappbar/BottomAppBar) composable.

## Results

![ An example of a bottom app bar](/static/develop/ui/compose/quick-guides/content/bottom-app-bar.png)


**Figure 1.** An example of a bottom app bar.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

## Create a bottom app bar

Use the following code to create a bottom app bar containing four icon buttons,
and a floating action button:

```
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

AppBar.kt
```

### Key points about the code

* An outer [`Scaffold`](/reference/kotlin/androidx/compose/material/Scaffold.composable#Scaffold(androidx.compose.foundation.layout.WindowInsets,androidx.compose.ui.Modifier,androidx.compose.material.ScaffoldState,kotlin.Function0,kotlin.Function0,kotlin.Function1,kotlin.Function0,androidx.compose.material.FabPosition,kotlin.Boolean,kotlin.Function1,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1)) that has a `bottomBar` set.
* A `bottomBar` implementation that contains a list of actions.
* Actions that are implementations of [`IconButton`](/reference/kotlin/androidx/compose/material/IconButton.composable#IconButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)) that contain
  [`Icon`](/reference/kotlin/androidx/compose/material3/Icon.composable#Icon(androidx.compose.ui.graphics.ImageBitmap,kotlin.String,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color)) for image and content description text, each with an `onClick`
  lambda to perform these actions.

You can pass composables for the following key parameters:

* `actions`: a series of icons that appear on the left side of the bar. These
  are commonly either key actions for the given screen, or navigation items.
* [`floatingActionButton`](/reference/com/google/android/material/floatingactionbutton/FloatingActionButton): the floating action button that appears on the
  right side of the bar.

**Note:** After you add the bottom app bar, you can customize it with content as you
do with other containers by filling the `BottomAppBar` composable with other
content. You can also use `BottomAppBar` without passing a value for `actions`
or `floatingActionButton`.

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