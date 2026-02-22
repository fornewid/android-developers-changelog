---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/restrict-app-orientation-on-phones
url: https://developer.android.com/develop/ui/compose/quick-guides/content/restrict-app-orientation-on-phones
source: md.txt
---

<br />

Your app works great on phones in portrait orientation, so you've restricted the
app to portrait only. But you see an opportunity to do more on large screens in
landscape orientation or unfolded foldables.
| **Note:** For apps targeting Android 16 (API level 36) and higher, orientation, resizability, and aspect ratio restrictions no longer apply on displays with smallest width \>= 600dp. You can learn more at [Behavior changes: Apps targeting
| Android 16 or higher](https://developer.android.com/about/versions/16/behavior-changes-16#ignore-orientation).

How can you have it both ways---restrict the app to portrait orientation on
a foldable's outer screen, but enable landscape on the inner screen?

This guide is a temporary measure until you can improve your app to provide full
support for all device configurations.

## Results

Your app remains in portrait orientation on small screens regardless of device
rotation. On large screens, the app supports landscape and portrait
orientations.

## Version compatibility

This implementation is compatible with all API levels.

### Dependencies

### Kotlin

    implementation("androidx.window:window:1.5.1")
    implementation("androidx.window:window-core:1.5.1")

### Groovy

    implementation "androidx.window:window:1.5.1"
    implementation "androidx.window:window-core:1.5.1"

| **Note:** Set the version to the latest stable release.

## Manage app orientation

To enable landscape orientation on large screens, set your app manifest to
handle orientation changes by default. At runtime, determine the app window
size. If the app window is small, restrict the app's orientation by overriding
the manifest orientation setting.

### 1. Specify orientation setting in the app manifest

You can either avoid declaring the [`screenOrientation`](https://developer.android.com/guide/topics/manifest/activity-element#screen) element of the app
manifest (in which case orientation defaults to `unspecified`) or set screen
orientation to `fullUser`. If the user has not locked sensor-based rotation,
your app will support all device orientations.  

    <activity
        android:name=".MyActivity"
        android:screenOrientation="fullUser">

| **Note:** `screenOrientation` is ignored (or is equivalent to `unspecified`) when apps run in multi‑window mode. So, if you restrict your app to one orientation, the app might not work properly in multi‑window mode.

The difference between `unspecified` and `fullUser` is subtle but important. If
you don't declare a `screenOrientation` value, the system chooses the
orientation, and the policy the system uses to define the orientation might
differ from device to device.

On the other hand, specifying `fullUser` matches
more closely the behavior the user defined for the device: if the user has
locked sensor-based rotation, the app follows the user preference; otherwise,
the system allows any of the four possible screen orientations (portrait,
landscape, reverse portrait, or reverse landscape).

Additionally, you can
use `nosensor` to determine the orientation without taking into account the
sensor data, but the following code will work in the same way.
See [`screenOrientation`](https://developer.android.com/guide/topics/manifest/activity-element#screen).

### 2. Determine screen size

With the manifest set to support all user‑permitted orientations, you can
specify app orientation programmatically based on screen size.

Add the [Jetpack WindowManager](https://developer.android.com/jetpack/androidx/releases/window) libraries to the module's `build.gradle` or
`build.gradle.kts` file:  

### Kotlin

```kotlin
implementation("androidx.window:window:<var translate="no">version</var>")
implementation("androidx.window:window-core:<var translate="no">version</var>")
```

### Groovy

```groovy
implementation 'androidx.window:window:<var translate="no">version</var>'
implementation 'androidx.window:window-core:<var translate="no">version</var>'
```

Use the Jetpack WindowManager
[`WindowMetricsCalculator#computeMaximumWindowMetrics()`](https://developer.android.com/reference/kotlin/androidx/window/layout/WindowMetricsCalculator#computeMaximumWindowMetrics(android.app.Activity)) method to obtain the
device screen size as a [`WindowMetrics`](https://developer.android.com/reference/kotlin/androidx/window/layout/WindowMetrics) object. The window metrics can be
compared to window size classes to decide when to restrict orientation.

[Windows size classes](https://developer.android.com/develop/ui/compose/layouts/adaptive/use-window-size-classes) provide the breakpoints between small and large
screens.

Use the [`WindowSizeClass#minWidthDp`](https://developer.android.com/reference/kotlin/androidx/window/core/layout/WindowSizeClass#minWidthDp()) and
[`WindowSizeClass#minHeightDp`](https://developer.android.com/reference/kotlin/androidx/window/core/layout/WindowSizeClass#minHeightDp()) breakpoints to determine the screen size:  

    /** Determines whether the device has a compact screen. **/
    fun compactScreen() : Boolean {
        val metrics = WindowMetricsCalculator.getOrCreate().computeMaximumWindowMetrics(this)
        val width = metrics.bounds.width()
        val height = metrics.bounds.height()
        val density = resources.displayMetrics.density
        val windowSizeClass =
            BREAKPOINTS_V1.computeWindowSizeClass(width / density, height / density)
        return windowSizeClass.minWidthDp == 0
    }

**Note:**
- The examples are implemented as methods of an activity; and so, the activity is dereferenced as `this` in the argument of `computeMaximumWindowMetrics()`.
- The `computeMaximumWindowMetrics()` method is used instead of [`computeCurrentWindowMetrics()`](https://developer.android.com/reference/kotlin/androidx/window/layout/WindowMetricsCalculator) because the app can be launched in multi‑window mode, which ignores the screen orientation setting. There's no point in determining the app window size and overriding the orientation setting unless the app window is the entire device screen.

See [WindowManager](https://developer.android.com/jetpack/androidx/releases/window#declaring_dependencies) for instructions about declaring dependencies to make the
`computeMaximumWindowMetrics()` method available in your app.

### 3. Override app manifest setting

When you've determined that the device has compact screen size, you can call
[`Activity#setRequestedOrientation()`](https://developer.android.com/reference/kotlin/android/app/Activity#setrequestedorientation) to override the manifest's
`screenOrientation` setting:  

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        requestedOrientation = if (compactScreen())
            ActivityInfo.SCREEN_ORIENTATION_PORTRAIT else
            ActivityInfo.SCREEN_ORIENTATION_FULL_USER
        ...
        // Replace with a known container that you can safely add a
        // view to where the view won't affect the layout and the view
        // won't be replaced.
        val container: ViewGroup = binding.container

        // Add a utility view to the container to hook into
        // View.onConfigurationChanged. This is required for all
        // activities, even those that don't handle configuration
        // changes. You can't use Activity.onConfigurationChanged,
        // since there are situations where that won't be called when
        // the configuration changes. View.onConfigurationChanged is
        // called in those scenarios.
        container.addView(object : View(this) {
            override fun onConfigurationChanged(newConfig: Configuration?) {
                super.onConfigurationChanged(newConfig)
                requestedOrientation = if (compactScreen())
                    ActivityInfo.SCREEN_ORIENTATION_PORTRAIT else
                    ActivityInfo.SCREEN_ORIENTATION_FULL_USER
            }
        })
    }

| **Note:** The manifest setting is not changed, just overridden.

By adding the logic to the `onCreate()` and `View.onConfigurationChanged()`
methods, you're able to obtain the maximum window metrics and override the
orientation setting whenever the activity is resized or moved between displays,
such as after a device rotation or when a foldable device is folded or unfolded.
For more information about when configuration changes occur and when they cause
activity recreation, refer to [Handle configuration changes](https://developer.android.com/guide/topics/resources/runtime-changes).

If you are using Jetpack Compose, you can use the same `compactScreen()` function
in your app's root Composable to achieve the same result.
| **Note:** If you did not specify `android:screenOrientation` in the manifest, replace the occurrences of `ActivityInfo.SCREEN_ORIENTATION_FULL_USER` with `ActivityInfo.SCREEN_ORIENTATION_UNSPECIFIED` to match the defaults.

## Key points

- [`screenOrientation`](https://developer.android.com/guide/topics/manifest/activity-element#screen): App manifest setting that enables you to specify how your app responds to device orientation changes
- [Jetpack WindowManager](https://developer.android.com/jetpack/androidx/releases/window): Set of libraries that enable you to determine the size and aspect ratio of the app window; backward compatible to API level 14
- [`Activity#setRequestedOrientation()`](https://developer.android.com/reference/kotlin/android/app/Activity#setrequestedorientation): Method with which you can change the app orientation at runtime

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover broader
Android development goals:  
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png)  
![](https://developer.android.com/static/images/picto-icons/collection.svg)  

### Optimize for large screens

Enable your app to support an optimized user experience on tablets, foldables, and ChromeOS devices.  
[Quick guide collection](https://developer.android.com/quick-guides/collections/optimize-for-large-screens)
![](https://developer.android.com/static/images/picto-icons/help.svg)  

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.  
[Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)