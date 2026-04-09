---
title: https://developer.android.com/develop/ui/views/pip-jetpack
url: https://developer.android.com/develop/ui/views/pip-jetpack
source: md.txt
---

The [Picture-in-Picture (PiP) Jetpack Library](https://developer.android.com/jetpack/androidx/releases/core#core-pip-1.0.0-alpha) offers a streamlined and robust
solution for Android app developers to implement PiP functionality, particularly
for media playback, video communication, and navigation apps. By providing a
unified API, the library helps eliminate boilerplate code, common in-app bugs,
and improve the overall quality of the PiP user experience.

The PiP Jetpack library facilitates the existing PiP APIs by addressing several
key challenges and inconsistencies across the Android ecosystem:

- **OS fragmentation** : The library automatically handles differences in PiP API calls across various Android versions, such as using [`enterPictureInPictureMode`](https://developer.android.com/reference/android/app/Activity#enterPictureInPictureMode(android.app.PictureInPictureParams)) before Android 12 and [`isAutoEnterEnabled`](https://developer.android.com/reference/android/app/PictureInPictureParams#isAutoEnterEnabled()) after, so developers don't need to manage version differences.
- **Incorrect PiP parameters** : It provides a unified solution for correctly setting PiP parameters, for example [`setSourceRectHint`](https://developer.android.com/reference/android/app/PictureInPictureParams.Builder#setSourceRectHint(android.graphics.Rect)), to create smooth and high-quality animations during media playback.
- **Unified PiP state callbacks** : It consolidates `onPictureInPictureModeChanged` and `onPictureInPictureUiStateChanged` into a single, unified callback interface (`PictureInPictureDelegate.OnPictureInPictureEventListener`) for simplified state and UI management.
- **Boilerplate code reduction** : The library reduces the amount of repetitive, boilerplate code by offering predefined sets of `RemoteActions` for common use cases, such as playback controls and video call actions.
- **Future-proofing**: Further PiP features are delivered through the Jetpack library, allowing adopters to access additional functionality with minimal to no effort.

## Adopt Jetpack

In order to adopt the Jetpack Library, replace your existing custom PiP
implementation with the Jetpack Library APIs. The complexity and cost of
adoption will vary based on the app's current implementation.

The following sections describe some of the typical use cases of PiP and the
necessary implementation steps:

### Navigation

The app informs the library of the navigation's active or inactive state and
sets the aspect ratio. The Jetpack library handles the rest.

**Key differences:**

1. No need to differentiate auto-enter and legacy-enter on app side.
2. Consolidated callback interfaces.
3. New `PictureInPictureParams` builder for back compatibility.

### Video Call

The app informs the library of the call's active or inactive state and sets the
aspect ratio.

**Key differences:**

1. No need to differentiate auto-enter and legacy-enter on app side.
2. Consolidated callback interfaces.
3. New `PictureInPictureParams` builder for back compatibility.
4. Standardized action icons for video call.

### Video Playback

The Jetpack library offers player delegates that you can integrate to manage
PiP enablement or disablement and accurately set the source rectangle hint.
You can also opt into a predefined set of `RemoteAction` objects, similar to
those used in video call scenarios.

**Key features:**

1. Handles back compatibility, no OS version check is required.
2. Playback state synchronization and auto-entry control.
3. Continuous geometry tracking using `SourceRectHint`.