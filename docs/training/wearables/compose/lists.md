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

In order to add a scaling and scrolling effect, use `Modifier.transformedHeight`
to allow Compose to calculate the height change as the item scrolls through the
screen and `transformation = SurfaceTransformation(transformationSpec)` to apply
the visual effects, including scaling down the item visually to match the
previous.
Use a custom [`TransformationSpec`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/lazy/TransformationSpec) for components which don't take
`transformation` as a parameter, for example `Text`.


The following animation shows how a list element scales and changes shape
when approaching the top and bottom of the screen:

The following code snippet shows how to create a list using [`TransformingLazyColumn`](https://developer.android.com/reference/kotlin/androidx/wear/compose/foundation/lazy/package-summary#TransformingLazyColumn(androidx.compose.ui.Modifier,androidx.wear.compose.foundation.lazy.TransformingLazyColumnState,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.wear.compose.foundation.rotary.RotaryScrollableBehavior,androidx.compose.foundation.OverscrollEffect,kotlin.Function1)) layout to create content that [looks great on a variety of Wear OS screen sizes](https://developer.android.com/training/wearables/compose/screen-size), for example in the following sample code, it will add the necessary padding to the first and last elements of the list which are set in the `contentPadding` of the `TransformingLazyColumn`. In order for the scroll indicator to be shown, share the `columnState` between the `ScreenScaffold` and the `TransformingLazyColumn`:

<br />

```kotlin
val columnState = rememberTransformingLazyColumnState()
val contentPadding = rememberResponsiveColumnPadding(
    first = ColumnItemType.ListHeader,
    last = ColumnItemType.Button,
)
val transformationSpec = rememberTransformationSpec()
ScreenScaffold(
    scrollState = columnState,
    contentPadding = contentPadding
) { contentPadding ->
    TransformingLazyColumn(
        state = columnState,
        contentPadding = contentPadding
    ) {
        item {
            ListHeader(
                modifier = Modifier.fillMaxWidth().transformedHeight(this, transformationSpec),
                transformation = SurfaceTransformation(transformationSpec)
            ) {
                Text(text = "Header")
            }
        }
        // ... other items
        item {
            Button(
                modifier = Modifier.fillMaxWidth().transformedHeight(this, transformationSpec),
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

If you need to add a snap-and-fling behavior, we suggest to use `ScalingLazyColumn`. This effect helps users more precisely navigate through the items in a list while also helping them move more quickly through a long list.

To add this effect to the Horologist's version of the [`ScalingLazyColumn`](https://google.github.io/horologist/compose-layout/),
set the `rotaryMode` parameter of `columnState` to
[`RotaryWithSnap`](https://google.github.io/horologist/api/compose-layout/com.google.android.horologist.compose.rotaryinput/rotary-with-snap.html), as shown in the following code snippet:

```kotlin
val columnState = rememberResponsiveColumnState(
    // ...
    // ...
    rotaryMode = ScalingLazyColumnState.RotaryMode.Snap
)
ScreenScaffold(scrollState = columnState) {
    ScalingLazyColumn(
        columnState = columnState
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