---
title: https://developer.android.com/topic/performance/vitals/bitmap-memory-usage
url: https://developer.android.com/topic/performance/vitals/bitmap-memory-usage
source: md.txt
---

Bitmaps are often the largest memory-consuming objects in an app. Decoding and scaling operations are frequently on the critical path for frame rendering. Optimizing bitmap memory usage provides significant improvements in UI responsiveness, battery life, and overall stability by reducing jank, ANRs, and OOM-related process kills.

## Identify high bitmap memory usage

Android vitals provides metrics on an app's bitmap memory footprint by aggregating data from Android devices. These metrics include period-based (for example, 28-day) percentiles per package and process. This data helps identify trends and potential regressions in memory efficiency across different device types and versions.

Android vitals shares your app's bitmap memory usage broken down by the following [process states](https://developer.android.com/guide/components/activities/process-lifecycle):

- **Foreground**: The app's process is visible. It is expected for the P99 to be significantly higher in foreground versus in other process states, but developers should investigate if the P99/P50 ratio is significant (e.g. higher than 3.5x), as this often points to a bitmap memory leak. You can identify this by looking for a divergence between typical usage (P50) and outlier usage (P99); while general asset bloat inflates memory uniformly across all percentiles, memory leaks compound over time, heavily skewing the tail-end data (P99). Ensure that foreground bitmap allocations don't persist unnecessarily after the app transitions to other states.
- **User-perceived services** : The app's process is running in a [perceptible](https://developer.android.com/reference/android/app/ActivityManager.RunningAppProcessInfo#IMPORTANCE_PERCEPTIBLE) state. This includes [foreground services](https://developer.android.com/develop/background-work/services/fgs), expedited jobs, and [user-initiated data](https://developer.android.com/develop/background-work/background-tasks/uidt) transfer jobs. Apps must not retain heavy foreground bitmap allocations when transitioning to these states. Because these services are designed for long-running tasks, holding onto large assets degrades the overall user experience and forces the Low Memory Killer Daemon (LMKD) to reclaim memory by terminating lower-priority processes.
- **Background**: The app is running a background service, or was recently backgrounded, but isn't yet cached. Because this process state is less important than foreground or perceptible processes, apps should explicitly release large bitmap assets here to reduce memory pressure.
- **Cached**: The app is in a cached state. This state is highly sensitive to system memory pressure such as LMKs. Apps must proactively reduce bitmap memory usage in this state to avoid eviction by the OS.

### Contributors to high bitmap memory usage

> [!NOTE]
> **Note:** Bitmap memory usage doesn't always correlate with [anonymous RSS + swap memory usage](https://developer.android.com/topic/performance/vitals/memory-usage). This is because bitmap memory usage includes bitmaps allocated on the heap using `malloc` as well as other bitmaps (for example, bitmaps backed by shared memory or graphics buffers), while anonymous RSS + Swap includes only those bitmaps allocated using `malloc`.

Virtual memory that was never used may also be included in the calculation. If you see unexpectedly high bitmap memory usage, verify you're not allocating memory that goes unused.

## Resources

### Analyze bitmaps in Android Studio

#### Android Studio profiling for bitmaps

Use the Memory Profiler to inspect memory allocations in real-time, capture heap dumps, and analyze objects for memory leaks; additionally, use the heap analyzer to detect memory leaks, identify duplicate bitmap allocations, and visualize object retention.

#### Automated leak detection with LeakCanary

Integrate the LeakCanary library to automate the detection of memory leaks in your app. LeakCanary provides automatic heap analysis, identifying objects that should have been garbage collected but are still held in memory, such as bitmaps retained by destroyed Activities or Fragments.

### Bitmap Performance Documentation

These resources provide comprehensive guidance on best practices for efficient bitmap handling across different Android components.

- [Managing Bitmap Memory](https://developer.android.com/topic/performance/graphics/manage-memory)
- [Optimizing Bitmap Images](https://developer.android.com/develop/ui/compose/graphics/images/optimization)
- [Manage your app's memory](https://developer.android.com/topic/performance/memory)

### Developer checklist for optimizing bitmap memory usage

To optimize bitmap memory efficiency, follow the three core principles: reduce, reuse, and recycle.

- **Reduce**: Minimize the initial memory footprint when loading or displaying bitmaps.
- **Reuse**: Implement caching mechanisms to avoid redundant bitmap allocations.
- **Recycle**: Proactively release resources to allow memory re-allocation for active processes.

The following developer checklist can help you optimize bitmap memory usage.

| Core Principle | Area | Description |
|---|---|---|
| **Reduce** | Eliminate Duplicate Bitmaps | Analyze heap dumps [using the Memory Profiler](https://developer.android.com/topic/performance/memory#monitor) to detect redundant bitmap allocations. Refer to the [Managing Bitmap Memory](https://developer.android.com/topic/performance/graphics/manage-memory) guide. |
|   | Leverage Image Loading Libraries | Use [libraries like Glide and Coil](https://developer.android.com/develop/ui/compose/graphics/images/optimization#bitmap-libraries), to automate threading, caching, and efficient decoding. |
|   | Implement Downsampling | [Decode images](https://developer.android.com/develop/ui/compose/graphics/images/optimization#downsample) to match target UI container dimensions instead of loading full-resolution assets. |
|   | Use RGB_565 for Opaque Images | Reduce memory footprint by 50% by [switching from `ARGB_8888` to a 16-bit configuration](https://developer.android.com/develop/ui/compose/graphics/images/optimization#pixel-format) for images without transparency. |
|   | Prioritize VectorDrawables | Use [vectors for icons and basic graphics](https://developer.android.com/develop/ui/compose/graphics/images/optimization#vectors-bitmap) to ensure sharp scaling with minimal memory overhead. |
|   | Optimize Server-Side Image Delivery | Configure backend APIs to [serve images tailored to device density](https://www.youtube.com/watch?v=4BlGtrTeCMU&t=1234s) and ImageView dimensions. |
|   | Eliminate Transparent Margins | Avoid allocating memory for "invisible" pixels by using InsetDrawable or layout padding instead of baked-in margins. See [Engineering memory-performant Android apps](https://www.youtube.com/watch?v=fOXJR5qLq54). |
| **Reuse** | Configure Optimal Cache Sizes | Tailor memory and disk cache limits based on device RAM and screen resolution. Refer to [Caching Bitmaps](https://developer.android.com/topic/performance/graphics/cache-bitmap). |
| **Recycle** | Purge Resources in Background | [Implement `TRIM_MEMORY_BACKGROUND`](https://developer.android.com/topic/performance/memory#release) to clear caches and improve process survival during system memory pressure. |
|   | Release Assets when UI is Hidden | [Use `TRIM_MEMORY_UI_HIDDEN`](https://developer.android.com/topic/performance/memory#release) to release bitmap caches when the app is no longer visible to the user. |
|   | Monitor for Memory Leaks | Use LeakCanary and Memory Profiler to find bitmaps retained after their LifecycleOwner is destroyed. Refer to [Manage your app's memory](https://developer.android.com/topic/performance/memory). |