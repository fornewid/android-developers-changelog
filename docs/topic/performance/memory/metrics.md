---
title: https://developer.android.com/topic/performance/memory/metrics
url: https://developer.android.com/topic/performance/memory/metrics
source: md.txt
---

> Documentation index: https://developer.android.com/topic/performance/memory/llms.txt

There are many different metrics you can use to track your app's use of memory.
Each of these metrics has a different purpose. If you're trying to diagnose and
solve a problem with your app's performance, it's important to know which metric
you should be looking at. This page provides an overview of some of the most
important metrics.

## Background

To understand the different metrics, you need an understanding of how the
Android system handles memory. For detailed information, see [Overview of memory
management](https://developer.android.com/topic/performance/memory-overview). This section summarizes some of the most relevant information
for understanding memory metrics.

### Android memory

The Android operating system is built on a Linux kernel. Linux has two
fundamental categories of memory pages:

- **Anonymous memory** is memory that is *not* backed by a file in the device's storage. This includes memory that is allocated by functions like C's `malloc`, as well as memory allocated for objects on the heap.
- **File-backed memory** is memory that is mapped directly from a file in storage. This includes executable files (like DEX files) and resources like fonts.

This distinction is important because if memory is tight, the system can free up
a page that's directly mapped from a file. When that page is needed again, the
system can just map the file again. By contrast, anonymous memory has to be
swapped to zRAM or the information is lost.

File-backed memory can be further divided into two categories: **clean** and
**dirty** memory.

- Clean memory is a memory page that has been mapped from a file and has not been altered. That means the page can be dropped if the memory is needed.
- Dirty memory has been altered since it was mapped from the file. Private dirty pages are like anonymous memory---they can't be dropped, and have to be swapped to zRAM if memory is tight.

For more information about these categories, see the [Android memory
fundamental concepts](https://developer.android.com/topic/performance/memory/guide/concepts) page.

To improve the device's performance, it's important for your app to be using
clean file-backed memory as much as possible. If you're using a lot of dirty
or anonymous memory, that can result in system thrashing and, ultimately, in
low-memory killer (LMK) events.

This is why, for example, the DEX format has bytecode the app can use directly
without modifying. That means pages mapped from the DEX file stay clean, and can
be safely dropped if memory is tight.

### Zygote

When Android boots up, it creates a [zygote process](https://source.android.com/docs/core/runtime/zygote) containing core classes
and resources. Whenever a new app starts, the system forks the zygote process,
and uses the new copy for the app. This approach speeds up the app's launch. It
also helps save memory. Every app starts off sharing its zygote's memory, with
copy-on-write semantics. This means the app doesn't need its own copy of any
pages it shares with the zygote process unless the app modifies the page. If it
*does* modify a page, the app gets its own copy transparently--it doesn't have
to do anything special to get that copy.

## Key memory metrics

If you're trying to improve your app's performance, there are a number of memory
metrics to look at, each of which measures something slightly different.

### RSS, PSS, and USS

You might want to know how many pages a process is using. That's actually a
complicated question. There are three different metrics tracking your app's page
use. Each metric tells you something slightly different.

- [**Resident set size (RSS)**](https://developer.android.com/studio/profile/chart-glossary/process-memory.md.txt) measures the total number of pages used by your process, including shared pages.
  - The [Android vitals memory usage metric](https://developer.android.com/google/play/vitals/memory-usage.md.txt) is the sum of anonymous RSS pages in RAM plus anonymous pages swapped to zRAM.
- **Unique set size (USS)** measures the number of pages used *only* by your process, not shared with any other process.
- **Proportional set size (PSS)** is an approximation of how much memory your process is costing the system. It's the sum of USS, plus a proportional share of the pages your process is sharing with other processes. For example, if five processes share a page, each process gets 20% of that page's size counted in their PSS.

> [!NOTE]
> **Note:** The RSS, USS, and PSS metrics do *not* include pages that were swapped to zRAM. However, anonymous RSS + swap, [app memory budgets](https://developer.android.com/topic/performance/memory/app-memory-budgets.md.txt), and the [Android
> 17 memory limiter](https://source.android.com/docs/core/perf/memory-limiter) all include swapped pages, since these pages still sit compressed in RAM.

Each of these metrics is useful for some things, but each can be deceptive. A
process that's newly forked from zygote might have an RSS of 100 MB or more,
even though very little memory is uniquely allocated to the process---that 100 MB
might just be the pages it's sharing with zygote. By contrast, if you fork a
process, the two child processes might each have a very small USS, because the
processes are sharing almost all pages with each other. That might give a
deceptively small sense of how much memory each process needs. PSS attempts to
give you a full picture of the load your process is putting on the system, but
it's just an approximation.

### Bitmap usage

Bitmaps can end up being the largest share of your app's memory. Your app's
graphics resources might be coded in other formats, but the graphic has to be
expanded to a bitmap to be displayed on the device.

[Android vitals helps you track your app's bitmap memory usage](https://developer.android.com/google/play/vitals/bitmap-memory-usage.md.txt) across
devices. It provides four metrics you should be aware of:

- **Foreground** tracks bitmap usage when the app is visible. That's when an app's bitmap usage is expected to be the highest. However, you should check to see if there's a big divergence between your app's extreme cases (P99) and its median memory usage (P50), which might indicate a memory leak.
- **User-perceived services** tracks bitmap usage when the app is not in the foreground, but is still considered perceptible (for example, because the app is running a foreground service or an expedited job). An app might be in this state for a long time, so it's very important that it *not* be holding a lot of bitmaps while it's in the perceptible state.
- **Background** tracks an app's usage when it's running a background service, or when it's been recently sent to the background and is not yet cached. Apps in the background state should explicitly release large bitmap assets to relieve memory pressure.
- **Cached** tracks your app's usage while it's cached. If the device is low on memory, the system will start killing cached apps. It's best to proactively free whatever memory you can, especially bitmaps, to make your app less vulnerable to LMK events.

The [Android vitals bad behavior thresholds](https://developer.android.com/google/play/vitals.md.txt#what_are_the_bad_behavior_thresholds) for bitmap
memory apply to User-perceived services, Background, and Cached,
but not to Foreground, which is mainly a diagnostic signal.

> [!NOTE]
> **Note:** For standard heap bitmaps, the pixel data is stored on the native heap, with only a small wrapper in the Java heap. By contrast, [hardware bitmaps](https://developer.android.com/topic/performance/memory/guide/bitmaps.md.txt#hardware-bitmaps) store pixel data in graphics memory. The Android vitals bitmap metric counts both standard and hardware bitmaps.

You can use Android Studio to [check a heap dump for duplicate bitmaps](https://developer.android.com/studio/profile/capture-heap-dump.md.txt#duplicate-bitmaps).
Alternatively, if you're using an AI coding agent, you can use the
[`android-profiler` skill](https://github.com/android/skills/tree/main/profilers/android-profiler) to capture a heap dump, then
query `Bitmap` instances and their retaining paths with PerfettoSQL.

### DEX code optimization

You can improve your app's memory footprint by optimizing its DEX code.

You can use the [R8 configuration analyzer](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer.md.txt) to get detailed information on
the DEX file's shrinking, obfuscation, and optimization. You can also get this
information by using the [R8 analyzer skill](https://github.com/android/skills/tree/main/performance/r8-analyzer). The shrinking, obfuscation, and
optimization scores can help identify your app's potential for R8 optimization.
Android vitals also reports your DEX code optimization scores as the
[DEX code optimization](https://developer.android.com/google/play/vitals/code-optimization.md.txt) finding.

To make further improvements, use R8 with [baseline profiles](https://developer.android.com/topic/performance/baselineprofiles/overview.md.txt) and measure
memory usage with the [Macrobenchmark library](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview.md.txt).