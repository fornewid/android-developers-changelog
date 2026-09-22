---
title: https://developer.android.com/google/play/vitals/wakeup
url: https://developer.android.com/google/play/vitals/wakeup
source: md.txt
---

Wakeups are a mechanism in the
[`AlarmManager`](https://developer.android.com/reference/android/app/AlarmManager) API that
lets developers set an alarm to wake up a device at a specified time. When a
wakeup alarm is triggered, the device comes out of low-power mode and holds a
[partial wake lock](https://developer.android.com/google/play/vitals/stuck-wakelock) while executing the
alarm's
[`onReceive()`](https://developer.android.com/reference/android/content/BroadcastReceiver#onReceive(android.content.Context,%20android.content.Intent))
or
[`onAlarm()`](https://developer.android.com/reference/android/app/AlarmManager.OnAlarmListener#onAlarm())
method. If wakeup alarms are triggered excessively, they can drain a device's
battery.

> [!NOTE]
> **Note:** For information on how to diagnose and resolve this issue, see [Excessive wakeups](https://developer.android.com/topic/performance/issues/wakeup).

## Android vitals monitoring

To help you improve app quality, Android automatically monitors apps for
excessive wakeup alarms and displays the information in Android vitals. For
information on how the data is collected, see [Play Console
docs](https://support.google.com/googleplay/android-developer/answer/7385505).