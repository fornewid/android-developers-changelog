---
title: https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls
url: https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls
source: md.txt
---

Several libraries and system APIs can acquire wake locks that are attributable
to your app. This can make it difficult to identify a wake lock in your app that
might be causing a problem. If you misuse an API, that might result in your app
holding a wake lock for too long, even though you aren't calling the wake lock
APIs directly.

In scenarios where a wake lock is acquired by other APIs, you should avoid
manual wake lock acquisition.

This document lists some common wake lock names you might see when you use the
[wake lock debugging tools](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/debug-locally). You might also see these names in a report
from [vitals](https://developer.android.com/topic/performance/vitals). In some cases, the wake lock might have been
created by a library or system API. In other cases, there is a reason why the
tool is obfuscating the wake lock name you use in the app. You can use the
debugging tools to identify misbehaving wake locks, then search for the wake
lock name in this document to identify which API may be causing the problem and
how to solve it.
| **Note:** This document is not intended as a comprehensive list of wake locks that might be created by various APIs and libraries. In addition, the name of a wake lock is not usually part of a library's API, so the wake lock names in this document are subject to change.

This document covers the scenarios where wake locks might be created. In each
case, while the wake lock might be created by some other library or API, the
lock is attributed to the app which called that API. This page also describes
some APIs which don't create wake locks in situations where you might expect
them to.

- [AlarmManager](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#alarm)
- [Audio and media](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#media)
- [Bluetooth](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#bluetooth)
- [Device Sensors](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#sensor)
- [Firebase Cloud Message (FCM)](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#FCM)
- [JobScheduler](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#job)
- [Location](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#location)
- [WorkManager](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#workmanager)
- [`_UNKNOWN`](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#unknown): Shown by debugging tools if the wake lock name seems to use personally identifiable information (PII).

### AlarmManager

[`AlarmManager`](https://developer.android.com/reference/android/app/AlarmManager) acquires wake locks and attributes them to the calling
app. `AlarmManager` acquires the wake lock when the alarm goes off, and releases
the lock when the alarm broadcast's [`onReceive()`](https://developer.android.com/reference/android/content/BroadcastReceiver#onReceive(android.content.Context,%20android.content.Intent))
method finishes executing.

#### Wake lock names

`AlarmManager` creates wake locks with the name `*alarm*`. (The asterisks are
part of the wake lock name, they don't represent wild cards.)

#### Recommendation

We recommend the following practices to optimize alarm behavior:

- Use [`AlarmManager`](https://developer.android.com/reference/android/app/AlarmManager) to optimize alarm scheduling frequency.
- Only use alarm type [`RTC_WAKEUP`](https://developer.android.com/reference/android/app/AlarmManager#RTC_WAKEUP) alarms (which wake up the device) when necessary.
- Minimize the use of alarms, and avoid doing lengthy work in the [`onReceive()`](https://developer.android.com/reference/android/content/BroadcastReceiver#onReceive(android.content.Context,%20android.content.Intent)) method.

### Audio and media

Media APIs can acquire wake locks when recording or playing audio.
The wake locks are attributed to the calling app.

#### Wake lock names

Media APIs acquire wake locks with various names that begin with `Audio`:

- `AudioBitPerfect`: Used for lossless USB audio playback.
- `AudioDirectOut`: Used for lossless audio playback on a TV or special device.
- `AudioDup`: Used for playback of notifications while connected using Bluetooth or USB.
- `AudioIn`: Used for audio capture when in camcorder mode while the microphone is active.
- `AudioMix`: Used for audio playback to a common device.
- `AudioOffload`: Used for long-term music-only playback, for apps that support this mode.
- `AudioSpatial`: Used for playback of multi-channel movie or music audio on devices that support spatial audio.
- `AudioUnknown`: Used when the other situations don't apply.
- `MmapCapture`: Used for low-latency audio capture.
- `MmapPlayback`: Used for low-latency playback, such as for gaming or for professional audio applications.

#### Recommendation

We recommend the following practices:

- Don't use wake lock names that begin with `Audio`.
- If you're using the media APIs, you shouldn't need to acquire wake locks directly; you can rely on the APIs to acquire the necessary wake locks for you.
- When you use media APIs, end the media session when you no longer need it.

### Bluetooth

The platform Bluetooth APIs don't hold any wake locks attributable to the
application while Bluetooth actions occur.
To help verify Bluetooth transport occurs in the background,
schedule a task using WorkManager.

#### Recommendation

- Use [Companion Device pairing](https://developer.android.com/develop/connectivity/bluetooth/companion-device-pairing) to pair Bluetooth devices to avoid acquiring a manual wake lock during Bluetooth pairing.
- Consult the [communicate in the background](https://developer.android.com/develop/connectivity/bluetooth/ble/background) guidance to understand how to do background Bluetooth communication.
- If a manual wake lock is deemed necessary, only hold the wake lock for the duration of Bluetooth action.

### Device Sensors

There are several methods to track device sensor data such as step count,
accelerometer or gyroscope data.

On Wear OS, use [Wear Health Services](https://developer.android.com/health-and-fitness/guides/health-services) to grab device data such
as elevation, heart rate and distance travelled.

If the data is collected by other applications,
you can use [Health Connect](https://developer.android.com/health-and-fitness/guides/health-connect) combined with WorkManager
to periodically retrieve the data.

For scenarios such as tracking delta of steps or distance traveled,
you can use the [Recording API on mobile](https://developer.android.com/health-and-fitness/guides/recording-api) combined with
WorkManager to periodically retrieve the data. To access historical steps data
(such as the daily step total, or steps in the last 6 hours), Health Connect
also supports [on-device step tracking](https://developer.android.com/health-and-fitness/health-connect/features/steps) for devices running
Android 14 or higher.

In certain situations, custom device sensor tracking may be needed using
[`SensorManager`](https://developer.android.com/reference/android/hardware/SensorManager). `SensorManager` does not acquire
wake locks on behalf of the app, unless the sensor is a wake up sensor,
which can be identified using the [`isWakeUpSensor`](https://developer.android.com/reference/android/hardware/Sensor#isWakeUpSensor()) API.

#### Recommendation

Using sensors to record at high sampling rates can drain battery significantly,
here are recommendations to reduce battery drain and wake lock usage:

- If tracking step counts or distance traveled, use the [Recording API](https://developer.android.com/health-and-fitness/guides/recording-api) to record data in a battery-efficient manner. For devices running Android 14 or higher, consider [Health Connect](https://developer.android.com/health-and-fitness/health-connect/features/steps) for accessing historical device and aggregated step count.
- For passive sensor tracking on Wear OS, use [Wear Health Services](https://developer.android.com/health-and-fitness/guides/health-services) to optimize battery usage.
- Reduce your sensor frequency to less than 200hz.
- When registering a sensor with `SensorManager`, define a [`maxReportLatencyUs`](https://developer.android.com/reference/android/hardware/SensorManager#registerListener(android.hardware.SensorEventListener,%20android.hardware.Sensor,%20int)) of more than 30 seconds to use sensor batching logic and reduce the number of interrupts the application receives.
- Avoid holding a long wake lock for the full duration of sensor tracking, instead schedule alarms using [AlarmManager](https://developer.android.com/reference/android/app/AlarmManager) to poll for sensor data every 30+ seconds.

### Firebase Cloud Message (FCM)

A wake lock is acquired while delivering a
Firebase Cloud Message (FCM) broadcast to the app.
The wake lock is released once the FCM broadcast
[`onMessageReceived()`](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessagingService#onMessageReceived(com.google.firebase.messaging.RemoteMessage)) method finishes executing.

#### Wake lock names

A wake lock is acquired with the name `GOOGLE_C2DM`.

#### Recommendation

We recommend the following practices to optimize FCM behavior:

- Optimize the frequency of FCM delivery.
- Don't use [high-priority FCM](https://firebase.google.com/docs/cloud-messaging/android/message-priority) unless the message actually needs to be delivered immediately.
- Have the `onMessageReceived()` method complete as quickly as possible. See the [firebase guidance](https://firebase.google.com/docs/cloud-messaging/android/receive) for more information.

### JobScheduler

[JobScheduler](https://developer.android.com/reference/android/app/job/JobScheduler) jobs acquire wake locks while executing tasks in
the background. The wake locks are attributed to the app that created the
workers.

#### Wake lock names

The wake lock names acquired by JobScheduler depend on what version of the
Android system they're running on, and the purpose of the job.

The items surrounded by angle brackets are variables. For example,
"\<package_name\>" is the name of your app's package, not the
literal text `<package name>`. However, `*job*` is the character sequence
`*job*`, with asterisks; the asterisks are not being used as wild cards.

##### Android 15 and lower

User initiated jobs create wake locks with names following this pattern:  

    *job*u/@<name_space>@/<package_name>/<classname>

Other jobs use this pattern:  

    *job*/@<name_space>@/<package_name>/<classname>

##### Android 16 and higher

User-initiated jobs create wake locks with names following this pattern:  

    *job*u/@<name_space>@/#<trace_tag>#/<package_name>/<classname>

Expedited jobs use this pattern:  

    *job*e/@<name_space>@/#<trace_tag>#/<package_name>/<classname>

Regular jobs use this pattern:  

    *job*r/@<name_space>@/#<trace_tag>#/<package_name>/<classname>

##### Example

Suppose there's an expedited job with the namespace `backup` and the trace
tag `started`. The package name is `com.example.app`, and the class that
created the job is `com.backup.BackupFileService`.

On devices running Android 15 or lower, the wake lock would be named:  

    *job*/@backup@/com.example.app/com.backup.BackupFileService

On devices running Android 16 or higher, the wake lock would be named:  

    *job*e/@backup@/#started#/com.example.app/com.backup.BackupFileService

#### Recommendation

Audit your usage of JobScheduler tasks. In particular, follow our guidance for
[optimizing battery use for task scheduling APIs](https://developer.android.com/develop/background-work/background-tasks/optimize-battery).

### Location

[`LocationManager`](https://developer.android.com/reference/android/location/LocationManager) and [`FusedLocationProviderClient`](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient) use
wake locks to acquire and deliver the device location. The wake locks are
attributed to the app that called those APIs.

#### Wake lock names

Location services use the following names:

- `CollectionLib-SigCollector`
- `NetworkLocationLocator`
- `NetworkLocationScanner`
- `NlpCollectorWakeLock`
- `NlpWakeLock`
- `*location*`

| **Note:** The last wake lock name is the string literal "`*location*`", with asterisks. The asterisks are not being used as wildcards.

#### Recommendation

- [Optimize location use](https://developer.android.com/develop/sensors-and-location/location/battery/optimize). For example, set timeouts, batch location requests, or use passive location updates.
- If you're using the location APIs, you shouldn't need to acquire wake locks directly; you can rely on the APIs to acquire the necessary wake locks for you.

### WorkManager

[WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager) workers acquire wake locks while executing tasks in
the background. The wake locks are attributed to the app that created the
workers.

#### Wake lock names

The wake lock names acquired by WorkManager depend on what version of the
Android system they're running on.
| **Note:** The items surrounded by angle brackets are variables. For example, "\<package_name\>" is the name of your app's package, not the literal text `<package name>`. However, `*job*` is the character sequence `*job*`, with asterisks; the asterisks are not being used as wild cards.

##### Android 15 and lower

WorkManager tasks create wake locks with names following this pattern:  

    *job*/<package_name>/androidx.work.impl.background.systemjob.SystemJobService

##### Android 16 and higher

Expedited tasks create wake locks with names following this pattern:  

    *job*e/#<trace_tag>#/<package_name>/androidx.work.impl.background.systemjob.SystemJobService

Regular tasks follow this pattern:  

    *job*r/#<trace_tag>#/<package_name>/androidx.work.impl.background.systemjob.SystemJobService

By default, `<trace_tag>` is the worker name.

##### Example

Suppose there's an expedited worker named `BackupFileWorker`. The package name
is `com.example.app`.

On devices running Android 15 or lower, the wake lock would be named:  

    *job*/com.example.app/androidx.work.impl.background.systemjob.SystemJobService

On devices running Android 16 or higher and using `WorkManager 2.10.0+`,
the wake lock would be named:  

    *job*e/#BackupFileWorker#/com.example.app/androidx.work.impl.background.systemjob.SystemJobService

#### Recommendation

- Upgrade your WorkManager version to make the wake lock tags more verbose on Android 16 or higher.
- Audit your usage of WorkManager workers. In particular, follow our guidance for [optimizing battery use for task scheduling APIs](https://developer.android.com/develop/background-work/background-tasks/optimize-battery).

### _UNKNOWN

If the debugging tools think a wake lock name contains personally identifiable
information (PII), they don't display the actual wake lock name. Instead, they
label the wake lock as `_UNKNOWN`. For example, tools might do this if the wake
lock name contains an email address.

#### Recommendation

[Follow wake lock naming best practices](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/best-practices#name), and avoid using PII in the wake
lock name. If you find a wake lock named `_UNKNOWN` attributed to your app, try
to identify which wake lock that is, and give it a different name.