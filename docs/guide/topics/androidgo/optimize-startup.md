---
title: https://developer.android.com/guide/topics/androidgo/optimize-startup
url: https://developer.android.com/guide/topics/androidgo/optimize-startup
source: md.txt
---

# Improve startup latency

Startup latency is an important metric to retain daily active users and ensure a seamless user experience from the first interaction. This is especially true in low-RAM environments where performance tradeoffs might be considered. However, before beginning to improve app startup, it's important to understand the underlying aspects that contribute to startup itself.

## Best practices

### Ship with a Baseline Profile

Baseline Profiles improve code execution speed by around 30% from the first launch by avoiding interpretation and[just-in-time (JIT)](https://developer.android.com/about/versions/nougat/android-7.0#jit_aot)compilation steps for included code paths. By shipping a Baseline Profile in an app,[Android Runtime (ART)](https://source.android.com/docs/core/runtime)can optimize included code paths through Ahead of Time (AOT) compilation, providing performance enhancements for every new user and on every app update.

### Avoid eager initialization

Avoid doing eager work that may not be necessary in your app's startup sequence. The most likely scenario for your app starting a process is through the launching of the app. However,[WorkManager](https://developer.android.com/reference/androidx/work/WorkManager),[JobScheduler](https://developer.android.com/reference/android/app/job/JobScheduler),[BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver), bound services, and the[AndroidX startup library](https://developer.android.com/topic/libraries/app-startup)can also start app processes in the background. If possible, avoid unnecessarily initializing anything eagerly in your`Application`class. A lot of libraries offer on-demand initialization, which lets you invoke them only when necessary.

### Move tasks from UI thread to background thread

If there are tasks that are taking longer and blocking the main thread, move them to a background thread or use WorkManager to ensure efficiency. Identify operations that occupy large time frames or consume more time than expected. Optimizing these tasks can help drastically improve startup latency.

### Analyze and fix severe disk read contention

[StrictMode](https://developer.android.com/reference/android/os/StrictMode)is a developer tool that can help detect the use of accidental disk or network access on the app's main thread, where UI operations are received and animations take place. Once the tool detects a possible area of improvement, you can automatically terminate the app or log the violation for further inspection at a later time.

### Avoid synchronous IPCs

Often long pauses in your app's execution are caused by binder calls, the inter-process communication (IPC) mechanism on Android. On recent versions of Android, it's one of the most common reasons for the UI Thread to stop running. Generally, the fix is to avoid calling functions that make binder calls; if it's unavoidable, you should cache the value, or move work to background threads. For more information, see[Thread scheduling delays](https://developer.android.com/topic/performance/vitals/render#thread_scheduling_delays).