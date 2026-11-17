---
title: https://developer.android.com/develop/ui/compose/animation/advanced
url: https://developer.android.com/develop/ui/compose/animation/advanced
source: md.txt
---

> Documentation index: https://developer.android.com/develop/ui/llms.txt

When you work with touch events and animations, you have more to consider than
when you work with animations alone. First, you might need to interrupt an
ongoing animation when touch events begin, because user interaction should have
the highest priority.

The following example uses an `Animatable` to represent the offset position of
a circle component. Touch events are processed with the
[`pointerInput`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/pointer/package-summary.md.txt#(androidx.compose.ui.Modifier).pointerInput(kotlin.Any,%20kotlin.coroutines.SuspendFunction1)) modifier. When the example detects a new tap
event, it calls `animateTo` to animate the offset value to the tap position. A
tap event can happen during the animation too, and in that case, `animateTo`
interrupts the ongoing animation and starts the animation to the new target
position while maintaining the velocity of the interrupted animation.


```kotlin
@Composable
fun Gesture() {
    val offset = remember { Animatable(Offset(0f, 0f), Offset.VectorConverter) }
    Box(
        modifier = Modifier
            .fillMaxSize()
            .pointerInput(Unit) {
                coroutineScope {
                    while (true) {
                        // Detect a tap event and obtain its position.
                        awaitPointerEventScope {
                            val position = awaitFirstDown().position

                            launch {
                                // Animate to the tap position.
                                offset.animateTo(position)
                            }
                        }
                    }
                }
            }
    ) {
        Circle(modifier = Modifier.offset { offset.value.toIntOffset() })
    }
}

private fun Offset.toIntOffset() = IntOffset(x.roundToInt(), y.roundToInt())
```

<br />

Another frequent pattern is synchronizing animation values with values coming
from touch events, such as drag. The following example implements "swipe to
dismiss" as a modifier, rather than using the
[`SwipeToDismissBox`](https://developer.android.com/reference/kotlin/androidx/compose/material3/SwipeToDismissBox.composable.md.txt) composable. The horizontal offset
of the element is represented as an `Animatable`. This API has a characteristic
useful in gesture animation. Its value can be changed by touch events as well
as the animation. On a touch down event, the modifier stops the `Animatable`
with the `stop` method so that any ongoing animation is intercepted.

During a drag event, the modifier uses `snapTo` to update the `Animatable`
value with the value calculated from touch events. For fling, Compose provides
`VelocityTracker` to record drag events and calculate velocity. The velocity
can be fed directly to `animateDecay` for the fling animation. To slide the
offset value back to the original position, the modifier specifies the target
offset value of `0f` with the `animateTo` method.


```kotlin
fun Modifier.swipeToDismiss(
    onDismissed: () -> Unit
): Modifier = composed {
    val offsetX = remember { Animatable(0f) }
    pointerInput(Unit) {
        // Used to calculate fling decay.
        val decay = splineBasedDecay<Float>(this)
        // Use suspend functions for touch events and the Animatable.
        coroutineScope {
            while (true) {
                val velocityTracker = VelocityTracker()
                // Stop any ongoing animation.
                offsetX.stop()
                awaitPointerEventScope {
                    // Detect a touch down event.
                    val pointerId = awaitFirstDown().id

                    horizontalDrag(pointerId) { change ->
                        // Update the animation value with touch events.
                        launch {
                            offsetX.snapTo(
                                offsetX.value + change.positionChange().x
                            )
                        }
                        velocityTracker.addPosition(
                            change.uptimeMillis,
                            change.position
                        )
                    }
                }
                // No longer receiving touch events. Prepare the animation.
                val velocity = velocityTracker.calculateVelocity().x
                val targetOffsetX = decay.calculateTargetValue(
                    offsetX.value,
                    velocity
                )
                // The animation stops when it reaches the bounds.
                offsetX.updateBounds(
                    lowerBound = -size.width.toFloat(),
                    upperBound = size.width.toFloat()
                )
                launch {
                    if (targetOffsetX.absoluteValue <= size.width) {
                        // Not enough velocity; Slide back.
                        offsetX.animateTo(
                            targetValue = 0f,
                            initialVelocity = velocity
                        )
                    } else {
                        // The element was swiped away.
                        offsetX.animateDecay(velocity, decay)
                        onDismissed()
                    }
                }
            }
        }
    }
        .offset { IntOffset(offsetX.value.roundToInt(), 0) }
}
```

<br />

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Value-based animations](https://developer.android.com/develop/ui/compose/animation/value-based.md.txt)
- [Drag, swipe, and fling](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/drag-swipe-fling)
- [Understand gestures](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/understand-gestures.md.txt)