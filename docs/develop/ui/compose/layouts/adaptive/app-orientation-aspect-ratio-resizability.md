---
title: https://developer.android.com/develop/ui/compose/layouts/adaptive/app-orientation-aspect-ratio-resizability
url: https://developer.android.com/develop/ui/compose/layouts/adaptive/app-orientation-aspect-ratio-resizability
source: md.txt
---

Android apps run on devices of all kinds: phones, tablets, foldables, ChromeOS
devices, cars, TVs, and even XR. To adapt to this varied environment, your app
should support all device form factors and display sizes.

Android 16 (API level 36) enables apps to adapt to different form factors and
display sizes by overriding app restrictions for screen orientation, aspect
ratio, and resizability. The overrides apply to devices with smallest width \>=
600dp which defines the following:

- Tablets
- Inner displays of large screen foldables
- Desktop windowing (on all form factors)

Apps that target API level 36 are resizable and able to enter multi‑window
mode (equivalent to [`resizeableActivity="true"`](https://developer.android.com/guide/topics/manifest/activity-element#resizeableActivity)) if the display's smallest
width is \>= 600dp.
![App is letterboxed on an unfolded large screen device prior to Android 16, but is full sceen when targeting Android 16. App shows more news items when full screen rather thanp letterboxed.](https://developer.android.com/static/develop/ui/compose/images/layouts/adaptive/app_letterboxed_and_full_screen.png) **Figure 1.** Developer News feed previously letterboxed on large screen devices (left) runs full screen when targeting Android 16 (right).

Android 16 enforces a consistent model of adaptive app design that optimizes the
user experience by respecting user preferences for device orientation, aspect
ratio, and display size.

## Changes

The following manifest attributes and APIs are ignored for apps targeting
Android 16 (API level 36) on large screens:

| Attribute or API | Ignored values |
|---|---|
| `screenOrientation` | `portrait`, `landscape`, `reversePortrait`, `reverseLandscape`, `sensorPortrait`, `sensorLandscape`, `userPortrait`, `userLandscape` |
| `resizeableActivity` | all |
| `minAspectRatio` | all |
| `maxAspectRatio` | all |
| `setRequestedOrientation()` `getRequestedOrientation()` | `portrait`, `landscape`, `reversePortrait`, `reverseLandscape`, `sensorPortrait`, `sensorLandscape`, `userPortrait`, `userLandscape` |

## Exceptions

Exceptions to the Android 16 changes include the following:

- Displays smaller than sw600dp (most phones, flippables, and outer displays
  of large screen foldables)

- Games, based on the [`android:appCategory`](https://developer.android.com/guide/topics/manifest/application-element#appCategory) flag

  Publish your game using Android App Bundles and Play App Signing, allowing
  Google Play to manage the flag and provide the benefits of app bundles
  automatically. See also [App manifest overview](https://developer.android.com/guide/topics/manifest/manifest-intro).
- User opt in to app's default behavior in the aspect ratio settings

## Opt out

To opt out of the API level 36 behavior, declare the
`PROPERTY_COMPAT_ALLOW_RESTRICTED_RESIZABILITY` manifest property.

To opt out for a specific activity, set the property in the `<activity>`
element:

    <activity ...>
        <property
            android:name="android.window.PROPERTY_COMPAT_ALLOW_RESTRICTED_RESIZABILITY"
            android:value="true" />
        ...
    </activity>

To opt out for your entire app, set the property in the `<application>` element:

    <application ...>
        <property
            android:name="android.window.PROPERTY_COMPAT_ALLOW_RESTRICTED_RESIZABILITY"
            android:value="true" />
        ...
    </application>

> [!WARNING]
> **Warning:** The Android framework will eliminate the opt-out capability in API level 37. For apps that target API level 37 or higher, orientation, aspect ratio, and resizability restrictions will always be ignored on displays that are at least sw600dp.

## Tests

To test whether your app is impacted by the Android 16 changes, use the Pixel
Tablet and Pixel Fold series emulators in Android Studio and set
`targetSdkPreview = "Baklava"` in your app's module `build.gradle` file.

Or use the app compatibility framework on your test devices by enabling the
[UNIVERSAL_RESIZABLE_BY_DEFAULT](https://developer.android.com/about/versions/16/reference/compat-framework-changes#universal_resizable_by_default) flag (see [Compatibility framework tools](https://developer.android.com/guide/app-compatibility/test-debug)).

You can automate testing with the [Espresso](https://developer.android.com/training/testing/espresso) testing framework and [Jetpack
Compose testing APIs](https://developer.android.com/develop/ui/compose/testing/apis).

## Common problems

Apps that restrict device orientation, aspect ratio, or app resizability might
have display issues on Android 16, such as overlapping layouts.

To provide an optimal user experience on phones, foldables, tablets, ChromeOS
devices, car displays, and XR, build your app to be responsive and adaptive:

- **Avoid stretched UI components:** Layouts designed for standard, portrait
  phone screens will likely fail to accommodate other aspect ratios. For
  example, UI elements that fill the entire width of the display will appear
  stretched in landscape orientation. Add a maximum width to components to
  avoid stretching.

- **Enable layouts to scroll:** If layouts don't scroll, users might not be
  able to access buttons or other UI elements that are off screen in landscape
  orientation. Enable app layouts to scroll to verify all content is reachable
  regardless of the height of the display.

- **Verify camera compatibility in portrait and landscape:** Camera viewfinder
  previews that assume a specific aspect ratio and orientation relative to the
  camera sensor can result in stretched or flipped previews on nonconforming
  displays. Verify that viewfinders rotate properly with orientation changes.
  Enable viewfinders to adjust to UI aspect ratios that differ from the sensor
  aspect ratio.

- **Preserve state during window size changes:** The removal of orientation
  and aspect ratio restrictions can result in frequent app window size changes
  in response to how users prefer to use an app, for example, by rotating,
  folding, or unfolding a device or by resizing an app in multi-window or
  desktop windowing mode. Configuration changes such as orientation changes
  and window resizing cause activity recreation (by default). To help provide
  an optimal user experience, preserve app state during configuration changes
  so your app retains data (such as form input) and users can maintain
  context.

- **Use window size classes:** Support different window sizes and aspect
  ratios without device‑specific customizations. Assume window sizes
  will change frequently. Use window size classes to characterize the window
  dimensions, and then apply an appropriate adaptive layout.

- **Build responsive layouts:** Within window size classes, responsive layouts
  adjust to changes in display dimensions to always create an optimal app
  presentation.

## Timeline

- **Android 16 (2025):** Support for all orientations and aspect ratios and for app resizability is the baseline experience for large screen devices (smallest screen width \>= 600dp) for apps that target API level 36. However, developers can opt out.

| Target API level | Applicable devices | Developer opt out allowed |
|---|---|---|
| 36 (Android 16) | Large screen devices (smallest screen width \>= 600dp) | Yes |

The deadlines for targeting specific API levels are app store specific. Google
Play will require apps to target API level 36 as of August 2026.

## Additional resources

- [Behavior changes: Apps targeting Android 16 or higher](https://developer.android.com/about/versions/16/behavior-changes-16)
- [Build adaptive apps](https://developer.android.com/develop/ui/compose/build-adaptive-apps)
- [Adaptive do's and don'ts](https://developer.android.com/develop/ui/compose/layouts/adaptive/adaptive-dos-and-donts)