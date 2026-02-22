---
title: https://developer.android.com/training/wearables/versions/5/changes
url: https://developer.android.com/training/wearables/versions/5/changes
source: md.txt
---

# Test how your app handles behavior changes

Wear OS 5 is based on Android 14 (API level 34). When you prepare your Wear OS app for use on Wear OS 5, handle the system[behavior changes that affect all apps in Android 14](https://developer.android.com/about/versions/14/behavior-changes-all), as well as the[changes for apps that target Android 14](https://developer.android.com/about/versions/14/behavior-changes-14).
| **Caution:** Before you upload your app to the Play Store,[target Android 14](https://developer.android.com/training/wearables/versions/5/update-target-sdk)and[configure an emulator](https://developer.android.com/training/wearables/get-started/creating#configure-emulator)to test your app.

## Wear OS 5 changes affecting all apps

The following behavior changes affect use cases and libraries that are specific to Wear OS. These changes affect all apps that run on Wear OS 5 or higher, regardless of target SDK version.

### Privacy dashboard

Wear OS 5 adds support for the[privacy dashboard](https://developer.android.com/training/wearables/principles#privacy-dashboard), which offers users a centralized view of each app's data usage.

### New watches only show watch faces that use Watch Face Format

Watches that launch with Wear OS 5 or higher only support watch faces that use the[Watch Face Format](https://developer.android.com/training/wearables/wff). For this reason, we recommend that you migrate to using the Watch Face Format.

## Wear OS 5 changes affecting apps that target Android 14

The following changes affect your app only if you[update your target SDK version to Android 14](https://developer.android.com/training/wearables/versions/5/update-target-sdk), the version on which Wear OS 5 is based.

### Always-on apps can move to the background

Starting in Wear OS 5, the[system moves always-on apps to the background](https://developer.android.com/training/wearables/always-on#background)after they're visible in ambient mode for a certain period of time. Users can configure the timeout in system settings.

### Exercise-recording apps must declare a foreground service type

If your app records exercise as part of a user's workout session on devices that run Wear OS 5 or higher, you must[specify the`health`foreground service type](https://developer.android.com/health-and-fitness/guides/health-services/active-data#structure)in the foreground service that invokes[`ExerciseClient`](https://developer.android.com/reference/kotlin/androidx/health/services/client/ExerciseClient). Additionally, if your app can monitor location information during the workout session, you must also specify the`location`foreground service type.

### Some off-wrist devices stay unlocked longer

On supported devices that run Wear OS 5 or higher, if the user turns off wrist detection and then takes the device off of their wrist, the[system keeps the device unlocked for a longer period of time](https://developer.android.com/training/wearables/apps/auth-wear#device-unlocked-longer)than it would otherwise.

If your app requires a higher level of security---such as when displaying potentially sensitive or private data---check whether wrist detection is enabled.

### Draggable content might overlap system gesture activation points

Starting in Wear OS 5, the system treats motion event gestures separately from gesture navigation used in the system's UI.

If your app's UI includes large draggable spaces that overlap system gesture areas, you might need to add system gesture exclusion rectangles for these views. To do so, call[`setSystemGestureExclusionRects()`](https://developer.android.com/reference/android/view/View#setSystemGestureExclusionRects(java.util.List%3Candroid.graphics.Rect%3E))to instruct the system UI to ignore navigation gestures in the given areas. This is similar to how you[handle conflicting app gestures](https://developer.android.com/develop/ui/views/touch-and-input/gestures/gesturenav#conflicting-gestures)in your mobile app to provide an edge-to-edge UI experience.

You can use the`setSystemGestureExclusionRects()`API to have the system UI respond to gesture requests differently. For example, the system UI might show additional UI hints, like a horizontal bar, to confirm the user's intent.

### Restrictions to implicit and pending intents

If you use[tiles](https://developer.android.com/training/wearables/tiles)in your app, check whether your intents are affected by the[restrictions to implicit and pending intents](https://developer.android.com/about/versions/14/behavior-changes-14#safer-intents).

### Some notifications are still non-dismissible

When using the handheld version of your app on a device that runs Android 14 (API level 34) or higher,[users can dismiss notifications](https://developer.android.com/about/versions/14/behavior-changes-all#non-dismissable-notifications)that, on previous versions, were non-dismissible.

On Wear OS 5 and higher, however, these notifications are still non-dismissible.

## Other changes from Android 14

The following changes from Android 14 are most likely to affect your Wear OS app.

### Android 14 changes that affect all apps

- [Schedule exact alarms are denied by default](https://developer.android.com/about/versions/14/behavior-changes-all#schedule-exact-alarms)
- [Context-registered broadcasts are queued while apps are cached](https://developer.android.com/about/versions/14/behavior-changes-all#pending-broadcasts-queued)
- [Additional reason an app can be placed in the restricted standby bucket](https://developer.android.com/about/versions/14/behavior-changes-all#triggers-to-restricted-bucket)

### Android 14 changes that affect apps targeting API level 34

- [Foreground service types are required](https://developer.android.com/about/versions/14/behavior-changes-14#fgs-types)
- [Non-linear font scaling](https://developer.android.com/about/versions/14/features#non-linear-font-scaling)(only affects view-based UI elements)
- [Enforcement of`BLUETOOTH_CONNECT`permission in`BluetoothAdapter`](https://developer.android.com/about/versions/14/behavior-changes-14#enforce-bluetooth_connect)
- [`JobScheduler`reinforces callback and network behavior](https://developer.android.com/about/versions/14/behavior-changes-14#jobscheduler-reinforces-behavior)
- [Runtime-registered broadcasts receivers must be explicitly exported or not exported](https://developer.android.com/about/versions/14/behavior-changes-14#runtime-receivers-exported)
- [Safer dynamic code loading](https://developer.android.com/about/versions/14/behavior-changes-14#safer-dynamic-code-loading)
- [Additional restrictions on starting activities from the background](https://developer.android.com/about/versions/14/behavior-changes-14#background-activity-restrictions)
- [User can grant partial access to photos and videos](https://developer.android.com/about/versions/14/behavior-changes-14#partial-photo-library-access)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Privacy changes in Android 10](https://developer.android.com/about/versions/10/privacy/changes)
- [Connect to a GATT server {:#connect}](https://developer.android.com/develop/connectivity/bluetooth/ble/connect-gatt-server)
- [Communicate in the background](https://developer.android.com/develop/connectivity/bluetooth/ble/background)