---
title: https://developer.android.com/about/versions/17/release-notes
url: https://developer.android.com/about/versions/17/release-notes
source: md.txt
---

### Beta 2

|---|---|
| **Release date** | February 26, 2026 |
| **Builds** | CP21.260206.011 CP21.260206.011.A1 (Pixel 6 Pro, Pixel 6, Pixel 6a, Pixel 7 Pro, Pixel 7) |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-02-05 |
| **Google Play services** | 25.49.33 |

### Beta 1

|---|---|
| **Release date** | February 13, 2026 |
| **Builds** | CP21.260116.011.B1 CP21.260116.011.A1 (Pixel 6 Pro, Pixel 6, Pixel 6a, Pixel 7 Pro, Pixel 7) |
| **Emulator support** | x86 (64-bit), ARM (v8-A) |
| **Security patch level** | 2026-01-05 |
| **Google Play services** | 25.47.33 |

### Android 17 Beta 2 (February 2026)

[Beta 2 is now available](https://android-developers.googleblog.com/2026/02/the-second-beta-of-android-17.html).
Similar to beta 1, this release is suitable for development, testing, and
general use. However, Android 17 is still in active development, so the Android
system and apps running on it **might not always work as expected**.

### What's new in Beta 2

#### **User Experience \& System UI**

- **Bubbles:** Users can now bubble any app by long-pressing launcher icons. On large screens, a new **bubble bar** in the taskbar manages organized and anchored bubbles. Apps should follow [multi-window guidelines](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode).
- **EyeDropper API:** A new system API allows apps to capture pixel colors from anywhere on the display without requiring screen capture permissions.
- **Contacts Picker:** The [`ACTION_PICK_CONTACTS`](https://developer.android.com/reference/kotlin/android/provider/ContactsPickerSessionContract#ACTION_PICK_CONTACTS:kotlin.String) intent provides a system-level picker. It grants temporary, session-based access to specific fields, reducing the need for full [`READ_CONTACTS`](https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS) permissions.
- **Touchpad Pointer Capture:** By default, captured touchpads now behave like mice, reporting relative movement and gestures instead of raw finger coordinates. Legacy absolute mode remains available via `POINTER_CAPTURE_MODE_ABSOLUTE`.
- **Interactive Chooser:** Apps can use [`getInitialRestingBounds`](https://developer.android.com/reference/kotlin/android/service/chooser/ChooserSession#getinitialrestingbounds) on a [`ChooserSession`](https://developer.android.com/reference/android/service/chooser/ChooserSession) to identify the final UI position of the Chooser for better layout adjustments.

#### **Connectivity \& Cross-Device**

- **Cross-device Handoff:** The new [Handoff API](https://developer.android.com/reference/kotlin/android/app/Activity#sethandoffenabled) enables state resumption across devices (e.g., phone to tablet) via [`CompanionDeviceManager`](https://developer.android.com/reference/android/companion/CompanionDeviceManager).
- **Advanced Ranging:**
  - **UWB DL-TDOA:** Supports FiRA 4.0 for privacy-preserving indoor navigation.
  - **Proximity Detection:** Implements WiFi Alliance specs for improved WiFi-based ranging.
- **Data Plan Enhancements:** Apps can query carrier-allocated downlink/uplink max rates for streaming using [`getStreamingAppMaxDownlinkKbps`](https://developer.android.com/reference/kotlin/android/telephony/SubscriptionInfo#getstreamingappmaxdownlinkkbps) and [`getStreamingAppMaxUplinkKbps`](https://developer.android.com/reference/kotlin/android/telephony/SubscriptionInfo#getstreamingappmaxuplinkkbps).

#### **Core Functionality, Privacy \& Performance**

- **Local Network Access:** Android 17 introduces the [`ACCESS_LOCAL_NETWORK`](https://developer.android.com/reference/kotlin/android/Manifest.permission#access_local_network) permission (part of the [`NEARBY_DEVICES`](https://developer.android.com/reference/android/Manifest.permission_group#NEARBY_DEVICES) group) to protect LAN communication.
- **Time Zone Broadcast:** A new intent, [`ACTION_TIMEZONE_OFFSET_CHANGED`](https://developer.android.com/reference/kotlin/android/content/Intent#action_timezone_offset_changed), triggers specifically on offset changes like DST transitions.
- **NPU Management:** Apps targeting Android 17 must declare the [FEATURE_NEURAL_PROCESSING_UNIT](https://developer.android.com/reference/kotlin/android/content/pm/PackageManager#feature_neural_processing_unit) hardware feature to directly access the NPU.
- **ICU 78:** Updated internationalization libraries support [Unicode 17](https://blog.unicode.org/2025/10/icu-78-released.html).
- **SMS OTP Protection:** To prevent hijacking, Android 17 delays programmatic access to OTP messages by three hours for most apps. Developers should transition to [SMS Retriever](https://developer.android.com/identity/sms-retriever) or [SMS User Consent](https://developer.android.com/identity/sms-retriever/user-consent/overview) APIs.

### Issues fixed in Beta 2

- *A platform stability regression in Android 16 that caused active apps to unexpectedly restart or refresh, preventing lost user progress and intermittent UI flickering during app usage. ([**Issue #440017096**](https://issuetracker.google.com/issues/440017096))*
- *A UI layout regression in the Recent Apps screen for users with German-language settings. ([**Issue #476830557**](https://issuetracker.google.com/issues/476830557), [**Issue #486511401**](https://issuetracker.google.com/issues/486511401))*
- *Improved video streaming reliability by enabling developers to confirm temporal layering support via getOutputFormat after encoder configuration to address missing frame dependency metadata. ([**Issue #306222291**](https://issuetracker.google.com/issues/306222291))*
- *A bug where the Clock screensaver omitted the leading zero in 24-hour format during low-light mode. ([**Issue #444255729**](https://issuetracker.google.com/issues/444255729))*
- *An issue where closing a folder blocked immediate subsequent interactions like opening another folder or switching screens. ([**Issue #470541347**](https://issuetracker.google.com/issues/470541347), [**Issue #471533397**](https://issuetracker.google.com/issues/471533397), [**Issue #477848604**](https://issuetracker.google.com/issues/477848604))*
- *A system crash and spontaneous reboot issue that interrupted device usage. ([**Issue #413562426**](https://issuetracker.google.com/issues/413562426))*
- *A critical system instability causing device freezes and reboots during app transitions or service calls. ([**Issue #419070024**](https://issuetracker.google.com/issues/419070024), [**Issue #428572458**](https://issuetracker.google.com/issues/428572458), [**Issue #430393241**](https://issuetracker.google.com/issues/430393241), [**Issue #424912278**](https://issuetracker.google.com/issues/424912278), [**Issue #431440391**](https://issuetracker.google.com/issues/431440391), [**Issue #426346396**](https://issuetracker.google.com/issues/426346396))*
- *A System UI deadlock that caused lock screen unresponsiveness and display hangs after disconnecting from Android Auto. ([**Issue #457527675**](https://issuetracker.google.com/issues/457527675))*
- *A UI typo in the system location permission disclosure dialog where the Back button was incorrectly displayed as 'Bac'. ([**Issue #460242870**](https://issuetracker.google.com/issues/460242870), [**Issue #477245738**](https://issuetracker.google.com/issues/477245738))*
- *An issue where Live Translate and Rules were incorrectly categorized in the System menu. ([**Issue #476754995**](https://issuetracker.google.com/issues/476754995))*
- *A critical System UI crash and subsequent device instability triggered by repeated navigation into Display and Touch settings. ([**Issue #474486679**](https://issuetracker.google.com/issues/474486679))*
- *A persistent crash that prevented users from opening Wallpaper \& style settings from the home screen. ([**Issue #478520173**](https://issuetracker.google.com/issues/478520173))*
- *A UI layout issue in the Wireless Debugging QR scanner where the back arrow overlapped the QR icon. ([**Issue #474769647**](https://issuetracker.google.com/issues/474769647))*
- *An issue in the Sound settings where ringtone previews failed to play upon selection. ([**Issue #355086959**](https://issuetracker.google.com/issues/355086959), [**Issue #375840924**](https://issuetracker.google.com/issues/375840924), [**Issue #381007949**](https://issuetracker.google.com/issues/381007949), [**Issue #381077928**](https://issuetracker.google.com/issues/381077928), [**Issue #419301121**](https://issuetracker.google.com/issues/419301121), [**Issue #452646483**](https://issuetracker.google.com/issues/452646483), [**Issue #468837747**](https://issuetracker.google.com/issues/468837747))*
- *A bug that caused redundant notifications to appear following a system update by improving the notification service logic to correctly clear stale alerts during the post-update initialization process. ([**Issue #454647834**](https://issuetracker.google.com/issues/454647834))*
- *A GPU shader compiler optimization bug on Pixel 6 Pro that caused specific GLSL mathematical expressions to evaluate incorrectly as constants, resulting in visual rendering artifacts in apps. ([**Issue #473226715**](https://issuetracker.google.com/issues/473226715))*

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
- [`CONFIG_COLOR_MODE`](https://developer.android.com/reference/android/content/pm/ActivityInfo#CONFIG_COLOR_MODE)
- [`CONFIG_UI_MODE`](https://developer.android.com/reference/android/content/pm/ActivityInfo#CONFIG_UI_MODE) (only when the UI mode changes to [`UI_MODE_TYPE_DESK`](https://developer.android.com/reference/android/content/res/Configuration#UI_MODE_TYPE_DESK) or from [`UI_MODE_TYPE_DESK`](https://developer.android.com/reference/android/content/res/Configuration#UI_MODE_TYPE_DESK) to another type)

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