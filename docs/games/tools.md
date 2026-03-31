---
title: Tools for optimizing your game  |  Android game development  |  Android Developers
url: https://developer.android.com/games/tools
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Games dev center](https://developer.android.com/games)

Send feedback

# Tools for optimizing your game Stay organized with collections Save and categorize content based on your preferences.




To prepare your environment for debugging and optimizing Android games, get
access to the following tools that help you analyze CPU usage and graphics
calls.

## CPU

Use the following tools to evaluate and improve your game's CPU performance:

* **Systrace:** Records CPU and disk activity over a short period of time.
  [Access this tool from the command line](/topic/performance/tracing/command-line),
  or [use the on-device tool](/topic/performance/tracing/on-device) that's
  available when running Android 9 (API level 28) or higher. Also see the
  [overview of system tracing](/topic/performance/tracing).
* **CPU Profiler:** Inspect your game's CPU usage and thread activity, either
  in real time or from recorded traces.
  See documentation on [how to access and use the CPU Profiler](/studio/profile)
  within Android Studio. A
  [standalone version of this profiler](/studio/profile#standalone-profilers)
  that doesn't require a Gradle project at launch is installed with both
  [Android Studio](/studio) and the
  [Android Game Development Extension](/games/agde).

## Memory

* **Meminfo:** Collects memory statistics to show how much
  [PSS memory](/topic/performance/memory-management#calculating_memory_footprint)
  was allocated and the categories for which it was used. Use the command
  `adb shell dumpsys meminfo package-name` or the
  [`MemoryInfo`](/reference/android/os/Debug.MemoryInfo) call.
* **Perfetto:** Collects performance and memory information on a device and
  displays it in a web-based UI. [Perfetto](https://docs.perfetto.dev)
  supports arbitrarily long traces so you can view how RSS changes over time.
  Enable long traces from the
  [System Tracing app](/topic/performance/tracing/on-device).
* **bugreport:** Shows if your game crashed because it ran out of memory or if
  it was killed by the
  [LMK](/topic/performance/memory-management#low-memory_killer). Use the
  command `adb bugreport bugreport-name` or go to
  **Developer Options > Bug report**.

## Graphics

Use the following tools to evaluate and improve your game's display pipeline:

* **Android Frame Pacing API:** Helps synchronize your game engine's rendering
  process with Android's display pipeline.
  [Download from the Android Open Source Project (AOSP)](https://android.googlesource.com/platform/frameworks/opt/gamesdk/),
  or
  [access the plugin from Unity 2019.2.0 Alpha 6](https://unity3d.com/unity/whats-new)
  or higher. Also
  [see documentation for the Android Frame Pacing API](/topic/performance/frame-pacing).
* **Android GPU Inspector (AGI):** A GPU profiling tool. You can take traces
  of your games and find interesting performance insights to help you make
  graphics optimization decisions. [Learn more
  here.](/agi)

## Additional resources

* [Improve your game's performance](/games/optimize)
* [GAPID](https://gapid.dev)






Send feedback