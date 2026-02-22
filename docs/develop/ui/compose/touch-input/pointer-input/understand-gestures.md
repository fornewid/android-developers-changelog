---
title: https://developer.android.com/develop/ui/compose/touch-input/pointer-input/understand-gestures
url: https://developer.android.com/develop/ui/compose/touch-input/pointer-input/understand-gestures
source: md.txt
---

[Video](https://www.youtube.com/watch?v=1tkVjBxdGrk)

There are several terms and concepts that are important to understand
when working on gesture handling in an application. This page explains the terms
pointers, pointer events, and gestures, and introduces the different abstraction
levels for gestures. It also dives deeper into event consumption and
propagation.

## Definitions

To understand the various concepts on this page, you need to understand some
of the terminology used:

- **Pointer** : A physical object you can use to interact with your application. For mobile devices, the most common pointer is your finger interacting with the touchscreen. Alternatively, you could use a stylus to replace your finger. For large screens, you can use a mouse or trackpad to indirectly interact with the display. An input device must be able to "point" at a coordinate to be considered a pointer, so a keyboard, for example, cannot be considered a pointer. In Compose, the pointer type is included in pointer changes using [`PointerType`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/pointer/PointerType).
- **Pointer event** : Describes a low-level interaction of one or more pointers with the application at a given time. Any pointer interaction, such as putting a finger on the screen or dragging a mouse, would trigger an event. In Compose, all relevant information for such an event is contained in the [`PointerEvent`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/pointer/PointerEvent) class.
- **Gesture**: A sequence of pointer events that can be interpreted as a single action. For example, a tap gesture can be considered a sequence of a down event followed by an up event. There are common gestures that are used by many apps, such as tap, drag, or transform, but you can also create your own custom gesture when needed.

## Different levels of abstraction

Jetpack Compose provides different levels of abstraction for handling gestures.
On the top level is *component support* . Composables like [`Button`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Button(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1))
automatically include gesture support. To add gesture support to custom
components, you can add *gesture modifiers* like [`clickable`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).clickable(androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.foundation.Indication,kotlin.Boolean,kotlin.String,androidx.compose.ui.semantics.Role,kotlin.Function0)) to arbitrary
composables. Finally, if you need a custom gesture, you can use the
[`pointerInput`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/pointer/package-summary#(androidx.compose.ui.Modifier).pointerInput(kotlin.Any,kotlin.Any,kotlin.coroutines.SuspendFunction1)) modifier.

As a rule, build on the highest level of abstraction that offers the
functionality you need. This way, you benefit from the best practices included
in the layer. For example, `Button` contains more semantic information, used for
accessibility, than `clickable`, which contains more information than a raw
`pointerInput` implementation.

> [!NOTE]
> **Note:** Choosing the right level of abstraction is a common theme in Compose. Read more in the documentation on [architectural layering](https://developer.android.com/develop/ui/compose/layering).

### Component support

Many out-of-the-box components in Compose include some sort of internal gesture
handling. For example, a [`LazyColumn`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/package-summary#LazyColumn(androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.LazyListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,kotlin.Function1)) responds to drag gestures by
scrolling its content, a [`Button`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Button(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) shows a ripple when you press down on it,
and the [`SwipeToDismiss`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#SwipeToDismiss(androidx.compose.material3.DismissState,kotlin.Function1,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.collections.Set)) component contains swiping logic to dismiss an
element. This type of gesture handling works automatically.

Next to internal gesture handling, many components also require the caller to
handle the gesture. For example, a [`Button`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Button(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) automatically detects taps
and triggers a click event. You pass an `onClick` lambda to the `Button` to
react to the gesture. Similarly, you add an `onValueChange` lambda to a
[`Slider`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Slider(kotlin.Float,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.ranges.ClosedFloatingPointRange,kotlin.Int,kotlin.Function0,androidx.compose.material3.SliderColors,androidx.compose.foundation.interaction.MutableInteractionSource)) to react to the user dragging the slider handle.

When it fits your use case, prefer gestures included in components, as they
include out-of-the-box support for focus and accessibility, and they are
well-tested. For example, a `Button` is marked in a special way so that
accessibility services correctly describe it as a button, instead of just any
clickable element:


```kotlin
// Talkback: "Click me!, Button, double tap to activate"
Button(onClick = { /* TODO */ }) { Text("Click me!") }
// Talkback: "Click me!, double tap to activate"
Box(Modifier.clickable { /* TODO */ }) { Text("Click me!") }
```

<br />

To learn more about accessibility in Compose, see [Accessibility in
Compose](https://developer.android.com/develop/ui/compose/accessibility).

### Add specific gestures to arbitrary composables with modifiers

You can apply gesture modifiers to any arbitrary composable to make the
composable listen to gestures. For example, you can let a generic [`Box`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#Box(androidx.compose.ui.Modifier))
handle tap gestures by making it [`clickable`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).clickable(androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.foundation.Indication,kotlin.Boolean,kotlin.String,androidx.compose.ui.semantics.Role,kotlin.Function0)), or let a [`Column`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#Column(androidx.compose.ui.Modifier,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,kotlin.Function1))
handle vertical scroll by applying [`verticalScroll`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).verticalScroll(androidx.compose.foundation.ScrollState,kotlin.Boolean,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean)).

There are many modifiers to handle different types of gestures:

- [Handle taps and presses](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/tap-and-press) with the [`clickable`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).clickable(androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.foundation.Indication,kotlin.Boolean,kotlin.String,androidx.compose.ui.semantics.Role,kotlin.Function0)), [`combinedClickable`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).combinedClickable(androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.foundation.Indication,kotlin.Boolean,kotlin.String,androidx.compose.ui.semantics.Role,kotlin.String,kotlin.Function0,kotlin.Function0,kotlin.Function0)), [`selectable`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/selection/package-summary#(androidx.compose.ui.Modifier).selectable(kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.foundation.Indication,kotlin.Boolean,androidx.compose.ui.semantics.Role,kotlin.Function0)) , [`toggleable`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/selection/package-summary#(androidx.compose.ui.Modifier).toggleable(kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.foundation.Indication,kotlin.Boolean,androidx.compose.ui.semantics.Role,kotlin.Function1)), and [`triStateToggleable`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/selection/package-summary#(androidx.compose.ui.Modifier).triStateToggleable(androidx.compose.ui.state.ToggleableState,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.foundation.Indication,kotlin.Boolean,androidx.compose.ui.semantics.Role,kotlin.Function0)) modifiers.
- [Handle scrolling](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/scroll) with the [`horizontalScroll`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).horizontalScroll(androidx.compose.foundation.ScrollState,kotlin.Boolean,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean)), [`verticalScroll`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#(androidx.compose.ui.Modifier).verticalScroll(androidx.compose.foundation.ScrollState,kotlin.Boolean,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean)), and more generic [`scrollable`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.Modifier).scrollable(androidx.compose.foundation.gestures.ScrollableState,androidx.compose.foundation.gestures.Orientation,kotlin.Boolean,kotlin.Boolean,androidx.compose.foundation.gestures.FlingBehavior,androidx.compose.foundation.interaction.MutableInteractionSource)) modifiers.
- [Handle dragging](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/drag-swipe-fling) with the [`draggable`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.Modifier).draggable(androidx.compose.foundation.gestures.DraggableState,androidx.compose.foundation.gestures.Orientation,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Boolean,kotlin.coroutines.SuspendFunction2,kotlin.coroutines.SuspendFunction2,kotlin.Boolean)) and [`swipeable`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#(androidx.compose.ui.Modifier).swipeable(androidx.compose.material.SwipeableState,kotlin.collections.Map,androidx.compose.foundation.gestures.Orientation,kotlin.Boolean,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function2,androidx.compose.material.ResistanceConfig,androidx.compose.ui.unit.Dp)) modifier.
- [Handle multi-touch gestures](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/multi-touch) such as panning, rotating, and zooming, with the [`transformable`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.Modifier).transformable(androidx.compose.foundation.gestures.TransformableState,kotlin.Boolean,kotlin.Boolean)) modifier.

As a rule, prefer out-of-the-box gesture modifiers over custom gesture handling.
The modifiers add more functionality on top of the pure pointer event handling.
For example, the `clickable` modifier not only adds detection of presses and
taps, but also adds semantic information, visual indications on interactions,
hovering, focus, and keyboard support. You can check the [source code
of `clickable`](https://cs.android.com/android/platform/frameworks/support/+/androidx-main:compose/foundation/foundation/src/commonMain/kotlin/androidx/compose/foundation/Clickable.kt) to see how the functionality
is being added.

### Add custom gesture to arbitrary composables with `pointerInput` modifier

Not every gesture is implemented with an out-of-the-box gesture modifier. For
example, you cannot use a modifier to react to a drag after long-press, a
control-click, or a three-finger tap. Instead, you can write your own gesture
handler to identify these custom gestures. You can create a gesture handler with
the [`pointerInput`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/pointer/package-summary#(androidx.compose.ui.Modifier).pointerInput(kotlin.Any,kotlin.Any,kotlin.coroutines.SuspendFunction1)) modifier, which gives you access to the raw pointer
events.

The following code listens to raw pointer events:


```kotlin
@Composable
private fun LogPointerEvents(filter: PointerEventType? = null) {
    var log by remember { mutableStateOf("") }
    Column {
        Text(log)
        Box(
            Modifier
                .size(100.dp)
                .background(Color.Red)
                .pointerInput(filter) {
                    awaitPointerEventScope {
                        while (true) {
                            val event = awaitPointerEvent()
                            // handle pointer event
                            if (filter == null || event.type == filter) {
                                log = "${event.type}, ${event.changes.first().position}"
                            }
                        }
                    }
                }
        )
    }
}
```

<br />

If you break this snippet up, the core components are:

- The [`pointerInput`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/pointer/package-summary#(androidx.compose.ui.Modifier).pointerInput(kotlin.Any,kotlin.Any,kotlin.coroutines.SuspendFunction1)) modifier. You pass it one or more *keys*. When the value of one of those keys changes, the modifier content lambda is re-executed. The sample passes an optional filter to the composable. If the value of that filter changes, the pointer event handler should be re-executed to make sure the right events are logged.
- [`awaitPointerEventScope`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/pointer/AwaitPointerEventScope) creates a coroutine scope that can be used to wait for pointer events.
- [`awaitPointerEvent`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/pointer/AwaitPointerEventScope#awaitPointerEvent(androidx.compose.ui.input.pointer.PointerEventPass)) suspends the coroutine until a next pointer event occurs.

Although listening to raw input events is powerful, it is also complex to write
a custom gesture based on this raw data. To simplify the creation of custom
gestures, many utility methods are available.

#### Detect full gestures

Instead of handling the raw pointer events, you can listen for specific gestures
to occur and respond appropriately. The [`AwaitPointerEventScope`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/pointer/AwaitPointerEventScope) provides
methods for listening for:

- Press, tap, double tap, and long-press: [`detectTapGestures`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.PointerInputScope).detectTapGestures(kotlin.Function1,kotlin.Function1,kotlin.coroutines.SuspendFunction2,kotlin.Function1))
- Drags: [`detectHorizontalDragGestures`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.PointerInputScope).detectHorizontalDragGestures(kotlin.Function1,kotlin.Function0,kotlin.Function0,kotlin.Function2)), [`detectVerticalDragGestures`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.PointerInputScope).detectVerticalDragGestures(kotlin.Function1,kotlin.Function0,kotlin.Function0,kotlin.Function2)), [`detectDragGestures`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.PointerInputScope).detectDragGestures(kotlin.Function1,kotlin.Function0,kotlin.Function0,kotlin.Function2)) and [`detectDragGesturesAfterLongPress`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.PointerInputScope).detectDragGesturesAfterLongPress(kotlin.Function1,kotlin.Function0,kotlin.Function0,kotlin.Function2))
- Transforms: [`detectTransformGestures`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.PointerInputScope).detectTransformGestures(kotlin.Boolean,kotlin.Function4))

These are top-level detectors, so you can't add multiple detectors within one
`pointerInput` modifier. The following snippet only detects the taps, not the
drags:


```kotlin
var log by remember { mutableStateOf("") }
Column {
    Text(log)
    Box(
        Modifier
            .size(100.dp)
            .background(Color.Red)
            .pointerInput(Unit) {
                detectTapGestures { log = "Tap!" }
                // Never reached
                detectDragGestures { _, _ -> log = "Dragging" }
            }
    )
}
```

<br />

Internally, the `detectTapGestures` method blocks the coroutine, and the second
detector is never reached. If you need to add more than one gesture listener to
a composable, use separate `pointerInput` modifier instances instead:


```kotlin
var log by remember { mutableStateOf("") }
Column {
    Text(log)
    Box(
        Modifier
            .size(100.dp)
            .background(Color.Red)
            .pointerInput(Unit) {
                detectTapGestures { log = "Tap!" }
            }
            .pointerInput(Unit) {
                // These drag events will correctly be triggered
                detectDragGestures { _, _ -> log = "Dragging" }
            }
    )
}
```

<br />

#### Handle events per gesture

By definition, gestures start with a pointer down event. You can use the
[`awaitEachGesture`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.PointerInputScope).awaitEachGesture(kotlin.coroutines.SuspendFunction1)) helper method instead of the `while(true)` loop that
passes through each raw event. The `awaitEachGesture` method restarts the
containing block when all pointers have been lifted, indicating the gesture is
completed:


```kotlin
@Composable
private fun SimpleClickable(onClick: () -> Unit) {
    Box(
        Modifier
            .size(100.dp)
            .pointerInput(onClick) {
                awaitEachGesture {
                    awaitFirstDown().also { it.consume() }
                    val up = waitForUpOrCancellation()
                    if (up != null) {
                        up.consume()
                        onClick()
                    }
                }
            }
    )
}
```

<br />

In practice, you almost always want to use `awaitEachGesture` unless you're
responding to pointer events without identifying gestures. An example of this is
[`hoverable`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).hoverable(androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Boolean)), which does not respond to pointer down or up events--- it just
needs to know when a pointer enters or exits its bounds.

#### Wait for a specific event or sub-gesture

There's a set of methods that helps identify common parts of gestures:

- Suspend until a pointer goes down with [`awaitFirstDown`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.AwaitPointerEventScope).awaitFirstDown(kotlin.Boolean,androidx.compose.ui.input.pointer.PointerEventPass)), or wait for all pointers to go up with [`waitForUpOrCancellation`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.AwaitPointerEventScope).waitForUpOrCancellation(androidx.compose.ui.input.pointer.PointerEventPass)).
- Create a low-level drag listener using [`awaitTouchSlopOrCancellation`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.AwaitPointerEventScope).awaitTouchSlopOrCancellation(androidx.compose.ui.input.pointer.PointerId,kotlin.Function2)) and [`awaitDragOrCancellation`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.AwaitPointerEventScope).awaitDragOrCancellation(androidx.compose.ui.input.pointer.PointerId)). The gesture handler first suspends until the pointer reaches the touch slop and then suspends until a first drag event comes through. If you're only interested in drags along a single axis, use [`awaitHorizontalTouchSlopOrCancellation`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.AwaitPointerEventScope).awaitHorizontalTouchSlopOrCancellation(androidx.compose.ui.input.pointer.PointerId,kotlin.Function2)) plus [`awaitHorizontalDragOrCancellation`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.AwaitPointerEventScope).awaitHorizontalDragOrCancellation(androidx.compose.ui.input.pointer.PointerId)), or [`awaitVerticalTouchSlopOrCancellation`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.AwaitPointerEventScope).awaitVerticalTouchSlopOrCancellation(androidx.compose.ui.input.pointer.PointerId,kotlin.Function2)) plus [`awaitVerticalDragOrCancellation`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.AwaitPointerEventScope).awaitVerticalDragOrCancellation(androidx.compose.ui.input.pointer.PointerId)) instead.
- Suspend until a long press happens with [`awaitLongPressOrCancellation`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.AwaitPointerEventScope).awaitLongPressOrCancellation(androidx.compose.ui.input.pointer.PointerId)).
- Use the [`drag`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.AwaitPointerEventScope).drag(androidx.compose.ui.input.pointer.PointerId,kotlin.Function1)) method to continuously listen to drag events, or [`horizontalDrag`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.AwaitPointerEventScope).horizontalDrag(androidx.compose.ui.input.pointer.PointerId,kotlin.Function1)) or [`verticalDrag`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.AwaitPointerEventScope).verticalDrag(androidx.compose.ui.input.pointer.PointerId,kotlin.Function1)) to listen to drag events on one axis.

#### Apply calculations for multi-touch events

When a user is performing a multi-touch gesture using more than one pointer,
it's complex to understand the required transformation based on the raw values.
If the [`transformable`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.Modifier).transformable(androidx.compose.foundation.gestures.TransformableState,kotlin.Boolean,kotlin.Boolean)) modifier or the [`detectTransformGestures`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.PointerInputScope).detectTransformGestures(kotlin.Boolean,kotlin.Function4))
methods aren't giving enough fine-grained control for your use case, you can
listen to the raw events and apply calculations on those. These helper methods
are [`calculateCentroid`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.PointerEvent).calculateCentroid(kotlin.Boolean)), [`calculateCentroidSize`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.PointerEvent).calculateCentroidSize(kotlin.Boolean)),
[`calculatePan`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.PointerEvent).calculatePan()), [`calculateRotation`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.PointerEvent).calculateRotation()), and [`calculateZoom`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.PointerEvent).calculateZoom()).

## Event dispatching and hit-testing

Not every pointer event is sent to every `pointerInput` modifier. Event
dispatching works as follows:

- Pointer events are dispatched to a *composable hierarchy* . The moment that a new pointer triggers its first pointer event, the system starts hit-testing the "eligible" composables. A composable is considered eligible when it has pointer input handling capabilities. Hit-testing flows from the top of the UI tree to the bottom. A composable is "hit" when the pointer event occurred within the bounds of that composable. This process results in a *chain of
  composables* that hit-test positively.
- By default, when there are multiple eligible composables on the same level of the tree, only the composable with the highest z-index is "hit". For example, when you add two overlapping `Button` composables to a `Box`, only the one drawn on top receives any pointer events. You can theoretically override this behavior by creating your own [`PointerInputModifierNode`](https://developer.android.com/reference/kotlin/androidx/compose/ui/node/PointerInputModifierNode#sharePointerInputWithSiblings()) implementation and setting [`sharePointerInputWithSiblings`](https://developer.android.com/reference/kotlin/androidx/compose/ui/node/PointerInputModifierNode#sharePointerInputWithSiblings()) to true.
- Further events for the same pointer are dispatched *to that same chain of
  composables* , and flow according to [event propagation logic](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/understand-gestures#event-propagation). The system does not perform any more hit-testing for this pointer. This means that each composable in the chain receives all events for that pointer, even when those occur outside of the bounds of that composable. Composables that are not in the chain never receive pointer events, even when the pointer is inside of their bounds.

Hover events, triggered by a mouse or stylus hovering, are an exception to the
rules defined here. Hover events are sent to any composable that they hit. So
when a user hovers a pointer from the bounds of one composable to the next,
instead of sending the events to that first composable, events are sent to the
new composable.

## Event consumption

When more than one composable has a gesture handler assigned to it, those
handlers shouldn't conflict. For example, take a look at this UI:

![List item with an Image, a Column with two texts, and a Button.](https://developer.android.com/static/develop/ui/compose/images/touchinput/jetnews_list_item.png)

When a user taps the bookmark button, the button's `onClick` lambda handles that
gesture. When a user taps on any other part of the list item, the `ListItem`
handles that gesture and navigates to the article. In terms of pointer input,
the Button must *consume* this event, so that its parent knows not to
react to it anymore. Gestures included in out-of-the-box components and the
common gesture modifiers include this consumption behavior, but if you are
writing your own custom gesture, you must consume events manually. You do this
with the [`PointerInputChange.consume`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/pointer/PointerInputChange#consume()) method:


```kotlin
Modifier.pointerInput(Unit) {

    awaitEachGesture {
        while (true) {
            val event = awaitPointerEvent()
            // consume all changes
            event.changes.forEach { it.consume() }
        }
    }
}
```

<br />

Consuming an event does not stop the event propagation to other composables. A
composable needs to explicitly ignore consumed events instead. When writing
custom gestures, you should check if an event was already consumed by another
element:


```kotlin
Modifier.pointerInput(Unit) {
    awaitEachGesture {
        while (true) {
            val event = awaitPointerEvent()
            if (event.changes.any { it.isConsumed }) {
                // A pointer is consumed by another gesture handler
            } else {
                // Handle unconsumed event
            }
        }
    }
}
```

<br />

## Event propagation

As mentioned before, pointer changes are passed to each composable that it hits.
But if more than one such composable exists, in what order do the events
propagate? If you take the example from the last section, this UI translates to
the following UI tree, where only the `ListItem` and the `Button` respond to
pointer events:

![Tree structure. Top layer is ListItem, second layer has Image, Column, and Button, and the Column splits out into two Texts. ListItem and Button are highlighted.](https://developer.android.com/static/develop/ui/compose/images/touchinput/ui_tree.png)

Pointer events flow through each of these composables three times, during three
"passes":

- In the **Initial pass** , the event flows from the top of the UI tree to the bottom. This flow allows a parent to intercept an event before the child can consume it. For example, [tooltips](https://m3.material.io/components/tooltips/guidelines#00e87770-86d0-436d-b50b-436ff3cefe75) need to [intercept a
  long-press](https://cs.android.com/android/platform/frameworks/support/+/androidx-main:compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/Tooltip.kt;l=214;drc=a4afaec2343443fe848dc44da26358a809f5d379) instead of passing it on to their children. In our example, `ListItem` receives the event before the `Button`.
- In the **Main pass** , the event flows from the UI tree's leaf nodes up to the root of the UI tree. This phase is where you normally consume gestures, and is the default pass when listening to events. Handling gestures in this pass means that leaf nodes takes precedence over their parents, which is the most logical behavior for most gestures. In our example, the `Button` receives the event before the `ListItem`.
- In the **Final pass**, the event flows one more time from the top of the UI tree to the leaf nodes. This flow allows elements higher in the stack to respond to event consumption by their parent. For example, a button removes its ripple indication when a press turns into a drag of its scrollable parent.

Visually, the event flow can be represented as follows:

Once an input change is consumed, this information is passed from that
point in the flow onwards:

In code, you can specify the pass that you're interested in:


```kotlin
Modifier.pointerInput(Unit) {
    awaitPointerEventScope {
        val eventOnInitialPass = awaitPointerEvent(PointerEventPass.Initial)
        val eventOnMainPass = awaitPointerEvent(PointerEventPass.Main) // default
        val eventOnFinalPass = awaitPointerEvent(PointerEventPass.Final)
    }
}
```

<br />

In this code snippet, the same identical event is returned by each of
these await method calls, although the data about the consumption might have
changed.

## Test gestures

In your test methods, you can manually send pointer events using the
[`performTouchInput`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/package-summary#(androidx.compose.ui.test.SemanticsNodeInteraction).performTouchInput(kotlin.Function1)) method. This lets you perform either higher-level
full gestures (such as pinch or long click) or low level gestures (such as
moving the cursor by a certain amount of pixels):


```kotlin
composeTestRule.onNodeWithTag("MyList").performTouchInput {
    swipeUp()
    swipeDown()
    click()
}
```

<br />

See the [`performTouchInput`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/package-summary#(androidx.compose.ui.test.SemanticsNodeInteraction).performTouchInput(kotlin.Function1)) documentation for more examples.

## Learn more

You can learn more about gestures in Jetpack Compose from the following
resources:

- [Types of gestures](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/multi-touch)
- [`PointerInputChange`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/pointer/PointerInputChange)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Accessibility in Compose](https://developer.android.com/develop/ui/compose/accessibility)
- [Scroll](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/scroll)
- [Tap and press](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/tap-and-press)