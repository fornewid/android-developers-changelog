---
title: https://developer.android.com/develop/ui/compose/layouts/containers
url: https://developer.android.com/develop/ui/compose/layouts/containers
source: md.txt
---

Jetpack Compose provides several layout containers to help you structure and
arrange your UI components. While fundamental layout composables like `Row` and
`Column` handle straightforward arrangements, many apps require more responsive
and adaptive container solutions as screen sizes change and user data grows.

Layout containers include the following:

- [Lazy lists and lazy grids](https://developer.android.com/develop/ui/compose/lists): Components such as `LazyColumn`, `LazyRow`, and `LazyVerticalGrid` that efficiently display large or dynamically-sized data sets by only composing and laying out items currently visible in the viewport.
- [Pager](https://developer.android.com/develop/ui/compose/layouts/pager): Containers like `HorizontalPager` and `VerticalPager` that let users swipe or scroll between pages of content.
- [Flow layouts](https://developer.android.com/develop/ui/compose/layouts/flow): Responsive one-dimensional containers (`FlowRow` and `FlowColumn`) that automatically wrap overflowing items onto the next row or column when space runs out.
- [Grid](https://developer.android.com/develop/ui/compose/layouts/adaptive/grid): A flexible, two-dimensional structure that displays items in multi-column or multi-row layouts that adapt to the container size.
- [FlexBox](https://developer.android.com/develop/ui/compose/layouts/adaptive/flexbox): A CSS Flexbox-inspired, adaptive container that provides granular control over how items wrap, grow, shrink, and align along main and cross axes to fill available space.

## Choose the correct layout container

When building layouts in Compose, choosing between basic and more advanced
layout containers depends on your design, whether items must wrap when space is
constrained, and how items dynamically resize.

The following table summarizes the capabilities for each of the Compose 1D
layout containers:

|---|---|---|---|---|---|---|---|---|
| **Container** | **Wraps items to new lines** | **Per-item grow** | **Per-item shrink** | **Per-item starting size** | **Items grow to fill available space on multiple lines** | **Reorder items** | **Lazy loading** | **Best for**: |
| **Row / Column** | ❌ | ✅ (via `weight`) single line only | ❌ | ❌ | ❌ | ❌ | ❌ | - Uniform rows with a small, fixed number of items. Items fit within available bounds and don't need to wrap across multiple lines. |
| **FlowRow / FlowColumn** | ✅ | Limited | ❌ | ❌ | Partial | ❌ | ❌ | - Superseded by `FlexBox`. |
| **LazyRow / LazyColumn** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | - Long or infinite lists of items where only the visible items need to be rendered for performance optimization. - Dynamic or large datasets scrolling in a single direction. |
| **FlexBox** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | - Layouts requiring adaptive capabilities, such as specifying initial size, dynamic item growth/shrinking (`grow/shrink`), visual reordering (`order`), or item-level cross-axis alignment (`alignSelf`). - Arranging mixed-size items. |

The following table summarizes the capabilities for `Grid` and other similar
composables:

|---|---|---|---|---|---|
| **Container** | **Strict 2D alignment** | **Item spanning (columns)** | **Item spanning (rows)** | **Lazy loading** | **Best for**: |
| **Grid** | ✅ | ✅ (via `GridArea`) | ✅ | ❌ | - Structural two-dimensional layouts where all items are on screen, and need explicit horizontal and vertical alignment. - Adaptively restructuring layouts across screen sizes. |
| **LazyVerticalGrid** | ✅ | ✅ (via `span`) | ❌ | ✅ | - Vertical scrolling feeds and large catalogs requiring columns. |
| **LazyStaggeredGrid** | ❌ (1D only) | Partial (full span only) | ❌ | ✅ | - Scrolling feeds with mixed-height items. |
| **LazyHorizontalGrid** | ✅ | ❌ | ✅ | ✅ | - Horizontal scrolling carousels or multi-row paginated data. |
| **Combining rows and columns** | ❌ | ❌ | ❌ | ❌ | - Simple component assembly, like placing a text label next to an icon. |