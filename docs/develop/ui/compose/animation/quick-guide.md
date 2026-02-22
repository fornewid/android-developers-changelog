---
title: https://developer.android.com/develop/ui/compose/animation/quick-guide
url: https://developer.android.com/develop/ui/compose/animation/quick-guide
source: md.txt
---

[Video](https://www.youtube.com/watch?v=HNSKJIQtb4c)

Compose has many built-in animation mechanisms and it can be overwhelming to
know which one to choose. Below is a list of common animation use cases. For
more detailed information about the full set of different API options available
to you, read the full [Compose Animation documentation](https://developer.android.com/develop/ui/compose/animation/introduction).

## Animate common composable properties

Compose provides convenient APIs that allow you to solve for many common
animation use cases. This section demonstrates how you can animate common
properties of a composable.

### Animate appearing / disappearing

![Green composable showing and hiding itself](https://developer.android.com/static/develop/ui/compose/images/animations/animated_visibility_column.gif) **Figure 1.** Animating the appearance and disappearance of an item in a Column

Use [`AnimatedVisibility`](https://developer.android.com/develop/ui/compose/animation/composables-modifiers#animatedvisibility) to hide or show a Composable. Children inside
`AnimatedVisibility` can use `Modifier.animateEnterExit()` for their own enter
or exit transition.


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

The enter and exit parameters of `AnimatedVisibility` allow you to configure how
a composable behaves when it appears and disappears. Read the [full
documentation](https://developer.android.com/develop/ui/compose/animation/composables-modifiers#animatedvisibility) for more information.

Another option for animating the visibility of a composable is to animate the
alpha over time using [`animateFloatAsState`](https://developer.android.com/develop/ui/compose/animation/value-based#animate-as-state):


```kotlin
var visible by remember {
    mutableStateOf(true)
}
val animatedAlpha by animateFloatAsState(
    targetValue = if (visible) 1.0f else 0f,
    label = "alpha"
)
Box(
    modifier = Modifier
        .size(200.dp)
        .graphicsLayer {
            alpha = animatedAlpha
        }
        .clip(RoundedCornerShape(8.dp))
        .background(colorGreen)
        .align(Alignment.TopCenter)
) {
}
```

<br />

However, changing the alpha comes with the caveat that the composable **remains
in the composition** and continues to occupy the space it's laid out in. This
could cause screen readers and other accessibility mechanisms to still consider
the item on screen. On the other hand, `AnimatedVisibility` eventually removes
the item from the composition.
![Animating the alpha of a composable](https://developer.android.com/static/develop/ui/compose/images/animations/animated_visibility_alpha.gif) **Figure 2.** Animating the alpha of a composable

### Animate background color

![Composable with background color changing over time as an animation, where the colors are fading into one another.](https://developer.android.com/static/develop/ui/compose/images/animations/animated_forever.gif) **Figure 3.** Animating background color of composable


```kotlin
val animatedColor by animateColorAsState(
    if (animateBackgroundColor) colorGreen else colorBlue,
    label = "color"
)
Column(
    modifier = Modifier.drawBehind {
        drawRect(animatedColor)
    }
) {
    // your composable here
}
```

<br />

This option is more performant than using `Modifier.background()`.
`Modifier.background()` is acceptable for a one-shot color setting, but when
animating a color over time, this could cause more recompositions than
necessary.

For infinitely animating the background color, see [repeating an animation
section](https://developer.android.com/develop/ui/compose/animation/quick-guide#repeat-animation).

### Animate the size of a composable

![Green composable animating its size change smoothly.](https://developer.android.com/static/develop/ui/compose/images/animations/animated_content_size.gif) **Figure 4.** Composable smoothly animating between a small and a larger size

Compose lets you animate the size of composables in a few different ways. Use
[`animateContentSize()`](https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#(androidx.compose.ui.Modifier).animateContentSize(androidx.compose.animation.core.FiniteAnimationSpec,kotlin.Function2)) for animations between composable size changes.

For example, if you have a box that contains text which can expand from one to
multiple lines you can use `Modifier.animateContentSize()` to achieve a smoother
transition:


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

> [!NOTE]
> **Note:** [Ordering of the modifiers](https://developer.android.com/develop/ui/compose/modifiers#order-modifier-matters) matters here. Make sure to place it **before** any size modifiers.

You can also use [`AnimatedContent`](https://developer.android.com/develop/ui/compose/animation/composables-modifiers#animatedcontent), with a [`SizeTransform`](https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#SizeTransform(kotlin.Boolean,kotlin.Function2)) to describe
how size changes should take place.

### Animate position of composable

![Green composable smoothly animating down and to the right](https://developer.android.com/static/develop/ui/compose/images/animations/animated_offset.gif) **Figure 5.** Composable moving by an offset

To animate the position of a composable, use `Modifier.offset{ }` combined with
`animateIntOffsetAsState()`.


```kotlin
var moved by remember { mutableStateOf(false) }
val pxToMove = with(LocalDensity.current) {
    100.dp.toPx().roundToInt()
}
val offset by animateIntOffsetAsState(
    targetValue = if (moved) {
        IntOffset(pxToMove, pxToMove)
    } else {
        IntOffset.Zero
    },
    label = "offset"
)

Box(
    modifier = Modifier
        .offset {
            offset
        }
        .background(colorBlue)
        .size(100.dp)
        .clickable(
            interactionSource = remember { MutableInteractionSource() },
            indication = null
        ) {
            moved = !moved
        }
)
```

<br />

> [!CAUTION]
> **Caution:** This does not change where the parent perceives the composable to be placed, and therefore does not affect where siblings are placed. This may result in siblings drawing over or under one another. The offset only influences the position of child layouts of the `Modifier.offset{}`.

If you want to ensure that composables are not drawn over or under other
composables when animating position or size, use `Modifier.layout{ }`. This
modifier propagates size and position changes to the parent, which then affects
other children.

For example, if you are moving a `Box` within a `Column` and the other children
need to move when the `Box` moves, include the offset information with
`Modifier.layout{ }` as follows:


```kotlin
var toggled by remember {
    mutableStateOf(false)
}
val interactionSource = remember {
    MutableInteractionSource()
}
Column(
    modifier = Modifier
        .padding(16.dp)
        .fillMaxSize()
        .clickable(indication = null, interactionSource = interactionSource) {
            toggled = !toggled
        }
) {
    val offsetTarget = if (toggled) {
        IntOffset(150, 150)
    } else {
        IntOffset.Zero
    }
    val offset = animateIntOffsetAsState(
        targetValue = offsetTarget, label = "offset"
    )
    Box(
        modifier = Modifier
            .size(100.dp)
            .background(colorBlue)
    )
    Box(
        modifier = Modifier
            .layout { measurable, constraints ->
                val offsetValue = if (isLookingAhead) offsetTarget else offset.value
                val placeable = measurable.measure(constraints)
                layout(placeable.width + offsetValue.x, placeable.height + offsetValue.y) {
                    placeable.placeRelative(offsetValue)
                }
            }
            .size(100.dp)
            .background(colorGreen)
    )
    Box(
        modifier = Modifier
            .size(100.dp)
            .background(colorBlue)
    )
}
```

<br />

![2 boxes with the 2nd box animating its X,Y position, the third box responding by moving itself by Y amount too.](https://developer.android.com/static/develop/ui/compose/images/animations/animated_layout_modifier.gif) **Figure 6.** Animating with `Modifier.layout{ }`

### Animate padding of a composable

![Green composable getting smaller and bigger on click, with padding being animated](https://developer.android.com/static/develop/ui/compose/images/animations/animated_padding.gif) **Figure 7.** Composable with its padding animating

To animate the padding of a composable, use `animateDpAsState` combined with
`Modifier.padding()`:


```kotlin
var toggled by remember {
    mutableStateOf(false)
}
val animatedPadding by animateDpAsState(
    if (toggled) {
        0.dp
    } else {
        20.dp
    },
    label = "padding"
)
Box(
    modifier = Modifier
        .aspectRatio(1f)
        .fillMaxSize()
        .padding(animatedPadding)
        .background(Color(0xff53D9A1))
        .clickable(
            interactionSource = remember { MutableInteractionSource() },
            indication = null
        ) {
            toggled = !toggled
        }
)
```

<br />

### Animate elevation of a composable

**Figure 8.** Composable's elevation animating on click

To animate the elevation of a composable, use `animateDpAsState` combined with
`Modifier.graphicsLayer{ }`. For once-off elevation changes, use
`Modifier.shadow()`. If you are animating the shadow, using
`Modifier.graphicsLayer{ }` modifier is the more performant option.


```kotlin
val mutableInteractionSource = remember {
    MutableInteractionSource()
}
val pressed = mutableInteractionSource.collectIsPressedAsState()
val elevation = animateDpAsState(
    targetValue = if (pressed.value) {
        32.dp
    } else {
        8.dp
    },
    label = "elevation"
)
Box(
    modifier = Modifier
        .size(100.dp)
        .align(Alignment.Center)
        .graphicsLayer {
            this.shadowElevation = elevation.value.toPx()
        }
        .clickable(interactionSource = mutableInteractionSource, indication = null) {
        }
        .background(colorGreen)
) {
}
```

<br />

Alternatively, use the [`Card`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Card(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.material3.CardColors,androidx.compose.material3.CardElevation,androidx.compose.foundation.BorderStroke,kotlin.Function1)) composable, and set the elevation property to
different values per state.

### Animate text scale, translation or rotation

![Text composable saying](https://developer.android.com/static/develop/ui/compose/images/animations/animated_text.gif) **Figure 9.** Text animating smoothly between two sizes

When animating scale, translation, or rotation of text, set the `textMotion`
parameter on `TextStyle` to [`TextMotion.Animated`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/style/TextMotion). This ensures smoother
transitions between text animations. Use [`Modifier.graphicsLayer{ }`](https://developer.android.com/develop/ui/compose/graphics/draw/modifiers#graphicsLayer) to
translate, rotate or scale the text.


```kotlin
val infiniteTransition = rememberInfiniteTransition(label = "infinite transition")
val scale by infiniteTransition.animateFloat(
    initialValue = 1f,
    targetValue = 8f,
    animationSpec = infiniteRepeatable(tween(1000), RepeatMode.Reverse),
    label = "scale"
)
Box(modifier = Modifier.fillMaxSize()) {
    Text(
        text = "Hello",
        modifier = Modifier
            .graphicsLayer {
                scaleX = scale
                scaleY = scale
                transformOrigin = TransformOrigin.Center
            }
            .align(Alignment.Center),
        // Text composable does not take TextMotion as a parameter.
        // Provide it via style argument but make sure that we are copying from current theme
        style = LocalTextStyle.current.copy(textMotion = TextMotion.Animated)
    )
}
```

<br />

### Animate text color

![The words](https://developer.android.com/static/develop/ui/compose/images/animations/animated_text_color.gif) **Figure 10.** Example showing animating text color

To animate text color, use the `color` lambda on the `BasicText` composable:


```kotlin
val infiniteTransition = rememberInfiniteTransition(label = "infinite transition")
val animatedColor by infiniteTransition.animateColor(
    initialValue = Color(0xFF60DDAD),
    targetValue = Color(0xFF4285F4),
    animationSpec = infiniteRepeatable(tween(1000), RepeatMode.Reverse),
    label = "color"
)

BasicText(
    text = "Hello Compose",
    color = {
        animatedColor
    },
    // ...
)
```

<br />

## Switch between different types of content

![Green screen saying](https://developer.android.com/static/develop/ui/compose/images/animations/animated_content_slower.gif) **Figure 11.** Using AnimatedContent to animate changes between different composables (slowed down)

Use [`AnimatedContent`](https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#AnimatedContent(kotlin.Any,androidx.compose.ui.Modifier,kotlin.Function1,androidx.compose.ui.Alignment,kotlin.Function2)) to animate between different composables, if you
just want a standard fade between composables, use `Crossfade`.


```kotlin
var state by remember {
    mutableStateOf(UiState.Loading)
}
AnimatedContent(
    state,
    transitionSpec = {
        fadeIn(
            animationSpec = tween(3000)
        ) togetherWith fadeOut(animationSpec = tween(3000))
    },
    modifier = Modifier.clickable(
        interactionSource = remember { MutableInteractionSource() },
        indication = null
    ) {
        state = when (state) {
            UiState.Loading -> UiState.Loaded
            UiState.Loaded -> UiState.Error
            UiState.Error -> UiState.Loading
        }
    },
    label = "Animated Content"
) { targetState ->
    when (targetState) {
        UiState.Loading -> {
            LoadingScreen()
        }
        UiState.Loaded -> {
            LoadedScreen()
        }
        UiState.Error -> {
            ErrorScreen()
        }
    }
}
```

<br />

`AnimatedContent` can be customized to show many different kinds of enter and
exit transitions. For more information, read the documentation on
[`AnimatedContent`](https://developer.android.com/develop/ui/compose/animation/composables-modifiers#animatedcontent) or read this [blog post on](https://medium.com/androiddevelopers/customizing-animatedcontent-in-jetpack-compose-629c67b45894)
[`AnimatedContent`](https://medium.com/androiddevelopers/customizing-animatedcontent-in-jetpack-compose-629c67b45894).

## Animate whilst navigating to different destinations

![Two composables, one green saying Landing and one blue saying Detail, animating by sliding the detail composable over the landing composable.](https://developer.android.com/static/develop/ui/compose/images/animations/navigation_compose_animation.gif) **Figure 12.** Animating between composables using navigation-compose

To animate transitions between composables when using the
[navigation-compose](https://developer.android.com/jetpack/androidx/releases/navigation) artifact, specify the `enterTransition` and
`exitTransition` on a composable. You can also set the default animation to be
used for all destinations at the top level `NavHost`:


```kotlin
val navController = rememberNavController()
NavHost(
    navController = navController, startDestination = "landing",
    enterTransition = { EnterTransition.None },
    exitTransition = { ExitTransition.None }
) {
    composable("landing") {
        ScreenLanding(
            // ...
        )
    }
    composable(
        "detail/{photoUrl}",
        arguments = listOf(navArgument("photoUrl") { type = NavType.StringType }),
        enterTransition = {
            fadeIn(
                animationSpec = tween(
                    300, easing = LinearEasing
                )
            ) + slideIntoContainer(
                animationSpec = tween(300, easing = EaseIn),
                towards = AnimatedContentTransitionScope.SlideDirection.Start
            )
        },
        exitTransition = {
            fadeOut(
                animationSpec = tween(
                    300, easing = LinearEasing
                )
            ) + slideOutOfContainer(
                animationSpec = tween(300, easing = EaseOut),
                towards = AnimatedContentTransitionScope.SlideDirection.End
            )
        }
    ) { backStackEntry ->
        ScreenDetails(
            // ...
        )
    }
}
```

<br />

There are many different kinds of enter and exit transitions that apply
different effects to the incoming and outgoing content, see the
[documentation](https://developer.android.com/develop/ui/compose/animation/composables-modifiers#enter-exit-transition) for more.

> [!NOTE]
> **Note:** Enter and Exit transitions are only available from navigation-compose [2.7.0-alpha01](https://developer.android.com/jetpack/androidx/releases/navigation#2.7.0-alpha01).

## Repeat an animation

![A green background that transforms into a blue background, infinitely by animating between the two colors.](https://developer.android.com/static/develop/ui/compose/images/animations/animated_forever.gif) **Figure 13.** Background color animating between two values, infinitely

Use [`rememberInfiniteTransition`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/InfiniteTransition) with an `infiniteRepeatable`
`animationSpec` to continuously repeat your animation. Change `RepeatModes` to
specify how it should go back and forth.

Use [`repeatable`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/package-summary#repeatable(kotlin.Int,androidx.compose.animation.core.DurationBasedAnimationSpec,androidx.compose.animation.core.RepeatMode,androidx.compose.animation.core.StartOffset)) to repeat a set number of times.


```kotlin
val infiniteTransition = rememberInfiniteTransition(label = "infinite")
val color by infiniteTransition.animateColor(
    initialValue = Color.Green,
    targetValue = Color.Blue,
    animationSpec = infiniteRepeatable(
        animation = tween(1000, easing = LinearEasing),
        repeatMode = RepeatMode.Reverse
    ),
    label = "color"
)
Column(
    modifier = Modifier.drawBehind {
        drawRect(color)
    }
) {
    // your composable here
}
```

<br />

## Start an animation on launch of a composable

[`LaunchedEffect`](https://developer.android.com/develop/ui/compose/side-effects#launchedeffect) runs when a composable enters the composition. It starts
an animation on launch of a composable, you can use this to drive the animation
state change. Using `Animatable` with the `animateTo` method to start the
animation on launch:


```kotlin
val alphaAnimation = remember {
    Animatable(0f)
}
LaunchedEffect(Unit) {
    alphaAnimation.animateTo(1f)
}
Box(
    modifier = Modifier.graphicsLayer {
        alpha = alphaAnimation.value
    }
)
```

<br />

> [!CAUTION]
> **Caution:** Be careful when using `LaunchedEffects` inside lazy layouts. They relaunch when the items re-enter the composition. For example, this can occur when scrolling the list offscreen and back on screen. Instead, [hoist your
> state](https://developer.android.com/develop/ui/compose/state#state-hoisting) outside the lazy layout to ensure the animation doesn't happen for each scroll in and out of the composition.

## Create sequential animations

![Four circles with green arrows animating between each one, animating one by one after one another.](https://developer.android.com/static/develop/ui/compose/images/animations/multiple_properties_sequential.gif) **Figure 14.** Diagram indicating how a sequential animation progresses, one by one.

Use the `Animatable` coroutine APIs to perform sequential or concurrent
animations. Calling `animateTo` on the `Animatable` one after the other causes
each animation to wait for the previous animations to finish before proceeding .
This is because it is a suspend function.


```kotlin
val alphaAnimation = remember { Animatable(0f) }
val yAnimation = remember { Animatable(0f) }

LaunchedEffect("animationKey") {
    alphaAnimation.animateTo(1f)
    yAnimation.animateTo(100f)
    yAnimation.animateTo(500f, animationSpec = tween(100))
}
```

<br />

## Create concurrent animations

![Three circles with green arrows animating to each one, animating all together at the same time.](https://developer.android.com/static/develop/ui/compose/images/animations/multiple_properties.gif) **Figure 15.** Diagram indicating how concurrent animations progress, all at the same time.

Use the coroutine APIs ([`Animatable#animateTo()`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/Animatable#animateTo(kotlin.Any,androidx.compose.animation.core.AnimationSpec,kotlin.Any,kotlin.Function1)) or [`animate`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/package-summary#animate(kotlin.Float,kotlin.Float,kotlin.Float,androidx.compose.animation.core.AnimationSpec,kotlin.Function2))())), or
the [`Transition`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/Transition) API to achieve concurrent animations. If you use multiple
launch functions in a coroutine context, it launches the animations at the same
time:


```kotlin
val alphaAnimation = remember { Animatable(0f) }
val yAnimation = remember { Animatable(0f) }

LaunchedEffect("animationKey") {
    launch {
        alphaAnimation.animateTo(1f)
    }
    launch {
        yAnimation.animateTo(100f)
    }
}
```

<br />

You could use the [`updateTransition`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/package-summary#updateTransition(kotlin.Any,kotlin.String)) API to use the same state to drive
many different property animations at the same time. The example below animates
two properties controlled by a state change, `rect` and `borderWidth`:


```kotlin
var currentState by remember { mutableStateOf(BoxState.Collapsed) }
val transition = updateTransition(currentState, label = "transition")

val rect by transition.animateRect(label = "rect") { state ->
    when (state) {
        BoxState.Collapsed -> Rect(0f, 0f, 100f, 100f)
        BoxState.Expanded -> Rect(100f, 100f, 300f, 300f)
    }
}
val borderWidth by transition.animateDp(label = "borderWidth") { state ->
    when (state) {
        BoxState.Collapsed -> 1.dp
        BoxState.Expanded -> 0.dp
    }
}
```

<br />

## Optimize animation performance

Animations in Compose can cause performance problems. This is due to the nature
of what an animation is: moving or changing pixels on screen quickly,
frame-by-frame to create the illusion of movement.

Consider the [different phases of Compose](https://developer.android.com/develop/ui/compose/phases): composition, layout and draw. If
your animation changes the layout phase, it requires all affected composables to
relayout and redraw. If your animation occurs in the draw phase, it is by
default be more performant than if you were to run the animation in the layout
phase, as it would have less work to do overall.

To ensure your app does as little as possible while animating, choose the lambda
version of a `Modifier` where possible. This skips recomposition and performs
the animation outside of the composition phase, otherwise use
[`Modifier.graphicsLayer{ }`](https://developer.android.com/develop/ui/compose/graphics/draw/modifiers), as this modifier always runs in the draw
phase. For more information on this, see the [deferring reads](https://developer.android.com/develop/ui/compose/performance/bestpractices#defer-reads) section in
the performance documentation.

## Change animation timing

Compose by default uses **spring** animations for most animations. Springs, or
physics-based animations, feel more natural. They are also interruptible as
they take into account the object's current velocity, instead of a fixed time.
If you want to override the default, all the animation APIs demonstrated above
have the ability to set an `animationSpec` to customize how an animation runs,
whether you'd like it to execute over a certain duration or be more bouncy.

The following is a summary of the different `animationSpec` options:

- [`spring`](https://developer.android.com/develop/ui/compose/animation/customize#spring): Physics-based animation, the default for all animations. You can change the stiffness or dampingRatio to achieve a different animation look and feel.
- [`tween`](https://developer.android.com/develop/ui/compose/animation/customize#tween) (short for **between** ): Duration-based animation, animates between two values with an `Easing` function.
- [`keyframes`](https://developer.android.com/develop/ui/compose/animation/customize#keyframes): Spec for specifying values at certain key points in an animation.
- [`repeatable`](https://developer.android.com/develop/ui/compose/animation/customize#repeatable): Duration-based spec that runs a certain number of times, specified by `RepeatMode`.
- [`infiniteRepeatable`](https://developer.android.com/develop/ui/compose/animation/customize#infiniterepeatable): Duration-based spec that runs forever.
- [`snap`](https://developer.android.com/develop/ui/compose/animation/customize#snap): Instantly snaps to the end value without any animation.

![Write your alt text here](https://developer.android.com/static/develop/ui/compose/images/animations/animated_spec_set.gif) **Figure 16.** No spec set vs Custom Spring spec set

Read the full documentation for more information about [animationSpecs](https://developer.android.com/develop/ui/compose/animation/customize#animationspec).

## Additional resources

For more examples of fun animations in Compose, take a look at the following:

- [5 quick animations in Compose](https://www.youtube.com/watch?v=0mfCbXrYBPE&t=2s&ab_channel=AndroidDevelopers)
- [Making Jellyfish move in Compose](https://medium.com/androiddevelopers/making-jellyfish-move-in-compose-animating-imagevectors-and-applying-agsl-rendereffects-3666596a8888)
- [Customizing `AnimatedContent` in Compose](https://medium.com/androiddevelopers/customizing-animatedcontent-in-jetpack-compose-629c67b45894)
- [Easing into Easing functions in Compose](https://medium.com/androiddevelopers/easing-in-to-easing-curves-in-jetpack-compose-d72893eeeb4d)