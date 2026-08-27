---
title: https://developer.android.com/develop/adaptive-apps/cookbook/grid-ui-overlay
url: https://developer.android.com/develop/adaptive-apps/cookbook/grid-ui-overlay
source: md.txt
---

![Four star rating icon](https://developer.android.com/static/develop/adaptive-apps/cookbook/images/shared/four-star-rating.png)

The Jetpack Compose [`Grid`](https://developer.android.com/develop/adaptive-apps/guides/grid) API is designed for structural, two-dimensional screen
layouts. Unlike lazy grids, which are optimized for large data sets, `Grid` lets
you define a fixed *or* responsive layout structure using tracks (rows and columns),
gaps, and [grid areas](https://developer.android.com/develop/adaptive-apps/guides/grid#grid-area). You place items into this structure using `Modifier.gridItem`,
which gives you explicit control over positioning and spanning within the grid
container.

When your UI requires multiple items in the same [grid area](https://developer.android.com/develop/adaptive-apps/guides/grid#grid-area) or overlapping
areas---such as badge overlays, status indicators, or layered cards---coordinate
ambiguity can make layout behavior unpredictable. Managing the depth of overlapping
components without resorting to complex `Box` nesting or manual coordinate offsets is
essential for maintaining clean, readable layout code.

## Best practices

- **Declaration order:** `Grid` follows standard `zIndex` ordering based on the order of declaration within the `Grid` block. Items declared later in the `Grid` content block are rendered on top of items declared earlier.
- **Explicit z-index control:** Use [`Modifier.zIndex`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).zIndex(kotlin.Float)) if you need to explicitly control or override the default drawing order of overlapping elements.
- **Named area vs item overlays:** Use `Grid` and named areas to define the structure of your layout, but keep complex overlay logic inside the specific `gridItem` if those overlays are logically tied to that grid cell.
- **Intentional spans for overlays:** When overlaying, ensure that the `rowSpan` and `columnSpan` parameters are intentional for the overlapping elements to control how much of the underlying content is obscured.

## Ingredients

- [`Grid`](https://developer.android.com/develop/adaptive-apps/guides/grid): A structural, two-dimensional layout container
- [`GridConfigurationScope.area`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/GridConfigurationScope#(androidx.compose.foundation.layout.GridConfigurationScope).area(kotlin.Any,kotlin.Int,kotlin.Int,kotlin.Int,kotlin.Int)): Scope function used to define named regions and overlay areas across grid tracks
- [`Modifier.gridItem`](https://developer.android.com/develop/adaptive-apps/guides/grid/item-properties): Modifier used to place and span composables across grid tracks or into named grid areas
- [`Modifier.zIndex`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).zIndex(kotlin.Float)): Modifier used to explicitly control drawing and layer elevation order

## Steps

Configure your grid layout and named areas, position the base layer content
within target grid coordinates, and place overlay elements in the shared grid
cells or overlapping areas.

### 1. Define the grid configuration

Create a `Grid` composable configuration specifying row and column tracks, as well as named areas that span across cells to define overlay regions:


```kotlin
enum class Areas { BASE, OVERLAY }

val gridConfig: GridConfigurationScope.() -> Unit = {
    repeat(3) {
        column(GridTrackSize.Fixed(100.dp))
    }
    row(GridTrackSize.Fixed(100.dp))

    area(areaId = Areas.BASE, row = 1, column = 1, columnSpan = 2)
    // Define a named area spanning multiple columns that overlaps other cells
    area(areaId = Areas.OVERLAY, row = 1, column = 2, columnSpan = 2)
}
```

<br />

### 2. Place base content and declare overlays

Place your base composables in the grid cells using `Modifier.gridItem`. `Grid`
follows standard `zIndex` ordering based on composition order, so items declared
later within the `Grid` block are drawn on top of earlier items. When placing an
overlay in the same cell or an overlapping area, declare the overlay composable
after the base element, or reference a named area. You can use [`Modifier.zIndex`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).zIndex(kotlin.Float))
if you need to explicitly control or override this default drawing order.


```kotlin
Grid(
    config = gridConfig,
) {
    // Base Layer
    TextCard("BASE", Modifier.gridItem(areaId = Areas.BASE))
    // Overlay Layer
    TextCard(
        "OVERLAY",
        Modifier.gridItem(areaId = Areas.OVERLAY),
        color = Color(0xDD4B608D)
    )
}
```

<br />

## Results

Your UI elements overlay predictably within the 2D grid structure. By
relying on standard declaration ordering, you avoid complex nested
containers while maintaining clean, responsive layout code.
![Grid layout displaying overlaid UI elements](https://developer.android.com/static/develop/adaptive-apps/cookbook/images/grid-overlay-preview.png) **Figure 1.** Overlapping UI elements within a Compose Grid.