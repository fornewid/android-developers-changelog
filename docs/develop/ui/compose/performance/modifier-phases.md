---
title: Modifier breakdown by phase  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/performance/modifier-phases
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Modifier breakdown by phase Stay organized with collections Save and categorize content based on your preferences.





Jetpack Compose executes modifiers across distinct phases. The following
breakdown shows which phase common modifiers belong to and when their arguments
or lambdas are evaluated.

## Phase 1: Composition phase

These modifiers evaluate arguments **synchronously inside the `@Composable`
body**. Any state read here registers a dependency with the Composable restart
scope and triggers a full recomposition when changed.

* **Static Dimension & Sizing Modifiers**:
  + `Modifier.size(dp)`, `Modifier.width(dp)`, `Modifier.height(dp)`
  + `Modifier.fillMaxSize()`, `Modifier.fillMaxWidth()`, `Modifier.fillMaxHeight()`
  + `Modifier.wrapContentSize()`, `Modifier.wrapContentWidth()`, `Modifier.wrapContentHeight()`
  + `Modifier.requiredSize()`, `Modifier.defaultMinSize()`
  + `Modifier.aspectRatio(ratio)`
  + `Modifier.weight(weight)` *(in* *`RowScope`* *or* *`ColumnScope`**)*
  + `Modifier.width(IntrinsicSize.Min / Max)`
  + `Modifier.height(IntrinsicSize.Min / Max)`
* **Static Spacing & Insets**:
  + `Modifier.padding(all = dp)`, `Modifier.padding(start, top, end, bottom)`
  + `Modifier.windowInsetsPadding(insets)`, `Modifier.statusBarsPadding()`
* **Direct Value Visual Modifiers**:
  + `Modifier.alpha(float)` *(reads state during composition)*
  + `Modifier.rotate(degrees)` *(reads state during composition)*
  + `Modifier.scale(scaleX, scaleY)` *(reads state during composition)*
  + `Modifier.background(color = Color, shape = Shape)`
  + `Modifier.border(width, color, shape)`
  + `Modifier.shadow(elevation, shape)`
  + `Modifier.clip(shape)`
  + `Modifier.blur(radius)`
* **Static Position Modifiers**:
  + `Modifier.offset(x = dp, y = dp)` *(direct value overload)*
  + `Modifier.absoluteOffset(x = dp, y = dp)`
* **Dynamic Composable Modifiers**:
  + `Modifier.composed { ... }` *(runs the factory body during composition)*

## Phase 2: Layout phase

The Layout phase is split into two distinct sub-steps with separate invalidation
scopes:

### Step 2A: Measurement

Determines the size (`width`, `height`) and constraints. State read here
triggers **re-measurement** and re-placement:

* `Modifier.layout { measurable, constraints -> ... }`: Code before
  `layout(w, h)` executes during measurement.

### Step 2B: Placement & layout callbacks

Determines the `(x, y)` coordinate position. State read here triggers
**re-placement only** (skipping measurement and composition):

* `Modifier.offset { IntOffset(x, y) }` *(lambda overload)*
* `Modifier.absoluteOffset { IntOffset(x, y) }` *(lambda overload)*
* `Modifier.layout { ... layout(w, h) { placeable.place(x, y) } }`: Code inside
  the `layout(w, h) { ... }` block.
* `Modifier.onPlaced { layoutCoordinates -> ... }`: Invoked after parent
  coordinates are determined during placement.
* `Modifier.onSizeChanged { intSize -> ... }`: Invoked after layout measurement
  completes if the size changed.
* `Modifier.onGloballyPositioned { layoutCoordinates -> ... }`: Invoked after
  the entire window layout pass finishes.

## Phase 3: Drawing phase

These modifiers execute during canvas drawing. State read inside these blocks
skips **both Composition and Layout**, running only the draw pass:

* **`Modifier.graphicsLayer { ... }`**:
  + Properties updated in lambda: `alpha`, `translationX`, `translationY`,
    `scaleX`, `scaleY`, `rotationX`, `rotationY`, `rotationZ`,
    `shadowElevation`, `shape`, `clip`, `renderEffect`, `transformOrigin`.
* **`Modifier.drawBehind { ... }`**:
  + Draws canvas commands behind the composable content.
* **`Modifier.drawWithContent { ... }`**:
  + Controls drawing order with `drawContent()`.
* **`Modifier.drawWithCache { ... }`**:
  + Outer block runs on size or layout changes to cache `Path`, `Paint`, or
    `Brush` objects; `onDrawBehind` or `onDrawWithContent` runs on each frame
    draw.

## Outside of recomposition loop - observation modifiers

Some modifiers operate outside the three frame phases to handle accessibility,
user input, and lifecycle observations.

### Semantics & accessibility

Processes semantic properties for accessibility services (TalkBack) and testing:

* `Modifier.semantics { ... }`
* `Modifier.clearAndSetSemantics { ... }`

### Input, gestures & events

Operates outside the three-phase frame rendering pipeline, receiving OS motion
events and user interactions:

* `Modifier.pointerInput(key) { detectTapGestures { ... } }` /
  `detectDragGestures` / `awaitPointerEventScope`
* `Modifier.clickable(enabled, onClickLabel) { ... }`
* `Modifier.combinedClickable { ... }`
* `Modifier.toggleable { ... }`
* `Modifier.selectable { ... }`
* `Modifier.draggable(...)` / `Modifier.scrollable(...)` /
  `Modifier.draggable2D(...)`
* `Modifier.onFocusChanged { focusState -> ... }`
* `Modifier.onKeyEvent { keyEvent -> ... }`
* `Modifier.onVisibilityChanged { isVisible -> ... }`: The callback is invoked
  when visibility of a composable changes after configured delay, in a
  coroutine.

---

## Quick Reference: Value versus Lambda phase

Reading a state value in a lambda defers the read to a later phase, which
**skips earlier phases** when that state changes:

| **Modifier / Pattern** | **Direct Value (Composition)** | **Lambda Variant (Deferred Phase)** | **When State Changes** |
| --- | --- | --- | --- |
| **Offset** | `Modifier.offset(x, y)` | `Modifier.offset { IntOffset(x, y) }` | **Layout (Placement)** (Skips Composition) |
| **Alpha / Opacity** | `Modifier.alpha(alpha)` | `Modifier.graphicsLayer { this.alpha = alpha }` | **Drawing** (Skips Composition & Layout) |
| **Rotation** | `Modifier.rotate(degrees)` | `Modifier.graphicsLayer { rotationZ = degrees }` | **Drawing** (Skips Composition & Layout) |
| **Scale** | `Modifier.scale(scale)` | `Modifier.graphicsLayer { scaleX = s; scaleY = s }` | **Drawing** (Skips Composition & Layout) |
| **Translation** | `Modifier.padding(...)` | `Modifier.graphicsLayer { translationX = ... }` | **Drawing** (Skips Composition & Layout) |
| **Background Color** | `Modifier.background(color)` | `Modifier.drawBehind { drawRect(color) }` | **Drawing** (Skips Composition & Layout) |
| **Scroll / Parallax** | `Modifier.offset(scroll.dp)` | `Modifier.offset { IntOffset(0, scroll) }` | **Layout (Placement)** (Skips Composition) |

## Modifier.Node interface mapping

For custom modifiers using the high-performance `Modifier.Node` API, phases map
directly to node capability interfaces:

| **Phase** | **`Modifier.Node` Interface** | **Core Methods** |
| --- | --- | --- |
| **Layout (Measure & Place)** | `LayoutModifierNode` | `measure(measurable, constraints)` |
| **Layout (Global Coordinates)** | `GlobalPositionAwareModifierNode` | `onGloballyPositioned(coordinates)` |
| **Layout (Placement)** | `LayoutAwareModifierNode` | `onRemeasured(size)`, `onPlaced(coordinates)` |
| **Drawing** | `DrawModifierNode` | `draw(ContentDrawScope)` |
| **Input / Pointer** | `PointerInputModifierNode` | `onPointerEvent(...)`, `onCancelPointerInput()` |
| **Semantics** | `SemanticsModifierNode` | `applySemantics(SemanticsPropertyReceiver)` |
| **Focus** | `FocusEventModifierNode` | `onFocusEvent(focusState)` |