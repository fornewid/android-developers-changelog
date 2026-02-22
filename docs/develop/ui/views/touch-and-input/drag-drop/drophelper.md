---
title: https://developer.android.com/develop/ui/views/touch-and-input/drag-drop/drophelper
url: https://developer.android.com/develop/ui/views/touch-and-input/drag-drop/drophelper
source: md.txt
---

The [`DropHelper`](https://developer.android.com/reference/androidx/draganddrop/DropHelper) class simplifies
implementation of drag-and-drop capabilities. A member of the Jetpack
[`DragAndDrop`](https://developer.android.com/jetpack/androidx/releases/draganddrop) library, `DropHelper`
provides backward compatibility down to API level 24.

Use `DropHelper` to specify drop targets, customize drop target highlighting,
and define how dropped data is handled.

## Set drag source

| **Note:** See [Drag and Drop Demo](https://github.com/android/platform-samples/tree/main/samples/user-interface/draganddrop) for a complete implementation sample.

To get started, create [`DragStartHelper`](https://developer.android.com/reference/androidx/core/view/DragStartHelper)
with drag source view and
[`OnDragStartListener`](https://developer.android.com/reference/androidx/core/view/DragStartHelper.OnDragStartListener).

In [`OnDragStartListener`](https://developer.android.com/reference/androidx/core/view/DragStartHelper.OnDragStartListener),
override method [`onDragStart()`](https://developer.android.com/reference/androidx/core/view/DragStartHelper.OnDragStartListener#onDragStart(android.view.View,androidx.core.view.DragStartHelper)). Create a `ClipData` object
and `ClipData.Item` object for the data being moved. As part of the `ClipData`,
supply metadata that is stored in a `ClipDescription` object within the
`ClipData`. For a drag-and-drop operation that doesn't represent data movement,
you might want to use `null` instead of an actual object.  

### Kotlin

```kotlin
DragStartHelper(draggableView)
    { view: View, _: DragStartHelper ->
        val item = ClipData.Item(view.tag as? CharSequence)
        val dragData = ClipData(
            view.tag as? CharSequence,
            arrayOf(ClipDescription.MIMETYPE_TEXT_PLAIN),
            item
        )
        view.startDragAndDrop(
            dragData,
            View.DragShadowBuilder(view),
            null,
            0
        )
    }.attach()
```

### Java

```java
new DragStartHelper(draggableView, new DragStartHelper.OnDragStartListener() {
    @Override
    public void onDragStart(View view, DragStartHelper helper) {
        CharSequence tag = (CharSequence) view.getTag();
        ClipData.Item item = new ClipData.Item(tag);
        ClipData dragData = new ClipData(
          tag, new String[]{ClipDescription.MIMETYPE_TEXT_PLAIN}, item);
        view.startDragAndDrop(
          dragData, new View.DragShadowBuilder(view), null, 0);
    }
});
```

## Specify drop targets

When a user release a drop shadow over a view, the view needs to be configured
properly to accept the data and respond correctly.

[`DropHelper.configureView()`](https://developer.android.com/reference/androidx/draganddrop/DropHelper#configureView(android.app.Activity,%20android.view.View,%20java.lang.String%5B%5D,%20androidx.core.view.OnReceiveContentListener))
is a static, overloaded method that lets you specify drop targets. Its
parameters include the following:

- The current [`Activity`](https://developer.android.com/reference/android/app/Activity)---used for [URI
  permissions](https://developer.android.com/reference/android/app/Activity#requestDragAndDropPermissions(android.view.DragEvent)).
  - A [`View`](https://developer.android.com/reference/android/view/View) that serves as the drop target.
    - The [MIME types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types) the drop target can accept from the dropped data.
- Configuration options for the drop target---in particular, a list of [embedded `EditText` fields](https://developer.android.com/develop/ui/views/touch-and-input/drag-drop/drophelper#EditTextComponentsInDropTargets).
- An [`OnReceiveContentListener`](https://developer.android.com/reference/androidx/core/view/OnReceiveContentListener) to handle dropped data.

For example, to create a drop target that accepts images, use either of the
following method calls:  

### Kotlin

```kotlin
configureView(
    myActivity,
    targetView,
    arrayOf("image/*"),
    options,
    onReceiveContentListener)

// or

configureView(
    myActivity,
    targetView,
    arrayOf("image/*"),
    onReceiveContentListener)
```

### Java

```java
DropHelper.configureView(
    myActivity,
    targetView,
    new String[] {"image/*"},
    options,
    onReceiveContentlistener);

// or

DropHelper.configureView(
    myActivity,
    targetView,
    new String[] {"image/*"},
    onReceiveContentlistener);
```

The second call omits the drop target configuration options, in which case the
drop target highlight color is set to the theme's secondary (or accent) color,
the highlight corner radius is set to 16 dp, and the list of `EditText`
components is empty. See the following section for details.

## Configure drop targets

The [`DropHelper.Options`](https://developer.android.com/reference/androidx/draganddrop/DropHelper.Options)
inner class lets you configure drop targets. Provide an instance of the class to
the [`DropHelper.configureView(Activity, View, String[], Options,
OnReceiveContentListener`)](https://developer.android.com/reference/androidx/draganddrop/DropHelper#configureView(android.app.Activity,%20android.view.View,%20java.lang.String%5B%5D,%20androidx.draganddrop.DropHelper.Options,%20androidx.core.view.OnReceiveContentListener))
method. See the previous section for more information.

## Customize drop target highlighting

`DropHelper` configures drop targets to display a highlight as users drag
content over the targets. `DropHelper` provides default styling, and
`DropHelper.Options` lets you set the color of the highlight and specify the
corner radius of the highlight's rectangle.

Use the
[`DropHelper.Options.Builder`](https://developer.android.com/reference/androidx/draganddrop/DropHelper.Options.Builder)
class to create a `DropHelper.Options` instance and set configuration options,
as shown in the following example:  

### Kotlin

```kotlin
val options: DropHelper.Options = DropHelper.Options.Builder()
                                      .setHighlightColor(getColor(R.color.purple_300))
                                      .setHighlightCornerRadiusPx(resources.getDimensionPixelSize(R.dimen.drop_target_corner_radius))
                                      .build()
```

### Java

```java
DropHelper.Options options = new DropHelper.Options.Builder()
                                     .setHighlightColor(getColor(R.color.purple_300))
                                     .setHighlightCornerRadiusPx(getResources().getDimensionPixelSize(R.dimen.drop_target_corner_radius))
                                     .build();
```

### Handle EditText components in drop targets

`DropHelper` also controls focus within the drop target when the target contains
editable text fields.

Drop targets can be a single view or a view hierarchy. If the drop target view
hierarchy contains one or more [`EditText`](https://developer.android.com/reference/android/widget/EditText)
components, provide a list of the components to
[`DropHelper.Options.Builder.addInnerEditTexts(EditText...)`](https://developer.android.com/reference/androidx/draganddrop/DropHelper.Options.Builder#addInnerEditTexts(android.widget.EditText...))
to ensure that drop target highlighting and text data handling work correctly.

`DropHelper` prevents `EditText` components within the drop target view
hierarchy from stealing focus from the containing view during drag interactions.

Also, if the drag-and-drop [`ClipData`](https://developer.android.com/reference/android/content/ClipData)
includes text and URI data, `DropHelper` selects one of the `EditText`
components in the drop target to handle the text data. Selection is based on the
following order of precedence:

1. The `EditText` on which the `ClipData` is dropped.
2. The `EditText` that contains the text cursor (caret).
3. The first `EditText` provided to the call to `DropHelper.Options.Builder.addInnerEditTexts(EditText...)`.

To set an `EditText` as the default text data handler, pass the `EditText` as
the first argument of the call to
`DropHelper.Options.Builder.addInnerEditTexts(EditText...)`. For example, if
your drop target handles images but contains editable text fields `T1`, `T2`,
and `T3`, make `T2` the default as follows:  

### Kotlin

```kotlin
val options: DropHelper.Options = DropHelper.Options.Builder()
                                      .addInnerEditTexts(T2, T1, T3)
                                      .build()
```

### Java

```java
DropHelper.Options options = new DropHelper.Options.Builder()
                                     .addInnerEditTexts(T2, T1, T3)
                                     .build();
```

## Handle data in drop targets

The `DropHelper.configureView()` method accepts an `OnReceiveContentListener`
that you create to handle the drag-and-drop `ClipData`. The drag-and-drop data
is provided to the listener in a
[`ContentInfoCompat`](https://developer.android.com/reference/androidx/core/view/ContentInfoCompat) object.
Text data is present in the object. Media, such as images, is represented by
URIs.
| **Warning:** `DropHelper` configures the drop target to listen for drag-and-drop events and to handle the dropped data. Don't attach a [`View.OnDragListener`](https://developer.android.com/reference/android/view/View.OnDragListener) or `OnReceiveContentListener` to drop targets when using `DropHelper`.

The `OnReceiveContentListener` also handles data provided to the drop target by
user interactions other than drag and drop---such as copy and
paste---when `DropHelper.configureView()` is used to configure the following
types of views:

- All views, if the user is running Android 12 or higher.
- [`AppCompatEditText`](https://developer.android.com/reference/androidx/appcompat/widget/AppCompatEditText), if the user is running a version of Android down to Android 7.0.

| **Note:** `DropHelper` supports the Jetpack [`OnReceiveContentListener`](https://developer.android.com/reference/androidx/core/view/OnReceiveContentListener) interface, which is backward compatible down to API level 24. `DropHelper` doesn't support the platform [`OnReceiveContentListener`](https://developer.android.com/reference/android/view/OnReceiveContentListener) interface introduced in API level 31.

### MIME types, permissions, and content validation

The MIME type checking by `DropHelper` is based on the drag-and-drop
[`ClipDescription`](https://developer.android.com/reference/android/content/ClipDescription), which is
created by the app providing the drag-and-drop data. Validate the
`ClipDescription` to ensure the MIME types are set correctly.

`DropHelper` requests all access permissions for content URIs contained in the
drag-and-drop `ClipData`. For more information, see
[`DragAndDropPermissions`](https://developer.android.com/reference/android/view/DragAndDropPermissions). The
permissions let you resolve the content URIs when processing the drag-and-drop
data.

`DropHelper` doesn't validate the data returned by content providers when
resolving URIs in the dropped data. Check for null and verify the correctness of
any resolved data.