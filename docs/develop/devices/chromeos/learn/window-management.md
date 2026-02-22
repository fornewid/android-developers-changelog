---
title: https://developer.android.com/develop/devices/chromeos/learn/window-management
url: https://developer.android.com/develop/devices/chromeos/learn/window-management
source: md.txt
---

ChromeOS supports Android apps in multiple windows. The system renders apps
into window containers whose size is determined by the form factor of the
device, as shown in figure 1.
![An app window on different devices.](https://developer.android.com/static/images/develop/chromeos/fullscreen_and_windows.png) **Figure 1.**: Caption goes here.

**Figure 1.** An app window on different devices.

It is important to design layouts that work with different screen sizes. If you
follow the Android guidelines to [support different screen
sizes](https://developer.android.com/training/multiscreen/screensizes), then your app also works well
when running on ChromeOS.

This page shows how to help your app's window launch correctly, resizes
smoothly, and displays all of its contents when its size changes.
| **Note:** In addition to window management, Android apps that run on ChromeOS pose lifecycle management challenges. There are also other issues to consider, such as multiple apps competing for exclusive resources like the camera or microphone and the possibility that a visible app is not necessarily the active app. Read [Multi-window support](https://developer.android.com/guide/topics/ui/multi-window) for information on how to handle these issues.

## Initial launch size

Apps can request their initial launch size in the following ways:

- Use a launch size only in desktop environments.
  This helps the window manager to give you the proper bounds and
  orientation. To indicate a preferences when used in desktop mode, add
  the following meta tags inside the
  [`<activity>`](https://developer.android.com/guide/topics/manifest/activity-elemen):

      &lt;meta-data android:name=&#34;WindowManagerPreference:FreeformWindowSize&#34;
                 android:value=&#34;[phone|tablet|maximize]&#34; /&gt;
      &lt;meta-data android:name=&#34;WindowManagerPreference:FreeformWindowOrientation&#34;
                 android:value=&#34;[portrait|landscape]&#34; /&gt;

- Use static launch bounds. Use `<layout>` inside the manifest entry of your
  activity to specify a "fixed" starting size, as in the following example:

      &lt;layout android:defaultHeight=&#34;500dp&#34;
                  android:defaultWidth=&#34;600dp&#34;
                  android:gravity=&#34;top|end&#34;
                  android:minHeight=&#34;450dp&#34;
                  android:minWidth=&#34;300dp&#34; /&gt;

- Use dynamic launch bounds. An activity can create and use
  `ActivityOptions.setLaunchBounds(Rect)` when creating a new activity. By
  specifying an empty rectangle, your app can be maximized.

| **Note:** These options work only if the activity started is a root activity. You can also do this using a springboard activity to clear the activity stack in the task with a new start.

## Resize windows

In ChromeOS, users can resize an app's window in the usual way: by dragging
the lower-right corner, as shown in figure 2.
![](https://developer.android.com/static/images/develop/chromeos/resizable.png) **Figure 2.**: Caption goes here.

**Figure 2.** A resizable app window.

There are two options for handling window resizing when using the
`View` class:

- Respond to configuration changes dynamically by calling `onConfigurationChanged(..)`. As an example, you can add `android:configChanges="screenSize|smallestScreenSize|orientation|screenLayout"` to the activity's manifest. For more information about handling configuration changes, read [Handling configuration changes](https://developer.android.com/guide/topics/resources/runtime-changes).
- Let the system restart the activity. In this case, implement `onSaveInstanceState` and use the [ViewModel architecture
  component](https://developer.android.com/topic/libraries/architecture/viewmodel) to restore the previous saved state.

When using [Jetpack Compose](https://developer.android.com/jetpack/compose), the resizing behavior depends on
how your activity is configured. If it handles changes dynamically, a
recomposition is triggered when the window size changes. If the activity is
restarted by the system, an initial composition occurs after the restart. Either
way, it's important to create Compose layouts that adapt to changing window
sizes. Don't assume fixed sizes.
| **Note:** To learn more about configuration changes, how to restrict Activity recreation if needed, and how to react to those configuration changes from the View system and Jetpack Compose, check out the [Handle configuration changes](https://developer.android.com/guide/topics/resources/runtime-changes) page.

## Window dimensions

Have your activities read their window dimensions every time they start and
arrange their contents according to the current configuration.

To determine the current configuration, call `getResources().getConfiguration()`
on the current activity. Don't use the
configuration of the background activity or the system resource.
The background activity doesn't have a size, and the system configuration might
contain multiple windows with conflicting sizes and orientations, so no usable
data can be extracted.

Note that the *window* size and the *screen* size are not the same. To get the
window size in DP, use `Activity.getResources().getConfiguration().screenWidth`
and `Activity.getResources().getConfiguration().screenHeight`. You probably
never need to use the screen size.

### Content bounds

A window's content bounds can change after resizing. For example, the area
within the window that is used by the app can change if the window becomes too
big to fit on the screen. Follow these guidelines:

- Apps that use Android's layout process are automatically laid out in the available space.
- Native apps need to read the available area and monitor size changes to
  avoid having inaccessible UI elements. Call the following methods to
  determine the initial available size for this surface:

  - `NativeActivity.mLastContent[X/Y/Width/Height]()`
  - `findViewById(android.R.id.content).get[Width/Height]()`

  Continuous monitoring can be done using an observer:
  - `NativeActivity.onContentRectChangedNative()`
  - `NativeActivity.onGlobalLayout()`
  - Add a listener to `view.addOnLayoutChangeListener(findViewById(android.R.id.content))`

  If the app is pre-scaling its artwork, do so every time the resolution
  changes.

### Free-form resizing

ChromeOS lets any window be freely resized: the user can change a window's
width, height, and position on the screen. Many Android apps are written without
free-form resizing in mind. Consider these issues:

- The screen position might change. Always use the system to perform window-to-screen and screen-to-window coordinate transformations.
- If you are using Android's view system, your window layout automatically changes when its size changes.
- If you don't use the view system and take over the surface, your app must handle size changes on its own.
- For native apps, use the `mLastContent` members or use the content view to determine the initial size.
- When the app is running, listen to `onContentRectChangedNative` or `onGlobalLayout` events to react to size changes.
- When the app's size changes, rescale or reload layouts and artwork and update input areas.

### Full screen mode

Full screen mode works the same as on stock Android.
If the window is not covering the full screen, requests for full screening
(hiding all system UI elements) are ignored. When the app is maximized
the normal fullscreen methods, layouts, and functions are performed.
This hides the system UI elements (window control bar and the shelf).

## Screen orientation

The most common orientation for an Android app is portrait, since that's how
most phones are held. While portrait is good for phones, it's terrible for
laptops and tablets, where landscape is preferred. To get
the best results for your app, consider supporting both orientations.

Some Android apps assume that when a device is held in the portrait mode, the
rotation value is
[`Surface.ROTATION_0`](https://developer.android.com/reference/android/view/Surface#ROTATION_0).
This might be true for most Android devices. However, when the app is in a
certain
[ARC](https://developer.chrome.com/apps/getstarted_arc) mode,
the rotation value for the portrait orientation might not be
`Surface.ROTATION_0`.

To get an accurate rotation value while reading the accelerometer or similar
sensors, use the [`Display.getRotation()`](https://developer.android.com/reference/android/view/Display#getRotation())
method and swap the axis accordingly.

### The root activity and orientation

A Chromebook window consists of a stack of activity windows. Each window
in the stack has the same size and orientation.

Sudden orientation and size changes are confusing in a desktop
environment. The Chromebook window manager avoids this in a way that's similar
to Android's side-by-side mode: the activity at the bottom of the stack controls
the attributes of all the activities above it. This can lead to unexpected
situations where a newly started activity that is portrait and unresizable
becomes landscape and resizable.

Device mode has an effect here: in tablet mode, the orientation is not locked,
and each window preserves its own orientation, as is normal on Android.

### Orientation guidelines

Follow these guidelines for handling orientation:

- If you support only one orientation, add the information to the manifest so the window manager knows about it before starting the application. When you specify the orientation, also specify the sensor orientations when possible. Chromebooks are often convertibles, and an upside-down app is a bad user experience.
- Try to stay with a single selected orientation. Avoid requesting one orientation in the manifest and setting another programmatically later.
- Be careful changing the orientation based on window size. The user might get stuck in a small portrait-size window and not be able to return to a larger landscape window.
- There are window controls in Chrome to toggle between all available layouts. By choosing the correct orientation option, you can ensure that the user has the correct layout after launching the app. If an app is available in portrait and landscape, make it default to landscape, if possible. After this option is set, it is remembered on a per-app basis.
- Try to avoid unnecessary orientation changes. For example, if the activity orientation is portrait, but the app calls `setRequestedOrientation(LANDSCAPE)` at runtime, this causes unnecessary window resizing, which is annoying to the user and might restart the app the app can't handle it. It's better to set the orientation once, for example, in the manifest, and only change it if necessary.

## Other considerations

Here are some other things to consider when working with Android apps in
ChromeOS:

- Don'''t call `finish()` in your activity's `onDestroy` method. This causes the app to close upon resize and not restart.
- Don't use window types that aren't compatible, such as `TYPE_KEYGUARD` and `TYPE_APPLICATION_MEDIA`.
- Make activity restarts fast by caching objects that have been previously allocated.
- If you don't want the user to resize your app, specify `android:resizeableActivity=false` in your manifest file.
- Test your app to ensure that it handles changes in window size appropriately.