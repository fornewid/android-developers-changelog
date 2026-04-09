---
title: https://developer.android.com/games/playgames/pc-compatibility
url: https://developer.android.com/games/playgames/pc-compatibility
source: md.txt
---

[Google Play Games on PC](https://developer.android.com/games/playgames/overview) requires that you make PC
compatibility and optimization changes to your game. These changes ensure your
game can run on a PC and the user experience is optimized for the platform.

Additionally, Google Play Games on PC has graphics, device input, and
cross-device play requirements. For more information, see the
[Get started guide](https://developer.android.com/games/playgames/start#requirements-checklist).

When making the PC compatibility and optimization changes (other than x86-64
support), you can set up your game to
[detect Google Play Games on PC](https://developer.android.com/games/playgames/pc-compatibility#detect-hpe) and then disable or enable
platform-specific features. This allows you to use the same APK or App bundle
for your Android mobile and PC releases.

> [!NOTE]
> **Note:** For information about the minimum requirements for players to run Google Play Games on PC on a PC, see [minimum PC requirements](https://support.google.com/googleplay?p=eligibility_requirements) in Google Help Center.

Here's a summary of the requirements and recommendations on this page:

- [Include x86-64 ABI](https://developer.android.com/games/playgames/pc-compatibility#x86-requirement) (required)
- [Detect Google Play Games at runtime](https://developer.android.com/games/playgames/pc-compatibility#detect-hpe) (recommended)
- [Handle the onPause event](https://developer.android.com/games/playgames/pc-compatibility#lifecycle-events) (recommended)
- [Update UI elements](https://developer.android.com/games/playgames/pc-compatibility#ui-compatibility) (required)
- [Disable Android app permissions dialogs](https://developer.android.com/games/playgames/pc-compatibility#permissions-dialogs) (required)
- [Disable unsupported Android features and permissions](https://developer.android.com/games/playgames/pc-compatibility#unsupported-android-features) (required)
- [Replace WebViews with browser intents](https://developer.android.com/games/playgames/pc-compatibility#browser-intent) (recommended)
- [Disable unsupported Google Play Service APIs](https://developer.android.com/games/playgames/pc-compatibility#unsupported-google-apis) (required)
- [Enable scoped storage](https://developer.android.com/games/playgames/pc-compatibility#scoped-storage) (required)
- [Migrate to Google Analytics 4](https://developer.android.com/games/playgames/pc-compatibility#analytics) (recommended)

> [!NOTE]
> **Note:** If your game is using Unity, you could checkout this [Google Play Games Unity Package](https://github.com/android/games-samples/tree/main/googleplaygamesforpc/unity_projects/platform_utils_package) to automate routines for Google Play Games on PC development with Unity.

## Include x86-64 ABI architecture

*Required by the [release process](https://developer.android.com/games/playgames/checklist)*

All the libraries included in your game require x86-64 ABI compatible versions
to ensure the best performance and stability on the platform.

If it's technically infeasible for your game to ship a 64 bit x86 executable,
you must reach out to the review team for an exception. Your game can't reach
[full certification](https://developer.android.com/games/playgames/pc-compatibility#target_architecture_in_unity) with an
exception, but can be placed into the catalog as a "playable" game.

### Library compilation

To ensure the greatest x86-64 processor compatibility, don't use the atom
instruction set when compiling your libraries. For example, when using `gcc`
avoid using `-march=atom` and instead use `-march=x86-64`.

### Target architecture in Unity

Some versions of Unity 2019 and 2020 lack x86-64 architecture support on
Android. Make sure you're using Unity 2019.4.31f1, 2020.3.19f1, or later.

If your game uses a compatible version of the Unity game engine, do the
following to enable x86-64 Android targets:

1. Go to **Player Settings \> Other Settings \> Configuration \> Scripting
   Backend** and select **IL2CPP** from the dropdown menu to enable the
   IL2CPP Scripting Backend.

2. Enable x86-64 Android targets for your version of Unity:

   - **Unity 2018 and earlier:** go to **Player Settings \> Other Settings \>
     Target Architecture** , and select the **x86** checkbox.
     Since Unity 2018 only supports x86 targets,
     you won't be able to build x86-64.
     This build will require an exception from the review team.
     Please reach out to your google contact to request an x86 exception.

   - **Unity 2019 Long Term Support (LTS) release and later** : go to **Player
     Settings \> Other Settings \> Target Architectures**
     and enable **x86-64 (ChromeOS)**.

## Detect Google Play Games on PC

You can detect the Google Play Games on PC platform at runtime, allowing you
to enable or disable platform-specific features in your game.

Check for the system feature `com.google.android.play.feature.HPE_EXPERIENCE` to
determine if your game is running on the Google Play Games on PC platform:

### Kotlin

```kotlin
    var isPC = packageManager.hasSystemFeature("com.google.android.play.feature.HPE_EXPERIENCE")
  
```

### Java

```java
    PackageManager pm = getPackageManager();
    boolean isPC = pm.hasSystemFeature("com.google.android.play.feature.HPE_EXPERIENCE")
  
```

### C#

```c#
var unityPlayerClass = new AndroidJavaClass("com.unity3d.player.UnityPlayer");
var currentActivity = unityPlayerClass.GetStatic<AndroidJavaObject>("currentActivity");
var packageManager = currentActivity.Call<AndroidJavaObject>("getPackageManager");
var isPC = packageManager.Call<bool>("hasSystemFeature", "com.google.android.play.feature.HPE_EXPERIENCE");
  
```

## Handle Android lifecycle Events

It's important to handle the
[`onPause`](https://developer.android.com/guide/components/activities/activity-lifecycle#onpause)
([c++](https://developer.android.com/ndk/reference/struct/a-native-activity-callbacks#struct_a_native_activity_callbacks_1ad7bd685219371874af86549772d7fbaa))
event in the Google Play Games on PC environment. Your game is visible
when a player activates the emulator overlay, so failing to listen to the
`onPause` event can lead to a poor user experience.

## Update the UI

Certain UI elements and gestures are not suitable on PC and should be updated.

Required:

- Replace UI actions that need two or more fingers (multi-touch gestures). For example, you should replace pinch-to-zoom and other multi-touch gestures with the corresponding mouse and keyboard input. For details about device input changes, see [Input support](https://developer.android.com/games/playgames/input).

Recommended:

- All user-visible text should say "click" instead of "tap".
- Scrollable lists should have scrollbars.
- Areas that users can pan should either have scrollbars or some other way to traverse large distances quickly.
- Don't display a clickable keyboard on screen for text entry.
- All text entries should be within the text field bounds.
- Clicks on visible elements should:
  - Accept a click *anywhere* within the visible bounds of the element.
  - Not accept a click in the area outside of the visible element.
- Dialogs should have a visible close button. Don't detect a click outside of the dialog bounds.

## Disable most permissions dialogs

With the exception of microphone and notification permissions,
Google Play Games on PC doesn't display permissions dialogs, so you shouldn't
attempt to display them or request permissions at runtime. If you
[displayed permission dialogs previously](https://developer.android.com/training/permissions/usage-notes#be_transparent),
you should update your game so it no longer displays them on PCs.

## Unsupported Android features and permissions

*Required by the [release process](https://developer.android.com/games/playgames/checklist)*

Some common hardware features on mobile phones and tablets are not available on
PC. This includes hardware features such as the camera or a player's location.
Any game that requires missing features can't be downloaded and installed on a
player's PC. Requests for any missing features on a PC automatically fail.

You can view a complete list of available features by typing:

    adb shell pm list features

To make your game compatible with PCs, the following changes are required:

- **Do** mark features as optional in your app manifest by adding
  `android:required="false"` to the `<uses-feature>` declaration. This only
  applies to the features already declared in your app manifest.

- **Don't** attempt to use missing features at runtime. If you are using the
  same APK on both your mobile and PC tracks, [detect the PC environment at
  runtime](https://developer.android.com/games/playgames/pc-compatibility#detect-hpe) and avoid the relevant
  code paths.

- **Don't** request unsupported Android permissions at runtime. If you are using
  the same APK on both your mobile and PC tracks, [detect the PC environment at
  runtime](https://developer.android.com/games/playgames/pc-compatibility#detect-hpe) and avoid the relevant
  code paths. You don't need to update your manifest.

For more information about app manifest compatibility, see the
[Chromebook app manifest compatibility](https://developer.android.com/topic/arc/manifest) guide.

### Functional testing requirements

Remove these hardware features before submitting the first
[test build](https://developer.android.com/games/playgames/checklist#m1-requirements) to
Google Play Console:

- `android.hardware.wifi`
- `android.hardware.bluetooth`
- `android.hardware.camera`
- `android.hardware.location`

Some of these features may be listed as supported when running
`pm list features` for compatibility reasons, but aren't fully implemented. For
more information about how to remove the `android.hardware.wifi` feature, see
[Monitor connectivity status and connection metering](https://developer.android.com/training/monitoring-device-state/connectivity-status-type). For a
complete list of unsupported features, see the [app manifest compatibility guide
for Chromebooks](https://developer.android.com/topic/arc/manifest#unsupported-hardware-features).

### Quality testing requirements

These commonly-used hardware features *aren't compatible* with PCs, so you must
remove them before the
[final submission](https://developer.android.com/games/playgames/checklist#m2-requirements) to
Google Play Console:

- `android.hardware.audio.pro`
- `android.hardware.bluetooth`
- `android.hardware.camera`
- `android.hardware.consumerir`
- `android.hardware.location`
- `android.hardware.nfc`
- `android.hardware.sensor.light`
- `android.hardware.sensor.accelerometer`
- `android.hardware.sensor.barometer`
- `android.hardware.sensor.compass`
- `android.hardware.sensor.gyroscope`
- `android.hardware.sensor.proximity`
- `android.hardware.telephony`
- `android.hardware.touchscreen`
- `android.hardware.usb.accessory`
- `android.hardware.usb.host`
- `android.hardware.wifi`
- `android.software.midi`

### Unsupported permissions

The following commonly-used permissions *aren't supported* on PCs, so your game
must disable them for Google Play Games on PC:

- `android.permission.ACCESS_COARSE_LOCATION`
- `android.permission.ACCESS_FINE_LOCATION`
- `android.permission.ACCESS_WIFI_STATE`
- `android.permission.BLUETOOTH`
- `android.permission.CAMERA`
- `android.permission.FOREGROUND_SERVICE`
- `android.permission.GET_ACCOUNTS`
- `android.permission.INSTALL_PACKAGES`
- `android.permission.READ_CONTACTS`
- `android.permission.READ_EXTERNAL_STORAGE`
- `android.permission.READ_PHONE_STATE`
- `android.permission.RECEIVE_BOOT_COMPLETED`
- `android.permission.REQUEST_INSTALL_PACKAGES`
- `android.permission.SYSTEM_ALERT_WINDOW`
- `android.permission.USE_CREDENTIALS`
- `android.permission.WRITE_EXTERNAL_STORAGE`
- `android.permission.WRITE_SETTINGS`
- `com.google.android.gms.permission.ACTIVITY_RECOGNITION`

## External websites and WebViews

[A browser intent](https://developer.android.com/guide/components/intents-common#Browser)
loads in a PC's native web browser instead of one in the
Google Play Games on PC environment. This is an ideal experience for players in
most situations.

To ease porting, Google Play Games on PC does support
[WebView](https://developer.android.com/reference/android/webkit/WebView). Since
this opens in the Google Play Games on PC environment, it will lack the typical
desktop browser. If you were previously using `WebView` for sharing your Terms
of Service, Privacy Policy, or other similar content, you should instead
[invoke a browser intent](https://developer.android.com/guide/components/intents-common#Browser).

## Disable unsupported Google Play Service APIs

*Required by the [release process](https://developer.android.com/games/playgames/checklist)*

Google Play Games on PC ships its own Google Play Services variant that
contains only a subset of the Google Play Services APIs. You need to confirm
that your application does not strongly depend on modules that are omitted or
unsupported on PC. Consider that some modules may be available, but their
functionality is not supported at all times. For example, Firebase Cloud
Messaging will not function when Google Play Games on PC is closed.

### Supported Modules

These modules are currently available and supported by
Google Play Games on PC, with plans for additional feature support:

- [Google Sign-In](https://developers.google.com/identity/sign-in/android/start-integrating) (not including [account transfer](https://developers.google.com/android/reference/com/google/android/gms/auth/api/accounttransfer/package-summary), [SmartLock](https://developers.google.com/identity/smartlock-passwords/android), [SMS verification](https://developers.google.com/identity/sms-retriever), [Password complexity calculation](https://developers.google.com/android/reference/com/google/android/gms/auth/managed/password/package-summary))
- [Cronet](https://developer.android.com/guide/topics/connectivity/cronet/start)
- [Google Play Games Services](https://developers.google.com/games/services/android/quickstart)
- [Tasks](https://developers.google.com/android/reference/com/google/android/gms/tasks/package-summary)
- [Vision](https://developers.google.com/android/reference/com/google/android/gms/vision/barcode/package-summary)
- [Google Pay](https://developers.google.com/android/reference/com/google/android/gms/wallet/package-summary)

### Limited Support

The following modules are partially functional. We will do our best to support
them on Google Play Games on PC, but we cannot guarantee their functionality.

- [Google Cloud Messaging](https://developers.google.com/android/reference/com/google/android/gms/gcm/package-summary) (Deprecated, use Firebase Cloud Messaging)
- [Firebase Authentication](https://firebase.google.com/docs/auth) (Phone number auth does not work)
- [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging)
- [Firebase Common Libraries](https://developers.google.com/android/reference/com/google/firebase/package-summary)
- [Firebase ML](https://firebase.google.com/docs/ml)
- [Firebase Remote Config](https://firebase.google.com/docs/remote-config)
- [Firebase Analytics](https://firebase.google.com/docs/analytics)

### Not Supported

These modules are not supported in Google Play Games on PC, but don't cause
issues in Google Play Games on PC when they fail:

- [Google Analytics](https://developers.google.com/android/reference/com/google/android/gms/analytics/package-summary) (Deprecated, use Firebase Analytics)
- [Google Cast](https://developers.google.com/cast/docs/android_sender)
- [Awareness API](https://developers.google.com/awareness)
- [Drive](https://developers.google.com/android/reference/com/google/android/gms/drive/package-summary) (Deprecated, will be removed soon)
- [FIDO](https://developers.google.com/identity/fido/android/native-apps)
- [Firebase Realtime Database](https://firebase.google.com/docs/database)
- [Firestore](https://firebase.google.com/docs/firestore)
- [Firebase A/B Testing](https://firebase.google.com/docs/ab-testing)
- [Google Fit](https://developers.google.com/fit/android/get-started)
- [Address API](https://developers.google.com/android/reference/com/google/android/gms/identity/intents/package-summary)
- [Instant Apps API](https://developers.google.com/android/reference/com/google/android/gms/instantapps/package-summary)
- [Location API](https://developers.google.com/location-context/)
- [Google Maps SDK](https://developers.google.com/maps/documentation/android-sdk/overview)
- [Nearby](https://developers.google.com/android/reference/com/google/android/gms/nearby/package-summary)
- [Panorama](https://developers.google.com/android/reference/com/google/android/gms/panorama/package-summary)
- [Places](https://developers.google.com/android/reference/com/google/android/gms/location/places/package-summary)
- [Google+](https://developers.google.com/android/reference/com/google/android/gms/plus/package-summary)
- [SafetyNet](https://developer.android.com/training/safetynet) (Deprecated, please fill the [interest form](https://services.google.com/fb/forms/play-integrity-api-eap-interest/) for opting-in to the upcoming [Play Integrity API](https://developer.android.com/google/play/integrity))
- [Google Tag Manager](https://developers.google.com/tag-manager/android/v5)
- [Wear OS](https://developers.google.com/android/reference/com/google/android/gms/wearable/package-summary)

### Broken

*Required by the [release process](https://developer.android.com/games/playgames/checklist)*

You must not use these modules on PCs because they can cause unexpected
behavior in Google Play Games on PC.

- [Firebase Dynamic Links](https://firebase.google.com/docs/dynamic-links)

### Enable scoped storage

*Required by the [release process](https://developer.android.com/games/playgames/checklist)*

This section applies if your game reads or writes to external storage. Scope
storage enforcement is required as an alternative way to read and write to
storage. Doing this removes the need to prompt the player for these sensitive
permissions:

- `android.permission.READ_EXTERNAL_STORAGE`
- `android.permission.WRITE_EXTERNAL_STORAGE`

For more information on scoped storage see:

- [How to enable scoped storage](https://developer.android.com/about/versions/11/privacy/storage)
- [Best practices for handling non-media files](https://developer.android.com/training/data-storage/use-cases#handle-non-media-files)

## Analytics

Legacy Google Analytics products don't function in Google Play Games on PC. If
this applies to your games, you should migrate it to
[Google Analytics 4](https://support.google.com/analytics/answer/10089681).

This should only affect your game if you're currently using
[Google Analytics 360](https://support.google.com/analytics/answer/3437434). If
you're using the [Firebase SDK](https://firebase.google.com/docs/analytics) to
track analytics events in your game and can see your game as a property in the
[Google Analytics Console](https://analytics.google.com/), then you don't have
to take any further action.