---
title: List of Compose modifiers  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/modifiers-list
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# List of Compose modifiers Stay organized with collections Save and categorize content based on your preferences.



## Actions

|  |  |
| --- | --- |
| Scope: **Any** | `<T : Any?> Modifier.anchoredDraggable(      state: AnchoredDraggableState<T>,      orientation: Orientation,      enabled: Boolean,      interactionSource: MutableInteractionSource?,      overscrollEffect: OverscrollEffect?,      flingBehavior: FlingBehavior?  )`  Enable drag gestures between a set of predefined values. |
| Scope: **Any** | `<T : Any?> Modifier. anchoredDraggable(      state: AnchoredDraggableState<T>,      orientation: Orientation,      enabled: Boolean,      interactionSource: MutableInteractionSource?,      overscrollEffect: OverscrollEffect?,      startDragImmediately: Boolean,      flingBehavior: FlingBehavior?  )`  **This function is deprecated.** startDragImmediately has been removed without replacement. |
| Scope: **Any** | `<T : Any?> Modifier.anchoredDraggable(      state: AnchoredDraggableState<T>,      reverseDirection: Boolean,      orientation: Orientation,      enabled: Boolean,      interactionSource: MutableInteractionSource?,      overscrollEffect: OverscrollEffect?,      flingBehavior: FlingBehavior?  )`  Enable drag gestures between a set of predefined values. |
| Scope: **Any** | `<T : Any?> Modifier. anchoredDraggable(      state: AnchoredDraggableState<T>,      reverseDirection: Boolean,      orientation: Orientation,      enabled: Boolean,      interactionSource: MutableInteractionSource?,      overscrollEffect: OverscrollEffect?,      startDragImmediately: Boolean,      flingBehavior: FlingBehavior?  )`  **This function is deprecated.** startDragImmediately has been removed without replacement. |
| Scope: **Any** | `Modifier.clickable(      enabled: Boolean,      onClickLabel: String?,      role: Role?,      interactionSource: MutableInteractionSource?,      onClick: () -> Unit  )`  Configure component to receive clicks via input or accessibility "click" event. |
| Scope: **Any** | `Modifier.clickable(      interactionSource: MutableInteractionSource?,      indication: Indication?,      enabled: Boolean,      onClickLabel: String?,      role: Role?,      onClick: () -> Unit  )`  Configure component to receive clicks via input or accessibility "click" event. |
| Scope: **Any** | `Modifier.combinedClickable(      enabled: Boolean,      onClickLabel: String?,      role: Role?,      onLongClickLabel: String?,      onLongClick: (() -> Unit)?,      onDoubleClick: (() -> Unit)?,      hapticFeedbackEnabled: Boolean,      interactionSource: MutableInteractionSource?,      onClick: () -> Unit  )`  Configure component to receive clicks, double clicks and long clicks via input or accessibility "click" event. |
| Scope: **Any** | `Modifier.combinedClickable(      interactionSource: MutableInteractionSource?,      indication: Indication?,      enabled: Boolean,      onClickLabel: String?,      role: Role?,      onLongClickLabel: String?,      onLongClick: (() -> Unit)?,      onDoubleClick: (() -> Unit)?,      hapticFeedbackEnabled: Boolean,      onClick: () -> Unit  )`  Configure component to receive clicks, double clicks and long clicks via input or accessibility "click" event. |
| Scope: **Any** | `Modifier.draggable2D(      state: Draggable2DState,      enabled: Boolean,      interactionSource: MutableInteractionSource?,      startDragImmediately: Boolean,      onDragStarted: (startedPosition: Offset) -> Unit,      onDragStopped: (velocity: Velocity) -> Unit,      reverseDirection: Boolean  )`  Configure touch dragging for the UI element in both orientations. |
| Scope: **Any** | `Modifier.draggable(      state: DraggableState,      orientation: Orientation,      enabled: Boolean,      interactionSource: MutableInteractionSource?,      startDragImmediately: Boolean,      onDragStarted: suspend CoroutineScope.(startedPosition: Offset) -> Unit,      onDragStopped: suspend CoroutineScope.(velocity: Float) -> Unit,      reverseDirection: Boolean  )`  Configure touch dragging for the UI element in a single `Orientation`. |
| Scope: **Any** | `Modifier.selectableGroup()`  Use this modifier to group a list of `selectable` items like Tabs or RadioButtons together for accessibility purpose. |
| Scope: **Any** | `Modifier.selectable(      selected: Boolean,      enabled: Boolean,      role: Role?,      interactionSource: MutableInteractionSource?,      onClick: () -> Unit  )`  Configure component to be selectable, usually as a part of a mutually exclusive group, where only one item can be selected at any point in time. |
| Scope: **Any** | `Modifier.selectable(      selected: Boolean,      interactionSource: MutableInteractionSource?,      indication: Indication?,      enabled: Boolean,      role: Role?,      onClick: () -> Unit  )`  Configure component to be selectable, usually as a part of a mutually exclusive group, where only one item can be selected at any point in time. |
| Scope: **Any** | `@ExperimentalMaterialApi  <T : Any?> Modifier. swipeable(      state: SwipeableState<T>,      anchors: Map<Float, T>,      orientation: Orientation,      enabled: Boolean,      reverseDirection: Boolean,      interactionSource: MutableInteractionSource?,      thresholds: (from, to) -> ThresholdConfig,      resistance: ResistanceConfig?,      velocityThreshold: Dp  )`  **This function is deprecated.** Material's Swipeable has been replaced by Foundation's AnchoredDraggable APIs. |
| Scope: **Any** | `@ExperimentalWearMaterialApi  <T : Any?> Modifier.swipeable(      state: SwipeableState<T>,      anchors: Map<Float, T>,      orientation: Orientation,      enabled: Boolean,      reverseDirection: Boolean,      interactionSource: MutableInteractionSource?,      thresholds: (from, to) -> ThresholdConfig,      resistance: ResistanceConfig?,      velocityThreshold: Dp  )`  Enable swipe gestures between a set of predefined states. |
| Scope: **Any** | `Modifier.toggleable(      value: Boolean,      enabled: Boolean,      role: Role?,      interactionSource: MutableInteractionSource?,      onValueChange: (Boolean) -> Unit  )`  Configure component to make it toggleable via input and accessibility events |
| Scope: **Any** | `Modifier.toggleable(      value: Boolean,      interactionSource: MutableInteractionSource?,      indication: Indication?,      enabled: Boolean,      role: Role?,      onValueChange: (Boolean) -> Unit  )`  Configure component to make it toggleable via input and accessibility events. |
| Scope: **Any** | `Modifier.triStateToggleable(      state: ToggleableState,      enabled: Boolean,      role: Role?,      interactionSource: MutableInteractionSource?,      onClick: () -> Unit  )`  Configure component to make it toggleable via input and accessibility events with three states: On, Off and Indeterminate. |
| Scope: **Any** | `Modifier.triStateToggleable(      state: ToggleableState,      interactionSource: MutableInteractionSource?,      indication: Indication?,      enabled: Boolean,      role: Role?,      onClick: () -> Unit  )`  Configure component to make it toggleable via input and accessibility events with three states: On, Off and Indeterminate. |
| Scope: `PaneScaffoldScope` | `Modifier.paneExpansionDraggable(      state: PaneExpansionState,      minTouchTargetSize: Dp,      interactionSource: MutableInteractionSource,      semanticsProperties: (SemanticsPropertyReceiver.() -> Unit)?  )`  The modifier that should be applied on a drag handle composable so the drag handle can be dragged and operate on the provided `PaneExpansionState` properly. |

## Alignment

|  |  |
| --- | --- |
| Scope: `RowScope` | `Modifier.align(alignment: Alignment.Vertical)`  Align the element vertically within the `Row`. |
| Scope: `RowScope` | `Modifier.alignBy(alignmentLineBlock: (Measured) -> Int)`  Position the element vertically such that the alignment line for the content as determined by `alignmentLineBlock` aligns with sibling elements also configured to `alignBy`. |
| Scope: `RowScope` | `Modifier.alignBy(alignmentLine: HorizontalAlignmentLine)`  Position the element vertically such that its `alignmentLine` aligns with sibling elements also configured to `alignBy`. |
| Scope: `RowScope` | `Modifier.alignByBaseline()`  Position the element vertically such that its first baseline aligns with sibling elements also configured to `alignByBaseline` or `alignBy`. |
| Scope: `ColumnScope` | `Modifier.align(alignment: Alignment.Horizontal)`  Align the element horizontally within the `Column`. |
| Scope: `ColumnScope` | `Modifier.alignBy(alignmentLineBlock: (Measured) -> Int)`  Position the element horizontally such that the alignment line for the content as determined by `alignmentLineBlock` aligns with sibling elements also configured to `alignBy`. |
| Scope: `ColumnScope` | `Modifier.alignBy(alignmentLine: VerticalAlignmentLine)`  Position the element horizontally such that its `alignmentLine` aligns with sibling elements also configured to `alignBy`. |
| Scope: `BoxScope` | `Modifier.align(alignment: Alignment)`  Pull the content element to a specific `Alignment` within the `Box`. |

## Animation

|  |  |
| --- | --- |
| Scope: **Any** | `Modifier.animateBounds(      lookaheadScope: LookaheadScope,      modifier: Modifier,      boundsTransform: BoundsTransform,      animateMotionFrameOfReference: Boolean  )`  `Modifier` to animate layout changes (position and/or size) that occur within a `LookaheadScope`. |
| Scope: **Any** | `@ExperimentalMaterial3ExpressiveApi Modifier.animateFloatingActionButton(      visible: Boolean,      alignment: Alignment,      targetScale: Float,      scaleAnimationSpec: AnimationSpec<Float>?,      alphaAnimationSpec: AnimationSpec<Float>?  )`  Apply this modifier to a `FloatingActionButton` to show or hide it with an animation, typically based on the app's main content scrolling. |
| Scope: `AnimatedVisibilityScope` `open` | `Modifier.animateEnterExit(      enter: EnterTransition,      exit: ExitTransition,      label: String  )`  `animateEnterExit` modifier can be used for any direct or indirect children of `AnimatedVisibility` to create a different enter/exit animation than what's specified in `AnimatedVisibility`. |
| Scope: `LazyItemScope` `open` | `Modifier.animateItem(      fadeInSpec: FiniteAnimationSpec<Float>?,      placementSpec: FiniteAnimationSpec<IntOffset>?,      fadeOutSpec: FiniteAnimationSpec<Float>?  )`  This modifier animates the item appearance (fade in), disappearance (fade out) and placement changes (such as an item reordering). |
| Scope: `LazyGridItemScope` | `Modifier.animateItem(      fadeInSpec: FiniteAnimationSpec<Float>?,      placementSpec: FiniteAnimationSpec<IntOffset>?,      fadeOutSpec: FiniteAnimationSpec<Float>?  )`  This modifier animates the item appearance (fade in), disappearance (fade out) and placement changes (such as an item reordering). |
| Scope: `LazyStaggeredGridItemScope` | `Modifier.animateItem(      fadeInSpec: FiniteAnimationSpec<Float>?,      placementSpec: FiniteAnimationSpec<IntOffset>?,      fadeOutSpec: FiniteAnimationSpec<Float>?  )`  This modifier animates the item appearance (fade in), disappearance (fade out) and placement changes (such as an item reordering). |

## Border

|  |  |
| --- | --- |
| Scope: **Any** | `Modifier.border(border: BorderStroke, shape: Shape)`  Modify element to add border with appearance specified with a `border` and a `shape` and clip it. |
| Scope: **Any** | `Modifier.border(width: Dp, brush: Brush, shape: Shape)`  Modify element to add border with appearance specified with a `width`, a `brush` and a `shape` and clip it. |
| Scope: **Any** | `Modifier.border(width: Dp, color: Color, shape: Shape)`  Modify element to add border with appearance specified with a `width`, a `color` and a `shape` and clip it. |

## Drawing

|  |  |
| --- | --- |
| Scope: **Any** | `Modifier.alpha(alpha: Float)`  Draw content with modified alpha that may be less than 1. |
| Scope: **Any** | `Modifier.background(color: Color, shape: Shape)`  Draws `shape` with a solid `color` behind the content. |
| Scope: **Any** | `Modifier.background(      brush: Brush,      shape: Shape,      alpha: @FloatRange(from = 0.0, to = 1.0) Float  )`  Draws `shape` with `brush` behind the content. |
| Scope: **Any** | `Modifier.clip(shape: Shape)`  Clip the content to `shape`. |
| Scope: **Any** | `Modifier.clipToBounds()`  Clip the content to the bounds of a layer defined at this modifier. |
| Scope: **Any** | `Modifier.drawBehind(onDraw: DrawScope.() -> Unit)`  Draw into a `Canvas` behind the modified content. |
| Scope: **Any** | `Modifier.drawWithCache(onBuildDrawCache: CacheDrawScope.() -> DrawResult)`  Draw into a `DrawScope` with content that is persisted across draw calls as long as the size of the drawing area is the same or any state objects that are read have not changed. |
| Scope: **Any** | `Modifier.drawWithContent(onDraw: ContentDrawScope.() -> Unit)`  Creates a `DrawModifier` that allows the developer to draw before or after the layout's contents. |
| Scope: **Any** | `Modifier.indication(      interactionSource: InteractionSource,      indication: Indication?  )`  Draws visual effects for this component when interactions occur. |
| Scope: **Any** | `Modifier.paint(      painter: Painter,      sizeToIntrinsics: Boolean,      alignment: Alignment,      contentScale: ContentScale,      alpha: Float,      colorFilter: ColorFilter?  )`  Paint the content using `painter`. |
| Scope: **Any** | `Modifier.dropShadow(shape: Shape, block: DropShadowScope.() -> Unit)`  Draws a drop shadow behind the rest of the content with the geometry specified by the given shape and the shadow properties defined the `DropShadowScope`. |
| Scope: **Any** | `Modifier.dropShadow(shape: Shape, shadow: Shadow)`  Draws a drop shadow behind the rest of the content with the geometry specified by the given shape and the shadow properties defined by the `Shadow`. |
| Scope: **Any** | `Modifier.innerShadow(shape: Shape, block: InnerShadowScope.() -> Unit)`  Draws an inner shadow behind the rest of the content with the geometry specified by the given shape and the shadow properties defined the `InnerShadowScope`. |
| Scope: **Any** | `Modifier.innerShadow(shape: Shape, shadow: Shadow)`  Draws an inner shadow on top of the rest of the content with the geometry specified by the given shape and the shadow properties defined by the `Shadow`. |
| Scope: **Any** | `Modifier.shadow(      elevation: Dp,      shape: Shape,      clip: Boolean,      ambientColor: Color,      spotColor: Color  )`  Creates a `graphicsLayer` that draws a shadow. |
| Scope: **Any** | `Modifier.safeDrawingPadding()`  Adds padding to accommodate the `safe drawing` insets. |
| Scope: **Any** | `Modifier.zIndex(zIndex: Float)`  Creates a modifier that controls the drawing order for the children of the same layout parent. |

## Focus

|  |  |
| --- | --- |
| Scope: **Any** | `Modifier.onFocusChanged(onFocusChanged: (FocusState) -> Unit)`  Add this modifier to a component to observe focus state events. |
| Scope: **Any** | `Modifier.onFocusEvent(onFocusEvent: (FocusState) -> Unit)`  Add this modifier to a component to observe focus state events. |
| Scope: **Any** | `Modifier. focusModifier()`  **This function is deprecated.** Replaced by focusTarget |
| Scope: **Any** | `Modifier.focusTarget()`  Add this modifier to a component to make it focusable. |
| Scope: **Any** | `Modifier. focusOrder(focusOrderReceiver: FocusOrder.() -> Unit)`  **This function is deprecated.** Use focusProperties() instead |
| Scope: **Any** | `Modifier. focusOrder(focusRequester: FocusRequester)`  **This function is deprecated.** Use focusRequester() instead |
| Scope: **Any** | `Modifier. focusOrder(      focusRequester: FocusRequester,      focusOrderReceiver: FocusOrder.() -> Unit  )`  **This function is deprecated.** Use focusProperties() and focusRequester() instead |
| Scope: **Any** | `Modifier.focusProperties(scope: FocusProperties.() -> Unit)`  This modifier allows you to specify properties that are accessible to `focusTarget`s further down the modifier chain or on child layout nodes. |
| Scope: **Any** | `Modifier.focusRequester(focusRequester: FocusRequester)`  Add this modifier to a component to request changes to focus. |
| Scope: **Any** | `Modifier.focusRestorer(fallback: FocusRequester)`  This modifier can be used to save and restore focus to a focus group. |
| Scope: **Any** | `@ExperimentalComposeUiApi Modifier. focusRestorer(onRestoreFailed: (() -> FocusRequester)?)`  **This function is deprecated.** Use focusRestorer(FocusRequester) instead |
| Scope: **Any** | `Modifier.focusGroup()`  Creates a focus group or marks this component as a focus group. |
| Scope: **Any** | `Modifier.focusable(      enabled: Boolean,      interactionSource: MutableInteractionSource?  )`  Configure component to be focusable via focus system or accessibility "focus" event. |
| Scope: **Any** | `Modifier.onFocusedBoundsChanged(      onPositioned: (LayoutCoordinates?) -> Unit  )`  Calls `onPositioned` whenever the bounds of the currently-focused area changes. |
| Scope: **Any** | `Modifier.hierarchicalFocusGroup(active: Boolean)`  `hierarchicalFocusGroup` is used to annotate composables in an application, so we can keep track of what is the active part of the composition. |
| Scope: **Any** | `Modifier.requestFocusOnHierarchyActive()`  This Modifier is used in conjunction with `hierarchicalFocusGroup` and will request focus on the following focusable element when needed (i.e. this needs to be before that element in the Modifier chain). |

## Graphics

|  |  |
| --- | --- |
| Scope: **Any** | `Modifier.graphicsLayer(block: GraphicsLayerScope.() -> Unit)`  A `Modifier.Node` that makes content draw into a draw layer. |
| Scope: **Any** | `Modifier.graphicsLayer(      scaleX: Float,      scaleY: Float,      alpha: Float,      translationX: Float,      translationY: Float,      shadowElevation: Float,      rotationX: Float,      rotationY: Float,      rotationZ: Float,      cameraDistance: Float,      transformOrigin: TransformOrigin,      shape: Shape,      clip: Boolean,      renderEffect: RenderEffect?,      ambientShadowColor: Color,      spotShadowColor: Color,      compositingStrategy: CompositingStrategy,      blendMode: BlendMode,      colorFilter: ColorFilter?  )`  A `Modifier.Element` that makes content draw into a draw layer. |
| Scope: **Any** | `Modifier.toolingGraphicsLayer()`  A `Modifier.Element` that adds a draw layer such that tooling can identify an element in the drawn image. |

## Keyboard

|  |  |
| --- | --- |
| Scope: **Any** | `Modifier.onKeyEvent(onKeyEvent: (KeyEvent) -> Boolean)`  Adding this `modifier` to the `modifier` parameter of a component will allow it to intercept hardware key events when it (or one of its children) is focused. |
| Scope: **Any** | `Modifier.onPreviewKeyEvent(onPreviewKeyEvent: (KeyEvent) -> Boolean)`  Adding this `modifier` to the `modifier` parameter of a component will allow it to intercept hardware key events when it (or one of its children) is focused. |

## Layout

|  |  |
| --- | --- |
| Scope: **Any** | `Modifier.layoutId(layoutId: String, tag: String?)`  Alternative to `androidx.compose.ui.layout.layoutId` that enables the use of `tag`. |
| Scope: **Any** | `Modifier.layoutId(layoutId: Any)`  Tag the element with `layoutId` to identify the element within its parent. |
| Scope: **Any** | `Modifier.layout(measure: MeasureScope.(Measurable, Constraints) -> MeasureResult)`  Creates a `LayoutModifier` that allows changing how the wrapped element is measured and laid out. |
| Scope: **Any** | `Modifier.onGloballyPositioned(      onGloballyPositioned: (LayoutCoordinates) -> Unit  )`  Invoke `onGloballyPositioned` with the `LayoutCoordinates` of the element when the global position of the content may have changed. |

## Padding

|  |  |
| --- | --- |
| Scope: **Any** | `Modifier.paddingFrom(alignmentLine: AlignmentLine, before: Dp, after: Dp)`  A `Modifier` that can add padding to position the content according to specified distances from its bounds to an `alignment line`. |
| Scope: **Any** | `Modifier.paddingFrom(      alignmentLine: AlignmentLine,      before: TextUnit,      after: TextUnit  )`  A `Modifier` that can add padding to position the content according to specified distances from its bounds to an `alignment line`. |
| Scope: **Any** | `Modifier.paddingFromBaseline(top: Dp, bottom: Dp)`  A `Modifier` that positions the content in a layout such that the distance from the top of the layout to the `baseline of the first line of text in the content` is `top`, and the distance from the `baseline of the last line of text in the content` to the bottom of the layout is `bottom`. |
| Scope: **Any** | `Modifier.paddingFromBaseline(top: TextUnit, bottom: TextUnit)`  A `Modifier` that positions the content in a layout such that the distance from the top of the layout to the `baseline of the first line of text in the content` is `top`, and the distance from the `baseline of the last line of text in the content` to the bottom of the layout is `bottom`. |
| Scope: **Any** | `Modifier.absolutePadding(left: Dp, top: Dp, right: Dp, bottom: Dp)`  Apply additional space along each edge of the content in `Dp`: `left`, `top`, `right` and `bottom`. |
| Scope: **Any** | `Modifier.padding(all: Dp)`  Apply `all` dp of additional space along each edge of the content, left, top, right and bottom. |
| Scope: **Any** | `Modifier.padding(paddingValues: PaddingValues)`  Apply `PaddingValues` to the component as additional space along each edge of the content's left, top, right and bottom. |
| Scope: **Any** | `Modifier.padding(horizontal: Dp, vertical: Dp)`  Apply `horizontal` dp space along the left and right edges of the content, and `vertical` dp space along the top and bottom edges. |
| Scope: **Any** | `Modifier.padding(start: Dp, top: Dp, end: Dp, bottom: Dp)`  Apply additional space along each edge of the content in `Dp`: `start`, `top`, `end` and `bottom`. |
| Scope: **Any** | `Modifier.captionBarPadding()`  Adds padding to accommodate the `caption bar` insets. |
| Scope: **Any** | `Modifier.displayCutoutPadding()`  Adds padding to accommodate the `display cutout`. |
| Scope: **Any** | `Modifier.imePadding()`  Adds padding to accommodate the `ime` insets. |
| Scope: **Any** | `Modifier.mandatorySystemGesturesPadding()`  Adds padding to accommodate the `mandatory system gestures` insets. |
| Scope: **Any** | `Modifier.navigationBarsPadding()`  Adds padding to accommodate the `navigation bars` insets. |
| Scope: **Any** | `Modifier.safeContentPadding()`  Adds padding to accommodate the `safe content` insets. |
| Scope: **Any** | `Modifier.safeGesturesPadding()`  Adds padding to accommodate the `safe gestures` insets. |
| Scope: **Any** | `Modifier.statusBarsPadding()`  Adds padding to accommodate the `status bars` insets. |
| Scope: **Any** | `Modifier.systemBarsPadding()`  Adds padding to accommodate the `system bars` insets. |
| Scope: **Any** | `Modifier.systemGesturesPadding()`  Adds padding to accommodate the `system gestures` insets. |
| Scope: **Any** | `Modifier.waterfallPadding()`  Adds padding to accommodate the `waterfall` insets. |
| Scope: **Any** | `Modifier.windowInsetsPadding(insets: WindowInsets)`  Adds padding so that the content doesn't enter `insets` space. |

## Pointer

|  |  |
| --- | --- |
| Scope: **Any** | `Modifier.onIndirectPointerGesture(      enabled: Boolean,      onClick: () -> Unit,      onSwipeForward: () -> Unit,      onSwipeBackward: () -> Unit  )`  A `Modifier` that listens for and detects high-level gestures from an `IndirectPointerEvent` source. |
| Scope: **Any** | `Modifier.pointerHoverIcon(      icon: PointerIcon,      overrideDescendants: Boolean  )`  Modifier that lets a developer define a pointer icon to display when the cursor is hovered over the element. |
| Scope: **Any** | `Modifier.pointerInteropFilter(      requestDisallowInterceptTouchEvent: RequestDisallowInterceptTouchEvent?,      onTouchEvent: (MotionEvent) -> Boolean  )`  A special PointerInputModifier that provides access to the underlying `MotionEvent`s originally dispatched to Compose. |
| Scope: **Any** | `Modifier. pointerInput(block: suspend PointerInputScope.() -> Unit)`  **This function is deprecated.** Modifier.pointerInput must provide one or more 'key' parameters that define the identity of the modifier and determine when its previous input processing coroutine should be cancelled and a new effect launched for the new key. |
| Scope: **Any** | `Modifier.pointerInput(key1: Any?, block: PointerInputEventHandler)`  Create a modifier for processing pointer input within the region of the modified element. |
| Scope: **Any** | `Modifier.pointerInput(vararg keys: Any?, block: PointerInputEventHandler)`  Create a modifier for processing pointer input within the region of the modified element. |
| Scope: **Any** | `Modifier.pointerInput(      key1: Any?,      key2: Any?,      block: PointerInputEventHandler  )`  Create a modifier for processing pointer input within the region of the modified element. |

## Position

|  |  |
| --- | --- |
| Scope: **Any** | `Modifier.absoluteOffset(offset: Density.() -> IntOffset)`  Offset the content by `offset` px. |
| Scope: **Any** | `Modifier.absoluteOffset(x: Dp, y: Dp)`  Offset the content by (`x` dp, `y` dp). |
| Scope: **Any** | `Modifier.offset(offset: Density.() -> IntOffset)`  Offset the content by `offset` px. |
| Scope: **Any** | `Modifier.offset(x: Dp, y: Dp)`  Offset the content by (`x` dp, `y` dp). |
| Scope: `TabRowDefaults` | `Modifier.tabIndicatorOffset(currentTabPosition: TabPosition)`  `Modifier` that takes up all the available width inside the `TabRow`, and then animates the offset of the indicator it is applied to, depending on the `currentTabPosition`. |
| Scope: `TabRowDefaults` | `Modifier. tabIndicatorOffset(currentTabPosition: TabPosition)`  **This function is deprecated.** Solely for use alongside deprecated TabRowDefaults.Indicator method. |

## Semantics

|  |  |
| --- | --- |
| Scope: **Any** | `Modifier.progressSemantics()`  Contains the `semantics` required for an indeterminate progress indicator, that represents the fact of the in-progress operation. |
| Scope: **Any** | `Modifier.progressSemantics(      value: Float,      valueRange: ClosedFloatingPointRange<Float>,      steps: @IntRange(from = 0) Int  )`  Contains the `semantics` required for a determinate progress indicator or the progress part of a slider, that represents progress within `valueRange`. |
| Scope: **Any** | `Modifier.rangeSemantics(      value: Float,      enabled: Boolean,      onValueChange: (Float) -> Unit,      valueRange: ClosedFloatingPointRange<Float>,      steps: Int  )`  Modifier to add semantics signifying progress of the Stepper/Slider. |
| Scope: **Any** | `Modifier.clearAndSetSemantics(properties: SemanticsPropertyReceiver.() -> Unit)`  Clears the semantics of all the descendant nodes and sets new semantics. |
| Scope: **Any** | `Modifier.semantics(mergeDescendants: Boolean, properties: SemanticsPropertyReceiver.() -> Unit)`  Add semantics key/value pairs to the layout node, for use in testing, accessibility, etc. |

## Scroll

|  |  |
| --- | --- |
| Scope: **Any** | `Modifier.clipScrollableContainer(orientation: Orientation)`  Clips bounds of scrollable container on main axis while leaving space for background effects (like shadows) on cross axis. |
| Scope: **Any** | `Modifier.nestedScroll(      connection: NestedScrollConnection,      dispatcher: NestedScrollDispatcher?  )`  Modify element to make it participate in the nested scrolling hierarchy. |
| Scope: **Any** | `Modifier.overscroll(overscrollEffect: OverscrollEffect?)`  Renders overscroll from the provided `overscrollEffect`. |
| Scope: **Any** | `Modifier.onPreRotaryScrollEvent(      onPreRotaryScrollEvent: (RotaryScrollEvent) -> Boolean  )`  Adding this `modifier` to the `modifier` parameter of a component will allow it to intercept `RotaryScrollEvent`s if it (or one of its children) is focused. |
| Scope: **Any** | `Modifier.onRotaryScrollEvent(      onRotaryScrollEvent: (RotaryScrollEvent) -> Boolean  )`  Adding this `modifier` to the `modifier` parameter of a component will allow it to intercept `RotaryScrollEvent`s if it (or one of its children) is focused. |
| Scope: **Any** | `Modifier.rotaryScrollable(      behavior: RotaryScrollableBehavior,      focusRequester: FocusRequester,      reverseDirection: Boolean,      overscrollEffect: OverscrollEffect?  )`  A modifier which connects rotary events with scrollable containers such as Column, LazyList and others. |
| Scope: **Any** | `Modifier.scrollAway(      scrollInfoProvider: ScrollInfoProvider,      screenStage: () -> ScreenStage  )`  Scroll an item vertically in/out of view based on scroll state provided by a scrolling list. |
| Scope: **Any** | `Modifier.scrollAway(scrollState: ScrollState, offset: Dp)`  Scroll an item vertically in/out of view based on a `ScrollState`. |
| Scope: **Any** | `Modifier.scrollAway(      scrollState: LazyListState,      itemIndex: Int,      offset: Dp  )`  Scroll an item vertically in/out of view based on a `LazyListState`. |
| Scope: **Any** | `Modifier.scrollAway(      scrollState: ScalingLazyListState,      itemIndex: Int,      offset: Dp  )`  Scroll an item vertically in/out of view based on a `ScalingLazyListState`. |
| Scope: **Any** | `Modifier. scrollAway(      scrollState: ScalingLazyListState,      itemIndex: Int,      offset: Dp  )`  **This function is deprecated.** This overload is provided for backwards compatibility with Compose for Wear OS 1.1.A newer overload is available which uses ScalingLazyListState from wear.compose.foundation.lazy package |
| Scope: **Any** | `Modifier.horizontalScroll(      state: ScrollState,      enabled: Boolean,      flingBehavior: FlingBehavior?,      reverseScrolling: Boolean  )`  Modify element to allow to scroll horizontally when width of the content is bigger than max constraints allow. |
| Scope: **Any** | `Modifier.horizontalScroll(      state: ScrollState,      overscrollEffect: OverscrollEffect?,      enabled: Boolean,      flingBehavior: FlingBehavior?,      reverseScrolling: Boolean  )`  Modify element to allow to scroll horizontally when width of the content is bigger than max constraints allow. |
| Scope: **Any** | `Modifier.verticalScroll(      state: ScrollState,      enabled: Boolean,      flingBehavior: FlingBehavior?,      reverseScrolling: Boolean  )`  Modify element to allow to scroll vertically when height of the content is bigger than max constraints allow. |
| Scope: **Any** | `Modifier.verticalScroll(      state: ScrollState,      overscrollEffect: OverscrollEffect?,      enabled: Boolean,      flingBehavior: FlingBehavior?,      reverseScrolling: Boolean  )`  Modify element to allow to scroll vertically when height of the content is bigger than max constraints allow. |
| Scope: **Any** | `Modifier.scrollable2D(      state: Scrollable2DState,      enabled: Boolean,      overscrollEffect: OverscrollEffect?,      flingBehavior: FlingBehavior?,      interactionSource: MutableInteractionSource?  )`  Configure touch scrolling and flinging for the UI element in both XY orientations. |
| Scope: **Any** | `Modifier.scrollableArea(      state: ScrollableState,      orientation: Orientation,      enabled: Boolean,      reverseScrolling: Boolean,      flingBehavior: FlingBehavior?,      interactionSource: MutableInteractionSource?,      bringIntoViewSpec: BringIntoViewSpec?  )`  Configure a component to act as a scrollable area. |
| Scope: **Any** | `Modifier.scrollableArea(      state: ScrollableState,      orientation: Orientation,      overscrollEffect: OverscrollEffect?,      enabled: Boolean,      reverseScrolling: Boolean,      flingBehavior: FlingBehavior?,      interactionSource: MutableInteractionSource?,      bringIntoViewSpec: BringIntoViewSpec?  )`  Configure a component to act as a scrollable area. |
| Scope: **Any** | `Modifier.scrollable(      state: ScrollableState,      orientation: Orientation,      enabled: Boolean,      reverseDirection: Boolean,      flingBehavior: FlingBehavior?,      interactionSource: MutableInteractionSource?  )`  Configure touch scrolling and flinging for the UI element in a single `Orientation`. |
| Scope: **Any** | `Modifier.scrollable(      state: ScrollableState,      orientation: Orientation,      overscrollEffect: OverscrollEffect?,      enabled: Boolean,      reverseDirection: Boolean,      flingBehavior: FlingBehavior?,      interactionSource: MutableInteractionSource?,      bringIntoViewSpec: BringIntoViewSpec?  )`  Configure touch scrolling and flinging for the UI element in a single `Orientation`. |
| Scope: **Any** | `@ExperimentalLayoutApi Modifier.imeNestedScroll()`  Controls the soft keyboard as a nested scrolling on Android `R` and later. |

## Size

|  |  |
| --- | --- |
| Scope: **Any** | `Modifier.animateContentSize(      animationSpec: FiniteAnimationSpec<IntSize>,      finishedListener: ((initialValue: IntSize, targetValue: IntSize) -> Unit)?  )`  This modifier animates its own size when its child modifier (or the child composable if it is already at the tail of the chain) changes size. |
| Scope: **Any** | `Modifier.animateContentSize(      animationSpec: FiniteAnimationSpec<IntSize>,      alignment: Alignment,      finishedListener: ((initialValue: IntSize, targetValue: IntSize) -> Unit)?  )`  This modifier animates its own size when its child modifier (or the child composable if it is already at the tail of the chain) changes size. |
| Scope: **Any** | `Modifier.aspectRatio(      ratio: @FloatRange(from = 0.0, fromInclusive = false) Float,      matchHeightConstraintsFirst: Boolean  )`  Attempts to size the content to match a specified aspect ratio by trying to match one of the incoming constraints in the following order: `Constraints.maxWidth`, `Constraints.maxHeight`, `Constraints.minWidth`, `Constraints.minHeight` if `matchHeightConstraintsFirst` is `false` (which is the default), or `Constraints.maxHeight`, `Constraints.maxWidth`, `Constraints.minHeight`, `Constraints.minWidth` if `matchHeightConstraintsFirst` is `true`. |
| Scope: **Any** | `Modifier.minimumInteractiveComponentSize()`  Reserves at least 48.dp in size to disambiguate touch interactions if the element would measure smaller. |
| Scope: **Any** | `Modifier.minimumInteractiveComponentSize()`  Reserves at least 48.dp in size to disambiguate touch interactions if the element would measure smaller. |
| Scope: **Any** | `Modifier.minimumInteractiveComponentSize()`  Reserves at least 48.dp in size to disambiguate touch interactions if the element would measure smaller. |
| Scope: **Any** | `Modifier.height(intrinsicSize: IntrinsicSize)`  Declare the preferred height of the content to be the same as the min or max intrinsic height of the content. |
| Scope: **Any** | `Modifier.requiredHeight(intrinsicSize: IntrinsicSize)`  Declare the height of the content to be exactly the same as the min or max intrinsic height of the content. |
| Scope: **Any** | `Modifier.requiredWidth(intrinsicSize: IntrinsicSize)`  Declare the width of the content to be exactly the same as the min or max intrinsic width of the content. |
| Scope: **Any** | `Modifier.width(intrinsicSize: IntrinsicSize)`  Declare the preferred width of the content to be the same as the min or max intrinsic width of the content. |
| Scope: **Any** | `Modifier.onSizeChanged(onSizeChanged: (IntSize) -> Unit)`  Invoked with the size of the modified Compose UI element when the element is first measured or when the size of the element changes. |
| Scope: **Any** | `Modifier.defaultMinSize(minWidth: Dp, minHeight: Dp)`  Constrain the size of the wrapped layout only when it would be otherwise unconstrained: the `minWidth` and `minHeight` constraints are only applied when the incoming corresponding constraint is `0`. |
| Scope: **Any** | `Modifier.fillMaxHeight(fraction: @FloatRange(from = 0.0, to = 1.0) Float)`  Have the content fill (possibly only partially) the `Constraints.maxHeight` of the incoming measurement constraints, by setting the `minimum height` and the `maximum height` to be equal to the `maximum height` multiplied by `fraction`. |
| Scope: **Any** | `Modifier.fillMaxSize(fraction: @FloatRange(from = 0.0, to = 1.0) Float)`  Have the content fill (possibly only partially) the `Constraints.maxWidth` and `Constraints.maxHeight` of the incoming measurement constraints, by setting the `minimum width` and the `maximum width` to be equal to the `maximum width` multiplied by `fraction`, as well as the `minimum height` and the `maximum height` to be equal to the `maximum height` multiplied by `fraction`. |
| Scope: **Any** | `Modifier.fillMaxWidth(fraction: @FloatRange(from = 0.0, to = 1.0) Float)`  Have the content fill (possibly only partially) the `Constraints.maxWidth` of the incoming measurement constraints, by setting the `minimum width` and the `maximum width` to be equal to the `maximum width` multiplied by `fraction`. |
| Scope: **Any** | `Modifier.height(height: Dp)`  Declare the preferred height of the content to be exactly `height`dp. |
| Scope: **Any** | `Modifier.heightIn(min: Dp, max: Dp)`  Constrain the height of the content to be between `min`dp and `max`dp as permitted by the incoming measurement `Constraints`. |
| Scope: **Any** | `Modifier.requiredHeight(height: Dp)`  Declare the height of the content to be exactly `height`dp. |
| Scope: **Any** | `Modifier.requiredHeightIn(min: Dp, max: Dp)`  Constrain the height of the content to be between `min`dp and `max`dp. |
| Scope: **Any** | `Modifier.requiredSize(size: Dp)`  Declare the size of the content to be exactly `size`dp width and height. |
| Scope: **Any** | `Modifier.requiredSize(size: DpSize)`  Declare the size of the content to be exactly `size`. |
| Scope: **Any** | `Modifier.requiredSize(width: Dp, height: Dp)`  Declare the size of the content to be exactly `width`dp and `height`dp. |
| Scope: **Any** | `Modifier.requiredSizeIn(      minWidth: Dp,      minHeight: Dp,      maxWidth: Dp,      maxHeight: Dp  )`  Constrain the width of the content to be between `minWidth`dp and `maxWidth`dp, and the height of the content to be between `minHeight`dp and `maxHeight`dp. |
| Scope: **Any** | `Modifier.requiredWidth(width: Dp)`  Declare the width of the content to be exactly `width`dp. |
| Scope: **Any** | `Modifier.requiredWidthIn(min: Dp, max: Dp)`  Constrain the width of the content to be between `min`dp and `max`dp. |
| Scope: **Any** | `Modifier.size(size: Dp)`  Declare the preferred size of the content to be exactly `size`dp square. |
| Scope: **Any** | `Modifier.size(size: DpSize)`  Declare the preferred size of the content to be exactly `size`. |
| Scope: **Any** | `Modifier.size(width: Dp, height: Dp)`  Declare the preferred size of the content to be exactly `width`dp by `height`dp. |
| Scope: **Any** | `Modifier.sizeIn(minWidth: Dp, minHeight: Dp, maxWidth: Dp, maxHeight: Dp)`  Constrain the width of the content to be between `minWidth`dp and `maxWidth`dp and the height of the content to be between `minHeight`dp and `maxHeight`dp as permitted by the incoming measurement `Constraints`. |
| Scope: **Any** | `Modifier.width(width: Dp)`  Declare the preferred width of the content to be exactly `width`dp. |
| Scope: **Any** | `Modifier.widthIn(min: Dp, max: Dp)`  Constrain the width of the content to be between `min`dp and `max`dp as permitted by the incoming measurement `Constraints`. |
| Scope: **Any** | `Modifier.wrapContentHeight(      align: Alignment.Vertical,      unbounded: Boolean  )`  Allow the content to measure at its desired height without regard for the incoming measurement `minimum height constraint`, and, if `unbounded` is true, also without regard for the incoming measurement `maximum height constraint`. |
| Scope: **Any** | `Modifier.wrapContentSize(align: Alignment, unbounded: Boolean)`  Allow the content to measure at its desired size without regard for the incoming measurement `minimum width` or `minimum height` constraints, and, if `unbounded` is true, also without regard for the incoming maximum constraints. |
| Scope: **Any** | `Modifier.wrapContentWidth(      align: Alignment.Horizontal,      unbounded: Boolean  )`  Allow the content to measure at its desired width without regard for the incoming measurement `minimum width constraint`, and, if `unbounded` is true, also without regard for the incoming measurement `maximum width constraint`. |
| Scope: **Any** | `Modifier.touchTargetAwareSize(size: Dp)`  Modifier to set both the size and recommended touch target for `IconButton` and TextButton. |
| Scope: **Any** | `Modifier.transformedHeight(      scope: TransformingLazyColumnItemScope,      transformationSpec: TransformationSpec  )`  Convenience modifier to calculate transformed height using `TransformationSpec`. |
| Scope: **Any** | `Modifier.windowInsetsBottomHeight(insets: WindowInsets)`  Sets the height to that of `insets` at the `bottom` of the screen. |
| Scope: **Any** | `Modifier.windowInsetsEndWidth(insets: WindowInsets)`  Sets the width to that of `insets` at the `end` of the screen, using either `left` or `right`, depending on the `LayoutDirection`. |
| Scope: **Any** | `Modifier.windowInsetsStartWidth(insets: WindowInsets)`  Sets the width to that of `insets` at the `start` of the screen, using either `left` or `right`, depending on the `LayoutDirection`. |
| Scope: **Any** | `Modifier.windowInsetsTopHeight(insets: WindowInsets)`  Sets the height to that of `insets` at the `top` of the screen. |
| Scope: **Any** | `@UnstableApi  @Composable Modifier.resizeWithContentScale(      contentScale: ContentScale,      sourceSizeDp: Size?,      density: Density  )`  Attempts to size the original content rectangle to be inscribed into a destination by applying a specified `ContentScale` type. |
| Scope: `SharedTransitionScope` | `Modifier.skipToLookaheadSize(enabled: () -> Boolean)`  `skipToLookaheadSize` enables a layout to measure its child with the lookahead constraints, therefore laying out the child as if the transition has finished. |
| Scope: `RowScope` | `Modifier.weight(      weight: @FloatRange(from = 0.0, fromInclusive = false) Float,      fill: Boolean  )`  Size the element's width proportional to its `weight` relative to other weighted sibling elements in the `Row`. |
| Scope: `ColumnScope` | `Modifier.weight(      weight: @FloatRange(from = 0.0, fromInclusive = false) Float,      fill: Boolean  )`  Size the element's height proportional to its `weight` relative to other weighted sibling elements in the `Column`. |
| Scope: `FlowRowScope` | `@ExperimentalLayoutApi Modifier.fillMaxRowHeight(fraction: @FloatRange(from = 0.0, to = 1.0) Float)`  Have the item fill (possibly only partially) the max height of the tallest item in the row it was placed in, within the `FlowRow`. |
| Scope: `FlowColumnScope` | `@ExperimentalLayoutApi Modifier.fillMaxColumnWidth(      fraction: @FloatRange(from = 0.0, to = 1.0) Float  )`  Have the item fill (possibly only partially) the max width of the widest item in the column it was placed in, within the `FlowColumn`. |
| Scope: `BoxScope` | `Modifier.matchParentSize()`  Size the element to match the size of the `Box` after all other content elements have been measured. |
| Scope: `LazyItemScope` | `Modifier.fillParentMaxHeight(      fraction: @FloatRange(from = 0.0, to = 1.0) Float  )`  Have the content fill the `Constraints.maxHeight` of the incoming measurement constraints by setting the `minimum height` to be equal to the `maximum height` multiplied by `fraction`. |
| Scope: `LazyItemScope` | `Modifier.fillParentMaxSize(      fraction: @FloatRange(from = 0.0, to = 1.0) Float  )`  Have the content fill the `Constraints.maxWidth` and `Constraints.maxHeight` of the parent measurement constraints by setting the `minimum width` to be equal to the `maximum width` multiplied by `fraction` and the `minimum height` to be equal to the `maximum height` multiplied by `fraction`. |
| Scope: `LazyItemScope` | `Modifier.fillParentMaxWidth(      fraction: @FloatRange(from = 0.0, to = 1.0) Float  )`  Have the content fill the `Constraints.maxWidth` of the parent measurement constraints by setting the `minimum width` to be equal to the `maximum width` multiplied by `fraction`. |
| Scope: `ExposedDropdownMenuBoxScope` `abstract` | `Modifier.exposedDropdownSize(matchTextFieldWidth: Boolean)`  Modifier which should be applied to an `ExposedDropdownMenu` placed inside the scope. |
| Scope: `ExposedDropdownMenuBoxScope` `abstract` | `Modifier.exposedDropdownSize(matchAnchorWidth: Boolean)`  Modifier which should be applied to a menu placed inside the `ExposedDropdownMenuBoxScope`. |
| Scope: `PaneScaffoldScope` | `Modifier.preferredHeight(height: Dp)`  This modifier specifies the preferred height for a pane in `Dp`s, and the pane scaffold implementation will try its best to respect this height when the associated pane is rendered as a reflowed or a levitated pane. |
| Scope: `PaneScaffoldScope` | `Modifier.preferredHeight(      proportion: @FloatRange(from = 0.0, to = 1.0) Float  )`  This modifier specifies the preferred height for a pane as a proportion of the overall scaffold height. |
| Scope: `PaneScaffoldScope` | `Modifier.preferredWidth(proportion: @FloatRange(from = 0.0, to = 1.0) Float)`  This modifier specifies the preferred width for a pane as a proportion of the overall scaffold width. |
| Scope: `PaneScaffoldScope` | `Modifier.preferredWidth(width: Dp)`  This modifier specifies the preferred width for a pane in `Dp`s, and the pane scaffold implementation will try its best to respect this width when the associated pane is rendered as a fixed pane, i.e., a pane that are not stretching to fill the remaining spaces. |

## Testing

|  |  |
| --- | --- |
| Scope: **Any** | `Modifier.testTag(tag: String)`  Applies a tag to allow modified element to be found in tests. |

## Transformations

|  |  |
| --- | --- |
| Scope: **Any** | `Modifier.rotate(degrees: Float)`  Sets the degrees the view is rotated around the center of the composable. |
| Scope: **Any** | `Modifier.scale(scale: Float)`  Scale the contents of both the horizontal and vertical axis uniformly by the same scale factor. |
| Scope: **Any** | `Modifier.scale(scaleX: Float, scaleY: Float)`  Scale the contents of the composable by the following scale factors along the horizontal and vertical axis respectively. |
| Scope: **Any** | `Modifier.transformable(      state: TransformableState,      lockRotationOnZoomPan: Boolean,      enabled: Boolean  )`  Enable transformation gestures of the modified UI element. |
| Scope: **Any** | `Modifier.transformable(      state: TransformableState,      canPan: (Offset) -> Boolean,      lockRotationOnZoomPan: Boolean,      enabled: Boolean  )`  Enable transformation gestures of the modified UI element. |

## Other

|  |  |
| --- | --- |
| Scope: **Any** | `@ExperimentalFoundationApi Modifier. dragAndDropSource(block: suspend DragAndDropSourceScope.() -> Unit)`  **This function is deprecated.** Replaced by overload with a callback for obtain a transfer data,start detection is performed by Compose itself |
| Scope: **Any** | `Modifier.contentType(contentType: ContentType)`  Set autofill hint with `contentType`. |
| Scope: **Any** | `Modifier.basicMarquee(      iterations: Int,      animationMode: MarqueeAnimationMode,      repeatDelayMillis: Int,      initialDelayMillis: Int,      spacing: MarqueeSpacing,      velocity: Dp  )`  Applies an animated marquee effect to the modified content if it's too wide to fit in the available space. |
| Scope: **Any** | `Modifier.edgeSwipeToDismiss(      swipeToDismissBoxState: SwipeToDismissBoxState,      edgeWidth: Dp  )`  Handles swipe to dismiss from the edge of the viewport. |
| Scope: **Any** | `Modifier.blur(radius: Dp, edgeTreatment: BlurredEdgeTreatment)`  Draw content blurred with the specified radii. |
| Scope: **Any** | `Modifier.blur(      radiusX: Dp,      radiusY: Dp,      edgeTreatment: BlurredEdgeTreatment  )`  Draw content blurred with the specified radii. |
| Scope: **Any** | `Modifier.bringIntoViewRequester(      bringIntoViewRequester: BringIntoViewRequester  )`  Modifier that can be used to send `bringIntoView` requests. |
| Scope: **Any** | `Modifier. bringIntoViewResponder(responder: BringIntoViewResponder)`  **This function is deprecated.** Use BringIntoViewModifierNode instead |
| Scope: **Any** | `Modifier.composed(      inspectorInfo: InspectorInfo.() -> Unit,      factory: @Composable Modifier.() -> Modifier  )`  Declare a just-in-time composition of a `Modifier` that will be composed for each element it modifies. |
| Scope: **Any** | `Modifier.composed(      fullyQualifiedName: String,      key1: Any?,      inspectorInfo: InspectorInfo.() -> Unit,      factory: @Composable Modifier.() -> Modifier  )`  Declare a just-in-time composition of a `Modifier` that will be composed for each element it modifies. |
| Scope: **Any** | `Modifier.composed(      fullyQualifiedName: String,      vararg keys: Any?,      inspectorInfo: InspectorInfo.() -> Unit,      factory: @Composable Modifier.() -> Modifier  )`  Declare a just-in-time composition of a `Modifier` that will be composed for each element it modifies. |
| Scope: **Any** | `Modifier.composed(      fullyQualifiedName: String,      key1: Any?,      key2: Any?,      inspectorInfo: InspectorInfo.() -> Unit,      factory: @Composable Modifier.() -> Modifier  )`  Declare a just-in-time composition of a `Modifier` that will be composed for each element it modifies. |
| Scope: **Any** | `Modifier.composed(      fullyQualifiedName: String,      key1: Any?,      key2: Any?,      key3: Any?,      inspectorInfo: InspectorInfo.() -> Unit,      factory: @Composable Modifier.() -> Modifier  )`  Declare a just-in-time composition of a `Modifier` that will be composed for each element it modifies. |
| Scope: **Any** | `Modifier.contentColorProvider(contentColor: Color)`  Provides `contentColor` for text and iconography to consume. |
| Scope: **Any** | `Modifier.depth(depth: Depth?, shape: Shape)`  Renders shadows for the provided `depth`. |
| Scope: **Any** | `Modifier.dragAndDropSource(      transferData: (Offset) -> DragAndDropTransferData?  )`  A `Modifier` that allows an element it is applied to be treated like a source for drag and drop operations. |
| Scope: **Any** | `@ExperimentalFoundationApi Modifier. dragAndDropSource(      drawDragDecoration: DrawScope.() -> Unit,      block: suspend DragAndDropSourceScope.() -> Unit  )`  **This function is deprecated.** Replaced by overload with a callback for obtain a transfer data,start detection is performed by Compose itself |
| Scope: **Any** | `Modifier.dragAndDropSource(      drawDragDecoration: DrawScope.() -> Unit,      transferData: (Offset) -> DragAndDropTransferData?  )`  A `Modifier` that allows an element it is applied to be treated like a source for drag and drop operations. |
| Scope: **Any** | `Modifier.dragAndDropTarget(      shouldStartDragAndDrop: (startEvent: DragAndDropEvent) -> Boolean,      target: DragAndDropTarget  )`  A modifier that allows for receiving from a drag and drop gesture. |
| Scope: **Any** | `Modifier. excludeFromSystemGesture()`  **This function is deprecated.** Use systemGestureExclusion |
| Scope: **Any** | `Modifier. excludeFromSystemGesture(      exclusion: (LayoutCoordinates) -> Rect  )`  **This function is deprecated.** Use systemGestureExclusion |
| Scope: **Any** | `Modifier.preferredFrameRate(frameRateCategory: FrameRateCategory)`  Set a requested frame rate on Composable |
| Scope: **Any** | `Modifier.preferredFrameRate(      frameRate: @FloatRange(from = 0.0, to = 360.0) Float  )`  Set a requested frame rate on Composable |
| Scope: **Any** | `Modifier.handwritingDetector(callback: () -> Unit)`  Configures an element to act as a handwriting detector which detects stylus handwriting and delegates handling of the recognised text to another element. |
| Scope: **Any** | `Modifier.handwritingHandler()`  Configures an element to act as a stylus handwriting handler which can handle text input from a handwriting session which was triggered by stylus handwriting on a handwriting detector. |
| Scope: **Any** | `Modifier.hoverable(      interactionSource: MutableInteractionSource,      enabled: Boolean  )`  Configure component to be hoverable via pointer enter/exit events. |
| Scope: **Any** `inline` | `Modifier. inspectable(      noinline inspectorInfo: InspectorInfo.() -> Unit,      factory: Modifier.() -> Modifier  )`  **This function is deprecated.** This API will create more invalidations of your modifier than necessary, so it's use is discouraged. |
| Scope: **Any** | `Modifier.keepScreenOn()`  A modifier that keeps the device screen on as long as it is part of the composition on supported platforms. |
| Scope: **Any** | `Modifier.layoutBounds(holder: LayoutBoundsHolder)`  This will map the `RelativeLayoutBounds` of the modifier into the provided `LayoutBoundsHolder`. |
| Scope: **Any** | `Modifier.approachLayout(      isMeasurementApproachInProgress: (lookaheadSize: IntSize) -> Boolean,      isPlacementApproachInProgress: Placeable.PlacementScope.(lookaheadCoordinates: LayoutCoordinates) -> Boolean,      approachMeasure: ApproachMeasureScope.(measurable: Measurable, constraints: Constraints) -> MeasureResult  )`  Creates an approach layout intended to help gradually approach the destination layout calculated in the lookahead pass. |
| Scope: **Any** | `Modifier.magnifier(      sourceCenter: Density.() -> Offset,      magnifierCenter: (Density.() -> Offset)?,      onSizeChanged: ((DpSize) -> Unit)?,      zoom: Float,      size: DpSize,      cornerRadius: Dp,      elevation: Dp,      clip: Boolean  )`  Shows a `Magnifier` widget that shows an enlarged version of the content at `sourceCenter` relative to the current layout node. |
| Scope: **Any** | `Modifier.modifierLocalConsumer(consumer: ModifierLocalReadScope.() -> Unit)`  A Modifier that can be used to consume `ModifierLocal`s that were provided by other modifiers to the left of this modifier, or above this modifier in the layout tree. |
| Scope: **Any** | `<T : Any?> Modifier.modifierLocalProvider(      key: ProvidableModifierLocal<T>,      value: () -> T  )`  A Modifier that can be used to provide `ModifierLocal`s that can be read by other modifiers to the right of this modifier, or modifiers that are children of the layout node that this modifier is attached to. |
| Scope: **Any** | `Modifier.onFirstVisible(      minDurationMs: @IntRange(from = 0) Long,      minFractionVisible: @FloatRange(from = 0.0, to = 1.0) Float,      viewportBounds: LayoutBoundsHolder?,      callback: () -> Unit  )`  Registers a callback to monitor when the node is first inside of the viewport of the window or not. |
| Scope: **Any** | `Modifier.onLayoutRectChanged(      throttleMillis: Long,      debounceMillis: Long,      callback: (RelativeLayoutBounds) -> Unit  )`  Invokes `callback` with the position of this layout node relative to the coordinate system of the root of the composition, as well as in screen coordinates and window coordinates. |
| Scope: **Any** | `Modifier.onPlaced(onPlaced: (LayoutCoordinates) -> Unit)`  Invoke `onPlaced` after the parent `LayoutModifier` and parent layout has been placed and before child `LayoutModifier` is placed. |
| Scope: **Any** | `Modifier.onVisibilityChanged(      minDurationMs: @IntRange(from = 0) Long,      minFractionVisible: @FloatRange(from = 0.0, to = 1.0) Float,      viewportBounds: LayoutBoundsHolder?,      callback: (Boolean) -> Unit  )`  Registers a callback to monitor whether or not the node is inside of the viewport of the window or not. |
| Scope: **Any** | `@ExperimentalWearMaterialApi  @Composable Modifier.placeholder(      placeholderState: PlaceholderState,      shape: Shape,      color: Color  )`  Draws a placeholder shape over the top of a composable and animates a wipe off effect to remove the placeholder. |
| Scope: **Any** | `@Composable Modifier.placeholder(      placeholderState: PlaceholderState,      shape: Shape,      color: Color  )`  Modifier.placeholder draws a skeleton shape over a component, for situations when no provisional content (such as cached data) is available. |
| Scope: **Any** | `@ExperimentalWearMaterialApi  @Composable Modifier.placeholderShimmer(      placeholderState: PlaceholderState,      shape: Shape,      color: Color  )`  Modifier to draw a placeholder shimmer over a component. |
| Scope: **Any** | `@Composable Modifier.placeholderShimmer(      placeholderState: PlaceholderState,      shape: Shape,      color: Color  )`  Modifier.placeholderShimmer draws a periodic shimmer over content, indicating to the user that contents are loading or potentially out of date. |
| Scope: **Any** | `Modifier.stylusHoverIcon(      icon: PointerIcon,      overrideDescendants: Boolean,      touchBoundsExpansion: DpTouchBoundsExpansion?  )`  Modifier that lets a developer define a pointer icon to display when a stylus is hovered over the element. |
| Scope: **Any** | `Modifier.motionEventSpy(watcher: (motionEvent: MotionEvent) -> Unit)`  Calls `watcher` with each `MotionEvent` that the layout area or any child `pointerInput` receives. |
| Scope: **Any** | `Modifier.preferKeepClear()`  Mark the layout rectangle as preferring to stay clear of floating windows. |
| Scope: **Any** | `Modifier.preferKeepClear(rectProvider: (LayoutCoordinates) -> Rect)`  Mark a rectangle within the local layout coordinates preferring to stay clear of floating windows. |
| Scope: **Any** | `@ExperimentalMaterialApi Modifier.pullRefreshIndicatorTransform(      state: PullRefreshState,      scale: Boolean  )`  A modifier for translating the position and scaling the size of a pull-to-refresh indicator based on the given `PullRefreshState`. |
| Scope: **Any** | `@ExperimentalMaterialApi Modifier.pullRefresh(state: PullRefreshState, enabled: Boolean)`  A nested scroll modifier that provides scroll events to `state`. |
| Scope: **Any** | `@ExperimentalMaterialApi Modifier.pullRefresh(      onPull: (pullDelta: Float) -> Float,      onRelease: suspend (flingVelocity: Float) -> Float,      enabled: Boolean  )`  A nested scroll modifier that provides `onPull` and `onRelease` callbacks to aid building custom pull refresh components. |
| Scope: **Any** | `Modifier.pullToRefresh(      isRefreshing: Boolean,      state: PullToRefreshState,      enabled: Boolean,      threshold: Dp,      onRefresh: () -> Unit  )`  A Modifier that adds nested scroll to a container to support a pull-to-refresh gesture. |
| Scope: **Any** | `@ExperimentalFoundationApi Modifier.contentReceiver(      receiveContentListener: ReceiveContentListener  )`  Configures the current node and any children nodes as a Content Receiver. |
| Scope: **Any** | `Modifier.fitInside(rulers: RectRulers)`  Fits the contents within `rulers`. |
| Scope: **Any** | `Modifier.fitOutside(rulers: RectRulers)`  If one of the `Ruler`s in `rulers` has a value within the bounds of the Layout, this sizes the content to that `Ruler` and the edge. |
| Scope: **Any** | `Modifier.sensitiveContent(isContentSensitive: Boolean)`  This modifier hints that the composable renders sensitive content (i.e. username, password, credit card etc) on the screen, and the content should be protected during screen share in supported environments. |
| Scope: **Any** | `Modifier.onInterceptKeyBeforeSoftKeyboard(      onInterceptKeyBeforeSoftKeyboard: (KeyEvent) -> Boolean  )`  Adding this `modifier` to the `modifier` parameter of a component will allow it to intercept hardware key events before they are sent to the software keyboard. |
| Scope: **Any** | `Modifier.onPreInterceptKeyBeforeSoftKeyboard(      onPreInterceptKeyBeforeSoftKeyboard: (KeyEvent) -> Boolean  )`  Adding this `modifier` to the `modifier` parameter of a component will allow it to intercept hardware key events before they are sent to the software keyboard. |
| Scope: **Any** | `@Composable Modifier.surface(      focusable: Boolean,      shape: Shape,      color: Color,      contentColor: Color,      depth: SurfaceDepth?,      border: BorderStroke?,      interactionSource: MutableInteractionSource?  )`  A surface is a fundamental building block in Glimmer. |
| Scope: **Any** | `@Composable Modifier.surface(      enabled: Boolean,      shape: Shape,      color: Color,      contentColor: Color,      depth: SurfaceDepth?,      border: BorderStroke?,      interactionSource: MutableInteractionSource?,      onClick: () -> Unit  )`  A surface is a fundamental building block in Glimmer. |
| Scope: **Any** | `Modifier. edgeSwipeToDismiss(      swipeToDismissBoxState: SwipeToDismissBoxState,      edgeWidth: Dp  )`  **This function is deprecated.** SwipeToDismiss has been migrated to androidx.wear.compose.foundation. |
| Scope: **Any** | `Modifier.systemGestureExclusion()`  Excludes the layout rectangle from the system gesture. |
| Scope: **Any** | `Modifier.systemGestureExclusion(exclusion: (LayoutCoordinates) -> Rect)`  Excludes a rectangle within the local layout coordinates from the system gesture. |
| Scope: **Any** | `Modifier.appendTextContextMenuComponents(builder: TextContextMenuBuilderScope.() -> Unit)`  Adds a `builder` to be run when the text context menu is shown within this hierarchy. |
| Scope: **Any** | `Modifier.filterTextContextMenuComponents(      filter: (TextContextMenuComponent) -> Boolean  )`  Adds a `filter` to be run when the text context menu is shown within this hierarchy. |
| Scope: **Any** | `Modifier.consumeWindowInsets(insets: WindowInsets)`  Consume insets that haven't been consumed yet by other insets Modifiers similar to `windowInsetsPadding` without adding any padding. |
| Scope: **Any** | `Modifier.consumeWindowInsets(paddingValues: PaddingValues)`  Consume `paddingValues` as insets as if the padding was added irrespective of insets. |
| Scope: **Any** | `Modifier.onConsumedWindowInsetsChanged(      block: (consumedWindowInsets: WindowInsets) -> Unit  )`  Calls `block` with the `WindowInsets` that have been consumed, either by `consumeWindowInsets` or one of the padding Modifiers, such as `imePadding`. |
| Scope: **Any** | `Modifier.recalculateWindowInsets()`  This recalculates the `WindowInsets` based on the size and position. |
| Scope: `SharedTransitionScope` | `Modifier.renderInSharedTransitionScopeOverlay(      zIndexInOverlay: Float,      renderInOverlay: () -> Boolean  )`  Renders the content in the `SharedTransitionScope`'s overlay, where shared content (i.e. shared elements and shared bounds) is rendered by default. |
| Scope: `SharedTransitionScope` | `Modifier.sharedBounds(      sharedContentState: SharedTransitionScope.SharedContentState,      animatedVisibilityScope: AnimatedVisibilityScope,      enter: EnterTransition,      exit: ExitTransition,      boundsTransform: BoundsTransform,      resizeMode: SharedTransitionScope.ResizeMode,      placeholderSize: SharedTransitionScope.PlaceholderSize,      renderInOverlayDuringTransition: Boolean,      zIndexInOverlay: Float,      clipInOverlayDuringTransition: SharedTransitionScope.OverlayClip  )`  `sharedBounds` is a modifier that tags a layout with a `SharedContentState.key`, such that entering and exiting shared bounds of the same key share the animated and continuously changing bounds during the layout change. |
| Scope: `SharedTransitionScope` | `Modifier.sharedElement(      sharedContentState: SharedTransitionScope.SharedContentState,      animatedVisibilityScope: AnimatedVisibilityScope,      boundsTransform: BoundsTransform,      placeholderSize: SharedTransitionScope.PlaceholderSize,      renderInOverlayDuringTransition: Boolean,      zIndexInOverlay: Float,      clipInOverlayDuringTransition: SharedTransitionScope.OverlayClip  )`  `sharedElement` is a modifier that tags a layout with a `SharedContentState.key`, such that entering and exiting shared elements of the same key share the animated and continuously changing bounds during the layout change. |
| Scope: `SharedTransitionScope` | `Modifier.sharedElementWithCallerManagedVisibility(      sharedContentState: SharedTransitionScope.SharedContentState,      visible: Boolean,      boundsTransform: BoundsTransform,      placeholderSize: SharedTransitionScope.PlaceholderSize,      renderInOverlayDuringTransition: Boolean,      zIndexInOverlay: Float,      clipInOverlayDuringTransition: SharedTransitionScope.OverlayClip  )`  `sharedElementWithCallerManagedVisibility` is a modifier that tags a layout with a `SharedContentState.key`, such that entering and exiting shared elements of the same key share the animated and continuously changing bounds during the layout change. |
| Scope: `SharedTransitionScope` `open` | `Modifier.skipToLookaheadPosition(enabled: () -> Boolean)`  A modifier that anchors a layout at the target position obtained from the lookahead pass during shared element transitions. |
| Scope: `ExposedDropdownMenuBoxScope` | `Modifier. menuAnchor()`  **This function is deprecated.** Use overload that takes ExposedDropdownMenuAnchorType and enabled parameters |
| Scope: `ExposedDropdownMenuBoxScope` `abstract` | `Modifier.menuAnchor(      type: ExposedDropdownMenuAnchorType,      enabled: Boolean  )`  Modifier which should be applied to an element inside the `ExposedDropdownMenuBoxScope`, typically a text field or an icon within the text field. |
| Scope: `PaneScaffoldScope` | `@ExperimentalMaterial3AdaptiveApi  @Composable Modifier.paneMargins(vararg insets: RectRulers)`  This modifier specifies the associated pane's margins according to the provided `RectRulers` as insets. |
| Scope: `PaneScaffoldScope` | `@ExperimentalMaterial3AdaptiveApi  @Composable Modifier.paneMargins(      fixedMargins: PaddingValues,      vararg insets: RectRulers  )`  This modifier specifies the associated pane's margins according to specified fixed margins and the provided `RectRulers` as insets, if any. |

[Previous

arrow\_back

Custom modifiers](/develop/ui/compose/custom-modifiers)

[Next

Lists and grids

arrow\_forward](/develop/ui/compose/lists)