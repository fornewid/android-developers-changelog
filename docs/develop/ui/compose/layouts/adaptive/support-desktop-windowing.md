---
title: https://developer.android.com/develop/ui/compose/layouts/adaptive/support-desktop-windowing
url: https://developer.android.com/develop/ui/compose/layouts/adaptive/support-desktop-windowing
source: md.txt
---

Desktop windowing enables users to run multiple apps simultaneously in resizable
app windows for a versatile, desktop-like experience.

In figure 1, you can see the organization of the screen with desktop windowing
enabled. Things to note:

- Users can run multiple apps side by side simultaneously.
- Taskbar is in a fixed position at the bottom of the display showing the running apps. Users can pin apps for quick access.
- New customizable header bar decorates the top of each window with controls such as minimize and maximize.

![](https://developer.android.com/static/develop/ui/compose/images/layouts/adaptive/desktop-windowing/desktop-windowing.png) **Figure 1.** Desktop windowing on a tablet.

By default, apps open full screen on Android tablets.
To launch an app in desktop windowing, press and hold the window handle at the
top of the screen and drag the handle within the UI, as seen in figure 2.

When an app is open in desktop windowing, other apps open in desktop windows as
well.
Your browser doesn't support the video tag. **Figure 2.** Press, hold, and drag the app window handle to enter desktop windowing.

Users can also invoke desktop windowing from the menu that shows up below the
window handle when you tap or click the handle or use the keyboard shortcut
<kbd>Meta key (Windows, Command, or Search) + Ctrl + Down</kbd>.

Users exit desktop windowing by closing all active windows or by grabbing
the window handle at the top of a desktop window and dragging the app to the top
of the screen. The <kbd>Meta + H</kbd> keyboard shortcut also exits
desktop windowing and runs apps full screen again.

To return to desktop windowing, tap or click the desktop space tile in the
Recents screen.
| **Note:** Desktop windowing is available starting from Android 15 QPR1 as a developer preview for Pixel Tablet (and emulator). Other premium tablets and foldable phones are expected to support the feature in following releases.

## Resizability and compatibility mode

In desktop windowing, apps with locked orientation are freely resizable.
That means even if an activity is
[locked to portrait orientation](https://developer.android.com/guide/topics/manifest/activity-element#screen),
users can still resize the app to a landscape orientation window.
Your browser doesn't support the video tag. **Figure 3.** Resizing the window of a portrait-restricted app to landscape.

Apps declared as nonresizable (that is,
[`resizeableActivity = false`](https://developer.android.com/guide/topics/manifest/activity-element#resizeableActivity))
have their UI scaled while keeping the same aspect ratio.
Your browser doesn't support the video tag. **Figure 4.** The UI of a nonresizable app scales as the window resizes.

Camera apps that lock the orientation or are declared as nonresizable have a
special treatment for their camera viewfinders: the window is fully resizable,
but the viewfinder keeps the same aspect ratio. By assuming apps
always run in portrait or landscape, the apps hardcode or otherwise make
assumptions that lead to miscalculations of the preview or captured image
orientation or aspect ratio resulting in stretched, sideways, or upside-down images.

Until apps are ready to implement fully responsive camera viewfinders, the
special treatment provides a more basic user experience that mitigates the
effects wrong assumptions may cause.

To learn more about compatibility mode for camera apps, see
[Device compatibility mode](https://developer.android.com/guide/practices/device-compatibility-mode#camera_preview).
Your browser doesn't support the video tag. **Figure 5.** Camera viewfinder retains its aspect ratio as the window resizes.

## Customizable header insets

All apps running in desktop windowing have a header bar, even in
[immersive mode](https://developer.android.com/develop/ui/views/layout/immersive).   

Ensure your app's content isn't obscured by the header bar.
The header bar is a caption bar inset type:
[`androidx.compose.foundation.layout.WindowInsets.Companion.captionBar()`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#(androidx.compose.foundation.layout.WindowInsets.Companion).captionBar());
in views, [`WindowInsets.Type.captionBar()`](https://developer.android.com/reference/android/view/WindowInsets.Type#captionBar()),
which is part of the system bars.

You can learn more about handling insets in [Display content edge-to-edge in your app and handle window insets in Compose](https://developer.android.com/develop/ui/compose/layouts/insets).

The header bar is also customizable. Android 15 introduced the appearance type
[`APPEARANCE_TRANSPARENT_CAPTION_BAR_BACKGROUND`](https://developer.android.com/reference/kotlin/android/view/WindowInsetsController#appearance_transparent_caption_bar_background) to make
the header bar transparent to allow apps to draw custom content inside
the header bar.

Apps then become responsible for styling the top portion of their content to
look like the caption bar (background, custom content, and so forth) with the
exception of the system caption elements (close and maximize buttons), which are
drawn by the system on the transparent caption bar on top of the app.

Apps can toggle the appearance of the system elements inside the caption for
light and dark themes using [`APPEARANCE_LIGHT_CAPTION_BARS`](https://developer.android.com/reference/kotlin/android/view/WindowInsetsController#appearance_light_caption_bars),
similar to how the status bar and navbar are toggled.

Android 15 also introduced the
[`WindowInsets#getBoundingRects()`](https://developer.android.com/reference/kotlin/android/view/WindowInsets#getboundingrects)
method which enables apps to introspect caption bar insets in more detail.
Apps can differentiate between areas where the system draws system elements and
unutilized areas where apps can place custom content without overlapping system elements.

The list of [`Rect`](https://developer.android.com/reference/kotlin/android/graphics/Rect)
objects returned by the API indicates system regions that
should be avoided. Any remaining space (calculated by subtracting the rectangles
from the caption bar Insets) is where the app can draw without
overlapping system elements and with the ability to receive input.
![Chrome before and after implementing custom headers.](https://developer.android.com/static/develop/ui/compose/images/layouts/adaptive/desktop-windowing/chrome-custom-headers-before-after.png) **Figure 6.** Chrome before and after implementing custom headers. **Note:** By default, input within the caption bar region is handled by the system for its own elements (for example the close button) or to start a drag operation of the desktop window. Apps that customize their app header can request priority input handling for their app UI inside the customizable region by using the [`setSystemGestureExclusionRects()`](https://developer.android.com/reference/kotlin/android/view/View#setsystemgestureexclusionrects) API.

## Multitasking and multi-instance support

Multitasking is at the core of desktop windowing, and allowing multiple
instances of your app can highly increase users productivity.

Android 15 introduces [PROPERTY_SUPPORTS_MULTI_INSTANCE_SYSTEM_UI](https://developer.android.com/reference/android/view/WindowManager#PROPERTY_SUPPORTS_MULTI_INSTANCE_SYSTEM_UI),
which apps can set to specify that system UI should be shown for the app to
allow it to be launched as multiple instances.
| **Note:** In desktop windowing and other multi-window environments, new tasks open in a new window, so double-check the user journey any time your app starts multiple tasks.

## Manage app instances with dragging gestures

In multi-window mode, users can start a new app instance by dragging a view
element out of the app's window.
Users can also move elements between instances of the same app.
Your browser doesn't support the video tag. **Figure 7.** Start a new instance of Chrome by dragging a tab out of the desktop window.

Android 15 introduces two flags to customize drag and drop behavior:

- [`DRAG_FLAG_START_INTENT_SENDER_ON_UNHANDLED_DRAG`](https://developer.android.com/reference/kotlin/android/view/View#drag_flag_start_intent_sender_on_unhandled_drag):
  Indicates that an unhandled drag should be delegated to the system to be started
  if no visible window handles the drop.
  When using this flag, the caller must provide
  [`ClipData`](https://developer.android.com/reference/kotlin/android/content/ClipData) with an
  [`Item`](https://developer.android.com/reference/kotlin/android/content/ClipData.Item) that contains an
  immutable [`IntentSender`](https://developer.android.com/reference/kotlin/android/content/IntentSender) to an
  activity to be launched
  (see [`ClipData.Item.Builder#setIntentSender()`](https://developer.android.com/reference/kotlin/android/content/ClipData.Item.Builder#setintentsender)).
  The system can launch the intent or not based on factors like the current screen
  size or windowing mode. If the system does not launch the intent, the intent is
  canceled by means of the normal drag and drop flow.

- [`DRAG_FLAG_GLOBAL_SAME_APPLICATION`](https://developer.android.com/reference/kotlin/android/view/View#drag_flag_global_same_application):
  Indicates that a drag operation can cross window boundaries (for multiple instances of the same application).

  When [`startDragAndDrop()`](https://developer.android.com/reference/kotlin/android/view/View#startdraganddrop)
  is called with this flag set, only visible windows belonging to the same
  application are able to participate in the drag operation and receive the dragged content.

Your browser doesn't support the video tag. **Figure 8.** Move a tab between two instances of the Chrome app.

## Additional optimizations

Customize app launches and transition apps from desktop windowing to full screen.

### Specify default size and position

Not all apps, even if resizable, need a large window to offer user value.
You can use the [`ActivityOptions#setLaunchBounds()`](https://developer.android.com/reference/kotlin/android/app/ActivityOptions#setlaunchbounds)
method to specify a default size and position when an activity is launched.

### Enter full-screen from the desktop space

Apps can go full-screen by calling [`Activity#requestFullScreenMode()`](https://developer.android.com/reference/kotlin/android/app/Activity#requestfullscreenmode).
The method displays the app full screen directly from desktop windowing.