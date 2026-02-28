---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/finite-scrolling-list
url: https://developer.android.com/develop/ui/compose/quick-guides/content/finite-scrolling-list
source: md.txt
---

<br />

Scrollable lists can help manage datasets, create responsive designs, and
facilitate navigation. You can display smaller sets of items in your app
by using a finite scrolling list. To avoid performance issues with larger
datasets or a list of unknown length, see
[Lazily load data with lists and Paging](https://developer.android.com/develop/ui/compose/quick-guides/content/lazily-load-list).

## Results

<br />

![A vertical list responding to scroll
gestures](https://developer.android.com/static/develop/ui/compose/images/gestures-simplescroll.gif) **Figure 1.** A vertical scrolling list.

<br />

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/finite-scrolling-list_a1e19bb9399af83328f4f119460605b05ca7b024e7aa299476e2a91b55b09539.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Create a vertical scrolling list

Use the following code to create a vertical scrolling list:


```kotlin
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
```

<br />

### Key points about the code

- Sets the [`Column`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#Column(androidx.compose.ui.Modifier,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,kotlin.Function1)) scrolling behavior with the [`verticalScroll`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).verticalScroll(androidx.compose.foundation.ScrollState,kotlin.Boolean,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean)) modifier and the [`rememberScrollState`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#rememberScrollState(kotlin.Int)) function.
- To create a horizontal scrolling list, create a [`Row`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#Row(androidx.compose.ui.Modifier,androidx.compose.foundation.layout.Arrangement.Horizontal,androidx.compose.ui.Alignment.Vertical,kotlin.Function1)) with a [`horizontalScroll`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).horizontalScroll(androidx.compose.foundation.ScrollState,kotlin.Boolean,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean)) modifier.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Display a list or grid

Lists and grids allow your app to display collections in a visually pleasing form that's easy for users to consume. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-a-list-or-grid) ![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Display interactive components

Learn how composable functions can enable you to easily create beautiful UI components based on the Material Design design system. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-interactive-components) ![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Compose basics (video collection)

This series of videos introduces various Compose APIs, quickly showing you what's available and how to use them. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/compose-basics) ![](https://developer.android.com/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts. [Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)