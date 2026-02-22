---
title: Support trifolds and landscape foldables  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/layouts/adaptive/foldables/trifolds-and-landscape-foldables
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Support trifolds and landscape foldables Stay organized with collections Save and categorize content based on your preferences.




![A landscape foldable in closed and fully open postures next to a trifold in closed and fully open postures.](/static/develop/ui/compose/images/layouts/adaptive/foldables/dev_trifold_overview.png)

Developers often encounter unique difficulties when creating applications for
foldables—especially devices like the Samsung Trifold or the original Pixel
Fold, which opens in landscape format (rotation\_0 = landscape). Developer
mistakes include:

* Wrong assumptions about device orientation
* Overlooked use-cases
* Failure to recalculate or cache values across configuration changes

Specific device-related issues include:

* A mismatch in device natural orientation between the cover and inner displays
  (assumptions based on rotation\_0 = portrait), causing apps to fail on fold
  and unfold journeys
* Different screen densities and incorrect *density* config change handling
* Camera preview issues caused by camera sensor dependency on natural
  orientation

To deliver a high-quality user experience on foldable devices, focus on the
following critical areas:

* Determine the app's orientation based on the actual screen area the app
  occupies, not the device's physical orientation
* Update camera previews to manage device orientation and aspect ratios
  correctly, avoid sideways previews, and prevent stretched or cropped images
* Maintain app continuity during device folding or unfolding by either retaining
  the state with [`ViewModel`](/topic/libraries/architecture/viewmodel) or similar approaches, or manually handling
  screen density changes and orientation changes, which avoids app restarts or
  loss of state
* For apps utilizing motion sensors, adjust the coordinate system to align with
  the screen's current orientation and avoid assumptions based on rotation\_0 =
  portrait, guaranteeing precise user interactions

## Build adaptive

If your app is already [adaptive](/adaptive-apps) and adheres to the optimized level (Tier 2)
outlined in the [Large screen app quality](/docs/quality-guidelines/large-screen-app-quality) guidelines, the app should
function well on foldable devices. Otherwise, before double-checking the
specific details of trifold and landscape foldables, review the following
foundational Android adaptive development concepts.

### Adaptive layouts

Your UI must handle not just different screen sizes, but real-time changes in
aspect ratio, such as unfolding and entering multi-window or desktop windowing
modes. See [About adaptive layouts](/develop/ui/compose/layouts/adaptive) for further guidance on how to:

* Design and implement adaptive layouts
* Adjust your app's primary navigation based on window size
* Use window size classes to adapt your app's UI
* Simplify implementation of canonical layouts, such as list‑detail, using the
  Jetpack APIs

![App letterboxed on an open foldable, and the same app full screen with an adaptive layout on another open foldable.](/static/develop/ui/compose/images/layouts/adaptive/app_letterboxed_and_full_screen.png)


**Figure 1.** Difference between non-adaptive (letterboxed) and adaptive layouts.

### Window size classes

Foldable devices, including landscape foldables and trifolds, can shift between
compact, medium, and expanded window size classes instantly. Understanding and
implementing these classes ensures your app displays the correct navigation
components and content density for the current device state.

![Depiction of an app on devices sized to the compact, medium, and expanded window size classes.](/static/develop/ui/compose/images/layouts/adaptive/window-size-classes/window_size_classes_width.png)


**Figure 2.** Window size classes.

The following example uses the Material 3 adaptive library to determine how much
space the app has available by first invoking the
[`currentWindowAdaptiveInfo()`](/reference/kotlin/androidx/compose/material3/adaptive/package-summary#currentWindowAdaptiveInfo(kotlin.Boolean)) function, then using the corresponding
layouts for the three window size classes:

```
val adaptiveInfo = currentWindowAdaptiveInfo()
val windowSizeClass = adaptiveInfo.windowSizeClass

when {
  windowSizeClass.isWidthAtLeastBreakpoint(WIDTH_DP_EXPANDED_LOWER_BOUND) -> // Expanded
  windowSizeClass.isWidthAtLeastBreakpoint(WIDTH_DP_MEDIUM_LOWER_BOUND) -> // Medium
  else -> // Compact
}
```

For more information, see [Use window size classes](/develop/ui/compose/layouts/adaptive/use-window-size-classes).

### Large screen app quality

Adhering to **Tier 2 (Large screen optimized)** or **Tier 1 (Large screen
differentiated)** of the [Large screen app quality](/docs/quality-guidelines/large-screen-app-quality) guidelines ensures your
app provides a compelling user experience on trifold devices, landscape
foldables, and other large-screen devices. The guidelines cover critical checks
across multiple tier levels to go from adaptive ready to a differentiated
experience.

### Android 16 and higher

For apps targeting Android 16 (API level 36) and higher, the system ignores
orientation, resizability, and aspect ratio restrictions on displays with
smallest width >= 600dp. Apps fill the entire display window, regardless of
aspect ratio or a user's preferred orientation, and the [letterboxing](/guide/practices/device-compatibility-mode#letterboxing)
compatibility mode isn't used anymore.

## Special considerations

Trifolds and landscape foldables introduce unique hardware behaviors that
require specific handling, particularly regarding sensors, camera preview, and
configuration continuity (retaining state when folding, unfolding, or resizing).

### Camera preview

A common problem on landscape foldables or aspect ratio calculations (in
scenarios like multi-window, desktop windowing, or connected displays), is when
the camera preview appears stretched, sideways, cropped, or rotated.

#### Mismatched assumptions

This issue often happens on large screen and foldable devices because apps can
assume fixed relationships between camera features—like aspect ratio and sensor
orientation—and device features—like device orientation and natural
orientation.

New form factors challenge this assumption. A foldable device can change its
display size and aspect ratio without device rotation changing. For example,
unfolding a device changes the aspect ratio, but if the user doesn't rotate
the device, its rotation stays the same. If an app assumes that aspect ratio
correlates to device rotation, it may incorrectly rotate or scale the camera
preview. The same can happen if an app assumes camera sensor orientation
matches a portrait device orientation, which isn't always true for landscape
foldables.

#### Solution 1: Jetpack CameraX (Best)

The simplest and most robust solution is to use the Jetpack CameraX library. Its
[`PreviewView`](/media/camera/camerax/preview) UI element is designed to handle all preview complexities
automatically:

* `PreviewView` correctly adjusts for sensor orientation, device rotation, and
  scaling.
* It maintains the aspect ratio of the camera image, typically by centering and
  cropping (FILL\_CENTER).
* You can set the scale type to `FIT_CENTER` to letterbox the preview if
  needed.

For more information, see [Implement a preview](/training/camerax/preview) in the CameraX documentation.

#### Solution 2: CameraViewfinder

If you are using an existing Camera2 codebase, the `CameraViewfinder` library
(backward compatible to API level 21) is another modern solution. It simplifies
displaying the camera feed by using a `TextureView` or `SurfaceView`
and applying all the necessary transformations (aspect ratio, scale, and
rotation) for you.

For more information, see the [Introducing Camera Viewfinder](https://android-developers.googleblog.com/2022/11/introducing-camera-viewfinder.html) blog post and
[Camera preview](/media/camera/camera2/camera-preview#cameraviewfinder) developer guide.

#### Solution 3: Manual Camera2 implementation

If you can't use CameraX or `CameraViewfinder`, you must manually calculate the
orientation and aspect ratio and ensure the calculations are updated on each
configuration change:

* Get the camera sensor orientation (for example, 0, 90, 180, 270 degrees) from
  `CameraCharacteristics`.
* Get the device's current display rotation (for example, 0, 90, 180, 270
  degrees).
* Use these two values to determine the necessary transformations for your
  `SurfaceView` or `TextureView`.
* Ensure the aspect ratio of your output `Surface` matches the aspect ratio of
  the camera preview to prevent distortion.
* The camera app might be running in a portion of the screen, either in
  multi-window or desktop windowing mode or on a connected display. For this
  reason, screen size should not be used to determine the dimensions of the
  camera viewfinder, use [window metrics](/media/camera/camera2/camera-preview#window_metrics) instead.

For more information, see the [Camera preview](/media/camera/camera2/camera-preview) developer guide and
[Your Camera app on different form factors](https://www.youtube.com/watch?v=XcJIrTedfus) video.

#### Solution 4: Perform basic camera actions using an intent

If you don't need many camera features, a simple and straightforward solution is
to perform basic camera actions like capturing a photo or video using the
device's default camera application. You don't need to integrate with a camera
library; instead, use an [Intent](/reference/android/content/Intent).

For more information, see [Camera intents](/media/camera/camera-intents).

### Configuration and continuity

Foldable devices enhance UI versatility but can initiate more configuration
changes than nonfoldable. Your app must manage these configuration
changes and their combinations, such as device rotation, folding/unfolding, and
window resizing in multi-window or desktop modes, while retaining or restoring
app state. For example, apps must maintain the following continuity:

* App state without crashing or causing disruptive changes to users (for
  example, when switching screens or sending the app to the background)
* Scroll position of scrollable fields
* Text typed into text fields and keyboard state
* Media playback position so playback resumes where it left off when the
  configuration change was initiated

The configuration changes that are frequently triggered include `screenSize`,
`smallestScreenSize`, `screenLayout`, `orientation`, `density`, `fontScale`,
`touchscreen`, and `keyboard`.

See [`android:configChanges`](/guide/topics/manifest/activity-element#config) and [Handle configuration changes](/guide/topics/resources/runtime-changes). For
additional information about managing app state, see [Save UI states](/topic/libraries/architecture/saving-states).

### Density config changes

The outer and inner screens of trifolds and landscape foldable devices might
feature different pixel densities. Therefore, managing the configuration change
for `density` requires extra attention. Android typically restarts the
activity when display density changes, which can cause data loss. To prevent
the system from restarting the activity, declare density handling in your manifest
and manage the configuration change programmatically in your app.

#### AndroidManifest.xml configuration

* `density`: Declares that the app will handle the screen density change
* Other config changes: It's also good to declare other frequently occurring
  config changes, for example, `screenSize`, `orientation`, `keyboardHidden`,
  `fontScale`, and so forth

Declaring density (and other config changes) prevents the system from
restarting the activity and instead calls onConfigurationChanged().

#### onConfigurationChanged() implementation

When a density change occurs, you must update your resources (like reloading
bitmaps or recalculating layout sizes) in the callback:

* Verify that the DPI changed to `newConfig.densityDpi`
* Reset custom views, custom drawables, and so forth to he new density

#### Resource items to process

* **Image resource**: Replace bitmaps and drawables with density-specific
  resources, or adjust the scale directly
* **Layout unit (dp to px conversion)**: Recalculate view size, margin, padding
* **Font and text size**: Reapply sp unit text size
* **Custom `View`/`Canvas` drawing**: Update the pixel-based values used to draw
  `Canvas`

### Determining app orientation

Never rely on the physical device rotation when building adaptive, because it
will be [ignored on large screen devices](/about/versions/16/behavior-changes-16#ignore-orientation) and an app in multi-window mode
could have a different orientation than the device. Instead, use
Configuration.orientation or WindowMetrics to identify if your app is currently
in landscape or portrait orientation based on the window size.

#### Solution 1: Use Configuration.orientation

This property identifies the orientation in which your app is currently
displayed.

#### Solution 2: Use WindowMetrics#getBounds()

You can get the app's current display bounds and check its width and height to
determine orientation.

If you need to limit app orientation on phones (or the outer screens of
foldables) but not on large screen devices, see
[Restrict app orientation on phones](/develop/ui/compose/quick-guides/content/restrict-app-orientation-on-phones).

### Postures and display modes

Foldable postures and states such as tabletop and [`HALF_OPENED`](/reference/kotlin/androidx/window/layout/FoldingFeature.State#HALF_OPENED()) are
supported by both portrait foldables and landscape foldables. Trifolds, however,
do not support tabletop posture and cannot be used `HALF_OPENED`. Trifolds
instead offer a larger screen for a unique user experience when fully unfolded.

To differentiate your app on foldables that support `HALF_OPENED`, use Jetpack
WindowManager APIs such as [`FoldingFeature`](/reference/kotlin/androidx/window/layout/FoldingFeature).

Learn more about foldable postures, states, and support for camera preview in
the following developer guides:

* [Learn about foldables](/develop/ui/compose/layouts/adaptive/foldables/learn-about-foldables)
* [Make your app fold aware](/develop/ui/compose/layouts/adaptive/foldables/make-your-app-fold-aware)

Foldables offer unique viewing experiences. Rear display mode and
dual‑screen mode enable you to build special display features for foldable
devices such as rear‑camera selfie preview and simultaneous but different
displays on inner and outer screens. For more information see:

* [Support foldable display modes](/develop/ui/compose/layouts/adaptive/foldables/support-foldable-display-modes)

### Locking orientation to natural sensor orientation

For very specific use cases—in particular, apps that need to take over the whole
screen unrelated to the folded state of the device—the `nosensor` flag allows
you to lock the app to the natural orientation of the device. For example, on a
Pixel Fold, the natural orientation of the device when folded is portrait, while
the natural orientation when unfolded is landscape. Adding the `nosensor` flag
forces the app to be locked in portrait when running on the outer display and
locked to landscape when running on the inner display.

```
<activity
  android:name=".MainActivity"
  android:screenOrientation="nosensor">
```

**Important:** The `nosensor` flag doesn't cause any app compatibility issues; however,
using the flag is not advised because doing so is contrary to the adaptive app guidelines.

### Games and XR sensor remapping

For games and XR apps, raw sensor data (like gyroscope or accelerometer) is
provided in the device-fixed coordinate system. If the user rotates the device
to play a game in landscape, the sensor axes do not rotate with the screen,
leading to incorrect game controls.

To fix this issue, check the current [Display.getRotation()](/reference/android/view/Display#getRotation()) and remap the axes
accordingly:

* **Rotation 0**: x=x, y=y
* **Rotation 90**: x=-y, y=x
* **Rotation 180**: x=-x, y=-y
* **Rotation 270**: x=y, y=-x

For rotation vectors (used in compass or XR apps), use
[SensorManager.remapCoordinateSystem()](/reference/android/hardware/SensorManager#remapCoordinateSystem(float%5B%5D,%20int,%20int,%20float%5B%5D)) to map the camera lens direction or
top of the screen to the new axes based on the current rotation.

### App compatibility

Applications must follow the app quality guidelines to guarantee compatibility
across all form factors and connected displays. If an application cannot comply
with the guidelines, device manufacturers can implement compatibility
treatments, although this may degrade the user experience.

For additional information, review the comprehensive list of [compatibility
workarounds](/guide/practices/device-compatibility-mode#common_compatibility_issues) provided in the platform, specifically those related to [camera
preview](/guide/practices/device-compatibility-mode#camera_preview), [overrides](/guide/practices/device-compatibility-mode#per-app_overrides), and [Android 16 API changes](/guide/practices/device-compatibility-mode#android_16) that could change
your app behavior.

To learn more about building adaptive apps, see [Large screen app quality](/docs/quality-guidelines/large-screen-app-quality).

[Previous

arrow\_back

Support foldable display modes](/develop/ui/compose/layouts/adaptive/foldables/support-foldable-display-modes)

[Next

Visibility tracking

arrow\_forward](/develop/ui/compose/layouts/visibility-modifiers)