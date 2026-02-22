---
title: https://developer.android.com/develop/ui/views/touch-and-input/gestures/detector
url: https://developer.android.com/develop/ui/views/touch-and-input/gestures/detector
source: md.txt
---

# Detect common gestures

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to use touch and input in Compose.  
[Gestures →](https://developer.android.com/jetpack/compose/touch-input/pointer-input)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

A*touch gesture*occurs when a user places one or more fingers on the touchscreen and your app interprets this pattern of touches as a gesture. There are two phases to gesture detection:

1. Gathering touch event data.
2. Interpreting the data to determine whether it meets the criteria for the gestures your app supports.

#### AndroidX classes

The examples in this document use the[GestureDetectorCompat](https://developer.android.com/reference/androidx/core/view/GestureDetectorCompat)and[MotionEventCompat](https://developer.android.com/reference/androidx/core/view/MotionEventCompat)classes. These classes are in the[AndroidX Library](https://developer.android.com/jetpack/androidx). Use AndroidX classes where possible to provide compatibility with earlier devices.`MotionEventCompat`is*not* a replacement for the[MotionEvent](https://developer.android.com/reference/android/view/MotionEvent)class. Rather, it provides static utility methods to which you pass your`MotionEvent`object to receive the action associated with that event.

## Gather data

When a user places one or more fingers on the screen, this triggers the callback[onTouchEvent()](https://developer.android.com/reference/android/view/View#onTouchEvent(android.view.MotionEvent))on the view that receives the touch events. For each sequence of touch events---such as position, pressure, size, and addition of another finger---that is identified as a gesture,`onTouchEvent()`is fired several times.

The gesture starts when the user first touches the screen, continues as the system tracks the position of the user's finger or fingers, and ends by capturing the final event of the user's last finger leaving the screen. Throughout this interaction, the`MotionEvent`delivered to`onTouchEvent()`provides the details of every interaction. Your app can use the data provided by the`MotionEvent`to determine whether a gesture it cares about happens.

### Capture touch events for an Activity or View

<br />

To intercept touch events in an`Activity`or`View`, override the`onTouchEvent()`callback.

The following code snippet uses[getAction()](https://developer.android.com/reference/android/view/MotionEvent#getAction())to extract the action the user performs from the`event`parameter. This gives you the raw data you need to determine whether a gesture you care about occurs.  

### Kotlin

```kotlin
class MainActivity : Activity() {
    ...
    // This example shows an Activity. You can use the same approach if you are 
    // subclassing a View.
    override fun onTouchEvent(event: MotionEvent): Boolean {
        return when (event.action) {
            MotionEvent.ACTION_DOWN -> {
                Log.d(DEBUG_TAG, "Action was DOWN")
                true
            }
            MotionEvent.ACTION_MOVE -> {
                Log.d(DEBUG_TAG, "Action was MOVE")
                true
            }
            MotionEvent.ACTION_UP -> {
                Log.d(DEBUG_TAG, "Action was UP")
                true
            }
            MotionEvent.ACTION_CANCEL -> {
                Log.d(DEBUG_TAG, "Action was CANCEL")
                true
            }
            MotionEvent.ACTION_OUTSIDE -> {
                Log.d(DEBUG_TAG, "Movement occurred outside bounds of current screen element")
                true
            }
            else -> super.onTouchEvent(event)
        }
    }
}
```

### Java

```java
public class MainActivity extends Activity {
...
// This example shows an Activity. You can use the same approach if you are
// subclassing a View.
@Override
public boolean onTouchEvent(MotionEvent event){
    switch(event.getAction()) {
        case (MotionEvent.ACTION_DOWN) :
            Log.d(DEBUG_TAG,"Action was DOWN");
            return true;
        case (MotionEvent.ACTION_MOVE) :
            Log.d(DEBUG_TAG,"Action was MOVE");
            return true;
        case (MotionEvent.ACTION_UP) :
            Log.d(DEBUG_TAG,"Action was UP");
            return true;
        case (MotionEvent.ACTION_CANCEL) :
            Log.d(DEBUG_TAG,"Action was CANCEL");
            return true;
        case (MotionEvent.ACTION_OUTSIDE) :
            Log.d(DEBUG_TAG,"Movement occurred outside bounds of current screen element");
            return true;
        default :
            return super.onTouchEvent(event);
    }
}
```

This code produces messages like the following in Logcat as the user taps, touches \& holds, and drags:  

```bash
GESTURES D   Action was DOWN
GESTURES D   Action was UP
GESTURES D   Action was MOVE
```

For custom gestures, you can then do your own processing on these events to determine whether they represent a gesture you need to handle. However, if your app uses common gestures, such as double-tap, touch \& hold, fling, and so on, you can take advantage of the[GestureDetector](https://developer.android.com/reference/android/view/GestureDetector)class.`GestureDetector`makes it easier for you to detect common gestures without processing the individual touch events yourself. This is discussed further in[Detect gestures](https://developer.android.com/develop/ui/views/touch-and-input/gestures/detector#detect).

### Capture touch events for a single view

As an alternative to`onTouchEvent()`, you can attach a[View.OnTouchListener](https://developer.android.com/reference/android/view/View.OnTouchListener)object to any[View](https://developer.android.com/reference/android/view/View)object using the[setOnTouchListener()](https://developer.android.com/reference/android/view/View#setOnTouchListener(android.view.View.OnTouchListener))method. This makes it possible to listen for touch events without subclassing an existing`View`, as shown in the following example:  

### Kotlin

```kotlin
findViewById<View>(R.id.my_view).setOnTouchListener { v, event ->
    // Respond to touch events.
    true
}
```

### Java

```java
View myView = findViewById(R.id.my_view);
myView.setOnTouchListener(new OnTouchListener() {
    public boolean onTouch(View v, MotionEvent event) {
        // Respond to touch events.
        return true;
    }
});
```

Beware of creating a listener that returns`false`for the[ACTION_DOWN](https://developer.android.com/reference/android/view/MotionEvent#ACTION_DOWN)event. If you do this, the listener isn't called for the subsequent[ACTION_MOVE](https://developer.android.com/reference/android/view/MotionEvent#ACTION_MOVE)and[ACTION_UP](https://developer.android.com/reference/android/view/MotionEvent#ACTION_UP)sequence of events. This is because`ACTION_DOWN`is the starting point for all touch events.

If you are creating a custom view, you can override`onTouchEvent()`, as described earlier.

## Detect gestures

Android provides the`GestureDetector`class for detecting common gestures. Some of the gestures it supports include[onDown()](https://developer.android.com/reference/android/view/GestureDetector.OnGestureListener#onDown(android.view.MotionEvent)),[onLongPress()](https://developer.android.com/reference/android/view/GestureDetector.OnGestureListener#onLongPress(android.view.MotionEvent)), and[onFling()](https://developer.android.com/reference/android/view/GestureDetector.OnGestureListener#onFling(android.view.MotionEvent, android.view.MotionEvent, float, float)). You can use`GestureDetector`in conjunction with the`onTouchEvent()`method described earlier.

### Detect all supported gestures

When you instantiate a`GestureDetectorCompat`object, one of the parameters it takes is a class that implements the[GestureDetector.OnGestureListener](https://developer.android.com/reference/android/view/GestureDetector.OnGestureListener)interface.`GestureDetector.OnGestureListener`notifies users when a particular touch event occurs. To make it possible for your`GestureDetector`object to receive events, override the view or activity's`onTouchEvent()`method and pass along all observed events to the detector instance.

In the following snippet, a return value of`true`from the individual`on`*<TouchEvent>*methods indicates that the touch event is handled. A return value of`false`passes events down through the view stack until the touch is successfully handled.

If you run the following snippet in a test app, you can get a feel for how actions are triggered when you interact with the touch screen and what the contents of the`MotionEvent`are for each touch event. You then see how much data is being generated for simple interactions.  

### Kotlin

```kotlin
private const val DEBUG_TAG = "Gestures"

class MainActivity :
        Activity(),
        GestureDetector.OnGestureListener,
        GestureDetector.OnDoubleTapListener {

    private lateinit var mDetector: GestureDetectorCompat

    // Called when the activity is first created.
    public override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        // Instantiate the gesture detector with the
        // application context and an implementation of
        // GestureDetector.OnGestureListener.
        mDetector = GestureDetectorCompat(this, this)
        // Set the gesture detector as the double-tap
        // listener.
        mDetector.setOnDoubleTapListener(this)
    }

    override fun onTouchEvent(event: MotionEvent): Boolean {
        return if (mDetector.onTouchEvent(event)) {
            true
        } else {
            super.onTouchEvent(event)
        }
    }

    override fun onDown(event: MotionEvent): Boolean {
        Log.d(DEBUG_TAG, "onDown: $event")
        return true
    }

    override fun onFling(
            event1: MotionEvent,
            event2: MotionEvent,
            velocityX: Float,
            velocityY: Float
    ): Boolean {
        Log.d(DEBUG_TAG, "onFling: $event1 $event2")
        return true
    }

    override fun onLongPress(event: MotionEvent) {
        Log.d(DEBUG_TAG, "onLongPress: $event")
    }

    override fun onScroll(
            event1: MotionEvent,
            event2: MotionEvent,
            distanceX: Float,
            distanceY: Float
    ): Boolean {
        Log.d(DEBUG_TAG, "onScroll: $event1 $event2")
        return true
    }

    override fun onShowPress(event: MotionEvent) {
        Log.d(DEBUG_TAG, "onShowPress: $event")
    }

    override fun onSingleTapUp(event: MotionEvent): Boolean {
        Log.d(DEBUG_TAG, "onSingleTapUp: $event")
        return true
    }

    override fun onDoubleTap(event: MotionEvent): Boolean {
        Log.d(DEBUG_TAG, "onDoubleTap: $event")
        return true
    }

    override fun onDoubleTapEvent(event: MotionEvent): Boolean {
        Log.d(DEBUG_TAG, "onDoubleTapEvent: $event")
        return true
    }

    override fun onSingleTapConfirmed(event: MotionEvent): Boolean {
        Log.d(DEBUG_TAG, "onSingleTapConfirmed: $event")
        return true
    }

}
```

### Java

```java
public class MainActivity extends Activity implements
        GestureDetector.OnGestureListener,
        GestureDetector.OnDoubleTapListener{

    private static final String DEBUG_TAG = "Gestures";
    private GestureDetectorCompat mDetector;

    // Called when the activity is first created.
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // Instantiate the gesture detector with the
        // application context and an implementation of
        // GestureDetector.OnGestureListener.
        mDetector = new GestureDetectorCompat(this,this);
        // Set the gesture detector as the double-tap
        // listener.
        mDetector.setOnDoubleTapListener(this);
    }

    @Override
    public boolean onTouchEvent(MotionEvent event){
        if (this.mDetector.onTouchEvent(event)) {
            return true;
        }
        return super.onTouchEvent(event);
    }

    @Override
    public boolean onDown(MotionEvent event) {
        Log.d(DEBUG_TAG,"onDown: " + event.toString());
        return true;
    }

    @Override
    public boolean onFling(MotionEvent event1, MotionEvent event2,
            float velocityX, float velocityY) {
        Log.d(DEBUG_TAG, "onFling: " + event1.toString() + event2.toString());
        return true;
    }

    @Override
    public void onLongPress(MotionEvent event) {
        Log.d(DEBUG_TAG, "onLongPress: " + event.toString());
    }

    @Override
    public boolean onScroll(MotionEvent event1, MotionEvent event2, float distanceX,
            float distanceY) {
        Log.d(DEBUG_TAG, "onScroll: " + event1.toString() + event2.toString());
        return true;
    }

    @Override
    public void onShowPress(MotionEvent event) {
        Log.d(DEBUG_TAG, "onShowPress: " + event.toString());
    }

    @Override
    public boolean onSingleTapUp(MotionEvent event) {
        Log.d(DEBUG_TAG, "onSingleTapUp: " + event.toString());
        return true;
    }

    @Override
    public boolean onDoubleTap(MotionEvent event) {
        Log.d(DEBUG_TAG, "onDoubleTap: " + event.toString());
        return true;
    }

    @Override
    public boolean onDoubleTapEvent(MotionEvent event) {
        Log.d(DEBUG_TAG, "onDoubleTapEvent: " + event.toString());
        return true;
    }

    @Override
    public boolean onSingleTapConfirmed(MotionEvent event) {
        Log.d(DEBUG_TAG, "onSingleTapConfirmed: " + event.toString());
        return true;
    }
}
```

### Detect a subset of supported gestures

If you only want to process a few gestures, you can extend[GestureDetector.SimpleOnGestureListener](https://developer.android.com/reference/android/view/GestureDetector.SimpleOnGestureListener)instead of implementing the`GestureDetector.OnGestureListener`interface.

`GestureDetector.SimpleOnGestureListener`provides an implementation for all of the`on`*<TouchEvent>*methods by returning`false`for all of them. This lets you override only the methods you care about. For example, the following code snippet creates a class that extends`GestureDetector.SimpleOnGestureListener`and overrides`onFling()`and`onDown()`.

Whether you use`GestureDetector.OnGestureListener`or`GestureDetector.SimpleOnGestureListener`, it's a best practice to implement an`onDown()`method that returns`true`. This is because all gestures begin with an`onDown()`message. If you return`false`from`onDown()`, as`GestureDetector.SimpleOnGestureListener`does by default, the system assumes you want to ignore the rest of the gesture, and the other methods of`GestureDetector.OnGestureListener`aren't called. This might cause unexpected problems in your app. Only return`false`from`onDown()`if you truly want to ignore an entire gesture.  

### Kotlin

```kotlin
private const val DEBUG_TAG = "Gestures"

class MainActivity : Activity() {

    private lateinit var mDetector: GestureDetectorCompat

    public override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        mDetector = GestureDetectorCompat(this, MyGestureListener())
    }

    override fun onTouchEvent(event: MotionEvent): Boolean {
        mDetector.onTouchEvent(event)
        return super.onTouchEvent(event)
    }

    private class MyGestureListener : GestureDetector.SimpleOnGestureListener() {

        override fun onDown(event: MotionEvent): Boolean {
            Log.d(DEBUG_TAG, "onDown: $event")
            return true
        }

        override fun onFling(
                event1: MotionEvent,
                event2: MotionEvent,
                velocityX: Float,
                velocityY: Float
        ): Boolean {
            Log.d(DEBUG_TAG, "onFling: $event1 $event2")
            return true
        }
    }
}
```

### Java

```java
public class MainActivity extends Activity {

    private GestureDetectorCompat mDetector;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mDetector = new GestureDetectorCompat(this, new MyGestureListener());
    }

    @Override
    public boolean onTouchEvent(MotionEvent event){
        if (this.mDetector.onTouchEvent(event)) {
              return true;
        }
        return super.onTouchEvent(event);
    }

    class MyGestureListener extends GestureDetector.SimpleOnGestureListener {
        private static final String DEBUG_TAG = "Gestures";

        @Override
        public boolean onDown(MotionEvent event) {
            Log.d(DEBUG_TAG,"onDown: " + event.toString());
            return true;
        }

        @Override
        public boolean onFling(MotionEvent event1, MotionEvent event2,
                float velocityX, float velocityY) {
            Log.d(DEBUG_TAG, "onFling: " + event1.toString() + event2.toString());
            return true;
        }
    }
}
```

## Additional resources

- [Input events overview](https://developer.android.com/guide/topics/ui/ui-events)
- [Sensors overview](https://developer.android.com/guide/topics/sensors/sensors_overview)
- [Make a custom view interactive](https://developer.android.com/training/custom-views/making-interactive)