---
title: https://developer.android.com/develop/background-work/services/fgs/changes
url: https://developer.android.com/develop/background-work/services/fgs/changes
source: md.txt
---

The foreground service documentation describes the current behavior of
Android foreground services. The documentation gives guidance on best
practices for most apps, whether or not they target the most recent version
of Android.

This page describes some of the most recent important changes to foreground
services, and the implications for apps that aren't targeting the most
recent version of the Android platform. In many cases, best practices that
were optional for apps targeting lower API levels become mandatory for apps
that target higher API levels.

## Android 16 (API level 36)

The following changes apply to apps that run on Android 16 or higher,
regardless of what API level they target:

- Background jobs started from a foreground service now must adhere to their
  respective runtime quotas. This includes jobs scheduled directly with
  [`JobScheduler`](https://developer.android.com/reference/android/app/job/JobScheduler), as well as jobs created by other libraries like
  [WorkManager](https://developer.android.com/develop/background-work/background-tasks/persistent) or [`DownloadManager`](https://developer.android.com/reference/android/app/DownloadManager).

  To transfer data in response to a user action, consider using a
  [user-initiated data transfer job](https://developer.android.com/develop/background-work/background-tasks/uidt). These jobs are exempt from the
  ordinary job quotas.

## Android 15 (API level 35)

The following requirements apply to apps that target API
level 35 or higher:

- There are new restrictions on how long a `dataSync` foreground service can run. These restrictions are described in [Foreground service timeout
  behavior](https://developer.android.com/develop/background-work/services/fgs/timeout). Similar restrictions apply to the (new in Android 15) `mediaProcessing` foreground service type.
- [`BOOT_COMPLETED` foreground services are no longer allowed to launch certain
  foreground services](https://developer.android.com/about/versions/15/behavior-changes-15#fgs-boot-completed).
- Apps that hold the `SYSTEM_ALERT_WINDOW` permission are only allowed to launch foreground services from the background if they currently have a visible overlay window (or if they meet one of the other [exemptions from background
  start restrictions](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start#background-start-restriction-exemptions)). Previously, the exemption for those apps was broader.

## Android 14 (API level 34)

The following requirements apply to apps that target API
level 34 or higher:

- You must [declare all foreground services](https://developer.android.com/develop/background-work/services/fgs/declare) with their service types.
- Apps must request the appropriate permission type for the kind of work the foreground service will be doing. Each [foreground service type](https://developer.android.com/develop/background-work/services/fgs/service-types) has a corresponding permission type. For example, if an app launches a foreground service that uses the camera, you must request both the [`FOREGROUND_SERVICE`](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE) and [`FOREGROUND_SERVICE_CAMERA`](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_CAMERA) permissions. If an app targets API level 34 or higher and doesn't request the appropriate specific permission, the system throws a `SecurityException`.

## Android 12 (API level 31)

The following requirements apply to apps that target API
level 31 or higher:

- Apps are not allowed to launch foreground services while the app is in the background, with a few specific exceptions. For more information, and information about the exceptions to this rule, see [Restrictions on starting
  a foreground service from the background](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start).

## Android 11 (API level 30)

The following requirements apply to apps that target API
level 30 or higher:

- If an app's foreground services use the camera or microphone, the app must [declare the service](https://developer.android.com/develop/background-work/services/fgs/declare) with the [`camera`](https://developer.android.com/develop/background-work/services/fgs/service-types#camera) or [`microphone`](https://developer.android.com/develop/background-work/services/fgs/service-types#microphone) service type, respectively.

## Android 10 (API level 29)

The following requirements apply to apps that target API
level 29 or higher:

- If an app's foreground services use location information, the app must [declare the service](https://developer.android.com/develop/background-work/services/fgs/declare) with the [`location`](https://developer.android.com/develop/background-work/services/fgs/service-types#location) service type.

## Android 9 (API level 28)

Android 9 introduces the
[`FOREGROUND_SERVICE`](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE) permission. Apps running on
Android 9 that use foreground services must have that permission.

If an app that targets API level 28 or higher attempts
to create a foreground service without requesting the `FOREGROUND_SERVICE`
permission, the system throws a [`SecurityException`](https://developer.android.com/reference/java/lang/SecurityException).