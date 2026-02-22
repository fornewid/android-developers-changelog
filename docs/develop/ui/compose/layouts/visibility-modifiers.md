---
title: https://developer.android.com/develop/ui/compose/layouts/visibility-modifiers
url: https://developer.android.com/develop/ui/compose/layouts/visibility-modifiers
source: md.txt
---

Tracking when a UI element is visible on-screen is helpful for a variety of
use cases, such as logging analytics, managing UI state, and optimizing
resources by automatically playing or pausing video content. Compose offers
several modifiers for tracking UI element visibility such as:

- [`onVisibilityChanged`](https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/package-summary#(androidx.compose.ui.Modifier).onVisibilityChanged(kotlin.Long,kotlin.Float,androidx.compose.ui.layout.LayoutBoundsHolder,kotlin.Function1)) - This modifier notifies you when the visibility of a composable changes. It's ideal for triggering an action or side effect every time the composable becomes visible.
- [`onLayoutRectChanged`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).onLayoutRectChanged(kotlin.Long,kotlin.Long,kotlin.Function1)) - This modifier provides information about a composable's bounds relative to the root, window, and screen. It offers low-level control and is the foundation API for `onVisibilityChanged`. The modifier is similar to [`onGloballyPositioned`](https://developer.android.com/reference/kotlin/androidx/compose/ui/layout/OnGloballyPositionedModifier#onGloballyPositioned(androidx.compose.ui.layout.LayoutCoordinates)), but offers better performance and increased flexibility.

You can use these APIs with any composable as part of the modifier chain.

## Track visibility changes with `onVisibilityChanged`

Understanding when an item is visible or partially visible to a user can
help you track analytics (for example, viewer count), optimize performance
(fetching or prefetching data from the network only when the item is visible),
or even trigger events (playing or pausing videos).

To be notified when an item's visibility changes, use the
`onVisibilityChanged` modifier, as shown in the following example:


```kotlin
Text(
    text = "Some text",
    modifier = Modifier
        .onVisibilityChanged { visible ->
            if (visible) {
                // Do something if visible
            } else {
                // Do something if not visible
            }
        }
        .padding(vertical = 8.dp)
)
```

<br />

The `onVisibilityChanged` modifier provides a boolean value that reflects the
current visibility state of the composable. Additionally, it offers
parameters such as `minFraction` and `minDurationMs`, which give you
finer control over when the visibility callback needs to be triggered.

Like every other modifier, sequencing matters with the `onVisibilityChanged`
modifier. The preceding example shows a composable function that renders text
with padding. To make sure that the modifier affects the entire composable along
with the padding, add the `onVisibilityChanged` modifier before the `padding`
modifier.

### Set a time limit on a composable before triggering visibility callback

In some situations, you might want to trigger an action only after an item has
been visible to the user for a certain amount of time. For example, you can
autoplay a video if it's been visible to the user for some time.

To trigger an action after an item is visible for a defined period, use the
`minDurationMs` parameter in the `onVisibilityChanged` modifier. This parameter
specifies the minimum amount of time a composable needs to be continuously
visible for the callback to be triggered. If the composable stops being visible
before the duration is met, the timer is reset. The default value is **0
milliseconds**.

The following snippet changes the background to purple after the composable
has been visible to the user for 3 seconds:


```kotlin
var background by remember { mutableStateOf(PalePink) }
Card(
    modifier = modifier
        // ...
        .onVisibilityChanged(minDurationMs = 3000) {
            if (it) {
                background = MutedPlum
            }
        }
) {

    Box(
        modifier = Modifier
            // ...
            .background(background),
        contentAlignment = Alignment.Center,
    ) {
        // ...
    }
}
```

<br />

**Figure 1.** The background changes from pink to plum after the composable has been on screen for 3 seconds continuously.

### Set a minimum visible fraction

Setting a minimum visible fraction for the composable's visibility callback is
useful when working with scrollable content (for example, `LazyColumn`) to
optimize data fetching for items that exceed the screen size.

In such cases, use the `minFractionVisible` parameter in the
`onVisibilityChanged` modifier to define the fraction that needs to be on screen
for the composable to be marked as visible.
It supports float values ranging from `0.0f` to `1.0f`, and is set as `1.0f` by
default.
`1.0f` means the composable needs to be completely visible on screen for the
callback to be triggered.


```kotlin
LazyColumn(
    modifier = modifier.fillMaxSize()
) {
    item {
        Box(
            modifier = Modifier
                // ...
                // Here the visible callback gets triggered when 20% of the composable is visible
                .onVisibilityChanged(
                    minFractionVisible = 0.2f,
                ) { visible ->
                    if (visible) {
                        // Call specific logic here
                        // viewModel.fetchDataFromNetwork()
                    }
                }
                .padding(vertical = 16.dp)
        ) {
            Text(
                text = "Sample Text",
                modifier = Modifier.padding(horizontal = 16.dp)
            )
        }
    }
}
```

<br />

|---|---|
|   |   |
| **Figure 2.** Without `minFractionVisible` being set. | **Figure 3.** With `minFractionVisible` set as **0.2f**. |

The example used earlier preloads the Androidify Bots from the network before
the composable is completely visible. In Figure 2, the third bot doesn't load,
as the composable isn't completely visible. In Figure 3, `minFractionVisible` is
set, and the third bot loads before it is completely visible on screen.

> [!NOTE]
> **Note:** The preceding videos have been intentionally slowed down for clarity.