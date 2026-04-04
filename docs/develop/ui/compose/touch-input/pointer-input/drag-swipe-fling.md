---
title: Drag, swipe, and fling  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/touch-input/pointer-input/drag-swipe-fling
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Drag, swipe, and fling Stay organized with collections Save and categorize content based on your preferences.




The
[`draggable`](/reference/kotlin/androidx/compose/foundation/gestures/draggable.modifier#(androidx.compose.ui.Modifier).draggable(androidx.compose.foundation.gestures.DraggableState,androidx.compose.foundation.gestures.Orientation,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Boolean,kotlin.coroutines.SuspendFunction2,kotlin.coroutines.SuspendFunction2,kotlin.Boolean))
modifier is the high-level entry point to drag gestures in a single orientation,
and reports the drag distance in pixels.

It's important to note that this modifier is similar to `scrollable`, in that it
only detects the gesture. You need to hold the state and represent it on screen
by, for example, moving the element via the
[`offset`](/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.ui.Modifier).offset(androidx.compose.ui.unit.Dp,%20androidx.compose.ui.unit.Dp))
modifier:

```
@Composable
private fun DraggableText() {
    var offsetX by remember { mutableFloatStateOf(0f) }
    Text(
        modifier = Modifier
            .offset { IntOffset(offsetX.roundToInt(), 0) }
            .draggable(
                orientation = Orientation.Horizontal,
                state = rememberDraggableState { delta ->
                    offsetX += delta
                }
            ),
        text = "Drag me!"
    )
}

GesturesSnippets.kt
```

If you need to control the whole dragging gesture, consider using the drag
gesture detector instead, via the
[`pointerInput`](/reference/kotlin/androidx/compose/ui/input/pointer/package-summary#(androidx.compose.ui.Modifier).pointerInput(kotlin.Any,kotlin.coroutines.SuspendFunction1))
modifier.

```
@Composable
private fun DraggableTextLowLevel() {
    Box(modifier = Modifier.fillMaxSize()) {
        var offsetX by remember { mutableFloatStateOf(0f) }
        var offsetY by remember { mutableFloatStateOf(0f) }

        Box(
            Modifier
                .offset { IntOffset(offsetX.roundToInt(), offsetY.roundToInt()) }
                .background(Color.Blue)
                .size(50.dp)
                .pointerInput(Unit) {
                    detectDragGestures { change, dragAmount ->
                        change.consume()
                        offsetX += dragAmount.x
                        offsetY += dragAmount.y
                    }
                }
        )
    }
}

GesturesSnippets.kt
```

![A UI element being dragged by a finger press](/static/develop/ui/compose/images/gestures-drag.gif)

## Swiping

The
[`swipeable`](/reference/kotlin/androidx/compose/material/swipeable.modifier#(androidx.compose.ui.Modifier).swipeable(androidx.compose.material.SwipeableState,kotlin.collections.Map,androidx.compose.foundation.gestures.Orientation,kotlin.Boolean,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function2,androidx.compose.material.ResistanceConfig,androidx.compose.ui.unit.Dp))
modifier lets you drag elements which, when released, animate towards typically
two or more anchor points defined in an orientation. A common usage for this is
to implement a ‘swipe-to-dismiss’ pattern.

**Caution:** The [`swipeable`](/reference/kotlin/androidx/compose/material/swipeable.modifier#(androidx.compose.ui.Modifier).swipeable(androidx.compose.material.SwipeableState,kotlin.collections.Map,androidx.compose.foundation.gestures.Orientation,kotlin.Boolean,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function2,androidx.compose.material.ResistanceConfig,androidx.compose.ui.unit.Dp)) APIs have been replaced by
Foundation's [`anchoredDraggable`](/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.Modifier).anchoredDraggable(androidx.compose.foundation.gestures.AnchoredDraggableState,androidx.compose.foundation.gestures.Orientation,kotlin.Boolean,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource)) APIs in Jetpack Compose 1.6.0-alpha01.

It's important to note that this modifier does not move the element, it only
detects the gesture. You need to hold the state and represent it on screen by,
for example, moving the element via the
[`offset`](/reference/kotlin/androidx/compose/foundation/layout/offset.modifier#(androidx.compose.ui.Modifier).offset(androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp))
modifier.

The swipeable state is required in the `swipeable` modifier, and can be created
and remembered with
[`rememberSwipeableState()`](/reference/kotlin/androidx/compose/material/rememberSwipeableState.composable#rememberSwipeableState(kotlin.Any,androidx.compose.animation.core.AnimationSpec,kotlin.Function1)).
This state also provides a set of useful methods to programmatically animate to
anchors (see
[`snapTo`](/reference/kotlin/androidx/compose/material/SwipeableState#snapTo(kotlin.Any)),
[`animateTo`](/reference/kotlin/androidx/compose/material/SwipeableState#animateTo(kotlin.Any,androidx.compose.animation.core.AnimationSpec)),
[`performFling`](/reference/kotlin/androidx/compose/material/SwipeableState#performFling(kotlin.Float)),
and
[`performDrag`](/reference/kotlin/androidx/compose/material/SwipeableState#performDrag(kotlin.Float)))
as well as properties to observe the dragging progress.

The swipe gesture can be configured to have different threshold types, such as
[`FixedThreshold(Dp)`](/reference/kotlin/androidx/compose/material/FixedThreshold#FixedThreshold(androidx.compose.ui.unit.Dp))
and
[`FractionalThreshold(Float)`](/reference/kotlin/androidx/compose/material/FractionalThreshold#FractionalThreshold(kotlin.Float)),
and they can be different for each anchor point from-to combination.

For more flexibility, you can configure the `resistance` when swiping past the
bounds and, also, the `velocityThreshold` which will animate a swipe to the
next state, even if the positional `thresholds`have not been reached.

```
@OptIn(ExperimentalMaterialApi::class)
@Composable
private fun SwipeableSample() {
    val width = 96.dp
    val squareSize = 48.dp

    val swipeableState = rememberSwipeableState(0)
    val sizePx = with(LocalDensity.current) { squareSize.toPx() }
    val anchors = mapOf(0f to 0, sizePx to 1) // Maps anchor points (in px) to states

    Box(
        modifier = Modifier
            .width(width)
            .swipeable(
                state = swipeableState,
                anchors = anchors,
                thresholds = { _, _ -> FractionalThreshold(0.3f) },
                orientation = Orientation.Horizontal
            )
            .background(Color.LightGray)
    ) {
        Box(
            Modifier
                .offset { IntOffset(swipeableState.offset.value.roundToInt(), 0) }
                .size(squareSize)
                .background(Color.DarkGray)
        )
    }
}

GesturesSnippets.kt
```

![A UI element responding to a swipe gesture](/static/develop/ui/compose/images/gestures-swipe.gif)

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Understand gestures](/develop/ui/compose/touch-input/pointer-input/understand-gestures)
* [Advanced animation example: Gestures {:#gesture-and-animation}](/develop/ui/compose/animation/advanced)
* [Value-based animations](/develop/ui/compose/animation/value-based)

[Previous

arrow\_back

Tap and press](/develop/ui/compose/touch-input/pointer-input/tap-and-press)

[Next

Multi-touch gestures

arrow\_forward](/develop/ui/compose/touch-input/pointer-input/multi-touch)