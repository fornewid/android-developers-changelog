---
title: https://developer.android.com/develop/devices/chromeos/learn/pointer-styling
url: https://developer.android.com/develop/devices/chromeos/learn/pointer-styling
source: md.txt
---

Android users come to your app from all different types of form factors i.e., phones, tablets, foldables, and Chromebooks. When interacting with your application, especially on larger screens, users may also use some sort of pointing device like a three-button mouse. Android applications have support for applying different styling to the mouse pointer to help those users have a visual indication that they can interact with an object.

## Use the system default cursors


Users are familiar with different conventions for interacting with different types of objects on large screen devices. Android provides developers with some of the most common cursor icons that users are familiar with. You can add these system default cursor icons with a few lines of code. Let's take a look at the following Kotlin snippet:  

```kotlin
myView.setOnHoverListener { view, _ ->
      view.pointerIcon =
         PointerIcon.getSystemIcon(applicationContext, PointerIcon.TYPE_HAND)
      false // Listener did not consume the event.
}
```


In this example, `myView` is the view that will be set to a pointer icon under certain conditions. The condition demonstrated here is a hover state, which occurs when the mouse pointer is over a view. In other scenarios, you might want a waiting icon during processing or a crosshair in a game.


The `setOnHoverListener` listens for when the pointer enters the hover state and then acts upon that event. Inside the event listener, `view.pointerIcon` is called to set the pointer icon for that particular view. An existing system icon is used to set the pointer's icon.


There are several system icons built into Android; a full list is at the [bottom of this page](https://developer.android.com/develop/devices/chromeos/learn/pointer-styling#system-default-cursors). The `TYPE_HAND` icon was used, which shows a closed hand with the index finger extended.

## Use your own special cursor

```kotlin
// Loading a bitmap to use as a pointer icon
    BitmapFactory.decodeResource(
        this.resources,
        R.drawable.dollar_sign
    ), CURSOR_WIDTH, CURSOR_HEIGHT, false
)

// Creating the pointer icon and sending clicks from the center of the mouse icon
PointerIcon.create(dollarBitmap, (CURSOR_WIDTH/2).toFloat(), (CURSOR_HEIGHT/2).toFloat())
```

**Note:** The location of the hotspot depends on your use case. For example, a drawing app would set the hotspot to be the tip of the pen or paintbrush.

## Examples


Adding pointer icons to your application is a great way to help enable your users to have more intuitive experiences across the different device form factors they use. There are plenty of great [default system icons](https://developer.android.com/develop/devices/chromeos/learn/pointer-styling#system-default-cursors) available and if those do not suit your needs, you are always able to load or create your own.

- **Drag and Drop -** If your application supports dragging from another application and dropping into your application you could implement the `TYPE_NO_DROP` icon. This would give a visual indication that your application does not support the mime type that is trying to be dropped into your app.
- **Mapping -** If you have a mapping application and you want to show users that they can pan the map, they could have an option to have the `TYPE_GRAB` icon when you are hovering over the map. When the user clicks, you can update the icon to a grabbing hand to show that they are panning the map.
- **Photo Editing -** Photo editing users like to have controls that allow them to select a magnifying glass to zoom in. You could change the cursor to a magnifying glass with the `TYPE_ZOOM_IN` icon when zoom in mode is selected.
- **And many more opportunities**

**Note:** To see different pointer changes in action check out this [GitHub Pointer Sample](https://github.com/chromeos/pointer-icon-sample)


![Custom pointer icons in an Android app.](https://developer.android.com/static/images/develop/chromeos/pointer-1-gif.gif)

## Appendix

### Additional Reading

- [GitHub Pointer Sample](https://github.com/chromeos/pointer-icon-sample)
- [PointerIcon Android Class Documentation](https://developer.android.com/reference/android/view/PointerIcon)
- [Optimizing Apps for ChromeOS : Custom Cursors](https://developer.android.com/topic/arc/optimizing#custom-cursors)

### System Default Cursors


These are the available cursors by default in the Android System.

| Cursor Name | Icon |
|---|---|
| TYPE_ALIAS | ![The alias cursor, an arrow with a small curved arrow next to it.](https://developer.android.com/images/develop/chromeos/pointer-1.avif) |
| TYPE_ALL_SCROLL | ![The all-scroll cursor, a circle with four arrows pointing outwards.](https://developer.android.com/images/develop/chromeos/pointer-2.avif) |
| TYPE_ARROW | ![The standard arrow cursor.](https://developer.android.com/images/develop/chromeos/pointer-3.avif) |
| TYPE_CELL | Cell Cursor |
| TYPE_CONTEXT_MENU | ![The context menu cursor, an arrow with a small menu icon next to it.](https://developer.android.com/images/develop/chromeos/pointer-4.avif) |
| TYPE_COPY | ![The copy cursor, an arrow with a plus sign next to it.](https://developer.android.com/images/develop/chromeos/pointer-5.avif) |
| TYPE_CROSSHAIR | ![The crosshair cursor, a plus sign with a dot in the center.](https://developer.android.com/images/develop/chromeos/pointer-6.avif) |
| TYPE_DEFAULT | ![The default arrow cursor.](https://developer.android.com/images/develop/chromeos/pointer-7.avif) |
| TYPE_GRAB | ![The grab cursor, an open hand.](https://developer.android.com/images/develop/chromeos/pointer-8.avif) |
| TYPE_GRABBING | ![The grabbing cursor, a closed hand.](https://developer.android.com/images/develop/chromeos/pointer-9.avif) |
| TYPE_HAND | ![The hand cursor, a hand with the index finger pointing.](https://developer.android.com/images/develop/chromeos/pointer-10.avif) |
| TYPE_HELP | ![The help cursor, an arrow with a question mark next to it.](https://developer.android.com/images/develop/chromeos/pointer-11.avif) |
| TYPE_HORIZONTAL_DOUBLE_ARROW | ![The horizontal double arrow cursor for resizing.](https://developer.android.com/images/develop/chromeos/pointer-12.avif) |
| TYPE_NO_DROP | ![The no-drop cursor, a circle with a line through it.](https://developer.android.com/images/develop/chromeos/pointer-13.avif) |
| TYPE_NULL | No Cursor Will Display |
| TYPE_TEXT | ![The text cursor, an I-beam.](https://developer.android.com/images/develop/chromeos/pointer-14.avif) |
| TYPE_TOP_LEFT_DIAGONAL_DOUBLE_ARROW | ![The top-left to bottom-right diagonal double arrow cursor for resizing.](https://developer.android.com/images/develop/chromeos/pointer-15.avif) |
| TYPE_TOP_RIGHT_DIAGONAL_DOUBLE_ARROW | ![The top-right to bottom-left diagonal double arrow cursor for resizing.](https://developer.android.com/images/develop/chromeos/pointer-16.avif) |
| TYPE_VERTICAL_DOUBLE_ARROW | ![The vertical double arrow cursor for resizing.](https://developer.android.com/images/develop/chromeos/pointer-17.avif) |
| TYPE_VERTICAL_TEXT | ![The vertical text cursor, a horizontal I-beam.](https://developer.android.com/images/develop/chromeos/pointer-18.avif) |
| TYPE_WAIT | ![The wait cursor, an hourglass or spinning circle.](https://developer.android.com/static/images/develop/chromeos/pointer-19.gif) |
| TYPE_ZOOM_IN | ![The zoom-in cursor, a magnifying glass with a plus sign.](https://developer.android.com/images/develop/chromeos/pointer-20.avif) |
| TYPE_ZOOM_OUT | ![The zoom-out cursor, a magnifying glass with a minus sign.](https://developer.android.com/images/develop/chromeos/pointer-21.avif) |