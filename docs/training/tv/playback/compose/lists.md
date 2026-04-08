---
title: Create scrollable layouts for TV  |  Android TV  |  Android Developers
url: https://developer.android.com/training/tv/playback/compose/lists
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android TV](https://developer.android.com/training/tv)

# Create scrollable layouts for TV Stay organized with collections Save and categorize content based on your preferences.




For TV apps, the browsing experience relies on efficient focus-based navigation.
Using standard Compose Foundation lazy layouts, you can create performant
vertical and horizontal lists that automatically handle focus-driven scrolling
to keep active items in view.

## Default scroll behavior optimized for TV

Starting with Compose Foundation 1.7.0, standard lazy layouts (like `LazyRow`
and `LazyColumn`) include built-in support for focus-positioning features. This
is the recommended way to build catalogs for TV apps as it helps keep focused
items remain visible and positioned intuitively for the user.

To implement a basic scrollable list, use the standard lazy components. These
components automatically handle D-pad navigation and bring the focused item into
view.

```
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items

@Composable
fun MovieCatalog(movies: List<Movie>) {
    LazyRow {
        items(movies) { movie ->
            MovieCard(
                movie = movie,
                onClick = { /* Handle click */ }
            )
        }
    }
}
```

## Customize scroll behavior with `BringIntoViewSpec`

If your design requires a specific "pivot" point (for example, keeping the
focused item exactly 30% from the left edge), you can customize the scrolling
behavior using a `BringIntoViewSpec`. This replaces the older `pivotOffsets`
functionality by allowing you to define exactly how the viewport should scroll
to accommodate a focused item.

### 1. Define a custom `BringIntoViewSpec`

The following helper composable lets you define a "pivot" based on parent and
child fractions. The `parentFraction` determines where in the container the item
should land, and the `childFraction` determines which part of the item aligns
with that point.

```
@OptIn(ExperimentalFoundationApi::class)
@Composable
fun PositionFocusedItemInLazyLayout(
    parentFraction: Float = 0.3f,
    childFraction: Float = 0f,
    content: @Composable () -> Unit,
) {
    val bringIntoViewSpec = remember(parentFraction, childFraction) {
        object : BringIntoViewSpec {
            override fun calculateScrollDistance(
                offset: Float,       // Item's initial position
                size: Float,         // Item's size
                containerSize: Float // Container's size
            ): Float {
                // Calculate the offset position of the item's leading edge.
                val initialTargetForLeadingEdge =
                    parentFraction * containerSize - (childFraction * size)
                // If the item fits in the container, and scrolling would cause
                // its trailing edge to be clipped, adjust targetForLeadingEdge
                // to prevent over-scrolling near the end of list.
                val targetForLeadingEdge = if (size <= containerSize &&
                    (containerSize - initialTargetForLeadingEdge) < size) {
                    // If clipped, align the item's trailing edge with the
                    // container's trailing edge.
                    containerSize - size
                } else {
                    initialTargetForLeadingEdge
                }
                // Return scroll distance relative to initial item position.
                return offset - targetForLeadingEdge
            }
        }
    }

    // Apply the spec to all scrollables in the hierarchy
    CompositionLocalProvider(
        LocalBringIntoViewSpec provides bringIntoViewSpec,
        content = content,
    )
}
```

### 2. Apply the custom spec

Wrap your layouts with the helper to apply the positioning. This is useful for
creating a "consistent focus line" across different rows of your catalog.

```
PositionFocusedItemInLazyLayout(
    parentFraction = 0.3f, // Pivot 30% from the edge
    childFraction = 0.5f   // Center of the item aligns with the pivot
) {
    LazyColumn {
        items(sectionList) { section ->
            // This row and its items will respect the 30% pivot
            LazyRow { ... }
        }
    }
}
```

### 3. Opt-out for specific nested layouts

If you have a specific nested layout that should use standard scrolling behavior
instead of your custom pivot, provide the `DefaultBringIntoViewSpec`:

```
private val DefaultBringIntoViewSpec = object : BringIntoViewSpec {}

PositionFocusedItemInLazyLayout {
    LazyColumn {
        item {
            // This row will ignore the custom pivot and use default behavior
            CompositionLocalProvider(LocalBringIntoViewSpec provides DefaultBringIntoViewSpec) {
                LazyRow { ... }
            }
        }
    }
}
```

In effect, by passing an empty `BringIntoViewSpec` enables the framework's
default behavior to take over.

## Migration from TV Foundation to Compose Foundation

The TV-specific lazy layouts in `androidx.tv.foundation` are deprecated in favor
of the standard Compose Foundation layouts.

### Dependency updates

Verify that your `build.gradle` uses version 1.7.0 or higher for:

* `androidx.compose.foundation`
* `androidx.compose.runtime`

### Component mapping

To migrate, update your imports and remove the `Tv` prefix from your components:

| Deprecated TV component | Compose Foundation replacement |
| --- | --- |
| TvLazyRow | LazyRow |
| TvLazyColumn | LazyColumn |
| TvLazyHorizontalGrid | LazyHorizontalGrid |
| TvLazyVerticalGrid | LazyVerticalGrid |
| pivotOffsets | BringIntoViewSpec (via LocalBringIntoViewSpec) |

[Previous

arrow\_back

Build a details screen](/training/tv/playback/compose/details)

[Next

In this guide

arrow\_forward](/training/tv/playback/leanback)