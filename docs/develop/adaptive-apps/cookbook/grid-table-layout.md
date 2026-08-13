---
title: https://developer.android.com/develop/adaptive-apps/cookbook/grid-table-layout
url: https://developer.android.com/develop/adaptive-apps/cookbook/grid-table-layout
source: md.txt
---

![Four star rating icon](https://developer.android.com/static/develop/adaptive-apps/cookbook/images/shared/four-star-rating.png)

This recipe shows how the [`Grid`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/Grid.composable#Grid(kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1)) API improves code readability compared to traditional nested structures. By configuring auto-sized tracks, you can create a grid that dynamically adapts to cell width and height based on the intrinsic size of your text composables.

In this recipe, you build a table using the `Grid` API.

> [!NOTE]
> **Note:** The table content compares `FlexBox` and `Grid` features. `FlexBox` is not used in the layout's code implementation.

|   | Layout | Lazy loading | Soft wrap | Dynamic layout update |
|---|---|---|---|---|
| `FlexBox` | 1D | No | Yes | Yes |
| `Grid` | 2D | No | No | Yes |
[**Table 1.** Feature comparison of the `FlexBox` and `Grid` APIs]

## Best practices

Use the [`Grid`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/Grid.composable#Grid(kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1)) composable to improve table readability and maintainability. `Grid` gives you precise control over column dimensions and alignment across all rows without manually synchronizing widths.

## Ingredients

- [`Grid`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/Grid.composable#Grid(kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1)): A composable layout that places items in a two-dimensional grid. The layout configuration is specified inside the `config` lambda parameter, while UI content items are declared inside the `content` lambda parameter.
- [`GridTrackSize.Auto`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/GridTrackSize#Auto()): Specifies automatic track sizing within the grid configuration based on content intrinsic size, for example, `column(GridTrackSize.Auto)` and `row(GridTrackSize.Auto)`.
- [`gap()`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/GridConfigurationScope#gap(androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp)): Configures row and column spacing within `GridConfigurationScope`, such as `gap(row = 8.dp, column = 16.dp)`.

## Steps

Build a multi-column comparison table using a single `Grid` layout with
automatic column alignment and track sizing for all items.

### 1. Count grid rows and columns to determine track sizes

First, count your columns and rows to determine the size of the tracks:

- **Columns**: The number of attributes you are comparing, plus one column for the item name.
- **Rows**: The number of items you are comparing, plus one header row.

For this recipe comparing two components (`FlexBox` and `Grid`) across four attributes, you need five columns and three rows.

### 2. Implement comparison table using Grid

Create a `TableInGrid` composable that uses `Grid` to lay out your table items. Call the `column` and `row` functions inside the `config` lambda to define track sizes, and set cell spacing with `gap()`. Because text has intrinsic size, `GridTrackSize.Auto` automatically sizes columns and rows to fit their content.

Inside the `content` lambda, place your table headers and data. `Grid` automatically handles the placement and alignment of all cells:


```kotlin
@Composable
fun TableInGrid(
    modifier: Modifier = Modifier,
) {
    Grid(
        config = {
            column(GridTrackSize.Auto)
            column(GridTrackSize.Auto)
            column(GridTrackSize.Auto)
            column(GridTrackSize.Auto)
            column(GridTrackSize.Auto)
            row(GridTrackSize.Auto)
            row(GridTrackSize.Auto)
            row(GridTrackSize.Auto)
            gap(row = 8.dp, column = 16.dp)
        },
        modifier = modifier,
    ) {
        // Table Header
        Text(text = "", fontWeight = FontWeight.Bold)
        Text(text = "Layout", fontWeight = FontWeight.Bold)
        Text(text = "Lazy loading", fontWeight = FontWeight.Bold)
        Text(text = "Soft wrap", fontWeight = FontWeight.Bold)
        Text(text = "Dynamic layout update", fontWeight = FontWeight.Bold)

        // FlexBox Row
        Text(text = "FlexBox", fontWeight = FontWeight.Bold)
        Text(text = "1D")
        Text(text = "No")
        Text(text = "Yes")
        Text(text = "Yes")

        // Grid Row
        Text(text = "Grid", fontWeight = FontWeight.Bold)
        Text(text = "2D")
        Text(text = "No")
        Text(text = "No")
        Text(text = "Yes")
    }
}
```

<br />

## Results

You've now built a clean, two-dimensional comparison table with automatic column alignment and cellspacing.
![](https://developer.android.com/static/develop/adaptive-apps/cookbook/images/feature-comparison-table.png) **Figure 1.** The comparison table using a `Grid`.

## Additional resources

- [Grid in Compose](https://developer.android.com/develop/ui/compose/layouts/adaptive/grid)
- [Set container properties](https://developer.android.com/develop/ui/compose/layouts/adaptive/grid/container-properties)