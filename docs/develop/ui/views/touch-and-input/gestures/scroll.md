---
title: https://developer.android.com/develop/ui/views/touch-and-input/gestures/scroll
url: https://developer.android.com/develop/ui/views/touch-and-input/gestures/scroll
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn how to use touch and input in Compose. [Scrolling →](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/scroll) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)

<br />

In Android, scrolling is typically achieved by using the
`https://developer.android.com/reference/android/widget/ScrollView`
class. Nest any standard layout that might extend beyond the bounds of its
container in a `ScrollView` to provide a scrollable view managed by
the framework. Implementing a custom scroller is only necessary for special
scenarios. This document describes how to display a scrolling effect in response
to touch gestures using *scrollers*.

Your app can use
scrollers---`https://developer.android.com/reference/android/widget/Scroller`
or
`https://developer.android.com/reference/android/widget/OverScroller`---to
collect the data needed to produce a scrolling animation in response to a touch
event. They are similar, but `OverScroller` also includes methods for
indicating to users when they reach the content edges after a pan or fling
gesture.

- Starting in Android 12 (API level 31), the visual elements stretch and bounce back on a drag event and fling and bounce back on a fling event.
- On Android 11 (API level 30) and earlier, the boundaries display a "glow" effect after a drag or fling gesture to the edge.

The `InteractiveChart` sample in this document uses the
`https://developer.android.com/reference/android/widget/EdgeEffect`
class to display these overscroll effects.

> [!NOTE]
> **Note:** Use `OverScroller` instead of `Scroller`
> for scrolling animations. `OverScroller` provides the best backward
> compatibility with earlier devices.
>
> You generally only need to use scrollers when implementing scrolling
> yourself. `ScrollView` and
> `https://developer.android.com/reference/android/widget/HorizontalScrollView`
> do all of this for you if you nest your layout within them.

You can use a scroller to animate scrolling over time, using
platform-standard scrolling physics such as friction, velocity, and other
qualities. The scroller itself doesn't draw anything. Scrollers track scroll
offsets for you over time, but they don't automatically apply those positions to
your view. You must get and apply new coordinates at a rate that makes the
scrolling animation look smooth.

## Understand scrolling terminology

Scrolling is a word that can mean different things in Android, depending on
the context.

*Scrolling* is the general process of moving the viewport---that is,
the "window" of content you're looking at. When scrolling is in both the
*x*- and *y*-axes, it's called *panning*. The
`InteractiveChart` sample app in this document illustrates two
different types of scrolling, dragging and flinging:

- **Dragging:** this is the type of scrolling that occurs when a user drags their finger across the touchscreen. You can implement dragging by overriding `https://developer.android.com/reference/android/view/GestureDetector.OnGestureListener#onScroll(android.view.MotionEvent, android.view.MotionEvent, float, float)` in `https://developer.android.com/reference/android/view/GestureDetector.OnGestureListener`. For more information about dragging, see [Drag and scale](https://developer.android.com/develop/ui/views/touch-and-input/gestures/scale).
- **Flinging:** this is the type of scrolling that occurs when a user drags and lifts their finger quickly. After the user lifts their finger, you generally want to keep moving the viewport, but decelerate until the viewport stops moving. You can implement flinging by overriding `https://developer.android.com/reference/android/view/GestureDetector.OnGestureListener#onFling(android.view.MotionEvent, android.view.MotionEvent, float, float)` in `GestureDetector.OnGestureListener` and using a scroller object.
- **Panning:** scrolling simultaneously along both the *x*- and *y*-axes is called *panning*.

It's common to use scroller objects in conjunction with a fling gesture, but
you can use them in any context where you want the UI to display scrolling in
response to a touch event. For example, you can override
`https://developer.android.com/reference/android/view/View#onTouchEvent(android.view.MotionEvent)`
to process touch events directly and produce a scrolling effect or a
"snap-to-page" animation in response to those touch events.

## Components that contain built-in scrolling implementations

The following Android components contain built-in support for scrolling and
overscrolling behavior:

- `https://developer.android.com/reference/android/widget/GridView`
- `https://developer.android.com/reference/android/widget/HorizontalScrollView`
- `https://developer.android.com/reference/android/widget/ListView`
- `https://developer.android.com/reference/androidx/core/widget/NestedScrollView`
- `https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView`
- `https://developer.android.com/reference/android/widget/ScrollView`
- `https://developer.android.com/reference/kotlin/androidx/viewpager/widget/ViewPager`
- `https://developer.android.com/reference/androidx/viewpager2/widget/ViewPager2`

If your app needs to support scrolling and overscrolling inside a different
component, complete the following steps:

1. [Create a custom touch-based scrolling
   implementation](https://developer.android.com/develop/ui/views/touch-and-input/gestures/scroll#scroll).
2. To support devices that run Android 12 and later, [implement the stretch overscroll
   effect](https://developer.android.com/develop/ui/views/touch-and-input/gestures/scroll#implement-stretch-overscroll).

## Create a custom touch-based scrolling implementation

This section describes how to create your own scroller if your app uses a
component that doesn't
[contain built-in support](https://developer.android.com/develop/ui/views/touch-and-input/gestures/scroll#components-built-in-support) for
scrolling and overscrolling.

The following snippet comes from the
[`InteractiveChart`
sample](https://android.googlesource.com/platform/frameworks/base/+/8c4a8243c77bcbd434fb30587be2feffd2835728/docs/html/training/gestures/scroll.jd). It uses a
`https://developer.android.com/reference/android/view/GestureDetector`
and overrides the
`https://developer.android.com/reference/android/view/GestureDetector.SimpleOnGestureListener`
method `onFling()`. It uses `OverScroller` to track the
fling gesture. If the user reaches the content edges after they perform the
fling gesture, the container indicates when the user reaches the end of the
content. The indication depends on the version of Android that a device
runs:

- On Android 12 and later, the visual elements stretch and bounce back.
- On Android 11 and earlier, the visual elements display a glow effect.

> [!NOTE]
> **Note:** The `InteractiveChart` sample app displays a chart that you can zoom, pan, or scroll. In the following snippet, `contentRect` represents the rectangle coordinates within the view that the chart is drawn into. At any given time, a subset of the total chart domain and range are drawn into this rectangular area. `currentViewport` represents the portion of the chart that is visible on the screen. Because pixel offsets are generally treated as integers, `contentRect` is of the type `https://developer.android.com/reference/android/graphics/Rect`. Because the graph domain and range are decimal or float values, `currentViewport` is of the type `https://developer.android.com/reference/android/graphics/RectF`.

The first part of the following snippet shows the implementation of
`onFling()`:

### Kotlin

```kotlin
// Viewport extremes. See currentViewport for a discussion of the viewport.
private val AXIS_X_MIN = -1f
private val AXIS_X_MAX = 1f
private val AXIS_Y_MIN = -1f
private val AXIS_Y_MAX = 1f

// The current viewport. This rectangle represents the visible chart
// domain and range. The viewport is the part of the app that the
// user manipulates via touch gestures.
private val currentViewport = RectF(AXIS_X_MIN, AXIS_Y_MIN, AXIS_X_MAX, AXIS_Y_MAX)

// The current destination rectangle---in pixel coordinates---into which
// the chart data must be drawn.
private lateinit var contentRect: Rect

private lateinit var scroller: OverScroller
private lateinit var scrollerStartViewport: RectF
...
private val gestureListener = object : GestureDetector.SimpleOnGestureListener() {

    override fun onDown(e: MotionEvent): Boolean {
        // Initiates the decay phase of any active edge effects.
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.S) {
            releaseEdgeEffects()
        }
        scrollerStartViewport.set(currentViewport)
        // Aborts any active scroll animations and invalidates.
        scroller.forceFinished(true)
        ViewCompat.postInvalidateOnAnimation(this@InteractiveLineGraphView)
        return true
    }
    ...
    override fun onFling(
            e1: MotionEvent,
            e2: MotionEvent,
            velocityX: Float,
            velocityY: Float
    ): Boolean {
        fling((-velocityX).toInt(), (-velocityY).toInt())
        return true
    }
}

private fun fling(velocityX: Int, velocityY: Int) {
    // Initiates the decay phase of any active edge effects.
    // On Android 12 and later, the edge effect (stretch) must
    // continue.
    if (Build.VERSION.SDK_INT < Build.VERSION_CODES.S) {
            releaseEdgeEffects()
    }
    // Flings use math in pixels, as opposed to math based on the viewport.
    val surfaceSize: Point = computeScrollSurfaceSize()
    val (startX: Int, startY: Int) = scrollerStartViewport.run {
        set(currentViewport)
        (surfaceSize.x * (left - AXIS_X_MIN) / (AXIS_X_MAX - AXIS_X_MIN)).toInt() to
                (surfaceSize.y * (AXIS_Y_MAX - bottom) / (AXIS_Y_MAX - AXIS_Y_MIN)).toInt()
    }
    // Before flinging, stops the current animation.
    scroller.forceFinished(true)
    // Begins the animation.
    scroller.fling(
            // Current scroll position.
            startX,
            startY,
            velocityX,
            velocityY,
            /*
             * Minimum and maximum scroll positions. The minimum scroll
             * position is generally 0 and the maximum scroll position
             * is generally the content size less the screen size. So if the
             * content width is 1000 pixels and the screen width is 200
             * pixels, the maximum scroll offset is 800 pixels.
             */
            0, surfaceSize.x - contentRect.width(),
            0, surfaceSize.y - contentRect.height(),
            // The edges of the content. This comes into play when using
            // the EdgeEffect class to draw "glow" overlays.
            contentRect.width() / 2,
            contentRect.height() / 2
    )
    // Invalidates to trigger computeScroll().
    ViewCompat.postInvalidateOnAnimation(this)
}
```

### Java

```java
// Viewport extremes. See currentViewport for a discussion of the viewport.
private static final float AXIS_X_MIN = -1f;
private static final float AXIS_X_MAX = 1f;
private static final float AXIS_Y_MIN = -1f;
private static final float AXIS_Y_MAX = 1f;

// The current viewport. This rectangle represents the visible chart
// domain and range. The viewport is the part of the app that the
// user manipulates via touch gestures.
private RectF currentViewport =
  new RectF(AXIS_X_MIN, AXIS_Y_MIN, AXIS_X_MAX, AXIS_Y_MAX);

// The current destination rectangle---in pixel coordinates---into which
// the chart data must be drawn.
private final Rect contentRect = new Rect();

private final OverScroller scroller;
private final RectF scrollerStartViewport =
  new RectF(); // Used only for zooms and flings.
...
private final GestureDetector.SimpleOnGestureListener gestureListener
        = new GestureDetector.SimpleOnGestureListener() {
    @Override
    public boolean onDown(MotionEvent e) {
         if (Build.VERSION.SDK_INT < Build.VERSION_CODES.S) {
            releaseEdgeEffects();
        }
        scrollerStartViewport.set(currentViewport);
        scroller.forceFinished(true);
        ViewCompat.postInvalidateOnAnimation(InteractiveLineGraphView.this);
        return true;
    }
...
    @Override
    public boolean onFling(MotionEvent e1, MotionEvent e2, float velocityX, float velocityY) {
        fling((int) -velocityX, (int) -velocityY);
        return true;
    }
};

private void fling(int velocityX, int velocityY) {
    // Initiates the decay phase of any active edge effects.
    // On Android 12 and later, the edge effect (stretch) must
    // continue.
    if (Build.VERSION.SDK_INT < Build.VERSION_CODES.S) {
            releaseEdgeEffects();
    }
    // Flings use math in pixels, as opposed to math based on the viewport.
    Point surfaceSize = computeScrollSurfaceSize();
    scrollerStartViewport.set(currentViewport);
    int startX = (int) (surfaceSize.x * (scrollerStartViewport.left -
            AXIS_X_MIN) / (
            AXIS_X_MAX - AXIS_X_MIN));
    int startY = (int) (surfaceSize.y * (AXIS_Y_MAX -
            scrollerStartViewport.bottom) / (
            AXIS_Y_MAX - AXIS_Y_MIN));
    // Before flinging, stops the current animation.
    scroller.forceFinished(true);
    // Begins the animation.
    scroller.fling(
            // Current scroll position.
            startX,
            startY,
            velocityX,
            velocityY,
            /*
             * Minimum and maximum scroll positions. The minimum scroll
             * position is generally 0 and the maximum scroll position
             * is generally the content size less the screen size. So if the
             * content width is 1000 pixels and the screen width is 200
             * pixels, the maximum scroll offset is 800 pixels.
             */
            0, surfaceSize.x - contentRect.width(),
            0, surfaceSize.y - contentRect.height(),
            // The edges of the content. This comes into play when using
            // the EdgeEffect class to draw "glow" overlays.
            contentRect.width() / 2,
            contentRect.height() / 2);
    // Invalidates to trigger computeScroll().
    ViewCompat.postInvalidateOnAnimation(this);
}
```

When `onFling()` calls
`https://developer.android.com/reference/androidx/core/view/ViewCompat#postInvalidateOnAnimation(android.view.View)`,
it triggers
`https://developer.android.com/reference/android/view/View#computeScroll()`
to update the values for *x* and *y*. This is typically done when a
view child is animating a scroll using a scroller object, as shown the preceding
example.

Most views pass the scroller object's *x* and *y* position directly
to
`https://developer.android.com/reference/android/view/View#scrollTo(int, int)`.
The following implementation of `computeScroll()` takes a different
approach: it calls
`https://developer.android.com/reference/android/widget/OverScroller#computeScrollOffset()`
to get the current location of *x* and *y*. When the criteria for
displaying an overscroll "glow" edge effect are met--- that is, the display
is zoomed in, *x* or *y* is out of bounds, and the app isn't already
showing an overscroll---the code sets up the overscroll glow effect and
calls `postInvalidateOnAnimation()` to trigger an invalidate on the
view.

### Kotlin

```kotlin
// Edge effect/overscroll tracking objects.
private lateinit var edgeEffectTop: EdgeEffect
private lateinit var edgeEffectBottom: EdgeEffect
private lateinit var edgeEffectLeft: EdgeEffect
private lateinit var edgeEffectRight: EdgeEffect

private var edgeEffectTopActive: Boolean = false
private var edgeEffectBottomActive: Boolean = false
private var edgeEffectLeftActive: Boolean = false
private var edgeEffectRightActive: Boolean = false

override fun computeScroll() {
    super.computeScroll()

    var needsInvalidate = false

    // The scroller isn't finished, meaning a fling or
    // programmatic pan operation is active.
    if (scroller.computeScrollOffset()) {
        val surfaceSize: Point = computeScrollSurfaceSize()
        val currX: Int = scroller.currX
        val currY: Int = scroller.currY

        val (canScrollX: Boolean, canScrollY: Boolean) = currentViewport.run {
            (left > AXIS_X_MIN || right < AXIS_X_MAX) to (top > AXIS_Y_MIN || bottom < AXIS_Y_MAX)
        }

        /*
         * If you are zoomed in, currX or currY is
         * outside of bounds, and you aren't already
         * showing overscroll, then render the overscroll
         * glow edge effect.
         */
        if (canScrollX
                && currX < 0
                && edgeEffectLeft.isFinished
                && !edgeEffectLeftActive) {
            edgeEffectLeft.onAbsorb(scroller.currVelocity.toInt())
            edgeEffectLeftActive = true
            needsInvalidate = true
        } else if (canScrollX
                && currX > surfaceSize.x - contentRect.width()
                && edgeEffectRight.isFinished
                && !edgeEffectRightActive) {
            edgeEffectRight.onAbsorb(scroller.currVelocity.toInt())
            edgeEffectRightActive = true
            needsInvalidate = true
        }

        if (canScrollY
                && currY < 0
                && edgeEffectTop.isFinished
                && !edgeEffectTopActive) {
            edgeEffectTop.onAbsorb(scroller.currVelocity.toInt())
            edgeEffectTopActive = true
            needsInvalidate = true
        } else if (canScrollY
                && currY > surfaceSize.y - contentRect.height()
                && edgeEffectBottom.isFinished
                && !edgeEffectBottomActive) {
            edgeEffectBottom.onAbsorb(scroller.currVelocity.toInt())
            edgeEffectBottomActive = true
            needsInvalidate = true
        }
        ...
    }
}
```

### Java

```java
// Edge effect/overscroll tracking objects.
private EdgeEffectCompat edgeEffectTop;
private EdgeEffectCompat edgeEffectBottom;
private EdgeEffectCompat edgeEffectLeft;
private EdgeEffectCompat edgeEffectRight;

private boolean edgeEffectTopActive;
private boolean edgeEffectBottomActive;
private boolean edgeEffectLeftActive;
private boolean edgeEffectRightActive;

@Override
public void computeScroll() {
    super.computeScroll();

    boolean needsInvalidate = false;

    // The scroller isn't finished, meaning a fling or
    // programmatic pan operation is active.
    if (scroller.computeScrollOffset()) {
        Point surfaceSize = computeScrollSurfaceSize();
        int currX = scroller.getCurrX();
        int currY = scroller.getCurrY();

        boolean canScrollX = (currentViewport.left > AXIS_X_MIN
                || currentViewport.right < AXIS_X_MAX);
        boolean canScrollY = (currentViewport.top > AXIS_Y_MIN
                || currentViewport.bottom < AXIS_Y_MAX);

        /*
         * If you are zoomed in, currX or currY is
         * outside of bounds, and you aren't already
         * showing overscroll, then render the overscroll
         * glow edge effect.
         */
        if (canScrollX
                && currX < 0
                && edgeEffectLeft.isFinished()
                && !edgeEffectLeftActive) {
            edgeEffectLeft.onAbsorb((int)mScroller.getCurrVelocity());
            edgeEffectLeftActive = true;
            needsInvalidate = true;
        } else if (canScrollX
                && currX > (surfaceSize.x - contentRect.width())
                && edgeEffectRight.isFinished()
                && !edgeEffectRightActive) {
            edgeEffectRight.onAbsorb((int)mScroller.getCurrVelocity());
            edgeEffectRightActive = true;
            needsInvalidate = true;
        }

        if (canScrollY
                && currY < 0
                && edgeEffectTop.isFinished()
                && !edgeEffectTopActive) {
            edgeEffectRight.onAbsorb((int)mScroller.getCurrVelocity());
            edgeEffectTopActive = true;
            needsInvalidate = true;
        } else if (canScrollY
                && currY > (surfaceSize.y - contentRect.height())
                && edgeEffectBottom.isFinished()
                && !edgeEffectBottomActive) {
            edgeEffectRight.onAbsorb((int)mScroller.getCurrVelocity());
            edgeEffectBottomActive = true;
            needsInvalidate = true;
        }
        ...
    }
```

Here is the section of the code that performs the actual zoom:

### Kotlin

```kotlin
lateinit var zoomer: Zoomer
val zoomFocalPoint = PointF()
...
// If a zoom is in progress---either programmatically
// or through double touch---this performs the zoom.
if (zoomer.computeZoom()) {
    val newWidth: Float = (1f - zoomer.currZoom) * scrollerStartViewport.width()
    val newHeight: Float = (1f - zoomer.currZoom) * scrollerStartViewport.height()
    val pointWithinViewportX: Float =
            (zoomFocalPoint.x - scrollerStartViewport.left) / scrollerStartViewport.width()
    val pointWithinViewportY: Float =
            (zoomFocalPoint.y - scrollerStartViewport.top) / scrollerStartViewport.height()
    currentViewport.set(
            zoomFocalPoint.x - newWidth * pointWithinViewportX,
            zoomFocalPoint.y - newHeight * pointWithinViewportY,
            zoomFocalPoint.x + newWidth * (1 - pointWithinViewportX),
            zoomFocalPoint.y + newHeight * (1 - pointWithinViewportY)
    )
    constrainViewport()
    needsInvalidate = true
}
if (needsInvalidate) {
    ViewCompat.postInvalidateOnAnimation(this)
}
```

### Java

```java
// Custom object that is functionally similar to Scroller.
Zoomer zoomer;
private PointF zoomFocalPoint = new PointF();
...
// If a zoom is in progress---either programmatically
// or through double touch---this performs the zoom.
if (zoomer.computeZoom()) {
    float newWidth = (1f - zoomer.getCurrZoom()) *
            scrollerStartViewport.width();
    float newHeight = (1f - zoomer.getCurrZoom()) *
            scrollerStartViewport.height();
    float pointWithinViewportX = (zoomFocalPoint.x -
            scrollerStartViewport.left)
            / scrollerStartViewport.width();
    float pointWithinViewportY = (zoomFocalPoint.y -
            scrollerStartViewport.top)
            / scrollerStartViewport.height();
    currentViewport.set(
            zoomFocalPoint.x - newWidth * pointWithinViewportX,
            zoomFocalPoint.y - newHeight * pointWithinViewportY,
            zoomFocalPoint.x + newWidth * (1 - pointWithinViewportX),
            zoomFocalPoint.y + newHeight * (1 - pointWithinViewportY));
    constrainViewport();
    needsInvalidate = true;
}
if (needsInvalidate) {
    ViewCompat.postInvalidateOnAnimation(this);
}
```

This is the `computeScrollSurfaceSize()` method that's called in
the preceding snippet. It computes the current scrollable surface size in
pixels. For example, if the entire chart area is visible, this is the current
size of `mContentRect`. If the chart is zoomed in 200% in both
directions, the returned size is twice as large horizontally and vertically.

### Kotlin

```kotlin
private fun computeScrollSurfaceSize(): Point {
    return Point(
            (contentRect.width() * (AXIS_X_MAX - AXIS_X_MIN) / currentViewport.width()).toInt(),
            (contentRect.height() * (AXIS_Y_MAX - AXIS_Y_MIN) / currentViewport.height()).toInt()
    )
}
```

### Java

```java
private Point computeScrollSurfaceSize() {
    return new Point(
            (int) (contentRect.width() * (AXIS_X_MAX - AXIS_X_MIN)
                    / currentViewport.width()),
            (int) (contentRect.height() * (AXIS_Y_MAX - AXIS_Y_MIN)
                    / currentViewport.height()));
}
```

For another example of scroller usage, see the
[source code](https://android.googlesource.com/platform/frameworks/support/+/5b614a46f6ffb3e9ca5ab6321c12412550a4e13a/viewpager/src/main/java/androidx/viewpager/widget/ViewPager.java)
for the `ViewPager` class. It scrolls in response to flings and uses
scrolling to implement the "snap-to-page" animation.

## Implement the stretch overscroll effect

Starting in Android 12, `EdgeEffect` adds the
following APIs for implementing the stretch overscroll effect:

- `getDistance()`
- `onPullDistance()`

To provide the best user experience with stretch overscroll, do the
following:

1. When the stretch animation is in effect when the user touches the contents, register the touch as a "catch." The user stops the animation and begins manipulating the stretch again.
2. When the user moves their finger in the opposite direction of the stretch, release the stretch until it's fully gone, and then begin scrolling.
3. When the user flings during a stretch, fling the `EdgeEffect` to enhance the stretch effect.

### Catch the animation

When a user catches an active stretch animation,
`EdgeEffect.getDistance()` returns `0`. This condition
indicates that the stretch must be manipulated by the touch motion. In most
containers, the catch is detected in `onInterceptTouchEvent()`, as
shown in the following code snippet:

### Kotlin

```kotlin
override fun onInterceptTouchEvent(ev: MotionEvent): Boolean {
  ...
  when (action and MotionEvent.ACTION_MASK) {
    MotionEvent.ACTION_DOWN ->
      ...
      isBeingDragged = EdgeEffectCompat.getDistance(edgeEffectBottom) > 0f ||
          EdgeEffectCompat.getDistance(edgeEffectTop) > 0f
      ...
  }
  return isBeingDragged
}
```

### Java

```java
@Override
public boolean onInterceptTouchEvent(MotionEvent ev) {
  ...
  switch (action & MotionEvent.ACTION_MASK) {
    case MotionEvent.ACTION_DOWN:
      ...
      isBeingDragged = EdgeEffectCompat.getDistance(edgeEffectBottom) > 0
          || EdgeEffectCompat.getDistance(edgeEffectTop) > 0;
      ...
  }
}
```

In the preceding example, `onInterceptTouchEvent()` returns
`true` when `mIsBeingDragged` is `true`, so
it's sufficient to consume the event before the child has an opportunity to
consume it.

### Release the overscroll effect

It's important to release the stretch effect prior to scrolling to prevent
the stretch from being applied to the scrolling content. The following code
sample applies this best practice:

### Kotlin

```kotlin
override fun onTouchEvent(ev: MotionEvent): Boolean {
  val activePointerIndex = ev.actionIndex

  when (ev.getActionMasked()) {
    MotionEvent.ACTION_MOVE ->
      val x = ev.getX(activePointerIndex)
      val y = ev.getY(activePointerIndex)
      var deltaY = y - lastMotionY
      val pullDistance = deltaY / height
      val displacement = x / width

      if (deltaY < 0f && EdgeEffectCompat.getDistance(edgeEffectTop) > 0f) {
        deltaY -= height * EdgeEffectCompat.onPullDistance(edgeEffectTop,
            pullDistance, displacement);
      }
      if (deltaY > 0f && EdgeEffectCompat.getDistance(edgeEffectBottom) > 0f) {
        deltaY += height * EdgeEffectCompat.onPullDistance(edgeEffectBottom,
            -pullDistance, 1 - displacement);
      }
      ...
  }
```

### Java

```java
@Override
public boolean onTouchEvent(MotionEvent ev) {

  final int actionMasked = ev.getActionMasked();

  switch (actionMasked) {
    case MotionEvent.ACTION_MOVE:
      final float x = ev.getX(activePointerIndex);
      final float y = ev.getY(activePointerIndex);
      float deltaY = y - lastMotionY;
      float pullDistance = deltaY / getHeight();
      float displacement = x / getWidth();

      if (deltaY < 0 && EdgeEffectCompat.getDistance(edgeEffectTop) > 0) {
        deltaY -= getHeight() * EdgeEffectCompat.onPullDistance(edgeEffectTop,
            pullDistance, displacement);
      }
      if (deltaY > 0 && EdgeEffectCompat.getDistance(edgeEffectBottom) > 0) {
        deltaY += getHeight() * EdgeEffectCompat.onPullDistance(edgeEffectBottom,
            -pullDistance, 1 - displacement);
      }
            ...
```

When the user is dragging, consume the `EdgeEffect` pull distance
before you pass the touch event to a nested scrolling container or drag the
scroll. In the preceding code sample, `getDistance()` returns a
positive value when an edge effect is being displayed and can be released with
motion. When the touch event releases the stretch, it is first consumed by the
`EdgeEffect` so that it is completely released before other effects,
such as nested scrolling, are displayed. You can use `getDistance()`
to learn how much pull distance is required to release the current effect.

Unlike `onPull()`, `onPullDistance()` returns the
consumed amount of the passed delta. Starting in Android 12, if
`onPull()` or `onPullDistance()` are passed negative
`deltaDistance` values when `getDistance()` is
`0`, the stretch effect doesn't change. On Android 11
and earlier, `onPull()` lets negative values for the total distance
show glow effects.

### Opt out of overscroll

You can opt out of overscroll in your layout file or programmatically.

To opt out in your layout file, set `android:overScrollMode` as
shown in the following example:

```xml
<MyCustomView android:overScrollMode="never">
    ...
</MyCustomView>
```

To opt out programmatically, use code like the following:

### Kotlin

```kotlin
customView.overScrollMode = View.OVER_SCROLL_NEVER
```

### Java

```java
customView.setOverScrollMode(View.OVER_SCROLL_NEVER);
```

## Additional resources

Refer to the following related resources:

- [Input events overview](https://developer.android.com/guide/topics/ui/ui-events)
- [Sensors overview](https://developer.android.com/guide/topics/sensors/sensors_overview)
- [Make a custom view interactive](https://developer.android.com/training/custom-views/making-interactive)