---
title: https://developer.android.com/develop/ui/compose/animation/customize
url: https://developer.android.com/develop/ui/compose/animation/customize
source: md.txt
---

Many of the Animation APIs commonly accept parameters for customizing their
behavior.

## Customize animations with the `AnimationSpec` parameter

Most animation APIs allow developers to customize animation specifications by an
optional `AnimationSpec` parameter.


```kotlin
val alpha: Float by animateFloatAsState(
    targetValue = if (enabled) 1f else 0.5f,
    // Configure the animation duration and easing.
    animationSpec = tween(durationMillis = 300, easing = FastOutSlowInEasing),
    label = "alpha"
)
```

<br />

There are different kinds of `AnimationSpec` for creating different types of
animation.

### Create physics-based animation with `spring`

`spring` creates a physics-based animation between start and end values. It
takes 2 parameters: `dampingRatio` and `stiffness`.

`dampingRatio` defines how bouncy the spring should be. The default value is
`Spring.DampingRatioNoBouncy`.
**Figure 1**. Setting different spring damping ratios.

`stiffness` defines how fast the spring should move toward the end value. The
default value is `Spring.StiffnessMedium`.
**Figure 2**. Setting different spring stiffness.


```kotlin
val value by animateFloatAsState(
    targetValue = 1f,
    animationSpec = spring(
        dampingRatio = Spring.DampingRatioHighBouncy,
        stiffness = Spring.StiffnessMedium
    ),
    label = "spring spec"
)
```

<br />

`spring` can handle interruptions more smoothly than duration-based
`AnimationSpec` types because it guarantees the continuity of velocity when
target value changes amid animations. `spring` is used as the default
AnimationSpec by many animation APIs, such as `animate*AsState` and
`updateTransition`.

For example, if we apply a `spring` config to the following animation that is
driven by user touch, when interrupting the animation as its progressing, you
can see that using `tween` doesn't respond as smoothly as using `spring`.
**Figure 3** . Setting `tween` versus `spring` specs for animation, and interrupting it.

### Animate between start and end values with easing curve with `tween`

`tween` animates between start and end values over the specified
`durationMillis` using an easing curve. `tween` is short for the word between -
as it goes *between* two values.

You can also specify `delayMillis` to postpone the start of the animation.


```kotlin
val value by animateFloatAsState(
    targetValue = 1f,
    animationSpec = tween(
        durationMillis = 300,
        delayMillis = 50,
        easing = LinearOutSlowInEasing
    ),
    label = "tween delay"
)
```

<br />

See [Easing](https://developer.android.com/develop/ui/compose/animation/customize#easing) for more information.

### Animate to specific values at certain timings with `keyframes`

`keyframes` animates based on the snapshot values specified at different
timestamps in the duration of the animation. At any given time, the animation
value will be interpolated between two keyframe values. For each of these
keyframes, Easing can be specified to determine the interpolation curve.

It is optional to specify the values at 0 ms and at the duration time. If you do
not specify these values, they default to the start and end values of the
animation, respectively.


```kotlin
val value by animateFloatAsState(
    targetValue = 1f,
    animationSpec = keyframes {
        durationMillis = 375
        0.0f at 0 using LinearOutSlowInEasing // for 0-15 ms
        0.2f at 15 using FastOutLinearInEasing // for 15-75 ms
        0.4f at 75 // ms
        0.4f at 225 // ms
    },
    label = "keyframe"
)
```

<br />

### Animate between keyframes smoothly with `keyframesWithSplines`

To create an animation that follows a smooth curve as it transitions between
values, you can use `keyframesWithSplines` instead of `keyframes` animation
specs.


```kotlin
val offset by animateOffsetAsState(
    targetValue = Offset(300f, 300f),
    animationSpec = keyframesWithSpline {
        durationMillis = 6000
        Offset(0f, 0f) at 0
        Offset(150f, 200f) atFraction 0.5f
        Offset(0f, 100f) atFraction 0.7f
    }
)
```

<br />

Spline-based keyframes are particularly useful for 2D movement of items on
screen.

The following videos showcase the differences between `keyframes` and
`keyframesWithSpline` given the same set of x, y coordinates that a circle
should follow.

| `keyframes` | `keyframesWithSplines` |
|---|---|
|   |   |

As you can see, the spline-based keyframes offer smoother transitions between
points, as they use bezier curves to smoothly animate between items. This spec
is useful for a preset animation. However,if you're working with user-driven
points, it's preferable to use springs to achieve a similar smoothness between
points because those are interruptible.

### Repeat an animation with `repeatable`

`repeatable` runs a duration-based animation (such as `tween` or `keyframes`)
repeatedly until it reaches the specified iteration count. You can pass the
`repeatMode` parameter to specify whether the animation should repeat by
starting from the beginning (`RepeatMode.Restart`) or from the end
(`RepeatMode.Reverse`).


```kotlin
val value by animateFloatAsState(
    targetValue = 1f,
    animationSpec = repeatable(
        iterations = 3,
        animation = tween(durationMillis = 300),
        repeatMode = RepeatMode.Reverse
    ),
    label = "repeatable spec"
)
```

<br />

### Repeat an animation infinitely with `infiniteRepeatable`

`infiniteRepeatable` is like `repeatable`, but it repeats for an infinite amount
of iterations.


```kotlin
val value by animateFloatAsState(
    targetValue = 1f,
    animationSpec = infiniteRepeatable(
        animation = tween(durationMillis = 300),
        repeatMode = RepeatMode.Reverse
    ),
    label = "infinite repeatable"
)
```

<br />

In tests using
[`ComposeTestRule`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/junit4/ComposeTestRule),
animations using `infiniteRepeatable` are not run. The component will be
rendered using the initial value of each animated value.

### Immediately snap to end value with `snap`

`snap` is a special `AnimationSpec` that immediately switches the value to the
end value. You can specify `delayMillis` in order to delay the start of the
animation.


```kotlin
val value by animateFloatAsState(
    targetValue = 1f,
    animationSpec = snap(delayMillis = 50),
    label = "snap spec"
)
```

<br />

> [!NOTE]
> **Note:** In the View system, you needed to use `ObjectAnimator` for duration-based animations, and `SpringAnimation` for physics-based animation. It was not straightforward to use these two different animation APIs simultaneously. `AnimationSpec` in Compose allows for to handling these in a unified manner.

## Set a custom easing function

Duration-based `AnimationSpec` operations (such as `tween` or `keyframes`) use
`Easing` to adjust an animation's fraction. This allows the animating value to
speed up and slow down, rather than moving at a constant rate. Fraction is a
value between 0 (start) and 1.0 (end) indicating the current point in the
animation.

Easing is in fact a function that takes a fraction value between 0 and 1.0 and
returns a float. The returned value can be outside the boundary to represent
overshoot or undershoot. A custom Easing can be created like the code below.


```kotlin
val CustomEasing = Easing { fraction -> fraction * fraction }

@Composable
fun EasingUsage() {
    val value by animateFloatAsState(
        targetValue = 1f,
        animationSpec = tween(
            durationMillis = 300,
            easing = CustomEasing
        ),
        label = "custom easing"
    )
    // ......
}
```

<br />

Compose provides several built-in `Easing` functions that cover most use cases.
See [Speed - Material Design](https://m3.material.io/styles/motion/easing-and-duration/applying-easing-and-duration) for more
information about what Easing to use depending on your scenario.

- `FastOutSlowInEasing`
- `LinearOutSlowInEasing`
- `FastOutLinearEasing`
- `LinearEasing`
- `CubicBezierEasing`
- [See more](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/package-summary#Ease())

> [!NOTE]
> **Note:** Easing objects work the same way as instances of `Interpolator` classes in the platform. Instead of the `getInterpolation()` method, it has the `transform()` method.

## Animate custom data types by converting to and from `AnimationVector`

Most Compose animation APIs support `Float`, `Color`, `Dp`, and other basic data
types as animation values by default, but you sometimes need to animate
other data types including your custom ones. During animation, any animating
value is represented as an `AnimationVector`. The value is converted into an
`AnimationVector` and vice versa by a corresponding `TwoWayConverter` so that
the core animation system can handle them uniformly. For example, an `Int` is
represented as an `AnimationVector1D` that holds a single float value.
`TwoWayConverter` for `Int` looks like this:


```kotlin
val IntToVector: TwoWayConverter<Int, AnimationVector1D> =
    TwoWayConverter({ AnimationVector1D(it.toFloat()) }, { it.value.toInt() })
```

<br />

`Color` is essentially a set of 4 values, red, green, blue, and alpha, so
`Color` is converted into an `AnimationVector4D` that holds 4 float values. In
this manner, every data type used in animations is converted to either
`AnimationVector1D`, `AnimationVector2D`, `AnimationVector3D`, or
`AnimationVector4D` depending on its dimensionality. This allows different
components of the object to be animated independently, each with their own
velocity tracking. Built-in converters for basic data types can be accessed
using converters such as `Color.VectorConverter` or `Dp.VectorConverter`.

When you want to add support for a new data type as an animating value, you can
create your own `TwoWayConverter` and provide it to the API. For example, you
can use `animateValueAsState` to animate your custom data type like this:


```kotlin
data class MySize(val width: Dp, val height: Dp)

@Composable
fun MyAnimation(targetSize: MySize) {
    val animSize: MySize by animateValueAsState(
        targetSize,
        TwoWayConverter(
            convertToVector = { size: MySize ->
                // Extract a float value from each of the `Dp` fields.
                AnimationVector2D(size.width.value, size.height.value)
            },
            convertFromVector = { vector: AnimationVector2D ->
                MySize(vector.v1.dp, vector.v2.dp)
            }
        ),
        label = "size"
    )
}
```

<br />

The following list includes some built-in `VectorConverter`s:

- [`Color.VectorConverter`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/Color.Companion#(androidx.compose.ui.graphics.Color.Companion).VectorConverter())
- [`Dp.VectorConverter`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/package-summary#(androidx.compose.ui.unit.Dp.Companion).VectorConverter())
- [`Offset.VectorConverter`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/package-summary#(androidx.compose.ui.geometry.Offset.Companion).VectorConverter())
- [`Int.VectorConverter`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/package-summary#(kotlin.Int.Companion).VectorConverter())
- [`Float.VectorConverter`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/package-summary#(kotlin.Float.Companion).VectorConverter())
- [`IntSize.VectorConverter`](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/package-summary#(androidx.compose.ui.unit.IntSize.Companion).VectorConverter())

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Value-based animations](https://developer.android.com/develop/ui/compose/animation/value-based)
- [Iterative code development {:#iterative-code-dev }](https://developer.android.com/develop/ui/compose/tooling/iterative-development)
- [Animations in Compose](https://developer.android.com/develop/ui/compose/animation/introduction)