---
title: Two-dimensional scrolling: scrollable2D, draggable2D  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/touch-input/scroll/two-dimensional-scrolling
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Two-dimensional scrolling: scrollable2D, draggable2D Stay organized with collections Save and categorize content based on your preferences.




In Jetpack Compose, **[`scrollable2D`](/reference/kotlin/androidx/compose/foundation/gestures/scrollable2D.modifier#(androidx.compose.ui.Modifier).scrollable2D(androidx.compose.foundation.gestures.Scrollable2DState,kotlin.Boolean,androidx.compose.foundation.OverscrollEffect,androidx.compose.foundation.gestures.FlingBehavior,androidx.compose.foundation.interaction.MutableInteractionSource))** and **[`draggable2D`](/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).draggable2D(androidx.compose.foundation.gestures.Draggable2DState,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Boolean,kotlin.Function1,kotlin.Function1,kotlin.Boolean))** are
low-level modifiers designed to handle pointer input in two dimensions. While
the standard 1D modifiers **[`scrollable`](/reference/kotlin/androidx/compose/foundation/gestures/scrollable.modifier#(androidx.compose.ui.Modifier).scrollable(androidx.compose.foundation.gestures.ScrollableState,androidx.compose.foundation.gestures.Orientation,kotlin.Boolean,kotlin.Boolean,androidx.compose.foundation.gestures.FlingBehavior,androidx.compose.foundation.interaction.MutableInteractionSource))** and **[`draggable`](/reference/kotlin/androidx/compose/foundation/gestures/draggable.modifier#(androidx.compose.ui.Modifier).draggable(androidx.compose.foundation.gestures.DraggableState,androidx.compose.foundation.gestures.Orientation,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Boolean,kotlin.coroutines.SuspendFunction2,kotlin.coroutines.SuspendFunction2,kotlin.Boolean)))** are
restricted to a single orientation, the 2D variants track movement across both
the X and Y axes simultaneously.

For example, the existing `scrollable` modifier is used for single-orientation
scrolling and flinging, while `scrollable2d` is used for scrolling and flinging
in 2D. This allows you to create more complex layouts that move in all
directions, such as spreadsheets or image viewers. The `scrollable2d` modifier
also supports nested scrolling in 2D scenarios.

[

](/static/develop/ui/compose/images/scroll/two-dimensional-scroll.mp4)

**Figure 1.** A bi-directional panning on a map.

## Choose `scrollable2D` or `draggable2D`

Choosing the right API depends on the UI elements you want to move and the
preferred physical behavior for these elements.

**[`Modifier.scrollable2D`](/reference/kotlin/androidx/compose/foundation/gestures/scrollable2D.modifier#(androidx.compose.ui.Modifier).scrollable2D(androidx.compose.foundation.gestures.Scrollable2DState,kotlin.Boolean,androidx.compose.foundation.OverscrollEffect,androidx.compose.foundation.gestures.FlingBehavior,androidx.compose.foundation.interaction.MutableInteractionSource))**: Use this modifier on a container to move content inside it. For example, use it with maps, spreadsheets, or photo viewers, where the container's content needs to scroll in both horizontal and vertical directions. It includes built-in fling support so the content keeps moving after a swipe, and it coordinates with other scrolling components on the page.

**[`Modifier.draggable2D`](/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).draggable2D(androidx.compose.foundation.gestures.Draggable2DState,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Boolean,kotlin.Function1,kotlin.Function1,kotlin.Boolean))**: Use this modifier to move a component itself. It's a lightweight modifier, so the movement stops exactly when the user's finger stops. It does not include fling support.

If you want to make a component draggable, but don't need fling or nested scroll
support, use `draggable2D`.

## Implement 2D modifiers

The following sections provide examples to show how to use the 2D modifiers.

### Implement `Modifier.scrollable2D`

Use this modifier for containers where the user needs to move content in all
directions.

#### Capture 2D movement data

This example shows how to capture raw 2D movement data and display the X,Y
offset:

```
@Composable
private fun Scrollable2DSample() {
    // 1. Manually track the total distance the user has moved in both X and Y directions
    var offset by remember { mutableStateOf(Offset.Zero) }

    Box(
        modifier = Modifier
            .fillMaxSize()
            // ...
        contentAlignment = Alignment.Center
    ) {
        Box(
            modifier = Modifier
                .size(200.dp)
                // 2. Attach the 2D scroll logic to capture XY movement deltas
                .scrollable2D(
                    state = rememberScrollable2DState { delta ->
                        // 3. Update the cumulative offset state with the new movement delta
                        offset += delta

                        // Return the delta to indicate the entire movement was handled by this box
                        delta
                    }
                )
                // ...
            contentAlignment = Alignment.Center
        ) {
            Column(horizontalAlignment = Alignment.CenterHorizontally) {
                // 4. Display the current X and Y values from the offset state in real-time
                Text(
                    text = "X: ${offset.x.roundToInt()}",
                    // ...
                )
                Spacer(modifier = Modifier.height(8.dp))
                Text(
                    text = "Y: ${offset.y.roundToInt()}",
                    // ...
                )
            }
        }
    }
}

TwoDimensionalScrollSnippets.kt
```

[

](/static/develop/ui/compose/images/scroll/two-dimensional-movement.mp4)

**Figure 2.** A purple box that tracks and displays the current X and Y coordinate offsets as a user drags the pointer across its surface.

The preceding snippet does the following:

* Uses `offset` as a state that holds the total distance the user has scrolled.
* Inside `rememberScrollable2DState`, a lambda function is defined to handle
  every delta, generated by the user's finger. The code `offset.value += delta`
  updates the manual state with the new position.
* The `Text` components display the current X and Y values of that `offset`
  state, which update in real-time as the user drags.

#### Pan a large viewport

This example shows how to use captured 2D scrollable data and apply a
`translationX` and `translationY` to content that is larger than its parent
container:

```
@Composable
private fun Panning2DImage() {

    // Manually track the total distance the user has moved in both X and Y directions
    val offset = remember { mutableStateOf(Offset.Zero) }

    // Define how gestures are captured. The lambda is called for every finger movement
    val scrollState = rememberScrollable2DState { delta ->
        offset.value += delta
        delta
    }

    // The Viewport (Container): A fixed-size box that acts as a window into the larger content
    Box(
        modifier = Modifier
            .size(600.dp, 400.dp) // The visible area dimensions
            // ...
            // Hide any parts of the large content that sit outside this container's boundaries
            .clipToBounds()
            // Apply the 2D scroll modifier to intercept touch and fling gestures in all directions
            .scrollable2D(state = scrollState),
        contentAlignment = Alignment.Center,
    ) {
        // The Content: An image given a much larger size than the container viewport
        Image(
            painter = painterResource(R.drawable.cheese_5),
            contentDescription = null,
            modifier = Modifier
                .requiredSize(1200.dp, 800.dp)
                // Manual Scroll Effect: Since scrollable2D doesn't move content automatically,
                // we use graphicsLayer to shift the drawing position based on the tracked offset.
                .graphicsLayer {
                    translationX = offset.value.x
                    translationY = offset.value.y
                },
            contentScale = ContentScale.FillBounds
        )
    }
}

TwoDimensionalScrollSnippets.kt
```

[

](/static/develop/ui/compose/images/scroll/panning-image.mp4)

**Figure 3.** A bi-directional panning image viewport, created with `Modifier.scrollable2D`.



[

](/static/develop/ui/compose/images/scroll/panning-text.mp4)

**Figure 4.** A bi-directional panning text viewport, created with `Modifier.scrollable2D`.

The preceding snippet includes the following:

* The container is set to a fixed size (`600x400dp`), while the content is given
  a much larger size (`1200x800dp`) to avoid it resizing to
  its parent size.
* The `clipToBounds()` modifier on the container ensures that any part of the
  large content that sits outside the `600x400` box is hidden from view.
* Unlike high-level components like `LazyColumn`, `scrollable2D` does not move the
  content for you automatically. Instead, you must apply the tracked `offset` to
  your content, either using `graphicsLayer` transformations or layout offsets.
* Inside the `graphicsLayer` block, `translationX = offset.value.x` and
  `translationY = offset.value.y` shift the drawing position of the image or
  text based on your finger's movement, creating the visual effect of scrolling.

#### Implement nested scrolling with scrollable2D

This example demonstrates how a bi-directional component can be integrated into
a standard one-dimensional parent, like a vertical news feed.

Keep the following points in mind when implementing nested scrolling:

* The lambda for `rememberScrollable2DState` should return only the **consumed
  delta**, to let the **parent list take over naturally** when the child reaches
  its limit.
* When a user performs a diagonal fling, the 2D velocity is shared. If the child
  hits a boundary during the animation, the **remaining momentum is propagated**
  to the parent to continue the scroll naturally.

```
@Composable
private fun NestedScrollable2DSample() {
    var offset by remember { mutableStateOf(Offset.Zero) }
    val maxScrollDp = 250.dp
    val maxScrollPx = with(LocalDensity.current) { maxScrollDp.toPx() }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .verticalScroll(rememberScrollState())
            .background(Color(0xFFF5F5F5)),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(
            "Scroll down to find the 2D Box",
            modifier = Modifier.padding(top = 100.dp, bottom = 500.dp),
            style = TextStyle(fontSize = 18.sp, color = Color.Gray)
        )

        // The Child: A 2D scrollable box with nested scroll coordination
        Box(
            modifier = Modifier
                .size(250.dp)
                .scrollable2D(
                    state = rememberScrollable2DState { delta ->
                        val oldOffset = offset

                        // Calculate new potential offset and clamp it to our boundaries
                        val newX = (oldOffset.x + delta.x).coerceIn(-maxScrollPx, maxScrollPx)
                        val newY = (oldOffset.y + delta.y).coerceIn(-maxScrollPx, maxScrollPx)

                        val newOffset = Offset(newX, newY)

                        // Calculate exactly how much was consumed by the child
                        val consumed = newOffset - oldOffset

                        offset = newOffset

                        // IMPORTANT: Return ONLY the consumed delta.
                        // The remaining (unconsumed) delta propagates to the parent Column.
                        consumed
                    }
                )
                // ...
            contentAlignment = Alignment.Center
        ) {
            Column(horizontalAlignment = Alignment.CenterHorizontally) {
                val density = LocalDensity.current
                Text("2D Panning Zone", color = Color.White.copy(alpha = 0.7f), fontSize = 12.sp)
                Spacer(Modifier.height(8.dp))
                Text("X: ${with(density) { offset.x.toDp().value.roundToInt() }}dp", color = Color.White, fontWeight = FontWeight.Bold)
                Text("Y: ${with(density) { offset.y.toDp().value.roundToInt() }}dp", color = Color.White, fontWeight = FontWeight.Bold)
            }
        }

        Text(
            "Once the Purple Box hits Y: 250 or -250,\nthis parent list will take over the vertical scroll.",
            textAlign = TextAlign.Center,
            modifier = Modifier.padding(top = 40.dp, bottom = 800.dp),
            style = TextStyle(fontSize = 14.sp, color = Color.Gray)
        )
    }
}

TwoDimensionalScrollSnippets.kt
```

[

](/static/develop/ui/compose/images/scroll/nested-scrolling.mp4)

**Figure 5.** A purple box within a vertical scrolling list that allows internal 2D movement, but passes vertical scroll control to the parent list once the box's internal Y-offset reaches its 300-pixel limit.

In the preceding snippet:

* The 2D component can consume X axis movement to pan internally while
  simultaneously dispatching Y axis movement to the parent list once the child's
  own vertical boundaries are reached.
* Instead of trapping the user within the 2D surface, the system calculates the
  consumed delta and passes the remainder up the hierarchy. This ensures the
  user can continue scrolling through the rest of the page without lifting their
  finger.

### Implement `Modifier.draggable2D`

Use the `draggable2D` modifier for moving individual UI elements.

#### Drag a composable element

This example shows the most common use case for `draggable2D` — allowing a user
to pick up a UI element and reposition it anywhere within a parent container.

**Note:** `draggable2D` shouldn't be confused with the [Drag and Drop](/develop/ui/compose/touch-input/user-interactions/drag-and-drop) pattern.
The `dragAndDropSource` modifier is for use with transferring data (URIs, text)
between applications, whereas `draggable2D` is for within the same composable
hierarchy.

```
@Composable
private fun DraggableComposableElement() {
    // 1. Track the position of the floating window
    var offset by remember { mutableStateOf(Offset.Zero) }

    Box(modifier = Modifier.fillMaxSize().background(Color(0xFFF5F5F5))) {
        Box(
            modifier = Modifier
                // 2. Apply the offset to the box's position
                .offset { IntOffset(offset.x.roundToInt(), offset.y.roundToInt()) }
                // ...
                // 3. Attach the 2D drag logic
                .draggable2D(
                    state = rememberDraggable2DState { delta ->
                        // 4. Update the position based on the movement delta
                        offset += delta
                    }
                ),
            contentAlignment = Alignment.Center
        ) {
            Text("Video Preview", color = Color.White, fontSize = 12.sp)
        }
    }
}

TwoDimensionalScrollSnippets.kt
```

[

](/static/develop/ui/compose/images/scroll/dragging.mp4)

**Figure 6.** A small purple box being repositioned on a gray background, demonstrating direct 2D dragging where the element stops moving the instant the user's finger is lifted.

The preceding code snippet includes the following:

* Tracks the box's position using an `offset` state.
* Uses `offset` modifier to shift the component's position based on the drag
  deltas.
* Since there is no fling support, the box stops moving the instant the user
  lifts their finger.

#### Drag a child composable based on parent's drag area

This example demonstrates how to use `draggable2D` to create a 2D input area
where a selector knob is constrained within a specific surface. Unlike the
draggable element example, which moves the component itself, this implementation
uses the 2D deltas to move a child composable "selector" across a color picker:

```
@Composable
private fun ExampleColorSelector(
    // ...
)  {
    // 1. Maintain the 2D position of the selector in state.
    var selectorOffset by remember { mutableStateOf(Offset.Zero) }

    // 2. Track the size of the background container.
    var containerSize by remember { mutableStateOf(IntSize.Zero) }

    Box(
        modifier = Modifier
            .size(300.dp, 200.dp)
            // Capture the actual pixel dimensions of the container when it's laid out.
            .onSizeChanged { containerSize = it }
            .clip(RoundedCornerShape(12.dp))
            .background(
                brush = remember(hue) {
                    // Create a simple gradient representing Saturation and Value for the given Hue.
                    Brush.linearGradient(listOf(Color.White, Color.hsv(hue, 1f, 1f)))
                }
            )
    ) {
        Box(
            modifier = Modifier
                .size(24.dp)
                .graphicsLayer {
                    // Center the selector on the finger by subtracting half its size.
                    translationX = selectorOffset.x - (24.dp.toPx() / 2)
                    translationY = selectorOffset.y - (24.dp.toPx() / 2)
                }
                // ...
                // 3. Configure 2D touch dragging.
                .draggable2D(
                    state = rememberDraggable2DState { delta ->
                        // 4. Calculate the new position and clamp it to the container bounds
                        val newX = (selectorOffset.x + delta.x)
                            .coerceIn(0f, containerSize.width.toFloat())
                        val newY = (selectorOffset.y + delta.y)
                            .coerceIn(0f, containerSize.height.toFloat())

                        selectorOffset = Offset(newX, newY)
                    }
                )
        )
    }
}

TwoDimensionalScrollSnippets.kt
```

[

](/static/develop/ui/compose/images/scroll/color-picker.mp4)

**Figure 7.** A color gradient with a white circular selector knob that can be dragged in any direction, demonstrating how 2D deltas are clamped to the container's boundaries to update selected color values.

The preceding snippet includes the following:

* It uses the `onSizeChanged` modifier to capture the actual dimensions of the
  gradient container. The selector knows exactly where the edges are.
* Inside the `graphicsLayer`, it adjusts the `translationX` and `translationY`
  to make sure the selector stays centered while dragging.

[Previous

arrow\_back

Nested scroll modifiers](/develop/ui/compose/touch-input/scroll/nested-scroll-modifiers)