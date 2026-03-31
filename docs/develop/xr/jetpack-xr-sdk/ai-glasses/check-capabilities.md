---
title: Check device capabilities at runtime for AI glasses  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/ai-glasses/check-capabilities
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Check device capabilities at runtime for AI glasses Stay organized with collections Save and categorize content based on your preferences.



Different types of AI glasses have different capabilities. After [planning how
you'll support different types of AI devices](/develop/xr/jetpack-xr-sdk/ai-glasses/support-different-types), you can check for device
capabilities at runtime to provide the best experience for a user's device.

## Check whether a device has a display

Some AI glasses have a display where your app can show [UIs built with Jetpack
Compose Glimmer](/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer). The following example shows how to check whether a glasses
device has a display:

```
// Check device capabilities
val projectedDeviceController = ProjectedDeviceController.create(this@GlassesMainActivity)
isVisualUiSupported = projectedDeviceController.capabilities.contains(CAPABILITY_VISUAL_UI)

GlassesMainActivity.kt
```

## React to display state changes

On AI glasses with a display, the display can time out or the user can turn off
the display. To design activities that run whether the display is on or off,
use [`addPresentationModeChangedListener`](/reference/kotlin/androidx/xr/projected/ProjectedDisplayController#addPresentationModeChangedListener(java.util.concurrent.Executor,java.util.function.Consumer)) to be notified when the display
state changes. You can tune your activity for the appropriate amount of
audio information depending on display state.

```
ProjectedDisplayController.create(activity).addPresentationModeChangedListener {
    presentationModeFlags ->

    val areVisualsOff = !presentationModeFlags.hasPresentationMode(VISUALS_ON)
}
```

## Keep the display on

On AI glasses with a display, you can request that the system keep the screen on
and prevent the screen from timing out using [`addLayoutParamsFlags`](/reference/kotlin/androidx/xr/projected/ProjectedDisplayController#addLayoutParamsFlags(kotlin.Int)).

**Note:** Keeping the device's screen on can drain the battery quickly. Ordinarily,
you should let the device turn the screen off if the user isn't interacting
with it. If you do need to keep the screen on, do so for as short a time as
possible.

```
var projectedDisplayController = ProjectedDisplayController.create(activity)

projectedDisplayController.addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON)
```

[Previous

arrow\_back

Plan to support different types of AI glasses](/develop/xr/jetpack-xr-sdk/ai-glasses/support-different-types)