---
title: https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls
url: https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls
source: md.txt
---

This document helps you identify and optimize wake lock use cases in your app,
as well as highlight if there are for wake locks acquired by other libraries
or system APIs associated with this use case.
Since these wake locks are attributable to your app,
it can be challenging to pinpoint the source of a problematic wake lock.
Incorrect API usage can cause your app to be flagged for excessive wake lock
usage, even if you aren't explicitly acquiring wake locks.

This document lists some common wake lock names you might encounter when using
the [wake lock debugging tools](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/debug-locally) or in reports from [vitals](https://developer.android.com/topic/performance/vitals). These names can
originate from a library or system API, or they might be obfuscated. By using
the debugging tools to identify misbehaving wake locks and then searching for
the wake lock name in this document, you can determine which API may be causing
the problem and find recommendations on how to optimize its usage.

> [!NOTE]
> **Note:** This document provides common wake lock names but is not exhaustive. Wake lock names may also change with platform or library updates.

This document outlines common use cases for acquiring wake locks, detailing
the wake lock names used by various APIs and libraries, and provides
recommendations and best practices for optimizing and reducing wake lock usage.

- [AlarmManager](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#alarm)
- [Audio and media](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#media)
- [Bluetooth](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#bluetooth)
- [Device Sensors](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#sensor)
- [Firebase Cloud Message (FCM)](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#FCM)
- [JobScheduler](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#job)
- [Location](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#location)
- [Remote Messaging](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#remote-messaging)
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

- Refer to [choose alarm type](https://developer.android.com/develop/background-work/background-tasks/scheduling/alarms#choose-alarm-type) to decide between an inexact or exact alarm. If your alarm doesn't need to be precise, use inexact alarms to give the system more flexibility in scheduling, which can improve battery life.
- Be aware of [system-imposed alarm quotas](https://developer.android.com/topic/performance/power/power-details) and design your app to respect them.
- Avoid doing lengthy work in the [`onReceive()`](https://developer.android.com/reference/android/content/BroadcastReceiver#onReceive(android.content.Context,%20android.content.Intent)) method and schedule workers if additional processing is required after the alarm.

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

- Don't declare wake lock names that begin with `Audio`.
- If you're using the media APIs, you shouldn't need to acquire wake locks directly; you can rely on the APIs to acquire the necessary wake locks for you.
- When you use media APIs, end the media session and associated foreground service when you no longer need it.

### Bluetooth

The platform Bluetooth APIs mainly hold kernel wake locks while Bluetooth actions
occur, which are not attributable to the application.

#### Recommendation

- Use [Companion Device pairing](https://developer.android.com/develop/connectivity/bluetooth/companion-device-pairing) to pair Bluetooth devices to avoid acquiring a manual wake lock during Bluetooth pairing.
- Consult the [communicate in the background](https://developer.android.com/develop/connectivity/bluetooth/ble/background) guidance to understand how to do background Bluetooth communication.
- Using `WorkManager` is often sufficient if there is no user impact to a delayed communication. If a manual wake lock is deemed necessary, only hold the wake lock for the duration of Bluetooth activity or processing of the activity data.

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
- When registering a sensor with `SensorManager`, define a [`maxReportLatencyUs`](https://developer.android.com/reference/android/hardware/SensorManager#registerListener(android.hardware.SensorEventListener,%20android.hardware.Sensor,%20int)) of more than 30 seconds to use sensor batching logic and reduce the number of interrupts the application receives. When the device is subsequently woken by another trigger such as a user interaction, location retrieval, or a scheduled job, the system will immediately dispatch the cached sensor data.
- If your app requires both location and sensor data, synchronize their event retrieval and processing. By coalescing sensor readings onto the brief wake lock the system holds for location updates, you avoid needing a wake lock to keep the CPU awake. Use a worker or a short-duration wake lock to handle the upload and processing of this combined data.

### Firebase Cloud Message (FCM)

A wake lock is acquired while delivering a
Firebase Cloud Message (FCM) broadcast to the app.
The wake lock is released once the FCM broadcast
[`onMessageReceived()`](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessagingService#onMessageReceived(com.google.firebase.messaging.RemoteMessage)) method finishes executing.

#### Wake lock names

When a FCM message is received on the device, a brief wake lock is held with the
name `GOOGLE_C2DM`, on Android 16+ the wake lock name is `GCM_MESSAGE`.

#### Recommendation

We recommend the following practices to optimize FCM behavior:

- Optimize the frequency of FCM delivery.
- Don't use [high-priority FCM](https://firebase.google.com/docs/cloud-messaging/android/message-priority) unless the message actually needs to be delivered immediately.
- Have the `onMessageReceived()` method complete as quickly as possible or schedule a worker to continue the task if additional processing is required. See the [firebase guidance](https://firebase.google.com/docs/cloud-messaging/android/receive) for more information.

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

##### Android 16.1 and higher

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

On devices running Android 16.1 or higher, the wake lock would be named:

    *job*e/@backup@/#started#/com.example.app/com.backup.BackupFileService

#### Recommendation

- Don't acquire a manual wake lock for user initiated download/ upload use cases. Instead, use the [User-Initiated Data Transfer (UIDT)](https://developer.android.com/develop/background-work/background-tasks/uidt) API. This is the designated path for long running data transfer tasks initiated by the user.
- If you identify wake locks created by JobScheduler with high wake lock usage, it may be because you've misconfigured your job to not complete in certain scenarios. Consider analyzing the job [stop reasons](https://developer.android.com/reference/android/app/job/JobParameters#getStopReason()), particularly if you're seeing high occurrences of `STOP_REASON_TIMEOUT`.
- Audit your usage of JobScheduler tasks. In particular, follow our guidance for [optimizing battery use for task scheduling APIs](https://developer.android.com/develop/background-work/background-tasks/optimize-battery).

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

> [!NOTE]
> **Note:** The last wake lock name is the string literal "`*location*`", with asterisks. The asterisks are not being used as wildcards.

#### Recommendation

- Consult our guidance to [Optimize location usage](https://developer.android.com/develop/sensors-and-location/location/battery/optimize). Consider implementing timeouts, leveraging location request batching, or utilizing passive location updates.
- Avoid acquiring a separate, continuous wake lock for caching location data, as this is redundant and should be removed. When [requesting location updates](https://developer.android.com/develop/sensors-and-location/location/request-updates) using the `FusedLocationProvider` or `LocationManager` APIs, the system automatically triggers a device wake-up during the location event callback. Instead, store the location events in memory or storage, and process the location events periodically using `WorkManager`.

### Remote Messaging

This section discusses scenarios involving remote messaging where apps might
need to maintain connections or react to events from other devices,
potentially impacting wake lock usage. Common use cases include:

- Video or sound monitoring companion apps that need to monitor events occurring on an external device connected via a local network.
- Messaging apps that maintain a network socket connection with a desktop variant.

Most wakeups in these remote messaging scenarios are kernel wake locks. As kernel
wake locks are not attributed to the app, there are no associated wake lock names
to list here.

#### Recommendation

- If the network events can be processed on the server side, use FCM to receive information on the client. You may choose to schedule an [expedited worker](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started/define-work#expedited) if additional processing of FCM data is required.
- If events must be processed on the client side using a socket connection, a wake lock is not needed to listen for event interrupts. When data packets arrive at the Wi-Fi or cellular radio, the radio hardware triggers an interrupt in the form of a kernel wake lock. You may then choose to schedule a worker or acquire a wake lock to process the data.
- For example, if you're using [`ktor-network`](https://ktor.io/docs/server-sockets.html) to listen for data packets on a network socket, you should only acquire a wake lock when packets have been delivered to the client.

### WorkManager

[WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager) workers acquire wake locks while executing tasks in
the background. The wake locks are attributed to the app that created the
workers.

#### Wake lock names

The wake lock names acquired by WorkManager depend on what version of the
Android system they're running on.

> [!NOTE]
> **Note:** The items surrounded by angle brackets are variables. For example, "\<package_name\>" is the name of your app's package, not the literal text `<package name>`. However, `*job*` is the character sequence `*job*`, with asterisks; the asterisks are not being used as wild cards.

##### Android 15 and lower

WorkManager tasks create wake locks with names following this pattern:

    *job*/<package_name>/androidx.work.impl.background.systemjob.SystemJobService

##### Android 16.1 and higher

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

- Upgrade your WorkManager version to latest stable version to make the wake lock tags more verbose on Android 16.1 or higher.
- Audit your usage of WorkManager workers. In particular, verify it follows our guidance for [optimizing battery use for task scheduling APIs](https://developer.android.com/develop/background-work/background-tasks/optimize-battery). To make wake lock tags more verbose on Android 16.1 or higher, use the [`setTraceTag`](https://developer.android.com/reference/androidx/work/WorkRequest.Builder#setTraceTag(kotlin.String)) method on the worker to add more debug information, such as which class scheduled the worker.
- If you identify wake locks created by WorkManager with high wake lock usage, it may be because you've misconfigured your worker to not complete in certain scenarios. Consider analyzing the [worker stop reasons](https://developer.android.com/develop/background-work/background-tasks/persistent/how-to/observe#stop-reason), particularly if you're seeing high occurrences of [`STOP_REASON_TIMEOUT`](https://developer.android.com/reference/androidx/work/WorkInfo.StopReason#STOP_REASON_TIMEOUT).
- In addition to logging worker stop reasons, refer to our documentation on [debugging your workers](https://developer.android.com/develop/background-work/background-tasks/persistent/how-to/debug). Also, consider collecting and analyzing [system traces](https://developer.android.com/topic/performance/tracing) to understand when wake locks are acquired and released.

### _UNKNOWN

If the debugging tools think a wake lock name contains personally identifiable
information (PII), they don't display the actual wake lock name. Instead, they
label the wake lock as `_UNKNOWN`. For example, tools might do this if the wake
lock name contains an email address.

#### Recommendation

[Follow wake lock naming best practices](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/best-practices#name), and avoid using PII in the wake
lock name. If you find a wake lock named `_UNKNOWN` attributed to your app, try
to identify which wake lock that is, and give it a different name.