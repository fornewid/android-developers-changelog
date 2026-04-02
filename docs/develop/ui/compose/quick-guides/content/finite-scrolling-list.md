---
title: Create a finite scrollable list  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/finite-scrolling-list
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Create a finite scrollable list Stay organized with collections Save and categorize content based on your preferences.



Scrollable lists can help manage datasets, create responsive designs, and
facilitate navigation. You can display smaller sets of items in your app
by using a finite scrolling list. To avoid performance issues with larger
datasets or a list of unknown length, see
[Lazily load data with lists and Paging](/develop/ui/compose/quick-guides/content/lazily-load-list).

## Results

![A vertical list responding to scroll
gestures](/static/develop/ui/compose/images/gestures-simplescroll.gif)


**Figure 1.** A vertical scrolling list.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

## Create a vertical scrolling list

Use the following code to create a vertical scrolling list:

```
@Composable
private fun ScrollBoxes() {
    Column(
        modifier = Modifier
            .background(Color.LightGray)
            .size(100.dp)
            .verticalScroll(rememberScrollState())
    ) {
        repeat(10) {
            Text("Item $it", modifier = Modifier.padding(2.dp))
        }
    }
}

GesturesSnippets.kt
```

### Key points about the code

* Sets the [`Column`](/reference/kotlin/androidx/compose/foundation/layout/Column.composable#Column(androidx.compose.ui.Modifier,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,kotlin.Function1)) scrolling behavior with the [`verticalScroll`](/reference/kotlin/androidx/compose/foundation/verticalScroll.modifier#(androidx.compose.ui.Modifier).verticalScroll(androidx.compose.foundation.ScrollState,kotlin.Boolean,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean))
  modifier and the [`rememberScrollState`](/reference/kotlin/androidx/compose/foundation/rememberScrollState.composable#rememberScrollState(kotlin.Int)) function.
* To create a horizontal scrolling list, create a [`Row`](/reference/kotlin/androidx/compose/foundation/layout/Row.composable#Row(androidx.compose.ui.Modifier,androidx.compose.foundation.layout.Arrangement.Horizontal,androidx.compose.ui.Alignment.Vertical,kotlin.Function1)) with a
  [`horizontalScroll`](/reference/kotlin/androidx/compose/foundation/horizontalScroll.modifier#(androidx.compose.ui.Modifier).horizontalScroll(androidx.compose.foundation.ScrollState,kotlin.Boolean,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean)) modifier.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Display a list or grid

Lists and grids allow your app to display collections in a
visually pleasing form that's easy for users to consume.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/display-a-list-or-grid)

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Display interactive components

Learn how composable functions can enable you to easily
create beautiful UI components based on the Material Design design
system.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/display-interactive-components)

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Compose basics (video collection)

This series of videos introduces various Compose APIs,
quickly showing you what’s available and how to use them.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/compose-basics)

![](/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.

[Go to FAQ](/quick-guides/faq)
[Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)