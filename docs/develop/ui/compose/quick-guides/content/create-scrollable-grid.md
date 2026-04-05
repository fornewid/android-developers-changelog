---
title: Create a scrollable grid  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/create-scrollable-grid
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Create a scrollable grid Stay organized with collections Save and categorize content based on your preferences.



You can manage large datasets and dynamic content with lazy grids, improving app
performance. With lazy grid composables, you can display items in a scrollable
container, spanned across multiple columns or rows.

## Results

[

](/static/develop/ui/compose/quick-guides/content/horizontal_grid_scrolling_example.mp4)


**Figure 1.** A horizontal scrollable grid using `LazyHorizontalGrid`.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

## Decide grid orientation

The [`LazyHorizontalGrid`](/reference/kotlin/androidx/compose/foundation/lazy/grid/LazyHorizontalGrid.composable) and [`LazyVerticalGrid`](/reference/kotlin/androidx/compose/foundation/lazy/grid/LazyVerticalGrid.composable) composables provide
support for displaying items in a grid. A lazy vertical grid displays its items
in a vertically scrollable container, spanned across multiple columns, while
lazy horizontal grids have the same behavior on the horizontal axis.

### Create a scrollable grid

The following code creates a horizontal scrolling grid with three columns:

```
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

LazyListSnippets.kt
```

### Key points about the code

* The `LazyHorizontalGrid` composable determines the horizontal orientation of
  the grid.
  + To create a vertical grid, use the `LazyVerticalGrid` instead.
* The `rows` property specifies how to arrange the grid content.
  + For a vertical grid, use the `columns` property to specify the
    arrangement.
* [`items(itemsList)`](/reference/kotlin/androidx/compose/foundation/lazy/LazyListScope#items(kotlin.Int,kotlin.Function1,kotlin.Function1,kotlin.Function2)) adds `itemsList` to `LazyHorizontalGrid`. The lambda
  renders a [`Text`](/reference/kotlin/androidx/compose/material/Text.composable#Text(androidx.compose.ui.text.AnnotatedString,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.font.FontStyle,androidx.compose.ui.text.font.FontWeight,androidx.compose.ui.text.font.FontFamily,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextDecoration,androidx.compose.ui.text.style.TextAlign,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextOverflow,kotlin.Boolean,kotlin.Int,kotlin.Int,kotlin.collections.Map,kotlin.Function1,androidx.compose.ui.text.TextStyle)) composable for each item and set the text to the item
  description.
* [`item()`](/reference/kotlin/androidx/compose/foundation/lazy/LazyListScope#item(kotlin.Any,kotlin.Any,kotlin.Function1)) adds a single item to `LazyHorizontalGrid` while the lambda
  renders a single `Text` composable in a similar manner to `items()`.
* [`GridCells.Fixed`](/reference/kotlin/androidx/compose/foundation/lazy/grid/GridCells.Fixed) defines the number of rows or columns.
* To create a grid with as many rows as possible, set the number of rows using
  [`GridCells.Adaptive`](/reference/kotlin/androidx/compose/foundation/lazy/grid/GridCells.Adaptive).

  In the following code, the `20.dp` value
  specifies that every column is at least 20.dp, and all columns have equal
  widths. If the screen is 88.dp wide, there are 4 columns at 22.dp each.

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