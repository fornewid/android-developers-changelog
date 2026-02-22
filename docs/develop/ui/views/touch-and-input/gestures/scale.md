---
title: https://developer.android.com/develop/ui/views/touch-and-input/gestures/scale
url: https://developer.android.com/develop/ui/views/touch-and-input/gestures/scale
source: md.txt
---

# Drag and scale

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to use touch and input in Compose.  
[Drag, swipe, and fling →](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/drag-swipe-fling)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)  

This document describes how to use touch gestures to drag and scale on-screen objects, using[onTouchEvent()](https://developer.android.com/reference/android/view/View#onTouchEvent(android.view.MotionEvent))to intercept touch events.

## Drag an object

| **Important:** We recomment using[Receive rich content](https://developer.android.com/develop/ui/views/receive-rich-content)to implement drag and drop.

A common operation for a touch gesture is to use it to drag an object across the screen.

In a drag or scroll operation, the app has to keep track of the original pointer, even if additional fingers touch the screen. For example, imagine that while dragging the image, the user places a second finger on the touch screen and lifts the first finger. If your app is only tracking individual pointers, it regards the second pointer as the default and moves the image to that location.

To prevent this from happening, your app needs to distinguish between the original pointer and any subsequent pointers. To do this, it tracks the[ACTION_POINTER_DOWN](https://developer.android.com/reference/android/view/MotionEvent#ACTION_POINTER_DOWN)and[ACTION_POINTER_UP](https://developer.android.com/reference/android/view/MotionEvent#ACTION_POINTER_UP)events as described in[Handle multi-touch gestures](https://developer.android.com/develop/ui/views/touch-and-input/gestures/multi).`ACTION_POINTER_DOWN`and`ACTION_POINTER_UP`are passed to the`onTouchEvent()`callback whenever a secondary pointer goes down or up.

In the`ACTION_POINTER_UP`case, you can extract this index and ensure that the active pointer ID isn't referring to a pointer that is no longer touching the screen. If it is, you can select a different pointer to be active and save its current X and Y position. Use this saved position in the[ACTION_MOVE](https://developer.android.com/reference/android/view/MotionEvent#ACTION_MOVE)case to calculate the distance to move the on-screen object. This way, the app always calculates the distance to move using data from the correct pointer.

The following code snippet lets a user drag an object on the screen. It records the initial position of the active pointer, calculates the distance the pointer travels, and moves the object to the new position. It also correctly manages the possibility of additional pointers.

The snippet uses the[getActionMasked()](https://developer.android.com/reference/android/view/MotionEvent#getActionMasked())method. Always use this method to retrieve the action of a[MotionEvent](https://developer.android.com/reference/android/view/MotionEvent).  

### Kotlin

```kotlin
// The "active pointer" is the one moving the object.
private var mActivePointerId = INVALID_POINTER_ID

override fun onTouchEvent(ev: MotionEvent): Boolean {
    // Let the ScaleGestureDetector inspect all events.
    mScaleDetector.onTouchEvent(ev)

    val action = MotionEventCompat.getActionMasked(ev)

    when (action) {
        MotionEvent.ACTION_DOWN -> {
            MotionEventCompat.getActionIndex(ev).also { pointerIndex ->
                // Remember where you start for dragging.
                mLastTouchX = MotionEventCompat.getX(ev, pointerIndex)
                mLastTouchY = MotionEventCompat.getY(ev, pointerIndex)
            }

            // Save the ID of this pointer for dragging.
            mActivePointerId = MotionEventCompat.getPointerId(ev, 0)
        }

        MotionEvent.ACTION_MOVE -> {
            // Find the index of the active pointer and fetch its position.
            val (x: Float, y: Float) =
                    MotionEventCompat.findPointerIndex(ev, mActivePointerId).let { pointerIndex ->
                        // Calculate the distance moved.
                        MotionEventCompat.getX(ev, pointerIndex) to
                                MotionEventCompat.getY(ev, pointerIndex)
                    }

            mPosX += x - mLastTouchX
            mPosY += y - mLastTouchY

            invalidate()

            // Remember this touch position for the next move event.
            mLastTouchX = x
            mLastTouchY = y
        }
        MotionEvent.ACTION_UP, MotionEvent.ACTION_CANCEL -> {
            mActivePointerId = INVALID_POINTER_ID
        }
        MotionEvent.ACTION_POINTER_UP -> {

            MotionEventCompat.getActionIndex(ev).also { pointerIndex ->
                MotionEventCompat.getPointerId(ev, pointerIndex)
                        .takeIf { it == mActivePointerId }
                        ?.run {
                            // This is the active pointer going up. Choose a new
                            // active pointer and adjust it accordingly.
                            val newPointerIndex = if (pointerIndex == 0) 1 else 0
                            mLastTouchX = MotionEventCompat.getX(ev, newPointerIndex)
                            mLastTouchY = MotionEventCompat.getY(ev, newPointerIndex)
                            mActivePointerId = MotionEventCompat.getPointerId(ev, newPointerIndex)
                        }
            }
        }
    }
    return true
}
```

### Java

```java
// The "active pointer" is the one moving the object.
private int mActivePointerId = INVALID_POINTER_ID;

@Override
public boolean onTouchEvent(MotionEvent ev) {
    // Let the ScaleGestureDetector inspect all events.
    mScaleDetector.onTouchEvent(ev);

    final int action = MotionEventCompat.getActionMasked(ev);

    switch (action) {
    case MotionEvent.ACTION_DOWN: {
        final int pointerIndex = MotionEventCompat.getActionIndex(ev);
        final float x = MotionEventCompat.getX(ev, pointerIndex);
        final float y = MotionEventCompat.getY(ev, pointerIndex);

        // Remember the starting position of the pointer.
        mLastTouchX = x;
        mLastTouchY = y;
        // Save the ID of this pointer for dragging.
        mActivePointerId = MotionEventCompat.getPointerId(ev, 0);
        break;
    }

    case MotionEvent.ACTION_MOVE: {
        // Find the index of the active pointer and fetch its position.
        final int pointerIndex =
                MotionEventCompat.findPointerIndex(ev, mActivePointerId);

        final float x = MotionEventCompat.getX(ev, pointerIndex);
        final float y = MotionEventCompat.getY(ev, pointerIndex);

        // Calculate the distance moved.
        final float dx = x - mLastTouchX;
        final float dy = y - mLastTouchY;

        mPosX += dx;
        mPosY += dy;

        invalidate();

        // Remember this touch position for the next move event.
        mLastTouchX = x;
        mLastTouchY = y;

        break;
    }

    case MotionEvent.ACTION_UP: {
        mActivePointerId = INVALID_POINTER_ID;
        break;
    }

    case MotionEvent.ACTION_CANCEL: {
        mActivePointerId = INVALID_POINTER_ID;
        break;
    }

    case MotionEvent.ACTION_POINTER_UP: {

        final int pointerIndex = MotionEventCompat.getActionIndex(ev);
        final int pointerId = MotionEventCompat.getPointerId(ev, pointerIndex);

        if (pointerId == mActivePointerId) {
            // This is the active pointer going up. Choose a new
            // active pointer and adjust it accordingly.
            final int newPointerIndex = pointerIndex == 0 ? 1 : 0;
            mLastTouchX = MotionEventCompat.getX(ev, newPointerIndex);
            mLastTouchY = MotionEventCompat.getY(ev, newPointerIndex);
            mActivePointerId = MotionEventCompat.getPointerId(ev, newPointerIndex);
        }
        break;
    }
    }
    return true;
}
```

## Drag to pan

The previous section shows an example of dragging an object on the screen. Another common scenario is panning, which is when a user's dragging motion causes scrolling in both the X- and Y-axes. The preceding snippet directly intercepts the`MotionEvent`actions to implement dragging. The snippet in this section takes advantage of the platform's built-in support for common gestures by overriding[onScroll()](https://developer.android.com/reference/android/view/GestureDetector.OnGestureListener#onScroll(android.view.MotionEvent, android.view.MotionEvent, float, float))in[GestureDetector.SimpleOnGestureListener](https://developer.android.com/reference/android/view/GestureDetector.SimpleOnGestureListener).

To provide more context,`onScroll()`is called when a user drags a finger to pan the content.`onScroll()`is only called when a finger is down. As soon as the finger is lifted from the screen, either the gesture either ends or a fling gesture starts, if the finger is moving with some speed just before it is lifted. For more information about scrolling versus flinging, see[Animate a scroll gesture](https://developer.android.com/develop/ui/views/touch-and-input/gestures/scroll).

The following is the code snippet for`onScroll()`:  

### Kotlin

```kotlin
// The current viewport. This rectangle represents the visible
// chart domain and range.
private val mCurrentViewport = RectF(AXIS_X_MIN, AXIS_Y_MIN, AXIS_X_MAX, AXIS_Y_MAX)

// The current destination rectangle, in pixel coordinates, into which the
// chart data must be drawn.
private val mContentRect: Rect? = null

private val mGestureListener = object : GestureDetector.SimpleOnGestureListener() {
    ...
    override fun onScroll(
            e1: MotionEvent,
            e2: MotionEvent,
            distanceX: Float,
            distanceY: Float
    ): Boolean {
        // Scrolling uses math based on the viewport, as opposed to math using
        // pixels.

        mContentRect?.apply {
            // Pixel offset is the offset in screen pixels, while viewport offset is the
            // offset within the current viewport.
            val viewportOffsetX = distanceX * mCurrentViewport.width() / width()
            val viewportOffsetY = -distanceY * mCurrentViewport.height() / height()


            // Updates the viewport and refreshes the display.
            setViewportBottomLeft(
                    mCurrentViewport.left + viewportOffsetX,
                    mCurrentViewport.bottom + viewportOffsetY
            )
        }

        return true
    }
}
```

### Java

```java
// The current viewport. This rectangle represents the visible
// chart domain and range.
private RectF mCurrentViewport =
        new RectF(AXIS_X_MIN, AXIS_Y_MIN, AXIS_X_MAX, AXIS_Y_MAX);

// The current destination rectangle, in pixel coordinates, into which the
// chart data must be drawn.
private Rect mContentRect;

private final GestureDetector.SimpleOnGestureListener mGestureListener
            = new GestureDetector.SimpleOnGestureListener() {
...

@Override
public boolean onScroll(MotionEvent e1, MotionEvent e2,
            float distanceX, float distanceY) {
    // Scrolling uses math based on the viewport, as opposed to math using
    // pixels.

    // Pixel offset is the offset in screen pixels, while viewport offset is the
    // offset within the current viewport.
    float viewportOffsetX = distanceX * mCurrentViewport.width()
            / mContentRect.width();
    float viewportOffsetY = -distanceY * mCurrentViewport.height()
            / mContentRect.height();
    ...
    // Updates the viewport, refreshes the display.
    setViewportBottomLeft(
            mCurrentViewport.left + viewportOffsetX,
            mCurrentViewport.bottom + viewportOffsetY);
    ...
    return true;
}
```

The implementation of`onScroll()`scrolls the viewport in response to the touch gesture:  

### Kotlin

```kotlin
/**
 * Sets the current viewport, defined by mCurrentViewport, to the given
 * X and Y positions. The Y value represents the topmost pixel position,
 * and thus the bottom of the mCurrentViewport rectangle.
 */
private fun setViewportBottomLeft(x: Float, y: Float) {
    /*
     * Constrains within the scroll range. The scroll range is the viewport
     * extremes, such as AXIS_X_MAX, minus the viewport size. For example, if
     * the extremes are 0 and 10 and the viewport size is 2, the scroll range
     * is 0 to 8.
     */

    val curWidth: Float = mCurrentViewport.width()
    val curHeight: Float = mCurrentViewport.height()
    val newX: Float = Math.max(AXIS_X_MIN, Math.min(x, AXIS_X_MAX - curWidth))
    val newY: Float = Math.max(AXIS_Y_MIN + curHeight, Math.min(y, AXIS_Y_MAX))

    mCurrentViewport.set(newX, newY - curHeight, newX + curWidth, newY)

    // Invalidates the View to update the display.
    ViewCompat.postInvalidateOnAnimation(this)
}
```

### Java

```java
/**
 * Sets the current viewport (defined by mCurrentViewport) to the given
 * X and Y positions. Note that the Y value represents the topmost pixel
 * position, and thus the bottom of the mCurrentViewport rectangle.
 */
private void setViewportBottomLeft(float x, float y) {
    /*
     * Constrains within the scroll range. The scroll range is the viewport
     * extremes, such as AXIS_X_MAX, minus the viewport size. For example, if
     * the extremes are 0 and 10 and the viewport size is 2, the scroll range
     * is 0 to 8.
     */

    float curWidth = mCurrentViewport.width();
    float curHeight = mCurrentViewport.height();
    x = Math.max(AXIS_X_MIN, Math.min(x, AXIS_X_MAX - curWidth));
    y = Math.max(AXIS_Y_MIN + curHeight, Math.min(y, AXIS_Y_MAX));

    mCurrentViewport.set(x, y - curHeight, x + curWidth, y);

    // Invalidates the View to update the display.
    ViewCompat.postInvalidateOnAnimation(this);
}
```

## Use touch to perform scaling

As discussed in[Detect common gestures](https://developer.android.com/develop/ui/views/touch-and-input/gestures/detector), use[GestureDetector](https://developer.android.com/reference/android/view/GestureDetector)to detect common gestures used by Android, such as scrolling, flinging, and touch and hold. For scaling, Android provides[ScaleGestureDetector](https://developer.android.com/reference/android/view/ScaleGestureDetector). You can use`GestureDetector`and`ScaleGestureDetector`together when you want a view to recognize additional gestures.

To report detected gesture events, gesture detectors use listener objects passed to their constructors.`ScaleGestureDetector`uses[ScaleGestureDetector.OnScaleGestureListener](https://developer.android.com/reference/android/view/ScaleGestureDetector.OnScaleGestureListener). Android provides[ScaleGestureDetector.SimpleOnScaleGestureListener](https://developer.android.com/reference/android/view/ScaleGestureDetector.SimpleOnScaleGestureListener)as a helper class that you can extend if you don't need all of the reported events.

### Basic scaling example

The following snippet illustrates the basic elements involved in scaling.  

### Kotlin

```kotlin
private var mScaleFactor = 1f

private val scaleListener = object : ScaleGestureDetector.SimpleOnScaleGestureListener() {

    override fun onScale(detector: ScaleGestureDetector): Boolean {
        mScaleFactor *= detector.scaleFactor

        // Don't let the object get too small or too large.
        mScaleFactor = Math.max(0.1f, Math.min(mScaleFactor, 5.0f))

        invalidate()
        return true
    }
}

private val mScaleDetector = ScaleGestureDetector(context, scaleListener)

override fun onTouchEvent(ev: MotionEvent): Boolean {
    // Let the ScaleGestureDetector inspect all events.
    mScaleDetector.onTouchEvent(ev)
    return true
}

override fun onDraw(canvas: Canvas?) {
    super.onDraw(canvas)

    canvas?.apply {
        save()
        scale(mScaleFactor, mScaleFactor)
        // onDraw() code goes here.
        restore()
    }
}
```

### Java

```java
private ScaleGestureDetector mScaleDetector;
private float mScaleFactor = 1.f;

public MyCustomView(Context mContext){
    ...
    // View code goes here.
    ...
    mScaleDetector = new ScaleGestureDetector(context, new ScaleListener());
}

@Override
public boolean onTouchEvent(MotionEvent ev) {
    // Let the ScaleGestureDetector inspect all events.
    mScaleDetector.onTouchEvent(ev);
    return true;
}

@Override
public void onDraw(Canvas canvas) {
    super.onDraw(canvas);

    canvas.save();
    canvas.scale(mScaleFactor, mScaleFactor);
    ...
    // onDraw() code goes here.
    ...
    canvas.restore();
}

private class ScaleListener
        extends ScaleGestureDetector.SimpleOnScaleGestureListener {
    @Override
    public boolean onScale(ScaleGestureDetector detector) {
        mScaleFactor *= detector.getScaleFactor();

        // Don't let the object get too small or too large.
        mScaleFactor = Math.max(0.1f, Math.min(mScaleFactor, 5.0f));

        invalidate();
        return true;
    }
}
```

### More complex scaling example

The following is a more complex example from the`InteractiveChart`sample shown in[Animate a scroll gesture](https://developer.android.com/develop/ui/views/touch-and-input/gestures/scroll). The`InteractiveChart`sample supports scrolling, panning, and scaling with multiple fingers, using the`ScaleGestureDetector`span ([getCurrentSpanX](https://developer.android.com/reference/android/view/ScaleGestureDetector#getCurrentSpanX())and[getCurrentSpanY](https://developer.android.com/reference/android/view/ScaleGestureDetector#getCurrentSpanY())) and "focus" ([getFocusX](https://developer.android.com/reference/android/view/ScaleGestureDetector#getFocusX())and[getFocusY](https://developer.android.com/reference/android/view/ScaleGestureDetector#getFocusY())) features.  

### Kotlin

```kotlin
private val mCurrentViewport = RectF(AXIS_X_MIN, AXIS_Y_MIN, AXIS_X_MAX, AXIS_Y_MAX)
private val mContentRect: Rect? = null
...
override fun onTouchEvent(event: MotionEvent): Boolean {
    return mScaleGestureDetector.onTouchEvent(event)
            || mGestureDetector.onTouchEvent(event)
            || super.onTouchEvent(event)
}

/**
 * The scale listener, used for handling multi-finger scale gestures.
 */
private val mScaleGestureListener = object : ScaleGestureDetector.SimpleOnScaleGestureListener() {

    /**
     * This is the active focal point in terms of the viewport. It can be a
     * local variable, but keep it here to minimize per-frame allocations.
     */
    private val viewportFocus = PointF()
    private var lastSpanX: Float = 0f
    private var lastSpanY: Float = 0f

    // Detects new pointers are going down.
    override fun onScaleBegin(scaleGestureDetector: ScaleGestureDetector): Boolean {
        lastSpanX = scaleGestureDetector.currentSpanX
        lastSpanY = scaleGestureDetector.currentSpanY
        return true
    }

    override fun onScale(scaleGestureDetector: ScaleGestureDetector): Boolean {
        val spanX: Float = scaleGestureDetector.currentSpanX
        val spanY: Float = scaleGestureDetector.currentSpanY

        val newWidth: Float = lastSpanX / spanX * mCurrentViewport.width()
        val newHeight: Float = lastSpanY / spanY * mCurrentViewport.height()

        val focusX: Float = scaleGestureDetector.focusX
        val focusY: Float = scaleGestureDetector.focusY
        // Ensures the chart point is within the chart region.
        // See the sample for the implementation of hitTest().
        hitTest(focusX, focusY, viewportFocus)

        mContentRect?.apply {
            mCurrentViewport.set(
                    viewportFocus.x - newWidth * (focusX - left) / width(),
                    viewportFocus.y - newHeight * (bottom - focusY) / height(),
                    0f,
                    0f
            )
        }
        mCurrentViewport.right = mCurrentViewport.left + newWidth
        mCurrentViewport.bottom = mCurrentViewport.top + newHeight
        // Invalidates the View to update the display.
        ViewCompat.postInvalidateOnAnimation(this@InteractiveLineGraphView)

        lastSpanX = spanX
        lastSpanY = spanY
        return true
    }
}
```

### Java

```java
private RectF mCurrentViewport =
        new RectF(AXIS_X_MIN, AXIS_Y_MIN, AXIS_X_MAX, AXIS_Y_MAX);
private Rect mContentRect;
private ScaleGestureDetector mScaleGestureDetector;
...
@Override
public boolean onTouchEvent(MotionEvent event) {
    boolean retVal = mScaleGestureDetector.onTouchEvent(event);
    retVal = mGestureDetector.onTouchEvent(event) || retVal;
    return retVal || super.onTouchEvent(event);
}

/**
 * The scale listener, used for handling multi-finger scale gestures.
 */
private final ScaleGestureDetector.OnScaleGestureListener mScaleGestureListener
        = new ScaleGestureDetector.SimpleOnScaleGestureListener() {
    /**
     * This is the active focal point in terms of the viewport. It can be a
     * local variable, but keep it here to minimize per-frame allocations.
     */
    private PointF viewportFocus = new PointF();
    private float lastSpanX;
    private float lastSpanY;

    // Detects new pointers are going down.
    @Override
    public boolean onScaleBegin(ScaleGestureDetector scaleGestureDetector) {
        lastSpanX = ScaleGestureDetectorCompat.
                getCurrentSpanX(scaleGestureDetector);
        lastSpanY = ScaleGestureDetectorCompat.
                getCurrentSpanY(scaleGestureDetector);
        return true;
    }

    @Override
    public boolean onScale(ScaleGestureDetector scaleGestureDetector) {

        float spanX = ScaleGestureDetectorCompat.
                getCurrentSpanX(scaleGestureDetector);
        float spanY = ScaleGestureDetectorCompat.
                getCurrentSpanY(scaleGestureDetector);

        float newWidth = lastSpanX / spanX * mCurrentViewport.width();
        float newHeight = lastSpanY / spanY * mCurrentViewport.height();

        float focusX = scaleGestureDetector.getFocusX();
        float focusY = scaleGestureDetector.getFocusY();
        // Ensures the chart point is within the chart region.
        // See the sample for the implementation of hitTest().
        hitTest(scaleGestureDetector.getFocusX(),
                scaleGestureDetector.getFocusY(),
                viewportFocus);

        mCurrentViewport.set(
                viewportFocus.x
                        - newWidth * (focusX - mContentRect.left)
                        / mContentRect.width(),
                viewportFocus.y
                        - newHeight * (mContentRect.bottom - focusY)
                        / mContentRect.height(),
                0,
                0);
        mCurrentViewport.right = mCurrentViewport.left + newWidth;
        mCurrentViewport.bottom = mCurrentViewport.top + newHeight;
        ...
        // Invalidates the View to update the display.
        ViewCompat.postInvalidateOnAnimation(InteractiveLineGraphView.this);

        lastSpanX = spanX;
        lastSpanY = spanY;
        return true;
    }
};
```

## Additional resources

See the following references for more information about input events, sensors, and making custom views interactive.

- [Input events overview](https://developer.android.com/guide/topics/ui/ui-events)
- [Sensors overview](https://developer.android.com/guide/topics/sensors/sensors_overview)
- [Make a custom view interactive](https://developer.android.com/training/custom-views/making-interactive)