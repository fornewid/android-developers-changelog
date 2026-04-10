---
title: https://developer.android.com/develop/ui/views/touch-and-input/gestures/multi
url: https://developer.android.com/develop/ui/views/touch-and-input/gestures/multi
source: md.txt
---

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to use touch and input in Compose.  
[Multi-touch gestures →](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/multi-touch)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

A multi-touch gesture is when multiple pointers (fingers) tap the screen at
the same time. This document describes how to detect gestures that involve
multiple pointers.

## Track multiple pointers

When multiple pointers tap the screen at the same time, the system generates
the following touch events:

- [ACTION_DOWN](https://developer.android.com/reference/android/view/MotionEvent#ACTION_DOWN): sent when the first pointer taps the screen. This starts the gesture. The pointer data for this pointer is always at index `0` in the [MotionEvent](https://developer.android.com/reference/android/view/MotionEvent).
- [ACTION_POINTER_DOWN](https://developer.android.com/reference/android/view/MotionEvent#ACTION_POINTER_DOWN): sent when extra pointers enter the screen after the first. You can obtain the index of the pointer that just went down using [getActionIndex()](https://developer.android.com/reference/android/view/MotionEvent#getActionIndex()).
- [ACTION_MOVE](https://developer.android.com/reference/android/view/MotionEvent#ACTION_MOVE): sent when a change occurs in a gesture, involving any number of pointers.
- [ACTION_POINTER_UP](https://developer.android.com/reference/android/view/MotionEvent#ACTION_POINTER_UP): sent when a non-primary pointer goes up. You can obtain the index of the pointer that just went up using `getActionIndex()`.
- [ACTION_UP](https://developer.android.com/reference/android/view/MotionEvent#ACTION_UP): sent when the last pointer leaves the screen.
- [ACTION_CANCEL](https://developer.android.com/reference/android/view/MotionEvent#ACTION_CANCEL): indicates that the entire gesture, including all pointers, is canceled.

### Start and end gestures

A gesture is a series of events starting with an `ACTION_DOWN`
event and ending with either an `ACTION_UP` or
`ACTION_CANCEL` event. There is one active gesture at a time. The
actions DOWN, MOVE, UP, and CANCEL apply to the entire gesture. For example, an
event with `ACTION_MOVE` can indicate a movement for all pointers
down at that moment.

### Keep track of pointers

Use the pointer's index and ID to keep track of the individual pointers
positions within a `MotionEvent`.

- **Index** : a `MotionEvent` stores pointer information in an array. The index of a pointer is its position within this array. Most of the `MotionEvent` methods take the pointer index as a parameter, rather than the pointer ID.
- **ID**: each pointer also has an ID mapping that stays persistent across touch events to allow for tracking of an individual pointer across the entire gesture.

Individual pointers appear within a motion event in an undefined order. Thus,
the index of a pointer can change from one event to the next, but the pointer ID
of a pointer is guaranteed to remain constant as long as the pointer remains
active. Use the
[getPointerId()](https://developer.android.com/reference/android/view/MotionEvent#getPointerId(int))
method to obtain a pointer's ID to track the pointer across all subsequent
motion events in a gesture. Then, for successive motion events, use the
[findPointerIndex()](https://developer.android.com/reference/android/view/MotionEvent#findPointerIndex(int))
method to obtain the pointer index for a given pointer ID in that motion event.
For example:  

### Kotlin

```kotlin
private var mActivePointerId: Int = 0

override fun onTouchEvent(event: MotionEvent): Boolean {
    ...
    // Get the pointer ID.
    mActivePointerId = event.getPointerId(0)

    // ... Many touch events later...

    // Use the pointer ID to find the index of the active pointer
    // and fetch its position.
    val (x: Float, y: Float) = event.findPointerIndex(mActivePointerId).let { pointerIndex ->
        // Get the pointer's current position.
        event.getX(pointerIndex) to event.getY(pointerIndex)
    }
    ...
}
```

### Java

```java
private int mActivePointerId;

public boolean onTouchEvent(MotionEvent event) {
    ...
    // Get the pointer ID.
    mActivePointerId = event.getPointerId(0);

    // ... Many touch events later...

    // Use the pointer ID to find the index of the active pointer
    // and fetch its position.
    int pointerIndex = event.findPointerIndex(mActivePointerId);
    // Get the pointer's current position.
    float x = event.getX(pointerIndex);
    float y = event.getY(pointerIndex);
    ...
}
```

To support multiple touch pointers, you can cache all active pointers with
their IDs at their individual `ACTION_POINTER_DOWN` and
`ACTION_DOWN` event time. Remove the pointers from your cache at
their `ACTION_POINTER_UP` and `ACTION_UP`events. You might
find these cached IDs helpful to handle other action events correctly. For
example, when processing an `ACTION_MOVE` event, find the index for
each cached active pointer ID, retrieve the pointer's coordinates using the
[getX()](https://developer.android.com/reference/android/view/MotionEvent#getX(int))
and
[getY()](https://developer.android.com/reference/android/view/MotionEvent#getY(int))
functions, then compare these coordinates with your cached coordinates to
discover which pointers moved.

Use the `getActionIndex()` function with
`ACTION_POINTER_UP` and `ACTION_POINTER_DOWN` events
only. Don't use this function with `ACTION_MOVE` events, as this
always returns `0`.

## Retrieve `MotionEvent` actions

Use the
[getActionMasked()](https://developer.android.com/reference/android/view/MotionEvent#getActionMasked())
method or the compatibility version
[MotionEventCompat.getActionMasked()](https://developer.android.com/reference/androidx/core/view/MotionEventCompat#getActionMasked(android.view.MotionEvent))
to retrieve the action of a `MotionEvent`. Unlike the earlier
[getAction()](https://developer.android.com/reference/android/view/MotionEvent#getAction())
method, `getActionMasked()` is designed to work with multiple
pointers. It returns the action without the pointer indices. For actions with a
valid pointer index, use `getActionIndex()` to return the index of
the pointers associated with the action as shown in the following snippet:
| **Note:** This example uses the [MotionEventCompat](https://developer.android.com/reference/androidx/core/view/MotionEventCompat) class, a class in the [Support
Library](https://developer.android.com/tools/support-library). Use `MotionEventCompat` to provide the best support for a wide range of platforms. `MotionEventCompat` is *not* a replacement for the `MotionEvent` class. Rather, it provides static utility methods to which you pass your `MotionEvent` object to receive the desired action associated with that event.  

### Kotlin

```kotlin
val (xPos: Int, yPos: Int) = MotionEventCompat.getActionMasked(event).let { action ->
    Log.d(DEBUG_TAG, "The action is ${actionToString(action)}")
    // Get the index of the pointer associated with the action.
    MotionEventCompat.getActionIndex(event).let { index ->
        // The coordinates of the current screen contact, relative to
        // the responding View or Activity.
        MotionEventCompat.getX(event, index).toInt() to MotionEventCompat.getY(event, index).toInt()
    }
}

if (event.pointerCount > 1) {
    Log.d(DEBUG_TAG, "Multitouch event")

} else {
    // Single touch event.
    Log.d(DEBUG_TAG, "Single touch event")
}

...

// Given an action int, returns a string description.
fun actionToString(action: Int): String {
    return when (action) {
        MotionEvent.ACTION_DOWN -> "Down"
        MotionEvent.ACTION_MOVE -> "Move"
        MotionEvent.ACTION_POINTER_DOWN -> "Pointer Down"
        MotionEvent.ACTION_UP -> "Up"
        MotionEvent.ACTION_POINTER_UP -> "Pointer Up"
        MotionEvent.ACTION_OUTSIDE -> "Outside"
        MotionEvent.ACTION_CANCEL -> "Cancel"
        else -> ""
    }
}
```

### Java

```java
int action = MotionEventCompat.getActionMasked(event);
// Get the index of the pointer associated with the action.
int index = MotionEventCompat.getActionIndex(event);
int xPos = -1;
int yPos = -1;

Log.d(DEBUG_TAG,"The action is " + actionToString(action));

if (event.getPointerCount() > 1) {
    Log.d(DEBUG_TAG,"Multitouch event");
    // The coordinates of the current screen contact, relative to
    // the responding View or Activity.
    xPos = (int)MotionEventCompat.getX(event, index);
    yPos = (int)MotionEventCompat.getY(event, index);

} else {
    // Single touch event.
    Log.d(DEBUG_TAG,"Single touch event");
    xPos = (int)MotionEventCompat.getX(event, index);
    yPos = (int)MotionEventCompat.getY(event, index);
}
...

// Given an action int, returns a string description
public static String actionToString(int action) {
    switch (action) {

        case MotionEvent.ACTION_DOWN: return "Down";
	case MotionEvent.ACTION_MOVE: return "Move";
	case MotionEvent.ACTION_POINTER_DOWN: return "Pointer Down";
	case MotionEvent.ACTION_UP: return "Up";
	case MotionEvent.ACTION_POINTER_UP: return "Pointer Up";
	case MotionEvent.ACTION_OUTSIDE: return "Outside";
	case MotionEvent.ACTION_CANCEL: return "Cancel";
    }
    return "";
}
```
**Figure 1.** Multi-touch drawing patterns.

## Additional resources

For more information related to input events, see the following
references:

- [Input events overview](https://developer.android.com/guide/topics/ui/ui-events)
- [Sensors
  overview](https://developer.android.com/guide/topics/sensors/sensors_overview)
- [Make a custom
  view interactive](https://developer.android.com/training/custom-views/making-interactive)
- [Drag and scale](https://developer.android.com/develop/ui/views/touch-and-input/gestures/scale)