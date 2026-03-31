---
title: About WindowInsetsRulers  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/system/evaluate-rulers
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# About WindowInsetsRulers Stay organized with collections Save and categorize content based on your preferences.




[`WindowInsets`](/reference/kotlin/androidx/compose/foundation/layout/WindowInsets) is the standard API in Jetpack Compose for handling
areas of the screen that are partially or fully obscured by the system UI. These
areas include the status bar, navigation bar, and on-screen keyboard. You can
alternatively pass predefined [`WindowInsetsRulers`](/reference/kotlin/androidx/compose/ui/layout/WindowInsetsRulers) like [`SafeDrawing`](/reference/kotlin/androidx/compose/ui/layout/WindowInsetsRulers#SafeDrawing()) to
[`Modifier.fitInside`](/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).fitInside(androidx.compose.ui.layout.RectRulers)) or [`Modifier.fitOutside`](/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).fitOutside(androidx.compose.ui.layout.RectRulers)) to align your content
with the system bars and the display cutout or create custom
`WindowInsetsRulers`.

## Advantages of `WindowInsetsRulers`

* **Avoids Consumption Complexity**: It operates during the **placement phase**
  of layout. This means it completely bypasses the inset consumption chain and
  can always provide the correct, absolute positions of system bars and display
  cutouts, regardless of what parent layouts have done. Using the
  `Modifier.fitInside` or `Modifier.fitOutside` methods are helpful in fixing
  issues when ancestor Composables incorrectly consume insets.
* **Easily avoid the system bars**: It helps your app content avoid system bars
  and the display cutout, and can be more straightforward than using
  `WindowInsets` directly.
* **Highly customizable**: Developers can align content to custom rulers, and
  have precise control over their layouts with custom layouts.

## Disadvantages of `WindowInsetsRulers`

* **Can't be used for Measurement**: Because it operates during the placement
  phase, the positional information it provides is **not available** during the
  earlier measurement phase.

## Align your content with Modifier methods

[`Modifier.fitInside`](/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).fitInside(androidx.compose.ui.layout.RectRulers)) allows apps to align content to system bars and display
cutouts. It can be used instead of `WindowInsets`. [`Modifier.fitOutside`](/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).fitOutside(androidx.compose.ui.layout.RectRulers)) is
usually the inverse of `Modifier.fitInside`.

For example, to verify that app content avoids the system bars and display
cutout, you can use `fitInside(WindowInsetsRulers.safeDrawing.current)`.

```
@Composable
fun FitInsideDemo(modifier: Modifier) {
    Box(
        modifier = modifier
            .fillMaxSize()
            // Or DisplayCutout, Ime, NavigationBars, StatusBar, etc...
            .fitInside(WindowInsetsRulers.SafeDrawing.current)
    )
}

InsetsSnippets.kt
```

The following table shows what your app content would look like with predefined
rulers with either `Modifier.fitInside` or `Modifier.fitOutside`.

| Predefined ruler type | [`Modifier.fitInside`](/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).fitInside(androidx.compose.ui.layout.RectRulers)) | [`Modifier.fitOutside`](/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).fitOutside(androidx.compose.ui.layout.RectRulers)) |
| --- | --- | --- |
| [`DisplayCutout`](/reference/kotlin/androidx/compose/ui/layout/WindowInsetsRulers#DisplayCutout()) |  |  |
| [`Ime`](/reference/kotlin/androidx/compose/ui/layout/WindowInsetsRulers#Ime()) |  | N/A |
| [`NavigationBars`](/reference/kotlin/androidx/compose/ui/layout/WindowInsetsRulers#NavigationBars()) |  |  |
| [`SafeDrawing`](/reference/kotlin/androidx/compose/ui/layout/WindowInsetsRulers#SafeDrawing()) |  | N/A (use `StatusBar`, `CaptionBar`, `NavigationBar` instead) |
| [`StatusBar`](/reference/kotlin/androidx/compose/ui/layout/WindowInsetsRulers#StatusBars()) |  |  |

Using `Modifier.fitInside` and `Modifier.fitOutside` requires that the
composables are constrained. This means you must define modifiers like
`Modifier.size` or `Modifier.fillMaxSize`.

Some rulers like `Modifier.fitOutside` on `SafeDrawing` and `SystemBars` return
multiple rulers. In this case, Android places the Composable using one ruler
from left, top, right, bottom.

### Avoid the IME with Modifier.fitInside

To handle bottom elements with an IME with `Modifier.fitInside`, pass in a
`RectRuler` that takes the innermost value of `NavigationBar` and `Ime`.

```
@Composable
fun FitInsideWithImeDemo(modifier: Modifier) {
    Box(
        modifier = modifier
            .fillMaxSize()
            .fitInside(
                RectRulers.innermostOf(
                    WindowInsetsRulers.NavigationBars.current,
                    WindowInsetsRulers.Ime.current
                )
            )
    ) {
        TextField(
            value = "Demo IME Insets",
            onValueChange = {},
            modifier = modifier.align(Alignment.BottomStart).fillMaxWidth()
        )
    }
}

InsetsSnippets.kt
```

### Avoid the status bar and caption bar with Modifier.fitInside

Similarly, to verify top elements avoid the status bar and caption bar together
with `Modifier.fitInsider`, pass a `RectRuler` that takes the innermost value of
`StatusBars` and `CaptionBar`.

```
@Composable
fun FitInsideWithStatusAndCaptionBarDemo(modifier: Modifier) {
    Box(
        modifier = modifier
            .fillMaxSize()
            .fitInside(
                RectRulers.innermostOf(
                    WindowInsetsRulers.StatusBars.current,
                    WindowInsetsRulers.CaptionBar.current
                )
            )
    )
}

InsetsSnippets.kt
```

## Create custom `WindowInsetsRulers`

You can align content to custom rulers. For example, consider the use case where
a parent composable improperly handles insets causing padding issues in a
downstream child. While this issue can be solved in other ways, including by
using `Modifier.fitInside`, you can also create a custom ruler to precisely
align the child composable without having the fix the issue in the parent
upstream as shown in the following example and video:

```
@Composable
fun WindowInsetsRulersDemo(modifier: Modifier) {
    Box(
        contentAlignment = BottomCenter,
        modifier = modifier
            .fillMaxSize()
            // The mistake that causes issues downstream, as .padding doesn't consume insets.
            // While it's correct to instead use .windowInsetsPadding(WindowInsets.navigationBars),
            // assume it's difficult to identify this issue to see how WindowInsetsRulers can help.
            .padding(WindowInsets.navigationBars.asPaddingValues())
    ) {
        TextField(
            value = "Demo IME Insets",
            onValueChange = {},
            modifier = modifier
                // Use alignToSafeDrawing() instead of .imePadding() to precisely place this child
                // Composable without having to fix the parent upstream.
                .alignToSafeDrawing()

            // .imePadding()
            // .fillMaxWidth()
        )
    }
}

fun Modifier.alignToSafeDrawing(): Modifier {
    return layout { measurable, constraints ->
        if (constraints.hasBoundedWidth && constraints.hasBoundedHeight) {
            val placeable = measurable.measure(constraints)
            val width = placeable.width
            val height = placeable.height
            layout(width, height) {
                val bottom = WindowInsetsRulers.SafeDrawing.current.bottom
                    .current(0f).roundToInt() - height
                val right = WindowInsetsRulers.SafeDrawing.current.right
                    .current(0f).roundToInt()
                val left = WindowInsetsRulers.SafeDrawing.current.left
                    .current(0f).roundToInt()
                measurable.measure(Constraints.fixed(right - left, height))
                    .place(left, bottom)
            }
        } else {
            val placeable = measurable.measure(constraints)
            layout(placeable.width, placeable.height) {
                placeable.place(0, 0)
            }
        }
    }
}

InsetsSnippets.kt
```

The following video shows an example of problematic IME inset consumption
caused by an upstream parent in the image on the left, and using custom rulers
to fix the issue on the right. Extra padding is shown underneath the `TextField`
Composable as the navigation bar padding wasn't consumed by the parent. The
child is placed in the correct location in the right image using a custom ruler
as seen in the preceding code sample.

[](/static/develop/ui/compose/images/layouts/insets/WindowInsetsRulers.mp4)

### Verify that parents are constrained

In order to safely use `WindowInsetsRulers`, make sure the parent provides valid
constraints. Parents must have a defined size and can't depend on the size of a
child that uses `WindowInsetsRulers`. Use `fillMaxSize` or other size modifiers
on parent Composables.

Similarly, placing a composable that uses `WindowInsetsRulers` inside a
scrolling container like `verticalScroll` can cause unexpected behavior as the
scrolling container provides unbounded height constraints, which are
incompatible with the ruler's logic.

[Previous

arrow\_back

Set up edge-to-edge](/develop/ui/compose/system/setup-e2e)

[Next

About window insets

arrow\_forward](/develop/ui/compose/system/insets)