---
title: https://developer.android.com/games/optimize/vitals/anr
url: https://developer.android.com/games/optimize/vitals/anr
source: md.txt
---

When the UI thread of an Android app is blocked for too long, an "Application
Not Responding" (ANR) error is triggered. Android vitals tracks and reports ANR
metrics in the Google Play Console to help you monitor your app's stability and
responsiveness across devices.

> [!NOTE]
> **Note:** For information on how to diagnose and resolve this issue, see [ANRs](https://developer.android.com/topic/performance/issues/anr).

## Android vitals metrics and thresholds

Android vitals can help you monitor and improve your app's ANR rate. Android
vitals measures several ANR rates:

- **ANR rate:** The percentage of your daily active users who experienced any type of ANR.
- **User-perceived ANR rate:** The percentage of your daily active users who experienced at least one *user-perceived ANR* . Currently only ANRs of type `Input dispatching timed out` are considered user-perceived.
- **Multiple ANR rate:** The percentage of your daily active users who experienced at least two ANRs.

A *daily active user* is a unique user who uses your app on a single day on a
single device, potentially over multiple sessions. If a user uses your app on
more than one device in a single day, each device will contribute to the number
of active users for that day.

User-perceived ANR rate is a *core vital*, meaning that it affects the
discoverability of your app on Google Play. It is important because the ANRs it
counts always occur when the user is engaged with the app, causing the most
disruption.

Play has defined two **bad behavior thresholds** on this metric:

- **Overall bad behavior threshold:** At least 0.47% of daily active users experience a user-perceived ANR, across all device models.
- **Per-device bad behavior threshold:** At least 8% of daily users experience a user-perceived ANR, **for a single device model**.

If your app exceeds the overall bad behavior threshold, it is likely to be less
discoverable on all devices. If your app exceeds the per-device bad behavior
threshold on some devices, it is likely to be less discoverable on those
devices, and a warning may be shown on your store listing.

Android vitals can alert you through the [Play Console](https://play.google.com/console/) when your app is
exhibiting excessive ANRs.

For information on how Google Play collects Android vitals data, see the [Play
Console](https://support.google.com/googleplay/android-developer/answer/7385505) documentation.

## Detect the problem

If the app is in the foreground when an ANR occurs, the system displays a dialog
to the user, as shown in figure 1. The ANR dialog gives the user the opportunity
to force quit the app.
![ANR dialog displayed to the user.](https://developer.android.com/static/topic/performance/images/anr-example-framed-rev.png) **Figure 1.** ANR dialog displayed to the user

ANRs are a problem because the app's main thread, which is responsible for
updating the UI, can't process user input events or draw, causing frustration to
the user. For more information on the app's main thread, see [Processes and
threads overview](https://developer.android.com/guide/components/processes-and-threads).

An ANR is triggered for your app when one of the following conditions occur:

- **Input dispatching timed out:** If your app hasn't responded to an input event (such as a key press or screen touch) within 5 seconds.
- **Executing service:** If a service declared by your app can't finish executing `Service.onCreate` and `Service.onStartCommand` or `Service.onBind` within a few seconds.
- **`Service.startForeground` not called:** If your app uses `Context.startForegroundService` to start a new service in the foreground but the service doesn't call `startForeground` within 5 seconds.
- **Broadcast of intent:** If a [`BroadcastReceiver`](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver) hasn't finished executing within a set amount of time. If the app has any activity in the foreground, this timeout is 10 seconds.
- **`JobScheduler` interactions:** If a [`JobService`](https://developer.android.com/reference/kotlin/android/app/job/JobService) doesn't return from `JobService.onStartJob` or `JobService.onStopJob` within a few seconds, or if a [user-initiated job](https://developer.android.com/reference/android/app/job/JobParameters#isUserInitiatedJob()) starts and your app doesn't call `JobService.setNotification` within a few seconds after `JobService.onStartJob` was called. For apps targeting Android 13 and lower, the ANRs are silent and not reported to the app. For apps targeting Android 14 and higher, the ANRs are explicit and are reported to the app.

In addition to Android vitals, you can use other tools to detect ANRs in the
field, though third-party tools can't report ANRs on Android 10 (API level 29)
and lower.

## Diagnose ANRs

There are some common patterns to look for when diagnosing ANRs:

- The app is doing slow operations involving I/O on the main thread.
- The app is doing a long calculation on the main thread.
- The main thread is doing a synchronous binder call to another process, and that other process is taking a long time to return.
- The main thread is blocked waiting for a synchronized block for a long operation that is happening on another thread.
- The main thread is in a deadlock with another thread, either in your process or through a binder call. The main thread isn't just waiting for a long operation to finish, but is in a [deadlock](https://en.wikipedia.org/wiki/Deadlock) situation.

The following techniques can help you determine the cause of your ANRs.

### HealthStats

[`HealthStats`](https://developer.android.com/reference/kotlin/android/os/health/HealthStats) provides metrics about the health of an application by
capturing total user and system time, CPU time, network, radio stats, screen
on and off time, and wake up alarms. This can help you measure overall CPU
usage and battery drainage.

### Debug

[`Debug`](https://developer.android.com/reference/kotlin/android/os/Debug#public-methods) helps you inspect Android applications during development,
including tracing and allocation counts to identify jank and lag in the apps.
You can also use `Debug` to get runtime and native memory counters, and memory
metrics that can help you identify the memory footprint of a particular process.

### ApplicationExitInfo

[`ApplicationExitInfo`](https://developer.android.com/reference/kotlin/android/app/ApplicationExitInfo) is available on Android 11 (API level 30) and
higher, and provides information about the reason for application exit. This
includes ANRs, low memory, app crashes, excessive CPU usage, user interruptions,
system interruptions, and runtime permission changes.

### Strict mode

Using [`StrictMode`](https://developer.android.com/reference/kotlin/android/os/StrictMode) helps you find accidental I/O operations on the main
thread while you're developing your app. You can use `StrictMode` at the
application or activity level.

### Enable background ANR dialogs

Android shows ANR dialogs for apps that take too long to process the broadcast
message only if **Show all ANRs** is enabled in the device's **Developer
options**. For this reason, background ANR dialogs are not always displayed to
the user, even when the app is experiencing performance issues.

### Profile CPU and system traces

Use the [Android Studio CPU Profiler](https://developer.android.com/studio/profile/cpu-profiler) to record system traces and CPU
activity while your game runs. Inspecting the main `Activity` thread alongside
your game engine's render, audio, and worker threads helps you spot long frames,
synchronous asset loads, and thread contention before they trigger an ANR.

### Pull a traces file

Android stores trace information when it experiences an ANR. On lower Android
versions, there's a single `/data/anr/traces.txt` file on the device. On higher
Android versions, there are multiple `/data/anr/anr_*` files. You can access ANR
traces from a device or emulator by using [Android Debug Bridge (adb)](https://developer.android.com/tools/adb) as
root:

    adb root
    adb shell ls /data/anr
    adb pull /data/anr/<filename>

You can capture a bug report from a physical device by using either the Take bug
report developer option on the device or the `adb bugreport` command on your
development machine. For more information, see
[Capture and read bug reports](https://developer.android.com/studio/debug/bug-report).

## Fix the problems

After you have identified the problem, you can use the tips in this section to
fix commonly found problems.

### Slow code on the main thread

Identify the places in your code where the app's main thread is busy for more
than 5 seconds. Look for the suspicious use cases in your game and try to
reproduce the ANR.

In games, main-thread stalls commonly happen when synchronous asset
decompression, shader compilation, or heavy game-state initialization runs on
the Android main `Activity` thread (such as inside `onCreate`, `onResume`, or
JNI callbacks invoked from the UI thread). Move game loop execution, asset
processing, and scene initialization to dedicated engine, render, or background
worker threads so the main thread remains free to process input and lifecycle
events.

### I/O on the main thread

Executing I/O operations on the main thread is a common cause of slow operations
on the main thread, which can cause ANRs.

Move all asset bundle reads, save-game serialization, `SharedPreferences`
accesses, and network requests off the main `Activity` thread onto background
worker threads so storage or network latency can't block input dispatching.

### Deadlocks

A deadlock occurs when a thread enters a waiting state because a required
resource is held by another thread, which is also waiting for a resource held by
the first thread. If the app's main thread is in this situation, ANRs are likely
to happen.

In games, deadlocks and lock contention frequently occur between the Android
main `Activity` thread (handling lifecycle, surface, or input callbacks) and
native C or C++ render, logic, or audio threads. Avoid synchronous waits on the
main thread for native engine locks, and use consistent lock ordering or
lock-free message queues when communicating across JNI and engine threads.

Deadlocks are a well-studied phenomenon in computer science, and there are
deadlock prevention algorithms that you can use to avoid deadlocks.

For more information, see [Deadlock](https://en.wikipedia.org/wiki/Deadlock) and
[Deadlock prevention algorithms](https://en.wikipedia.org/wiki/Deadlock_prevention_algorithms) on Wikipedia.

### Slow broadcast receivers

Apps can respond to broadcast messages, such as enabling or disabling airplane
mode or a change in connectivity status, by means of broadcast receivers. An ANR
occurs when an app takes too long to process the broadcast message.

An ANR occurs in the following cases:

- A broadcast receiver hasn't finished executing its [`onReceive`](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver#onreceive) method within a considerable amount of time.
- A broadcast receiver calls [`goAsync`](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver#goasync) and fails to call [`finish`](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.PendingResult#finish) on the [`PendingResult`](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.PendingResult) object.

Your app should only perform short operations in the [`onReceive`](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver#onreceive) method
of a [`BroadcastReceiver`](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver). However, if your app requires more complex
processing as a result of a broadcast message, you should defer the task to a
background worker thread if the task is expected to take a few seconds at most,
or to [`WorkManager`](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started) for tasks expected to take longer than a few seconds.

### GameActivity

The [`GameActivity`](https://developer.android.com/games/agdk/game-activity) library has reduced ANRs in [case studies](https://developer.android.com/stories/games/cat-daddy-agdk) of
games and apps that are written in C or C++. If you replace your existing native
activity with `GameActivity`, you can reduce UI thread blocking and prevent some
ANRs from happening.

If you're building your game with Unity, see
[Debug ANRs for Unity games](https://developer.android.com/games/engines/unity/unity-anrs), [Common Unity Games ANRs](https://developer.android.com/games/engines/unity/unity-anrs-list), and
[Symbolicate Android crashes and ANR for Unity games](https://developer.android.com/games/engines/unity/unity-symbolicate).

For more information about ANRs, see [Keep your app responsive](https://developer.android.com/topic/performance/anrs/keep-your-app-responsive). For more
information about threads, see [Better performance through threading](https://developer.android.com/topic/performance/threads).

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Excessive wakeups](https://developer.android.com/topic/performance/issues/wakeup)