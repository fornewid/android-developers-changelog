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

If you need to add a snap-and-fling behavior, set the `flingBehavior` parameter to `TransformingLazyColumnDefaults.snapFlingBehavior(columnState)`, as shown in the following code snippet:

```kotlin
val columnState = rememberTransformingLazyColumnState()
ScreenScaffold(scrollState = columnState) {
    TransformingLazyColumn(
        state = columnState,
        flingBehavior = TransformingLazyColumnDefaults.snapFlingBehavior(columnState)
    ) {
        // ...
        // ...
    }
}
```

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Compose for Wear OS Codelab](https://developer.android.com/codelabs/compose-for-wear-os)
- [Lists and Grids](https://developer.android.com/develop/ui/compose/lists)
- [Using Views in Compose](https://developer.android.com/develop/ui/compose/migrate/interoperability-apis/views-in-compose)