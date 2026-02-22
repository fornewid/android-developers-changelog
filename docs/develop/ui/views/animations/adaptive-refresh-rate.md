---
title: https://developer.android.com/develop/ui/views/animations/adaptive-refresh-rate
url: https://developer.android.com/develop/ui/views/animations/adaptive-refresh-rate
source: md.txt
---

| **Caution:** Adaptive refresh rate is supported on devices that implement [specific
| HAL APIs](https://source.android.com/docs/core/graphics/arr#implementation) and run on Android 15-QPR1 and above. To check device support, use the [`hasArrSupport()`](https://developer.android.com/reference/android/view/Display#hasArrSupport()) API.

When an animation is initiated in Android, the display often boosts to the
maximum refresh rate to ensure a smooth experience. For small animations such as
progress bars and audio visualizers, this high refresh rate is unnecessary, and
results in high power consumption.

Starting in Android 15, with the adaptive refresh rate (ARR) feature, enabled
devices can reduce high refresh rate residency on two fronts:

- With new platform frame rate management optimizations, apps can render at a lower frame rate by default and only boost to a high frame rate when necessary.
- The display refresh rate dynamically matches the content render rate without jank.

While most apps should benefit from ARR without
any modifications, you can also override the default frame rate behavior as
needed.

This page describes the following:

- How each View's frame rate is determined.
- The general policy for how ARR determines what the frame rate is set to.
- How you can manually override the default frame rate behavior.

## The View voting mechanism

In Android's View system, each View in the UI hierarchy can express its
preferred frame rate. These preferences are collected and combined to determine
a final frame rate for each frame. This is achieved through a voting mechanism
where each View votes based on its frame rate attribute, which can be a category
or a specific rate. Views typically vote when drawn or updated. These votes are
combined to determine a final frame rate, which is then sent to the lower-level
layer as a hint for rendering.

Currently, most Views default to a "Normal" frame rate, which is often set
to 60 Hz. For higher frame rates, you can use specific
APIs to customize preferences, with the system generally selecting the highest
frame rate. For more information about using these APIs, see the [Set the frame
rate or category](https://developer.android.com/develop/ui/views/animations/adaptive-refresh-rate#set-frame) section. The general policies surrounding frame
rates are described in the [General ARR policy](https://developer.android.com/develop/ui/views/animations/adaptive-refresh-rate#general-adaptive) section.

### Frame rate categories

In the [`View`](https://developer.android.com/reference/android/view/View) class, there are different frame rate categories that can be
used in the vote. The description of each category is as follows:

- [`REQUESTED_FRAME_RATE_CATEGORY_DEFAULT`](https://developer.android.com/reference/android/view/View#REQUESTED_FRAME_RATE_CATEGORY_DEFAULT): This value can be set to return to default behavior, indicating that this View has no data for the frame rate.
- [`REQUESTED_FRAME_RATE_CATEGORY_NO_PREFERENCE`](https://developer.android.com/reference/android/view/View#REQUESTED_FRAME_RATE_CATEGORY_NO_PREFERENCE): The View will explicitly not influence the frame rate. This means that, even if the View is active, the framework will not consider it when determining the frame rate
- [`REQUESTED_FRAME_RATE_CATEGORY_NORMAL`](https://developer.android.com/reference/android/view/View#REQUESTED_FRAME_RATE_CATEGORY_NORMAL): Indicates a middle frame rate suitable for animations that don't require higher frame rates, or don't benefit from high smoothness. This is normally 60 Hz or close to it.
- [`REQUESTED_FRAME_RATE_CATEGORY_HIGH`](https://developer.android.com/reference/android/view/View#REQUESTED_FRAME_RATE_CATEGORY_HIGH): Indicates a frame rate suitable for animations that require a high frame rate, which may increase smoothness but may also increase power usage.

A View votes only if it requires redrawing. The final frame rate is determined
by the highest vote. For example, if all votes are for "Normal," "Normal"
is selected. When both "Normal" and "High" votes occur, "High" is chosen.

### Frame rate

In addition to frame rate categories, a View can also specify a preferred frame
rate, such as 30, 60, or 120 Hz. When multiple frame rate votes are cast, the
final frame rate is determined by the following rules:

- **Multiples of each other**: If the voted frame rates are multiples of one another, the highest value is chosen. For example, if there are two votes - 30 Hz and 90 Hz --- 90 Hz is selected as the final frame rate.
- **Not multiples of each other** :
  - If any of the votes is greater than 60 Hz, it counts as a "High" vote.
  - If all the votes are 60 Hz or lower, it counts as a "Normal" vote.

Additionally, if there is a combination of both frame rate values and frame rate
categories, the higher value typically determines the final render rate. For
example, with a combination of a 60 Hz vote and a "High" vote, or a 120 Hz vote
and a "Normal" vote, the render rate would typically be set to 120 Hz.

In addition to the votes from an app, there may also be other hints sent
to the lower-level layer from different components within the same frame. Many
of these can originate from System UI components, such as the notification
shade, status bar, navigation bar, and others. The final frame rate values are
determined based on the votes from multiple components.
| **Note:** The actual implementation is subject to change.

### Set the frame rate or category

Under certain circumstances, you may have a preferred frame rate for a View. For
example, you can set the preferred frame rate to "High" for a View to increase
the frame rate if an animation appears unsmooth. Additionally, if there is a
slow or static animation over a video (typically played at 24 or 30 Hz), you may
prefer the animation to run at a rate lower than "Normal" to reduce power
consumption.

You can use the [`setRequestedFrameRate()`](https://developer.android.com/reference/android/view/View#setRequestedFrameRate(float)) and
[`getRequestedFrameRate()`](https://developer.android.com/reference/android/view/View#getRequestedFrameRate()) APIs to designate the preferred frame rate or
category of a given View.  

### Kotlin

```kotlin
// Set the preferred frame rate category to a View

// set the frame rate category to NORMAL
view.requestedFrameRate = View.REQUESTED_FRAME_RATE_CATEGORY_NORMAL
// set the frame rate category to HIGH
view.requestedFrameRate = View.REQUESTED_FRAME_RATE_CATEGORY_HIGH
// reset the frame rate category
view.requestedFrameRate = View.REQUESTED_FRAME_RATE_CATEGORY_DEFAULT

// Set the preferred frame rate to a View

// set the frame rate to 30
view.requestedFrameRate = 30f
// set the frame rate to 60
view.requestedFrameRate = 60f
// set the frame rate to 120
view.requestedFrameRate = 120f
```

### Java

```java
// Set the preferred frame rate category to a View

// set the frame rate category to NORMAL
view.setRequestedFrameRate(View.REQUESTED_FRAME_RATE_CATEGORY_NORMAL);
// set the frame rate category to HIGH
view.setRequestedFrameRate(View.REQUESTED_FRAME_RATE_CATEGORY_HIGH);
// reset the frame rate category
view.setRequestedFrameRate(View.REQUESTED_FRAME_RATE_CATEGORY_DEFAULT);

// Set the preferred frame rate to a View

// set the frame rate to 30
view.setRequestedFrameRate(30);
// set the frame rate to 60
view.setRequestedFrameRate(60);
// set the frame rate to 120
view.setRequestedFrameRate(120);
```

For example usage, see [`TextureView`](https://android.googlesource.com/platform/frameworks/base/+/refs/heads/main/core/java/android/view/TextureView.java#488).
| **Note:** When `setRequestedFrameRate` is called on a `ViewGroup`, the specified value does not automatically propagate to its child Views.

## General ARR policy

In the previous section, we discussed that most animations are displayed at 60
Hz by default, as each View has "Normal" set as the preferred frame rate.
However, there are exceptions where the frame rate is increased to "High" to
ensure smoother animations.

The general ARR policy is as follows:

- **Touch boost** : When a touch event ([`MotionEvent.ACTION_DOWN`](https://developer.android.com/reference/android/view/MotionEvent#ACTION_DOWN)) is detected, the refresh rate is boosted to "High" for some time after the touch has been released to maintain responsiveness.
- **Fling gestures** : Fling gestures are handled differently---the refresh rate decreases gradually as the fling velocity slows down. You can find details about this behavior in the [Scrolling improvement](https://developer.android.com/develop/ui/views/animations/adaptive-refresh-rate#scrolling-improvement) section.
- **App launch and window transitions**: The refresh rate is also boosted for some time during app launches, window initialization, and window transitions to ensure a smooth visual experience.
- **Animations**: Animations that involve movement or size changes automatically receive a higher refresh rate to enhance smoothness when the position or size of a View changes.
- **`SurfaceView`** and **`TextureView`** : [Frame rates](https://developer.android.com/media/optimize/performance/frame-rate) explicitly set for [`TextureView`](https://developer.android.com/reference/android/view/TextureView) and [`SurfaceView`](https://developer.android.com/reference/android/view/SurfaceView) are respected and applied accordingly.

## Enable and disable touch boost

You can enable and/or disable touch boost at the `Window` level. By default,
when a user touches and lifts their finger from the screen, the render rate
increases for some time. The [`setFrameRateBoostOnTouchEnabled()`](https://developer.android.com/reference/kotlin/android/view/Window#setframerateboostontouchenabled) and
[`getFrameRateBoostOnTouchEnabled()`](https://developer.android.com/reference/kotlin/android/view/Window#getframerateboostontouchenabled) APIs allow you to prevent the render
rate from increasing when a specific [`Window`](https://developer.android.com/reference/android/view/Window) is touched.
**Note:** Disabling touch boost behavior is not recommended, as it could significantly impact user experience.  

### Kotlin

```kotlin
// disable touch boost on a Window
window.isFrameRateBoostOnTouchEnabled = false 
// enable touch boost on a Window
window.isFrameRateBoostOnTouchEnabled = true
// check if touch boost is enabled on a Window
val isTouchBoostEnabled = window.isFrameRateBoostOnTouchEnabled
```

### Java

```java
// disable touch boost on a Window
window.setFrameRateBoostOnTouchEnabled(false)
// enable touch boost on a Window
window.setFrameRateBoostOnTouchEnabled(true)
// check if touch boost is enabled on a Window
window.getFrameRateBoostOnTouchEnabled()
```

## Scrolling improvement

One key use case for optimizing frame rate dynamically is to improve the
scrolling (fling) experience. Many applications rely heavily on users swiping up
to view new content. The ARR scrolling enhancement dynamically
adjusts the refresh rate as the fling gesture slows down, gradually reducing the
frame rate. This provides a more efficient rendering while maintaining smooth
scrolling.
| **Note:** For the scrolling improvement feature, the frame rate is dynamically adjusted only after you lift your finger. While touching the screen, touch boost is still triggered to maintain a higher frame rate.

This improvement applies specifically to scrollable UI components, including
[`ScrollView`](https://developer.android.com/reference/android/widget/ScrollView), [`ListView`](https://developer.android.com/reference/android/widget/ListView), and [`GridView`](https://developer.android.com/reference/android/widget/GridView), and may not be
available for all custom implementations.

The ARR scrolling feature is available for `RecyclerView` and
`NestedScrollView`. To enable this feature in your app, upgrade to the latest
versions of `AndroidX.recyclerview` and `AndroidX.core`. See the following table
for details.

|---|---|
| **Library** | **Version** |
| `AndroidX.recyclerview` | 1.4.0 |
| `AndroidX.core` | 1.15.0 |

### Set the velocity information

If you have a custom scrollable component and want to take advantage of the
scrolling feature, call [`setFrameContentVelocity()`](https://developer.android.com/reference/android/view/View#setFrameContentVelocity(float)) on every frame while
smooth scrolling or flinging. See the following code snippet for an example:  

### Kotlin

```kotlin
// set the velocity to a View (1000 pixels/Second)
view.frameContentVelocity = 1000f
// get the velocity of a View
val velocity = view.frameContentVelocity
```

### Java

```java
// set the velocity to a View
view.setFrameContentVelocity(velocity);

// get the velocity of a View
final float velocity = view.getFrameContentVelocity()
```

For more examples, see [`RecyclerView`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:recyclerview/recyclerview/src/main/java/androidx/recyclerview/widget/RecyclerView.java;l=6011;drc=33540bc9032cb4ef2ce1e0f165a39386bd71088b) and
[`ScrollView`](https://android.googlesource.com/platform/frameworks/base/+/refs/heads/main/core/java/android/widget/ScrollView.java#734). To correctly set the velocity, calculate the
content velocity (pixels per second) manually if the required information cannot
be obtained from [`Scroller`](https://source.corp.google.com/h/googleplex-android/platform/superproject/main/+/main:frameworks/base/core/ajava/android/widget/Scroller.java) or
[`OverScroller`](https://source.corp.google.com/h/googleplex-android/platform/superproject/main/+/main:frameworks/base/core/java/android/widget/OverScroller.java).

Note that, if [`setFrameContentVelocity()`](https://developer.android.com/reference/android/view/View#setFrameContentVelocity(float)) and
[`getFrameContentVelocity()`](https://developer.android.com/reference/android/view/View#getFrameContentVelocity()) are called on Views that are not scrollable
components, they won't have any effect, as movement automatically triggers an
increased frame rate based on the current policy.
| **Caution:** The velocity information is reset each time a View is redrawn. To ensure proper functionality, update the velocity every frame during a fling gesture.

The velocity information is crucial for adjusting the render rate. For example,
consider the fling gesture. In the beginning, the velocity of a fling can be
high, necessitating a higher render rate to ensure smoothness. As the gesture
progresses, the velocity decreases, allowing the render rate to be lowered.

### Enable and disable ARR

ARR is enabled by default to enhance power efficiency. While
you can disable this feature, it is not recommended, as the app would consume
more power. Only consider disabling this feature if you encounter issues that
significantly impact user experience.

To enable or disable ARR, use the
[`setFrameRatePowerSavingsBalanced()`](https://developer.android.com/reference/kotlin/android/view/Window#setframeratepowersavingsbalanced) API on a `Window`, or use the
[`isFrameRatePowerSavingsBalanced()`](https://developer.android.com/reference/kotlin/android/view/Window#isFrameRatePowerSavingsBalanced()) API through your `styles.xml` file.

The following snippet shows how to enable or disable ARR on a `Window`:  

### Kotlin

```kotlin
// disable ARR on a Window
window.isFrameRatePowerSavingsBalanced = false 
// enable ARR on a Window
window.isFrameRatePowerSavingsBalanced = true  
// check if ARR is enabled on a Window
val isAdaptiveRefreshRateEnabled = window.isFrameRatePowerSavingsBalanced
```

### Java

```java
// disable ARR on a Window
window.setFrameRatePowerSavingsBalanced(false)
// enable ARR on a Window
window.setFrameRatePowerSavingsBalanced(true)
// check if ARR is enabled on a Window
window.isFrameRatePowerSavingsBalanced()
```

To disable ARR through the `styles.xml` file, add the
following item to your style in `res/values/styles.xml`:  

    <style name="frameRatePowerSavingsBalancedDisabled">
        <item name="android:windowIsFrameRatePowerSavingsBalanced">false</item>
    </style>

## ARR for Compose

Compose 1.9 also adds support for adaptive refresh rate.
In the View system, you use the [`setRequestedFrameRate()`](https://developer.android.com/reference/android/view/View#setRequestedFrameRate(float)) method to
request a specific frame rate for a View. In Compose, a new modifier lets you
specify the frame rate for a composable. This modifier functions
similarly to [`setRequestedFrameRate()`](https://developer.android.com/reference/android/view/View#setRequestedFrameRate(float)), accepting either a positive
frame rate value (in Hz) or a predefined frame rate category,
[`FrameRateCategory`](https://developer.android.com/reference/kotlin/androidx/compose/ui/FrameRateCategory).

The signatures for the APIs are as follows:

- [`Modifier.preferredFrameRate(frameRate: Float)`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).preferredFrameRate(kotlin.Float))
- [`Modifier.preferredFrameRate(frameRateCategory: FrameRateCategory)`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).preferredFrameRate(androidx.compose.ui.FrameRateCategory))

In the snippet below, the new frame rate modifier `(Modifier.requestedFrameRate(120f))` is applied to a `Text` composable. This modifier causes the `Text` composable to request a preferred frame rate of 120 when drawn or animating (for example, with opacity changes):  

    var targetAlpha by remember { mutableFloatStateOf(1f) }
    val alpha by
        animateFloatAsState(
            targetValue = targetAlpha,
            animationSpec = tween(durationMillis = 1000)
        )

    Button(
        onClick = { targetAlpha = if (targetAlpha == 1f) 0.2f else 1f },
        modifier =
            Modifier.background(LocalContentColor.current.copy(alpha = alpha))
    ) {
        Text(
            text = "Click",
            color = LocalContentColor.current.copy(alpha = alpha),
            modifier = Modifier.preferredFrameRate(120f)
         // You can also pass frame rate category such as FrameRateCategory.High  to increase the frame rate
        )
      }

The preferred frame rates from all composables are then collected and
consolidated to determine the final frame rate for each frame. For more details,
see [`SetFrameRateSample`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/ui/ui/samples/src/main/java/androidx/compose/ui/samples/SetFrameRateSample.kt) and
[`SetFrameRateCategorySample`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/ui/ui/samples/src/main/java/androidx/compose/ui/samples/SetFrameRateCategorySample.kt).