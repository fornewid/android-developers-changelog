---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/video/lists-in-compose
url: https://developer.android.com/develop/ui/compose/quick-guides/content/video/lists-in-compose
source: md.txt
---

<br />

Explore Compose's lazy components, which make it easy to display lists of items.
Learn how to show different item types, implement sticky headers, and
programmatically control or react to the scroll-position changes.  

## Key points

- The [`LazyColumn`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/package-summary#LazyColumn(androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.LazyListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,kotlin.Function1)) API is built as a DSL, differing from other layouts in Compose.
- Use `LazyColumn` to display items visible on screen.
- Use the [`items()`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/LazyListScope#items(kotlin.Int,kotlin.Function1,kotlin.Function1,kotlin.Function2)) function to pass items. The lambda defines the content of each of the items, so you can keep the existing code.
- To display many different item types, use the `groupBy` function.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:  
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png)  
![](https://developer.android.com/static/images/picto-icons/collection.svg)  

### Display a list or grid

Lists and grids allow your app to display collections in a visually pleasing form that's easy for users to consume.  
[Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-a-list-or-grid)  
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png)  
![](https://developer.android.com/static/images/picto-icons/collection.svg)  

### Compose basics (video collection)

This series of videos introduces various Compose APIs, quickly showing you what's available and how to use them.  
[Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/compose-basics)
![](https://developer.android.com/static/images/picto-icons/help.svg)  

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.  
[Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)