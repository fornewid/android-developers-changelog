---
title: https://developer.android.com/develop/ui/views/touch-and-input/drag-drop/multi-window
url: https://developer.android.com/develop/ui/views/touch-and-input/drag-drop/multi-window
source: md.txt
---

Devices that run Android 7.0 (API level 24) or higher support [multi-window
mode](https://developer.android.com/develop/ui/views/layout/support-multi-window-mode), which lets users
move data from one app to another by dragging and dropping.

The *source app* , where the operation starts, provides the data.
The *target app*, where the operation ends, receives the data.

When the user starts to drag content, the source app should set the
[`DRAG_FLAG_GLOBAL`](https://developer.android.com/reference/android/view/View#DRAG_FLAG_GLOBAL) flag to
indicate that the user can drag data to another app.

Because the data moves across app boundaries, the apps share access to the data
using a content URI. This requires the following:

- The source app must set either or both of the [`DRAG_FLAG_GLOBAL_URI_READ`](https://developer.android.com/reference/android/view/View#DRAG_FLAG_GLOBAL_URI_READ) and [`DRAG_FLAG_GLOBAL_URI_WRITE`](https://developer.android.com/reference/android/view/View#DRAG_FLAG_GLOBAL_URI_WRITE) flags, depending on the read or write access to the data that the source app wants to grant to the target app.
- The target app must call [`requestDragAndDropPermissions()`](https://developer.android.com/reference/android/app/Activity#requestDragAndDropPermissions(android.view.DragEvent)) immediately before handling the data that the user drags into the app. If the target app no longer needs access to the dragged data, the app can then call [`release()`](https://developer.android.com/reference/android/view/DragAndDropPermissions#release()) on the object that was returned from `requestDragAndDropPermissions()`. Otherwise, the permissions are released when the containing activity is destroyed. If your implementation involves starting a new Activity to process the dropped URIs, you will need to grant the new Activity the same permissions. You must set the clip data and a flag:

  ### Kotlin

  ```kotlin
  intent.setClipData(clipData)
  intent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
  ```

  ### Java

  ```java
  intent.setClipData(clipData);
  intent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
  ```

The following code snippets demonstrate how to release read-only access to
dragged data immediately after the user drop operation takes place. See the
[Drag and Drop Demo](https://github.com/android/user-interface-samples/tree/main/DragAndDrop)
on GitHub for a more complete example.

## Source activity

### Kotlin

```kotlin
// Drag a file stored in an images/ directory in internal storage.
val internalImagesDir = File(context.filesDir, "images")
val imageFile = File(internalImagesDir, imageFilename)
val uri = FileProvider.getUriForFile(context, contentAuthority, imageFile)

val listener = OnDragStartListener@{ view: View, _: DragStartHelper ->
    val clipData = ClipData(ClipDescription("Image Description",
                                            arrayOf("image/*")),
                            ClipData.Item(uri))
    // Must include DRAG_FLAG_GLOBAL to permit dragging data between apps.
    // This example provides read-only access to the data.
    val flags = View.DRAG_FLAG_GLOBAL or View.DRAG_FLAG_GLOBAL_URI_READ
    return@OnDragStartListener view.startDragAndDrop(clipData,
                                                     View.DragShadowBuilder(view),
                                                     null,
                                                     flags)
}

// Container where the image originally appears in the source app.
val srcImageView = findViewById<ImageView>(R.id.imageView)

// Detect and start the drag event.
DragStartHelper(srcImageView, listener).apply {
    attach()
}
```

### Java

```java
// Drag a file stored in an images/ directory in internal storage.
File internalImagesDir = new File(context.getFilesDir(), "images");
File imageFile = new File(internalImagesDir, imageFilename);
final Uri uri = FileProvider.getUriForFile(context, contentAuthority, imageFile);

// Container where the image originally appears in the source app.
ImageView srcImageView = findViewById(R.id.imageView);

// Enable the view to detect and start the drag event.
new DragStartHelper(srcImageView, (view, helper) -> {
    ClipData clipData = new ClipData(new ClipDescription("Image Description",
                                                          new String[] {"image/*"}),
                                     new ClipData.Item(uri));
    // Must include DRAG_FLAG_GLOBAL to permit dragging data between apps.
    // This example provides read-only access to the data.
    int flags = View.DRAG_FLAG_GLOBAL | View.DRAG_FLAG_GLOBAL_URI_READ;
    return view.startDragAndDrop(clipData,
                                 new View.DragShadowBuilder(view),
                                 null,
                                 flags);
}).attach();
```

## Target activity

### Kotlin

```kotlin
// Container where the image is to be dropped in the target app.
val targetImageView = findViewById<ImageView>(R.id.imageView)

targetImageView.setOnDragListener { view, event ->

    when (event.action) {

        ACTION_DROP -> {
            val imageItem: ClipData.Item = event.clipData.getItemAt(0)
            val uri = imageItem.uri

            // Request permission to access the image data being dragged into
            // the target activity's ImageView element.
            val dropPermissions = requestDragAndDropPermissions(event)
            (view as ImageView).setImageURI(uri)

            // Release the permission immediately afterward because it's no
            // longer needed.
            dropPermissions.release()
            return@setOnDragListener true
        }

        // Implement logic for other DragEvent cases here.

        // An unknown action type is received.
        else -> {
            Log.e("DragDrop Example", "Unknown action type received by View.OnDragListener.")
            return@setOnDragListener false
        }

    }
}
```

### Java

```java
// Container where the image is to be dropped in the target app.
ImageView targetImageView = findViewById(R.id.imageView);

targetImageView.setOnDragListener( (view, event) -> {

    switch (event.getAction()) {

        case ACTION_DROP:
            ClipData.Item imageItem = event.getClipData().getItemAt(0);
            Uri uri = imageItem.getUri();

            // Request permission to access the image data being dragged into
            // the target activity's ImageView element.
            DragAndDropPermissions dropPermissions =
                requestDragAndDropPermissions(event);

            ((ImageView)view).setImageURI(uri);

            // Release the permission immediately afterward because it's no
            // longer needed.
            dropPermissions.release();

            return true;

        // Implement logic for other DragEvent cases here.

        // An unknown action type was received.
        default:
            Log.e("DragDrop Example","Unknown action type received by View.OnDragListener.");
            break;
    }

    return false;
});
```