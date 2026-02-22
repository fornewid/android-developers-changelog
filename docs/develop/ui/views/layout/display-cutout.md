---
title: https://developer.android.com/develop/ui/views/layout/display-cutout
url: https://developer.android.com/develop/ui/views/layout/display-cutout
source: md.txt
---

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to work with display cutouts in Compose.  
[Display cutouts in Compose →](https://developer.android.com/jetpack/compose/system/cutouts)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

<br />

A [*display cutout*](https://developer.android.com/guide/topics/display-cutout) is an area on some devices
that extends into the display surface. It allows for an edge-to-edge experience
while providing space for important sensors on the front of the device.
| **Note:** Before attempting to render your app into the cutout area, ensure your app is configured to [display content edge to
| edge](https://developer.android.com/develop/ui/views/layout/edge-to-edge).

Android supports display cutouts on devices running Android 9 (API level 28) and
higher. However, device manufacturers can also support display cutouts on
devices running Android 8.1 or lower.

This document describes how to implement support for devices with cutouts,
including how to work with the *cutout area*---that is, the edge-to-edge
rectangle on the display surface that contains the cutout.
![An image showing an example of top-center display cutout](https://developer.android.com/static/develop/ui/views/layout/display-cutout/images/cutout-intro.png) **Figure 1.** 1 Display cutout.

## Choose how your app handles cutout areas

If you don't want your content to overlap with a cutout area, it's generally
sufficient to make sure your content doesn't overlap with the status bar and the
navigation bar. If you're rendering into the cutout area, use
[`WindowInsetsCompat.getDisplayCutout()`](https://developer.android.com/reference/androidx/core/view/WindowInsetsCompat#getDisplayCutout())
to retrieve a [`DisplayCutout`](https://developer.android.com/reference/android/view/DisplayCutout) object
that contains the safe insets and bounding box for each cutout. These APIs let
you check whether your content overlaps with the cutout so that you can
reposition if needed.

You can also determine whether content is laid out behind the cutout area. The
[`layoutInDisplayCutoutMode`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#layoutInDisplayCutoutMode)
window layout attribute controls how your content is drawn in the cutout area.
You can set `layoutInDisplayCutoutMode` to one of the following values:

- [`LAYOUT_IN_DISPLAY_CUTOUT_MODE_DEFAULT`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#LAYOUT_IN_DISPLAY_CUTOUT_MODE_DEFAULT): content renders into the cutout area when the display cutout is contained in a system bar. Otherwise, the window does not overlap the display cutout; for example, content may be letterboxed when displayed in landscape mode. If your app targets SDK 35, this is interpreted as `ALWAYS` for non-floating windows.
- [`LAYOUT_IN_DISPLAY_CUTOUT_MODE_ALWAYS`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#LAYOUT_IN_DISPLAY_CUTOUT_MODE_ALWAYS): content is always allowed to extend into the cutout areas. If your app targets SDK 35 and is running on an Android 15 device, this is the only allowed mode for non-floating windows to ensure an edge-to-edge display.
- [`LAYOUT_IN_DISPLAY_CUTOUT_MODE_SHORT_EDGES`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#LAYOUT_IN_DISPLAY_CUTOUT_MODE_SHORT_EDGES): content renders into the cutout area in both portrait and landscape modes. Don't use for floating windows. If your app targets SDK 35, this is interpreted as `ALWAYS` for non-floating windows.
- [`LAYOUT_IN_DISPLAY_CUTOUT_MODE_NEVER`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#LAYOUT_IN_DISPLAY_CUTOUT_MODE_NEVER): content never renders into the cutout area. If your app targets SDK 35, this is interpreted as `ALWAYS` for non-floating windows.

You can set the cutout mode either programmatically or by setting a
[style](https://developer.android.com/guide/topics/ui/look-and-feel/themes) in your activity. The following
example defines a style to apply the `LAYOUT_IN_DISPLAY_CUTOUT_MODE_SHORT_EDGES`
attribute to the activity.  

```xml
<style name="ActivityTheme">
  <item name="android:windowLayoutInDisplayCutoutMode">
    shortEdges <!-- default, shortEdges, or never -->
  </item>
</style>
```

The following sections describe the different cutout modes in more detail.

### Default behavior

If your app targets SDK 35 and is running on an Android 15 device,
[`LAYOUT_IN_DISPLAY_CUTOUT_MODE_ALWAYS`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#LAYOUT_IN_DISPLAY_CUTOUT_MODE_ALWAYS) is the default behavior, and
`LAYOUT_IN_DISPLAY_CUTOUT_MODE_DEFAULT` is interpreted as
`LAYOUT_IN_DISPLAY_CUTOUT_MODE_ALWAYS` for non-floating windows.

Otherwise, `LAYOUT_IN_DISPLAY_CUTOUT_MODE_DEFAULT` is the default.

### Render content in short edge cutout areas

If your app targets SDK 35 and is running on an Android 15 device,
`LAYOUT_IN_DISPLAY_CUTOUT_MODE_SHORT_EDGES` is interpreted as
`LAYOUT_IN_DISPLAY_CUTOUT_MODE_ALWAYS` for non-floating windows.

With `LAYOUT_IN_DISPLAY_CUTOUT_MODE_SHORT_EDGES`, the
content extends into the cutout area on the short edge of the display in both
portrait and landscape, regardless of whether the system bars are hidden or
visible. When using this mode, be sure that no important content overlaps with
the cutout area.
| **Note:** The window can never extend into a cutout area on the long edges of the screen.

The following image is an example of `LAYOUT_IN_DISPLAY_CUTOUT_MODE_SHORT_EDGES`
for a device in portrait:
![An image showing content rendering into the cutout area while in portrait mode](https://developer.android.com/static/develop/ui/views/layout/display-cutout/images/cutout-short-edges-1.png) **Figure 2.** Content rendering into the cutout area while in portrait mode.

The following image is an example of `LAYOUT_IN_DISPLAY_CUTOUT_MODE_SHORT_EDGES`
for a device in landscape:
![An image showing content rendering into the cutout area while in landscape mode](https://developer.android.com/static/develop/ui/views/layout/display-cutout/images/cutout-short-edges-2.png) **Figure 3.** Content rendering into the cutout area while in landscape mode.

In this mode, the window extends under cutouts on the short edge of the display
in both portrait and landscape, regardless of whether the window is hiding the
system bars.

A cutout in the corner is considered to be on the short edge:
![An image showing a device with a corner cutout](https://developer.android.com/static/develop/ui/views/layout/display-cutout/images/cutout-corner.png) **Figure 4.** A device with a corner cutout.

### Never render content in the display cutout area

If your app targets SDK 35 and is running on an Android 15 device,
`LAYOUT_IN_DISPLAY_CUTOUT_MODE_NEVER` is interpreted as
`LAYOUT_IN_DISPLAY_CUTOUT_MODE_ALWAYS` for non-floating windows.

With `LAYOUT_IN_DISPLAY_CUTOUT_MODE_NEVER`, the window is never allowed to
overlap with the cutout area.

The following is an example of `LAYOUT_IN_DISPLAY_CUTOUT_MODE_NEVER` in
portrait:
![An image showing the LAYOUT_IN_DISPLAY_CUTOUT_MODE_NEVER for portrait](https://developer.android.com/static/develop/ui/views/layout/display-cutout/images/cutout-never.png) **Figure 5.** Example of `LAYOUT_IN_DISPLAY_CUTOUT_MODE_NEVER` for portrait mode.

The following is an example of `LAYOUT_IN_DISPLAY_CUTOUT_MODE_NEVER` in
landscape mode:
![An image showing the LAYOUT_IN_DISPLAY_CUTOUT_MODE_NEVER for landscape](https://developer.android.com/static/develop/ui/views/layout/display-cutout/images/cutout-never-landscape.png) **Figure 6.** Example of `LAYOUT_IN_DISPLAY_CUTOUT_MODE_NEVER` in landscape mode.

## Best practices for display cutout support

When working with display cutouts, consider the following:

- Be mindful of the placement of critical elements of the UI. Don't let the cutout area obscure any important text, controls, or other information.
- Don't place or extend any interactive elements that require fine-touch recognition into the cutout area. Touch sensitivity might be lower in the cutout area.
- Where possible, use
  [`WindowInsetsCompat`](https://developer.android.com/reference/androidx/core/view/WindowInsetsCompat) to
  retrieve the status bar height and determine the appropriate padding to apply
  to your content. Avoid hardcoding the status bar height, as this can lead to
  overlapping or cut-off content.

  ![An image showing content cut at the top for improper insets setup](https://developer.android.com/static/develop/ui/views/layout/display-cutout/images/cutout-status-bar-1.png) **Figure 7.** Use `WindowInsetsCompat` to avoid overlapping or cutting off content.
- Use [`View.getLocationInWindow()`](https://developer.android.com/reference/android/view/View#getLocationInWindow(int%5B%5D))
  to determine how much window space your app is using. Don't assume the app is
  using the entire window, and don't use
  [`View.getLocationOnScreen()`](https://developer.android.com/reference/android/view/View#getLocationOnScreen(int%5B%5D)).

- Use `always`, `shortEdges` or `never` cutout modes if your app needs to
  transition into and out of immersive mode. Default cutout behavior can cause
  content in your app to render in the cutout area while the system bars are
  present, but not while in immersive mode. This results in the content moving up
  and down during transitions, as demonstrated in the following example.

  ![An image showing content moving up and down during transitions.](https://developer.android.com/static/develop/ui/views/layout/display-cutout/images/cutout-fullscreen.png) **Figure 8.** Example of content moving up and down during transitions.
- In immersive mode, be careful using window versus screen coordinates, since
  your app doesn't use the whole screen when letterboxed. Because of the
  letterbox, coordinates from the screen origin aren't the same as coordinates
  from the window origin. You can transform screen coordinates to the view's
  coordinates as needed by using `getLocationOnScreen()`. The following image
  shows how coordinates differ when content is letterboxed:

  ![An image showing window versus screen coordinates when content is letterboxed.](https://developer.android.com/static/develop/ui/views/layout/display-cutout/images/cutout-coordinates.png) **Figure 9.** Window versus screen coordinates when content is letterboxed.
- When handling `MotionEvent`, use
  [`MotionEvent.getX()`](https://developer.android.com/reference/android/view/MotionEvent#getX()) and
  [`MotionEvent.getY()`](https://developer.android.com/reference/android/view/MotionEvent#getY()) to avoid
  similar coordinate issues. Don't use
  [`MotionEvent.getRawX()`](https://developer.android.com/reference/android/view/MotionEvent#getRawX()) or
  [`MotionEvent.getRawY()`](https://developer.android.com/reference/android/view/MotionEvent#getRawY()).

## Test how your content renders

Test all of your app's screens and experiences. Test on devices with different
types of cutouts, if possible. If you don't have a device with a cutout, you can
simulate common cutout configurations on any device or emulator running Android
9 or higher by doing the following:

1. Enable [**Developer options**](https://developer.android.com/studio/debug/dev-options).
2. In the **Developer options** screen, scroll down to the **Drawing** section and select **Simulate a display with a cutout**.
3. Select the cutout type.

   ![An image showing how to simulate a display cutout in the emulator](https://developer.android.com/static/develop/ui/views/layout/display-cutout/images/cutout-example-1.png) **Figure 10.** Developer options to test how your content renders.

## Additional resources

- [LAYOUT_IN_DISPLAY_CUTOUT_MODE_ALWAYS](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#LAYOUT_IN_DISPLAY_CUTOUT_MODE_ALWAYS)
- [LAYOUT_IN_DISPLAY_CUTOUT_MODE_NEVER](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#LAYOUT_IN_DISPLAY_CUTOUT_MODE_NEVER)
- [LAYOUT_IN_DISPLAY_CUTOUT_MODE_SHORT_EDGES](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#LAYOUT_IN_DISPLAY_CUTOUT_MODE_SHORT_EDGES)
- [LAYOUT_IN_DISPLAY_CUTOUT_MODE_DEFAULT](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#LAYOUT_IN_DISPLAY_CUTOUT_MODE_DEFAULT)