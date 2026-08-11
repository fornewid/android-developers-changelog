---
title: https://developer.android.com/games/optimize/memory-overview
url: https://developer.android.com/games/optimize/memory-overview
source: md.txt
---

Memory optimization is critical to delivering stable, high-performance gaming experiences on Android. This guide provides an overview of why memory efficiency matters, how the Android operating system manages process memory limits, and the new memory metrics in the Google Play Console to help you monitor and improve your game's technical quality.

## The importance of memory optimization

Optimizing your game's memory is essential to maintain player retention, expand device compatibility, and comply with platform quality standards:

- **Cold start prevention (user experience and retention)** : When a player temporarily switches away from your game (for example, to answer a notification or check a message), the operating system places the game process into the background. If the game's background memory footprint is too high, the system's Low Memory Killer (LMK) prioritizes terminating the game process to reclaim RAM for foreground tasks. The next time the user resumes, instead of a seamless and instantaneous warm resume, the game must undergo a long cold start---completely reloading heavy graphics assets, audio, and game engine binaries from storage. Keeping your background memory usage low prevents these silent background terminations, preserving user state and ensuring players can resume their session immediately. For more details on system LMK behavior, see the [Android Vitals - Low memory killers](https://developer.android.com/games/optimize/vitals/lmk) guide.
- **Ecosystem and device stability**: Inefficient memory usage and memory leaks degrade overall system health. When system memory is scarce, the system faces severe pressure, resulting in frame rate drops, UI stuttering, and audio glitches. If memory pressure is too severe, the system's Low Memory Killer (LMK) aggressively terminates background processes, forcing other applications to experience slow cold starts and lost user state when players switch between tasks.
- **Platform-level terminations**: Starting in Android 17 (API level 37), the system is more proactive about terminating processes that use too much memory. If your game's footprint is too high, the OS can terminate its process abruptly without generating a standard stack trace.
- **Device compatibility**: While flagship devices feature 12 GB to 16 GB of RAM, a massive portion of the global gaming audience uses devices with 4 GB or 6 GB of RAM. Proper memory management ensures your game remains accessible and responsive across all hardware tiers without requiring complex, separate asset packages.

## Understanding memory in Android

To design effective memory-budgeting strategies, developers must understand how the Android platform manages physical memory and how it measures your game's active footprint.

### Core Android memory concepts

For foundational concepts regarding platform-level memory management, see the official [Memory Management Overview](https://developer.android.com/topic/performance/memory-management) documentation. This resource covers four architectural areas:

- **Memory overview**: Android uses paging and memory-mapping (mmap) to manage RAM. It doesn't support a traditional swap file on disk; instead, it relies on page compression (using zRAM) and page reclamation to free up physical memory.
- **Memory allocation among processes**: Android shares RAM across the entire system. It assigns specific heaps for Dalvik or ART virtual machine execution, while allowing native development environments (such as C++ game engines) to request memory from the native system heap.
- **App memory management**: Operating under a multi-process model, Android expects applications to monitor their lifecycle state dynamically and voluntarily release unnecessary resources (such as uncached graphics and bitmaps) to support system health.
- **Processes and threads overview**: The system categorizes processes into a hierarchy based on their current user-perceived visibility and importance, determining which processes are kept alive and which are terminated first during low-memory conditions.

### The total memory footprint metric

The platform-level Android 17 Memory Limiter evaluate process consumption using Total Memory Footprint rather than total resident size (RSS) or virtual memory size.

*Total Memory Footprint = Anonymous RSS (RssAnon) + Uncompressed Swap (VmSwap)*

To prevent games from exceeding platform limits, developers must understand exactly what these metrics represent at a system level. For more information about these metrics, physical RAM allocations, and how file-backed pages are handled, see [Understanding RSS and Swap Metrics](https://developer.android.com/games/optimize/memory-monitoring#understanding-rss-and-swap-metrics) in the [Monitor Memory Usage](https://developer.android.com/games/optimize/memory-monitoring) guide.

## Memory constraints

To maintain system stability and ensure that applications don't consume excessive resources, the Android platform manages memory limits for running processes.

### Memory Limiter in Android 17 and higher

Android 17 (API level 37) and higher manage strict, per-app memory limits using Linux cgroup v2 to prevent individual apps from causing system-wide instability. For more details on the technical implementation, see the [AOSP Memory Limiter Guide](https://source.android.com/docs/core/perf/memory-limiter) and [Prioritizing Memory Efficiency: Essential Steps for Android 17 Blog](https://android-developers.googleblog.com/2026/06/prioritizing-memory-efficiency-steps-for-android-17.html).

- **Mechanism** : The Memory Limiter monitors all application processes and dynamically assigns limits based on the process's lifecycle state:
  - **Visible processes (foreground)**: App processes currently displaying a UI are expected to run a larger resource working set, and are afforded a more generous limit.
  - **Non-visible processes (background or services)**: App processes doing active work without showing a UI are constrained to a tighter, more restrictive budget.
- **Kernel attributes** : The service relies on two main attributes:
  - **`memory.high`**: A soft limit. When exceeded, the kernel throttles the process and attempts to aggressively reclaim memory. This reclamation can cause the game to experience performance degradation.
  - **`memory.swap.max`**: Manages a hard cap on the swap or zRAM space the process can use.
- **Termination behavior** : If a process continues to allocate anonymous memory past `memory.high` and exhausts its swap capacity, allocations fail, and the OS silently kills the process. This termination is logged using [`ApplicationExitInfo`](https://developer.android.com/reference/android/app/ApplicationExitInfo) under the [Memory Limiter](https://source.android.com/docs/core/perf/memory-limiter) exit reason (available starting in Android 17, 26Q4).

## Monitor memory usage

To effectively optimize your game's memory, you must first understand how the Android platform measures its footprint. Android 17 updates the memory metric to track the sum of Anonymous RSS (RssAnon) and uncompressed Swap (VmSwap), excluding file-backed or GPU-private memory. This guide details how to leverage system-level tools such as Perfetto and `meminfo`, implement diagnostic APIs such as `ProfilingManager` and `onTrimMemory`, and extract precise memory allocations within Unity and Unreal Engine. Understand how to accurately profile your game and avoid the performance stutters associated with traditional runtime memory polling.

For more information, see [Monitor Memory Usage](https://developer.android.com/games/optimize/memory-monitoring).

> [!NOTE]
> **Note:** The Memory Advice API beta is deprecated and no longer recommended for use.

## Memory reduction strategies

While game engines simplify cross-platform development, their default memory handling can trigger OS-level memory limits. This page details practical optimization steps specifically tailored for Unity and Unreal Engine. Understand why relying on Java-based `onTrimMemory` can cause deadlocks in Unity---and how to use native lifecycle callbacks instead. You'll also discover key asset-level optimizations, such as using ASTC 8x8 texture compression and configuring asset unloads, to keep your game running smoothly on all hardware tiers.