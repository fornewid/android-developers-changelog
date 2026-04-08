---
title: Multitouch: Panning, zooming, rotating  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/touch-input/pointer-input/multi-touch
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Multitouch: Panning, zooming, rotating Stay organized with collections Save and categorize content based on your preferences.




To detect multitouch gestures used for panning, zooming and rotating, you can
use the `transformable` modifier. This modifier does not transform elements by
itself, it only detects the gestures.

```
@Composable
private fun TransformableSample() {
    // set up all transformation states
    var scale by remember { mutableFloatStateOf(1f) }
    var rotation by remember { mutableFloatStateOf(0f) }
    var offset by remember { mutableStateOf(Offset.Zero) }
    val state = rememberTransformableState { zoomChange, offsetChange, rotationChange ->
        scale *= zoomChange
        rotation += rotationChange
        offset += offsetChange
    }
    Box(
        Modifier
            // apply other transformations like rotation and zoom
            // on the pizza slice emoji
            .graphicsLayer(
                scaleX = scale,
                scaleY = scale,
                rotationZ = rotation,
                translationX = offset.x,
                translationY = offset.y
            )
            // add transformable to listen to multitouch transformation events
            // after offset
            .transformable(state = state)
            .background(Color.Blue)
            .fillMaxSize()
    )
}

GesturesSnippets.kt
```

![A UI element responding to multitouch gestures—panning, zooming, and rotating](/static/develop/ui/compose/images/gestures-multitouch.gif)

If you need to combine zooming, panning and rotation with other gestures, you
can use the
[`PointerInputScope.detectTransformGestures`](/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.PointerInputScope).detectTransformGestures(kotlin.Boolean,kotlin.Function4))
detector.

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Understand gestures](/develop/ui/compose/touch-input/pointer-input/understand-gestures)

[Previous

arrow\_back

Drag, swipe, and fling](/develop/ui/compose/touch-input/pointer-input/drag-swipe-fling)