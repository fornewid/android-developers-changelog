---
title: https://developer.android.com/games/tools
url: https://developer.android.com/games/tools
source: md.txt
---

# Tools for optimizing your game

To prepare your environment for debugging and optimizing Android games, get access to the following tools that help you analyze CPU usage and graphics calls.

## CPU

Use the following tools to evaluate and improve your game's CPU performance:

- **Systrace:** Records CPU and disk activity over a short period of time.[Access this tool from the command line](https://developer.android.com/topic/performance/tracing/command-line), or[use the on-device tool](https://developer.android.com/topic/performance/tracing/on-device)that's available when running Android 9 (API level 28) or higher. Also see the[overview of system tracing](https://developer.android.com/topic/performance/tracing).
- **CPU Profiler:** Inspect your game's CPU usage and thread activity, either in real time or from recorded traces. See documentation on[how to access and use the CPU Profiler](https://developer.android.com/studio/profile)within Android Studio. A[standalone version of this profiler](https://developer.android.com/studio/profile#standalone-profilers)that doesn't require a Gradle project at launch is installed with both[Android Studio](https://developer.android.com/studio)and the[Android Game Development Extension](https://developer.android.com/games/agde).

## Memory

- **Meminfo:** Collects memory statistics to show how much[PSS memory](https://developer.android.com/topic/performance/memory-management#calculating_memory_footprint)was allocated and the categories for which it was used. Use the command`adb shell dumpsys meminfo `<var translate="no">package-name</var>or the[`MemoryInfo`](https://developer.android.com/reference/android/os/Debug.MemoryInfo)call.
- **Perfetto:** Collects performance and memory information on a device and displays it in a web-based UI.[Perfetto](https://docs.perfetto.dev)supports arbitrarily long traces so you can view how RSS changes over time. Enable long traces from the[System Tracing app](https://developer.android.com/topic/performance/tracing/on-device).
- **bugreport:** Shows if your game crashed because it ran out of memory or if it was killed by the[LMK](https://developer.android.com/topic/performance/memory-management#low-memory_killer). Use the command`adb bugreport `<var translate="no">bugreport-name</var>or go to**Developer Options \> Bug report**.

## Graphics

Use the following tools to evaluate and improve your game's display pipeline:

- **Android Frame Pacing API:** Helps synchronize your game engine's rendering process with Android's display pipeline.[Download from the Android Open Source Project (AOSP)](https://android.googlesource.com/platform/frameworks/opt/gamesdk/), or[access the plugin from Unity 2019.2.0 Alpha 6](https://unity3d.com/unity/whats-new)or higher. Also[see documentation for the Android Frame Pacing API](https://developer.android.com/topic/performance/frame-pacing).
- **Android GPU Inspector (AGI):** A GPU profiling tool. You can take traces of your games and find interesting performance insights to help you make graphics optimization decisions.[Learn more here.](https://developer.android.com/agi)

## Additional resources

- [Improve your game's performance](https://developer.android.com/games/optimize)
- [GAPID](https://gapid.dev)