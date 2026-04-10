---
title: https://developer.android.com/games/optimize/vitals/lmk
url: https://developer.android.com/games/optimize/vitals/lmk
source: md.txt
---

The Android platform runs on the premise that free memory is wasted memory. Android
tries to use all available memory at all times. For example, the system keeps
apps in memory after they've been closed so the user can quickly switch back to
them. For this reason, Android devices often run with very little free memory
(see [Android Memory allocation here](https://developer.android.com/topic/performance/memory-management)).

The Android [low memory killer (LMK) daemon](https://source.android.com/docs/core/perf/lmkd)
process monitors the memory state of a running Android system and reacts to
high memory pressure by killing the least essential processes to keep the
system performing at acceptable levels.

To decide which process to kill, the LMK daemon uses an *out of memory* score called
[oom_adj_score](https://android.googlesource.com/platform/system/memory/lmkd/+/master/README.md)
to [prioritize the running processes](https://developer.android.com/topic/performance/memory-management#low-memory_killer).
Processes with a high score are killed first. Background apps are killed first;
system processes, last. The following table
lists the LMK scoring categories from high to low. Items in the
highest-scoring category, in row one, are killed first:

<br />

![Android processes ranked from highest score to lowest: Background apps, previous app, home app,
services, perceptible apps, foreground app, persistent, system, and native.](https://developer.android.com/static/topic/performance/vitals/images/oom-score.png) **Figure 1.** Android processes, with high scores at the top and low scores at the bottom.

<br />

## LMK metric on Android vitals

Android vitals can help you monitor and improve your app's LMK rate. Android
vitals measures only one LMK rate: **User-perceived LMK rate**.

The metric reflects the percentage of your daily active users who experienced
at least one user-perceived LMK. A user-perceived LMK is an LMK that is likely
to have been noticed by the user. For example, LMKs that happen while your app
is displaying an activity or running as a foreground service.

You can find the metric under the **Stability** section in Android vitals:
![](https://developer.android.com/static/topic/performance/vitals/images/lmk-in-vital.png) **Figure 2.** Access **User-perceived LMK rate** in Android vitals.

As with similar to other core vital metrics, such as ANRs and crashes, you can filter
the metrics, compare your metrics with your peer, or monitor the metric's change for a
long period of time (up to 3 years). Data is available for existing apps
starting from 28 Jan 2025.
![](https://developer.android.com/static/topic/performance/vitals/images/lmk-overview.png) **Figure 3.** Overview of LMK rate in Android Vitals.

## Memory profiling tools

The following tools can help you find and diagnose memory issues in the
following ways:

- See how your app allocates memory over time. You can find a real-time graph of how much memory your app is using, the number of allocated Java objects, and when garbage collection occurs.
- Initiate garbage collection events and take a snapshot of the Java heap while your app runs.
- Record your app's memory allocations, inspect all allocated objects, and view the stack trace for each allocation.

If your game is running on a native engine, use
[HWAddress Sanitizer](https://developer.android.com/ndk/guides/hwasan) to debug native memory allocation.

### Android Studio Memory Profiler

Android Studio provides the [Memory Profiler](https://developer.android.com/studio/profile/memory-profiler)
as a component of the
[Android Profiler](https://developer.android.com/studio/preview/features/android-profiler) which helps you
identify memory leaks and memory churn that can lead to stutter, freezes, and
even app crashes. The profiler shows a real-time graph of your app's memory use
and lets you capture a heap dump, force garbage collection, and track
memory allocation.
![](https://developer.android.com/static/studio/images/memory-profiler-jni-heap_2x.png) **Figure 4.** Viewing global JNI references in Android Studio Memory Profiler.

### Unity memory profiling tools

If you are using Unity Engine to build your apps, you can follow
[Unity memory profiling guidance](https://unity.com/how-to/use-memory-profiling-unity).
Unity offers two tools to analyze memory usage in your application in Unity.

The first is the [Memory Profiler module](https://docs.unity3d.com/Manual/ProfilerMemory.html),
which is a built-in profiler that gives you basic information about where your application uses memory.
![Memory module shows memory allocations such as texture memory and mesh memory.](https://developer.android.com/static/topic/performance/vitals/images/unity-profiler-memory-module.png) **Figure 5.** Unity Profiler window with the **Memory** module selected.

The second tool is the [Memory Profiler package](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@1.1/manual/index.html),
which is a Unity package that you can add to your project. The package adds an
additional Memory Profiler window to the Unity Editor. The Memory Profiler enables you
to analyze memory usage in your application in even more detail. You can store
and compare snapshots to find memory leaks or see the memory layout to find
memory fragmentation issues.
![](https://developer.android.com/static/topic/performance/vitals/images/unity-memory-snapshot.png) **Figure 6.** Analyzing a memory snapshot using the Memory Profiler window.

### Unreal Memory Insights

Apps built by Unreal Engine can use
[Unreal Memory Insights](https://dev.epicgames.com/documentation/en-us/unreal-engine/memory-insights-in-unreal-engine)
to see detailed information about memory allocation and deallocation,
including the Low Level Memory (LLM) tags and callstacks associated with
blocks of memory.

The Memory Insights query system can find live allocations at any
point in time, identify changes in memory usage, locate memory leaks, and
differentiate short-term from long-term allocations.

From UE 5.4, Memory Insights supports memory tracing with callstacks for
Android projects.
![Memory Insights tracker showing main memory graph, live allocation count, and alloc/free event count.](https://developer.android.com/static/topic/performance/vitals/images/unreal-memory-insights.png) **Figure 6.** Unreal's Memory Insights tracker.

## Low memory insights

Android provides callbacks and APIs that enable you to trim your game's memory requirements
and determine why previous game runs were terminated.

### Callbacks

Don't register for deprecated [trim](https://developer.android.com/reference/android/content/ComponentCallbacks2#summary)
callbacks. Android doesn't have any
APIs for detecting native memory pressure events when the system is running into memory limits.
Trim callbacks haven't been helpful at preventing low-memory kills,
so Android deprecated [all of them](https://developer.android.com/reference/android/content/ComponentCallbacks2#summary)
other than [`TRIM_MEMORY_UI_HIDDEN`](https://developer.android.com/reference/android/content/ComponentCallbacks2#TRIM_MEMORY_UI_HIDDEN)
and [`TRIM_MEMORY_BACKGROUND`](https://developer.android.com/reference/android/content/ComponentCallbacks2#TRIM_MEMORY_BACKGROUND).

### Game termination

Android tries to use all available memory to cache apps and games to ensure they
load quickly (improving the user experience), but when memory becomes limited,
the system kills the most memory-intensive apps and games to free up memory for
normal device operation.

Information, insights, and best practices to help you achieve better game memory
usage include the following:

- Use [`ApplicationExitInfo`](https://developer.android.com/reference/android/app/ApplicationExitInfo): This API returns the reason why the previous game run was killed by the Android system. Use `ApplicationExitInfo`to check for low memory as a reason for a previous process run [death](https://developer.android.com/reference/android/app/ApplicationExitInfo#REASON_LOW_MEMORY). Check whether the game was killed due to low memory so the game can be optimized to use less memory on that device.
- Look at total [physical RAM](https://developer.android.com/reference/android/app/ActivityManager.MemoryInfo#totalMem): To prevent games from being killed when in the foreground and to match the device's capabilities, look at the total physical RAM per device for fine granularity to adjust game memory usage based on that. If the goal is to prevent apps from being killed shortly after moving to the background (to allow the player to multitask), use the [trim](https://developer.android.com/reference/android/content/ComponentCallbacks2#constants_1) callbacks ([`TRIM_MEMORY_UI_HIDDEN`](https://developer.android.com/reference/android/content/ComponentCallbacks2#TRIM_MEMORY_UI_HIDDEN) specifically) to reduce your game memory usage.

## Additional resources

- [Overview of memory management](https://developer.android.com/topic/performance/memory-overview)