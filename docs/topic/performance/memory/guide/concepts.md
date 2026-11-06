---
title: https://developer.android.com/topic/performance/memory/guide/concepts
url: https://developer.android.com/topic/performance/memory/guide/concepts
source: md.txt
---

To understand memory usage on Android, you must look at the system from several
different perspectives, ranging from high-level Java objects down to low-level
kernel pages.

## The performance cliff

Memory use in and of itself is not a good or bad thing; what matters is what you
are using the memory for. However, as you approach the limit of available memory
on a device, you eventually "fall off a performance cliff."

![A graph showing stable performance until a certain memory threshold, followed
by a steep decline as the system starts thrashing and killing processes](https://developer.android.com/static/topic/performance/memory/guide/images/concepts/performance-cliff.png)

When you are far away from the cliff, adding a small amount of memory usage
(e.g., 50MB) may have no perceptible impact on performance. However, a cliff is
reached when the available RAM is exhausted. At this point, the operating system
must start paging out memory and killing processes to free up space. Beyond this
cliff, even a small increase in memory use can lead to significant "thrashing,"
where the device becomes unresponsive or appears to reboot because critical
processes are killed.

## The Android stack

Each layer of the Android stack has its own unique view of memory:

![A block diagram of the Android memory stack, showing Java applications at the
top, ART below them, and the Linux kernel with physical pages at the bottom](https://developer.android.com/static/topic/performance/memory/guide/images/concepts/android-stack.png)

1. **Applications (Java/Kotlin)**: Developers primarily see Java objects allocated on the Java heap.
2. **Android Runtime (ART)**: ART manages the Java/Kotlin heap by using virtual memory pages from the kernel. Formerly known as Dalvik (the terms are sometimes used interchangeably).
3. **Linux Kernel** : The kernel sees memory in terms of physical and virtual **pages**. Traditionally, these are 4KB, but Android also supports 16KB page sizes. The kernel knows nothing about "Java objects."

If you want to optimize memory, you must either optimize within your own layer
(e.g., loading fewer bitmaps) or understand the layers below you to see how your
high-level allocations translate to physical page usage.

## Memory types: anonymous vs. file-backed

Before diving into how the OS reclaims memory, you must understand the two
fundamental categories of memory pages in Linux:

1. **Anonymous Memory (`anon`)** : Memory that is *not* backed by a file on storage. This includes memory allocated by C/C++ `malloc` (like the Scudo allocator) and memory allocated for Java objects on the Java/Kotlin heap. Because this memory has no source file to return to, the OS must either keep it in RAM or compress and swap it out to ZRAM when under pressure.
2. **File-Backed Memory (`file`)** : Memory that is mapped directly from a file on storage. This includes executable code (DEX files, `.so` native libraries) and fonts.

> > [!NOTE]
> > **Note:** Android does not use traditional disk swap space. Instead, it uses **ZRAM**, a compressed block of memory within RAM.
>
## Memory mapped files (mmap)

Android uses `mmap` to map both file-backed and anonymous memory into a
process's address space.

When dealing with file-backed memory, pages are further classified into:

- **Clean Memory**: Pages mapped from a file that have not been modified. If the system needs more memory, the kernel can simply drop these pages, as they can be re-loaded directly from the file on storage later.
- **Dirty Memory**: Pages that have been modified by the process. These cannot be dropped; they behave like anonymous memory and must be kept in RAM or moved to ZRAM.

Android prefers file formats (like DEX) that are amenable to memory mapping,
allowing the system to easily reclaim clean memory under pressure. **Because
anonymous and dirty memory cannot be simply dropped, high private dirty/anon
memory is the primary cause of system thrashing and Low Memory Killer (LMK)
interventions.** If your application uses a lot of private dirty memory, you are
directly contributing to the performance cliff.

## The Zygote process model

Android minimizes the cost of starting new applications by using a process
called **Zygote**.

1. Zygote starts up at boot and preloads common framework classes and resources into its memory. From the kernel's perspective, this becomes **anonymous
   dirty memory**, but it is unique to the Zygote process.
2. When a new application starts, the system **forks** the Zygote process.
3. The new child process inherits the memory of the Zygote using a **shared
   mapping** with **copy-on-write (COW)** semantics.

![A diagram illustrating the Zygote process sharing memory pages with newly
forked child processes using Copy-on-Write semantics](https://developer.android.com/static/topic/performance/memory/guide/images/concepts/zygote-cow.png)

As long as the child process only reads the memory inherited from Zygote, the
physical memory pages remain shared between all processes. When a child process
modifies a shared page, the kernel transparently creates a private copy of that
page for the process. This model allows many processes to share a large portion
of their memory---especially the framework code and resources---significantly
reducing the overall system memory footprint.

## RSS, PSS, USS, and memcg

Because memory is shared heavily between processes---primarily through the Zygote
model---there are several ways to account for a process's memory usage. RSS, PSS,
and USS count the pages that are mapped into the address space of a process:

![A diagram visualizing the difference between Resident Set Size (RSS),
Proportional Set Size (PSS), and Unique Set Size (USS) showing how shared memory
pages are accounted for](https://developer.android.com/static/topic/performance/memory/guide/images/concepts/rss_pss_uss.png)

- **RSS (Resident Set Size)**: The total number of pages the process has in RAM. This overestimates usage because it counts shared pages multiple times (once for every process sharing them).
- **PSS (Proportional Set Size)**: The total amount of memory unique to the process, plus its proportional share of shared memory. If a page is shared by 5 processes, each process is charged for 1/5th of that page.
- **USS (Unique Set Size)**: The amount of memory that is unique to the process. This is the memory that would be returned to the system if the process were killed.

> [!NOTE]
> **Note:** None of these metrics (RSS, PSS, or USS) include pages that have been compressed and swapped into ZRAM, or pages that have been reclaimed by the kernel. Memory usage metrics on Android generally represent just resident memory.

### memcg: the kernel's own accounting

The kernel also keeps its own running total of the memory that each process
uses, whether or not that memory is mapped. On Android, every app process
belongs to its own [memory control group (memcg)](https://developer.android.com/topic/performance/memory/guide/reclaim#memory-control-groups-memcg), nested inside
a memcg for the whole app (see [The Android memcg hierarchy](https://developer.android.com/topic/performance/memory/guide/reclaim#android-memcg-hierarchy)).
Whenever a page of memory is allocated, the kernel *charges* it to the memcg of
the process that allocated it. The total charge is in the `memory.current` file
of the memcg.

memcg accounting differs from RSS, PSS, and USS in a few important ways:

- **Each page is charged exactly once**, to the memcg of the process that first brought it into memory. The charge stays there even if other processes map the same page later. Pages that Zygote preloads are charged to Zygote, not to your app. When your app writes to one of these pages, the private copy is charged to your app.
- **It includes memory that page-table metrics can't see.** `memory.current` counts file pages that your app reads without mapping them (for example, database pages read with `read` or `pread`).
- **It tracks swap separately.** Memory that's compressed into ZRAM moves out of `memory.current` and into `memory.swap.current`, so you can see both without guessing.
- **It's cheap to read.** The counters are always up to date, and reading them doesn't lock or scan your app's address space.
- **It's what the system limits.** The memory limits and [memory
  budgets](https://developer.android.com/topic/performance/memory/app-memory-budgets) that Android applies to apps act on memcg charge.

Graphics memory, such as the buffers behind hardware bitmaps, generally isn't
charged to your app's memcg.

> [!NOTE]
> **Note:** memcg metrics are supported on devices running Android 17 QPR2 (API level 37.2) and higher. On earlier versions, per-process memcg files might be missing or laid out differently, depending on the device.

### Which metrics to use, when?

Choosing the right memory metric depends on what you are trying to measure and
the environment in which you are measuring it. On devices running Android 17
QPR2 (API level 37.2) and higher, start with memcg when you track your own app.

| Metric | Best For | Key Strength | Main Drawback |
|---|---|---|---|
| **memcg** | Tracking an individual app over time, comparing against budgets | Counts each page once, includes unmapped page cache, tracks swap separately. Cheap to read. | Not available on all devices before Android 17 QPR2. Shared pages are charged to the process that touched them first. |
| **PSS** | System-wide memory snapshots | Accurately proportions shared memory. Summing PSS equals total memory used. | Fluctuates based on other running processes. Bad for comparing a specific app over time. |
| **RSS** | Tracking an individual app over time, field telemetry | Stable, independent of other processes. Fast and cheap to collect. | Overestimates total usage because it counts shared memory multiple times. |
| **USS** | Assessing the impact of killing a process | Shows exactly how much memory would be freed if the app was terminated. | Ignores shared memory entirely. |

#### memcg (memory control group charge)

- **Best for:** Tracking an individual app's memory usage over time, across Critical User Journeys (CUJs), or between app versions, on devices running Android 17 QPR2 or higher. It's also the metric to watch when you [calibrate memory budgets](https://developer.android.com/topic/performance/memory/app-memory-budgets#calibrate-budgets), because it's the number that budgets limit.
- **Why:** Like RSS, memcg charge doesn't change when other apps start or stop sharing pages with your app. Unlike RSS, it never counts a page twice, so you can add up the charge of all your app's running processes. The whole-app memcg can be higher than that sum, because it keeps cached file pages from exited processes until the kernel reclaims them. It also counts memory that RSS, PSS, and USS miss, such as unmapped file cache. Reading it is cheap, because the kernel updates the counters as it charges pages.
- **How to read it:** Read `memory.current`, `memory.swap.current`, and `memory.stat` in the memcg directory of a process (see [memcg
  statistics](https://developer.android.com/topic/performance/memory/guide/tools-overview#memcg)). In Android 18 and higher, [`dumpsys
  meminfo`](https://developer.android.com/topic/performance/memory/guide/tools-overview#memory-budget) also prints them. From inside your app, use [`MemoryBudgetManager`](https://developer.android.com/topic/performance/memory/app-memory-budgets#query-usage).
- **Field Measurement Best Practices:** For the same reasons explained in [RSS](https://developer.android.com/topic/performance/memory/guide/concepts#rss-resident-set-size), track **anonymous memory + swap** : the `anon` field of `memory.stat` plus `memory.swap.current`. The `file` field of `memory.stat` includes file pages that your app read once and that the kernel hasn't reclaimed yet, so `memory.current` can stay high for a while after your app stops using that memory.
- **When to be careful:** Because pages are charged to the process that touched them first, your app is charged for a shared file page (such as a font or a shared library) that it reads before any other process does. Conversely, another process might be charged for pages that your app also uses. Expect small differences between devices and runs for file-backed memory, and rely on `anon` and swap when you compare.

#### PSS (Proportional Set Size)

- **Best for:** Taking a complete system memory snapshot of a certain device at a given time.
- **Why:** PSS has the useful mathematical property that the sum of the PSS for all running processes equals the total memory used by processes in the system. It perfectly apportions shared memory without double-counting.
- **When to avoid:** You must not use PSS to compare a specific process across two different snapshots, at different times, or across different devices. Because PSS depends on how many *other* processes are currently sharing pages with your process, your app's PSS can fluctuate even if your app's actual behavior remains completely unchanged.

#### RSS (Resident Set Size)

- **Best for:** Tracking an individual app's memory usage over time, across different Critical User Journeys (CUJs), or comparing between app versions. It is also the most practical choice for field telemetry.
- **Why:** RSS is more stable than PSS. It tells you about the memory mapped into your process regardless of what other apps are doing. Furthermore, RSS is cheap to collect. Measuring PSS or USS requires scanning complex kernel memory management structures and obtaining locks, which can cause system performance issues (like UI jank) if collected too frequently.
- **Field Measurement Best Practices:** When collecting data from devices in the wild, it is usually best to measure **anonymous RSS + swap (ZRAM)** .
  - *Why anonymous only?* File-backed pages (like code, app resources, fonts, or other memory-mapped files) can be evicted by the kernel at any time due to system-wide pagecache pressure. Including file pages in metrics to track a particular app introduces noise from the OS's memory management decisions that may be driven by memory pressure from other apps or the system. Conversely, anonymous memory (like the Java and native heaps) is directly controlled by your app.
  - *Why add swap?* Under memory pressure, the OS will compress anonymous pages and move them to ZRAM (swap). If you only measure resident anonymous memory, your metrics might falsely show a "decrease" in memory usage simply because the system was under pressure and swapped out your pages. Adding swapped memory ensures you account for all the anonymous memory your app has allocated, whether it currently resides in RAM or ZRAM.
  - *Prefer memcg when you can.* On devices running Android 17 QPR2 and higher, `anon` in `memory.stat` plus `memory.swap.current` gives you a similar measurement that leaves out anonymous pages shared with Zygote, and is cheaper to collect (see [memcg](https://developer.android.com/topic/performance/memory/guide/concepts#memcg-charge)).

#### USS (Unique Set Size)

- **Best for:** Determining the immediate system impact of killing a process.
- **Why:** USS accurately represents the exact amount of memory that would be immediately reclaimed and returned to the system if the process were terminated (for instance, by the Low Memory Killer daemon, `lmkd`).
- **How to use:** This metric is highly valuable when evaluating persistent processes or background services. If you are assessing the system-wide cost of a background process, USS tells you exactly how much memory the system is sacrificing exclusively to keep that specific process alive.

*** ** * ** ***

**[↑ Up](https://developer.android.com/topic/performance/memory/guide) \| [Tools →](https://developer.android.com/topic/performance/memory/guide/tools-overview)**