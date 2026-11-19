---
title: https://developer.android.com/develop/ui/compose/layouts/alignment-lines
url: https://developer.android.com/develop/ui/compose/layouts/alignment-lines
source: md.txt
---

> Documentation index: https://developer.android.com/develop/ui/compose/layouts/llms.txt

The Compose layout model lets you use [`AlignmentLine`](https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/AlignmentLine.md.txt) to create custom
alignment lines that can be used by parent layouts to align and position their
children. For example, [`Row`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/Row.composable.md.txt#Row(androidx.compose.ui.Modifier,androidx.compose.foundation.layout.Arrangement.Horizontal,androidx.compose.ui.Alignment.Vertical,kotlin.Function1)(androidx.compose.ui.Modifier,androidx.compose.foundation.layout.Arrangement.Horizontal,androidx.compose.ui.Alignment.Vertical,kotlin.Function1)) can use its children's custom alignment lines
to align them.

When a layout provides a value for a particular `AlignmentLine`, the layout's
parents can read this value after measuring, using the [`Placeable.get`](https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/Placeable.md.txt#get(androidx.compose.ui.layout.AlignmentLine))
operator on the corresponding [`Placeable`](https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/Placeable.md.txt) instance. Based on the position
of the `AlignmentLine`, the parents can then decide the positioning of the
children.

Some composables in Compose already come with alignment lines. For example, the
[`BasicText`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/BasicText.composable.md.txt) composable exposes the `FirstBaseline` and `LastBaseline`
alignment lines.

In the following example, a custom [`LayoutModifier`](https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/LayoutModifier.md.txt) called
`firstBaselineToTop` reads the `FirstBaseline` to add padding to the `Text`
starting from its first baseline.
![Shows the difference between adding normal padding to an element,
and applying padding to a Text element's baseline.](https://developer.android.com/static/develop/ui/compose/images/layouts/alignmentlines-text.png) **Figure 1.** Shows the difference between adding normal padding to an element, and applying padding to a Text element's baseline.


```kotlin
fun Modifier.firstBaselineToTop(
    firstBaselineToTop: Dp,
) = layout { measurable, constraints ->
    // Measure the composable
    val placeable = measurable.measure(constraints)

    // Check the composable has a first baseline
    check(placeable[FirstBaseline] != AlignmentLine.Unspecified)
    val firstBaseline = placeable[FirstBaseline]

    // Height of the composable with padding - first baseline
    val placeableY = firstBaselineToTop.roundToPx() - firstBaseline
    val height = placeable.height + placeableY
    layout(placeable.width, height) {
        // Where the composable gets placed
        placeable.placeRelative(0, placeableY)
    }
}

@Preview
@Composable
private fun TextWithPaddingToBaseline() {
    MaterialTheme {
        Text("Hi there!", Modifier.firstBaselineToTop(32.dp))
    }
}
```

<br />

In order to read the `FirstBaseline` in the example, `placeable [FirstBaseline]`
is used in the measurement phase.

> [!NOTE]
> **Note:** The `firstBaselineToTop` modifier is shown for educational purposes. The Compose library provides a [`paddingFrom`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/paddingFrom.modifier.md.txt#(androidx.compose.ui.Modifier).paddingFrom(androidx.compose.ui.layout.AlignmentLine,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp)) modifier that lets you specify padding relative to any alignment line defined in that layout.

The following example uses `paddingFrom` to place the first baseline of the
`Text` 32 dp from the top, like the `firstBaselineToTop` example. To pad from
the first and last baselines of text, use [`paddingFromBaseline`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/paddingFromBaseline.modifier.md.txt#(androidx.compose.ui.Modifier).paddingFromBaseline(androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp)).


```kotlin
@Composable
private fun TextWithPaddingFromBaseline() {
    MaterialTheme {
        Text("Hi there!", Modifier.paddingFrom(FirstBaseline, before = 32.dp))
    }
}
```

<br />

![Hi there! text with 32 dp of padding above its first baseline.](https://developer.android.com/static/develop/ui/compose/images/layouts/alignmentlines-padding-from.png) **Figure 2.** `Text` with 32 dp of padding before its first baseline.

## Align the children of a row

In a `Row`, the [`alignByBaseline`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/RowScope.md.txt#(androidx.compose.ui.Modifier).alignByBaseline()) and [`alignBy`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/RowScope.md.txt#(androidx.compose.ui.Modifier).alignBy(androidx.compose.ui.layout.HorizontalAlignmentLine)) modifiers align
children with each other on an alignment line. Both modifiers are members of
`RowScope`, so you can use them only inside a `RowScope`, such as the content of
a `Row`. Apply the modifier to each child that must align. A child without it,
and without `align`, follows the `verticalAlignment` of the `Row`.

The following example aligns two texts of different sizes on their first
baselines:


```kotlin
@Composable
private fun TitleWithSubtitle() {
    MaterialTheme {
        Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
            Text(
                "Title",
                modifier = Modifier.alignByBaseline(),
                style = MaterialTheme.typography.headlineMedium
            )
            Text(
                "Subtitle",
                modifier = Modifier.alignByBaseline(),
                style = MaterialTheme.typography.bodySmall
            )
        }
    }
}
```

<br />

![Title text and smaller Subtitle text aligned on their baselines.](https://developer.android.com/static/develop/ui/compose/images/layouts/alignmentlines-align-baseline.png) **Figure 3.** Two `Text` elements of different sizes aligned on their first baselines.

`alignByBaseline` is the same as `alignBy(FirstBaseline)`. To align on a
position that isn't an alignment line, pass a block to `alignBy`. The block
receives the measured child and returns the distance, in pixels, from the top of
the child to the line to align on. In the following example, the middle of a
small box sits on the baseline of the text next to it:


```kotlin
@Composable
private fun BoxMiddleOnBaseline() {
    MaterialTheme {
        Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
            Box(
                modifier = Modifier
                    .size(8.dp)
                    .background(Color.Gray)
                    // Aligns the middle of the box with the text baseline.
                    .alignBy { it.measuredHeight / 2 }
            )
            Text(
                "Label",
                modifier = Modifier.alignByBaseline()
            )
        }
    }
}
```

<br />

![Small gray square centered vertically on the baseline of Label text.](https://developer.android.com/static/develop/ui/compose/images/layouts/alignmentlines-align-block.png) **Figure 4.** A gray `Box` with its vertical center aligned to the baseline of the adjacent `Text`.

The children that use these modifiers form one group. The `Row` places at least
one child of the group as if it had `Alignment.Top`, and positions the others so
that their lines match. A child that is alone in the group is placed as if it
had `Alignment.Top`, so it doesn't align with anything. `alignBy` is a form of
[`align`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/RowScope.md.txt#(androidx.compose.ui.Modifier).align(androidx.compose.ui.Alignment.Vertical)), so the two modifiers don't work together on the same child.

`paddingFrom` and `alignBy` solve different problems: `paddingFrom` adds padding
to one element based on its own alignment line, and `alignBy` aligns siblings
with each other.

In a [`Column`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/Column.composable.md.txt#Column(androidx.compose.ui.Modifier,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,kotlin.Function1)), `alignBy` takes a `VerticalAlignmentLine` or a block, and
aligns the children horizontally. `ColumnScope` has no `alignByBaseline`.

## Create custom alignment lines

When creating a custom [`Layout`](https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/Layout.composable.md.txt#Layout(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.layout.MeasurePolicy)) composable or a custom
[`LayoutModifier`](https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/LayoutModifier.md.txt), you can provide custom alignment lines so that other
parent composables can use them to align and position their children
accordingly.

> [!NOTE]
> **Note:** If you want to learn more about creating custom [`Layout`](https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/Layout.composable.md.txt#Layout(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.layout.MeasurePolicy)) composables and layout modifiers, check out the [Custom layouts](https://developer.android.com/develop/ui/compose/layouts/custom.md.txt) documentation.

The following example shows a custom `BarChart` composable that exposes two
alignment lines, `MaxChartValue` and `MinChartValue`, so that other composables
can align to the maximum and minimum data value of the chart. Two text elements,
*Max* and *Min*, have been aligned to the center of the custom alignment lines.
![BarChart composable with Text aligned to the maximum and
minimum data value.](https://developer.android.com/static/develop/ui/compose/images/layouts/alignmentlines-chart.png) **Figure 5.** `BarChart` composable with Text aligned to the maximum and minimum data value.

Custom alignment lines are defined as top-level variables in your project.


```kotlin
/**
 * AlignmentLine defined by the maximum data value in a [BarChart]
 */
private val MaxChartValue = HorizontalAlignmentLine(merger = { old, new ->
    min(old, new)
})

/**
 * AlignmentLine defined by the minimum data value in a [BarChart]
 */
private val MinChartValue = HorizontalAlignmentLine(merger = { old, new ->
    max(old, new)
})
```

<br />

The custom alignment lines to create our example are of type
[`HorizontalAlignmentLine`](https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/HorizontalAlignmentLine.md.txt), as
they're used to align children vertically. A merge policy is passed as a
parameter in case multiple layouts provide a value for these alignment lines. As
the Compose layout system coordinates and the [`Canvas`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/Canvas.composable.md.txt)
coordinates represent `[0, 0]`, the top left corner and the `x` and `y` axis are
positive downwards, so the `MaxChartValue` value will always be smaller than
`MinChartValue`. Therefore, the merge policy is `min` for the maximum chart
data value baseline, and `max` for the minimum chart data value baseline.

When creating a custom `Layout` or `LayoutModifier`, specify custom alignment
lines in the [`MeasureScope.layout`](https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/MeasureScope.md.txt#layout(kotlin.Int,kotlin.Int,kotlin.collections.Map,kotlin.Function1)) method, which takes an
`alignmentLines: Map<AlignmentLine, Int>` parameter.


```kotlin
@Composable
private fun BarChart(
    dataPoints: List<Int>,
    modifier: Modifier = Modifier,
) {
    val maxValue: Float = remember(dataPoints) { dataPoints.maxOrNull()!! * 1.2f }

    BoxWithConstraints(modifier = modifier) {
        val density = LocalDensity.current
        with(density) {
            // ...
            // Calculate baselines
            val maxYBaseline = // ...
            val minYBaseline = // ...
            Layout(
                content = {},
                modifier = Modifier.drawBehind {
                    // ...
                }
            ) { _, constraints ->
                with(constraints) {
                    layout(
                        width = if (hasBoundedWidth) maxWidth else minWidth,
                        height = if (hasBoundedHeight) maxHeight else minHeight,
                        // Custom AlignmentLines are set here. These are propagated
                        // to direct and indirect parent composables.
                        alignmentLines = mapOf(
                            MinChartValue to minYBaseline.roundToInt(),
                            MaxChartValue to maxYBaseline.roundToInt()
                        )
                    ) {}
                }
            }
        }
    }
}
```

<br />

**Direct and indirect parents of this composable can consume the alignment
lines** . The following composable creates a custom layout that takes as a
parameter two `Text` slots and data points, and aligns the two texts to the
maximum and minimum chart data values. The preview of this composable is
what's shown in Figure 5.


```kotlin
@Composable
private fun BarChartMinMax(
    dataPoints: List<Int>,
    maxText: @Composable () -> Unit,
    minText: @Composable () -> Unit,
    modifier: Modifier = Modifier,
) {
    Layout(
        content = {
            maxText()
            minText()
            // Set a fixed size to make the example easier to follow
            BarChart(dataPoints, Modifier.size(200.dp))
        },
        modifier = modifier
    ) { measurables, constraints ->
        check(measurables.size == 3)
        val placeables = measurables.map {
            it.measure(constraints.copy(minWidth = 0, minHeight = 0))
        }

        val maxTextPlaceable = placeables[0]
        val minTextPlaceable = placeables[1]
        val barChartPlaceable = placeables[2]

        // Obtain the alignment lines from BarChart to position the Text
        val minValueBaseline = barChartPlaceable[MinChartValue]
        val maxValueBaseline = barChartPlaceable[MaxChartValue]
        layout(constraints.maxWidth, constraints.maxHeight) {
            maxTextPlaceable.placeRelative(
                x = 0,
                y = maxValueBaseline - (maxTextPlaceable.height / 2)
            )
            minTextPlaceable.placeRelative(
                x = 0,
                y = minValueBaseline - (minTextPlaceable.height / 2)
            )
            barChartPlaceable.placeRelative(
                x = max(maxTextPlaceable.width, minTextPlaceable.width) + 20,
                y = 0
            )
        }
    }
}
@Preview
@Composable
private fun ChartDataPreview() {
    MaterialTheme {
        BarChartMinMax(
            dataPoints = listOf(4, 24, 15),
            maxText = { Text("Max") },
            minText = { Text("Min") },
            modifier = Modifier.padding(24.dp)
        )
    }
}
```

<br />

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Graphics in Compose](https://developer.android.com/develop/ui/compose/graphics/draw/overview.md.txt)
- [Custom layouts {:#custom-layouts }](https://developer.android.com/develop/ui/compose/layouts/custom.md.txt)
- [Intrinsic measurements in Compose layouts](https://developer.android.com/develop/ui/compose/layouts/intrinsic-measurements.md.txt)