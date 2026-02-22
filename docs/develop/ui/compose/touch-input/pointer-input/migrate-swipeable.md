---
title: https://developer.android.com/develop/ui/compose/touch-input/pointer-input/migrate-swipeable
url: https://developer.android.com/develop/ui/compose/touch-input/pointer-input/migrate-swipeable
source: md.txt
---

| **Warning:** This page and the snippets it contains are outdated.

[`Swipeable`](https://developer.android.com/reference/kotlin/androidx/compose/material/SwipeableState) is a Compose Material API that helps you build components that
can be swiped between discrete states, such as bottom sheets, drawers, or
swipe-to-dismiss. To better support advanced use cases, such as anchors that
depend on the size of a component, a successor was published in
Compose-Foundation 1.6.0-alpha01: [`AnchoredDraggable`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/AnchoredDraggableState). `AnchoredDraggable`
is a Foundation API for building draggable components with anchored states, such
as bottom sheets, drawers, or swipe-to-dismiss.

Material's `Swipeable` APIs have been deprecated in favor of Foundation's
`AnchoredDraggable` and will be removed in a future release. This guide
describes how to migrate from `Swipeable` APIs to `AnchoredDraggable`.
| **Note:** `AnchoredDraggable` is an experimental API. Experimental APIs may change in future.

## Migrate `SwipeableState` to `AnchoredDraggableState`

Start by identifying changes to your state holder. `AnchoredDraggableState`
cannot be inherited from, and the offset is represented as `Float.NaN` before it
is initialized.

### Update your state holder

[`AnchoredDraggableState`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/AnchoredDraggableState) is a final class, meaning it cannot be inherited
from. If your existing component inherits from [`SwipeableState`](https://developer.android.com/reference/kotlin/androidx/compose/material/SwipeableState), update
your state holder to hold a reference to the `AnchoredDraggableState` instead of
inheriting from it:

### Swipeable

    class MySwitchState: SwipeableState()

### AnchoredDraggable

    class MySwitchState {
        private val anchoredDraggableState = AnchoredDraggableState(...)
    }

Since your state holder does not inherit from `SwipeableState` anymore, you
might have to expose APIs yourself. The most common APIs you can use are
[`offset`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/AnchoredDraggableState#offset()), [`progress`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/AnchoredDraggableState#progress()), [`currentValue`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/AnchoredDraggableState#currentValue()) and [`targetValue`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/AnchoredDraggableState#targetValue()).

### Access the offset

Unlike in `Swipeable`, `AnchoredDraggableState`'s `offset` is `Float.NaN` before
it is initialized. In `AnchoredDraggable`, the anchors can be passed to
`AnchoredDraggableState`'s constructor or updated through
[`AnchoredDraggableState#updateAnchors`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/AnchoredDraggableState#updateAnchors(androidx.compose.foundation.gestures.DraggableAnchors,kotlin.Any)). Passing the anchors to
`AnchoredDraggableState`'s constructor initializes the offset immediately.

If your anchors depend on layout or could change, use
`AnchoredDraggableState#updateAnchors` to avoid recreating the state when the
anchors change.

If you use `updateAnchors`, the offset will be `Float.NaN` before passing the
anchors to `updateAnchors`. To avoid accidentally passing `Float.NaN` to
components, use [`AnchoredDraggableState#requireOffset`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/AnchoredDraggableState#requireOffset()) to require that the
offset has been initialized when reading it. This helps you catch
inconsistencies or possible bugs early on.

    @Composable
    fun AnchoredDraggableBox() {
        val state = remember { AnchoredDraggableState(...) }
        val density = LocalDensity.current
        val anchors = remember { DraggableAnchors { ... } }
        SideEffect {
            state.updateAnchors(anchors)
        }
        Box(
            Modifier.offset { IntOffset(x = state.requireOffset(), y = 0) }
        }
    }

| **Note:** Overflow support for `AnchoredDraggable` is currently being implemented. See [b/288084801](https://issuetracker.google.com/288084801) for the latest status.

## Migrate `Modifier.swipeable` to `Modifier.anchoredDraggable`

[`Modifier.anchoredDraggable()`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.Modifier).anchoredDraggable(androidx.compose.foundation.gestures.AnchoredDraggableState,androidx.compose.foundation.gestures.Orientation,kotlin.Boolean,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource)) replaces [`Modifier.swipeable`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#(androidx.compose.ui.Modifier).swipeable(androidx.compose.material.SwipeableState,kotlin.collections.Map,androidx.compose.foundation.gestures.Orientation,kotlin.Boolean,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function2,androidx.compose.material.ResistanceConfig,androidx.compose.ui.unit.Dp))(). Some
of `Modifier.swipeable()`'s parameters have moved to `AnchoredDraggableState`
directly, as described in the following sections.

### Define anchors

Define the anchors using the [`DraggableAnchors`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/DraggableAnchors) builder method. Then, pass
them to `AnchoredDraggableState#updateAnchors` or `AnchoredDraggableState`'s
constructor:

### Constructor

    enum class DragValue { Start, Center, End }

    @Composable
    fun AnchoredDraggableBox() {
        val anchors = DraggableAnchors {
            Start at -100.dp.toPx()
            Center at 0f
            End at 100.dp.toPx()
        }
        val state = remember {
            AnchoredDraggableState(anchors = anchors)
        }
        Box(
            Modifier.offset { IntOffset(x = state.requireOffset(), y = 0) }
        )
    }

### updateAnchors

    enum class DragValue { Start, Center, End }

    @Composable
    fun AnchoredDraggableBox() {
        val state = remember { AnchoredDraggableState(...) }
        val density = LocalDensity.current
        val anchors = with (density) {
            DraggableAnchors {
                Start at -100.dp.toPx()
                Center at 0f
                End at 100.dp.toPx()
            }
        }
        SideEffect {
            state.updateAnchors(anchors)
        }
        Box(
            Modifier.offset { IntOffset(x = state.requireOffset(), y = 0) }
        )
    }

If the anchors are static, pass them to the constructor. If they depend on
layout, or are not static, use `updateAnchors`.

### Define positional thresholds

The type and name of the thresholds parameter has changed. Instead of having a
separate [`ThresholdConfig`](https://developer.android.com/reference/kotlin/androidx/compose/material/ThresholdConfig) interface, `AnchoredDraggableState` has a
`positionalThreshold` parameter that takes a lambda function that returns the
position of the threshold. For example, a positional threshold of 50% could be
expressed as:

    val anchoredDraggableState = AnchoredDraggableState(
        positionalThreshold = { distance -> distance * 0.5f },
        ...
    )

A positional threshold of `56dp` could be expressed as:

    val density = LocalDensity.current
    val anchoredDraggableState = AnchoredDraggableState(
        positionalThreshold = { with(density) { 56.dp.toPx() } },
        ...
    )

### Define velocity thresholds

Velocity thresholds are also passed to `AnchoredDraggableState`'s constructor,
and also expressed as a lambda:

    val density = LocalDensity.current
    val anchoredDraggableState = AnchoredDraggableState(
        velocityThreshold = { with(density) { 125.dp.toPx() } },
        ...
    )

## Changes to the API surface

Find an overview of changes to the API surface below.

### `AnchoredDraggableState`

| `SwipeableState` | `AnchoredDraggableState` |
|---|---|
| `open class SwipeableState(initialValue: T, animationSpec: AnimationSpec = ..., confirmStateChange: (T) -> Boolean = ...)` | `class AnchoredDraggableState( initialValue: T, animationSpec: AnimationSpec = ..., confirmValueChange: (T) -> Boolean = ..., positionalThreshold: Density.(Float) -> Float = ..., velocityThreshold: Dp = ...)` |
| `offset: State` | `offset: Float requireOffset()` |
| `progress: SwipeProgress` | `progress: Float [0f..1f`\] |
| `currentValue: T` | `currentValue: T` |
| `targetValue: T` | `targetValue: T` |
| `direction: Float [-1f, 0f, 1f`\] | N/A |
| `suspend animateTo( targetValue: T, anim: AnimationSpec = ...)` | `suspend animateTo( targetState: T, velocity: Float = lastVelocity)` |
| `suspend snapTo(targetValue: T)` | `suspend snapTo(targetValue: T)` |
| `performDrag(delta: Float)` | `dispatchRawDelta(delta: Float)` |
| `suspend performFling(velocity: Float)` | `suspend settle(velocity: Float)` |
| `isAnimationRunning: Boolean` | `isAnimationRunning: Boolean` |
|   | `lastVelocity: Float` |

### `Modifier.anchoredDraggable`

| `Modifier.swipeable` | `Modifier.anchoredDraggable` |
|---|---|
| `state: SwipeableState` | `state: AnchoredDraggableState` |
| `anchors: Map` | `AnchoredDraggableState#updateAnchors or` `AnchoredDraggableState#constructor` |
| `orientation: Orientation` | `orientation: Orientation` |
| `enabled: Boolean = true` | `enabled: Boolean = true` |
| `reverseDirection: Boolean = false` | `reverseDirection: Boolean = false` |
| `interactionSource: MutableInteractionSource? = null` | `interactionSource: MutableInteractionSource? = null` |
| `thresholds: (from: T, to: T) -> ThresholdConfig = FixedThreshold(56.dp)` | Passed to `AnchoredDraggableState` constructor as `positionalThreshold` |
| `resistance: ResistanceConfig? = ...` | Not yet supported. See [b/288084801](https://issuetracker.google.com/288084801) for the latest status. |
| `velocityThreshold: Dp = 125.dp` | Passed to `AnchoredDraggable` constructor |