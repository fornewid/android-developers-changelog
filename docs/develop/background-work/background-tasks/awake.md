---
title: https://developer.android.com/develop/background-work/background-tasks/awake
url: https://developer.android.com/develop/background-work/background-tasks/awake
source: md.txt
---

# Choose the right API to keep the device awake

When the user leaves their Android-powered device idle, it quickly goes into the suspend state to avoid draining the battery. However, there are times when an app needs to prevent the CPU from going to the suspend state. In some cases, the app may need to keep the screen on while it's working. In other cases, the app doesn't need to keep the screen on but still needs the CPU to be active.

The approach you take depends on the needs of your app. However, a general rule is that you should use the most lightweight approach possible, to minimize your app's impact on system resources. This document helps you choose the correct Android technology for your situation.
| **Note:** You may be familiar with**wake locks**. An app can set a wake lock to keep the device from suspending. However, using a wake lock can quickly drain the device battery. You should only use a wake lock if there's no other option that will do what you need. If you do use a wake lock, you should release it as soon as possible.

## Choose the right technology

The best option for keeping your device awake depends on your app's needs. This section helps you choose the right approach.

![Flowchart summarizing how to choose the right approach for keeping the device awake. The contents of the flowchart are expanded on in the following text.](https://developer.android.com/static/images/develop/background-work/background-tasks/keep-awake-choose-option.svg)

- Does your app need to keep the screen on?
  - If**Yes** , see[Keep the screen on](https://developer.android.com/develop/background-work/background-tasks/awake/screen-on). There may be a special-purpose API that does what you need; for example, if you're implementing a phone-call UI, you can use the[Android telecom framework](https://developer.android.com/reference/android/telecom/package-summary), which keeps the screen on when needed. If there's no special purpose API for your situation, you can use the`keepScreenOn`API.
- Is your app running a foreground service, and you need to keep the device awake when screen is off while the service is running?
  - If**No** , you do not need to keep the device awake. If the user is actively interacting with the app, the device will stay awake. If the user is not interacting with your app and you are not running a foreground service, you should let the device go into suspend mode when necessary. If you just need to make sure some work gets done while the user is away from the app, see the[background tasks](https://developer.android.com/develop/background-work/background-tasks)documentation to find the best option.
  - If**Yes** , first confirm that you actually need to use a foreground service. Depending on your situation, there may be some special-purpose API you can use to accomplish your need instead of a foreground service. You can find information about these[in the Foreground Service documentation](https://developer.android.com/develop/background-work/services/fgs/service-types). For example, if you need to track the user's location, you might be able to use the[geofencing API](https://developer.android.com/develop/sensors-and-location/location/geofencing)instead of a`location`foreground service.
- Would it be detrimental to the user experience if the device suspends while the foreground service is running and the device screen is off? (For example, if you're using a foreground service to update notifications, it wouldn't be a bad user experience if the device is suspended.)
  - If**No**, do not use a wake lock. The action resumes automatically once the user engages with their device, which takes it out of suspend.
  - If**Yes** , you might need to[use a wake lock](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock). However, you should still check to see if you're already using an API or doing an action that declares a wake lock on your behalf, as discussed in[Actions that keep the device awake](https://developer.android.com/develop/background-work/background-tasks/awake#actions-keep).

## Actions that keep the device awake

If your app is doing any of the following, you don't need to set a wake lock yourself. The following actions and APIs all keep the device awake for you.

- If you're playing audio, the audio system sets and manages a wake lock for you; you don't need to do it yourself.
- If you're using task scheduling APIs or libraries such as[WorkManager](https://developer.android.com/develop/background-work/background-tasks/persistent),[`JobScheduler`](https://developer.android.com/reference/android/app/job/JobScheduler), or[`DownloadManager`](https://developer.android.com/reference/android/app/DownloadManager), the system or library acquires a wake lock that is attributed to your app.
- If you're using[Media3 ExoPlayer](https://developer.android.com/media/media3/exoplayer), you can use[`ExoPlayer.setWakeMode()`](https://developer.android.com/reference/androidx/media3/exoplayer/ExoPlayer#setWakeMode(int))to have the player set a wake lock for you.
- Certain device sensors are wake-up sensors; you can use[`SensorManager`](https://developer.android.com/reference/android/hardware/SensorManager)to have those sensors wake up the device when they have data to report. To check if a sensor is a wake-up sensor, call[`Sensor.isWakeUpSensor`](https://developer.android.com/reference/android/hardware/Sensor#isWakeUpSensor())).
- If you[schedule an alarm](https://developer.android.com/develop/background-work/services/alarms), the device wakes up when the alarm goes off, even if your app is not running.

## See also

- [Use wake locks](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock)
- [Keep the screen on](https://developer.android.com/develop/background-work/background-tasks/awake/screen-on)