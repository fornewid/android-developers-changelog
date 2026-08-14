---
title: https://developer.android.com/about/versions/14/behavior-changes-all
url: https://developer.android.com/about/versions/14/behavior-changes-all
source: md.txt
---

The Android 14 platform includes behavior changes that might affect your app.
The following behavior changes apply to *all apps* when they run on Android 14,
regardless of
[`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target). You should
test your app and then modify it as needed to support these properly, where
applicable.

Make sure to also review the list of [behavior changes that only affect apps
targeting Android 14](https://developer.android.com/about/versions/14/behavior-changes-14).

## Core functionality

### Schedule exact alarms are denied by default

Exact alarms are meant for user-intentioned notifications, or for actions that
need to happen at a precise time. Starting in Android 14, the
[`SCHEDULE_EXACT_ALARM`](https://developer.android.com/reference/android/Manifest.permission#SCHEDULE_EXACT_ALARM)
permission is **no longer being pre-granted to most newly installed apps
targeting Android 13 and higher**---the permission is denied by default.

Learn more about the [changes to the permission for scheduling exact
alarms](https://developer.android.com/about/versions/14/changes/schedule-exact-alarms).

### Context-registered broadcasts are queued while apps are cached

On Android 14, the system can
[place context-registered broadcasts in a queue](https://developer.android.com/develop/background-work/background-tasks/broadcasts#android-14) while the app
is in the [cached state](https://developer.android.com/guide/components/activities/process-lifecycle). This is similar to the queuing
behavior that Android 12 (API level 31) introduced for async binder
transactions. Manifest-declared broadcasts aren't queued, and apps are removed
from the cached state for broadcast delivery.

When the app leaves the cached state, such as returning to the foreground, the
system delivers any queued broadcasts. Multiple instances of certain broadcasts
might be merged into one broadcast. Depending on other factors, such as system
health, apps might be removed from the cached state, and any previously queued
broadcasts are delivered.

### Apps can kill only their own background processes

Starting in Android 14, when your app calls [`killBackgroundProcesses()`](https://developer.android.com/reference/android/app/ActivityManager#killBackgroundProcesses(java.lang.String)),
the API can kill only the background processes of your own app.

If you pass in the package name of another app, this method has no effect on
that app's background processes, and the following message appears in Logcat:

    Invalid packageName: com.example.anotherapp

Your app shouldn't use the `killBackgroundProcesses()` API or otherwise attempt
to influence the process lifecycle of other apps, even on older OS versions.
Android is designed to keep cached apps in the background and kill them
automatically when the system needs memory. If your app kills other apps
unnecessarily, it can reduce system performance and increase battery consumption
by requiring full restarts of those apps later, which takes significantly more
resources than resuming an existing cached app.

> [!NOTE]
> **Note:** It isn't possible for a 3rd-party application to improve the memory, power, or thermal behavior of an Android device. You should ensure that your app is compliant with [Google Play's policy regarding misleading claims](https://support.google.com/googleplay/android-developer/answer/9888077#zippy=%2Cexamples-of-common-violations).

### MTU is set to 517 for the first GATT client requesting an MTU

Starting from Android 14, the Android Bluetooth stack more strictly adheres to
[Version 5.2 of the Bluetooth Core Specification](https://www.bluetooth.com/wp-content/uploads/2020/01/Bluetooth_5.2_Feature_Overview.pdf) and requests
the BLE ATT MTU to 517 bytes when the first GATT client requests an MTU using
the [`BluetoothGatt#requestMtu(int)`](https://developer.android.com/reference/android/bluetooth/BluetoothGatt#requestMtu(int)) API, and disregards all subsequent MTU
requests on that ACL connection.

> [!NOTE]
> **Note:** This change doesn't have an impact unless the peripheral device isn't handling the MTU negotiation properly and accepting any MTU size even if it doesn't support it. In such cases, it could cause issues when your app sends large amounts of data from Android 14 devices.

To address this change and make your app more robust, consider the following
options:

- Your peripheral device should respond to the Android device's MTU request with a reasonable value that can be accommodated by the peripheral. The final negotiated value will be a minimum of the Android requested value and the remote provided value (for example, `min(517, remoteMtu)`)
  - Implementing this fix could require a firmware update for peripheral
- Alternatively, limit your GATT characteristic writes based on the minimum between the known supported value of your peripheral and the received MTU change
  - A reminder that you should reduce 5 bytes from the supported size for the headers
  - For example: `arrayMaxLength = min(SUPPORTED_MTU,
    GATT_MAX_ATTR_LEN(517)) - 5`

### New reason an app can be placed in the restricted standby bucket

Android 14 introduces a new reason an app can be placed into the [restricted standby bucket](https://developer.android.com/topic/performance/appstandby#restricted-bucket).
The app's jobs trigger ANR errors multiple times due to [`onStartJob`](https://developer.android.com/reference/android/app/job/JobService#onStartJob(android.app.job.JobParameters)),
[`onStopJob`](https://developer.android.com/reference/android/app/job/JobService#onStopJob(android.app.job.JobParameters)), or [`onBind`](https://developer.android.com/reference/android/app/Service#onBind(android.content.Intent)) method timeouts.
(See [JobScheduler reinforces callback and network behavior](https://developer.android.com/about/versions/14/behavior-changes-14#jobscheduler-reinforces-behavior) for changes
to `onStartJob` and `onStopJob`.)

> [!NOTE]
> **Note:** See [power management](https://developer.android.com/topic/performance/power/power-details) to see how the app is impacted if it is placed into the restricted bucket. The app is moved back to the [active](https://developer.android.com/topic/performance/appstandby#active-bucket) bucket when the user launches the app to the foreground, just as in previous Android versions.

To track whether or not the app has entered the restricted standby bucket,
we recommend logging with the API [`UsageStatsManager.getAppStandbyBucket()`](https://developer.android.com/reference/android/app/usage/UsageStatsManager#getAppStandbyBucket())
on job execution or [`UsageStatsManager.queryEventsForSelf()`](https://developer.android.com/reference/android/app/usage/UsageStatsManager#queryEventsForSelf()) on app startup.

### mlock limited to 64 KB

In Android 14 (API level 34) and higher, the platform reduces the maximum memory
that can be locked using [`mlock()`](https://developer.android.com/reference/android/system/Os#mlock(long,%20long)) to 64 KB per process. In
previous versions, the limit was 64 MB per process. This restriction
promotes better memory management across apps and the system. To provide more
consistency across devices, Android 14 adds [a new CTS test](https://cs.android.com/android/platform/superproject/main/+/main:system/core/init/init_test.cpp;l=667?q=MemLockLimit) for the
new `mlock()` limit on compatible devices.

### System enforces cached-app resource usage

[By design](https://developer.android.com/guide/components/activities/process-lifecycle), an app's process is in a cached state when it's moved to the
background and no other app process components are running. Such an app process
is subject to being killed due to system memory pressure. Any work that
`Activity` instances perform after the `onStop()` method has been called and
returned, while in this state, is unreliable and strongly discouraged.

Android 14 introduces consistency and enforcement to this design. Shortly after
an app process enters a cached state, background work is disallowed, until a
process component re-enters an active state of the lifecycle.

Apps that use typical framework-supported lifecycle APIs -- such as
[services](https://developer.android.com/guide/components/services), [`JobScheduler`](https://developer.android.com/reference/android/app/job/JobScheduler), and [Jetpack WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager) -- shouldn't be
impacted by these changes.

## User experience

### Changes to how users experience non-dismissible notifications

If your app shows non-dismissable foreground notifications to users, Android 14
has changed the behavior to allow users to dismiss such notifications.

This change applies to apps that prevent users from dismissing foreground
notifications by setting [`Notification.FLAG_ONGOING_EVENT`](https://developer.android.com/reference/android/app/Notification#FLAG_ONGOING_EVENT) through
[`Notification.Builder#setOngoing(true)`](https://developer.android.com/reference/android/app/Notification.Builder#setOngoing(boolean)) or
[`NotificationCompat.Builder#setOngoing(true)`](https://developer.android.com/reference/android/app/Notification.Builder#setOngoing(boolean)). The behavior of
`FLAG_ONGOING_EVENT` has changed to make such notifications actually
dismissable by the user.

These kinds of notifications are still non-dismissable in the following
conditions:

- When the phone is locked
- If the user selects a **Clear all** notification action (which helps with accidental dismissals)

Also, this new behavior doesn't apply to notifications in the
following use cases:

- [`CallStyle`](https://developer.android.com/reference/androidx/core/app/NotificationCompat.CallStyle) notifications
- Device policy controller (DPC) and supporting packages for enterprise
- Media notifications
- The default Search Selector package

### Data safety information is more visible

To enhance user privacy, Android 14 increases the number of places where the
system shows the information you have declared in the Play Console form.
Currently, users can view this information in the **Data safety** section on
your app's listing in Google Play.

We encourage you to review your app's location data sharing policies and take a
moment to make any applicable updates to your app's [Google Play Data safety
section](https://support.google.com/googleplay/android-developer/answer/10787469).

Learn more in the guide about how [data safety information is more visible](https://developer.android.com/about/versions/14/changes/data-safety)
on Android 14.

## Accessibility

### Non-linear font scaling to 200%

Starting in Android 14, the system supports font scaling up to 200%, providing
users with additional accessibility options.

If you already use scaled pixels (sp) units to define text sizing, then this
change probably won't have a high impact on your app. However, you should
[perform UI testing with the maximum font size enabled
(200%)](https://developer.android.com/about/versions/14/features#test-scaling) to
ensure that your app can accommodate larger font sizes without impacting
usability.

## Security

### Minimum installable target API level

Starting with Android 14, apps with a
[`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element) lower than 23
can't be installed. Requiring apps to meet these minimum target API level
requirements improves security and privacy for users.

Malware often targets older API levels in order to bypass security and privacy
protections that have been introduced in newer Android versions. For example,
some malware apps use a `targetSdkVersion` of 22 to avoid being subjected to the
runtime permission model introduced in 2015 by Android 6.0 Marshmallow (API
level 23). This Android 14 change makes it harder for malware to avoid security
and privacy improvements.
Attempting to install an app targeting a lower API level will result in an
installation failure, with the following message appearing in Logcat:

    INSTALL_FAILED_DEPRECATED_SDK_VERSION: App package must target at least SDK version 23, but found 7

On devices upgrading to Android 14, any apps with a `targetSdkVersion` lower
than 23 will remain installed.

If you need to test an app targeting an older API level, use the following ADB
command:

```
adb install --bypass-low-target-sdk-block FILENAME.apk
```

### Media owner package names might be redacted

The media store supports queries for the [`OWNER_PACKAGE_NAME`](https://developer.android.com/reference/android/provider/MediaStore.MediaColumns#OWNER_PACKAGE_NAME) column, which
indicates the [app that stored a particular media file](https://developer.android.com/training/data-storage/shared/media#app-attribution). Starting in Android
14, this value is redacted unless at least one of the following conditions is
true:

- The app that stored the media file has a package name that is always visible to other apps.
- The app that queries the media store requests the [`QUERY_ALL_PACKAGES`](https://developer.android.com/reference/android/Manifest.permission#QUERY_ALL_PACKAGES)
  permission.

  > [!CAUTION]
  > **Caution:** Use of the `QUERY_ALL_PACKAGES` permission is [subject to Google
  > Play Policy](https://support.google.com/googleplay/android-developer/answer/10158779).

Learn more about how [Android filters package visibility](https://developer.android.com/training/package-visibility) for privacy
purposes.