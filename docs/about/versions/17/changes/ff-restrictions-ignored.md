---
title: https://developer.android.com/about/versions/17/changes/ff-restrictions-ignored
url: https://developer.android.com/about/versions/17/changes/ff-restrictions-ignored
source: md.txt
---

With Android apps now running on a variety of devices (such as phones, tablets,
foldables, desktops, cars, and TVs) and windowing modes on large screens (such
as split screen and desktop windowing), developers should build Android apps
that adapt to any screen and window size, regardless of device orientation.
Paradigms like restricting orientation and resizability are too restrictive in
today's multidevice world.

## Ignore orientation, resizability, and aspect ratio restrictions

For apps targeting Android 17 or higher, orientation,
resizability, and aspect ratio restrictions no longer apply on displays whose
smallest width is greater than 600dp. Apps fill the entire display window,
regardless of aspect ratio or a user's preferred orientation, and pillarboxing
isn't used.

Android 17 removes the [temporary developer opt-out for
orientation and resizability restrictions on large screen devices](https://developer.android.com/about/versions/16/behavior-changes-16#temporary-opt-out) that was
provided in Android 16.

This change introduces a new standard platform behavior. Android is moving
toward a model where apps are expected to adapt to various orientations, display
sizes, and aspect ratios. Restrictions like fixed orientation or limited
resizability hinder app adaptability. [Make your app adaptive](https://developer.android.com/adaptive-apps) to deliver the
best possible user experience.

You can also test this behavior by using the [app compatibility framework](https://developer.android.com/guide/app-compatibility/test-debug)
and enabling the `UNIVERSAL_RESIZABLE_BY_DEFAULT` compat flag.

## Common breaking changes

Ignoring orientation, resizability, and aspect ratio restrictions might impact
your app's UI on some devices, especially elements that were designed for small
layouts locked in portrait orientation. For example, apps might have issues like
stretched layouts and off-screen animations and components. Any assumptions you
make about aspect ratio or orientation can cause visual issues with your app.
[Learn more about how to avoid these issues](https://developer.android.com/develop/ui/compose/layouts/adaptive) and improve your app's adaptive
behaviour.

A common problem on landscape foldables or for aspect ratio calculations in
scenarios like multi-window, desktop windowing, or connected displays, is when
the camera preview appears stretched, rotated, or cropped. This issue often
happens on large screen and foldable devices because apps assume fixed
relationships between camera features (like aspect ratio and sensor orientation)
and device features (like device orientation and natural orientation). [Learn
more about managing camera preview](https://developer.android.com/guide/topics/large-screens/camera-preview-and-media-projection).

Allowing device rotation results in more activity re-creation, which can result
in losing user state if not properly preserved. Learn how to correctly save the
UI state in [Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states).

## Implementation details

The following manifest attributes and runtime APIs are ignored across large
screen devices in full-screen and multi-window modes:

- [`screenOrientation`](https://developer.android.com/guide/topics/manifest/activity-element#screen)
- [`resizableActivity`](https://developer.android.com/guide/topics/manifest/activity-element#resizeableActivity)
- [`minAspectRatio`](https://developer.android.com/guide/topics/manifest/activity-element#minaspectratio)
- [`maxAspectRatio`](https://developer.android.com/guide/topics/manifest/activity-element#maxaspectratio)
- [`setRequestedOrientation()`](https://developer.android.com/reference/android/app/Activity#setRequestedOrientation(int))
- [`getRequestedOrientation()`](https://developer.android.com/reference/android/app/Activity#getRequestedOrientation())

The following values for `screenOrientation, setRequestedOrientation()`, and
`getRequestedOrientation()` are ignored:

- `portrait`
- `reversePortrait`
- `sensorPortrait`
- `userPortrait`
- `landscape`
- `reverseLandscape`
- `sensorLandscape`
- `userLandscape`

Regarding display resizability, `android:resizeableActivity="false",
android:minAspectRatio`, and `android:maxAspectRatio` have no effect.

## Exceptions

The Android 17 orientation, resizability, and aspect ratio restrictions
don't apply in the following situations:

- Games (based on the [`android:appCategory`](https://developer.android.com/guide/topics/manifest/application-element#appCategory) flag)
- Users explicitly opting in to the app's default behavior in the device's aspect ratio settings
- Screens whose smallest width is smaller than `sw600dp`