---
title: https://developer.android.com/about/versions/17/release-notes
url: https://developer.android.com/about/versions/17/release-notes
source: md.txt
---

### Beta 1

|---|---|
| **Release date** | February 13, 2026 |
| **Builds** | CP21.260116.011.B1 CP21.260116.011.A1 (Pixel 6 Pro, Pixel 6, Pixel 6a, Pixel 7 Pro, Pixel 7) |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-01-05 |
| **Google Play services** | 25.47.33 |

### Android 17 Beta 1 (February 2026)

[Beta 1 is now available](https://android-developers.googleblog.com/2026/02/the-first-beta-of-android-17.html),
with the latest features and changes to try with your apps. This release is suitable for development,
testing, and general use. However, Android 17 is still in active development, so
the Android system and apps running on it **might not always work as expected**.

As with previous versions, Android 17 includes system changes. In some cases,
these changes can affect apps until they are updated to support Android 17, so
you might see impacts ranging from minor issues to more significant limitations.
In general, most apps will work as expected, as will most APIs and features.

### What's new in Beta 1

Android 17 continues our work for more adaptable Android apps, introduces significant
enhancements to camera and media capabilities, new tools for optimizing connectivity,
and expanded profiles for companion devices. Highlights include:

#### User Interface \& Windowing

##### Mandatory Large Screen Adaptivity

Apps targeting **Android 17 (API level 37)** running on large screens ([sw ≥ 600dp](https://developer.android.com/guide/topics/large-screens/support-different-screen-sizes)) can no longer opt-out of resizing or orientation changes.

- **Ignored Attributes** : [`screenOrientation`](https://developer.android.com/guide/topics/manifest/activity-element#screen), [`resizeableActivity`](https://developer.android.com/guide/topics/manifest/activity-element#resizeableActivity), [`minAspectRatio`](https://developer.android.com/guide/topics/manifest/activity-element#minaspectratio), and [`maxAspectRatio`](https://developer.android.com/guide/topics/manifest/activity-element#maxaspectratio) are ignored on large screens.
- **Exemptions** : Devices smaller than 600dp and apps categorized as Games (`android:appCategory`).

##### Optimized Configuration Changes

To prevent state loss, the system **no longer restarts Activities** by default
for specific configuration changes, including:

- [`CONFIG_KEYBOARD`](https://developer.android.com/reference/android/content/pm/ActivityInfo#CONFIG_KEYBOARD) / [`CONFIG_KEYBOARD_HIDDEN`](https://developer.android.com/reference/android/content/pm/ActivityInfo#CONFIG_KEYBOARD)
- [`CONFIG_NAVIGATION`](https://developer.android.com/reference/android/content/pm/ActivityInfo#CONFIG_NAVIGATION)
- [`CONFIG_TOUCHSCREEN`](https://developer.android.com/reference/android/content/pm/ActivityInfo#CONFIG_TOUCHSCREEN)

**Action Required**: If your app relies on restarts to reload resources for
these events, you must explicitly opt-in using the new
android:recreateOnConfigChanges manifest attribute.

#### Performance \& Runtime

- **Lock-free MessageQueue** : A new lock-free implementation of [`android.os.MessageQueue`](https://developer.android.com/reference/android/os/MessageQueue) reduces missed frames.
- **Generational Garbage Collection**: ART's Concurrent Mark-Compact collector now supports generational GC, prioritizing frequent, low-cost "young generation" collections.
- **New Profiling Triggers** : [`ProfilingManager`](https://developer.android.com/reference/android/os/ProfilingManager) adds triggers for [`COLD_START`](https://developer.android.com/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_COLD_START), [`OOM`](https://developer.android.com/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_OOM), and [`KILL_EXCESSIVE_CPU_USAGE`](https://developer.android.com/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_KILL_EXCESSIVE_CPU_USAGE).
- **Notification Restrictions**: Strict size limits enforced on custom notification views to reduce memory usage.

#### Media \& Camera

##### Camera

- **Dynamic Session Updates** : Use [`CameraCaptureSession.updateOutputConfigurations()`](https://developer.android.com/reference/android/hardware/camera2/CameraCaptureSession#updateOutputConfigurations(java.util.List%3Candroid.hardware.camera2.params.OutputConfiguration%3E)) to switch use cases (e.g., Photo to Video) without closing the session or causing glitches.

##### Audio \& Video

- **Constant Quality for Video Recording** : [setVideoEncodingQuality()](https://developer.android.com/reference/android/media/MediaRecorder#setVideoQuality(int)) in [MediaRecorder](https://developer.android.com/reference/android/media/MediaRecorder) allows you to configure a constant quality (CQ) mode for video encoders.
- **Background Audio Hardening**: Audio playback, focus requests, and volume changes initiate silently (fail) if the app is not in a valid lifecycle state.
- **VVC Support** : Added platform support for [Versatile Video Coding (H.266)](https://developer.android.com/guide/topics/media/media-formats#video-formats).

#### Privacy \& Security

- **Cleartext Deprecation** : [`android:usesCleartextTraffic`](https://developer.android.com/guide/topics/manifest/application-element#usesCleartextTraffic) is deprecated. Apps targeting SDK 37+ relying on this attribute will default to blocking cleartext; migrate to [**Network Security Configuration**](https://developer.android.com/training/articles/security-config).
- **HPKE Hybrid Cryptography** : Introduced a public [Service Provider Interface](https://developer.android.com/reference/android/crypto/hpke/HpkeSpi) for an implementation of HPKE hybrid cryptography.

#### Connectivity \& Tools

- [**Companion Device Manager**](https://developer.android.com/guide/topics/connectivity/companion-device-pairing):
  - **New Profiles** : [Medical Devices](https://developer.android.com/reference/android/companion/AssociationRequest#DEVICE_PROFILE_MEDICAL) and [Fitness Trackers](https://developer.android.com/reference/android/companion/AssociationRequest#DEVICE_PROFILE_FITNESS_TRACKER).
  - **Unified Permission Dialog** : [`setExtraPermissions`](https://developer.android.com/reference/android/companion/AssociationRequest.Builder#setExtraPermissions(java.util.Set%3Cjava.lang.String%3E)) bundles nearby permissions into the association dialog.