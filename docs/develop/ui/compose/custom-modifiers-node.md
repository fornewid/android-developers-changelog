---
title: https://developer.android.com/develop/ui/compose/custom-modifiers-node
url: https://developer.android.com/develop/ui/compose/custom-modifiers-node
source: md.txt
---

[`Modifier.composed`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).composed(kotlin.Function1,kotlin.Function1)) was introduced in Compose 1.0 to let you access
composition elements from modifiers. For example, one key use case is creating
a stateful modifier that remembers local state and shares it with other
modifiers in the `Modifier.composed` factory:


```kotlin
// ❌ BAD: Using Modifier.composed is no longer recommended
fun Modifier.pressScale(
    pressedScale: Float = 0.95f,
    onClick: () -> Unit
): Modifier = composed(
    inspectorInfo = debugInspectorInfo {
        name = "pressScale"
        properties["pressedScale"] = pressedScale
    }
) {
    val interactionSource = remember { MutableInteractionSource() }
    val isPressed by interactionSource.collectIsPressedAsState()
    val scale by animateFloatAsState(
        targetValue = if (isPressed) pressedScale else 1f,
        animationSpec = spring(),
        label = "pressScale"
    )

    this
        .graphicsLayer {
            scaleX = scale
            scaleY = scale
        }
        .clickable(
            interactionSource = interactionSource,
            indication = null,
            onClick = onClick
        )
}
```

<br />

Use [`Modifier.Node`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier.Node) instead of `Modifier.composed`, as
`Modifier.Node` improves how state is managed within modifiers. A
`Modifier.Node` is a long-lived, stateful object created once per
`Modifier.Element` applied to a `LayoutNode`, and it survives recomposition
instead of being re-materialized through composition on every pass. For more
information about why and how we designed `Modifier.Node`, see
[Compose Modifiers deep dive](https://www.youtube.com/watch?v=BjGX2RftXsU).

This document describes how to migrate from `Modifier.composed` to
`Modifier.Node`. For more information about general usage of this API, see
[Implement custom modifier behavior using Modifier.Node](https://developer.android.com/develop/ui/compose/custom-modifiers#implement-custom).

## Performance benefits of Modifier.Node

Using `Modifier.composed` introduces several fundamental performance
bottlenecks:

- **State management overhead:** Managing state in this scope requires `remember` calls and snapshot state objects, which inflates the slot table with unnecessary composition groups and increases memory pressure.
- **Expensive lifecycle access:** Accessing the modifier's lifecycle requires using effects like `DisposableEffect`, which quickly increases the work required for the simpler use cases.
- **Lack of skippability:** Because the lambda passed to `composed` returns a `Modifier`, the Compose compiler can't mark it as skippable, forcing it to re-execute whenever the layout recomposes.
- **Broken memoization and equality:** Because the outer extension function itself isn't a `@Composable`, the compiler can't memoize the inner lambda, resulting in fresh lambda allocations on every call. This lack of memoization directly breaks modifier equality (`equals`), as `ComposedModifier` compares lambdas by reference. Consequently, Compose treats the modifier as changed on every frame even when parameters are static.
- **No smart change propagation:** Without top-level composable parameter tracking, there is no way to diff new inputs against previous ones for smart change propagation.

Overall, the `Modifier.composed` API shape encourages writing expensive code
and prevents the Compose runtime from applying additional modifier
optimizations.

## Core migration steps

The following example shows a typical custom modifier implemented with
`Modifier.composed`. For more context, see
[Implement custom modifier behavior using Modifier.Node](https://developer.android.com/develop/ui/compose/custom-modifiers#implement-custom).


```kotlin
fun Modifier.underline(
    color: Color,
    thickness: Dp = 2.dp,
    animationDurationMillis: Int = 300
): Modifier = composed {
    val density = LocalDensity.current
    val strokePx = with(density) { thickness.toPx() }

    // Drives how much of the underline is drawn: 0f -> 1f
    val progress = remember { Animatable(0f) }

    LaunchedEffect(color, thickness) {
        progress.snapTo(0f)
        progress.animateTo(
            targetValue = 1f,
            animationSpec = tween(durationMillis = animationDurationMillis)
        )
    }

    drawBehind {
        val y = size.height - strokePx / 2
        drawLine(
            color = color,
            start = Offset(0f, y),
            end = Offset(size.width * progress.value, y),
            strokeWidth = strokePx
        )
    }
}
```

<br />

1. Create a custom `Modifier.Node` (or `DelegatingNode`):


   ```kotlin
   private class UnderlineNode(
       private var color: Color,
       private var thickness: Dp,
       private var animationDurationMillis: Int
   ) : Modifier.Node() {
       fun update(color: Color, thickness: Dp, durationMillis: Int) {
       }
   }
   ```

   <br />

2. Implement one or more of `Modifier.Node`'s auxiliary APIs, depending on what
   your custom modifier needs (for example, `PointerInputModifierNode` if it
   needs access to pointer input APIs):


   ```kotlin
   private class UnderlineNode(
       private var color: Color,
       private var thickness: Dp,
       private var animationDurationMillis: Int
   ) : Modifier.Node(), DrawModifierNode {

       private val progress = Animatable(0f)
       private var animationJob: Job? = null

       override fun onAttach() {
           restartAnimation()
       }

       fun update(color: Color, thickness: Dp, durationMillis: Int) {
           val needsRestart = this.color != color || this.thickness != thickness
           this.color = color
           this.thickness = thickness
           this.animationDurationMillis = durationMillis
           if (needsRestart) restartAnimation()
       }

       private fun restartAnimation() {
           animationJob?.cancel()
           animationJob = coroutineScope.launch {
               progress.snapTo(0f)
               progress.animateTo(1f, tween(animationDurationMillis))
           }
       }

       override fun ContentDrawScope.draw() {
           val strokePx = thickness.toPx()
           val y = size.height - strokePx / 2
           drawLine(
               color = color,
               start = Offset(0f, y),
               end = Offset(size.width * progress.value, y),
               strokeWidth = strokePx
           )
           drawContent()
       }
   }
   ```

   <br />

3. Create a `ModifierNodeElement` that creates and updates your custom node:


   ```kotlin
   private class UnderlineElement(
       private val color: Color,
       private val thickness: Dp,
       private val animationDurationMillis: Int
   ) : ModifierNodeElement<UnderlineNode>() {

       override fun create() = UnderlineNode(color, thickness, animationDurationMillis)

       override fun update(node: UnderlineNode) {
           node.update(color, thickness, animationDurationMillis)
       }

       override fun InspectorInfo.inspectableProperties() {
           name = "underline"
           properties["color"] = color
           properties["thickness"] = thickness
           properties["animationDurationMillis"] = animationDurationMillis
       }

       override fun hashCode(): Int {
           var result = color.hashCode()
           result = 31 * result + thickness.hashCode()
           result = 31 * result + animationDurationMillis.hashCode()
           return result
       }

       override fun equals(other: Any?): Boolean {
           if (this === other) return true
           val otherElement = other as? UnderlineElement ?: return false
           return color == otherElement.color &&
               thickness == otherElement.thickness &&
               animationDurationMillis == otherElement.animationDurationMillis
       }
   }
   ```

   <br />

4. Update the modifier factory to point to the `ModifierNodeElement`:


   ```kotlin
   fun Modifier.underline(
       color: Color,
       thickness: Dp = 2.dp,
       animationDurationMillis: Int = 300
   ): Modifier = this then UnderlineElement(color, thickness, animationDurationMillis)
   ```

   <br />

## Common migration recipes

The following recipes show how to migrate common patterns from `Modifier.composed`
to `Modifier.Node` or `@Composable` modifier factories.

### Access a CompositionLocal

**Pattern:** Reading a single `CompositionLocal` such as `LocalDensity`,
`Theme`, or `LocalView`.

**Migration path:** Mark the modifier with `@Composable`. There is a semantic
difference between using a `composed` modifier and a `@Composable` modifier
factory to access a `CompositionLocal`---with a `@Composable` factory,
`CompositionLocal` values are resolved at the call site of the modifier
factory. If this isn't the intended behavior, use a custom `Modifier.Node`
implementation that reads `CompositionLocal`s using
`CompositionLocalConsumerModifierNode`.

For more information, see
[Create a custom modifier using a composable modifier factory](https://developer.android.com/develop/ui/compose/custom-modifiers#create-custom).


```kotlin
// ❌ BAD: Using Modifier.composed to read a single CompositionLocal
fun Modifier.themedContainerBorder(): Modifier =
    composed {
        Modifier.border(
            BorderStroke(
                width = 2.dp,
                color = LocalColorScheme.current.primaryColor,
            )
        )
            .clipToBounds()
    }
```

<br />


```kotlin
// ✅ GOOD: If the modifier is @Composable, it should be able to access the locals.
@Composable
fun Modifier.themedContainerBorder() =
    this then Modifier.border(
        BorderStroke(
            width = 2.dp,
            color = MyTheme.mainColor,
        )
    )
        .clipToBounds()
```

<br />

**Pattern:** Reading a `CompositionLocal` that might be applied to a subsequent
modifier.

**Migration path:** Create a custom `Modifier.Node` that implements
`CompositionLocalConsumerModifierNode` and combines all modifiers'
capabilities.


```kotlin
// ❌ BAD: Using Modifier.composed to read a CompositionLocal then using it in another modifier.
fun Modifier.adaptiveAccessibilityPadding(basePadding: Dp): Modifier = composed {
    // Reading LocalThemePadding.current.small (CompositionLocal)
    val extraPadding = LocalThemePadding.current.small
    Modifier.padding(basePadding + extraPadding)
}
```

<br />


```kotlin
// ✅ GOOD: A custom Modifier that combines the capabilities of both (layout and composition local reader) modifiers.
fun Modifier.adaptiveAccessibilityPadding(basePadding: Dp): Modifier =
    this.then(AdaptivePaddingElement(basePadding))

private data class AdaptivePaddingElement(
    val basePadding: Dp,
) : ModifierNodeElement<AdaptivePaddingNode>() {
    override fun create() = AdaptivePaddingNode(basePadding)

    override fun update(node: AdaptivePaddingNode) {
        node.basePadding = basePadding
    }

    override fun InspectorInfo.inspectableProperties() {
        name = "adaptiveAccessibilityPadding"
        properties["basePadding"] = basePadding
    }
}

private class AdaptivePaddingNode(
    var basePadding: Dp,
) : Modifier.Node(), LayoutModifierNode, CompositionLocalConsumerModifierNode {

    override fun MeasureScope.measure(
        measurable: Measurable,
        constraints: Constraints,
    ): MeasureResult {
        val extraPadding = currentValueOf(LocalThemePadding).small
        val total = (basePadding + extraPadding).roundToPx()

        val horizontal = total * 2
        val vertical = total * 2

        val placeable = measurable.measure(constraints.offset(-horizontal, -vertical))

        val width = constraints.constrainWidth(placeable.width + horizontal)
        val height = constraints.constrainHeight(placeable.height + vertical)

        return layout(width, height) {
            placeable.place(total, total)
        }
    }
}
```

<br />

### Access a non-layout composable function

**Pattern:** The modifier needs to access a function that is annotated with
`@Composable` and returns an object (for example, `colorResource` or
`ScrollableDefaults.flingBehavior`).

**Migration path:** Annotate the modifier with `@Composable`.


```kotlin
// ❌ BAD: Using Modifier.composed to access a composable function such as colorResource
fun Modifier.niceBackground() = composed {
    // Reading composable function colorResource
    val gradientColor1 = colorResource(R.color.my_special_color)
    background(color = gradientColor1, shape = CircleShape)
}
```

<br />


```kotlin
// ✅ GOOD: A modifier can be annotation with @Composable to reference composable functions.
@Composable // Modifier can be Composable itself.
private fun Modifier.niceBackground(): Modifier {
    val gradientColor1 = colorResource(R.color.my_special_color)
    return this.background(color = gradientColor1, shape = CircleShape)
}
```

<br />

### Access a coroutine scope

**Pattern:** `Modifier.composed` is used to execute `rememberCoroutineScope` to
access a `coroutineScope` object for launching coroutines.

**Migration path:** Use a custom `Modifier.Node`, which has a `coroutineScope`
property that is tied to the modifier lifecycle (like `rememberCoroutineScope`
inside `Modifier.composed`):


```kotlin
// ❌ BAD: Using Modifier.composed to get access to a coroutine scope.
fun Modifier.onClickAsyncComposed(onClick: suspend () -> Unit): Modifier =
    composed {
        val scope = rememberCoroutineScope()
        Modifier.pointerInput(onClick) {
            detectTapGestures {
                // Needs a coroutine scope to launch suspend lambda.
                scope.launch {
                    onClick()
                }
            }
        }
    }
```

<br />


```kotlin
// ✅ GOOD: A custom Modifier.Node has a scoped (modifier lifecycle) coroutineScope that can be used to launch async work.
fun Modifier.onClickAsync(onClick: suspend () -> Unit): Modifier =
    this.then(OnClickAsyncElement(onClick))

private data class OnClickAsyncElement(val onClick: suspend () -> Unit) :
    ModifierNodeElement<OnClickAsyncNode>() {
    override fun create(): OnClickAsyncNode = OnClickAsyncNode(onClick)

    override fun update(node: OnClickAsyncNode) {
        node.update(onClick)
    }

    override fun InspectorInfo.inspectableProperties() {
        name = "onClickAsync"
        properties["onClick"] = onClick
    }
}

private class OnClickAsyncNode(private var onClick: suspend () -> Unit) :
    DelegatingNode(), PointerInputModifierNode {

    private val pointerInputNode =
        delegate(
            SuspendingPointerInputModifierNode {
                detectTapGestures {
                    // Modifier.Node provides `coroutineScope` directly.
                    coroutineScope.launch { onClick() }
                }
            }
        )

    fun update(onClick: suspend () -> Unit) {
        if (this.onClick != onClick) {
            this.onClick = onClick
            pointerInputNode.resetPointerInputHandler()
        }
    }

    override fun onPointerEvent(
        pointerEvent: PointerEvent,
        pass: PointerEventPass,
        bounds: IntSize,
    ) {
        pointerInputNode.onPointerEvent(pointerEvent, pass, bounds)
    }

    override fun onCancelPointerInput() {
        pointerInputNode.onCancelPointerInput()
    }
}
```

<br />

### Remember a state

**Pattern:** Using `remember` in `Modifier.composed` to save state across
recompositions.

**Migration path:** `Modifier.Node` was built to hold state in the same
manner. State can be held inside an instance, just as any other class property
with a clearer lifecycle:


```kotlin
// ❌ BAD: Using Modifier.composed to make the modifier stateful.
fun Modifier.tapCountHighlightComposed(colors: List<Color>): Modifier = composed {
    // 1. Must use `remember` so `tapCount` isn't reset to 0 on every recomposition
    var tapCount by remember { mutableIntStateOf(0) }

    Modifier
        .pointerInput(colors) { detectTapGestures { tapCount++ } }
        .drawBehind { drawRect(colors[tapCount % colors.size]) }
}
```

<br />


```kotlin
// ✅ GOOD: Modifier.Node is the recommended way of creating stateful modifiers.
fun Modifier.tapCountHighlight(colors: List<Color>): Modifier =
    this then TapCountHighlightElement(colors)

private data class TapCountHighlightElement(
    val colors: List<Color>,
) : ModifierNodeElement<TapCountHighlightNode>() {
    override fun create() = TapCountHighlightNode(colors)

    override fun update(node: TapCountHighlightNode) {
        node.updateColors(colors)
    }

    override fun InspectorInfo.inspectableProperties() {
        name = "tapCountHighlight"
        properties["colors"] = colors
    }
}

private class TapCountHighlightNode(
    private var colors: List<Color>,
) : DelegatingNode(), DrawModifierNode {
    private var tapCount = 0 // Stateful modifier, this property will survive recompositions since Modifier.Nodes are held in the modifier tree.

    private val pointerInputNode = delegate(
        SuspendingPointerInputModifierNode {
            detectTapGestures {
                tapCount++
                invalidateDraw()
            }
        }
    )

    override fun ContentDrawScope.draw() {
        drawRect(colors[tapCount % colors.size])
        drawContent()
    }

    fun updateColors(colors: List<Color>) {
        this.colors = colors
        invalidateDraw()
    }
}
```

<br />

### Use an effect

**Pattern:** Using effects to execute operations tied to the composition
lifecycle (for example, when `Modifier.composed` entered or exited composition).

**Migration path:** `Modifier.Node` has clear lifecycle callbacks that can be
used to execute the same operations. For example, a `LaunchedEffect` can
generally be replaced with using the `coroutineScope` inside the
`Modifier.Node onAttach` method:


```kotlin
// ❌ BAD: Using Modifier.composed to launch/run an effect.
fun Modifier.logImpressionComposed(
    targetId: String,
    onLog: suspend (targetId: String) -> Unit,
): Modifier =
    composed {
        // LaunchedEffect is tied to Composition lifecycle
        LaunchedEffect(targetId) { onLog(targetId) }
        this
    }
```

<br />


```kotlin
// ✅ GOOD: Modifier.Node has lifecycle callbacks (e.g onAttach, onDetach) that can be used to emulate effects behaviors.
fun Modifier.logImpression(targetId: String, onLog: suspend (targetId: String) -> Unit): Modifier =
    this.then(LogImpressionElement(targetId, onLog))

private data class LogImpressionElement(
    val targetId: String,
    val onLog: suspend (targetId: String) -> Unit,
) : ModifierNodeElement<LogImpressionNode>() {
    override fun create(): LogImpressionNode = LogImpressionNode(targetId, onLog)

    override fun update(node: LogImpressionNode) {
        node.update(targetId, onLog)
    }

    override fun InspectorInfo.inspectableProperties() {
        name = "logImpression"
        properties["targetId"] = targetId
    }
}

private class LogImpressionNode(
    var targetId: String,
    var onLog: suspend (targetId: String) -> Unit,
) : Modifier.Node() {
    private var job: Job? = null

    override fun onAttach() {
        super.onAttach()
        runEffect() // Uses onAttach to track modifier lifecycle.
    }

    fun update(targetId: String, onLog: suspend (targetId: String) -> Unit) {
        // Re-run the effect if the key (`targetId`) changed
        if (this.targetId != targetId) {
            runEffect()
        }
        this.targetId = targetId
        this.onLog = onLog
    }

    private fun runEffect() {
        job?.cancel()
        job = coroutineScope.launch { onLog(targetId) }
    }
}
```

<br />

### Hold an animation state

**Pattern:** `Modifier.composed` using [`animate*AsState`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/animateDpAsState.composable#animateDpAsState(androidx.compose.ui.unit.Dp,androidx.compose.animation.core.AnimationSpec,kotlin.String,kotlin.Function1)).

**Migration path:** `animate*AsState` can be broken down into a custom modifier
that monitors the lifecycle callbacks and holds an `Animatable` state:


```kotlin
// ❌ BAD: Using Modifier.composed to save an animation state.
fun Modifier.fadeInOnHoverComposed(isHovered: Boolean): Modifier =
    composed {
        val alpha by
            animateFloatAsState(
                targetValue = if (isHovered) 1f else 0.4f,
                animationSpec = tween(durationMillis = 300),
                label = "alphaAnimation",
            )

        Modifier.graphicsLayer { this.alpha = alpha }
    }
```

<br />


```kotlin
// ✅ GOOD: Animation state can be saved in Modifier.Node like other types of stateful implementations.
fun Modifier.fadeInOnHover(isHovered: Boolean): Modifier =
    this.then(FadeInOnHoverElement(isHovered))

private data class FadeInOnHoverElement(val isHovered: Boolean) :
    ModifierNodeElement<FadeInOnHoverNode>() {
    override fun create(): FadeInOnHoverNode = FadeInOnHoverNode(isHovered)

    override fun update(node: FadeInOnHoverNode) {
        node.update(isHovered)
    }

    override fun InspectorInfo.inspectableProperties() {
        name = "fadeInOnHover"
        properties["isHovered"] = isHovered
    }
}

private class FadeInOnHoverNode(var isHovered: Boolean) : Modifier.Node(), LayoutModifierNode {
    // 1. Persistent Animatable field on the Node instance
    private val alphaAnimatable = Animatable(if (isHovered) 1f else 0.4f)

    override fun onAttach() {
        super.onAttach()
        startAnimation(isHovered)
    }

    // 2. Trigger animation imperatively when `isHovered` argument changes
    fun update(isHovered: Boolean) {
        if (this.isHovered != isHovered) {
            this.isHovered = isHovered
            if (isAttached) {
                startAnimation(isHovered)
            }
        }
    }

    private fun startAnimation(hovered: Boolean) {
        val targetAlpha = if (hovered) 1f else 0.4f
        // Use Node's built-in coroutineScope
        coroutineScope.launch {
            alphaAnimatable.animateTo(
                targetValue = targetAlpha,
                animationSpec = tween(durationMillis = 300),
            )
        }
    }

    override fun MeasureScope.measure(
        measurable: Measurable,
        constraints: Constraints,
    ): MeasureResult {
        val placeable = measurable.measure(constraints)
        return layout(placeable.width, placeable.height) {
            // Read current animation value during layout placement layer
            placeable.placeWithLayer(0, 0) { alpha = alphaAnimatable.value }
        }
    }
}
```

<br />