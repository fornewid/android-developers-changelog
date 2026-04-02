---
title: https://developer.android.com/develop/ui/views/touch-and-input/gestures
url: https://developer.android.com/develop/ui/views/touch-and-input/gestures
source: md.txt
---

# Use touch gestures

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to use touch and input in Compose.  
[Gestures →](https://developer.android.com/jetpack/compose/touch-input/pointer-input)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

This document describes how to write apps that let users interact with an app using touch gestures. Android provides a variety of APIs to help you create and detect gestures.

Although your app must not depend on touch gestures for basic behaviors---since the gestures might not be available to all users in all contexts---adding touch-based interaction to your app can greatly increase its usefulness and appeal.

To provide users with a consistent, intuitive experience, your app must follow the accepted Android conventions for touch gestures. The[Material Design Gestures](https://material.io/design/interaction/gestures.html)document shows you how to use common gestures in Android apps. Also, see[Material Motion](https://material.io/guidelines/motion/material-motion.html).

For more information about this topic, read the following related guides:

- [Input events overview](https://developer.android.com/guide/topics/ui/ui-events)
- [Sensors overview](https://developer.android.com/guide/topics/sensors/sensors_overview)
- [Make a custom view interactive](https://developer.android.com/training/custom-views/making-interactive)

## Topics

**[Detect common gestures](https://developer.android.com/develop/ui/views/touch-and-input/gestures/detector)**
:   Learn how to detect basic touch gestures, such as scrolling, flinging, and double-tapping, using[GestureDetector](https://developer.android.com/reference/android/view/GestureDetector).

**[Track touch and pointer movements](https://developer.android.com/develop/ui/views/touch-and-input/gestures/movement)**
:   Learn how to track movement.

**[Animate a scroll gesture](https://developer.android.com/develop/ui/views/touch-and-input/gestures/scroll)**
:   Learn how to use scrollers---[Scroller](https://developer.android.com/reference/android/widget/Scroller)or[OverScroller](https://developer.android.com/reference/android/widget/OverScroller)---to produce a scrolling animation in response to a touch event.

**[Handle multi-touch gestures](https://developer.android.com/develop/ui/views/touch-and-input/gestures/multi)**
:   Learn how to detect multi-pointer (finger) gestures.

**[Drag and scale](https://developer.android.com/develop/ui/views/touch-and-input/gestures/scale)**
:   Learn how to implement touch-based dragging and scaling.

**[Manage touch events in a ViewGroup](https://developer.android.com/develop/ui/views/touch-and-input/gestures/viewgroup)**
:   Learn how to manage touch events in a[ViewGroup](https://developer.android.com/reference/android/view/ViewGroup)to ensure that touch events are correctly dispatched to their target views.