---
title: https://developer.android.com/develop/adaptive-apps/cookbook/orientation-restriction
url: https://developer.android.com/develop/adaptive-apps/cookbook/orientation-restriction
source: md.txt
---

![Two star rating icon](https://developer.android.com/static/develop/adaptive-apps/cookbook/images/two-star-rating.png)

Your app works great on phones in portrait orientation, so you've restricted the
app to portrait only. But you see an opportunity to do more on large screens in
landscape orientation.

How can you have it both ways---restrict the app to portrait orientation on
small screens, but enable landscape on large?

## Best practices

The best apps respect user preferences such as device orientation.

The [Adaptive app quality guidelines](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality) recommend that apps support all device
configurations, including portrait and landscape orientations, multi-window
mode, and folded and unfolded states of foldable devices. Apps should optimize
layouts and user interfaces for different configurations, and apps should save
and restore state during configuration changes.

This recipe is a temporary measure---a pinch of large screen support. Use
the recipe until you can improve your app to provide full support for all device
configurations.

## Ingredients

- [`screenOrientation`](https://developer.android.com/guide/topics/manifest/activity-element#screen): App manifest setting that enables you to specify how your app responds to device orientation changes
- [`Activity#setRequestedOrientation()`](https://developer.android.com/reference/kotlin/android/app/Activity#setrequestedorientation): Method with which you can change the app orientation at runtime
- [`LocalConfiguration`](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/package-summary#LocalConfiguration()): Composable local provider that exposes the current device `Configuration`, allowing you to read screen dimensions in DPs.
- [`LaunchedEffect`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/package-summary#LaunchedEffect(kotlin.Any,kotlin.Function2)): Compose side-effect API that runs a block of code when a key changes (in this case, when the configuration changes).

## Steps

Enable the app to handle orientation changes by default in the app manifest.
Then, at runtime, use Jetpack Compose to dynamically restrict the orientation to
portrait on compact screens (phones) while allowing all orientations on large
screens.

### 1. Specify orientation setting in the app manifest

You can either avoid declaring the [`screenOrientation`](https://developer.android.com/guide/topics/manifest/activity-element#screen) element of the app
manifest (in which case orientation defaults to `unspecified`) or set screen
orientation to `fullUser`. If the user has not locked sensor-based rotation,
your app will support all device orientations.

    <activity
        android:name=".MyActivity"
        android:screenOrientation="fullUser">

> [!NOTE]
> **Note:** `screenOrientation` is ignored (or is equivalent to `unspecified`) when apps run in multi-window mode. So, if you restrict your app to one orientation or another, the app might not work properly in multi-window mode.

The difference between using `unspecified` and `fullUser` is subtle but
important. If you don't declare a `screenOrientation` value, the system chooses
the orientation, and the policy the system uses to define the orientation might
differ from device to device. On the other hand, specifying `fullUser` matches
more closely the behavior the user defined for the device: if the user has
locked sensor-based rotation, the app follows the user preference; otherwise,
the system allows any of the four possible screen orientations (portrait,
landscape, reverse portrait, or reverse landscape). See
[`android:screenOrientation`](https://developer.android.com/guide/topics/manifest/activity-element#screen).

### 2. Dynamically restrict orientation in Compose

In Jetpack Compose, you can read the current screen dimensions in DPs reactively
from `LocalConfiguration.current` and use a `LaunchedEffect` to update the
Activity's orientation whenever the configuration changes.

If either the screen width or height is less than `600dp` (corresponding to the
compact breakpoint for phones), restrict the orientation to portrait. Otherwise,
allow the system to rotate the app based on the user's preference (`unspecified`
or `fullUser`).

Here is the complete, compilable implementation:


```kotlin
val configuration = LocalConfiguration.current
val context = LocalActivity.current

LaunchedEffect(configuration) {
    val activity = context ?: return@LaunchedEffect
    // Determine if screen is compact (phone-sized) in either width or height
    val isCompact = configuration.screenWidthDp < 600 || configuration.screenHeightDp < 600
    activity.requestedOrientation = if (isCompact) {
        ActivityInfo.SCREEN_ORIENTATION_PORTRAIT
    } else {
        ActivityInfo.SCREEN_ORIENTATION_FULL_USER
    }
}
```

<br />

By adding the logic inside a `LaunchedEffect(configuration)` block, you're able
to reactively override the orientation setting whenever the app configuration
changes, such as when the activity is resized, moved between displays, or when a
foldable device is folded or unfolded.

> [!NOTE]
> **Note:** The manifest setting is not changed, just overridden at runtime.

For more information about when configuration changes occur and when they cause
activity recreation, refer to [Handle configuration changes](https://developer.android.com/guide/topics/resources/runtime-changes).

> [!NOTE]
> **Note:** If you did not specify `android:screenOrientation` in the app manifest, you should replace `ActivityInfo.SCREEN_ORIENTATION_FULL_USER` with `ActivityInfo.SCREEN_ORIENTATION_UNSPECIFIED` in your code to match the default system behavior.

## Results

Your app should now remain in portrait orientation on small screens regardless
of device rotation. On large screens, the app should support landscape and
portrait orientations.

## Additional resources

For help with upgrading your app to support all device configurations all the
time, see the following:

- [Support different screen sizes](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-different-screen-sizes)
- [Handle configuration changes](https://developer.android.com/guide/topics/resources/runtime-changes)
- [Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states)