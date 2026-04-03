---
title: https://developer.android.com/develop/ui/views/layout/custom-views/making-interactive
url: https://developer.android.com/develop/ui/views/layout/custom-views/making-interactive
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn how to work with layouts in Compose. [Gestures →](https://developer.android.com/jetpack/compose/touch-input/pointer-input) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)

Drawing a UI is only one part of creating a custom view. You also need to
make your view respond to user input in a way that closely resembles the
real-world action you're mimicking.

Make the objects in your app act like real objects do. For example, don't let
images in your app pop out of existence and reappear elsewhere, because objects
in the real world don't do that. Instead, move your images from one place to
another.

Users sense even subtle behavior or feel in an interface and react best to
subtleties that mimic the real world. For example, when users fling a UI object,
give them a sense of inertia at the beginning that delays the motion. At the end
of the motion, give them a sense of momentum that carries the object beyond the
fling.

This page demonstrates how to use features of the Android framework to add
these real-world behaviors to your custom view.

You can find additional related information in
[Input events overview](https://developer.android.com/guide/topics/ui/ui-events) and
[Property animation
overview](https://developer.android.com/guide/topics/graphics/prop-animation).

## Handle input gestures

Like many other UI frameworks, Android supports an input event model. User
actions turn into events that trigger callbacks, and you can override the
callbacks to customize how your app responds to the user. The most common input
event in the Android system is *touch* , which triggers
`https://developer.android.com/reference/android/view/View#onTouchEvent(android.view.MotionEvent)`.
Override this method to handle the event, as follows:

### Kotlin

```kotlin
override fun onTouchEvent(event: MotionEvent): Boolean {
    return super.onTouchEvent(event)
}
```

### Java

```java
@Override
   public boolean onTouchEvent(MotionEvent event) {
    return super.onTouchEvent(event);
   }
```

Touch events by themselves aren't particularly useful. Modern touch UIs
define interactions in terms of gestures such as tapping, pulling, pushing,
flinging, and zooming. To convert raw touch events into gestures, Android
provides
`https://developer.android.com/reference/android/view/GestureDetector`.

Construct a `GestureDetector` by passing in an instance of a class
that implements
`https://developer.android.com/reference/android/view/GestureDetector.OnGestureListener`.
If you only want to process a few gestures, you can extend
`https://developer.android.com/reference/android/view/GestureDetector.SimpleOnGestureListener`
instead of implementing the `GestureDetector.OnGestureListener`
interface. For example, this code creates a class that extends
`GestureDetector.SimpleOnGestureListener` and overrides
`https://developer.android.com/reference/android/view/GestureDetector.SimpleOnGestureListener#onDown(android.view.MotionEvent)`.

### Kotlin

```kotlin
private val myListener =  object : GestureDetector.SimpleOnGestureListener() {
    override fun onDown(e: MotionEvent): Boolean {
        return true
    }
}

private val detector: GestureDetector = GestureDetector(context, myListener)
```

### Java

```java
class MyListener extends GestureDetector.SimpleOnGestureListener {
   @Override
   public boolean onDown(MotionEvent e) {
       return true;
   }
}
detector = new GestureDetector(getContext(), new MyListener());
```

Whether or not you use `GestureDetector.SimpleOnGestureListener`,
always implement an
`https://developer.android.com/reference/android/view/GestureDetector.OnGestureListener#onDown(android.view.MotionEvent)`
method that returns `true`. This is necessary because all gestures
begin with an `onDown()` message. If you return `false`
from `onDown()`, as
`GestureDetector.SimpleOnGestureListener` does, the system assumes
you want to ignore the rest of the gesture, and the other methods of
`GestureDetector.OnGestureListener` aren't called. Only return
`false` from `onDown()` if you want to ignore an entire
gesture.

After you implement `GestureDetector.OnGestureListener` and create
an instance of `GestureDetector`, you can use your
`GestureDetector` to interpret the touch events you receive in
`https://developer.android.com/reference/android/view/GestureDetector#onTouchEvent(android.view.MotionEvent)`.

### Kotlin

```kotlin
override fun onTouchEvent(event: MotionEvent): Boolean {
    return detector.onTouchEvent(event).let { result ->
        if (!result) {
            if (event.action == MotionEvent.ACTION_UP) {
                stopScrolling()
                true
            } else false
        } else true
    }
}
```

### Java

```java
@Override
public boolean onTouchEvent(MotionEvent event) {
   boolean result = detector.onTouchEvent(event);
   if (!result) {
       if (event.getAction() == MotionEvent.ACTION_UP) {
           stopScrolling();
           result = true;
       }
   }
   return result;
}
```

When you pass `onTouchEvent()` a touch event that it doesn't
recognize as part of a gesture, it returns `false`. You can then run
your own custom gesture-detection code.

## Create physically plausible motion

Gestures are a powerful way to control touchscreen devices, but they can be
counterintuitive and difficult to remember unless they produce physically
plausible results.

For example, suppose you want to implement a horizontal fling gesture that
sets the item drawn in the view spinning around its vertical axis. This gesture
makes sense if the UI responds by moving quickly in the direction of the fling,
then slowing down, as if the user pushes on a flywheel and makes it spin.

The documentation on how to
[animate a scroll
gesture](https://developer.android.com/develop/ui/views/touch-and-input/gestures/scroll) gives a detailed explanation about how to implement your own scoll
behavior. But simulating the feel of a flywheel isn't trivial. A lot of physics
and math is required to make a flywheel model work correctly. Fortunately,
Android provides helper classes to simulate this and other behaviors. The
`https://developer.android.com/reference/android/widget/Scroller`
class is the basis for handling flywheel-style fling gestures.

To start a fling, call
`https://developer.android.com/reference/android/widget/Scroller#fling(int, int, int, int, int, int, int, int)`
with the starting velocity and the minimum and maximum *x* and *y*
values of the fling. For the velocity value, you can use the value computed by
`GestureDetector`.

### Kotlin

```kotlin
fun onFling(e1: MotionEvent, e2: MotionEvent, velocityX: Float, velocityY: Float): Boolean {
    scroller.fling(
            currentX,
            currentY,
            (velocityX / SCALE).toInt(),
            (velocityY / SCALE).toInt(),
            minX,
            minY,
            maxX,
            maxY
    )
    postInvalidate()
    return true
}
```

### Java

```java
@Override
public boolean onFling(MotionEvent e1, MotionEvent e2, float velocityX, float velocityY) {
   scroller.fling(currentX, currentY, velocityX / SCALE, velocityY / SCALE, minX, minY, maxX, maxY);
   postInvalidate();
    return true;
}
```
| **Note:** Although the velocity calculated by `GestureDetector` is physically accurate, many developers feel that using this value makes the fling animation too fast. It's common to divide the *x* and *y* velocity by a factor of four to eight.

The call to `fling()` sets up the physics model for the fling
gesture. Afterward, update the `Scroller` by calling
`https://developer.android.com/reference/android/widget/Scroller#computeScrollOffset()`
at regular intervals. `computeScrollOffset()` updates the
`Scroller` object's internal state by reading the current time and
using the physics model to calculate the *x* and *y* position at that
time. Call
`https://developer.android.com/reference/android/widget/Scroller#getCurrX()`
and
`https://developer.android.com/reference/android/widget/Scroller#getCurrY()`
to retrieve these values.

Most views pass the `Scroller` object's *x* and *y*
positions directly to
`https://developer.android.com/reference/android/view/View#scrollTo(int, int)`.
This example is a little different: it uses the current scroll *x* position
to set the rotational angle of the view.

### Kotlin

```kotlin
scroller.apply {
    if (!isFinished) {
        computeScrollOffset()
        setItemRotation(currX)
    }
}
```

### Java

```java
if (!scroller.isFinished()) {
    scroller.computeScrollOffset();
    setItemRotation(scroller.getCurrX());
}
```

The `Scroller` class computes scroll positions for you, but it
doesn't automatically apply those positions to your view. Apply new coordinates
often enough to make the scrolling animation look smooth. There are two ways to
do this:

- Force a redraw by calling `https://developer.android.com/reference/android/view/View#postInvalidate()` after calling `fling()`. This technique requires that you compute scroll offsets in `https://developer.android.com/reference/android/view/View#onDraw(android.graphics.Canvas)` and call `postInvalidate()` every time the scroll offset changes.
- Set up a `https://developer.android.com/reference/android/animation/ValueAnimator` to animate for the duration of the fling and add a listener to process animation updates by calling `https://developer.android.com/reference/android/animation/ValueAnimator#addUpdateListener(android.animation.ValueAnimator.AnimatorUpdateListener)`. This technique lets you animate properties of a `https://developer.android.com/reference/android/view/View`.

## Make your transitions smooth

Users expect a modern UI to transition smoothly between states: UI elements
fading in and out instead of appearing and disappearing, and motions beginning
and ending smoothly instead of starting and stopping abruptly. The Android
[property animation
framework](https://developer.android.com/guide/topics/graphics/prop-animation) makes smooth transitions easier.

To use the animation system, whenever a property changes what affects your
view's appearance, don't change the property directly. Instead, use
`ValueAnimator` to make the change. In the following example,
modifying the selected child component in the view makes the entire rendered
view rotate so that the selection pointer is centered.
`ValueAnimator` changes the rotation over a period of several hundred
milliseconds, rather than immediately setting the new rotation value.

### Kotlin

```kotlin
autoCenterAnimator = ObjectAnimator.ofInt(this, "Rotation", 0).apply {
    setIntValues(targetAngle)
    duration = AUTOCENTER_ANIM_DURATION
    start()
}
```

### Java

```java
autoCenterAnimator = ObjectAnimator.ofInt(this, "Rotation", 0);
autoCenterAnimator.setIntValues(targetAngle);
autoCenterAnimator.setDuration(AUTOCENTER_ANIM_DURATION);
autoCenterAnimator.start();
```

If the value you want to change is one of the base `View`
properties, doing the animation is even easier, because views have a built-in
`https://developer.android.com/reference/android/view/ViewPropertyAnimator`
that is optimized for simultaneous animation of multiple properties, as in the
following example:

### Kotlin

```kotlin
animate()
    .rotation(targetAngle)
    .duration = ANIM_DURATION
    .start()
```

### Java

```java
animate().rotation(targetAngle).setDuration(ANIM_DURATION).start();
```