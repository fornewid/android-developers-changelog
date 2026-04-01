---
title: Use touch gestures  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/touch-and-input/gestures
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Use touch gestures Stay organized with collections Save and categorize content based on your preferences.




Try the Compose way

Jetpack Compose is the recommended UI toolkit for Android. Learn how to use touch and input in Compose.

[Gestures →](https://developer.android.com/jetpack/compose/touch-input/pointer-input)

![](/static/images/android-compose-ui-logo.png)

This document describes how to write apps that let users interact with an app using touch
gestures. Android provides a variety of APIs to help you create and detect gestures.

Although your app must not depend on touch gestures for basic behaviors—since the gestures
might not be available to all users in all contexts—adding touch-based interaction to your app
can greatly increase its usefulness and appeal.

To provide users with a consistent, intuitive experience, your app must follow the accepted
Android conventions for touch gestures. The
[Material Design Gestures](https://material.io/design/interaction/gestures.html)
document shows you how to use common gestures in Android apps. Also, see
[Material Motion](https://material.io/guidelines/motion/material-motion.html).

For more information about this topic, read the following related guides:

* [Input events overview](/guide/topics/ui/ui-events)
* [Sensors overview](/guide/topics/sensors/sensors_overview)
* [Make a custom view
  interactive](/training/custom-views/making-interactive)

## Topics

**[Detect common gestures](/develop/ui/views/touch-and-input/gestures/detector)**
:   Learn how to detect basic touch gestures, such as scrolling, flinging, and double-tapping,
    using
    `GestureDetector`.

**[Track touch and pointer movements](/develop/ui/views/touch-and-input/gestures/movement)**
:   Learn how to track movement.

**[Animate a scroll gesture](/develop/ui/views/touch-and-input/gestures/scroll)**
:   Learn how to use
    scrollers—`Scroller`
    or
    `OverScroller`—to
    produce a scrolling animation in response to a touch event.

**[Handle multi-touch gestures](/develop/ui/views/touch-and-input/gestures/multi)**
:   Learn how to detect multi-pointer (finger) gestures.

**[Drag and scale](/develop/ui/views/touch-and-input/gestures/scale)**
:   Learn how to implement touch-based dragging and scaling.

**[Manage touch events in a ViewGroup](/develop/ui/views/touch-and-input/gestures/viewgroup)**
:   Learn how to manage touch events in a
    `ViewGroup` to ensure that
    touch events are correctly dispatched to their target views.