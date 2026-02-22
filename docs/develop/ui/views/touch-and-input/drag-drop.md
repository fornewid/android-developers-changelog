---
title: https://developer.android.com/develop/ui/views/touch-and-input/drag-drop
url: https://developer.android.com/develop/ui/views/touch-and-input/drag-drop
source: md.txt
---

# Enable drag and drop

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to use drag and drop in Compose.  
[Drag and drop →](https://developer.android.com/develop/ui/compose/touch-input/user-interactions/drag-and-drop)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

<br />

| **Note:** See the improved method of implementing drag and drop in[Receive rich content](https://developer.android.com/develop/ui/views/receive-rich-content)for a better UX and improved maintainability of your code.

The Android drag-and-drop framework lets you add interactive drag-and-drop capabilities to your app. With drag and drop, users can copy or move text, images, objects, and any content that can be represented by a URI, from one[`View`](https://developer.android.com/reference/android/view/View)to another within an app, or between apps in[multi-window mode](https://developer.android.com/develop/ui/views/touch-and-input/drag-drop/multi-window#DragPermissionsMultiWindow).

|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![Text string and image being dragged and dropped within an app.](https://developer.android.com/static/images/guide/topics/ui/drag-and-drop-within-app.gif) | ![Text string and image being dragged and dropped between apps in split-screen mode.](https://developer.android.com/static/images/guide/topics/ui/drag-and-drop-between-apps.gif) |
| **Figure 1.**Drag and drop within an app.                                                                                                                   | **Figure 2.**Drag and drop between apps.                                                                                                                                          |

The framework includes a drag event class, drag listeners, and helper classes and methods. Although primarily designed to enable the transfer of data, you can use the framework for other UI actions. For example, you can create an app that mixes colors when the user drags a color icon over another icon. However, the rest of document describes the drag-and-drop framework in the context of data transfer.

## Overview

There are a few elements involved in the drag process.

1. Drag source: The start point view of drag-and-drop process.

2. Drop target: A view that can accept the drag data.

3. [Drag shadow](https://developer.android.com/develop/ui/views/touch-and-input/drag-drop/concepts#AboutDragShadowBuilder): A*drag shadow*is a representation of the data being dragged, it's visible to users.

4. [Drag events](https://developer.android.com/develop/ui/views/touch-and-input/drag-drop/concepts#AboutDragEvent): As the user moves the drag shadow over the app's layout, the system sends drag events to the drag event listeners and callback methods associated with the`View`objects in the layout.

A drag-and-drop operation starts when the user makes a UI gesture that your app recognizes as a signal to start dragging data. In response, the app notifies the system that a drag-and-drop operation is starting. The system calls back to your app to get a*drag shadow*. and show it to users during drag-and-drop process.

As the user moves the drag shadow over the app's layout, the system sends drag events to the[drag event listeners and callback methods](https://developer.android.com/develop/ui/views/touch-and-input/drag-drop/concepts#AboutDragListeners)associated with the`View`objects in the layout. If the user releases the drag shadow over a drop target, the system sends the data to it. The drag-and-drop operation ends when the user releases the drag shadow, whether or not the drag shadow is over a drop target.

## Topics

[Key Concepts](https://developer.android.com/develop/ui/views/touch-and-input/drag-drop/concepts)
:   Understand the drag-and-drop process.

[DropHelper for simplified drag and drop](https://developer.android.com/develop/ui/views/touch-and-input/drag-drop/drophelper)
:   Learn how to implement drag and drop with`DropHelper`.

[Implement drag and drop with views](https://developer.android.com/develop/ui/views/touch-and-input/drag-drop/view)
:   Alternatively, implement drag and drop with Android views, this allows developers to have more control of the details.

[Drag and drop in multi-window mode](https://developer.android.com/develop/ui/views/touch-and-input/drag-drop/multi-window)
:   Support drag and drop in multi-window mode, allow objects to move across different applications.

## Additional resources

- [Codelab for Drag and Drop](https://developer.android.com/codelabs/codelab-dnd-views)using views
- [Drag \& drop for seamless multitasking](https://www.youtube.com/watch?v=WOm76wSfkbU)video
- [Drag and Drop Samples](https://github.com/android/platform-samples/tree/main/samples/user-interface/draganddrop)which contains various ways to implement drag and drop along with accepting rich media.