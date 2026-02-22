---
title: https://developer.android.com/develop/ui/views/touch-and-input/drag-drop/concepts
url: https://developer.android.com/develop/ui/views/touch-and-input/drag-drop/concepts
source: md.txt
---

# Key concepts

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to use drag and drop in Compose.  
[Drag and drop →](https://developer.android.com/develop/ui/compose/touch-input/user-interactions/drag-and-drop)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

<br />

The following sections explains a few key concepts for drag-and-drop process.

## Drag-and-drop process

There are four steps or states in the drag-and-drop process: started, continuing, dropped, and ended.

Started

:   In response to a user's drag gesture, your application calls`startDragAndDrop()`to tell the system to start a drag-and-drop operation. The method's arguments provide the following:

    - The data to be dragged.
    - A callback for drawing the drag shadow
    - Metadata that describes the dragged data
    - The system responds by calling back to your application to get a drag shadow. The system then displays the drag shadow on the device.
    - Next, the system sends a drag event with action type[`ACTION_DRAG_STARTED`](https://developer.android.com/reference/android/view/DragEvent#ACTION_DRAG_STARTED)to the drag event listener of all`View`objects in the current layout. To continue to receive drag events---including a possible drop event---the drag event listener must return`true`. This registers the listener with the system. Only registered listeners continue to receive drag events. At this point, listeners can also change the appearance of their drop target`View`object to show that the view can accept a drop event.
    - If the drag event listener returns`false`, it doesn't receive drag events for the current operation until the system sends a drag event with action type[`ACTION_DRAG_ENDED`](https://developer.android.com/reference/android/view/DragEvent#ACTION_DRAG_ENDED). By returning`false`, the listener tells the system that it isn't interested in the drag-and-drop operation and doesn't want to accept the dragged data.
| **Note:** A return value of`false`from a[`View.OnDragListener`](https://developer.android.com/reference/android/view/View.OnDragListener)triggers the view's`onDragEvent()`handler.

Continuing
:   The user continues the drag. As the drag shadow intersects the bounding box of a drop target, the system sends one or more drag events to the target's drag event listener. The listener might alter the appearance of the drop target`View`in response to the event. For example, if the event indicates that the drag shadow enters the bounding box of the drop target---action type[`ACTION_DRAG_ENTERED`](https://developer.android.com/reference/android/view/DragEvent#ACTION_DRAG_ENTERED)---the listener can react by highlighting the`View`.

Dropped
:   The user releases the drag shadow within the bounding box of a drop target. The system sends the drop target's listener a drag event with action type[`ACTION_DROP`](https://developer.android.com/reference/android/view/DragEvent#ACTION_DROP). The drag event object contains the data that passes to the system in the call to`startDragAndDrop()`that starts the operation. The listener is expected to return boolean`true`to the system if the listener successfully processes the dropped data. : This step only occurs if the user drops the drag shadow within the bounding box of a`View`whose listener is registered to receive drag events (a drop target). If the user releases the drag shadow in any other situation, no`ACTION_DROP`drag event is sent.

Ended

:   After the user releases the drag shadow, and after the system sends

    out a drag event with action type`ACTION_DROP`, if necessary, the system sends a drag event with action type`ACTION_DRAG_ENDED`to indicate that the drag-and-drop operation is over. This is done regardless of where the user releases the drag shadow. The event is sent to every listener that is registered to receive drag events, even if the listener also receives the`ACTION_DROP`event.

Each of these steps is described in more detail in the section called[A drag-and-drop operation](https://developer.android.com/develop/ui/views/touch-and-input/drag-drop/view#DesignDragOperation).
| **Note:** If apps are running in multi-window mode, users can drag data from one app to another. For more information, see[Drag and drop](https://developer.android.com/develop/ui/views/layout/support-multi-window-mode#dnd)in[Support multi-window mode](https://developer.android.com/develop/ui/views/layout/support-multi-window-mode).

## Drag events

The system sends out a drag event in the form of a`DragEvent`object, which contains an action type that describes what is happening in the drag-and-drop process. Depending on the action type, the object can also contain other data.

Drag event listeners receive the`DragEvent`object. To get the action type, listeners call[`DragEvent.getAction()`](https://developer.android.com/reference/android/view/DragEvent#getAction()). There are six possible values defined by constants in the`DragEvent`class, which are described in table 1:

**Table 1.**DragEvent action types

|                                                  Action type                                                   |                                                                                                                                                                                                                                                                                                       Meaning                                                                                                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ACTION_DRAG_STARTED](https://developer.android.com/reference/android/view/DragEvent#ACTION_DRAG_STARTED)      | The application calls`startDragAndDrop()`and obtains a drag shadow. If the listener wants to continue receiving drag events for this operation, it must return boolean`true`to the system.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ` `[ACTION_DRAG_ENTERED](https://developer.android.com/reference/android/view/DragEvent#ACTION_DRAG_ENTERED)   | The drag shadow enters the bounding box of the drag event listener's`View`. This is the first event action type the listener receives when the drag shadow enters the bounding box.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ` `[ACTION_DRAG_LOCATION](https://developer.android.com/reference/android/view/DragEvent#ACTION_DRAG_LOCATION) | Subsequent to an`ACTION_DRAG_ENTERED`event, the drag shadow is still within the bounding box of the drag event listener's`View`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ` `[ACTION_DRAG_EXITED](https://developer.android.com/reference/android/view/DragEvent#ACTION_DRAG_EXITED)     | Following an`ACTION_DRAG_ENTERED`and at least one`ACTION_DRAG_LOCATION`event, the drag shadow moves outside the bounding box of the drag event listener's`View`.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ` `[ACTION_DROP](https://developer.android.com/reference/android/view/DragEvent#ACTION_DROP)                   | The drag shadow releases over the drag event listener's`View`. This action type is sent to a`View`object's listener only if the listener returns boolean`true`in response to the`ACTION_DRAG_STARTED`drag event. This action type isn't sent if the user releases the drag shadow over a`View`whose listener isn't registered or if the user releases the drag shadow over anything that isn't part of the current layout. The listener returns boolean`true`if it successfully processes the drop. Otherwise, it must return`false`.                                                                               |
| ` `[ACTION_DRAG_ENDED](https://developer.android.com/reference/android/view/DragEvent#ACTION_DRAG_ENDED)       | The system is ending the drag-and-drop operation. This action type isn't necessarily preceded by an`ACTION_DROP`event. If the system sends an`ACTION_DROP`, receiving the`ACTION_DRAG_ENDED`action type doesn't imply that the drop succeeded. The listener must call[getResult()](https://developer.android.com/reference/android/view/DragEvent#getResult()), as shown in[table 2](https://developer.android.com/develop/ui/views/touch-and-input/drag-drop/concepts#table2), to get the value that is returned in response to`ACTION_DROP`. If an`ACTION_DROP`event isn't sent, then`getResult()`returns`false`. |

The`DragEvent`object also contains the data and metadata that your application provides to the system in the call to`startDragAndDrop()`. Some of the data is valid only for certain action types as summarized in table 2. For more information about events and their associated data, see the section called[A drag-and-drop operation](https://developer.android.com/develop/ui/views/touch-and-input/drag-drop/view#DesignDragOperation).

**Table 2.**Valid DragEvent data by action type

|       [getAction()](https://developer.android.com/reference/android/view/DragEvent#getAction()) value       | [getClipDescription()](https://developer.android.com/reference/android/view/DragEvent#getClipDescription()) value | [getLocalState()](https://developer.android.com/reference/android/view/DragEvent#getLocalState()) value | [getX()](https://developer.android.com/reference/android/view/DragEvent#getX()) value | [getY()](https://developer.android.com/reference/android/view/DragEvent#getY()) value | [getClipData()](https://developer.android.com/reference/android/view/DragEvent#getClipData()) value | [getResult()](https://developer.android.com/reference/android/view/DragEvent#getResult()) value |
|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [ACTION_DRAG_STARTED](https://developer.android.com/reference/android/view/DragEvent#ACTION_DRAG_STARTED)   | ✓                                                                                                                 | ✓                                                                                                       |                                                                                       |                                                                                       |                                                                                                     |                                                                                                 |
| [ACTION_DRAG_ENTERED](https://developer.android.com/reference/android/view/DragEvent#ACTION_DRAG_ENTERED)   | ✓                                                                                                                 | ✓                                                                                                       |                                                                                       |                                                                                       |                                                                                                     |                                                                                                 |
| [ACTION_DRAG_LOCATION](https://developer.android.com/reference/android/view/DragEvent#ACTION_DRAG_LOCATION) | ✓                                                                                                                 | ✓                                                                                                       | ✓                                                                                     | ✓                                                                                     |                                                                                                     |                                                                                                 |
| [ACTION_DRAG_EXITED](https://developer.android.com/reference/android/view/DragEvent#ACTION_DRAG_EXITED)     | ✓                                                                                                                 | ✓                                                                                                       |                                                                                       |                                                                                       |                                                                                                     |                                                                                                 |
| [ACTION_DROP](https://developer.android.com/reference/android/view/DragEvent#ACTION_DROP)                   | ✓                                                                                                                 | ✓                                                                                                       | ✓                                                                                     | ✓                                                                                     | ✓                                                                                                   |                                                                                                 |
| [ACTION_DRAG_ENDED](https://developer.android.com/reference/android/view/DragEvent#ACTION_DRAG_ENDED)       |                                                                                                                   | ✓                                                                                                       |                                                                                       |                                                                                       |                                                                                                     | ✓                                                                                               |

The`DragEvent`methods`getAction()`,[`describeContents()`](https://developer.android.com/reference/android/view/DragEvent#describeContents()),[`writeToParcel()`](https://developer.android.com/reference/android/view/DragEvent#writeToParcel(android.os.Parcel,%20int)), and[`toString()`](https://developer.android.com/reference/android/view/DragEvent#toString())always return valid data.

If a method doesn't contain valid data for a particular action type, it returns`null`or 0, depending on its result type.

## Drag shadow

During a drag-and-drop operation, the system displays an image that the user drags. For data movement, this image represents the data being dragged. For other operations, the image represents some aspect of the drag operation.

The image is called a*drag shadow* . You create it with methods you declare for a[`View.DragShadowBuilder`](https://developer.android.com/reference/android/view/View.DragShadowBuilder)object. You pass the builder to the system when you start a drag-and-drop operation using`startDragAndDrop()`. As part of its response to`startDragAndDrop()`, the system invokes the callback methods you define in`View.DragShadowBuilder`to obtain a drag shadow.

The`View.DragShadowBuilder`class has two constructors:

[`View.DragShadowBuilder(View)`](https://developer.android.com/reference/android/view/View.DragShadowBuilder#DragShadowBuilder(android.view.View))

:   This constructor accepts any of your application's[`View`](https://developer.android.com/reference/android/view/View)objects. The constructor stores the`View`object in the`View.DragShadowBuilder`object, so the callbacks can access it to construct the drag shadow. The view doesn't have to be a`View`that the user selects to start the drag operation.

    If you use this constructor, you don't have to extend`View.DragShadowBuilder`or override its methods. By default, you get a drag shadow that has the same appearance as the`View`you pass as an argument, centered under the location where the user touches the screen.

[`View.DragShadowBuilder()`](https://developer.android.com/reference/android/view/View.DragShadowBuilder#DragShadowBuilder())

:   If you use this constructor, no`View`object is available in the`View.DragShadowBuilder`object. The field is set to`null`. You must extend`View.DragShadowBuilder`and override its methods, or else you get an invisible drag shadow. The system doesn't throw an error.

The`View.DragShadowBuilder`class has two methods that together create the drag shadow:

[`onProvideShadowMetrics()`](https://developer.android.com/reference/android/view/View.DragShadowBuilder#onProvideShadowMetrics(android.graphics.Point,%20android.graphics.Point))

:   The system calls this method immediately after you call`startDragAndDrop()`. Use the method to send the dimensions and touch point of the drag shadow to the system. The method has two parameters:

    **`outShadowSize`:** a[`Point`](https://developer.android.com/reference/android/graphics/Point)object. The drag shadow width goes in[`x`](https://developer.android.com/reference/android/graphics/Point#x), and its height goes in[`y`](https://developer.android.com/reference/android/graphics/Point#y).

    **`outShadowTouchPoint`:** a`Point`object. The touch point is the location within the drag shadow that must be under the user's finger during the drag. Its*X* position goes in`x`and its*Y* position goes in`y`.

[`onDrawShadow()`](https://developer.android.com/reference/android/view/View.DragShadowBuilder#onDrawShadow(android.graphics.Canvas))

:   Immediately after the call to`onProvideShadowMetrics()`the system calls`onDrawShadow()`to create the drag shadow. The method has a single argument, a[`Canvas`](https://developer.android.com/reference/android/graphics/Canvas)object that the system constructs from the parameters you provide in`onProvideShadowMetrics()`. The method draws the drag shadow on the provided`Canvas`.

To improve performance, keep the size of the drag shadow small. For a single item, you might want to use an icon. For a multiple-item selection, you might want to use icons in a stack rather than full images spread out over the screen.

## Drag event listeners and callback methods

A`View`receives drag events with a drag event listener that implements`View.OnDragListener`or with the view's`onDragEvent()`callback method. When the system calls the method or listener, it provides a[`DragEvent`](https://developer.android.com/reference/android/view/DragEvent)argument.

In most cases, using a listener is preferable to using the callback method. When you design UIs, you usually don't subclass`View`classes, but using the callback method forces you to create subclasses to override the method. In comparison, you can implement one listener class and then use it with multiple different`View`objects. You can also implement it as an anonymous inline class or lambda expression. To set the listener for a`View`object, call`setOnDragListener()`.

As an alternative, you can alter the default implementation of`onDragEvent()`without overriding the method. Set an[`OnReceiveContentListener`](https://developer.android.com/reference/android/view/OnReceiveContentListener)on a view; for more details, see[`setOnReceiveContentListener()`](https://developer.android.com/reference/android/view/View#setOnReceiveContentListener(java.lang.String%5B%5D,%20android.view.OnReceiveContentListener)). The`onDragEvent()`method then does the following by default:

- Returns true in response to the call to`startDragAndDrop()`.
- Calls[`performReceiveContent()`](https://developer.android.com/reference/android/view/View#performReceiveContent(android.view.ContentInfo))if the drag-and-drop data is dropped on the view. The data is passed to the method as a[`ContentInfo`](https://developer.android.com/reference/android/view/ContentInfo)object. The method invokes the`OnReceiveContentListener`.

- Returns true if the drag-and-drop data is dropped on the view and the`OnReceiveContentListener`consumes any of the content.

Define the`OnReceiveContentListener`to handle the data specifically for your app. For backward compatibility down to API level 24, use the Jetpack version of[`OnReceiveContentListener`](https://developer.android.com/reference/androidx/core/view/OnReceiveContentListener).

You can have a drag event listener and a callback method for a`View`object, in which case the system first calls the listener. The system doesn't call the callback method unless the listener returns`false`.

The combination of the`onDragEvent()`method and`View.OnDragListener`is analogous to the combination of the[`onTouchEvent()`](https://developer.android.com/reference/android/view/View#onTouchEvent(android.view.MotionEvent))and[`View.OnTouchListener`](https://developer.android.com/reference/android/view/View.OnTouchListener)used with touch events.
| **Key Term:** The following sections refer to the method that receives drag events as the drag event*listener* . However, the method can be an`onDragEvent()`callback, a`View.OnDragListener`method, or both.