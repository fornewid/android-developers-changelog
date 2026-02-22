---
title: https://developer.android.com/about/versions/15/changes/foreground-service-types
url: https://developer.android.com/about/versions/15/changes/foreground-service-types
source: md.txt
---

# Changes to foreground service types for Android 15

We are making the following changes to foreground service types with Android 15.

### Media processing

Foreground service type to declare in manifest under
`android:foregroundServiceType`
:   `mediaProcessing`

Permission to declare in your manifest
:   `FOREGROUND_SERVICE_MEDIA_PROCESSING`

Constant to pass to`startForeground()`
:   `FOREGROUND_SERVICE_TYPE_MEDIA_PROCESSING`

Runtime prerequisites
:   None

Description

:   Service for performing time-consuming operations on media assets, like converting media to different formats. The system allows this service a limited time to run; under normal circumstances, this time limit would be 6 hours out of every 24. (This limit is shared by all of an app's`mediaProcessing`foreground services.)

:   Your app should manually stop the media processing service in the following scenario:

    - When the transcoding operation finishes or reaches a failure state, have the service call[`Service.stopForeground()`](https://developer.android.com/reference/android/app/Service#stopForeground(int))and[`Service.stopSelf()`](https://developer.android.com/reference/android/app/Service#stopSelf())to stop the service completely.

:   If the timeout period is reached, the system calls the service's[`Service.onTimeout(int, int)`](https://developer.android.com/reference/android/app/Service#onTimeout(int,%20int))method. At this time, the service has a few seconds to call[`Service.stopSelf()`](https://developer.android.com/reference/android/app/Service#stopSelf()). If the service does not call`Service.stopSelf()`, an ANR will occur with this error message: "A foreground service of*\<fgs_type\>* did not stop within its timeout:*\<component_name\>*".

    **Note** :`Service.onTimeout(int, int)`is not available on Android 14 or lower. On devices running those versions, if a media processing service reaches the timeout period, the system immediately caches the app. For this reason, your app shouldn't wait to get a timeout notification. Instead, it should terminate the foreground service or change it to a background service as soon as appropriate.

### Camera

Apps that target Android 15 or higher are not allowed to launch a camera foreground service from a`BOOT_COMPLETED`broadcast receiver. For more information, see[Restrictions on`BOOT_COMPLETED`broadcast receivers launching foreground services](https://developer.android.com/about/versions/15/behavior-changes-15#fgs-boot-completed).

### Data sync

Apps that target Android 15 or higher are not allowed to launch a data sync foreground service from a`BOOT_COMPLETED`broadcast receiver. For more information, see[Restrictions on`BOOT_COMPLETED`broadcast receivers launching foreground services](https://developer.android.com/about/versions/15/behavior-changes-15#fgs-boot-completed).

### Media playback

Apps that target Android 15 or higher are not allowed to launch a media playback foreground service from a`BOOT_COMPLETED`broadcast receiver. For more information, see[Restrictions on`BOOT_COMPLETED`broadcast receivers launching foreground services](https://developer.android.com/about/versions/15/behavior-changes-15#fgs-boot-completed).

### Media projection

Apps that target Android 15 or higher are not allowed to launch a media projection foreground service from a`BOOT_COMPLETED`broadcast receiver. For more information, see[Restrictions on`BOOT_COMPLETED`broadcast receivers launching foreground services](https://developer.android.com/about/versions/15/behavior-changes-15#fgs-boot-completed).

### Microphone

Apps that target Android 14 (API level 34) or higher are not allowed to launch a microphone foreground service from a`BOOT_COMPLETED`broadcast receiver. For more information, see[Restrictions on`BOOT_COMPLETED`broadcast receivers launching foreground services](https://developer.android.com/about/versions/15/behavior-changes-15#fgs-boot-completed).

### Phone call

Apps that target Android 15 or higher are not allowed to launch a phone call foreground service from a`BOOT_COMPLETED`broadcast receiver. For more information, see[Restrictions on`BOOT_COMPLETED`broadcast receivers launching foreground services](https://developer.android.com/about/versions/15/behavior-changes-15#fgs-boot-completed).