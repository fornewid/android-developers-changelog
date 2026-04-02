---
title: Mouse pointer icons  |  ChromeOS  |  Android Developers
url: https://developer.android.com/develop/devices/chromeos/learn/pointer-styling
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [ChromeOS](https://developer.android.com/chrome-os/intro)

# Mouse pointer icons Stay organized with collections Save and categorize content based on your preferences.



Android users come to your app from all different types of form factors i.e., phones, tablets, foldables, and Chromebooks. When interacting with your application, especially on larger screens, users may also use some sort of pointing device like a three-button mouse. Android applications have support for applying different styling to the mouse pointer to help those users have a visual indication that they can interact with an object.

## Use the system default cursors

Users are familiar with different conventions for interacting with different types of objects on large screen devices. Android provides developers with some of the most common cursor icons that users are familiar with. You can add these system default cursor icons with a few lines of code. Let's take a look at the following Kotlin snippet:

```
myView.setOnHoverListener { view, _ ->
      view.pointerIcon =
         PointerIcon.getSystemIcon(applicationContext, PointerIcon.TYPE_HAND)
      false // Listener did not consume the event.
}
```

In this example, `myView` is the view that will be set to a pointer icon under certain conditions. The condition demonstrated here is a hover state, which occurs when the mouse pointer is over a view. In other scenarios, you might want a waiting icon during processing or a crosshair in a game.

The `setOnHoverListener` listens for when the pointer enters the hover state and then acts upon that event. Inside the event listener, `view.pointerIcon` is called to set the pointer icon for that particular view. An existing system icon is used to set the pointer's icon.

There are several system icons built into Android; a full list is at the [bottom of this page](/develop/devices/chromeos/learn/pointer-styling#system-default-cursors). The `TYPE_HAND` icon was used, which shows a closed hand with the index finger extended.

## Use your own special cursor

```
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

Adding pointer icons to your application is a great way to help enable your users to have more intuitive experiences across the different device form factors they use. There are plenty of great [default system icons](/develop/devices/chromeos/learn/pointer-styling#system-default-cursors) available and if those do not suit your needs, you are always able to load or create your own.

* **Drag and Drop -** If your application supports dragging from another application and dropping into your application you could implement the `TYPE_NO_DROP` icon. This would give a visual indication that your application does not support the mime type that is trying to be dropped into your app.
* **Mapping -** If you have a mapping application and you want to show users that they can pan the map, they could have an option to have the `TYPE_GRAB` icon when you are hovering over the map. When the user clicks, you can update the icon to a grabbing hand to show that they are panning the map.
* **Photo Editing -** Photo editing users like to have controls that allow them to select a magnifying glass to zoom in. You could change the cursor to a magnifying glass with the `TYPE_ZOOM_IN` icon when zoom in mode is selected.
* **And many more opportunities**

**Note:** To see different pointer changes in action check out this [GitHub Pointer Sample](https://github.com/chromeos/pointer-icon-sample)

![Custom pointer icons in an Android app.](/static/images/develop/chromeos/pointer-1-gif.gif)

## Appendix

### Additional Reading

* [GitHub Pointer Sample](https://github.com/chromeos/pointer-icon-sample)
* [PointerIcon Android Class Documentation](/reference/android/view/PointerIcon)
* [Optimizing Apps for ChromeOS : Custom Cursors](/topic/arc/optimizing#custom-cursors)

### System Default Cursors

These are the available cursors by default in the Android System.

| Cursor Name | Icon |
| --- | --- |
| TYPE\_ALIAS | The alias cursor, an arrow with a small curved arrow next to it. |
| TYPE\_ALL\_SCROLL | The all-scroll cursor, a circle with four arrows pointing outwards. |
| TYPE\_ARROW | The standard arrow cursor. |
| TYPE\_CELL | Cell Cursor |
| TYPE\_CONTEXT\_MENU | The context menu cursor, an arrow with a small menu icon next to it. |
| TYPE\_COPY | The copy cursor, an arrow with a plus sign next to it. |
| TYPE\_CROSSHAIR | The crosshair cursor, a plus sign with a dot in the center. |
| TYPE\_DEFAULT | The default arrow cursor. |
| TYPE\_GRAB | The grab cursor, an open hand. |
| TYPE\_GRABBING | The grabbing cursor, a closed hand. |
| TYPE\_HAND | The hand cursor, a hand with the index finger pointing. |
| TYPE\_HELP | The help cursor, an arrow with a question mark next to it. |
| TYPE\_HORIZONTAL\_DOUBLE\_ARROW | The horizontal double arrow cursor for resizing. |
| TYPE\_NO\_DROP | The no-drop cursor, a circle with a line through it. |
| TYPE\_NULL | No Cursor Will Display |
| TYPE\_TEXT | The text cursor, an I-beam. |
| TYPE\_TOP\_LEFT\_DIAGONAL\_DOUBLE\_ARROW | The top-left to bottom-right diagonal double arrow cursor for resizing. |
| TYPE\_TOP\_RIGHT\_DIAGONAL\_DOUBLE\_ARROW | The top-right to bottom-left diagonal double arrow cursor for resizing. |
| TYPE\_VERTICAL\_DOUBLE\_ARROW | The vertical double arrow cursor for resizing. |
| TYPE\_VERTICAL\_TEXT | The vertical text cursor, a horizontal I-beam. |
| TYPE\_WAIT | The wait cursor, an hourglass or spinning circle. |
| TYPE\_ZOOM\_IN | The zoom-in cursor, a magnifying glass with a plus sign. |
| TYPE\_ZOOM\_OUT | The zoom-out cursor, a magnifying glass with a minus sign. |