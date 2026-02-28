---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/enable-snap-scrolling
url: https://developer.android.com/develop/ui/compose/quick-guides/content/enable-snap-scrolling
source: md.txt
---

<br />

You can display a button to let a user snap scroll to a specific point in a
list, saving time and increasing user engagement.

## Results

![A vertically scrolling list with an active button](https://developer.android.com/static/develop/ui/compose/quick-guides/content/snap-scroll.gif) **Figure 1.** A vertical scrolling list with a snap scroll button.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/enable-snap-scrolling_36533594c991309af129575c6432116d235a7b05b70534b2d1b89cdbe1ded244.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Create a button to enable snap scrolling

Use the following code to create a button for smooth snap scrolling in a
vertical lazy list with 10 items:


```kotlin
@Composable
fun MessageList(modifier: Modifier = Modifier) {
    val listState = rememberLazyListState()
    val coroutineScope = rememberCoroutineScope()

    LazyColumn(state = listState, modifier = Modifier.height(120.dp)) {
        items(10) { index ->
            Text(
                modifier = Modifier.height(40.dp),
                text = "Item $index"
            )
        }
    }

    Button(onClick = {
        coroutineScope.launch {
            listState.animateScrollToItem(index = 0)
        }
    }) {
        Text(text = "Go top")
    }
}
```

<br />

### Key points about the code

- Uses the [`listState`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/LazyListState) object to remember the scroll state of [`LazyColumn`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/package-summary#LazyColumn(androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.LazyListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,kotlin.Function1)) to the selected position.
- Launches a coroutine to call [`listState.animateScrollToItem`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/LazyListState#animateScrollToItem(kotlin.Int,kotlin.Int)), which scrolls to the indexed item while animating the scrolling action.

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