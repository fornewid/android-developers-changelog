---
title: https://developer.android.com/training/tv/accessibility/custom-views
url: https://developer.android.com/training/tv/accessibility/custom-views
source: md.txt
---

# Custom view accessibility support on Android TV

While many Android TV apps are built with native Android components, it's also important to consider the accessibility of third-party frameworks or components, especially when using[custom views](https://developer.android.com/guide/topics/ui/custom-components).

Custom view components interfacing directly with OpenGL or Canvas might not work well with accessibility services like Talkback and Switch Access.

Consider some of the following issues that might occur with Talkback switched on:

- The accessibility focus (a green rectangle) might disappear in your app.
- The accessibility focus might select the boundary of the whole screen.
- The accessibility focus might not be movable.
- The four direction keys on the D-pad might have no effect, even if your code is handling them.

<br />

If you observe any of these issues in your app, check that your app exposes its[`AccessibilityNodeInfo`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo)tree to the accessibility services.

The remainder of this guide provides some solutions and best practices to address these issues.

## D-pad events are consumed by accessibility services

The root cause of this issue is that key events are consumed by accessibility services.

![Dpad events consumption](https://developer.android.com/training/tv/images/DPAD-event-consumption.png)**Figure 1.**Diagrams depicting how the system functions with Talkback on and off.

As illustrated in figure 1, when Talkback is switched on, D-pad events are not passed to the D-pad handler defined by developer. Instead, accessibility services receive the key events so they can move the accessibility focus. Because custom Android components don't by default expose information to accessibility services about their position on the screen, accessibility services can't move the accessibility focus to highlight them.

Other accessibility services are similarly affected: D-pad events might also be consumed when using Switch Access.

Because D-pad events are submitted to accessibility services, and that service doesn't know where UI components are in a custom view, you must implement`AccessibilityNodeInfo`for your app to forward the key events correctly.

## Expose information to accessibility services

To provide accessibility services with sufficient information about the location and description of custom views, implement[`AccessibilityNodeInfo`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo)to expose details for each component. To define the logical relationship of views so that accessibility services can manage focus, implement[`ExploreByTouchHelper`](https://developer.android.com/reference/androidx/customview/widget/ExploreByTouchHelper)and set it using[`ViewCompat.setAccessibilityDelegate(View, AccessibilityDelegateCompat)`](https://developer.android.com/reference/androidx/core/view/ViewCompat#setAccessibilityDelegate(android.view.View,%20androidx.core.view.AccessibilityDelegateCompat))for custom views.

When implementing`ExploreByTouchHelper`, override its four abstract methods:  

### Kotlin

```kotlin
// Return the virtual view ID whose view is covered by the input point (x, y).
protected fun getVirtualViewAt(x: Float, y: Float): Int

// Fill the virtual view ID list into the input parameter virtualViewIds.
protected fun getVisibleVirtualViews(virtualViewIds: List<Int>)

// For the view whose virtualViewId is the input virtualViewId, populate the
// accessibility node information into the AccessibilityNodeInfoCompat parameter.
protected fun onPopulateNodeForVirtualView(virtualViewId: Int, @NonNull node: AccessibilityNodeInfoCompat)

// Set the accessibility handling when perform action.
protected fun onPerformActionForVirtualView(virtualViewId: Int, action: Int, @Nullable arguments: Bundle): Boolean
```

### Java

```java
// Return the virtual view ID whose view is covered by the input point (x, y).
protected int getVirtualViewAt(float x, float y)

// Fill the virtual view ID list into the input parameter virtualViewIds.
protected void getVisibleVirtualViews(List<Integer> virtualViewIds)

// For the view whose virtualViewId is the input virtualViewId, populate the
// accessibility node information into the AccessibilityNodeInfoCompat parameter.
protected void onPopulateNodeForVirtualView(int virtualViewId, @NonNull AccessibilityNodeInfoCompat node)

// Set the accessibility handling when perform action.
protected boolean onPerformActionForVirtualView(int virtualViewId, int action, @Nullable Bundle arguments)
```

For more details, watch[Google I/O 2013 - Enabling Blind and Low-Vision Accessibility on Android](https://www.youtube.com/watch?v=ld7kZRpMGb8&t=1196)or read more about[populating accessibility events](https://developer.android.com/guide/topics/ui/accessibility/custom-views#populate-events).

## Best practices

- **Required:** [`AccessibilityNodeInfo.getBoundsInScreen()`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo#getBoundsInScreen(android.graphics.Rect))must define the position of the component.

- **Required:** [`AccessibilityNodeInfo.setVisibleToUser()`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo#setVisibleToUser(boolean))must reflect the visibility of the component.

- **Required:** [`AccessibilityNodeInfo.getContentDescription()`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo#getContentDescription())must specify the content description for Talkback to announce.

- Specify[`AccessibilityNodeInfo.setClassName()`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo#setClassName(java.lang.CharSequence))so services can distinguish the component type.

- When implementing[`performAction()`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo#performAction(int)), reflect the action using a corresponding[`AccessibilityEvent`](https://developer.android.com/reference/android/view/accessibility/AccessibilityEvent).

- To implement more action types, such as`ACTION_CLICK`, invoke[`AccessibilityNodeInfo.addAction(ACTION_CLICK)`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo#addAction(android.view.accessibility.AccessibilityNodeInfo.AccessibilityAction))using the corresponding logic in`performAction()`.

- When applicable, reflect the component state for[`setFocusable()`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo#setFocusable(boolean)),[`setClickable()`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo#setClickable(boolean)),[`setScrollable()`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo#setScrollable(boolean)), and similar methods.

- Review the documentation for[`AccessibilityNodeInfo`](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo)to identify other ways in which accessibility services can better interact with your components.

## Sample

Consult the[custom view accessibility sample for Android TV](https://developer.android.com/training/tv/accessibility/custom-views-sample)to see best practices for adding accessibility support to apps using custom views.