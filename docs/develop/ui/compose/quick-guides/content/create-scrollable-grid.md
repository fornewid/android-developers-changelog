---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/create-scrollable-grid
url: https://developer.android.com/develop/ui/compose/quick-guides/content/create-scrollable-grid
source: md.txt
---

<br />

You can manage large datasets and dynamic content with lazy grids, improving app
performance. With lazy grid composables, you can display items in a scrollable
container, spanned across multiple columns or rows.

## Results

<br />

**Figure 1.** A horizontal scrollable grid using `LazyHorizontalGrid`.

<br />

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-scrollable-grid_a1e19bb9399af83328f4f119460605b05ca7b024e7aa299476e2a91b55b09539.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Decide grid orientation

The [`LazyHorizontalGrid`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/grid/package-summary#LazyHorizontalGrid(androidx.compose.foundation.lazy.grid.GridCells,androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.grid.LazyGridState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Horizontal,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,kotlin.Function1)) and [`LazyVerticalGrid`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/grid/package-summary#LazyVerticalGrid(androidx.compose.foundation.lazy.grid.GridCells,androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.grid.LazyGridState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.foundation.layout.Arrangement.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,kotlin.Function1)) composables provide
support for displaying items in a grid. A lazy vertical grid displays its items
in a vertically scrollable container, spanned across multiple columns, while
lazy horizontal grids have the same behavior on the horizontal axis.

### Create a scrollable grid

The following code creates a horizontal scrolling grid with three columns:


```kotlin
@Composable
fun ScrollingGrid() {
    val itemsList = (0..15).toList()

    val itemModifier = Modifier
        .border(1.dp, Color.Blue)
        .width(80.dp)
        .wrapContentSize()

    LazyHorizontalGrid(
        rows = GridCells.Fixed(3),
        horizontalArrangement = Arrangement.spacedBy(16.dp),
        verticalArrangement = Arrangement.spacedBy(16.dp)
    ) {
        items(itemsList) {
            Text("Item is $it", itemModifier)
        }

        item {
            Text("Single item", itemModifier)
        }
    }
}
```

<br />

### Key points about the code

- The `LazyHorizontalGrid` composable determines the horizontal orientation of the grid.
  - To create a vertical grid, use the `LazyVerticalGrid` instead.
- The `rows` property specifies how to arrange the grid content.
  - For a vertical grid, use the `columns` property to specify the arrangement.
- [`items(itemsList)`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/LazyListScope#items(kotlin.Int,kotlin.Function1,kotlin.Function1,kotlin.Function2)) adds `itemsList` to `LazyHorizontalGrid`. The lambda renders a [`Text`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Text(androidx.compose.ui.text.AnnotatedString,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.font.FontStyle,androidx.compose.ui.text.font.FontWeight,androidx.compose.ui.text.font.FontFamily,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextDecoration,androidx.compose.ui.text.style.TextAlign,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextOverflow,kotlin.Boolean,kotlin.Int,kotlin.Int,kotlin.collections.Map,kotlin.Function1,androidx.compose.ui.text.TextStyle)) composable for each item and set the text to the item description.
- [`item()`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/LazyListScope#item(kotlin.Any,kotlin.Any,kotlin.Function1)) adds a single item to `LazyHorizontalGrid` while the lambda renders a single `Text` composable in a similar manner to `items()`.
- [`GridCells.Fixed`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/grid/GridCells.Fixed) defines the number of rows or columns.
- To create a grid with as many rows as possible, set the number of rows using
  [`GridCells.Adaptive`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/grid/GridCells.Adaptive).

  In the following code, the `20.dp` value
  specifies that every column is at least 20.dp, and all columns have equal
  widths. If the screen is 88.dp wide, there are 4 columns at 22.dp each.
  <iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/create-scrollable-grid_fe5e0b12d80040bc72255125535a693104eb9686afe66e9008879790936f560f.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

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