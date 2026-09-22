---
title: https://developer.android.com/google/play/vitals/bitmap-memory-usage
url: https://developer.android.com/google/play/vitals/bitmap-memory-usage
source: md.txt
---

Bitmaps are often the largest memory-consuming objects in an app. Decoding and
scaling operations are frequently on the critical path for frame rendering.
Optimizing bitmap memory usage provides significant improvements in UI
responsiveness, battery life, and overall stability by reducing jank, ANRs, and
OOM-related process kills.

> [!NOTE]
> **Note:** For information on how to diagnose and resolve this issue, see [Bitmap memory usage](https://developer.android.com/topic/performance/issues/bitmap-memory-usage).

## Identify high bitmap memory usage

Android vitals provides metrics on an app's bitmap memory footprint by
aggregating data from Android devices. These metrics are calculated as a 28-day
summary of daily data by default. This data helps identify trends and potential
regressions in memory efficiency across different device types and versions.

Android vitals shares your app's bitmap memory usage broken down by the
following [process states](https://developer.android.com/guide/components/activities/process-lifecycle):

- **Foreground**: The app's process is visible. It's expected for the P99 to be significantly higher in foreground versus in other process states, but developers should investigate if the P99/P50 ratio is significant (e.g. higher than 3.5x), as this often points to a bitmap memory leak. You can identify this by looking for a divergence between typical usage (P50) and outlier usage (P99); while general asset bloat inflates memory uniformly across all percentiles, memory leaks compound over time, heavily skewing the tail-end data (P99). Ensure that foreground bitmap allocations don't persist unnecessarily after the app transitions to other states.
- **User-perceived services** : The app's process is running in a [perceptible](https://developer.android.com/reference/android/app/ActivityManager.RunningAppProcessInfo#IMPORTANCE_PERCEPTIBLE) state. This includes [foreground services](https://developer.android.com/develop/background-work/services/fgs), expedited jobs, and [user-initiated data](https://developer.android.com/develop/background-work/background-tasks/uidt) transfer jobs. Apps must not retain heavy foreground bitmap allocations when transitioning to these states. Because these services are designed for long-running tasks, holding onto large assets degrades the overall user experience and forces the Low Memory Killer Daemon (LMKD) to reclaim memory by terminating lower-priority processes.
- **Background**: The app is running a background service, or was recently backgrounded, but isn't yet cached. Because this process state is less important than foreground or perceptible processes, apps should explicitly release large bitmap assets here to reduce memory pressure.
- **Cached**: The app is in a cached state. This state is highly sensitive to system memory pressure such as LMKs. Apps must proactively reduce bitmap memory usage in this state to avoid eviction by the OS.

### Contributors to high bitmap memory usage

> [!NOTE]
> **Note:** Bitmap memory usage doesn't always correlate with [anonymous RSS + swap memory usage](https://developer.android.com/google/play/vitals/memory-usage). This is because bitmap memory usage includes bitmaps allocated on the heap using `malloc` as well as other bitmaps (for example, bitmaps backed by shared memory or graphics buffers), while anonymous RSS + Swap includes only those bitmaps allocated using `malloc`.

Virtual memory that was never used may also be included in the calculation. If
you see unexpectedly high bitmap memory usage, verify you're not allocating
memory that goes unused.