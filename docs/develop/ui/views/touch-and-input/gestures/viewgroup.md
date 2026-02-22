---
title: https://developer.android.com/develop/ui/views/touch-and-input/gestures/viewgroup
url: https://developer.android.com/develop/ui/views/touch-and-input/gestures/viewgroup
source: md.txt
---

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn about gestures in Compose.  
[Gestures →](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/understand-gestures#event-propagation)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

Handling touch events in a
[ViewGroup](https://developer.android.com/reference/android/view/ViewGroup) takes special care
because it's common for a `ViewGroup` to have children that are targets for different
touch events than the `ViewGroup` itself. To make sure each view correctly receives the
touch events intended for it, override the
[onInterceptTouchEvent()](https://developer.android.com/reference/android/view/ViewGroup#onInterceptTouchEvent(android.view.MotionEvent))
method.  
Refer to the following related resources:

- [Input events overview](https://developer.android.com/guide/topics/ui/ui-events)
- [Sensors overview](https://developer.android.com/guide/topics/sensors/sensors_overview)
- [Make a custom view interactive](https://developer.android.com/training/custom-views/making-interactive)

## Intercept touch events in a ViewGroup

The `onInterceptTouchEvent()` method is called whenever a touch event is detected on
the surface of a `ViewGroup`, including on the surface of its children. If
`onInterceptTouchEvent()` returns `true`, the
[MotionEvent](https://developer.android.com/reference/android/view/MotionEvent)
is intercepted, meaning it isn't passed onto the child but rather to the
[onTouchEvent()](https://developer.android.com/reference/android/view/View#onTouchEvent(android.view.MotionEvent))
method of the parent.

The `onInterceptTouchEvent()` method gives a parent the chance to see touch events
before its children do. If you return `true` from `onInterceptTouchEvent()`,
the child view that was previously handling touch events receives an
[ACTION_CANCEL](https://developer.android.com/reference/android/view/MotionEvent#ACTION_CANCEL),
and the events from that point forward are sent to the parent's `onTouchEvent()` method
for the usual handling. `onInterceptTouchEvent()` can also return `false` and
spy on events as they travel down the view hierarchy to their usual targets, which handle the
events with their own `onTouchEvent()`.

In the following snippet, the `MyViewGroup` class extends `ViewGroup`.
`MyViewGroup` contains multiple child views. If you drag your finger across a child view
horizontally, the child view no longer gets touch events, and `MyViewGroup` handles touch
events by scrolling its contents. However, if you tap buttons in the child view, or scroll the child
view vertically, the parent doesn't intercept those touch events because the child is the intended
target. In those cases, `onInterceptTouchEvent()` returns `false`, and the
`MyViewGroup` class's `onTouchEvent()` isn't called.  

### Kotlin

```kotlin
class MyViewGroup @JvmOverloads constructor(
        context: Context,
        private val mTouchSlop: Int = ViewConfiguration.get(context).scaledTouchSlop
) : ViewGroup(context) {
    ...
    override fun onInterceptTouchEvent(ev: MotionEvent): Boolean {
        // This method only determines whether you want to intercept the motion.
        // If this method returns true, onTouchEvent is called and you can do
        // the actual scrolling there.
        return when (ev.actionMasked) {
            // Always handle the case of the touch gesture being complete.
            MotionEvent.ACTION_CANCEL, MotionEvent.ACTION_UP -> {
                // Release the scroll.
                mIsScrolling = false
                false // Don't intercept the touch event. Let the child handle it.
            }
            MotionEvent.ACTION_MOVE -> {
                if (mIsScrolling) {
                    // You're currently scrolling, so intercept the touch event.
                    true
                } else {

                    // If the user drags their finger horizontally more than the
                    // touch slop, start the scroll.

                    // Left as an exercise for the reader.
                    val xDiff: Int = calculateDistanceX(ev)

                    // Touch slop is calculated using ViewConfiguration constants.
                    if (xDiff > mTouchSlop) {
                        // Start scrolling!
                        mIsScrolling = true
                        true
                    } else {
                        false
                    }
                }
            }
            ...
            else -> {
                // In general, don't intercept touch events. The child view
                // handles them.
                false
            }
        }
    }

    override fun onTouchEvent(event: MotionEvent): Boolean {
        // Here, you actually handle the touch event. For example, if the action
        // is ACTION_MOVE, scroll this container. This method is only called if
        // the touch event is intercepted in onInterceptTouchEvent.
        ...
    }
}
```

### Java

```java
public class MyViewGroup extends ViewGroup {

    private int mTouchSlop;
    ...
    ViewConfiguration vc = ViewConfiguration.get(view.getContext());
    mTouchSlop = vc.getScaledTouchSlop();
    ...
    @Override
    public boolean onInterceptTouchEvent(MotionEvent ev) {
        // This method only determines whether you want to intercept the motion.
        // If this method returns true, onTouchEvent is called and you can do
        // the actual scrolling there.

        final int action = MotionEventCompat.getActionMasked(ev);

        // Always handle the case of the touch gesture being complete.
        if (action == MotionEvent.ACTION_CANCEL || action == MotionEvent.ACTION_UP) {
            // Release the scroll.
            mIsScrolling = false;
            return false; // Don't intercept touch event. Let the child handle it.
        }

        switch (action) {
            case MotionEvent.ACTION_MOVE: {
                if (mIsScrolling) {
                    // You're currently scrolling, so intercept the touch event.
                    return true;
                }

                // If the user drags their finger horizontally more than the
                // touch slop, start the scroll.

                // Left as an exercise for the reader.
                final int xDiff = calculateDistanceX(ev);

                // Touch slop is calculated using ViewConfiguration constants.
                if (xDiff > mTouchSlop) {
                    // Start scrolling.
                    mIsScrolling = true;
                    return true;
                }
                break;
            }
            ...
        }

        // In general, don't intercept touch events. The child view handles them.
        return false;
    }

    @Override
    public boolean onTouchEvent(MotionEvent ev) {
        // Here, you actually handle the touch event. For example, if the
        // action is ACTION_MOVE, scroll this container. This method is only
        // called if the touch event is intercepted in onInterceptTouchEvent.
        ...
    }
}
```

Note that `ViewGroup` also provides a
[requestDisallowInterceptTouchEvent()](https://developer.android.com/reference/android/view/ViewGroup#requestDisallowInterceptTouchEvent(boolean))
method. The `ViewGroup` calls this method when a child doesn't want the parent and its
ancestors to intercept touch events with `onInterceptTouchEvent()`.

### Process ACTION_OUTSIDE events

If a `ViewGroup` receives a `MotionEvent` with an
[ACTION_OUTSIDE](https://developer.android.com/reference/android/view/MotionEvent#ACTION_OUTSIDE),
the event isn't dispatched to its children by default. To process a `MotionEvent` with
`ACTION_OUTSIDE`, either override
[dispatchTouchEvent(MotionEvent event)](https://developer.android.com/reference/android/view/ViewGroup#dispatchTouchEvent(android.view.MotionEvent))
to dispatch to the appropriate [View](https://developer.android.com/reference/android/view/View) or
handle it in the relevant
[Window.Callback](https://developer.android.com/reference/android/view/Window.Callback)---for
example, [Activity](https://developer.android.com/reference/android/app/Activity).

## Use ViewConfiguration constants

The preceding snippet uses the current `ViewConfiguration` to initialize a variable
called `mTouchSlop`. You can use the `ViewConfiguration` class to access
common distances, speeds, and times used by the Android system.

"Touch slop" refers to the distance in pixels a user's touch can wander before the gesture is
interpreted as scrolling. Touch slop is typically used to prevent accidental scrolling when the user
is performing another touch operation, such as touching on-screen elements.

Two other commonly used `ViewConfiguration` methods are
[getScaledMinimumFlingVelocity()](https://developer.android.com/reference/android/view/ViewConfiguration#getScaledMinimumFlingVelocity())
and
[getScaledMaximumFlingVelocity()](https://developer.android.com/reference/android/view/ViewConfiguration#getScaledMaximumFlingVelocity()).
These methods return the minimum and maximum velocity, respectively, to initiate a fling measured
in pixels per second. For example:  

### Kotlin

```kotlin
private val vc: ViewConfiguration = ViewConfiguration.get(context)
private val mSlop: Int = vc.scaledTouchSlop
private val mMinFlingVelocity: Int = vc.scaledMinimumFlingVelocity
private val mMaxFlingVelocity: Int = vc.scaledMaximumFlingVelocity
...
MotionEvent.ACTION_MOVE -> {
    ...
    val deltaX: Float = motionEvent.rawX - mDownX
    if (Math.abs(deltaX) > mSlop) {
        // A swipe occurs, do something.
    }
    return false
}
...
MotionEvent.ACTION_UP -> {
    ...
    if (velocityX in mMinFlingVelocity..mMaxFlingVelocity && velocityY < velocityX) {
        // The criteria are satisfied, do something.
    }
}
```

### Java

```java
ViewConfiguration vc = ViewConfiguration.get(view.getContext());
private int mSlop = vc.getScaledTouchSlop();
private int mMinFlingVelocity = vc.getScaledMinimumFlingVelocity();
private int mMaxFlingVelocity = vc.getScaledMaximumFlingVelocity();
...
case MotionEvent.ACTION_MOVE: {
    ...
    float deltaX = motionEvent.getRawX() - mDownX;
    if (Math.abs(deltaX) > mSlop) {
        // A swipe occurs, do something.
    }
...
case MotionEvent.ACTION_UP: {
    ...
    } if (mMinFlingVelocity <= velocityX && velocityX <= mMaxFlingVelocity
            && velocityY < velocityX) {
        // The criteria are satisfied, do something.
    }
}
```

## Extend a child view's touchable area

Android provides the
[TouchDelegate](https://developer.android.com/reference/android/view/TouchDelegate) class to make it
possible for a parent to extend the touchable area of a child view beyond the child's bounds. This
is useful when the child has to be small but needs a larger touch region. You can also use this
approach to shrink the child's touch region.

In the following example, an
[ImageButton](https://developer.android.com/reference/android/widget/ImageButton) is the _delegate
view_---that is, the child whose touch area the parent extends. Here is the layout file:  

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
     android:id="@+id/parent_layout"
     android:layout_width="match_parent"
     android:layout_height="match_parent"
     tools:context=".MainActivity" >

     <ImageButton android:id="@+id/button"
          android:layout_width="wrap_content"
          android:layout_height="wrap_content"
          android:background="@null"
          android:src="@drawable/icon" />
</RelativeLayout>
```

The following snippet completes these tasks:

- Gets the parent view and posts a [Runnable](https://developer.android.com/reference/java/lang/Runnable) on the UI thread. This makes sure that the parent lays out its children before calling the [getHitRect()](https://developer.android.com/reference/android/view/View#getHitRect(android.graphics.Rect)) method. The `getHitRect()` method gets the child's *hit rectangle* (or touchable area) in the parent's coordinates.
- Finds the `ImageButton` child view and calls `getHitRect()` to get the bounds of the child's touchable area.
- Extends the bounds of the `ImageButton` child view's hit rectangle.
- Instantiates a `TouchDelegate`, passing in the expanded hit rectangle and the `ImageButton` child view as parameters.
- Sets the `TouchDelegate` on the parent view so that touches within the touch delegate bounds are routed to the child.

In its capacity as touch delegate for the `ImageButton` child view, the parent view
receives all touch events. If the touch event occurs within the child's hit rectangle, the parent
passes the touch event to the child for handling.  

### Kotlin

```kotlin
public class MainActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Post in the parent's message queue to make sure the parent lays out
        // its children before you call getHitRect().
        findViewById<View>(R.id.parent_layout).post {
            // The bounds for the delegate view, which is an ImageButton in this
            // example.
            val delegateArea = Rect()
            val myButton = findViewById<ImageButton>(R.id.button).apply {
                isEnabled = true
                setOnClickListener {
                    Toast.makeText(
                            this@MainActivity,
                            "Touch occurred within ImageButton touch region.",
                            Toast.LENGTH_SHORT
                    ).show()
                }

                // The hit rectangle for the ImageButton.
                getHitRect(delegateArea)
            }

            // Extend the touch area of the ImageButton beyond its bounds on the
            // right and bottom.
            delegateArea.right += 100
            delegateArea.bottom += 100

            // Set the TouchDelegate on the parent view so that touches within
            // the touch delegate bounds are routed to the child.
            (myButton.parent as? View)?.apply {
                // Instantiate a TouchDelegate. "delegateArea" is the bounds in
                // local coordinates of the containing view to be mapped to the
                // delegate view. "myButton" is the child view that receives
                // motion events.
                touchDelegate = TouchDelegate(delegateArea, myButton)
            }
        }
    }
}
```

### Java

```java
public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // Get the parent view.
        View parentView = findViewById(R.id.parent_layout);

        parentView.post(new Runnable() {
            // Post in the parent's message queue to make sure the parent lays
            // out its children before you call getHitRect().
            @Override
            public void run() {
                // The bounds for the delegate view, which is an ImageButton in
                // this example.
                Rect delegateArea = new Rect();
                ImageButton myButton = (ImageButton) findViewById(R.id.button);
                myButton.setEnabled(true);
                myButton.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View view) {
                        Toast.makeText(MainActivity.this,
                                "Touch occurred within ImageButton touch region.",
                                Toast.LENGTH_SHORT).show();
                    }
                });

                // The hit rectangle for the ImageButton.
                myButton.getHitRect(delegateArea);

                // Extend the touch area of the ImageButton beyond its bounds on
                // the right and bottom.
                delegateArea.right += 100;
                delegateArea.bottom += 100;

                // Instantiate a TouchDelegate. "delegateArea" is the bounds in
                // local coordinates of the containing view to be mapped to the
                // delegate view. "myButton" is the child view that receives
                // motion events.
                TouchDelegate touchDelegate = new TouchDelegate(delegateArea,
                        myButton);

                // Set the TouchDelegate on the parent view so that touches
                // within the touch delegate bounds are routed to the child.
                if (View.class.isInstance(myButton.getParent())) {
                    ((View) myButton.getParent()).setTouchDelegate(touchDelegate);
                }
            }
        });
    }
}
```