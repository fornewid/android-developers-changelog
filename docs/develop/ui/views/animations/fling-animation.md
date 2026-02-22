---
title: https://developer.android.com/develop/ui/views/animations/fling-animation
url: https://developer.android.com/develop/ui/views/animations/fling-animation
source: md.txt
---

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to use Animations in Compose.  
[Spring AnimationSpec →](https://developer.android.com/jetpack/compose/animation#spring)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)


Fling-based animation uses a friction force that is proportional to an
object's velocity. Use it to animate a property of an object and
to end the animation gradually. It has an initial momentum, which is
mostly received from the gesture velocity, and gradually slows down. The
animation comes to an end when the velocity of the animation is low enough
that it makes no visible change on the device screen.
![](https://developer.android.com/static/images/guide/topics/graphics/fling-animation.gif) **Figure 1.** Fling animation


To learn about related topics, read the following guides:

- [Physics-based
  motion](https://developer.android.com/training/animation/overview#physics-based)
- [Animate movement
  using spring physics](https://developer.android.com/guide/topics/graphics/spring-animation)

## Add the AndroidX library

To use the physics-based animations, you must add the AndroidX library to your project
as follows:

1. Open the `build.gradle` file for your app module.
2. Add the AndroidX library to the `dependencies` section.  

   ### Groovy

   ```groovy
           dependencies {
               implementation 'androidx.dynamicanimation:dynamicanimation:1.0.0'
           }
           
   ```

   ### Kotlin

   ```kotlin
           dependencies {
               implementation("androidx.dynamicanimation:dynamicanimation:1.0.0")
           }
           
   ```

## Create a fling animation


The [FlingAnimation](https://developer.android.com/reference/androidx/dynamicanimation/animation/FlingAnimation) class lets you create
a fling animation for an object. To build a fling animation, create an
instance of the [FlingAnimation](https://developer.android.com/reference/androidx/dynamicanimation/animation/FlingAnimation) class and
provide an object and the object's property that you want to animate.  

### Kotlin

```kotlin
val fling = FlingAnimation(view, DynamicAnimation.SCROLL_X)
```

### Java

```java
FlingAnimation fling = new FlingAnimation(view, DynamicAnimation.SCROLL_X);
```

## Set velocity


The starting velocity defines the speed at which an animation property
changes at the beginning of the animation. The default starting velocity is
set to zero pixels per second. Therefore, you must define a start velocity
to ensure the animation does not end right away.


You can use a fixed value as the starting velocity, or you can base it off
of the velocity of a touch gesture. If you choose to provide a fixed value,
you should define the value in dp per second, then convert it to pixels
per second. Defining the value in dp per second allows the velocity to be
independent of a device's density and form factors. For more information about
converting the starting velocity to pixels per second, refer to the
[Converting
dp per second to pixels per second](https://developer.android.com/topic/libraries/support-library/preview/spring-animation#converting-value) section in
[Spring Animation](https://developer.android.com/topic/libraries/support-library/preview/spring-animation).


To set the velocity, call the `setStartVelocity()` method and pass
the velocity in pixels per second. The method returns the fling object on
which the velocity is set.

**Note:** Use the
[GestureDetector.OnGestureListener](https://developer.android.com/reference/android/view/GestureDetector.OnGestureListener) and the
[VelocityTracker](https://developer.android.com/reference/android/view/VelocityTracker) classes to retrieve and compute
the velocity of touch gestures, respectively.

### Set an animation value range


You can set the minimum and the maximum animation values when you want to
restrain the property value to a certain range. This range control is
particularly useful when you animate properties that have an intrinsic
range, such as alpha (from 0 to 1).

**Note**: When the value of a fling animation reaches the
minimum or maximum value, the animation ends.


To set the minimum and maximum values, call the `setMinValue()`
and `setMaxValue()` methods, respectively.
Both methods return the animation object for which you have set the value.

### Set friction


The `setFriction()` method lets you change the animation's
friction. It defines how quickly the velocity decreases in an animation.

**Note**: If you don't set the friction at the beginning of
the animation, the animation uses a default friction value of 1.


The method returns the object whose animation uses the friction value you
provide.

#### Sample code


The example below illustrates a horizontal fling. The velocity captured from
the velocity tracker is `velocityX` and, the scroll bounds are
set to 0 and
maxScroll. The friction is set to 1.1.  

### Kotlin

```kotlin
FlingAnimation(view, DynamicAnimation.SCROLL_X).apply {
    setStartVelocity(-velocityX)
    setMinValue(0f)
    setMaxValue(maxScroll)
    friction = 1.1f
    start()
}
```

### Java

```java
FlingAnimation fling = new FlingAnimation(view, DynamicAnimation.SCROLL_X);
fling.setStartVelocity(-velocityX)
        .setMinValue(0)
        .setMaxValue(maxScroll)
        .setFriction(1.1f)
        .start();
```

### Set the minimum visible change


When you animate a custom property that isn't defined in pixels, you should set the
minimal change of animation value that is visible to users. It
determines a reasonable threshold for ending the animation.

It isn't necessary to call this method when animating
[DynamicAnimation.ViewProperty](https://developer.android.com/reference/androidx/dynamicanimation/animation/DynamicAnimation.ViewProperty) because the
minimum visible change is derived from the property. For example:

- The default minimum visible change value is 1 pixel for view properties such as `TRANSLATION_X`, `TRANSLATION_Y`, `TRANSLATION_Z`, `SCROLL_X`, and `SCROLL_Y`.
- For animations that use rotation, such as `ROTATION`, `ROTATION_X`, and `ROTATION_Y`, the minimum visible change is `MIN_VISIBLE_CHANGE_ROTATION_DEGREES`, or 1/10 pixel.
- For animations that use opacity, the minimum visible change is `MIN_VISIBLE_CHANGE_ALPHA`, or 1/256.


To set the minimum visible change for an animation, call the
`setMinimumVisibleChange()` method and pass either
one of the minimum visible constants or a value that you need to calculate
for a custom property. For more information on calculating this value,
refer to the
[Calculating a minimum visible change value](https://developer.android.com/develop/ui/views/animations/fling-animation#calculating-mvc-value)
section.  

### Kotlin

```kotlin
anim.minimumVisibleChange = DynamicAnimation.MIN_VISIBLE_CHANGE_SCALE
```

### Java

```java
anim.setMinimumVisibleChange(DynamicAnimation.MIN_VISIBLE_CHANGE_SCALE);
```

**Note**: You need to pass a value only when you animate a
custom property that is not defined in pixels.

#### Calculating a minimum visible change value


To calculate the minimum visible change value for a custom property, use the
following formula:

Minimum visible change = Range of custom property value / Range of
animiation in pixels


For example, the property that you want to animate progresses from 0 to
100. This corresponds to a 200-pixel change. Per the formula, the minimum
visible change value is 100 / 200 is equal to 0.5 pixels.