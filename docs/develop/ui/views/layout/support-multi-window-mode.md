---
title: https://developer.android.com/develop/ui/views/layout/support-multi-window-mode
url: https://developer.android.com/develop/ui/views/layout/support-multi-window-mode
source: md.txt
---

Multi-window mode enables multiple apps to share the same screen simultaneously.
Apps can be side by side or one above the other (split-screen mode), one app in
a small window overlaying other apps (picture-in-picture mode), or individual
apps in separate movable, resizable windows (desktop windowing mode).
Your browser doesn't support the video tag. **Figure 1.** Display two apps side by side in split-screen mode.

For user instructions about how to access split‑screen mode on phones, go
to [See two apps at the same time on Pixel phone](https://support.google.com/pixelphone/answer/7444033?ref_topic=7084202&sjid=11184622767876814075-NA).

## Version-specific multi-window features

The multi-window user experience depends on the version of Android and type of device:

- **Android 7.0** (API level 24) introduced split-screen mode on small screen
  devices and picture-in-picture mode on select devices.

  - **Split-screen mode** fills the screen with two apps, showing them
    either side by side or one above the other. Users can drag the divider
    separating the two apps to make one app larger and the other smaller.

  - **Picture-in-picture mode** enables users to continue video playback
    while interacting with another app (see [Picture-in-picture support](https://developer.android.com/guide/topics/ui/picture-in-picture)).

  - **Desktop windowing mode**, in which users can freely resize each
    activity, can be enabled by manufacturers of large screen devices.

    You can configure how your app handles multi-window mode by specifying
    your activity's minimum allowable dimensions. You can also disable
    multi-window mode for your app by setting
    [`resizeableActivity="false"`](https://developer.android.com/guide/topics/manifest/application-element#resizeableActivity) to ensure the system always shows
    your app full screen.
- **Android 8.0** (API level 26) extends picture-in-picture mode to small
  screen devices.

- **Android 12** (API level 31) makes multi-window mode standard behavior.

  - **On large screens** ([medium](https://developer.android.com/develop/ui/views/layout/window-size-classes) or [expanded](https://developer.android.com/develop/ui/views/layout/window-size-classes) window size class), the
    platform supports all apps in multi-window mode regardless of app
    configuration. If `resizeableActivity="false"`, the app is put into
    compatibility mode when necessary to accommodate display dimensions.

  - **On small screens** ([compact](https://developer.android.com/develop/ui/views/layout/window-size-classes) window size class), the system checks
    an activity's [`minWidth`](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.WindowLayout#android:minwidth) and [`minHeight`](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.WindowLayout#android:minheight) to determine whether
    the activity can run in multi-window mode. If
    `resizeableActivity="false"`, the app is prevented from running in
    multi-window mode regardless of minimum width and height.

- **Android 16** (API level 36) overrides screen orientation, aspect ratio,
  and resizability restrictions.

  - **On large screens** (smallest width \>= 600dp) the system ignores
    manifest attributes and runtime APIs used to restrict an app's
    orientation, aspect ratio, and resizability, optimizing the user
    experience on all device form factors.

    To learn how to exclude games from the Android 16 changes, see
    [App orientation, aspect ratio, and resizability](https://developer.android.com/develop/ui/compose/layouts/adaptive/app-orientation-aspect-ratio-resizability#exceptions) exceptions.

> [!NOTE]
> **Note:** Device manufacturers can override these multi-window behaviors.

## Implementation strategies

Multi-window mode can be initiated multiple ways.

### Support user-initiated split-screen

1. Open the [Recents screen](https://developer.android.com/guide/components/recents)
2. Swipe an app into view
3. Press the app icon in the app's title bar
4. Select the **Split screen** menu option
5. Select another app from the Recents screen

Users exit split-screen mode by dragging the window divider to the edge of the
screen---up or down, left or right.

> [!NOTE]
> **Note:** Android 12L (API level 32) and higher enable users to activate split-screen mode from the Recents screen by selecting the **Split** action displayed below the active app when two or more apps are in Recents.

### Programmatic split-screen (launch adjacent)

If your app needs to launch another activity into an adjacent window, use the [`FLAG_ACTIVITY_LAUNCH_ADJACENT`](https://developer.android.com/reference/kotlin/android/content/Intent#flag_activity_launch_adjacent) intent flag. On Android 12L (API level 32) and higher, the flag allows an app running full screen to enter split-screen mode and launch a target activity into the adjacent window.
`FLAG_ACTIVITY_LAUNCH_ADJACENT` was introduced in Android 7.0 (API level 24).

To launch an adjacent activity, use `FLAG_ACTIVITY_LAUNCH_ADJACENT` in
conjunction with [`FLAG_ACTIVITY_NEW_TASK`](https://developer.android.com/reference/kotlin/android/content/Intent#flag_activity_new_task), for example:

<br />

### Kotlin

    fun openUrlInAdjacentWindow(url: String) {
        Intent(Intent.ACTION_VIEW).apply { data = Uri.parse(url)
           addFlags(Intent.FLAG_ACTIVITY_LAUNCH_ADJACENT or Intent.FLAG_ACTIVITY_NEW_TASK)
        }.also { intent -> startActivity(intent) }
    }

### Java

    public void openUrlInAdjacentWindow(String url) {
        Intent intent = new Intent(Intent.ACTION_VIEW);
        intent.setData(Uri.parse(url));
        intent.addFlags(Intent.FLAG_ACTIVITY_LAUNCH_ADJACENT | Intent.FLAG_ACTIVITY_NEW_TASK);
        startActivity(intent);
    }

> [!NOTE]
> **Note:** OEMs can enable 12L behavior on older Android versions, in which case `FLAG_ACTIVITY_LAUNCH_ADJACENT` functions as it does on API level 32.

### Activity embedding (split activities in the same task)

Activity embedding enables apps composed of multiple activities to split activities *within the same app task* , such as for a [list‑detail](https://developer.android.com/develop/ui/compose/layouts/adaptive/canonical-layouts#list-detail) layout on large screens. Activity embedding, part of [Jetpack WindowManager](https://developer.android.com/reference/androidx/window/embedding/package-summary), lets you define configuration rules (such as split-pair rules) using XML or API calls that determine whether activities are displayed side by side or stacked. For full details, see [Activity embedding](https://developer.android.com/develop/ui/views/layout/activity-embedding).

## Activity lifecycle in multi-window mode

Multi-window mode does not change the [activity lifecycle](https://developer.android.com/training/basics/activity-lifecycle). However, the
resumed state of apps in multiple windows differs on different versions of
Android.

### Multi-resume

Android 10 (API level 29) and higher versions support multi-resume---all
activities remain in the [`RESUMED`](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State#RESUMED) state when the device is in multi-window
mode. An activity can be paused if a transparent activity is on top of the
activity or the activity is not focusable, for example, the activity is in
[picture-in-picture mode](https://developer.android.com/guide/topics/ui/picture-in-picture). It's also possible that no activity has focus at a
given time, for example, if the notification drawer is open. The [`onStop()`](https://developer.android.com/reference/kotlin/android/app/Activity#onstop)
method works as usual: the method is called any time an activity is taken off
the screen.

Multi-resume is also available on select devices running Android 9 (API level
28). To opt in to multi-resume on Android 9 devices, add the following manifest
metadata:

    <meta-data android:name="android.allow_multiple_resumed_activities" android:value="true" />

To verify that a given device supports this manifest metadata, refer to the
device specifications.

### Android 9

In multi-window mode on Android 9 (API level 28) and lower, only the activity
the user has most recently interacted with is active at a given time. This
activity is considered *topmost* , and is the only activity in the `RESUMED`
state. All other visible activities are [`STARTED`](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State#STARTED) but are not `RESUMED`.
However, the system gives these visible but not resumed activities higher
priority than activities that are not visible. If the user interacts with one of
the visible activities, that activity is resumed, and the previously topmost
activity enters the `STARTED` state.

When there are multiple activities within a single active app process, the
activity with the highest z-order is resumed, and the others are paused.

> [!NOTE]
> **Note:** In multi-window mode on Android 9 and lower versions, an app might not be in the `RESUMED` state even though it is visible to the user, but the app might need to continue its operation while it is not topmost. For example, a video app in this state should continue playing its video. For this reason, we recommend that activities that play video *not* pause video playback in response to the [`ON_PAUSE`](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.Event#ON_PAUSE) lifecycle event. Instead, the activity should begin playback in response to [`ON_START`](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.Event#ON_START), and pause playback in response to [`ON_STOP`](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.Event#ON_STOP). If you handle the lifecycle events directly instead of using the [Lifecycle](https://developer.android.com/topic/libraries/architecture/lifecycle) package, pause video playback in your [`onStop()`](https://developer.android.com/reference/kotlin/android/app/Activity#onstop) handler, and resume playback in [`onStart()`](https://developer.android.com/reference/kotlin/android/app/Activity#onStart()).

### Configuration changes

When the user puts an app into multi-window mode, the system notifies the
activity of a configuration change as specified in [Handle configuration
changes](https://developer.android.com/guide/topics/resources/runtime-changes). This also happens when the user resizes the app or puts the app back
into full screen mode.

Essentially, this change has the same activity lifecycle implications as when
the system notifies the app that the device has switched from portrait to
landscape orientation, except that the app dimensions are changed instead of
just being swapped. Your activity can handle the configuration change itself, or
your app can allow the system to destroy the activity and recreate it with the
new dimensions.

If the user is resizing a window and makes it larger in either dimension, the
system resizes the activity to match the user action and issues configuration
changes as needed. If the app lags behind in drawing in newly exposed areas, the
system temporarily fills those areas with the color specified by the
[`windowBackground`](https://developer.android.com/reference/kotlin/android/R.attr#windowbackground) attribute or by the default
[`windowBackgroundFallback`](https://developer.android.com/reference/kotlin/android/R.attr#windowbackgroundfallback) style attribute.

## Exclusive resource access

To help support the multi-resume feature, use the
[`onTopResumedActivityChanged()`](https://developer.android.com/reference/kotlin/android/app/Activity#ontopresumedactivitychanged) lifecycle callback.

The callback is invoked when an activity gains or loses the top resumed activity
position, which is important when an activity uses a shared singleton resource,
such as the microphone or camera:

<br />

### Kotlin

    override fun onTopResumedActivityChanged(topResumed: Boolean) {
        if (topResumed) {
            // Top resumed activity.
            // Can be a signal to re-acquire exclusive resources.
        } else {
            // No longer the top resumed activity.
        }
    }

### Java

    @Override
    public void onTopResumedActivityChanged(boolean topResumed) {
        if (topResumed) {
            // Top resumed activity.
            // Can be a signal to re-acquire exclusive resources.
        } else {
            // No longer the top resumed activity.
        }
    }

Note that an app can lose resources for other reasons, such as removal of a
shared piece of hardware.

In any case, an app should gracefully handle events and state changes that
affect available resources.

For apps that use a camera,
[`CameraManager.AvailabilityCallback#onCameraAccessPrioritiesChanged()`](https://developer.android.com/reference/kotlin/android/hardware/camera2/CameraManager.AvailabilityCallback#oncameraaccessprioritieschanged)
provides a hint that it might be a good time to try to get access to the camera.
This method is available as of Android 10 (API level 29).

Remember that `resizeableActivity=false` is not a guarantee of exclusive camera
access, since other apps that use the camera can be opened on other displays.
:camera: **Figure 2.** Camera in multi-window mode.

Your app does not necessary have to release the camera when the app loses focus.
For example, you might want to continue camera preview while the user interacts
with the newly focused topmost resumed app. It's fine for your app to keep
running the camera when it's not the topmost resumed app, but it has to handle
the disconnect case properly. When the topmost resumed app wants to use the
camera, it can open it, and your app will lose access. Your app can reopen the
camera when the app gets the focus back.

After an app receives a [`CameraDevice.StateCallback#onDisconnected()`](https://developer.android.com/reference/kotlin/android/hardware/camera2/CameraDevice.StateCallback#ondisconnected)
callback, subsequent calls on the camera device will throw a
[`CameraAccessException`](https://developer.android.com/reference/kotlin/android/hardware/camera2/CameraAccessException).

## Window metrics

Android 11 (API level 30) introduced the following [`WindowManager`](https://developer.android.com/reference/kotlin/android/view/WindowManager) methods
to provide the bounds of apps running in multi-window mode:

- [`getCurrentWindowMetrics()`](https://developer.android.com/reference/kotlin/android/view/WindowManager#getcurrentwindowmetrics): Returns a [`WindowMetrics`](https://developer.android.com/reference/kotlin/android/view/WindowMetrics) object for the current windowing state of the system.
- [`getMaximumWindowMetrics()`](https://developer.android.com/reference/kotlin/android/view/WindowManager#getmaximumwindowmetrics): returns `WindowMetrics` for the largest potential windowing state of the system.

The Jetpack WindowManager library methods [`computeCurrentWindowMetrics()`](https://developer.android.com/reference/kotlin/androidx/window/layout/WindowMetricsCalculator#computeCurrentWindowMetrics(android.app.Activity))
and [`computeMaximumWindowMetrics()`](https://developer.android.com/reference/kotlin/androidx/window/layout/WindowMetricsCalculator#computeMaximumWindowMetrics(android.app.Activity)) offer similar functionality
respectively, but with backward compatibility to API level 14.

To obtain metrics for displays other than the current display, do the following
(as shown in the code snippet):

- Create a display context
- Create a window context for the display
- Get the `WindowManager` of the window context
- Get the `WindowMetrics` of the maximum display area available to the app

<br />

### Kotlin

    val windowMetrics = context.createDisplayContext(display)
                               .createWindowContext(WindowManager.LayoutParams.TYPE_APPLICATION, null)
                               .getSystemService(WindowManager::class.java)
                               .maximumWindowMetrics

### Java

    WindowMetrics windowMetrics = context.createDisplayContext(display)
                                         .createWindowContext(WindowManager.LayoutParams.TYPE_APPLICATION, null)
                                         .getSystemService(WindowManager.class)
                                         .getMaximumWindowMetrics();

### Deprecated methods

[`Display`](https://developer.android.com/reference/kotlin/android/view/Display) methods [`getSize()`](https://developer.android.com/reference/kotlin/android/view/Display#getsize) and [`getMetrics()`](https://developer.android.com/reference/kotlin/android/view/Display#getmetrics) were deprecated in
API level 30 in favor of the new `WindowManager` methods.

Android 12 (API level 31) deprecates `Display` methods [`getRealSize()`](https://developer.android.com/reference/kotlin/android/view/Display#getrealsize) and
[`getRealMetrics()`](https://developer.android.com/reference/kotlin/android/view/Display#getrealmetrics) and updates their behavior to more closely match the
behavior of `getMaximumWindowMetrics()`.

> [!NOTE]
> **Note:** Use [`Configuration#densityDpi`](https://developer.android.com/reference/kotlin/android/content/res/Configuration#densitydpi) instead of `getMetrics()` or `getRealMetrics()` to get the display density.

## Multi-window mode configuration

If your app targets Android 7.0 (API level 24) or higher, you can configure how
and whether your app's activities support multi-window mode. You can set
attributes in your manifest to control both size and layout. A root activity's
attribute settings apply to all activities within its task stack. For example,
if the root activity has `android:resizeableActivity="true"`, then all
activities in the task stack are resizable. On some larger devices, such as
Chromebooks, your app might run in a resizable window even if you specify
`android:resizeableActivity="false"`. If this breaks your app, you can use
[filters on Google Play](https://developer.android.com/google/play/filters) to restrict your app's availability on such devices.

> [!NOTE]
> **Note:** If you build a multi-orientation app that targets API level 23 or lower, and the user uses the app in multi-window mode, the system forcibly resizes the app. The system presents a dialog warning the user that the app might behave unexpectedly. The system does *not* resize fixed-orientation apps; if the user attempts to open a fixed-orientation app under multi-window mode, the app takes over the whole screen.

Android 12 (API level 31) defaults to multi-window mode. On large screens
([medium](https://developer.android.com/develop/ui/views/layout/window-size-classes) or [expanded](https://developer.android.com/develop/ui/views/layout/window-size-classes) window size class), all apps run in multi-window
mode regardless of app configuration. On small screens, the system checks an
activity's [`minWidth`](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.WindowLayout#android:minwidth), [`minHeight`](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.WindowLayout#android:minheight), and [`resizeableActivity`](https://developer.android.com/guide/topics/manifest/application-element#resizeableActivity)
settings to determine whether the activity can run in multi-window mode.

### `resizeableActivity`

Set this attribute in your manifest's [`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element) or [`<application>`](https://developer.android.com/guide/topics/manifest/application-element)
element to enable or disable multi-window mode for API level 30 and lower:

    <application
      android:name=".MyActivity"
      android:resizeableActivity=["true" | "false"] />;

If this attribute is set to `true`, the activity can be launched in split-screen
and desktop windowing modes. If the attribute is set to `false`, the activity
does not support multi-window mode. If the value is false, and the user
attempts to launch the activity in multi-window mode, the activity takes over
the full screen.

If your app targets API level 24 or higher, but you don't specify a value for
this attribute, the attribute's value defaults to true.

If your app targets API level 31 or higher, this attribute works differently on
small and large screens:

- **Large screens** ([medium](https://developer.android.com/develop/ui/views/layout/window-size-classes) or [expanded](https://developer.android.com/develop/ui/views/layout/window-size-classes) window size class): All apps support multi-window mode. The attribute indicates whether an activity can be resized. If `resizeableActivity="false"`, the app is put into compatibility mode when necessary to conform to display dimensions.
- **Small screens** ([compact](https://developer.android.com/develop/ui/views/layout/window-size-classes) window size class): If `resizeableActivity="true"` and activity minimum width and minimum height are within the multi-window requirements, the activity supports multi-window mode. If `resizeableActivity="false"`, the activity does not support multi-window mode regardless of activity minimum width and height.

If your app targets API level 36 or higher, this attribute is ignored on
displays having smallest width \>= 600dp. However, the app fully respects the
user's choice of aspect ratio (see [User per-app overrides](https://developer.android.com/guide/practices/device-compatibility-mode#user_per-app_overrides)).

If you're building a game, see [App orientation, aspect ratio, and
resizability](https://developer.android.com/develop/ui/compose/layouts/adaptive/app-orientation-aspect-ratio-resizability#exceptions) to learn how you can exclude your game from the Android 16 (API
level 36) changes.

### `supportsPictureInPicture`

Set this attribute in your manifest's [`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element) node to indicate whether
the activity supports picture-in-picture mode.

    <activity
      android:name=".MyActivity"
      android:supportsPictureInPicture=["true" | "false"] />

> [!NOTE]
> **Note:** If `supportsPictureInPicture="true"`, you must set the `android:configChanges` attribute to enable your activity to handle configuration changes. See [Add videos using picture-in-picture (PiP)](https://developer.android.com/training/tv/playback/picture-in-picture).

### `configChanges`

To handle multi-window configuration changes yourself, such as when a user
resizes a window, add the [`android:configChanges`](https://developer.android.com/reference/kotlin/android/R.attr#configchanges) attribute to your app
manifest [`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element) node with at least the following values:

    <activity
      android:name=".MyActivity"
      android:configChanges="screenSize | smallestScreenSize
          | screenLayout | orientation" />

After adding `android:configChanges`, your activity and fragments receive a
callback to [`onConfigurationChanged()`](https://developer.android.com/reference/kotlin/android/app/Activity#onconfigurationchanged) instead of being destroyed and
recreated. You can then manually update your views, reload resources, and
perform other operations as needed.

### `<layout>`

On Android 7.0 (API level 24) and higher, the [`<layout>`](https://developer.android.com/guide/topics/manifest/layout-element) manifest element
supports several attributes that affect how an activity behaves in multi-window
mode:

- `android:defaultHeight`, `android:defaultWidth`: Default height and width of
  the activity when launched in desktop windowing mode.

- `android:gravity`: Initial placement of the activity when launched in
  desktop windowing mode. See the [`Gravity`](https://developer.android.com/reference/kotlin/android/view/Gravity) class for suitable values.

- `android:minHeight`, `android:minWidth`: Minimum height and minimum width
  for the activity in both split-screen and desktop windowing modes. If the
  user moves the divider in split-screen mode to make an activity smaller
  than the specified minimum, the system crops the activity to the size the
  user requests.

The following code shows how to specify an activity's default size and location
and its minimum size when the activity is displayed in desktop windowing mode:

    <activity android:name=".MyActivity">
        <layout android:defaultHeight="500dp"
              android:defaultWidth="600dp"
              android:gravity="top|end|..."
              android:minHeight="450dp"
              android:minWidth="300dp" />
    </activity>

## Multi-window mode at runtime

Beginning with Android 7.0, the system offers functionality to support apps that
can run in multi-window mode.

### Disabled features in multi-window mode

In multi-window mode, Android might disable or ignore features that don't apply
to an activity that is sharing the device screen with other activities or apps.

Additionally, some system UI customization options are disabled. For example,
apps cannot hide the status bar if they are running in multi-window mode (see
[Control the system UI visibility](https://developer.android.com/training/system-ui)).

The system ignores changes to the [`android:screenOrientation`](https://developer.android.com/reference/kotlin/android/R.attr#screenorientation) attribute.

### Multi-window mode queries and callbacks

The [`Activity`](https://developer.android.com/reference/kotlin/android/app/Activity) class offers the following methods to support multi-window
mode:

- [`isInMultiWindowMode()`](https://developer.android.com/reference/kotlin/android/app/Activity#isinmultiwindowmode): Indicates whether the activity is in
  multi-window mode.

- [`isInPictureInPictureMode()`](https://developer.android.com/reference/kotlin/android/app/Activity#isinpictureinpicturemode): Indicates whether the activity is in
  picture-in-picture mode.

  > [!NOTE]
  > **Note:** Picture-in-picture mode is a special case of multi-window mode. If `myActivity.isInPictureInPictureMode()` returns `true`, then `myActivity.isInMultiWindowMode()` also returns `true`.

- [`onMultiWindowModeChanged()`](https://developer.android.com/reference/kotlin/android/app/Activity#onmultiwindowmodechanged): The system calls this method whenever the
  activity goes into or out of multi-window mode. The system passes the method
  a value of true if the activity is entering multi-window mode or false if
  the activity is leaving multi-window mode.

- [`onPictureInPictureModeChanged()`](https://developer.android.com/reference/kotlin/android/app/Activity#onpictureinpicturemodechanged): The system calls this method whenever
  the activity goes into or out of picture-in-picture mode. The system passes
  the method a value of true if the activity is entering picture-in-picture
  mode or false if the activity is leaving picture-in-picture mode.

The [`Fragment`](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment) class exposes versions of many of these methods; for example,
[`Fragment.onMultiWindowModeChanged()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onMultiWindowModeChanged(boolean)).

### Picture-in-picture mode

To put an activity in picture-in-picture mode, call
[`enterPictureInPictureMode()`](https://developer.android.com/reference/kotlin/android/app/Activity#enterpictureinpicturemode_1) This method has no effect if the device does
not support picture-in-picture mode. For more information, see [Add videos using
picture-in-picture (PiP)](https://developer.android.com/training/tv/playback/picture-in-picture).

### New activities in multi-window mode

When you launch a new activity, you can indicate that the new activity should be
displayed adjacent to the current one if possible. Use the intent flag
[`FLAG_ACTIVITY_LAUNCH_ADJACENT`](https://developer.android.com/reference/kotlin/android/content/Intent#flag_activity_launch_adjacent), which tells the system to try to create the
new activity in an adjacent window, so the two activities share the screen. The
system makes a best effort to do this, but it is not guaranteed to happen.

If a device is in desktop windowing mode and you are launching a new activity,
you can specify the new activity's dimensions and screen location by calling
[`ActivityOptions.setLaunchBounds()`](https://developer.android.com/reference/kotlin/android/app/ActivityOptions#setlaunchbounds). The method has no effect if the device
is not in multi-window mode.

On API level 30 and lower, if you launch an activity within a task stack, the
activity replaces the activity on the screen, inheriting all of its multi-window
properties. If you want to launch the new activity as a separate window in
multi-window mode, you must launch it in a new task stack.

Android 12 (API level 31) enables apps to split an application's task window
among multiple activities. You determine how your app displays its
activities---full screen, side by side, or stacked---by creating an XML
configuration file or making Jetpack WindowManager API calls.

### Drag and drop

Users can drag and drop data from one activity to another while the two
activities are sharing the screen. (Prior to Android 7.0, users could only drag
and drop data within a single activity.) To quickly add support for accepting
dropped content see the [`DropHelper`](https://developer.android.com/reference/kotlin/androidx/draganddrop/DropHelper) API. For comprehensive drag-and-drop
guidance, see [Enable drag and drop](https://developer.android.com/guide/topics/ui/drag-drop).

## Multi-instance

Each root activity has its own task, which is displayed in its own window. To
launch a new instance of your app in a separate window, start new activities
with the `FLAG_ACTIVITY_NEW_TASK` flag. You can combine this setting with
[multi-window attributes](https://developer.android.com/develop/ui/views/layout/support-multi-window-mode#launch) to request a specific location for the new
window. For example, a shopping app can display multiple adjacent windows to
compare products.

Android 12 (API level 31) and higher enable you to launch two instances of an
activity side by side in the *same* task window in [activity embedding](https://developer.android.com/develop/ui/views/layout/activity-embedding).

If you want to allow users to start another instance of your application from
the application launcher or the taskbar, set `android:resizeableActivity="true"`
in your launcher activity's manifest and don't use a [launch mode](https://developer.android.com/guide/topics/manifest/activity-element#lmode) that
prevents multiple instances. For example, a `singleInstancePerTask` activity can
be instantiated multiple times in different tasks when
[`FLAG_ACTIVITY_MULTIPLE_TASK`](https://developer.android.com/reference/kotlin/android/content/Intent#flag_activity_multiple_task) or [`FLAG_ACTIVITY_NEW_DOCUMENT`](https://developer.android.com/reference/kotlin/android/content/Intent#flag_activity_new_document) is set.

> [!NOTE]
> **Note:** The application launcher is a system dialog that displays a list of apps that satisfy a specified intent. Users can launch an app by selecting it from the list. See [Intent types](https://developer.android.com/guide/components/intents-filters#Types).

On Android 15 (API level 35) and higher,
[`PROPERTY_SUPPORTS_MULTI_INSTANCE_SYSTEM_UI`](https://developer.android.com/reference/kotlin/android/view/WindowManager#property_supports_multi_instance_system_ui) enables you to declare support
for multi‑instance. The property is an explicit signal for system UI to
expose controls to the user to create multiple instances of the app. The
property is independent of launch mode but should only be used when the launch
mode for an activity or application is compatible with the property, for
example, when the launch mode is not `singleInstance`.

When multiple instances of an app are running in separate windows on a foldable
device, one or more instances might be sent to the background if the device
posture changes. For example, assume a device is unfolded and has two app
instances running in separate windows on each side of the fold. If the device is
folded, one of the instances might be terminated instead of trying to fit the
windows for both instances on a smaller screen.

> [!CAUTION]
> **Caution:** Don't confuse multi-instance with a multi‑pane layout, such as a [list‑detail](https://developer.android.com/develop/ui/compose/layouts/adaptive/canonical-layouts#list-detail) presentation, which runs in a single window.

## Multi-window mode verification

Whether or not your app targets API level 24 or higher, you should verify how it
behaves in multi-window mode in case a user tries to launch it in multi-window
mode on a device running Android 7.0 or higher.

> [!CAUTION]
> **Caution:** Unity apps running on Unity Long Term Support (LTS) version 2018 or earlier lose focus and the app window turns black when the app is running full screen and split‑screen mode is activated. The app can be restored by focusing the app window. To eliminate the issue, upgrade your Unity app to LTS version 2019 or later.

### Test devices

Devices that run Android 7.0 (API level 24) or higher support multi-window mode.

### API level 23 or lower

When users attempt to use the app in multi-window mode, the system forcibly
resizes the app unless the app declares a fixed orientation.

If your app does not declare a fixed orientation, you should launch your app on
a device running Android 7.0 or higher and attempt to put the app in
split-screen mode. Verify that the user experience is acceptable when the app is
forcibly resized.

If the app declares a fixed orientation, you should attempt to put the app in
multi-window mode. Verify that when you do so, the app remains in full screen
mode.

### API levels 24 through 30

If your app targets API levels 24 through 30 and does not disable multi-window
support, verify the following behavior under both split-screen and desktop
windowing modes:

- Launch the app full screen, then switch to multi-window mode by
  long-pressing the **Recents** button. Verify that the app switches properly.

- Launch the app directly in multi-window mode and verify that the app
  launches properly. You can launch an app in multi-window mode by pressing
  the **Recents** button, then long-pressing the title bar of your app and
  dragging it to one of the highlighted areas on the screen.

- Resize your app in split-screen mode by dragging the screen divider. Verify
  that the app resizes without crashing and that necessary UI elements are
  visible.

- If you have specified minimum dimensions for your app, attempt to resize the
  app so that its window size is smaller than those dimensions. Verify that
  you can't resize the app to be smaller than the specified minimum
  dimensions.

- Through all tests, verify that your app's performance is acceptable. For
  example, verify that there is not too long a lag to update the UI after the
  app is resized.

### API level 31 or higher

If your app targets API level 31 or higher and the main activity's minimum width
and minimum height are less than or equal to the respective dimensions of the
available display area, verify all the behaviors listed for [API levels 24
through 30](https://developer.android.com/develop/ui/views/layout/support-multi-window-mode#test-mw).

> [!NOTE]
> **Note:** You can programmatically determine whether your app is in multi-window mode by checking the return value of [`Activity#isInMultiWindowMode()`](https://developer.android.com/reference/kotlin/android/app/Activity#isinmultiwindowmode).

#### Test checklist

To verify your app's performance in multi-window mode, try the following
operations. You should try these operations in both split-screen and desktop
windowing mode, except where otherwise noted.

- Enter and leave multi-window mode.

- Switch from your app to another app, and verify that the app behaves
  properly while it is visible but not active. For example, if your app is
  playing video, verify that the video continues to play while the user is
  interacting with another app.

- In split-screen mode, try moving the screen divider to make your app both
  larger and smaller. Try these operations in both side by side and one above
  the other configurations. Verify that the app does not crash, essential
  functionality is visible, and the resize operation doesn't take too long.

- Perform several resize operations in rapid succession. Verify that your app
  doesn't crash or leak memory. Android Studio's Memory Profiler provides
  information about your app's memory usage (see [Inspect your app's memory
  usage with Memory Profiler](https://developer.android.com/studio/profile/memory-profiler)).

- Use your app normally in a number of different window configurations, and
  verify that the app behaves properly. Verify that text is readable and that
  UI elements aren't too small to interact with.

### Multi-window support disabled

On API levels 24 through 30, if you disabled multi-window support by setting
`android:resizeableActivity="false"`, you should launch your app on a device
running Android 7.0 through 11 and attempt to put the app in split-screen and
desktop windowing modes. Verify that when you do so, the app remains in
full-screen mode.

## Additional resources

For further information about multi-window support in Android, see:

- Android [MultiWindowPlayground](https://github.com/android/views-widgets-samples/tree/main/MultiWindowPlayground) sample