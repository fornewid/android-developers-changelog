---
title: https://developer.android.com/games/optimize/memory-monitoring
url: https://developer.android.com/games/optimize/memory-monitoring
source: md.txt
---

To effectively optimize your game's memory footprint, you must first understand
how the Android platform measures memory and how to use system telemetry,
diagnostic APIs, and profiling tools. This guide details how to monitor,
capture, and analyze your game's memory allocations under the new platform
guidelines.

## Understanding RSS and swap metrics

To effectively analyze and debug your game's memory behavior, you must
understand the exact technical metrics the Android platform uses for memory
management. For detailed background information on how this telemetry parameter
is processed and monitored in the wild, see the
[Android Vitals - Memory usage (anonymous RSS + swap)](https://developer.android.com/topic/performance/vitals/memory-usage) documentation.

### 1. Anonymous RSS (RssAnon)

Resident Set Size (RSS) measures the portion of memory occupied by a process
that is held in the device's physical RAM. RSS is divided into file-backed
memory and anonymous memory. Android's memory metric focuses strictly on
Anonymous RSS:

- **What it includes** : Memory pages allocated directly by your game process that aren't linked to a physical file on storage. These pages include Java or Kotlin heaps, thread execution stacks, and crucially, native memory allocations (such as custom C++ engine allocators, or memory blocks requested using native malloc or new and dirtied by game logic). Learn more about this metric under the [Process Memory (RSS)](https://developer.android.com/studio/profile/chart-glossary/process-memory) dictionary.
- **Why it matters**: Game engines use massive native memory pools to handle physics, rendering, and logic. Because these pools aren't backed by files, they live entirely in Anonymous RSS and form the bulk of your game's physical footprint.

### 2. Uncompressed swap (VmSwap)

Android doesn't support a traditional disk-based swap space due to flash storage
wear and latency constraints. Instead, it uses zRAM (Uncompressed Swap):

- **What it includes**: When physical RAM pressure increases, the kernel's memory management daemon compresses inactive anonymous pages and moves them into a dedicated, uncompressed portion of physical RAM (zRAM).
- **The metric calculation**: The system tracks this based on the uncompressed size (VmSwap) to evaluate the game's actual physical memory demand. If your game allocates memory and the system swaps it to zRAM, it still counts toward your game's Total Memory Footprint.

### 3. Process states

The memory usage are [broken down by process states in Android Vitals](https://developer.android.com/topic/performance/vitals/memory-usage#identify-high).
For game developers, third-party SDKs or games can also trigger
user-perceived services or background services unexpectedly.

- **What it includes**: Foreground, Perceptible services, Background and Cached.
- **Why it matters** : Different process states have different impacts on the Android OS memory management. You might not know your game is running with a sensitive process state if any of the third-party SDK triggers a background task unintentionally. Monitor whether your game is running in the background using [`RunningAppProcessInfo`](https://developer.android.com/reference/android/app/ActivityManager.RunningAppProcessInfo).

## Application programming interfaces (APIs)

Android provides system APIs that allow your game to respond dynamically to
memory pressure and capture detailed memory diagnostics at runtime.

### Respond to memory trim events

The system uses [`onTrimMemory`](https://developer.android.com/reference/android/content/ComponentCallbacks2#onTrimMemory(int)) to notify your app of lifecycle events that
present a good opportunity for your app to voluntarily reduce its memory usage
and avoid being killed by the [low-memory killer (LMK)](https://developer.android.com/topic/performance/memory-management#low-memory_killer) to release memory for
other apps to use.

If the system kills your app in the background, the user experiences a slow
[cold start](https://developer.android.com/topic/performance/vitals/launch-time#cold) on resume. Reducing background memory usage helps prevent these
background terminations.

When responding to trim events, release large, reconstructible memory
allocations that aren't immediately needed:

- **Example:** Trim or purge cached bitmaps (decoded from local storage) in
  response to [`TRIM_MEMORY_UI_HIDDEN`](https://developer.android.com/reference/android/content/ComponentCallbacks2#TRIM_MEMORY_UI_HIDDEN).

### Kotlin

    class MainActivity : AppCompatActivity(), ComponentCallbacks2 {
        override fun onTrimMemory(level: Int) {
            if (level >= ComponentCallbacks2.TRIM_MEMORY_UI_HIDDEN) {
                // Release memory related to UI elements, such as bitmap caches.
            }
            if (level >= ComponentCallbacks2.TRIM_MEMORY_BACKGROUND) {
                // Release memory related to background processing, such as by
                // closing a database connection.
            }
        }
    }

### Java

    public class MainActivity extends AppCompatActivity implements ComponentCallbacks2 {
        public void onTrimMemory(int level) {
            switch (level) {
                if (level >= ComponentCallbacks2.TRIM_MEMORY_UI_HIDDEN) {
                    // Release memory related to UI elements, such as bitmap caches.
                }
                if (level >= ComponentCallbacks2.TRIM_MEMORY_BACKGROUND) {
                    // Release memory related to background processing, such as by
                    // closing a database connection.
                }
            }
        }
    }

> [!NOTE]
> **Note:** Some game engines might not support `onTrimMemory` callback with `TRIM_MEMORY_UI_HIDDEN` or `TRIM_MEMORY_BACKGROUND`. Additionally, game engines might pause execution when the application moves to the background. Consequently, events sent from customized Java or Kotlin code might not reach the engine main thread immediately. Handling these events on a running background thread to release unmanaged memory is an effective way to maintain your game's health.

### `ProfilingManager`

Introduced in Android 15 (API level 35), the [`ProfilingManager`](https://developer.android.com/reference/android/os/ProfilingManager) API allows
applications to capture programmatically defined snapshots (such as heap
profiles, system traces, and Java heap dumps) directly at runtime.

Developers can trigger captures manually at specific scenes, or register
automated triggers such as `TRIGGER_TYPE_ANOMALY` to automatically fire a
capture when the game process violates the Memory Limiter thresholds. However,
game developers must account for critical limitations in modern game engines:

**Note:** Modern game engines (such as Unity or Unreal) manage execution
performance by pre-allocating massive virtual memory blocks from the kernel
using mmap with the MAP_ANONYMOUS flag. The engines then use custom
sub-allocators (for example, Unity's native memory manager or Unreal's
BinnedAllocators) to subdivide and allocate memory blocks internally.

### ApplicationExitInfo

If your game is terminated in the background or killed because it violated
individual process memory limits, standard Java or native crash dump mechanisms
(such as Firebase Crashlytics) don't register the event. To query and log these
terminations programmatically, developers should leverage the
[`ApplicationExitInfo`](https://developer.android.com/reference/android/app/ApplicationExitInfo) API at game startup.

- Implementation: On start, call `ActivityManager.getHistoricalProcessExitReasons()` to retrieve the exit reasons of recent sessions.
- Key memory exit reasons:
  - [`REASON_LOW_MEMORY`](https://developer.android.com/reference/android/app/ApplicationExitInfo#REASON_LOW_MEMORY): Indicates the process was terminated by the system's Low Memory Killer (LMK). This termination occurs when device-wide memory pressure is high and the OS must reclaim RAM. This exit reason indicates your game's background footprint is too large to coexist with other applications.
  - [`REASON_MEMORY_LIMITER`](https://developer.android.com/reference/android/app/ApplicationExitInfo#REASON_MEMORY_LIMITER) (Android 17 (API level 37) and higher): Indicates the process was specifically killed because it exceeded its cgroup memory limit (RssAnon + VmSwap) assigned by the platform's Memory Limiter. This termination can happen even if there's ample physical memory remaining on the device, signifying a direct violation of individual process limits.

## Use available tools

Use the following platform tools during development and QA to measure your
game's memory usage accurately.

### `meminfo`

This tool collects memory statistics to show how much [PSS memory](https://developer.android.com/topic/performance/memory-management#calculating_memory_footprint) was
allocated and the categories for which it was used.

Print the [`meminfo`](https://developer.android.com/studio/command-line/dumpsys#meminfo) statistics in one of the following ways:

- Use the command `adb shell dumpsys meminfo
  package-name`.
- Use the [`MemoryInfo`](https://developer.android.com/reference/android/os/Debug.MemoryInfo) call from the Android Debug API.

The [`PrivateDirty`](https://developer.android.com/studio/command-line/dumpsys#meminfo) statistic shows the amount of RAM inside the process
that can't be paged to disk and isn't shared with any other processes. The bulk
of this amount becomes available to the system when that process is killed.

### Memory tracepoints

Memory tracepoints track the amount of [RSS memory](https://developer.android.com/topic/performance/memory-management#calculating_memory_footprint) your game is using.
Calculating RSS memory usage is much faster than calculating PSS usage. Because
it's faster to calculate, RSS shows finer granularity on changes in the memory
size for more accurate measurements of peak memory usage. Therefore, it's easier
to notice peaks that could cause the game to run out of memory.

### Perfetto

[Perfetto](https://docs.perfetto.dev/) is a suite of tools for collecting performance and memory
information on a device and displaying it in a web-based UI. It supports
arbitrarily long traces so you can view how RSS changes over time. You can also
issue SQL queries on the data it produces for offline processing. Enable long
traces from the [System Tracing app](https://developer.android.com/topic/performance/tracing/on-device). Make sure the `memory:Memory` category
is enabled for the trace. For custom memory instrumentation in development and
testing, you can also use the (Beta) [heapprofd API](https://perfetto.dev/docs/instrumentation/heapprofd-api).

#### Inspect RssAnon and swap in Perfetto

To check your game's anonymous memory and zRAM swap impact, load your trace file
in the web-based UI at [ui.perfetto.dev](https://ui.perfetto.dev/) and follow these analytical
techniques, designed for deep memory case-studies (see [Perfetto Memory Analysis
Case Studies](https://perfetto.dev/docs/case-studies/memory) for more details):

**1. Visualizing Memory Counters on the Timeline**

- Locate your process: In the navigation list, search for your game's package or process name.
- Expand track group: Click your process row to expand its thread tracks, and locate the sub-group named Memory.
- Analyze the tracks:
  - **mem.rss.anon (Anonymous RSS)**: This line graph shows the real-time physical RAM occupied by your game's unmanaged memory pools. Monitor this timeline during scene loads, UI popups, or gameplay transitions to check for high allocation peaks.
  - **mem.swap (Compressed Swap or VmSwap)**: This graph plots the pre-compressed size of memory blocks moved to zRAM. High swap activity coinciding with gameplay indicates that your game is running on a constrained memory device and the system is actively compressing background assets.

**2. Running SQL Queries (Trace Processor)** For detailed offline analysis, you
can execute SQL queries directly inside the Perfetto UI console or use
the standalone Trace Processor Python library to calculate statistical
peaks.

- Find the Peak Anonymous RSS Allocation:

      SELECT
        max(value) / 1024 / 1024 AS max_rss_anon_mb
      FROM counter
      JOIN counter_track ON counter.track_id = counter_track.id
      WHERE counter_track.name = 'mem.rss.anon'
        AND counter_track.upid IN (
          SELECT upid FROM process WHERE name = 'your.game.package.name'
        );

- Correlate RssAnon and VmSwap at any given timestamp:

      SELECT
        ts,
        track.name AS metric_type,
        value / 1024 / 1024 AS size_mb
      FROM counter
      JOIN counter_track track ON counter.track_id = track.id
      WHERE (track.name = 'mem.rss.anon' OR track.name = 'mem.swap')
        AND track.upid IN (
          SELECT upid FROM process WHERE name = 'your.game.package.name'
        )
      ORDER BY ts ASC;

For more details on inspecting trace files using Android Studio, see [Inspect
system traces: Process Memory (RSS)](https://developer.android.com/studio/profile/inspect-traces#system-traces-rss). For details on scripting memory
profiles, see [Record native allocations](https://developer.android.com/studio/profile/record-native-allocations).

### heapprofd

[`heapprofd`](https://docs.perfetto.dev/#/heapprofd) is a memory tracking tool that's part of Perfetto. This tool
can help you find memory leaks by showing where memory was allocated using
`malloc`. `heapprofd` can be started using a Python script, and because the tool
has low overhead, it doesn't affect performance like other tools such as Malloc
Debug.

> [!NOTE]
> **Note:** Because game engines use `mmap` with the `MAP_ANONYMOUS` flag to create memory pools, most allocations aren't tracked. If you have access to the game engine source code, replace the memory pool `mmap` calls with `malloc`. Some game engines have an option to use `malloc` instead of `mmap`.

### bugreport

`bugreport` is a logging tool for finding out whether or not your game crashed
because it ran out of memory. The tool's output is much more detailed than using
`logcat`. It's useful for memory debugging because it shows if your game crashed
because it ran out of memory or if it was killed by the LMK.

For more information, see [Capture and read bug reports](https://developer.android.com/studio/debug/bug-report).

### Game engine tools

While platform-level logs and system telemetry are vital for tracking OS
thresholds and compliance, game engine-specific tools help you attribute
allocations directly back to your game objects, script behaviors, and active
scene hierarchies.

#### Unity

In a Unity Engine environment, you can closely estimate the Android Anonymous
RSS + Swap memory footprint at runtime with high reliability (typically
displaying a variance of less than 10% compared to true OS-level values) using
Unity's native profiling tools and classes.

For a complete step-by-step tutorial, including configuration rules and runtime
scripts, see [How to check memory with Unity tools](https://developer.android.com/games/engines/unity/unity-memory-usage).

- **Unity profiler API** : You can programmatically approximate your game's unmanaged memory footprint at runtime by querying the core engine metrics:
  - **Using the Profiler class** : Track total memory allocations by summing the values of `Profiler.GetTotalReservedMemoryLong()` and `Profiler.GetMonoHeapSizeLong()`.
  - **Using the `ProfilerRecorder` class**: Monitor memory categories dynamically. To establish a reliable baseline approximation, fetch Total Reserved Memory (on Release builds) or subtract Gfx Reserved Memory from it (on Development builds) to strip out file-backed graphics memory components.
- **Unity memory profiler** : To identify and debug memory leaks offline, capture a memory snapshot and inspect the Resident Memory on Device chart found under the All of Memory section. To calculate the approximate footprint, sum the totals of the following categories: Untracked, Android Runtime, Native, and Managed.
  - **zRAM limitation**: Under tight memory conditions, the Android kernel can compress inactive memory pages into swap space (zRAM). Because the Unity Memory Profiler can't detect OS-level swap parameters, you might see minor footprint discrepancies during heavy memory scenes. Cross-reference your estimates with Perfetto to confirm exact values.

#### Unreal

In an Unreal Engine environment, you can evaluate your game's memory footprint
by combining engine diagnostics with platform telemetry. For step-by-step
instructions and profiling workflows, see [Check memory usage with Unreal
Engine](https://developer.android.com/games/engines/unreal/unreal-memory-usage).

Key diagnostic tools and interfaces include:

- **C++ Diagnostics API** : Use `GetMemoryUsedFast` for lightweight memory queries and the `GetStats` interface for hardware-level memory statistics.
- **Console Commands** : Monitor real-time memory allocation trends on device hardware using the `stat unit` and `stat unitmax` engine commands.
- **Unreal Insights**: Inspect frame-accurate timeline captures to analyze platform-level metrics and custom memory counters.