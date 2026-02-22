---
title: https://developer.android.com/develop/ui/views/layout/custom-views/optimizing-view
url: https://developer.android.com/develop/ui/views/layout/custom-views/optimizing-view
source: md.txt
---

# Optimize a custom view

When you have a well-designed view that responds to gestures and transitions between states, make sure the view runs fast. To avoid a UI that feels sluggish or stutters during playback, make sure animations consistently run at 60 frames per second.

## Speed up your view

To speed up your view, eliminate unnecessary code from routines that are called frequently. Start with[onDraw()](https://developer.android.com/reference/android/view/View#onDraw(android.graphics.Canvas)), which gives you the biggest payback. In particular, eliminate allocations in`onDraw()`, because allocations might lead to a garbage collection that causes a stutter. Allocate objects during initialization or between animations. Never make an allocation while an animation is running.

In addition to making`onDraw()`leaner, make sure it's called as infrequently as possible. Most calls to`onDraw()`are the result of a call to[invalidate()](https://developer.android.com/reference/android/view/View#invalidate()), so eliminate unnecessary calls to`invalidate()`.

Another very expensive operation is traversing layouts. When a view calls[requestLayout()](https://developer.android.com/reference/android/view/View#requestLayout()), the Android UI system traverses the entire view hierarchy to find how big each view needs to be. If it finds conflicting measurements, it might traverse the hierarchy multiple times. UI designers sometimes create deep hierarchies of nested[ViewGroup](https://developer.android.com/reference/android/view/ViewGroup)objects. These deep view hierarchies cause performance problems, so make your view hierarchies as shallow as possible.

If you have a complex UI, consider writing a custom`ViewGroup`to perform its layout. Unlike the built-in views, your custom view can make application-specific assumptions about the size and shape of its children and therefore avoid traversing its children to calculate measurements.

For example, if you have a custom`ViwGroup`that doesn't adjust its own size to fit all its child views, you avoid the overhead of measuring all the child views. This optimization isn't possible if you use the built-in layouts that cater to a wide range of use-cases.