---
title: https://developer.android.com/training/wearables/compose/lists
url: https://developer.android.com/training/wearables/compose/lists
source: md.txt
---

Compose for Wear OS Material version <button value="2.5">2.5</button> <button value="3" default="">3</button>

*** ** * ** ***

Lists let users select an item from a set of choices on Wear OS devices.


Many Wear OS devices use round screens, which makes it more difficult to see
list items that appear near the top and bottom of the screen. For this reason,
Compose for Wear OS includes a version of the `LazyColumn` class called
[`TransformingLazyColumn`](https://developer.android.com/reference/kotlin/androidx/wear/compose/foundation/lazy/package-summary#TransformingLazyColumn(androidx.compose.ui.Modifier,androidx.wear.compose.foundation.lazy.TransformingLazyColumnState,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.wear.compose.foundation.rotary.RotaryScrollableBehavior,androidx.compose.foundation.OverscrollEffect,kotlin.Function1)), which supports scaling and morphing animations.
When items move to the edges, they get smaller and fade out.

To apply the recommended scaling and scrolling effects:

1. Use `Modifier.transformedHeight` to allow Compose to calculate the height change as the item scrolls through the screen.
2. Use `transformation = SurfaceTransformation(transformationSpec)` to apply the visual effects, including scaling down the item contents.
3. Use a custom [`TransformationSpec`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/lazy/TransformationSpec) for components that don't take `transformation` as a parameter such as `Text`.

The following animation shows how a list element scales and changes shape
when approaching the top and bottom of the screen:
The following code snippet shows how to create a list using [`TransformingLazyColumn`](https://developer.android.com/reference/kotlin/androidx/wear/compose/foundation/lazy/package-summary#TransformingLazyColumn(androidx.compose.ui.Modifier,androidx.wear.compose.foundation.lazy.TransformingLazyColumnState,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.wear.compose.foundation.rotary.RotaryScrollableBehavior,androidx.compose.foundation.OverscrollEffect,kotlin.Function1)) layout to create content that [looks great on a variety of Wear OS screen sizes](https://developer.android.com/training/wearables/compose/screen-size).

<br />

The snippet also demonstrates the use of the
`minimumVerticalContentPadding` modifier, which you should set on the list items
to apply the correct padding at the top and bottom of the list.

To show the scroll indicator, share the `columnState` between
the `ScreenScaffold` and the `TransformingLazyColumn`:

```kotlin
val columnState = rememberTransformingLazyColumnState()
val transformationSpec = rememberTransformationSpec()
ScreenScaffold(
    scrollState = columnState
) { contentPadding ->
    TransformingLazyColumn(
        state = columnState,
        contentPadding = contentPadding
    ) {
        item {
            ListHeader(
                modifier = Modifier
                    .fillMaxWidth()
                    .transformedHeight(this, transformationSpec)
                    .minimumVerticalContentPadding(ListHeaderDefaults.minimumTopListContentPadding),
                transformation = SurfaceTransformation(transformationSpec)
            ) {
                Text(text = "Header")
            }
        }
        // ... other items
        item {
            Button(
                modifier = Modifier
                    .fillMaxWidth()
                    .transformedHeight(this, transformationSpec)
                    .minimumVerticalContentPadding(ButtonDefaults.minimumVerticalListContentPadding),
                transformation = SurfaceTransformation(transformationSpec),
                onClick = { /* ... */ },
                icon = {
                    Icon(
                        imageVector = Icons.Default.Build,
                        contentDescription = "build",
                    )
                },
            ) {
                Text(
                    text = "Build",
                    maxLines = 1,
                    overflow = TextOverflow.Ellipsis,
                )
            }
        }
    }
}
```

## Add a snap-and-fling effect

Snapping ensures that when a user finishes a scroll or fling gesture, the list settles with an item positioned precisely at a specific point, typically the center of the screen. On round screens, where items scale and morph as they move away from the center, snapping is particularly useful to ensure the most relevant item remains fully visible and readable in the optimal viewing area.

<br />

To add a snap-and-fling behavior, set the `flingBehavior` parameter to
`TransformingLazyColumnDefaults.snapFlingBehavior(columnState)`.
Set the `rotaryScrollableBehavior` to match, using
`RotaryScrollableDefaults.snapBehavior(columnState)` for a consistent experience
when using the physical crown or bezel.

```kotlin
val columnState = rememberTransformingLazyColumnState()
ScreenScaffold(scrollState = columnState) { contentPadding ->
    TransformingLazyColumn(
        state = columnState,
        flingBehavior = TransformingLazyColumnDefaults.snapFlingBehavior(columnState),
        rotaryScrollableBehavior = RotaryScrollableDefaults.snapBehavior(columnState)
    ) {
        // ...
        // ...
    }
}
```

## Reverse layout

By default, a scrollable list anchors to its top edge. If a user has scrolled to
the bottom of a standard list and a new item is added to the end, the list
maintains the user's view on the current item. For example, if the user is
viewing item 10 at the bottom of the screen, and item 11 is added, the view
remains focused on item 10, and item 11 appears off-screen below the current
view.

For use cases like messaging applications or live logs, this behavior is usually
not wanted. When new items arrive, users typically want to see the latest
content immediately if they are already at the bottom of the list. If many items
arrive at once, the list should skip to display the very latest item at the
bottom (meaning some intermediate items might not be displayed at all unless the
user scrolls back up).

To support these use cases, `TransformingLazyColumn` lets you reverse the
layout by setting `reverseLayout = true`. This changes the list's anchor from
the top edge to the bottom edge.

For convenience, setting `reverseLayout = true` also reverses the visual order
of the items and the direction of scrolling gestures:

- Items are composed from the bottom to the top, meaning index 0 appears at the bottom of the screen.
- Scrolling up reveals items with higher indexes.

To add a snap-and-fling behavior along with reverse layout, you can combine
`flingBehavior` and `rotaryScrollableBehavior` as shown in the following
snippet:

```kotlin
val columnState = rememberTransformingLazyColumnState()
val transformationSpec = rememberTransformationSpec()
ScreenScaffold(scrollState = columnState) { contentPadding ->
    TransformingLazyColumn(
        state = columnState,
        contentPadding = contentPadding,
        reverseLayout = true,
        modifier = Modifier.fillMaxWidth()
    ) {
        items(10) { index ->
            Button(
                label = {
                    Text(
                        text = "Item ${index + 1}"
                    )
                },
                onClick = {},
                modifier = Modifier
                    .fillMaxWidth()
                    .transformedHeight(this, transformationSpec)
                    .minimumVerticalContentPadding(ButtonDefaults.minimumVerticalListContentPadding),
                transformation = SurfaceTransformation(transformationSpec)
            )
        }
        item {
            // With reverseLayout = true, the last item declared appears at the top.
            ListHeader(
                modifier = Modifier
                    .fillMaxWidth()
                    .transformedHeight(this, transformationSpec)
                    .minimumVerticalContentPadding(ListHeaderDefaults.minimumTopListContentPadding),
                transformation = SurfaceTransformation(transformationSpec)
            ) {
                Text("Header")
            }
        }
    }
}
```

The following images show the difference between a normal list and a reversed
list:
![A TransformingLazyColumn with normal layout, showing Item 1 at the top and items in ascending order.](https://developer.android.com/static/images/wear/compose-tlc-normal.png) **Figure 1.** A standard list layout where content fills from top to bottom. ![A TransformingLazyColumn with reverse layout, showing Item 1 at the bottom and items in descending order towards the top.](https://developer.android.com/static/images/wear/compose-tlc-reverse.png) **Figure 2.** A reversed list layout where content fills from bottom to top.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Compose for Wear OS Codelab](https://developer.android.com/codelabs/compose-for-wear-os/index.lab)
- [Lists and Grids](https://developer.android.com/develop/ui/compose/lists)
- [Using Views in Compose](https://developer.android.com/develop/ui/compose/migrate/interoperability-apis/views-in-compose)