---
title: https://developer.android.com/topic/performance/issues/bitmap-memory-usage
url: https://developer.android.com/topic/performance/issues/bitmap-memory-usage
source: md.txt
---

> Documentation index: https://developer.android.com/topic/performance/issues/llms.txt

Bitmaps are often the largest memory-consuming objects in an app. Decoding and
scaling operations are frequently on the critical path for frame rendering.
Optimizing bitmap memory usage provides significant improvements in UI
responsiveness, battery life, and overall stability by reducing jank, ANRs, and
OOM-related process kills.

> [!NOTE]
> **Note:** For information on how Android Play Vitals tracks and reports this issue, see [Bitmap memory usage in Android vitals](https://developer.android.com/google/play/vitals/bitmap-memory-usage.md.txt).

## Contributors to high bitmap memory usage

> [!NOTE]
> **Note:** Bitmap memory usage doesn't always correlate with [anonymous RSS + swap memory usage](https://developer.android.com/topic/performance/issues/memory-usage.md.txt). This is because bitmap memory usage includes bitmaps allocated on the heap using `malloc` as well as other bitmaps (for example, bitmaps backed by shared memory or graphics buffers), while anonymous RSS + Swap includes only those bitmaps allocated using `malloc`.

Virtual memory that was never used may also be included in the calculation. If
you see unexpectedly high bitmap memory usage, verify you're not allocating
memory that goes unused.

## Resources

### Analyze bitmaps in Android Studio

#### Android Studio profiling for bitmaps

Use the Memory Profiler to inspect memory allocations in real-time, capture
heap dumps, and analyze objects for memory leaks; additionally, use the heap
analyzer to detect memory leaks, identify duplicate bitmap allocations, and
visualize object retention.

#### Automated leak detection with LeakCanary

Integrate the LeakCanary library to automate the detection of memory leaks in
your app. LeakCanary provides automatic heap analysis, identifying objects that
should have been garbage collected but are still held in memory, such as
bitmaps retained by destroyed components.

### Bitmap Performance Documentation

These resources provide comprehensive guidance on best practices for efficient
bitmap handling across different Android components.

- [Optimize bitmap memory](https://developer.android.com/topic/performance/memory/bitmaps.md.txt)
- [Bitmaps and memory](https://developer.android.com/topic/performance/memory/guide/bitmaps.md.txt)
- [Optimizing bitmap images (Compose)](https://developer.android.com/develop/ui/compose/graphics/images/optimization.md.txt)
- [Manage your app's memory](https://developer.android.com/topic/performance/memory/manage-app-memory.md.txt)

### Developer checklist for optimizing bitmap memory usage

To optimize bitmap memory efficiency, follow the three core principles: reduce,
reuse, and recycle. For architectural defect layers, adaptive cache formulas,
and library configuration snippets, see [Optimize bitmap memory](https://developer.android.com/topic/performance/memory/bitmaps.md.txt).

- **Reduce**: Minimize the initial memory footprint when loading or displaying bitmaps.
- **Reuse**: Consolidate image pipelines, eliminate duplicate decodes, and size caches to the active window.
- **Recycle**: Proactively release UI resources when your app's UI is hidden, including while running foreground services.

The following developer checklist can help you optimize bitmap memory usage.

| Core principle | Area | Description |
|---|---|---|
| **Reduce** | Implement container-bound downsampling | [Decode images to match target UI container bounds](https://developer.android.com/topic/performance/memory/bitmaps.md.txt#downsample-bounds) on both your CDN and client decoder instead of loading full-resolution or full-screen assets. |
| **Reduce** | Prefer `Bitmap.Config.HARDWARE` for static UI | [Enable hardware bitmaps](https://developer.android.com/topic/performance/memory/bitmaps.md.txt#pixel-configs) so immutable UI images reside in graphics memory rather than the native heap, and avoid blanket `RGB_565` on photo feeds. |
| **Reduce** | Prioritize `VectorDrawable` and zero-byte backgrounds | Use [vectors for icons](https://developer.android.com/develop/ui/compose/graphics/images/optimization.md.txt#vectors-bitmap) and `ColorDrawable` or `Modifier.background` instead of solid-color software bitmaps. |
| **Reduce** | Eliminate transparent margins | Avoid allocating memory for invisible border pixels by cropping margins and using `InsetDrawable` or layout padding. See [Trim transparent margins](https://developer.android.com/topic/performance/memory/bitmaps.md.txt#trim-and-vectors). |
| **Reuse** | Consolidate onto one image loader | Standardize on a [single shared image loader](https://developer.android.com/topic/performance/memory/bitmaps.md.txt#single-loader) per process (such as Coil or Glide) to avoid duplicate `LruCache` pools across Views and Compose. |
| **Reuse** | Eliminate duplicate bitmaps | Capture [lossless PNG heap dumps](https://developer.android.com/topic/performance/memory/bitmaps.md.txt#verify) (`adb shell am dumpheap -g -b png`) or use the [Memory Profiler](https://developer.android.com/studio/profile/capture-heap-dump.md.txt#duplicate-bitmaps) to detect and deduplicate identical pixel buffers, including vector animation raster frames. |
| **Reuse** | Size caches to the active window | Bound strong memory caches to [window pixel dimensions and RAM tier](https://developer.android.com/topic/performance/memory/bitmaps.md.txt#cache-formula) rather than static Java heap percentages. |
| **Recycle** | Configure `TRIM_MEMORY_UI_HIDDEN` eviction | [Configure Coil, Glide, Fresco, and Lottie](https://developer.android.com/topic/performance/memory/bitmaps.md.txt#loader-trim) to clear strong UI caches when the UI leaves the screen instead of waiting for `TRIM_MEMORY_BACKGROUND`. |
| **Recycle** | Clear UI caches under foreground services | Observe [`ProcessLifecycleOwner` `ON_STOP`](https://developer.android.com/topic/performance/memory/bitmaps.md.txt#fgs-trap) so UI bitmaps release even when an active foreground service keeps your process at perceptible priority. |
| **Recycle** | Cancel in-flight decodes and monitor leaks | Scope image requests to UI lifecycles so backgrounded scroll decodes don't inflate memory, and use LeakCanary and the Memory Profiler to catch backstack leaks. See [Manage your app's memory](https://developer.android.com/topic/performance/memory/manage-app-memory.md.txt). |