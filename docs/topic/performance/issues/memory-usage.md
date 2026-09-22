---
title: https://developer.android.com/topic/performance/issues/memory-usage
url: https://developer.android.com/topic/performance/issues/memory-usage
source: md.txt
---

Memory usage (anonymous RSS + swap) is a metric that reflects your app's memory
usage.

[Anonymous memory](https://developer.android.com/topic/performance/memory-management#memory_pages) is memory not backed by a file on storage, such as
heap allocations and mmap-allocated memory. This captures your app's dynamic
memory allocations, including the Java or Kotlin heap, unmanaged native heap
allocations (where Bitmap pixel data lives on Android 8.0 (API level 26) and
higher), and thread execution stacks. While the OS can drop file-backed memory
under pressure, it can't drop anonymous memory.

[Resident Set Size](https://developer.android.com/topic/performance/memory-management#calculating_memory_footprint) (RSS) is the total number of memory pages (both shared
and non-shared) used by a process that are held in physical RAM. A page is
considered "shared" if it's accessed by more than one process (such as apps
that access the same library).

For anonymous memory, the system can write pages to
[swap space (or zRAM on Android)](https://developer.android.com/topic/performance/memory-management#types_of_memory) when memory is under pressure.
The system can read these pages back from swap if needed.

Altogether, memory usage (anonymous RSS + swap) is a measure of your app's
total number of memory pages not backed by a file on storage, inclusive of any
memory that's also being preserved by the system in swap. Tracking anonymous
RSS + swap ensures you see your app's true, unevictable memory footprint.

If your app's memory usage is high, investigate further and fix the problem
using the guidance on this page.

> [!NOTE]
> **Note:** For information on how Android Play Vitals tracks and reports this issue, see [Memory usage (anonymous RSS + swap) in Android vitals](https://developer.android.com/google/play/vitals/memory-usage).

## Resources

### Diagnose excessive memory usage locally

To get started with diagnosing the source of excessive memory usage, you can
capture a heap dump with **Record heap dump** in developer settings, [Android
Studio](https://developer.android.com/studio/profile/capture-heap-dump), or [Perfetto](https://perfetto.dev/docs/getting-started/memory-profiling). We recommend you start by capturing a
heap dump locally after testing your app's core user journeys.

We especially recommend testing the following user journeys:

- Webviews and In-App Browser Sessions
- Media-heavy infinite scrolling
- Asset creation and editing flows

To investigate potential memory leaks, run the corresponding user journeys
locally and collect heap dumps across different [process states](https://developer.android.com/guide/components/activities/process-lifecycle) (visible,
[foreground service](https://developer.android.com/develop/background-work/services/fgs), and cached) to verify if the app releases memory after
being backgrounded. To understand how these process states correlate with
`onTrimMemory` callbacks, consult the guidance on [releasing memory in response
to events](https://developer.android.com/topic/performance/memory/manage-app-memory#release).

If you're debugging memory issues using the Android Studio Profiler, you can
also use the [LeakCanary integration to streamline leak and duplicate
bitmap detection to optimize your image usage](https://developer.android.com/studio/releases#leakcanary).

> [!NOTE]
> **Note:** Android Studio doesn't support viewing a heap dump that was captured with a tool other than the Android Studio Memory Profiler.

After you've collected the heap dump, we recommend using the [Android profiler
skill](https://developer.android.com/topic/performance/issues/memory-usage#skill-title_profilers) to analyze the heap dump and identify potential sources of high
memory usage.


## Android skills

[View on GitHub](https://github.com/android/skills/tree/main/profilers/android-profiler)

### Android profiler

Use an [Android skill](https://developer.android.com/tools/agents/android-skills) to record and analyze Android performance data so that you can diagnose bottlenecks, jank, and memory leaks, and convert natural language into executable trace queries, such as PerfettoSQL queries. To install this skill from the [Android CLI](https://developer.android.com/tools/agents/android-cli), run:

    android skills add android-profiler

<br />

Here's an example of what the AI skills could respond with:

> [!NOTE]
> **Note:** Skills are evolving and this output is provided only as an example.

    I have completed the analysis of memory leaks and bitmap issues for [app] using the provided Perfetto trace.
      Summary of Findings
      The investigation identified a critical memory pressure issue caused by massive bitmap retention within the app process.
    ...
    Recommendations for [app]
       1. [Library] Image Cache Optimization:
           * Review the [Library] caching strategy. Ensure that bitmaps
             loaded for animations are released or downsampled when the animation is
             not in the foreground.
       2. Asset Resolution Audit:
           * The 14.7 MB average size suggests full-screen or extremely high-density assets. Audit the [library] files in the native_home component to ensure they are not using unnecessarily large source images.
       3. View Lifecycle Management:
           * Investigate why 21 [LibraryImage] instances are alive simultaneously. Ensure that views in the bottom
          tab are properly detached or their animations are cleared when switching between tabs.
       4. Fix Surface Leaks:
           * Address the Surface.release failures observed in the logs, as these can lead to both memory leaks and
             native resource exhaustion.

#### Additional resources for interpreting heap dumps

The following resources provide more information about interpreting heap dumps
and debugging memory usage:

- **Manual analysis:** Use the [Perfetto Heap Dump Explorer guidance](https://perfetto.dev/docs/visualization/heap-dump-explorer) to learn how to navigate and interpret heap dump visualizations in the Perfetto UI.
- **Java/Kotlin allocations:** Read [Visualizing your first ART heap dump](https://perfetto.dev/docs/visualization/heap-dump-explorer#visualizing-your-first-art-heap-dump) for a step-by-step walkthrough of analyzing Android Runtime (ART) heap dumps.
- **Native allocations:** Consult the [Perfetto Native Profiling](https://perfetto.dev/docs/data-sources/native-heap-profiler) documentation to learn how to collect and analyze native (C/C++) memory profiles.
- **CLI inspection:** Use [adb dumpsys meminfo](https://developer.android.com/tools/dumpsys) to get a quick breakdown of your app's memory usage on a device.

## Improve memory usage

Consult these sections to learn more about improving your app's memory usage:

- [Reduce your app's code and resource footprint](https://developer.android.com/topic/performance/memory/manage-app-memory#reduce-footprint)
- [Monitor available memory and memory usage](https://developer.android.com/topic/performance/memory/manage-app-memory#monitor)
- [Use more memory-efficient code constructs](https://developer.android.com/topic/performance/memory/manage-app-memory#code)

For detailed guidance on fixing memory issues, consult the [Manage your app's
memory](https://developer.android.com/topic/performance/memory) guide.