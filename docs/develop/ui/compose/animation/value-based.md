---
title: https://developer.android.com/develop/ui/compose/animation/value-based
url: https://developer.android.com/develop/ui/compose/animation/value-based
source: md.txt
---

This page describes how to create value-based animations in Jetpack Compose,
focusing on APIs that animate values based on their current and target states.

## Animate a single value with `animate*AsState`

The [`animate*AsState`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/package-summary#animateDpAsState(androidx.compose.ui.unit.Dp,androidx.compose.animation.core.AnimationSpec,kotlin.String,kotlin.Function1)) functions are straightforward animation APIs in
Compose for animating a single value. You provide only the target value
(or end value), and the API starts animation from the current value to the
specified value.

The following example animates alpha using this API. By wrapping the target
value in [`animateFloatAsState`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/package-summary#animateFloatAsState(kotlin.Float,androidx.compose.animation.core.AnimationSpec,kotlin.Float,kotlin.String,kotlin.Function1)), the alpha value is now an animation value
between the provided values (`1f` or `0.5f` in this case).


```kotlin
var enabled by remember { mutableStateOf(true) }

val animatedAlpha: Float by animateFloatAsState(if (enabled) 1f else 0.5f, label = "alpha")
Box(
    Modifier
        .fillMaxSize()
        .graphicsLayer { alpha = animatedAlpha }
        .background(Color.Red)
)
```

<br />

You don't need to create an instance of any animation class or handle
interruption. Under the hood, an animation object (namely, an `Animatable`
instance) will be created and remembered at the call site, with the first target
value as its initial value. From there on, any time you supply this composable a
different target value, an animation is automatically started towards that
value. If there's already an animation in flight, the animation starts from its
current value (and velocity) and animates toward the target value. During the
animation, this composable gets recomposed and returns an updated animation
value every frame.

By default, Compose provides `animate*AsState` functions for `Float`, `Color`,
`Dp`, `Size`, `Offset`, `Rect`, `Int`, `IntOffset`, and `IntSize`. You can add
support for other data types by providing a `TwoWayConverter` to
`animateValueAsState` that takes a generic type.

You can customize the animation specifications by providing an
[`AnimationSpec`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/AnimationSpec). See [`AnimationSpec`](https://developer.android.com/develop/ui/compose/animation/customize#animationspec) for more information.

## Animate multiple properties simultaneously with a transition

[`Transition`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/Transition) manages one or more animations as its children and runs them
simultaneously between multiple states.

The states can be any data type. In many cases, you can use a custom `enum`
type to verify type safety, as in this example:


```kotlin
enum class BoxState {
    Collapsed,
    Expanded
}
```

<br />

[`updateTransition`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/package-summary#updateTransition(kotlin.Any,kotlin.String)) creates and remembers an instance of `Transition` and
updates its state.


```kotlin
var currentState by remember { mutableStateOf(BoxState.Collapsed) }
val transition = updateTransition(currentState, label = "box state")
```

<br />

You can then use one of `animate*` extension functions to define a child
animation in this transition. Specify the target values for each of the states.
These `animate*` functions return an animation value that is updated every frame
during the animation when the transition state is updated with
`updateTransition`.


```kotlin
val rect by transition.animateRect(label = "rectangle") { state ->
    when (state) {
        BoxState.Collapsed -> Rect(0f, 0f, 100f, 100f)
        BoxState.Expanded -> Rect(100f, 100f, 300f, 300f)
    }
}
val borderWidth by transition.animateDp(label = "border width") { state ->
    when (state) {
        BoxState.Collapsed -> 1.dp
        BoxState.Expanded -> 0.dp
    }
}
```

<br />

Optionally, you can pass a `transitionSpec` parameter to specify a different
`AnimationSpec` for each of the combinations of transition state changes. See
[`AnimationSpec`](https://developer.android.com/develop/ui/compose/animation/customize#animationspec) for more information.


```kotlin
val color by transition.animateColor(
    transitionSpec = {
        when {
            BoxState.Expanded isTransitioningTo BoxState.Collapsed ->
                spring(stiffness = 50f)

            else ->
                tween(durationMillis = 500)
        }
    }, label = "color"
) { state ->
    when (state) {
        BoxState.Collapsed -> MaterialTheme.colorScheme.primary
        BoxState.Expanded -> MaterialTheme.colorScheme.background
    }
}
```

<br />

Once a transition has arrived at the target state, `Transition.currentState` is
the same as `Transition.targetState`. You can use this as a signal for whether
the transition has finished.

Sometimes, you might want to have an initial state different from the first
target state. You can use `updateTransition` with `MutableTransitionState` to
achieve this. For example, it lets you start animation as soon as the code
enters composition.


```kotlin
// Start in collapsed state and immediately animate to expanded
var currentState = remember { MutableTransitionState(BoxState.Collapsed) }
currentState.targetState = BoxState.Expanded
val transition = rememberTransition(currentState, label = "box state")
// ......https://github.com/android/snippets/blob/bbf4e1ff2570641546d50270b121493ef1965774/compose/snippets/src/main/java/com/example/compose/snippets/animations/AnimationSnippets.kt#L467-L471
```

<br />

For a more complex transition involving multiple composable functions, you can
use [`createChildTransition`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/Transition#(androidx.compose.animation.core.Transition).createChildTransition(kotlin.String,kotlin.Function1)) to create a child transition. This technique is
useful for separating concerns among multiple subcomponents in a complex
composable. The parent transition is aware of all the animation values in the
child transitions.


```kotlin
enum class DialerState { DialerMinimized, NumberPad }

@Composable
fun DialerButton(isVisibleTransition: Transition<Boolean>) {
    // `isVisibleTransition` spares the need for the content to know
    // about other DialerStates. Instead, the content can focus on
    // animating the state change between visible and not visible.
}

@Composable
fun NumberPad(isVisibleTransition: Transition<Boolean>) {
    // `isVisibleTransition` spares the need for the content to know
    // about other DialerStates. Instead, the content can focus on
    // animating the state change between visible and not visible.
}

@Composable
fun Dialer(dialerState: DialerState) {
    val transition = updateTransition(dialerState, label = "dialer state")
    Box {
        // Creates separate child transitions of Boolean type for NumberPad
        // and DialerButton for any content animation between visible and
        // not visible
        NumberPad(
            transition.createChildTransition {
                it == DialerState.NumberPad
            }
        )
        DialerButton(
            transition.createChildTransition {
                it == DialerState.DialerMinimized
            }
        )
    }
}
```

<br />

### Use transition with `AnimatedVisibility` and `AnimatedContent`

[`AnimatedVisibility`](https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#(androidx.compose.animation.core.Transition).AnimatedVisibility(kotlin.Function1,androidx.compose.ui.Modifier,androidx.compose.animation.EnterTransition,androidx.compose.animation.ExitTransition,kotlin.Function1)) and [`AnimatedContent`](https://developer.android.com/reference/kotlin/androidx/compose/animation/package-summary#(androidx.compose.animation.core.Transition).AnimatedContent(androidx.compose.ui.Modifier,kotlin.Function1,androidx.compose.ui.Alignment,kotlin.Function2)) are available as extension
functions of `Transition`. The `targetState` for `Transition.AnimatedVisibility`
and `Transition.AnimatedContent` is derived from the `Transition`, and trigger
enter, exit, and `sizeTransform` animations as needed when the `Transition`'s
`targetState` changes. These extension functions let you hoist all enter, exit,
and `sizeTransform` animations that would otherwise be internal to
`AnimatedVisibility`/`AnimatedContent` into the `Transition`. With these
extension functions, you can observe `AnimatedVisibility`/`AnimatedContent`'s
state change from outside. Instead of a boolean `visible` parameter, this
version of `AnimatedVisibility` takes a lambda that converts the parent
transition's target state into a boolean.

See [`AnimatedVisibility`](https://developer.android.com/develop/ui/compose/animation/composables-modifiers#animatedvisibility) and [`AnimatedContent`](https://developer.android.com/develop/ui/compose/animation/composables-modifiers#animatedcontent) for the details.


```kotlin
var selected by remember { mutableStateOf(false) }
// Animates changes when `selected` is changed.
val transition = updateTransition(selected, label = "selected state")
val borderColor by transition.animateColor(label = "border color") { isSelected ->
    if (isSelected) Color.Magenta else Color.White
}
val elevation by transition.animateDp(label = "elevation") { isSelected ->
    if (isSelected) 10.dp else 2.dp
}
Surface(
    onClick = { selected = !selected },
    shape = RoundedCornerShape(8.dp),
    border = BorderStroke(2.dp, borderColor),
    shadowElevation = elevation
) {
    Column(
        modifier = Modifier
            .fillMaxWidth()
            .padding(16.dp)
    ) {
        Text(text = "Hello, world!")
        // AnimatedVisibility as a part of the transition.
        transition.AnimatedVisibility(
            visible = { targetSelected -> targetSelected },
            enter = expandVertically(),
            exit = shrinkVertically()
        ) {
            Text(text = "It is fine today.")
        }
        // AnimatedContent as a part of the transition.
        transition.AnimatedContent { targetState ->
            if (targetState) {
                Text(text = "Selected")
            } else {
                Icon(imageVector = Icons.Default.Phone, contentDescription = "Phone")
            }
        }
    }
}
```

<br />

### Encapsulate a transition and make it reusable

For straightforward use cases, defining transition animations in the same
composable as your UI is a valid option. When working on a complex component
with a number of animated values, however, you might want to separate the
animation implementation from the composable UI.

You can do so by creating a class that holds all the animation values and an
`update` function that returns an instance of that class. You can extract the
transition implementation into the new separate function. This pattern is useful
when you need to centralize the animation logic or make complex animations
reusable.


```kotlin
enum class BoxState { Collapsed, Expanded }

@Composable
fun AnimatingBox(boxState: BoxState) {
    val transitionData = updateTransitionData(boxState)
    // UI tree
    Box(
        modifier = Modifier
            .background(transitionData.color)
            .size(transitionData.size)
    )
}

// Holds the animation values.
private class TransitionData(
    color: State<Color>,
    size: State<Dp>
) {
    val color by color
    val size by size
}

// Create a Transition and return its animation values.
@Composable
private fun updateTransitionData(boxState: BoxState): TransitionData {
    val transition = updateTransition(boxState, label = "box state")
    val color = transition.animateColor(label = "color") { state ->
        when (state) {
            BoxState.Collapsed -> Color.Gray
            BoxState.Expanded -> Color.Red
        }
    }
    val size = transition.animateDp(label = "size") { state ->
        when (state) {
            BoxState.Collapsed -> 64.dp
            BoxState.Expanded -> 128.dp
        }
    }
    return remember(transition) { TransitionData(color, size) }
}
```

<br />

## Create an infinitely repeating animation with `rememberInfiniteTransition`

[`InfiniteTransition`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/InfiniteTransition) holds one or more child animations like `Transition`,
but the animations start running as soon as they enter the composition and don't
stop unless they're removed. You can create an instance of `InfiniteTransition`
with `rememberInfiniteTransition`, and add child animations with `animateColor`,
`animatedFloat`, or `animatedValue`. You also need to specify an
`infiniteRepeatable` to specify the animation specifications.


```kotlin
val infiniteTransition = rememberInfiniteTransition(label = "infinite")
val color by infiniteTransition.animateColor(
    initialValue = Color.Red,
    targetValue = Color.Green,
    animationSpec = infiniteRepeatable(
        animation = tween(1000, easing = LinearEasing),
        repeatMode = RepeatMode.Reverse
    ),
    label = "color"
)

Box(
    Modifier
        .fillMaxSize()
        .background(color)
)
```

<br />

## Low-level animation APIs

All the high-level animation APIs mentioned in the preceding section build on
the low-level animation APIs.

The `animate*AsState` functions are straightforward APIs that render an instant
value change as an animation value. This functionality is backed by
`Animatable`, a coroutine-based API for animating a single value.

`updateTransition` creates a transition object that can manage multiple
animating values and run them when a state changes. `rememberInfiniteTransition`
is similar, but it creates an infinite transition that can manage multiple
animations that continue indefinitely. All of these APIs are composables except
for `Animatable`, which means you can create these animations outside of
composition.

All these APIs are based on the more fundamental `Animation` API. Though most
apps won't interact directly with `Animation`, you can access some of its
customization capabilities through higher-level APIs. See [Customize
animations](https://developer.android.com/develop/ui/compose/animation/customize) for more information on `AnimationVector` and `AnimationSpec`.
![Relationship between low-level animation APIs](https://developer.android.com/static/develop/ui/compose/images/animation-low-level.svg) **Figure 1.** Relationship between low-level animation APIs.

### `Animatable`: Coroutine-based single value animation

[`Animatable`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/Animatable) is a value holder that can animate the value as it is changed
using `animateTo`. This is the API backing up the implementation of
`animate*AsState`. It ensures consistent continuation and mutual exclusiveness,
which means the value change is always continuous and Compose cancels any
ongoing animation.

Many features of `Animatable`, including `animateTo`, are suspend functions.
This means you must wrap them in an appropriate coroutine scope. For example,
you can use the `LaunchedEffect` composable to create a scope just for the
duration of the specified key value.


```kotlin
// Start out gray and animate to green/red based on `ok`
val color = remember { Animatable(Color.Gray) }
LaunchedEffect(ok) {
    color.animateTo(if (ok) Color.Green else Color.Red)
}
Box(
    Modifier
        .fillMaxSize()
        .background(color.value)
)
```

<br />

In the preceding example, you create and remember an instance of `Animatable`
with the initial value of `Color.Gray`. Depending on the value of the boolean
flag `ok`, the color animates to either `Color.Green` or `Color.Red`. Any
subsequent change to the boolean value starts an animation to the other color.
If an animation is in progress when the value changes, Compose cancels the
animation, and the new animation starts from the current snapshot value with the
current velocity.

This `Animatable` API is the underlying implementation for `animate*AsState`
mentioned in the previous section. Using `Animatable` directly offers
finer-grained control in several ways:

- First, `Animatable` can have an initial value different from its first target value. For example, the preceding code example shows a gray box at first, which immediately animates to either green or red.
- Second, `Animatable` provides more operations on the content value, specifically `snapTo` and `animateDecay`.
  - `snapTo` sets the current value to the target value immediately. This is useful when the animation is not the only source of truth and must synchronize with other states, such as touch events.
  - `animateDecay` starts an animation that slows down from the given velocity. This is useful for implementing fling behavior.

See [Gesture and animation](https://developer.android.com/develop/ui/compose/animation/advanced) for more information.

By default, `Animatable` supports `Float` and `Color`, but you can use any data
type by providing a `TwoWayConverter`. See [AnimationVector](https://developer.android.com/develop/ui/compose/animation/customize#animationvector) for more
information.

You can customize the animation specifications by providing an `AnimationSpec`.
See [`AnimationSpec`](https://developer.android.com/develop/ui/compose/animation/customize#animationspec) for more information.

### `Animation`: Manually controlled animation

[`Animation`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/Animation) is the lowest-level Animation API available. Many of the
animations we've seen so far build on `Animation`. There are two `Animation`
subtypes: [`TargetBasedAnimation`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/TargetBasedAnimation) and [`DecayAnimation`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/DecayAnimation).

Use `Animation` only to manually control the animation's time. `Animation` is
stateless, and it doesn't have any concept of lifecycle. It serves as an
animation calculation engine for higher-level APIs.

> [!NOTE]
> **Note:** Unless you need to control the timing manually, use higher-level animation APIs that build on these classes.

#### `TargetBasedAnimation`

Other APIs cover most use cases, but using `TargetBasedAnimation` directly lets
you control the animation's play time. In the following example, you manually
control the `TargetAnimation`'s play time based on the frame time provided by
`withFrameNanos`.


```kotlin
val anim = remember {
    TargetBasedAnimation(
        animationSpec = tween(200),
        typeConverter = Float.VectorConverter,
        initialValue = 200f,
        targetValue = 1000f
    )
}
var playTime by remember { mutableLongStateOf(0L) }

LaunchedEffect(anim) {
    val startTime = withFrameNanos { it }

    do {
        playTime = withFrameNanos { it } - startTime
        val animationValue = anim.getValueFromNanos(playTime)
    } while (someCustomCondition())
}
```

<br />

#### `DecayAnimation`

Unlike `TargetBasedAnimation`, [`DecayAnimation`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/DecayAnimation) doesn't require a
`targetValue` to be provided. Instead, it calculates its `targetValue` based on
the starting conditions, set by `initialVelocity` and `initialValue` and the
supplied `DecayAnimationSpec`.

Decay animations are often used after a fling gesture to slow elements to a
stop. The animation velocity starts at the value that `initialVelocityVector`
sets and slows down over time.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Customize animations](https://developer.android.com/develop/ui/compose/animation/customize)
- [Animations in Compose](https://developer.android.com/develop/ui/compose/animation/introduction)
- [Animation modifiers and composables](https://developer.android.com/develop/ui/compose/animation/composables-modifiers)