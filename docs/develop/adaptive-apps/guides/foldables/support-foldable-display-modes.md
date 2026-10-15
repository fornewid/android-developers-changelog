---
title: Support foldable display modes  |  Adaptive Apps  |  Android Developers
url: https://developer.android.com/develop/adaptive-apps/guides/foldables/support-foldable-display-modes
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Adaptive Apps](https://developer.android.com/develop/adaptive-apps)
* [Guides](https://developer.android.com/develop/adaptive-apps/guides/get-started-with-adaptive-apps)

# Support foldable display modes Stay organized with collections Save and categorize content based on your preferences.





Foldable devices offer unique viewing experiences. Rear display mode and
dual‑screen mode enable you to build special display features for foldable
devices such as rear‑camera selfie preview and simultaneous but different
displays on inner and outer screens.

## Rear display mode

Typically when a foldable device is unfolded, only the inner screen is active.
Rear display mode lets you move an activity to the outer screen of a foldable
device, which usually faces away from the user while the device is unfolded. The
inner display automatically turns off.

A novel application is to display the camera preview on the outer screen, so
users can take selfies with the rear camera, which usually provides much better
picture‑taking performance than the front camera.

To activate rear display mode, users respond to a dialog to allow the app to
switch screens, for example:

![](/static/develop/ui/compose/images/layouts/adaptive/foldables/rear-display-dialog.png)


**Figure 1.** System dialog to allow starting rear display mode.

The system creates the dialog, so no development on your part is required.
Different dialogs appear depending on the device state; for example, the system
directs users to unfold the device if the device is closed. You can't customize
the dialog, and it can vary on devices from different OEMs.

You can try out rear display mode with the Pixel Fold camera app. See a sample
implementation in the codelab [Optimize your camera app on foldable devices with
Jetpack WindowManager](/codelabs/android-camera-foldables).

## Dual-screen mode

Dual-screen mode lets you show content on both displays of a foldable at the
same time. Dual‑screen mode is available on Pixel Fold running Android 14
(API level 34) or higher.

An example use case is the dual-screen interpreter.

![](/static/develop/ui/compose/images/layouts/adaptive/foldables/dual-screen-interpreter.png)


**Figure 2.** Dual-screen interpreter showing different content on front and rear displays.

## Enable the modes programmatically

You can access rear display mode and dual‑screen mode through the [Jetpack
WindowManager](/jetpack/androidx/releases/window) APIs, starting from library version 1.2.0-beta03.

Add the WindowManager dependency to your app's module `build.gradle` file:

### Kotlin

```
dependencies {
    // Define window_version in your project's build configuration.
    implementation("androidx.window:window:$window_version")
}
```

### Groovy

```
dependencies {
    // TODO: Define window_version in your project's build configuration.
    implementation "androidx.window:window:$window_version"
}
```

The entry point is the [`WindowAreaController`](/reference/kotlin/androidx/window/area/WindowAreaController), which provides the
information and behavior related to moving windows between displays or between
display areas on a device. `WindowAreaController` lets you query the list of
available [`WindowAreaInfo`](/reference/kotlin/androidx/window/area/WindowAreaInfo) objects.

Use `WindowAreaInfo` to access the [`WindowAreaSession`](/reference/kotlin/androidx/window/area/WindowAreaSession), an interface that
represents an active window area feature. Use `WindowAreaSession` to determine
the availability of a specific [`WindowAreaCapability`](/reference/kotlin/androidx/window/area/WindowAreaCapability).

Each capability is related to a particular [`WindowAreaCapability.Operation`](/reference/kotlin/androidx/window/area/WindowAreaCapability.Operation).
In version 1.2.0-beta03, Jetpack WindowManager supports two kinds of operations:

* [`WindowAreaCapability.Operation.OPERATION_PRESENT_ON_AREA`](/reference/kotlin/androidx/window/area/WindowAreaCapability.Operation#OPERATION_PRESENT_ON_AREA()), which is
  used to start dual‑screen mode
* [`WindowAreaCapability.Operation.OPERATION_TRANSFER_ACTIVITY_TO_AREA`](/reference/kotlin/androidx/window/area/WindowAreaCapability.Operation#OPERATION_TRANSFER_ACTIVITY_TO_AREA()),
  which is used to start rear display mode

Here's an example of how to declare variables for rear display mode and
dual‑screen mode in your app's main activity:

### Kotlin

```
private lateinit var windowAreaController: WindowAreaController
private lateinit var displayExecutor: Executor
private var windowAreaSession: WindowAreaSession? = null
private var windowAreaInfo: WindowAreaInfo? = null
private var capabilityStatus: WindowAreaCapability.Status =
    WindowAreaCapability.Status.WINDOW_AREA_STATUS_UNSUPPORTED

private val dualScreenOperation = WindowAreaCapability.Operation.OPERATION_PRESENT_ON_AREA
private val rearDisplayOperation = WindowAreaCapability.Operation.OPERATION_TRANSFER_ACTIVITY_TO_AREA

SupportFoldableDisplayModes

.kt
```