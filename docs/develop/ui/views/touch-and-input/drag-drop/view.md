---
title: https://developer.android.com/develop/ui/views/touch-and-input/drag-drop/view
url: https://developer.android.com/develop/ui/views/touch-and-input/drag-drop/view
source: md.txt
---

You can implement your drag-and-drop process in views by responding to events
that might trigger a drag start and responding and consuming drop events.

## Start a drag

The user starts a drag with a gesture, usually by touching or clicking and
holding on an item they want to drag.

To handle this in a `View`, create a
[`ClipData`](https://developer.android.com/reference/android/content/ClipData) object and
[`ClipData.Item`](https://developer.android.com/reference/android/content/ClipData.Item) object for
the data being moved. As part of the `ClipData`, supply metadata that is
stored in a
[`ClipDescription`](https://developer.android.com/reference/android/content/ClipDescription) object
within the `ClipData`. For a drag-and-drop operation that doesn't represent
data movement, you might want to use `null` instead of an actual object.

For example, this code snippet shows how to respond to a touch \& hold
gesture on an `ImageView` by creating a `ClipData` object that contains the
tag (or label) of an `ImageView`:

### Kotlin

```kotlin
// Create a string for the ImageView label.
val IMAGEVIEW_TAG = "icon bitmap"
...
val imageView = ImageView(context).apply {
    // Set the bitmap for the ImageView from an icon bitmap defined elsewhere.
    setImageBitmap(iconBitmap)
    tag = IMAGEVIEW_TAG
    setOnLongClickListener { v ->
        // Create a new ClipData. This is done in two steps to provide
        // clarity. The convenience method ClipData.newPlainText() can
        // create a plain text ClipData in one step.

        // Create a new ClipData.Item from the ImageView object's tag.
        val item = ClipData.Item(v.tag as? CharSequence)

        // Create a new ClipData using the tag as a label, the plain text
        // MIME type, and the already-created item. This creates a new
        // ClipDescription object within the ClipData and sets its MIME type
        // to "text/plain".
        val dragData = ClipData(
            v.tag as? CharSequence,
            arrayOf(ClipDescription.MIMETYPE_TEXT_PLAIN),
            item)

        // Instantiate the drag shadow builder. We use this imageView object
        // to create the default builder.
        val myShadow = View.DragShadowBuilder(view: this)

        // Start the drag.
        v.startDragAndDrop(dragData,  // The data to be dragged.
                            myShadow,  // The drag shadow builder.
                            null,      // No need to use local data.
                            0          // Flags. Not currently used, set to 0.
        )

        // Indicate that the long-click is handled.
        true
    }
}
```

### Java

```java
// Create a string for the ImageView label.
private static final String IMAGEVIEW_TAG = "icon bitmap";
...
// Create a new ImageView.
ImageView imageView = new ImageView(context);

// Set the bitmap for the ImageView from an icon bitmap defined elsewhere.
imageView.setImageBitmap(iconBitmap);

// Set the tag.
imageView.setTag(IMAGEVIEW_TAG);

// Set a long-click listener for the ImageView using an anonymous listener
// object that implements the OnLongClickListener interface.
imageView.setOnLongClickListener( v -> {

    // Create a new ClipData. This is done in two steps to provide clarity. The
    // convenience method ClipData.newPlainText() can create a plain text
    // ClipData in one step.

    // Create a new ClipData.Item from the ImageView object's tag.
    ClipData.Item item = new ClipData.Item((CharSequence) v.getTag());

    // Create a new ClipData using the tag as a label, the plain text MIME type,
    // and the already-created item. This creates a new ClipDescription object
    // within the ClipData and sets its MIME type to "text/plain".
    ClipData dragData = new ClipData(
            (CharSequence) v.getTag(),
            new String[] { ClipDescription.MIMETYPE_TEXT_PLAIN },
            item);

    // Instantiate the drag shadow builder. We use this imageView object
    // to create the default builder.
    View.DragShadowBuilder myShadow = new View.DragShadowBuilder(imageView);

    // Start the drag.
    v.startDragAndDrop(dragData,  // The data to be dragged.
                            myShadow,  // The drag shadow builder.
                            null,      // No need to use local data.
                            0          // Flags. Not currently used, set to 0.
    );

    // Indicate that the long-click is handled.
    return true;
});
```

## Respond to a drag start

During the drag operation, the system dispatches drag events to the drag event
listeners of the `View` objects in the current layout. The listeners react by
calling `DragEvent.getAction()` to get the action type. At the start of a drag,
this method returns `ACTION_DRAG_STARTED`.

In response to an event with the action type `ACTION_DRAG_STARTED`, a drag event
listener must do the following:

1. Call
   [`DragEvent.getClipDescription()`](https://developer.android.com/reference/android/view/DragEvent#getClipDescription())
   and use the MIME type methods in the returned `ClipDescription` to see
   whether the listener can accept the data being dragged.

   If the drag-and-drop operation doesn't represent data movement, this might
   be unnecessary.
2. If the drag event listener can accept a drop, it must return `true` to tell
   the system to continue to send drag events to the listener. If the listener
   can't accept a drop, the listener must return `false`, and the system stops
   sending drag events to the listener until the system sends
   `ACTION_DRAG_ENDED` to conclude the drag-and-drop operation.

For an `ACTION_DRAG_STARTED` event, the following `DragEvent` methods aren't
valid: [`getClipData()`](https://developer.android.com/reference/android/view/DragEvent#getClipData()),
[`getX()`](https://developer.android.com/reference/android/view/DragEvent#getX()),
[`getY()`](https://developer.android.com/reference/android/view/DragEvent#getY()), and
[`getResult()`](https://developer.android.com/reference/android/view/DragEvent#getResult()).

## Handle events during the drag

During the drag action, drag event listeners that return `true` in response to
the `ACTION_DRAG_STARTED` drag event continue to receive drag events. The types
of drag events a listener receives during the drag depend on the location of the
drag shadow and the visibility of the listener's `View`. Listeners use the drag
events primarily to decide if they must change the appearance of their `View`.

During the drag action, `DragEvent.getAction()` returns one of three values:

- [`ACTION_DRAG_ENTERED`](https://developer.android.com/reference/android/view/DragEvent#ACTION_DRAG_ENTERED): the listener receives this event action type when the touch point---the point on the screen underneath the user's finger or mouse---enters the bounding box of the listener's `View`.
- [`ACTION_DRAG_LOCATION`](https://developer.android.com/reference/android/view/DragEvent#ACTION_DRAG_LOCATION): once the listener receives an `ACTION_DRAG_ENTERED` event, it receives a new `ACTION_DRAG_LOCATION` event every time the touch point moves until it receives an `ACTION_DRAG_EXITED` event. The `getX()` and `getY()` methods return the X and Y coordinates of the touch point.
- [`ACTION_DRAG_EXITED`](https://developer.android.com/reference/android/view/DragEvent#ACTION_DRAG_EXITED): this event action type is sent to a listener that previously receives `ACTION_DRAG_ENTERED`. The event is sent when the drag shadow touch point moves from within the bounding box of the listener's `View` to outside the bounding box.

The drag event listener doesn't need to react to any of these action types. If
the listener returns a value to the system, it is ignored.

Here are some guidelines for responding to each of these action types:

- In response to `ACTION_DRAG_ENTERED` or `ACTION_DRAG_LOCATION`, the listener can change the appearance of the `View` to indicate that the view is a potential drop target.
- An event with the action type `ACTION_DRAG_LOCATION` contains valid data for `getX()` and `getY()` corresponding to the location of the touch point. The listener can use this information to alter the `View` appearance at the touch point or to determine the exact position where the user can drop the content.
- In response to `ACTION_DRAG_EXITED`, the listener must reset any appearance changes it applies in response to `ACTION_DRAG_ENTERED` or `ACTION_DRAG_LOCATION`. This indicates to the user that the `View` is no longer an imminent drop target.

## Respond to a drop

When the user releases the drag shadow over a `View`, and the `View` previously
reports that it can accept the content being dragged, the system dispatches a
drag event to the `View` with the action type `ACTION_DROP`.

The drag event listener must do the following:

1. Call `getClipData()` to get the `ClipData` object that is originally
   supplied in the call to
   [`startDragAndDrop()`](https://developer.android.com/reference/android/view/View#startDragAndDrop(android.content.ClipData,%20android.view.View.DragShadowBuilder,%20java.lang.Object,%20int))
   and process the data. If the drag-and-drop operation doesn't represent data
   movement, this is unnecessary.

2. Return boolean `true` to indicate that the drop is processed successfully,
   or `false` if it isn't. The returned value becomes the value returned by
   `getResult()` for the eventual `ACTION_DRAG_ENDED` event. If the system
   doesn't send out an `ACTION_DROP` event, the value returned by `getResult()`
   for an `ACTION_DRAG_ENDED` event is `false`.

For an `ACTION_DROP` event, `getX()` and `getY()` use the coordinate system of
the `View` that receives the drop to return the *X* and *Y* position of the
touch point at the moment of the drop.

While the user is able to release the drag shadow over a `View` whose drag event
listener isn't receiving drag events, empty regions of your app's UI or even
over areas outside of your application, Android won't send an event with action
type `ACTION_DROP` and will only send an `ACTION_DRAG_ENDED` event.

## Respond to a drag end

Immediately after the user releases the drag shadow, the system sends a drag
event with an action type of `ACTION_DRAG_ENDED` to all the drag event listeners
in your application. This indicates that the drag operation is finished.

Each drag event listener must do the following:

1. If the listener changes its appearance during the operation, it should reset back to its default appearance as a visual indication to the user that the operation is finished.
2. The listener can optionally call `getResult()` to find out more about the operation. If a listener returns `true` in response to an event of action type `ACTION_DROP`, then `getResult()` returns boolean `true`. In all other cases, `getResult()` returns boolean `false`, including when the system doesn't send an `ACTION_DROP` event.
3. To indicate the successful completion of the drop operation, the listener should return boolean `true` to the system. By not returning `false`, a visual cue showing the drop shadow returning to its source may suggest to the user that the operation was unsuccessful.

## Respond to drag events: An example

All drag events are received by your drag event method or listener. The
following code snippet is an example of responding to drag events:

### Kotlin

```kotlin
val imageView = ImageView(this)

// Set the drag event listener for the View.
imageView.setOnDragListener { v, e ->

    // Handle each of the expected events.
    when (e.action) {
        DragEvent.ACTION_DRAG_STARTED -> {
            // Determine whether this View can accept the dragged data.
            if (e.clipDescription.hasMimeType(ClipDescription.MIMETYPE_TEXT_PLAIN)) {
                // As an example, apply a blue color tint to the View to
                // indicate that it can accept data.
                (v as? ImageView)?.setColorFilter(Color.BLUE)

                // Invalidate the view to force a redraw in the new tint.
                v.invalidate()

                // Return true to indicate that the View can accept the dragged
                // data.
                true
            } else {
                // Return false to indicate that, during the current drag and
                // drop operation, this View doesn't receive events again until
                // ACTION_DRAG_ENDED is sent.
                false
            }
        }
        DragEvent.ACTION_DRAG_ENTERED -> {
            // Apply a green tint to the View.
            (v as? ImageView)?.setColorFilter(Color.GREEN)

            // Invalidate the view to force a redraw in the new tint.
            v.invalidate()

            // Return true. The value is ignored.
            true
        }

        DragEvent.ACTION_DRAG_LOCATION ->
            // Ignore the event.
            true
        DragEvent.ACTION_DRAG_EXITED -> {
            // Reset the color tint to blue.
            (v as? ImageView)?.setColorFilter(Color.BLUE)

            // Invalidate the view to force a redraw in the new tint.
            v.invalidate()

            // Return true. The value is ignored.
            true
        }
        DragEvent.ACTION_DROP -> {
            // Get the item containing the dragged data.
            val item: ClipData.Item = e.clipData.getItemAt(0)

            // Get the text data from the item.
            val dragData = item.text

            // Display a message containing the dragged data.
            Toast.makeText(this, "Dragged data is $dragData", Toast.LENGTH_LONG).show()

            // Turn off color tints.
            (v as? ImageView)?.clearColorFilter()

            // Invalidate the view to force a redraw.
            v.invalidate()

            // Return true. DragEvent.getResult() returns true.
            true
        }

        DragEvent.ACTION_DRAG_ENDED -> {
            // Turn off color tinting.
            (v as? ImageView)?.clearColorFilter()

            // Invalidate the view to force a redraw.
            v.invalidate()

            // Do a getResult() and display what happens.
            when(e.result) {
                true ->
                    Toast.makeText(this, "The drop was handled.", Toast.LENGTH_LONG)
                else ->
                    Toast.makeText(this, "The drop didn't work.", Toast.LENGTH_LONG)
            }.show()

            // Return true. The value is ignored.
            true
        }
        else -> {
            // An unknown action type is received.
            Log.e("DragDrop Example", "Unknown action type received by View.OnDragListener.")
            false
        }
    }
}
```

### Java

```java
View imageView = new ImageView(this);

// Set the drag event listener for the View.
imageView.setOnDragListener( (v, e) -> {

    // Handle each of the expected events.
    switch(e.getAction()) {

        case DragEvent.ACTION_DRAG_STARTED:

            // Determine whether this View can accept the dragged data.
            if (e.getClipDescription().hasMimeType(ClipDescription.MIMETYPE_TEXT_PLAIN)) {

                // As an example, apply a blue color tint to the View to
                // indicate that it can accept data.
                ((ImageView)v).setColorFilter(Color.BLUE);

                // Invalidate the view to force a redraw in the new tint.
                v.invalidate();

                // Return true to indicate that the View can accept the dragged
                // data.
                return true;

            }

            // Return false to indicate that, during the current drag-and-drop
            // operation, this View doesn't receive events again until
            // ACTION_DRAG_ENDED is sent.
            return false;

        case DragEvent.ACTION_DRAG_ENTERED:

            // Apply a green tint to the View.
            ((ImageView)v).setColorFilter(Color.GREEN);

            // Invalidate the view to force a redraw in the new tint.
            v.invalidate();

            // Return true. The value is ignored.
            return true;

        case DragEvent.ACTION_DRAG_LOCATION:

            // Ignore the event.
            return true;

        case DragEvent.ACTION_DRAG_EXITED:

            // Reset the color tint to blue.
            ((ImageView)v).setColorFilter(Color.BLUE);

            // Invalidate the view to force a redraw in the new tint.
            v.invalidate();

            // Return true. The value is ignored.
            return true;

        case DragEvent.ACTION_DROP:

            // Get the item containing the dragged data.
            ClipData.Item item = e.getClipData().getItemAt(0);

            // Get the text data from the item.
            CharSequence dragData = item.getText();

            // Display a message containing the dragged data.
            Toast.makeText(this, "Dragged data is " + dragData, Toast.LENGTH_LONG).show();

            // Turn off color tints.
            ((ImageView)v).clearColorFilter();

            // Invalidate the view to force a redraw.
            v.invalidate();

            // Return true. DragEvent.getResult() returns true.
            return true;

        case DragEvent.ACTION_DRAG_ENDED:

            // Turn off color tinting.
            ((ImageView)v).clearColorFilter();

            // Invalidate the view to force a redraw.
            v.invalidate();

            // Do a getResult() and displays what happens.
            if (e.getResult()) {
                Toast.makeText(this, "The drop was handled.", Toast.LENGTH_LONG).show();
            } else {
                Toast.makeText(this, "The drop didn't work.", Toast.LENGTH_LONG).show();
            }

            // Return true. The value is ignored.
            return true;

        // An unknown action type is received.
        default:
            Log.e("DragDrop Example","Unknown action type received by View.OnDragListener.");
            break;
    }

    return false;

});
```

## Customize a drag shadow

You can define a customized `myDragShadowBuilder` by overriding the methods in
`View.DragShadowBuilder`. The following code snippet creates a small,
rectangular, gray drag shadow for a `TextView`:

### Kotlin

```kotlin
private class MyDragShadowBuilder(view: View) : View.DragShadowBuilder(view) {

    private val shadow = ColorDrawable(Color.LTGRAY)

    // Define a callback that sends the drag shadow dimensions and touch point
    // back to the system.
    override fun onProvideShadowMetrics(size: Point, touch: Point) {

            // Set the width of the shadow to half the width of the original
            // View.
            val width: Int = view.width / 2

            // Set the height of the shadow to half the height of the original
            // View.
            val height: Int = view.height / 2

            // The drag shadow is a ColorDrawable. Set its dimensions to
            // be the same as the Canvas that the system provides. As a result,
            // the drag shadow fills the Canvas.
            shadow.setBounds(0, 0, width, height)

            // Set the size parameter's width and height values. These get back
            // to the system through the size parameter.
            size.set(width, height)

            // Set the touch point's position to be in the middle of the drag
            // shadow.
            touch.set(width / 2, height / 2)
    }

    // Define a callback that draws the drag shadow in a Canvas that the system
    // constructs from the dimensions passed to onProvideShadowMetrics().
    override fun onDrawShadow(canvas: Canvas) {

            // Draw the ColorDrawable on the Canvas passed in from the system.
            shadow.draw(canvas)
    }
}
```

### Java

```java
private static class MyDragShadowBuilder extends View.DragShadowBuilder {

    // The drag shadow image, defined as a drawable object.
    private static Drawable shadow;

    // Constructor.
    public MyDragShadowBuilder(View view) {

            // Store the View parameter.
            super(view);

            // Create a draggable image that fills the Canvas provided by the
            // system.
            shadow = new ColorDrawable(Color.LTGRAY);
    }

    // Define a callback that sends the drag shadow dimensions and touch point
    // back to the system.
    @Override
    public void onProvideShadowMetrics (Point size, Point touch) {

            // Define local variables.
            int width, height;

            // Set the width of the shadow to half the width of the original
            // View.
            width = getView().getWidth() / 2;

            // Set the height of the shadow to half the height of the original
            // View.
            height = getView().getHeight() / 2;

            // The drag shadow is a ColorDrawable. Set its dimensions to
            // be the same as the Canvas that the system provides. As a result,
            // the drag shadow fills the Canvas.
            shadow.setBounds(0, 0, width, height);

            // Set the size parameter's width and height values. These get back
            // to the system through the size parameter.
            size.set(width, height);

            // Set the touch point's position to be in the middle of the drag
            // shadow.
            touch.set(width / 2, height / 2);
    }

    // Define a callback that draws the drag shadow in a Canvas that the system
    // constructs from the dimensions passed to onProvideShadowMetrics().
    @Override
    public void onDrawShadow(Canvas canvas) {

            // Draw the ColorDrawable on the Canvas passed in from the system.
            shadow.draw(canvas);
    }
}
```

> [!NOTE]
> **Note:** You don't have to extend `View.DragShadowBuilder`. The constructor [`View.DragShadowBuilder(View)`](https://developer.android.com/reference/android/view/View.DragShadowBuilder#DragShadowBuilder(android.view.View)) creates a default drag shadow that's the same size as the `View` argument passed to it. The constructor also centers the touch point in the drag shadow.