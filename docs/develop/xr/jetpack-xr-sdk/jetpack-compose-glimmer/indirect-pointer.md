---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/indirect-pointer
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/indirect-pointer
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) Audio \&  
Display Glasses [](https://developer.android.com/develop/xr/devices#audio-display) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

The [`onIndirectPointerGesture`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/onIndirectPointerGesture.modifier) modifier lets component receive and respond
to high-level indirect pointer events, such as those originating from a device's
touchpad. Use this modifier to capture and process gestures that come from a
touchpad or similar source.

## API surface

There are four callbacks that your app can use to control handling:

- `onClick`: Triggered on a successful tap or click without significant horizontal movement.
- `onSwipeForward`: Triggered when a horizontal swipe exceeds the distance and velocity threshold in the forward direction.
- `onSwipeBackward`: Triggered when a horizontal swipe exceeds the distance and velocity threshold in the backward direction.
- `Enabled`: When set to `false`, the modifier is ignored and no callbacks are invoked.

## System behavior for swiping and scrolling

The system uses a touch slop threshold to differentiate between a click and a
swipe.

- If the pointer moves significantly during a down state, `onClick` is cancelled.
- If the pointer backtracks significantly during a movement, the swipe gesture is invalidated.

## Example: Set up handling for swipes and clicks on a component

The following code sets up handling for swipes and clicks on a focusable `Box`:


```kotlin
@Composable
@Sampled
fun OnIndirectPointerGestureSample() {
    Box(
        modifier =
            Modifier.fillMaxSize()
                .onIndirectPointerGesture(
                    enabled = true,
                    onSwipeForward = { /* onSwipeForward */ },
                    onSwipeBackward = { /* onSwipeBackward */ },
                    onClick = { /* onClick */ },
                )
                .focusTarget()
    ) {
        // App()
    }
}
```

<br />

### Key points about the code

- `onIndirectPointerGesture` requires focus, so the [`focusTarget`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/focusTarget.modifier) is also applied to make the `Box` focusable. You can use `focusTarget` or another focus-enabling modifier such as [`surface`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/surface.composable#(androidx.compose.ui.Modifier).surface(kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.xr.glimmer.SurfaceDepthEffect,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.interaction.MutableInteractionSource)). Without focus, the modifier can't act upon indirect pointer events.
- This example implements both the `onSwipeForward` and `onClick` callbacks, so swipe and click gestures that are detected are intercepted and consumed, and don't reach outwards to parent containers. However, you can also leave a specific callback null to pass through a gesture to an `onIndirectPointerGesture` modifier in a parent container. -