---
title: https://developer.android.com/topic/performance/vitals/memory-usage
url: https://developer.android.com/topic/performance/vitals/memory-usage
source: md.txt
---

Memory usage (anonymous RSS + swap) is a metric in Android vitals that reflects
your app's memory usage.

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

## Identify high memory usage

### Android vitals

Android vitals shares your app's memory usage broken down by the following
[process states](https://developer.android.com/guide/components/activities/process-lifecycle):

- **Foreground**: The app's process is visible. High P99 here often affects user-perceived performance (jank or OOM crashes) and is heavily driven by retaining UI components or activities that are no longer needed.
- **Perceptible Service** : The app's process is running in a [perceptible](https://developer.android.com/reference/android/app/ActivityManager.RunningAppProcessInfo#IMPORTANCE_PERCEPTIBLE) state. This includes [foreground services](https://developer.android.com/develop/background-work/services/fgs), expedited jobs, and [user-initiated data](https://developer.android.com/develop/background-work/background-tasks/uidt) transfer jobs. It can also extend to system-bound services or services bound by other apps. Because these services are designed for long-running tasks, holding onto memory due to leaks or failing to release resources can inflate the P99 tail over time.
- **Background**: The app is running a background service, or was recently backgrounded, but isn't yet cached. This is where background processing leaks and unreleased resources can compound. Because this process state is less important than foreground or perceptible processes, try to avoid retaining large amounts of memory in this state.
- **Cached**: The app is in a cached state. This state is highly sensitive to system memory pressure such as LMKs. Because the OS can evict this process state at will, this state is provided only for debug purposes.

To understand how these process states correlate with `onTrimMemory` callbacks,
consult the guidance on [releasing memory in response to events](https://developer.android.com/topic/performance/memory#release).

Android vitals also breaks down your app's memory usage by RAM buckets.
The memory usage metric is displayed as a timeline of daily percentile values,
alongside the most recent daily value for the 50th and 90th percentiles.

Once you have identified your memory baseline, follow the guidance to
[diagnose](https://developer.android.com/topic/performance/vitals/memory-usage#diagnose-excessive) and [improve](https://developer.android.com/topic/performance/vitals/memory-usage#improve-memory) excessive memory usage.

> [!NOTE]
> **Note:** The Anonymous RSS + Swap metric has a process name breakdown. You might see names that don't reflect your app processes. These processes might be associated with SDKs or other services in the system your app uses. You should work with the SDK developer to address any issues that can't be resolved otherwise.

#### Identify memory leaks using tail skew

To help identify memory leaks, look for a divergence between your typical (P50)
and tail-end (P90) users in Android vitals. While general asset bloat inflates
memory uniformly across all percentiles, memory leaks compound over time,
heavily skewing the tail-end data.

You should compare your P90 and P99 metrics against your P50 baseline by process
name. If your P90 to P50 ratio exceeds 3.5x, it indicates a likely memory leak
during extended sessions. For certain use cases, an elevated ratio doesn't
always indicate a leak, but you should evaluate the specific workflow to
determine if the elevated memory usage is expected behavior.

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

To investigate potential memory leaks, first identify the highest-consuming
processes using the **Process name** table in the Android vitals memory usage
dashboard. Next, run the corresponding user journeys locally and collect heap
dumps across different process states (visible, foreground service, and cached)
to verify if the app releases memory after being backgrounded.

If you're debugging memory issues using the Android Studio Profiler, you can
also use the [LeakCanary integration to streamline leak and duplicate
bitmap detection to optimize your image usage](https://developer.android.com/studio/releases#leakcanary).

> [!NOTE]
> **Note:** Android Studio doesn't support viewing a heap dump that was captured with a tool other than the Android Studio Memory Profiler.

After you've collected the heap dump, we recommend using the [Perfetto AI
Skills](https://github.com/google/perfetto/tree/main/ai/skills) to analyze the heap dump and identify potential sources
of high memory usage.

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
- **AI-assisted analysis:** Leverage [Perfetto AI Skills](https://github.com/google/perfetto/tree/main/ai/skills) to run LLM-powered analysis to help detect memory leaks and excessive allocations in your traces.
- **SQL-based analysis:** Use [Perfetto SQL and Trace Analysis Skills](https://github.com/android/skills/tree/main/profilers) to run structured queries and specialized scripts to analyze complex trace data.

### Improve memory usage

Consult these sections to learn more about improving your app's memory usage:

- [Reduce your app's code and resource footprint](https://developer.android.com/topic/performance/memory#reduce-footprint)
- [Monitor available memory and memory usage](https://developer.android.com/topic/performance/memory#monitor)
- [Use more memory-efficient code constructs](https://developer.android.com/topic/performance/memory#code)

For detailed guidance on fixing memory issues, consult the [Manage your app's
memory](https://developer.android.com/topic/performance/memory) guide.