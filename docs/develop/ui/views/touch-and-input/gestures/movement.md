---
title: https://developer.android.com/develop/ui/views/touch-and-input/gestures/movement
url: https://developer.android.com/develop/ui/views/touch-and-input/gestures/movement
source: md.txt
---

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to use touch and input in Compose.  
[Gestures →](https://developer.android.com/jetpack/compose/touch-input/pointer-input)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

<br />

This lesson describes how to track movement in touch events.

A new
[`onTouchEvent()`](https://developer.android.com/reference/android/view/View#onTouchEvent(android.view.MotionEvent))
is triggered with an
[`ACTION_MOVE`](https://developer.android.com/reference/android/view/MotionEvent#ACTION_MOVE) event
whenever the current touch contact position, pressure, or size changes. As
described in [Detect common gestures](https://developer.android.com/training/gestures/detector), all
these events are recorded in the
[`MotionEvent`](https://developer.android.com/reference/android/view/MotionEvent) parameter of
`onTouchEvent()`.

Because finger-based touch isn't always the most precise form of interaction,
detecting touch events is often based more on movement than on simple contact.
To help apps distinguish between movement-based gestures (such as a swipe) and
non-movement gestures (such as a single tap), Android includes the notion of
*touch slop* . Touch slop refers to the distance in pixels a user's touch can
wander before the gesture is interpreted as a movement-based gesture. For more
information about this topic, see [Manage touch events in a
ViewGroup](https://developer.android.com/training/gestures/viewgroup#vc).

There are several ways to track movement in a gesture, depending on
the needs of your application. The following are examples:

- The starting and ending position of a pointer, such as moving an on-screen object from point A to point B.
- The direction the pointer is traveling in, as determined by the X and Y coordinates.
- History. You can find the size of a gesture's history by calling the `MotionEvent` method [`getHistorySize()`](https://developer.android.com/reference/android/view/MotionEvent#getHistorySize()). You can then obtain the positions, sizes, time, and pressures of each of the historical events by using the motion event's `getHistorical`*<Value>* methods. History is useful when rendering a trail of the user's finger, such as for touch drawing. See the `MotionEvent` reference for details.
- The velocity of the pointer as it moves across the touchscreen.

Refer to the following related resources:

- [Input events overview](https://developer.android.com/guide/topics/ui/ui-events)
- [Sensors overview](https://developer.android.com/guide/topics/sensors/sensors_overview)
- [Make a custom view interactive](https://developer.android.com/training/custom-views/making-interactive)

## Track velocity

You can have a movement-based gesture that is based on the distance or direction
the pointer travels. However, velocity is often a determining factor in tracking
a gesture's characteristics or deciding whether the gesture occurred. To make
velocity calculation easier, Android provides the
[`VelocityTracker`](https://developer.android.com/reference/android/view/VelocityTracker) class.
`VelocityTracker` helps you track the velocity of touch events. This is useful
for gestures in which velocity is part of the criteria for the gesture, such as
a fling.

Here is an example that illustrates the purpose of the methods in the
`VelocityTracker` API:  

### Kotlin

```kotlin
private const val DEBUG_TAG = "Velocity"

class MainActivity : Activity() {
    private var mVelocityTracker: VelocityTracker? = null

    override fun onTouchEvent(event: MotionEvent): Boolean {

        when (event.actionMasked) {
            MotionEvent.ACTION_DOWN -> {
                // Reset the velocity tracker back to its initial state.
                mVelocityTracker?.clear()
                // If necessary, retrieve a new VelocityTracker object to watch
                // the velocity of a motion.
                mVelocityTracker = mVelocityTracker ?: VelocityTracker.obtain()
                // Add a user's movement to the tracker.
                mVelocityTracker?.addMovement(event)
            }
            MotionEvent.ACTION_MOVE -> {
                mVelocityTracker?.apply {
                    val pointerId: Int = event.getPointerId(event.actionIndex)
                    addMovement(event)
                    // When you want to determine the velocity, call
                    // computeCurrentVelocity(). Then, call getXVelocity() and
                    // getYVelocity() to retrieve the velocity for each pointer
                    // ID.
                    computeCurrentVelocity(1000)
                    // Log velocity of pixels per second. It's best practice to
                    // use VelocityTrackerCompat where possible.
                    Log.d("", "X velocity: ${getXVelocity(pointerId)}")
                    Log.d("", "Y velocity: ${getYVelocity(pointerId)}")
                }
            }
            MotionEvent.ACTION_UP, MotionEvent.ACTION_CANCEL -> {
                // Return a VelocityTracker object back to be re-used by others.
                mVelocityTracker?.recycle()
                mVelocityTracker = null
            }
        }
        return true
    }
}
```

### Java

```java
public class MainActivity extends Activity {
    private static final String DEBUG_TAG = "Velocity";
        ...
    private VelocityTracker mVelocityTracker = null;
    @Override
    public boolean onTouchEvent(MotionEvent event) {
        int index = event.getActionIndex();
        int action = event.getActionMasked();
        int pointerId = event.getPointerId(index);

        switch(action) {
            case MotionEvent.ACTION_DOWN:
                if(mVelocityTracker == null) {
                    // Retrieve a new VelocityTracker object to watch the
                    // velocity of a motion.
                    mVelocityTracker = VelocityTracker.obtain();
                }
                else {
                    // Reset the velocity tracker back to its initial state.
                    mVelocityTracker.clear();
                }
                // Add a user's movement to the tracker.
                mVelocityTracker.addMovement(event);
                break;
            case MotionEvent.ACTION_MOVE:
                mVelocityTracker.addMovement(event);
                // When you want to determine the velocity, call
                // computeCurrentVelocity(). Then call getXVelocity() and
                // getYVelocity() to retrieve the velocity for each pointer ID.
                mVelocityTracker.computeCurrentVelocity(1000);
                // Log velocity of pixels per second. It's best practice to use
                // VelocityTrackerCompat where possible.
                Log.d("", "X velocity: " + mVelocityTracker.getXVelocity(pointerId));
                Log.d("", "Y velocity: " + mVelocityTracker.getYVelocity(pointerId));
                break;
            case MotionEvent.ACTION_UP:
            case MotionEvent.ACTION_CANCEL:
                // Return a VelocityTracker object back to be re-used by others.
                mVelocityTracker.recycle();
                break;
        }
        return true;
    }
}
```
| **Note:** Calculate velocity after an `ACTION_MOVE` event, not after [`ACTION_UP`](https://developer.android.com/reference/android/view/MotionEvent#ACTION_UP). After an `ACTION_UP`, the X and Y velocities are 0.

## Use pointer capture

Some apps, such as games and remote desktop and virtualization clients, benefit
from getting control over the mouse pointer. Pointer capture is a feature
available in Android 8.0 (API level 26) and higher that provides this control by
delivering all mouse events to a focused view in your app.

### Request pointer capture

A view in your app can request pointer capture only when the view hierarchy that
contains it has focus. For this reason, request pointer capture when there's a
specific user action on the view, such as during an
[`onClick()`](https://developer.android.com/reference/android/view/View.OnClickListener#onClick(android.view.View))
event or in the
[`onWindowFocusChanged()`](https://developer.android.com/reference/android/app/Activity#onWindowFocusChanged(boolean))
event handler of your activity.

To request pointer capture, call the
[`requestPointerCapture()`](https://developer.android.com/reference/android/view/View#requestPointerCapture())
method on the view. The following code example shows how to request pointer
capture when the user clicks a view:  

### Kotlin

```kotlin
fun onClick(view: View) {
    view.requestPointerCapture()
}
```

### Java

```java
@Override
public void onClick(View view) {
    view.requestPointerCapture();
}
```

Once the request to capture the pointer is successful, Android calls
[`onPointerCaptureChange(true)`](https://developer.android.com/reference/android/view/View#onPointerCaptureChange(boolean)).
The system delivers the mouse events to the focused view in your app as long as
it's in the same view hierarchy as the view that requested the capture. Other
apps stop receiving mouse events until the capture is released, including
[`ACTION_OUTSIDE`](https://developer.android.com/reference/android/view/MotionEvent#ACTION_OUTSIDE)
events. Android delivers pointer events from sources other than the mouse as
normal, but the mouse pointer is no longer visible.

### Handle captured pointer events

Once a view successfully acquires the pointer capture, Android delivers the
mouse events. Your focused view can handle the events by performing one of the
following tasks:

- If you're using a custom view, override [`onCapturedPointerEvent(MotionEvent)`](https://developer.android.com/reference/android/view/View#onCapturedPointerEvent(android.view.MotionEvent)).
- Otherwise, register an [`OnCapturedPointerListener`](https://developer.android.com/reference/android/view/View.OnCapturedPointerListener).

The following code example shows how to implement
[`onCapturedPointerEvent(MotionEvent)`](https://developer.android.com/reference/android/view/View#onCapturedPointerEvent(android.view.MotionEvent)):  

### Kotlin

```kotlin
override fun onCapturedPointerEvent(motionEvent: MotionEvent): Boolean {
    // Get the coordinates required by your app.
    val verticalOffset: Float = motionEvent.y
    // Use the coordinates to update your view and return true if the event is
    // successfully processed.
    return true
}
```

### Java

```java
@Override
public boolean onCapturedPointerEvent(MotionEvent motionEvent) {
  // Get the coordinates required by your app.
  float verticalOffset = motionEvent.getY();
  // Use the coordinates to update your view and return true if the event is
  // successfully processed.
  return true;
}
```

The following code example shows how to register an
[`OnCapturedPointerListener`](https://developer.android.com/reference/android/view/View.OnCapturedPointerListener):  

### Kotlin

```kotlin
myView.setOnCapturedPointerListener { view, motionEvent ->
    // Get the coordinates required by your app.
    val horizontalOffset: Float = motionEvent.x
    // Use the coordinates to update your view and return true if the event is
    // successfully processed.
    true
}
```

### Java

```java
myView.setOnCapturedPointerListener(new View.OnCapturedPointerListener() {
  @Override
  public boolean onCapturedPointer (View view, MotionEvent motionEvent) {
    // Get the coordinates required by your app.
    float horizontalOffset = motionEvent.getX();
    // Use the coordinates to update your view and return true if the event is
    // successfully processed.
    return true;
  }
});
```

Whether you use a custom view or register a listener, your view receives a
`MotionEvent` with pointer coordinates that specify relative movements such as X
or Y deltas, similar to the coordinates delivered by a trackball device. You can
retrieve the coordinates by using
[`getX()`](https://developer.android.com/reference/android/view/MotionEvent#getX()) and
[`getY()`](https://developer.android.com/reference/android/view/MotionEvent#getY()).

### Release pointer capture

The view in your app can release the pointer capture by calling
[`releasePointerCapture()`](https://developer.android.com/reference/android/view/View#releasePointerCapture()),
as shown in the following code example:  

### Kotlin

```kotlin
override fun onClick(view: View) {
    view.releasePointerCapture()
}
```

### Java

```java
@Override
public void onClick(View view) {
    view.releasePointerCapture();
}
```

The system can take the capture away from the view without you explicitly
calling `releasePointerCapture()`, commonly because the view hierarchy
containing the view that requests capture loses focus.