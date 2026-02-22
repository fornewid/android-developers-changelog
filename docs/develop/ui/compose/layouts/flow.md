---
title: https://developer.android.com/develop/ui/compose/layouts/flow
url: https://developer.android.com/develop/ui/compose/layouts/flow
source: md.txt
---

[Video](https://www.youtube.com/watch?v=QaMjBZCXHiI)

[`FlowRow`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#FlowRow(androidx.compose.ui.Modifier,androidx.compose.foundation.layout.Arrangement.Horizontal,androidx.compose.foundation.layout.Arrangement.Vertical,kotlin.Int,kotlin.Function1)) and [`FlowColumn`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#FlowColumn(androidx.compose.ui.Modifier,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.foundation.layout.Arrangement.Horizontal,kotlin.Int,kotlin.Function1))
are composables that are similar to `Row` and `Column`, but differ in that items
flow into the next line when the container runs out of space. This creates
multiple rows or columns. The number of items in a line can also be controlled
by setting `maxItemsInEachRow` or `maxItemsInEachColumn`. You can often use
`FlowRow` and `FlowColumn` to build responsive layouts--- content will not be cut
off if items are too large for one dimension, and using a combination of
`maxItemsInEach*` with `Modifier.weight(weight)` can help build layouts that
fill/expand the width of a row or column when needed.

The typical example is for a chip or filtering UI:
![5 chips in a FlowRow, showing the overflow to the next line when there is no
more space available.](https://developer.android.com/static/develop/ui/compose/images/layouts/flow/flow_row_simple.png) **Figure 1.** Example of `FlowRow`

## Basic usage

To use `FlowRow` or `FlowColumn`, create these composables and place the items
inside it that should follow the standard flow:


```kotlin
@Composable
private fun FlowRowSimpleUsageExample() {
    FlowRow(modifier = Modifier.padding(8.dp)) {
        ChipItem("Price: High to Low")
        ChipItem("Avg rating: 4+")
        ChipItem("Free breakfast")
        ChipItem("Free cancellation")
        ChipItem("£50 pn")
    }
}
```

<br />

This snippet results in the UI shown above, with items automatically flowing to
the next row when there is no more space in the first row.

## Features of flow layout

Flow layouts have the following features and properties that you can use to
create different layouts in your app.

### Main axis arrangement: horizontal or vertical arrangement

The main axis is the axis on which items are laid out (for example, in
`FlowRow`, items are arranged horizontally). The `horizontalArrangement`
parameter in `FlowRow` controls the way free space is distributed between items.

The following table shows examples of setting `horizontalArrangement` on items
for `FlowRow`:

|---|---|
| Horizontal arrangement set on `FlowRow` | Result |
| [`Arrangement.Start`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/Arrangement#Start()) (`Default`) | ![Items arranged with start](https://developer.android.com/static/develop/ui/compose/images/layouts/flow/flow_row_arrangement_start_default.png) |
| [`Arrangement.SpaceBetween`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/Arrangement#SpaceBetween()) | ![Items arrangement with space in between](https://developer.android.com/static/develop/ui/compose/images/layouts/flow/flow_row_arrangement_space_between.png) |
| [`Arrangement.Center`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/Arrangement#Center()) | ![Items arranged in the center](https://developer.android.com/static/develop/ui/compose/images/layouts/flow/flow_row_arrangement_space_center.png) |
| [`Arrangement.End`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/Arrangement#End()) | ![Items arranged at the end](https://developer.android.com/static/develop/ui/compose/images/layouts/flow/flow_row_arrangement_end.png) |
| [`Arrangement.SpaceAround`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/Arrangement#SpaceAround()) | ![Items arranged with space around them](https://developer.android.com/static/develop/ui/compose/images/layouts/flow/flow_row_arrangement_space_around.png) |
| [`Arrangement.spacedBy(8.dp)`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/Arrangement#spacedBy(androidx.compose.ui.unit.Dp)) | ![Items spaced by a certain dp](https://developer.android.com/static/develop/ui/compose/images/layouts/flow/flow_row_arrangement_spaced_by.png) |

For `FlowColumn`, similar options are available with `verticalArrangement`, with
the default of `Arrangement.Top`.

### Cross axis arrangement

The cross axis is the axis in the opposite direction to the main axis. For
example, in `FlowRow`, this is the vertical axis. To change how the overall
contents inside the container are arranged in the cross axis, use
`verticalArrangement` for `FlowRow`, and `horizontalArrangement` for
`FlowColumn`.

For `FlowRow`, the following table shows examples of setting different
`verticalArrangement` on the items:

|---|---|
| **Vertical arrangement set on `FlowRow`** | **Result** |
| [`Arrangement.Top`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/Arrangement#Top()) (`Default`) | ![Container top arrangement](https://developer.android.com/static/develop/ui/compose/images/layouts/flow/flow_container_arrangement_top.png) |
| [`Arrangement.Bottom`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/Arrangement#Bottom()) | ![Container bottom arrangement](https://developer.android.com/static/develop/ui/compose/images/layouts/flow/flow_container_arrangement_bottom.png) |
| [`Arrangement.Center`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/Arrangement#Center()) | ![Container center arrangement](https://developer.android.com/static/develop/ui/compose/images/layouts/flow/flow_container_arrangement_center.png) |

For `FlowColumn`, similar options are available with `horizontalArrangement`.
The default cross axis arrangement is `Arrangement.Start`.

### Individual item alignment

You may want to position individual items within the row with different
alignments. This is different from `verticalArrangement` and
`horizontalArrangement` as it aligns items *within the current line* . You can
apply this with `Modifier.align()`.

For example, when items in a `FlowRow` are different heights, the row takes the
height of the biggest item and applies `Modifier.align(alignmentOption)` to the
items:

|---|---|
| **Vertical alignment set on `FlowRow`** | **Result** |
| [`Alignment.Top`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Alignment#Top()) (`Default`) | ![Items aligned to the top](https://developer.android.com/static/develop/ui/compose/images/layouts/flow/flow_row_item_alignment_top.png) |
| [`Alignment.Bottom`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Alignment#Bottom()) | ![Items aligned to the bottom](https://developer.android.com/static/develop/ui/compose/images/layouts/flow/flow_row_item_alignment_bottom.png) |
| [`Alignment.CenterVertically`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Alignment#CenterVertically()) | ![Items aligned to the center](https://developer.android.com/static/develop/ui/compose/images/layouts/flow/flow_row_item_alignment_center.png) |

For `FlowColumn`, similar options are available. The default alignment is
`Alignment.Start`.

### Max items in row or column

The parameters `maxItemsInEachRow` or `maxItemsInEachColumn` define the maximum
items in the main axis to allow in one line before wrapping to the next. The
default is `Int.MAX_INT`, which allows as many items as possible, as long as
their sizes allow them to fit into the line.

For example, setting a `maxItemsInEachRow` forces the initial layout to only
have 3 items:

|---|---|
| No max set | `maxItemsInEachRow = 3` |
| ![No max set on flow row](https://developer.android.com/static/develop/ui/compose/images/layouts/flow/flow_row_no_max.png) | ![Max items set on flow row](https://developer.android.com/static/develop/ui/compose/images/layouts/flow/flow_row_max_items.png) |

### Item weights

Weight grows an item based on its factor and the available space on the line it
was placed in. Importantly, there is a difference between `FlowRow` and `Row`
with how weights are used to calculate the width of an item. For `Rows`, weight
is based on *all items* in the `Row`. With `FlowRow`, weight is based on the
*items in the line that an item is placed in* , not all the items in the
`FlowRow` container.

For example, if you have 4 items that all fall on a line, each with different
weights of `1f, 2f, 1f`, and `3f`, the total weight is `7f`. The remaining space
in a row or column will be divided by `7f`. Then, each item width will be
calculated using: `weight * (remainingSpace / totalWeight)`.

You can use a combination of `Modifier.weight` and max items with `FlowRow` or
`FlowColumn` to create a grid-like layout. This approach is useful for creating
responsive layouts that adjust to the sizing of your device.

There are a few different examples of what you can achieve using weights. One
example is a grid where items are equally sized, as shown below:
![Grid created with flow row](https://developer.android.com/static/develop/ui/compose/images/layouts/flow/flow_layout_grid_blue.png) **Figure 2.** Using `FlowRow` to create a grid

<br />

To create a grid of equal item sizes, you can do the following:


```kotlin
val rows = 3
val columns = 3
FlowRow(
    modifier = Modifier.padding(4.dp),
    horizontalArrangement = Arrangement.spacedBy(4.dp),
    maxItemsInEachRow = rows
) {
    val itemModifier = Modifier
        .padding(4.dp)
        .height(80.dp)
        .weight(1f)
        .clip(RoundedCornerShape(8.dp))
        .background(MaterialColors.Blue200)
    repeat(rows * columns) {
        Spacer(modifier = itemModifier)
    }
}
```

<br />

Importantly, if you add another item and repeat it 10 times instead of 9, the
last item takes up the entire last column, as the total weight for the whole row
is `1f`:
![Last item full size on grid](https://developer.android.com/static/develop/ui/compose/images/layouts/flow/flow_layout_grid_last_item_large.png) **Figure 3.** Using `FlowRow` to create a grid with the last item taking up full width

You can combine weights with other `Modifiers` such as
`Modifier.width(exactDpAmount), Modifier.aspectRatio(aspectRatio)`, or
`Modifier.fillMaxWidth(fraction)`. These modifiers all work in conjunction to
allow for responsive sizing of items within a `FlowRow` (or `FlowColumn`).

You can also create an alternating grid of different item sizes, where two items
take up half the width each, and one item takes up the full width of the next
column:
![Alternating grid with flow row](https://developer.android.com/static/develop/ui/compose/images/layouts/flow/flow_row_alternating_grid.png) **Figure 4.** `FlowRow` with alternating sizes of rows

You can achieve this with the following code:


```kotlin
FlowRow(
    modifier = Modifier.padding(4.dp),
    horizontalArrangement = Arrangement.spacedBy(4.dp),
    maxItemsInEachRow = 2
) {
    val itemModifier = Modifier
        .padding(4.dp)
        .height(80.dp)
        .clip(RoundedCornerShape(8.dp))
        .background(Color.Blue)
    repeat(6) { item ->
        // if the item is the third item, don't use weight modifier, but rather fillMaxWidth
        if ((item + 1) % 3 == 0) {
            Spacer(modifier = itemModifier.fillMaxWidth())
        } else {
            Spacer(modifier = itemModifier.weight(0.5f))
        }
    }
}
```

<br />

### Fractional sizing

Using `Modifier.fillMaxWidth(fraction)`, you can specify the size of the
container that an item should take up. This is different from how
`Modifier.fillMaxWidth(fraction)` works when applied to `Row` or `Column`, in
that `Row/Column` items take up a percentage of the remaining width, rather than
the whole container's width.

For example, the following code produces different results when using `FlowRow`
vs `Row`:


```kotlin
FlowRow(
    modifier = Modifier.padding(4.dp),
    horizontalArrangement = Arrangement.spacedBy(4.dp),
    maxItemsInEachRow = 3
) {
    val itemModifier = Modifier
        .clip(RoundedCornerShape(8.dp))
    Box(
        modifier = itemModifier
            .height(200.dp)
            .width(60.dp)
            .background(Color.Red)
    )
    Box(
        modifier = itemModifier
            .height(200.dp)
            .fillMaxWidth(0.7f)
            .background(Color.Blue)
    )
    Box(
        modifier = itemModifier
            .height(200.dp)
            .weight(1f)
            .background(Color.Magenta)
    )
}
```

<br />

|---|---|
| `FlowRow`: Middle item with 0.7 fraction of whole container width. | ![Fractional width with flow row](https://developer.android.com/static/develop/ui/compose/images/layouts/flow/flow_row_fractional_width_flow.png) |
| `Row`: Middle item taking up 0.7 percent of remaining `Row` width. | ![Fractional width with row](https://developer.android.com/static/develop/ui/compose/images/layouts/flow/flow_row_fractional_width_row.png) |

### `fillMaxColumnWidth()` and `fillMaxRowHeight()`

Applying either [`Modifier.fillMaxColumnWidth()`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/FlowColumnScope#(androidx.compose.ui.Modifier).fillMaxColumnWidth(kotlin.Float)) or
[`Modifier.fillMaxRowHeight()`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/FlowRowScope#(androidx.compose.ui.Modifier).fillMaxRowHeight(kotlin.Float)) to an item inside a `FlowColumn` or `FlowRow`
ensures that items in the same column or row take up the same width or height as
the biggest item in the column/row.

For example, this example uses `FlowColumn` to display the list of Android
desserts. You can see the difference in each items widths when
`Modifier.fillMaxColumnWidth()` is applied to the items versus when its not and
the items wrap.


```kotlin
FlowColumn(
    Modifier
        .padding(20.dp)
        .fillMaxHeight()
        .fillMaxWidth(),
    horizontalArrangement = Arrangement.spacedBy(8.dp),
    verticalArrangement = Arrangement.spacedBy(8.dp),
    maxItemsInEachColumn = 5,
) {
    repeat(listDesserts.size) {
        Box(
            Modifier
                .fillMaxColumnWidth()
                .border(1.dp, Color.DarkGray, RoundedCornerShape(8.dp))
                .padding(8.dp)
        ) {

            Text(
                text = listDesserts[it],
                fontSize = 18.sp,
                modifier = Modifier.padding(3.dp)
            )
        }
    }
}
```

<br />

|---|---|
| `Modifier.fillMaxColumnWidth()` applied to each item | ![fillMaxColumnWidth](https://developer.android.com/static/develop/ui/compose/images/layouts/flow/flow_max_column_width.png) |
| No width changes set (wrapping items) | ![No fill max column width set](https://developer.android.com/static/develop/ui/compose/images/layouts/flow/flow_no_fill_max_width.png) |

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Compose layout basics](https://developer.android.com/jetpack/compose/layouts/basics)
- [ConstraintLayout in Compose](https://developer.android.com/jetpack/compose/layouts/constraintlayout)
- [Editor actions {:#editor-actions}](https://developer.android.com/jetpack/compose/tooling/editor-actions)