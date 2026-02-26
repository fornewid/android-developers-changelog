---
title: https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/debug-locally
url: https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/debug-locally
source: md.txt
---

There are a number of tools you can use to debug a locally-running app that uses
wake locks. These tools can help you identify and fix performance issues.

> [!NOTE]
> **Note:** [Some APIs acquire wake locks that are attributed to your app](https://developer.android.com/develop/background-work/background-tasks/awake#actions-keep). This means your app might be using wake locks even though you aren't writing that code explicitly. If your app has mysterious performance issues, it can be helpful to check if there are misbehaving wake locks. If your app is holding wake locks and you don't recognize the names, [Identify wake locks created by other APIs](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls) can help you identify the API that might have created them.

The following tools can help you debug or optimize your wake locks:

- [dumpsys](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/debug-locally#dumpsys) provides information about the status of system services on a device.
- [System tracing](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/debug-locally#system-tracing) produces a trace file that you can use to generate a system report.
- The Android Studio [Background Task Inspector](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/debug-locally#bg-task) helps you to monitor wake locks, including wake locks that might be acquired by libraries like WorkManager.

### dumpsys

[dumpsys](https://developer.android.com/tools/dumpsys) is a tool that runs on Android devices and provides
information about the device's system services.

The following command is particularly useful for debugging wake locks:

- `adb shell dumpsys batterystats` provides a detailed history of wake locks held by each app. For more information, see the dumpsys [Inspect battery
  diagnostics](https://developer.android.com/tools/dumpsys#battery) documentation.

### System tracing

[System tracing](https://developer.android.com/topic/performance/tracing) records a wide range of device activity
over a short period. System tracing produces a *trace file* that you can use to
generate a system report. This report helps you identify ways to improve your
app's performance.

For information on how to get started, see this [system tracing quickstart
guide](https://perfetto.dev/docs/quickstart/android-tracing). You can also watch [this video on improving
Android battery efficiency](https://youtu.be/jS46zP8kQ3k?si=BCteWawO-rK7EAGl).

### Background Task Inspector

You can use Android Studio's
[Background Task Inspector](https://developer.android.com/studio/inspect/task) to monitor [wake locks,
alarms and jobs](https://developer.android.com/studio/inspect/task#inspect-jobs-alarms-wakelocks).

In particular, the WorkManager library uses JobScheduler to schedule and execute
jobs. While these jobs are running, they hold a wake lock that is attributed
to the app. You can use Background Task Inspector to monitor workers and jobs
that execute in the background and see details about their work.