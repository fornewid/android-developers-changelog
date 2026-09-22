---
title: https://developer.android.com/google/play/vitals/memory-usage
url: https://developer.android.com/google/play/vitals/memory-usage
source: md.txt
---

Memory usage (anonymous RSS + swap) is a metric in Android vitals that reflects
your app's memory usage.

[Anonymous memory](https://developer.android.com/topic/performance/memory-management#memory_pages) is memory not backed by a file on storage, such as
heap allocations and mmap-allocated memory. [Resident Set Size](https://developer.android.com/topic/performance/memory-management#calculating_memory_footprint) (RSS) is the
total number of memory pages (both shared and non-shared) used by a process that
are held in physical RAM. For anonymous memory, the system can write pages to
[swap space (or zRAM on Android)](https://developer.android.com/topic/performance/memory-management#types_of_memory) when memory is under pressure.

Altogether, memory usage (anonymous RSS + swap) is a measure of your app's
total number of memory pages not backed by a file on storage, inclusive of any
memory that's also being preserved by the system in swap. Tracking anonymous
RSS + swap ensures you see your app's true, unevictable memory footprint.

> [!NOTE]
> **Note:** For information on how to diagnose and resolve this issue, see [Memory usage (anonymous RSS + swap)](https://developer.android.com/topic/performance/issues/memory-usage).

## Identify high memory usage

### Android vitals

Android vitals shares your app's memory usage broken down by the following
[process states](https://developer.android.com/guide/components/activities/process-lifecycle):

- **Foreground**: The app's process is visible. High P99 here often affects user-perceived performance (jank or OOM crashes) and is heavily driven by retaining UI components or activities that are no longer needed.
- **User-perceived services** : The app's process is running in a [perceptible](https://developer.android.com/reference/android/app/ActivityManager.RunningAppProcessInfo#IMPORTANCE_PERCEPTIBLE) state. This includes [foreground services](https://developer.android.com/develop/background-work/services/fgs), expedited jobs, and [user-initiated data](https://developer.android.com/develop/background-work/background-tasks/uidt) transfer jobs. It can also extend to system-bound services or services bound by other apps. Because these services are designed for long-running tasks, holding onto memory due to leaks or failing to release resources can inflate the P99 tail over time.
- **Background**: The app is running a background service, or was recently backgrounded, but isn't yet cached. This is where background processing leaks and unreleased resources can compound. Because this process state is less important than foreground or perceptible processes, try to avoid retaining large amounts of memory in this state.
- **Cached**: The app is in a cached state. This state is highly sensitive to system memory pressure such as LMKs. Because the OS can evict this process state at will, this state is provided only for debug purposes.

To understand how these process states correlate with `onTrimMemory` callbacks,
consult the guidance on [releasing memory in response to events](https://developer.android.com/topic/performance/memory/manage-app-memory#release).

Android vitals also breaks down your app's memory usage by RAM buckets.
The memory usage metric is displayed as a timeline of daily percentile values,
alongside the most recent daily value for the 50th and 90th percentiles.

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