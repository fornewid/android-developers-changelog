---
title: https://developer.android.com/training/wearables/views/exit
url: https://developer.android.com/training/wearables/views/exit
source: md.txt
---

# Exit full-screen activities on Wear

Try the Compose way  
Jetpack Compose on Wear OS is the recommended UI toolkit for Wear OS.  
[Try Compose on Wear OS →](https://developer.android.com/training/wearables/compose)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

A user can exit a Wear OS activity by swiping from left to right. If the app has horizontal scrolling, the user exits by navigating to the edge of the content and then swiping from left to right. Pressing the power button also returns the user to the watch face.

## The swipe-to-dismiss gesture

Users swipe from left to right to close the current screen. Therefore, we recommend that you use the following:

- Vertical layouts
- Content containers

We also recommend that your app not contain horizontal swiping gestures.

### Dismiss an activity

Activities automatically support swipe-to-dismiss. Swiping an activity from left to right results in dismissal of the activity, and the app navigates down the[back stack](https://developer.android.com/guide/components/tasks-and-back-stack).

### Dismiss a fragment

To support swipe-to-dismiss in fragments, you must wrap the fragment-containing view in the[`SwipeDismissFrameLayout`](https://developer.android.com/reference/androidx/wear/widget/SwipeDismissFrameLayout)class. Take this into consideration when deciding whether to use fragments. Use the`SwipeDismissFrameLayout`class as shown in the following example:  

### Kotlin

```kotlin
class SwipeDismissFragment : Fragment() {
    private val callback = object : SwipeDismissFrameLayout.Callback() {
        override fun onSwipeStarted(layout: SwipeDismissFrameLayout) {
            // Optional
        }

        override fun onSwipeCanceled(layout: SwipeDismissFrameLayout) {
            // Optional
        }

        override fun onDismissed(layout: SwipeDismissFrameLayout) {
            // Code here for custom behavior, such as going up the
            // back stack and destroying the fragment but staying in the app.
        }
    }

    override fun onCreateView(
            inflater: LayoutInflater,
            container: ViewGroup?,
            savedInstanceState: Bundle?
    ): View =
            SwipeDismissFrameLayout(activity).apply {

                // If the fragment should fill the screen (optional), then in the layout file,
                // in the androidx.wear.widget.SwipeDismissFrameLayout element,
                // set the android:layout_width and android:layout_height attributes
                // to "match_parent".

                inflater.inflate(
                        R.layout.swipe_dismiss_frame_layout,
                        this,
                        false
                ).also { inflatedView ->
                    addView(inflatedView)
                }
                addCallback(callback)
            }
}
```

### Java

```java
public class SwipeDismissFragment extends Fragment {
  private final Callback callback =
    new Callback() {
      @Override
        public void onSwipeStart() {
          // Optional
        }

        @Override
        public void onSwipeCancelled() {
          // Optional
        }

        @Override
        public void onDismissed(SwipeDismissFrameLayout layout) {
          // Code here for custom behavior, such as going up the
          // back stack and destroying the fragment but staying in the app.
        }
      };

  @Override
  public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
    SwipeDismissFrameLayout swipeLayout = new SwipeDismissFrameLayout(getActivity());

    // If the fragment should fill the screen (optional), then in the layout file,
    // in the androidx.wear.widget.SwipeDismissFrameLayout element,
    // set the android:layout_width and android:layout_height attributes
    // to "match_parent".

    View inflatedView = inflater.inflate(R.layout.swipe_dismiss_frame_layout, swipeLayout, false);
    swipeLayout.addView(inflatedView);
    swipeLayout.addCallback(callback);

    return swipeLayout;
    }
}
```

**Note:** When you use fragments within your activity, use[`FragmentManager.add`](https://developer.android.com/reference/androidx/fragment/app/FragmentTransaction#add(int,%20java.lang.Class<?%20extends%20androidx.fragment.app.Fragment>,%20android.os.Bundle))rather than[`FragmentManager.replace`](https://developer.android.com/reference/androidx/fragment/app/FragmentTransaction#replace(int,%20java.lang.Class<?%20extends%20androidx.fragment.app.Fragment>,%20android.os.Bundle))to support the swipe-to-dismiss gesture. This helps ensure that your previous fragment renders under the top fragment while it is swiped away.

### Horizontal scrollable views

In some cases, such as in a view containing a map that supports panning, the user interface can't prevent horizontal swiping. In this scenario, there are two choices:

- If the back stack is short, the user can dismiss the app and return to the watch face home screen by pressing the power button.
- If you want the user to go down the back stack, you can wrap the view in a`SwipeDismissFrameLayout`object, which supports edge swipe. Edge swipe is enabled when the view or its children returns`true`from a[`canScrollHorizontally()`](https://developer.android.com/reference/android/view/View#canScrollHorizontally(int))call. Edge swipe lets the user dismiss the view by swiping from the leftmost 10% of the screen, rather than anywhere in the view.

The following examples show how to wrap a view in a`SwipeDismissFrameLayout`object:  

```xml
<androidx.wear.widget.SwipeDismissFrameLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:id="@+id/swipe_dismiss_root" >

    <TextView
        android:id="@+id/test_content"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:gravity="center"
        android:text="Swipe me to dismiss me." />
</androidx.wear.widget.SwipeDismissFrameLayout>
```  

### Kotlin

```kotlin
activity?.findViewById<SwipeDismissFrameLayout>(R.id.swipe_dismiss_root)?.apply {
    addCallback(object : SwipeDismissFrameLayout.Callback() {

        override fun onDismissed(layout: SwipeDismissFrameLayout) {
            layout.visibility = View.GONE
        }
    })
}
```

### Java

```java
SwipeDismissFrameLayout testLayout =
    (SwipeDismissFrameLayout) activity.findViewById(R.id.swipe_dismiss_root);
testLayout.addCallback(new SwipeDismissFrameLayout.Callback() {
    @Override
    public void onDismissed(SwipeDismissFrameLayout layout) {
        layout.setVisibility(View.GONE);
    }
  }
);
```

### Not recommended: Disable swipe-to-dismiss

We don't generally recommend disabling swipe-to-dismiss, because the user expects to dismiss any screen with a swipe. In an exceptional case, you can extend the default theme in a[style resource](https://developer.android.com/guide/topics/resources/style-resource)and set the`android:windowSwipeToDismiss`attribute to`false`, as shown in the following code sample:  

```xml
<resources>
  <style name="AppTheme" parent="@android:style/Theme.DeviceDefault">
    <item name="android:windowSwipeToDismiss">false</item>
  </style>
</resources>
```

You can then inform users on their first use of your app that they can exit the app by pressing the power button.

## Dismissal with the power button

A press of the physical power button sends a power key event. Therefore, you can't use the power button as a back button or for navigation in general.

When pressed, the power button returns the user to the watch face home screen. There are two exceptions:

- If the user is in an Input Method Editor (IME), such as a handwriting recognition screen, pressing the button closes the IME and returns the user to the app.
- If the user is at the watch face, pressing the hardware button opens the app launcher.

<br />

**Note** that when the power button is pressed, the[isFinishing()](https://developer.android.com/reference/android/app/Activity#isFinishing())method of the`Activity`class does not return`true`, and you can't intercept the key event.  
For more information, see[Navigation](https://developer.android.com/training/wearables/design/navigation).