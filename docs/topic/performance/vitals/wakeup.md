---
title: Excessive wakeups  |  App quality  |  Android Developers
url: https://developer.android.com/topic/performance/vitals/wakeup
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App quality](https://developer.android.com/quality)
* [Technical quality](https://developer.android.com/quality/technical)

# Excessive wakeups Stay organized with collections Save and categorize content based on your preferences.




Wakeups are a mechanism in the
[`AlarmManager`](/reference/android/app/AlarmManager) API that
lets developers set an alarm to wake up a device at a specified time. Your app
sets a wakeup alarm by calling one of the `set()` methods in
[`AlarmManager`](/reference/android/app/AlarmManager) with
either the
[`RTC_WAKEUP`](/reference/android/app/AlarmManager#RTC_WAKEUP)
or
[`ELAPSED_REALTIME_WAKEUP`](/reference/android/app/AlarmManager#ELAPSED_REALTIME_WAKEUP)
flag. When a wakeup alarm is triggered, the device comes out of low-power mode
and holds a [partial wake lock](/topic/performance/vitals/wakelock) while executing the alarm's
[`onReceive()`](/reference/android/content/BroadcastReceiver#onReceive(android.content.Context,%20android.content.Intent))
or
[`onAlarm()`](/reference/android/app/AlarmManager.OnAlarmListener#onAlarm())
method. If wakeup alarms are triggered excessively, they can drain a device's
battery.

To help you improve app quality, Android automatically monitors apps for
excessive wakeup alarms and displays the information in Android vitals. For
information on how the data is collected, see [Play Console
docs](https://support.google.com/googleplay/android-developer/answer/7385505).

If your app is waking up the device excessively, you can use the guidance in
this page to diagnose and fix the problem.

## Fix the problem

The [`AlarmManager`](/reference/android/app/AlarmManager) was
introduced in early versions of the Android platform, but over time, many use
cases that previously required
[`AlarmManager`](/reference/android/app/AlarmManager) are now
better served by newer features like
[WorkManager](/topic/libraries/architecture/workmanager).
This section contains tips for reducing wake up alarms, but in the long term,
consider migrating your app to follow the recommendations in the [best
practices](#best_practices) section.

Identify the places in your app where you schedule wakeup alarms and reduce
the frequency that those alarms are triggered. Here are some tips:

* Look for calls to the various
  [`set()`](/reference/android/app/AlarmManager#set(int,%20long,%20java.lang.String,%20android.app.AlarmManager.OnAlarmListener,%20android.os.Handler))
  methods in
  [`AlarmManager`](/reference/android/app/AlarmManager) that
  include either the
  [`RTC_WAKEUP`](/reference/android/app/AlarmManager#RTC_WAKEUP)
  or
  [`ELAPSED_REALTIME_WAKEUP`](/reference/android/app/AlarmManager#ELAPSED_REALTIME_WAKEUP)
  flag.
* We recommend including your package, class, or method name in your alarm's tag
  name so that you can easily identify the location in your source where the
  alarm was set. Here are some additional tips:

  + Leave out any personally identifying information (PII) in the name, such as
    an email address. Otherwise, the device logs `_UNKNOWN` instead of the alarm
    name.
  + Don't get the class or method name programmatically, for example by calling
    [`getName()`](/reference/java/lang/Class#getName()), because
    it could get obfuscated by Proguard. Instead use a hard-coded string.
  + Don't add a counter or unique identifiers to alarm tags. The system will not
    be able to aggregate alarms that are set that way because they all have
    unique identifiers.

After fixing the problem, verify that your wakeup alarms are working as
expected by running the following [ADB](/studio/command-line/adb)
command:

```
adb shell dumpsys alarm
```

This command provides information about the status of the alarm system service
on the device. For more information, see
[dumpsys](https://source.android.com/devices/tech/debug/dumpsys).

## Best practices

Use wakeup alarms only if your app needs to perform a user facing operation
(such as posting a notification or alerting the user). For a list of
AlarmManager best practices, see [Scheduling
Alarms](/training/scheduling/alarms).

Don't use
[`AlarmManager`](/reference/android/app/AlarmManager) to
schedule background tasks, especially repeating or network background tasks. Use
[WorkManager](/topic/libraries/architecture/workmanager)
to schedule background tasks because it offers the following benefits:

* batching - jobs are combined so that battery consumption is reduced
* persistence - if the device is rebooted, scheduled WorkManager jobs
  run after the reboot finishes
* criteria - jobs can run based on conditions, such as whether or not the device
  is charging or WiFi is available

For more information, see [Guide to background processing](/guide/background).

Don't use [`AlarmManager`](/reference/android/app/AlarmManager)
to schedule timing operations that are valid only while the app is running (in
other words, the timing operation should be canceled when the user exits the
app). In those situations, use the
[`Handler`](/reference/android/os/Handler) class because it is
easier to use and much more efficient.

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Stuck partial wake locks](/topic/performance/vitals/wakelock)
* [ANRs](/topic/performance/vitals/anr)

[Previous

arrow\_back

Stuck Partial Wake Locks](/topic/performance/vitals/stuck-wakelock)

[Next

Excessive Background Wi-Fi Scans

arrow\_forward](/topic/performance/vitals/bg-wifi)