---
title: https://developer.android.com/develop/ui/compose/animation/composables-modifiers
url: https://developer.android.com/develop/ui/compose/animation/composables-modifiers
source: md.txt
---

Compose comes with built-in composables and modifiers for handling common animation use cases.

## Built-in animated composables

Compose provides several composables that animate content appearance,
disappearance, and layout changes.

### Animate appearance and disappearance

![Green composable showing and hiding itself](https://developer.android.com/static/develop/ui/compose/images/animations/animated_visibility_column.gif) **Figure 1.** Animating the appearance and disappearance of an item in a column.

The
[`AnimatedVisibility`](https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#AnimatedVisibility(androidx.compose.animation.core.MutableTransitionState,androidx.compose.ui.Modifier,androidx.compose.animation.EnterTransition,androidx.compose.animation.ExitTransition,kotlin.String,kotlin.Function1))
composable animates the appearance and disappearance of its content.


```kotlin
var visible by remember {
    mutableStateOf(true)
}
// Animated visibility will eventually remove the item from the composition once the animation has finished.
AnimatedVisibility(visible) {
    // your composable here
    // ...
}
```

<br />

By default, the content appears by fading in and expanding, and it disappears by
fading out and shrinking. Customize this transition by specifying
[`EnterTransition`](https://developer.android.com/reference/kotlin/androidx/compose/animation/EnterTransition) and [`ExitTransition`](https://developer.android.com/reference/kotlin/androidx/compose/animation/ExitTransition) objects.


```kotlin
var visible by remember { mutableStateOf(true) }
val density = LocalDensity.current
AnimatedVisibility(
    visible = visible,
    enter = slideInVertically {
        // Slide in from 40 dp from the top.
        with(density) { -40.dp.roundToPx() }
    } + expandVertically(
        // Expand from the top.
        expandFrom = Alignment.Top
    ) + fadeIn(
        // Fade in with the initial alpha of 0.3f.
        initialAlpha = 0.3f
    ),
    exit = slideOutVertically() + shrinkVertically() + fadeOut()
) {
    Text(
        "Hello",
        Modifier
            .fillMaxWidth()
            .height(200.dp)
    )
}
```

<br />

As shown in the preceding example, you can combine multiple `EnterTransition`
or `ExitTransition` objects with a `+` operator, and each accepts optional
parameters to customize its behavior. See the reference pages for more
information.

#### Enter and exit transition examples

| EnterTransition | ExitTransition |
|---|---|
| `https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#fadeIn(androidx.compose.animation.core.FiniteAnimationSpec,kotlin.Float)` ![A UI element gradually fades into view.](https://developer.android.com/static/develop/ui/compose/images/animation-fadein.gif) | `https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#fadeOut(androidx.compose.animation.core.FiniteAnimationSpec,kotlin.Float)` ![A UI element gradually fades out of view.](https://developer.android.com/static/develop/ui/compose/images/animation-fadeout.gif) |
| `https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#slideIn(androidx.compose.animation.core.FiniteAnimationSpec,kotlin.Function1)` ![A UI element slides into view from off-screen.](https://developer.android.com/static/develop/ui/compose/images/animation-slidein.gif) | `https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#slideOut(androidx.compose.animation.core.FiniteAnimationSpec,kotlin.Function1)` ![A UI element slides out of view off the screen.](https://developer.android.com/static/develop/ui/compose/images/animation-slideout.gif) |
| `https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#slideInHorizontally(androidx.compose.animation.core.FiniteAnimationSpec,kotlin.Function1)` ![A UI element slides horizontally into view.](https://developer.android.com/static/develop/ui/compose/images/animation-slideinhorizontally.gif) | `https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#slideOutHorizontally(androidx.compose.animation.core.FiniteAnimationSpec,kotlin.Function1)` ![A UI element slides horizontally out of view.](https://developer.android.com/static/develop/ui/compose/images/animation-slideouthorizontally.gif) |
| `https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#slideInVertically(androidx.compose.animation.core.FiniteAnimationSpec,kotlin.Function1)` ![A UI element slides vertically into view.](https://developer.android.com/static/develop/ui/compose/images/animation-slideinvertically.gif) | `https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#slideOutVertically(androidx.compose.animation.core.FiniteAnimationSpec,kotlin.Function1)` ![A UI element slides vertically out of view.](https://developer.android.com/static/develop/ui/compose/images/animation-slideoutvertically.gif) |
| `https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#scaleIn(androidx.compose.animation.core.FiniteAnimationSpec,kotlin.Float,androidx.compose.ui.graphics.TransformOrigin)` ![A UI element scales up and into view.](https://developer.android.com/static/develop/ui/compose/images/animation-scalein.gif) | `https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#scaleOut(androidx.compose.animation.core.FiniteAnimationSpec,kotlin.Float,androidx.compose.ui.graphics.TransformOrigin)` ![A UI element scales down and out of view.](https://developer.android.com/static/develop/ui/compose/images/animation-scaleout.gif) |
| `https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#expandIn(androidx.compose.animation.core.FiniteAnimationSpec,androidx.compose.ui.Alignment,kotlin.Boolean,kotlin.Function1)` ![A UI element expands into view from a central point.](https://developer.android.com/static/develop/ui/compose/images/animation-expandin.gif) | `https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#shrinkOut(androidx.compose.animation.core.FiniteAnimationSpec,androidx.compose.ui.Alignment,kotlin.Boolean,kotlin.Function1)` ![A UI element shrinks out of view to a central point.](https://developer.android.com/static/develop/ui/compose/images/animation-shrinkout.gif) |
| `https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#expandHorizontally(androidx.compose.animation.core.FiniteAnimationSpec,androidx.compose.ui.Alignment.Horizontal,kotlin.Boolean,kotlin.Function1)` ![A UI element expands horizontally into view.](https://developer.android.com/static/develop/ui/compose/images/animation-expandhorizontally.gif) | `https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#shrinkHorizontally(androidx.compose.animation.core.FiniteAnimationSpec,androidx.compose.ui.Alignment.Horizontal,kotlin.Boolean,kotlin.Function1)` ![A UI element shrinks horizontally out of view.](https://developer.android.com/static/develop/ui/compose/images/animation-shrinkhorizontally.gif) |
| `https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#expandVertically(androidx.compose.animation.core.FiniteAnimationSpec,androidx.compose.ui.Alignment.Vertical,kotlin.Boolean,kotlin.Function1)` ![A UI element expands vertically into view.](https://developer.android.com/static/develop/ui/compose/images/animation-expandvertically.gif) | `https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#shrinkVertically(androidx.compose.animation.core.FiniteAnimationSpec,androidx.compose.ui.Alignment.Vertical,kotlin.Boolean,kotlin.Function1)` ![A UI element shrinks vertically out of view.](https://developer.android.com/static/develop/ui/compose/images/animation-shrinkvertically.gif) |

`AnimatedVisibility` also offers a variant that takes a
`MutableTransitionState` argument. This lets you trigger an animation as soon as
the `AnimatedVisibility` composable is added to the composition tree. It is also
useful for observing the animation state.


```kotlin
// Create a MutableTransitionState<Boolean> for the AnimatedVisibility.
val state = remember {
    MutableTransitionState(false).apply {
        // Start the animation immediately.
        targetState = true
    }
}
Column {
    AnimatedVisibility(visibleState = state) {
        Text(text = "Hello, world!")
    }

    // Use the MutableTransitionState to know the current animation state
    // of the AnimatedVisibility.
    Text(
        text = when {
            state.isIdle && state.currentState -> "Visible"
            !state.isIdle && state.currentState -> "Disappearing"
            state.isIdle && !state.currentState -> "Invisible"
            else -> "Appearing"
        }
    )
}
```

<br />

#### Animate enter and exit for children

Content within `AnimatedVisibility` (direct or indirect children) can use the
[`animateEnterExit`](https://developer.android.com/reference/kotlin/androidx/compose/animation/AnimatedVisibilityScope#(androidx.compose.ui.Modifier).animateEnterExit(androidx.compose.animation.EnterTransition,androidx.compose.animation.ExitTransition,kotlin.String))
modifier to specify different animation behavior for each of them. The visual
effect for each of these children is a combination of the animations specified
at the `AnimatedVisibility` composable and the child's own enter and
exit animations.


```kotlin
var visible by remember { mutableStateOf(true) }

AnimatedVisibility(
    visible = visible,
    enter = fadeIn(),
    exit = fadeOut()
) {
    // Fade in/out the background and the foreground.
    Box(
        Modifier
            .fillMaxSize()
            .background(Color.DarkGray)
    ) {
        Box(
            Modifier
                .align(Alignment.Center)
                .animateEnterExit(
                    // Slide in/out the inner box.
                    enter = slideInVertically(),
                    exit = slideOutVertically()
                )
                .sizeIn(minWidth = 256.dp, minHeight = 64.dp)
                .background(Color.Red)
        ) {
            // Content of the notification...
        }
    }
}
```

<br />

In some cases, you may want to have `AnimatedVisibility` apply no animations at
all so that children can each have their own distinct animations by
`animateEnterExit`. To achieve this, specify `EnterTransition.None` and
`ExitTransition.None` at the `AnimatedVisibility` composable.

#### Add custom animation

If you want to add custom animation effects beyond the built-in enter and exit
animations, access the underlying `Transition` instance using the `transition`
property inside the content lambda for `AnimatedVisibility`. Any animation
states added to the Transition instance will run simultaneously with the enter
and exit animations of `AnimatedVisibility`. `AnimatedVisibility` waits until
all animations in the `Transition` have finished before removing its content.
For exit animations created independent of `Transition` (such as using
`animate*AsState`), `AnimatedVisibility` wouldn't be able to account for them,
and therefore might remove the content composable before they finish.


```kotlin
var visible by remember { mutableStateOf(true) }

AnimatedVisibility(
    visible = visible,
    enter = fadeIn(),
    exit = fadeOut()
) { // this: AnimatedVisibilityScope
    // Use AnimatedVisibilityScope#transition to add a custom animation
    // to the AnimatedVisibility.
    val background by transition.animateColor(label = "color") { state ->
        if (state == EnterExitState.Visible) Color.Blue else Color.Gray
    }
    Box(
        modifier = Modifier
            .size(128.dp)
            .background(background)
    )
}
```

<br />

To learn more about using `Transition` to manage animations, see [Animate
multiple properties simultaneously with a transition](https://developer.android.com/develop/ui/compose/animation/value-based#updateTransition).

### Animate based on target state

The [`AnimatedContent`](https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#AnimatedContent(kotlin.Any,androidx.compose.ui.Modifier,kotlin.Function1,androidx.compose.ui.Alignment,kotlin.String,kotlin.Function1,kotlin.Function2))
composable animates its content as it changes based on a
target state.


```kotlin
Row {
    var count by remember { mutableIntStateOf(0) }
    Button(onClick = { count++ }) {
        Text("Add")
    }
    AnimatedContent(
        targetState = count,
        label = "animated content"
    ) { targetCount ->
        // Make sure to use `targetCount`, not `count`.
        Text(text = "Count: $targetCount")
    }
}
```

<br />

> [!NOTE]
> **Note:** You must always use the lambda parameter and reflect it to the content. The API uses this value as a key to identify the content that's currently being shown.

By default, the initial content fades out and then the target content fades in
(this behavior is called [fade through](https://material.io/design/motion/the-motion-system.html#fade-through)). You
can customize this animation behavior by specifying a [`ContentTransform`](https://developer.android.com/reference/kotlin/androidx/compose/animation/ContentTransform)
object to the `transitionSpec` parameter. You can create an
instance of `ContentTransform` by combining an
[`EnterTransition`](https://developer.android.com/reference/kotlin/androidx/compose/animation/EnterTransition) object
with an [`ExitTransition`](https://developer.android.com/reference/kotlin/androidx/compose/animation/ExitTransition) object
using the `with` infix function. You can apply [`SizeTransform`](https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#SizeTransform(kotlin.Boolean,kotlin.Function2))
to the `ContentTransform` object by attaching it with the
`using` infix function.


```kotlin
AnimatedContent(
    targetState = count,
    transitionSpec = {
        // Compare the incoming number with the previous number.
        if (targetState > initialState) {
            // If the target number is larger, it slides up and fades in
            // while the initial (smaller) number slides up and fades out.
            slideInVertically { height -> height } + fadeIn() togetherWith
                slideOutVertically { height -> -height } + fadeOut()
        } else {
            // If the target number is smaller, it slides down and fades in
            // while the initial number slides down and fades out.
            slideInVertically { height -> -height } + fadeIn() togetherWith
                slideOutVertically { height -> height } + fadeOut()
        }.using(
            // Disable clipping since the faded slide-in/out should
            // be displayed out of bounds.
            SizeTransform(clip = false)
        )
    }, label = "animated content"
) { targetCount ->
    Text(text = "$targetCount")
}
```

<br />

![](https://developer.android.com/static/develop/ui/compose/images/animation-count.gif)

`EnterTransition` defines how the target content should appear, and
`ExitTransition` defines how the initial content should disappear. In addition
to all of the `EnterTransition` and `ExitTransition` functions available for
`AnimatedVisibility`, `AnimatedContent` offers [`slideIntoContainer`](https://developer.android.com/reference/kotlin/androidx/compose/animation/AnimatedContentTransitionScope#slideIntoContainer(androidx.compose.animation.AnimatedContentTransitionScope.SlideDirection,androidx.compose.animation.core.FiniteAnimationSpec,kotlin.Function1))
and [`slideOutOfContainer`](https://developer.android.com/reference/kotlin/androidx/compose/animation/AnimatedContentTransitionScope#slideOutOfContainer(androidx.compose.animation.AnimatedContentTransitionScope.SlideDirection,androidx.compose.animation.core.FiniteAnimationSpec,kotlin.Function1)).
These are convenient alternatives to `slideInHorizontally/Vertically` and
`slideOutHorizontally/Vertically` that calculate the slide distance based on
the sizes of the initial content and the target content of the
`AnimatedContent` content.

[`SizeTransform`](https://developer.android.com/reference/kotlin/androidx/compose/animation/SizeTransform) defines how the
size should animate between the initial and the target contents. You have
access to both the initial size and the target size when you are creating the
animation. `SizeTransform` also controls whether the content should be clipped
to the component size during animations.


```kotlin
var expanded by remember { mutableStateOf(false) }
Surface(
    color = MaterialTheme.colorScheme.primary,
    onClick = { expanded = !expanded }
) {
    AnimatedContent(
        targetState = expanded,
        transitionSpec = {
            fadeIn(animationSpec = tween(150, 150)) togetherWith
                fadeOut(animationSpec = tween(150)) using
                SizeTransform { initialSize, targetSize ->
                    if (targetState) {
                        keyframes {
                            // Expand horizontally first.
                            IntSize(targetSize.width, initialSize.height) at 150
                            durationMillis = 300
                        }
                    } else {
                        keyframes {
                            // Shrink vertically first.
                            IntSize(initialSize.width, targetSize.height) at 150
                            durationMillis = 300
                        }
                    }
                }
        }, label = "size transform"
    ) { targetExpanded ->
        if (targetExpanded) {
            Expanded()
        } else {
            ContentIcon()
        }
    }
}
```

<br />

![](https://developer.android.com/static/develop/ui/compose/images/animation-sizetransform.gif)

#### Animate child enter and exit transitions

Just like `AnimatedVisibility`, the [`animateEnterExit`](https://developer.android.com/reference/kotlin/androidx/compose/animation/AnimatedVisibilityScope#(androidx.compose.ui.Modifier).animateEnterExit(androidx.compose.animation.EnterTransition,androidx.compose.animation.ExitTransition,kotlin.String))
modifier is available inside the content lambda of `AnimatedContent`. Use this
to apply `EnterAnimation` and `ExitAnimation` to each of the direct or indirect
children separately.

#### Add custom animation

Just like `AnimatedVisibility`, the `transition` field is available inside the
content lambda of `AnimatedContent`. Use this to create a custom animation
effect that runs simultaneously with the `AnimatedContent` transition. See
[updateTransition](https://developer.android.com/develop/ui/compose/animation/value-based#updateTransition) for the details.

### Animate between two layouts

`Crossfade` animates between two layouts with a crossfade animation. By toggling
the value passed to the `current` parameter, the content is switched with a
crossfade animation.


```kotlin
var currentPage by remember { mutableStateOf("A") }
Crossfade(targetState = currentPage, label = "cross fade") { screen ->
    when (screen) {
        "A" -> Text("Page A")
        "B" -> Text("Page B")
    }
}
```

<br />

## Built-in animation modifiers

Compose provides modifiers for animating specific changes directly on
composables.

### Animate composable size changes

![Green composable animating its size change smoothly.](https://developer.android.com/static/develop/ui/compose/images/animations/animated_content_size.gif) **Figure 2.** Composable smoothly animating between a small and a larger size

The `animateContentSize` modifier animates a size change.

> [!NOTE]
> **Note:** The ordering of where `animateContentSize` is placed in your modifier chain matters. For smooth animations, place it *before* any size modifiers such as `size` or `defaultMinSize` to confirm that `animateContentSize` reports the animated value change to the layout.


```kotlin
var expanded by remember { mutableStateOf(false) }
Box(
    modifier = Modifier
        .background(colorBlue)
        .animateContentSize()
        .height(if (expanded) 400.dp else 200.dp)
        .fillMaxWidth()
        .clickable(
            interactionSource = remember { MutableInteractionSource() },
            indication = null
        ) {
            expanded = !expanded
        }

) {
}
```

<br />

## List item animations

If you are looking to animate item reorderings inside a Lazy list or grid, take
a look at the [Lazy layout item animation documentation](https://developer.android.com/develop/ui/compose/lists#item-animations).

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Value-based animations](https://developer.android.com/develop/ui/compose/animation/value-based)
- [Animations in Compose](https://developer.android.com/develop/ui/compose/animation/introduction)
- [Animation tooling support {:#tooling}](https://developer.android.com/develop/ui/compose/animation/tooling)