---
title: https://developer.android.com/topic/performance/memory/guide/tools-overview
url: https://developer.android.com/topic/performance/memory/guide/tools-overview
source: md.txt
---

When you need to investigate memory usage, start with high-level assessment
tools to identify which categories of memory are most significant.

## dumpsys meminfo

The most common way to get an overview of an application's memory usage is
`dumpsys meminfo`. To see a detailed breakdown including all memory mappings, it
is often helpful to include the `-a` flag:

    adb shell dumpsys meminfo -a <package_name_or_pid>

Here is a sample output from an application under some memory pressure (notice
the high SwapPss):

    ** MEMINFO in pid 4562 [com.android.memorylab] **
                       Pss  Private  Private  SwapPss      Rss     Heap     Heap     Heap
                     Total    Dirty    Clean    Dirty    Total     Size    Alloc     Free
                    ---   ---   ---   ---   ---   ---   ---   ---
      Native Heap      394      268       64    17440     4264    29416    18128     8040
      Dalvik Heap      165        8        0      672     8196    40949    32757     8192
     Dalvik Other       47       28        0      604     1132
            Stack      112      108        4      312      120
    ...
            TOTAL    33197      580      788    21920   167776    70365    50885    16232

     App Summary
                           Pss(KB)                        Rss(KB)
                            ---                         ---
               Java Heap:       12                          32608
             Native Heap:      268                           4264
                    Code:      724                         125672
                   Stack:      108                            120
                Graphics:        0                              0
           Private Other:      256
                  System:    31829
                 Unknown:                                    5112

               TOTAL PSS:    33197            TOTAL RSS:   167776       TOTAL SWAP PSS:    21920

     Objects
                   Views:       15         ViewRootImpl:        1
             AppContexts:        5           Activities:        1
    ...

### Interpreting the data

- **Pss Total** : The Proportional Set Size. This is the sum of `Private Dirty + Private Clean` + your process's equitable share of memory shared with other processes (like the Zygote boot image). This is the best metric for "how much memory is this app responsible for."
- **Private Dirty**: This is RAM that only your process is using and has been modified (or is anonymous memory). This is the most critical number for finding leaks because this memory cannot be dropped.
- **Private Clean**: RAM that only your process is using, but is an unmodified copy of a file on storage (like a DEX file). It can be dropped by the OS if memory is low.
- **SwapPss** : Memory that has been compressed and swapped into ZRAM. This can
  happen either because the system is under memory pressure or because the
  Android Runtime has identified background processes to compact (moving their
  unused or inactive pages to ZRAM). In the `dumpsys` example, almost all of
  the `Native Heap` and `Dalvik Heap` have been moved to ZRAM.

- **Key Point** : The **Java Heap** and **Native Heap** values in the
  "App Summary"section represent **resident** (physical) memory. If an
  application's memory has been compressed into ZRAM, these specific summary
  values may appear much lower than expected. Always check the
  **TOTAL SWAP PSS** or the detailed `SwapPss` column to get the full picture.

- **App Summary**: A higher-level categorization combining the detailed rows
  into understandable buckets.

- **Objects** : Useful for tracking leaked `Activities` and `ViewRootImpl`
  instances. If you back out of your app and force a GC, the `Activities`
  count should return to 0.

### Memory budget section

In Android 18 and higher, `dumpsys meminfo` also prints a **Memory Budget**
section when it dumps a single app. This section reads the [memcg
statistics](https://developer.android.com/topic/performance/memory/guide/tools-overview#memcg) of the process and of the whole app (the package), so
you don't need to find the cgroup files yourself. Here is the section from
the MemoryLab sample app in the foreground, after three taps of **Allocate Java
Memory (10MB)**:

     Memory Budget
                            Process(KB)       Package(KB)
                            ---       ---
      Current Usage:              83820             87976
      Limit:                       none           4718592
      Limit Source:                none     MemoryLimiter
      Peak Usage:                 85136             89292
      Swap Used:                      0                 0

      Usage Breakdown
        Anonymous:                81700             81700
        File:                        96              4200
        File Mapped:                 16               616
        Shared Memory:               16                16
        Kernel:                    1580              1632
        Page Tables:                640               640
        Slab:                       439               458

      Pressure & Reclaim
        Throttle Events:              0                 0
        Refaults (Anon):              0                 0
        Refaults (File):              0                 0

- **Current Usage** : Memory charged to the memcg (`memory.current`). This is the number that memory budgets limit. In the sample, it rose by about 36,700 KB after the three 10MB Java allocations, in line with **TOTAL
  PSS**. The package total is higher than the process total even for a single-process app when cached file pages from an earlier run haven't been reclaimed yet.
- **Limit** : The reclaim threshold (`memory.high`) that applies right now, or `none` if there isn't one. In the sample, the package has a system memory limit and the process has no limit of its own.
- **Limit Source** : Where the limit comes from. `AndroidManifest` is a `<memory-budget>` declared in the app manifest, `MemoryBudgetManager` is a budget that the app set at run time, `MemoryLimiter` is a system memory limit, and `am memory-limiter` is a manual override set with `adb`.
- **Peak Usage** : The highest charge since the memcg was created (`memory.peak`). This shows `N/A` on kernels that don't support it.
- **Swap Used** : Memory compressed into ZRAM (`memory.swap.current`).
- **Usage Breakdown** : The main fields of `memory.stat`, such as anonymous and file-backed memory.
- **Pressure \& Reclaim** : **Throttle Events** counts how many times the memcg went over its `memory.high` limit. **Refaults** count pages that were swapped out or evicted and then needed again. If these numbers climb while you use the app, the limit is tighter than the working set of the app.

With the `-a` or `-v` flag, the section also lists every raw counter from
`memory.stat` and `memory.events`.

> [!NOTE]
> **Note:** The Memory Budget section was added in Android 18. On devices running Android 17 QPR2 (API level 37.2), read the [memcg statistics](https://developer.android.com/topic/performance/memory/guide/tools-overview#memcg) directly.

### Practice exercise: quick triage with meminfo

This exercise shows how different types of allocations show up in `meminfo`.

1. **Launch the app**:

       adb shell am start -W -n com.android.memorylab/.MainActivity

2. **Check baseline memory**:

       adb shell dumpsys meminfo -s com.android.memorylab

   (The `-s` flag provides a short, concise summary of memory categories).
3. **Allocate Java Memory** : Tap the **Allocate Java Memory (10MB)** button 3
   times in the app.

4. **Observe the change** : Run `meminfo -s` again. You should see the **Java
   Heap** value increase by approximately 30,000 KB (30MB).

5. **Allocate Native Memory** : Tap the **Allocate Native Memory (1GB
   Incompressible)** button once.

6. **Observe the change** : Run `meminfo -s` again. The **Native Heap** value
   should now show a massive increase (\~1,000,000 KB).

7. **Compare with memcg (Android 18 and higher)** : Look at the **Memory
   Budget** section at the end of the `meminfo -s` output. **Current Usage**
   grows along with **TOTAL PSS** after each allocation, because both the Java
   and the native allocations are charged to the app's memcg.

### Global view

To see memory usage across the entire system, run:

    adb shell dumpsys meminfo

This provides a summary of RAM usage, including total RAM, free RAM, and a list
of processes sorted by PSS.

#### Key system metrics

- **ZRAM**: Compressed swap in RAM.
- **DMA-BUF** : Graphics and shared memory buffers. Modern Android versions use DMA-BUF extensively for UI rendering. If the `DMA-BUF` total is very high, investigate graphics-heavy processes using `/sys/kernel/debug/dma_buf/bufinfo`.
- **Lost RAM**: Memory that is not accounted for by the kernel or any process (e.g., hardware-reserved regions).

## memcg statistics

Every app process has its own memory control group (memcg), and the kernel
keeps running totals of the memory charged to it (see
[memcg](https://developer.android.com/topic/performance/memory/guide/concepts#memcg) for how this accounting differs from RSS and PSS).
Reading these files is cheap and doesn't disturb your app, so you can sample
them every second while you run a user flow.

> [!NOTE]
> **Note:** memcg metrics are supported on devices running Android 17 QPR2 (API level 37.2) and higher.

Look up the memcg path of a process from the `0::` line of `/proc/<PID>/cgroup`
instead of building the path yourself, because the cgroup layout can differ
between devices. Pass each device command to `adb shell` as a single quoted
string so that the device shell sees the quotes:

    PID=$(adb shell pidof -s <package_name>)

    CG=/sys/fs/cgroup$(adb shell "sed -n 's/^0:://p' /proc/$PID/cgroup")

    adb shell "cat $CG/memory.current $CG/memory.swap.current"

    adb shell "grep -E '^(anon|file|workingset_refault_.*) ' $CG/memory.stat"

The key files are:

- **`memory.current`**: Memory charged to the process, in bytes. This is the number that memory budgets limit.
- **`memory.swap.current`**: Memory compressed into ZRAM, in bytes.
- **`memory.stat`** : A breakdown of the charge, in bytes for sizes. `anon` is anonymous memory, such as the Java and native heaps. `file` is file-backed page cache, such as code and resources. `workingset_refault_anon` and `workingset_refault_file` count pages that were swapped out or evicted and then needed again. Rising refault counts mean that the process is short on memory.
- **`memory.events`** : Counts of memory limit events. `high` counts how many times the process was throttled for going over its `memory.high` limit.

The parent directory of the process memcg belongs to the whole app (its UID).
Its files include the memory of all the app's running processes, plus cached
file pages left over from earlier processes of the app that have exited and
haven't been reclaimed yet:

    adb shell "cat $CG/../memory.current"

If you get a permission error, run `adb root` and try again. Some devices only
let you read these files as root.

For a guided walkthrough of these files with the MemoryLab sample app, see
[Hands-on exercise: exploring memcg](https://developer.android.com/topic/performance/memory/guide/reclaim#hands-on-memcg).

## showmap

For a much more detailed breakdown of a process's memory mappings, use
`showmap`. This tool reads from `/proc/<pid>/smaps`.

> [!NOTE]
> **Note:** To run this command, you must build your app with `<profileable
> android:shell="true"/>` or `<debuggable>`.

    adb shell showmap <pid>

`showmap` lists every memory map in the process. Key mappings to look for
include:

- **`[anon:scudo:primary]` or `[anon:libc_malloc]`**: The native heap. Modern Android versions use the Scudo allocator.
- **`*.art`**: Java heap images (e.g., boot image).
- **`[anon:dalvik-main space]`**: The main Java heap.
- **`*.so`**: Shared libraries.
- **`*.{oat,dex,odex,vdex}`**: Compiled DEX code.

You can sort the output to find the largest private memory consumers:

    # Sort by private clean + private dirty memory
    adb shell showmap <pid> | awk '{print $6+$7, $0}' | sort -rn | head -n 10

Sample output:

     virtual                     shared   shared  private  private                   Anon      Shmem     File      Shared   Private
        size      RSS      PSS    clean    dirty    clean    dirty     swap  swapPSS HugePages PmdMapped PmdMapped Hugetlb  Hugetlb    Locked    # object
    --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
    2776    18176     5784     2823        0     3008      308     2468     4700     4700         0         0         0        0        0        0   47 [anon:scudo:primary]
    560      952      876      657      316        0      560        0       12       12         0         0         0        0        0        0    8 /data/app/.../base.apk
    448   393216      448      448        0        0        0      448        0        0         0         0         0        0        0        0    2 [anon:dalvik-main space]
    ...

### Practice exercise: deep dive with showmap

Learn how to identify specific memory mappings and differentiate between clean
and dirty memory.

1. **Mmap Clean Memory** : Tap the **Mmap Clean Anon Memory (10MB)** button in the MemoryLab app once.
2. **Get the Process ID**: The app's UI shows its PID. You can also find it
   with this command:

       adb shell pidof com.android.memorylab

3. **Inspect with showmap**:

       # Replace <PID> with the actual process ID from the previous step
       adb shell showmap <PID> | grep "memorylab-clean"

4. **Identify the mapping** : You should see an anonymous mapping labeled
   **`[anon:memorylab-clean]`** with a virtual size of exactly 10240 KB. Note
   that the **private dirty** value for this map is likely 0. This is "clean"
   anonymous memory because we used `mmap` to reserve the virtual space but
   haven't written to it yet (so no physical RAM is actually consumed).

5. **Native Heap Comparison** : Contrast this with the `[anon:scudo:primary]`
   mappings which would have appeared in `showmap` if you had run it after step
   5 of the `meminfo` exercise. Because that 1GB native allocation actually
   writes to every page, those pages are "dirty" and will show up heavily in
   the **private dirty** column.

6. **Pro-tip (Large Objects)** : Notice the **Java Heap** allocations from the
   `meminfo` exercise. Because they are 10MB byte arrays, they likely appear in
   `showmap` as `[anon:dalvik-free list large object space]`. The Android
   Runtime (ART) puts objects larger than 12KB into a separate Large Object
   Space (LOS) to avoid fragmentation in the main heap.

## procstats

While `meminfo` provides a snapshot in time, `procstats` provides historical
data by periodically sampling the state and memory use of all running
applications. This is the primary tool used for long-term memory health
monitoring and is what drives the memory usage reporting in Android Settings.

    # View stats for the last 3 hours
    adb shell dumpsys procstats --hours 3

### Understanding the states

The output of `procstats` can be overwhelming. The most critical part is the
parenthetical metrics next to each process state:

    Top: 100% (54MB-64MB-67MB / 49MB-58MB-61MB / 110MB-120MB-130MB over 4)

The format is:
**(% time in state) (minPss-avgPss-maxPss / minUss-avgUss-maxUss /
minRss-avgRss-maxRss over samples)**

- **Pss (Proportional Set Size)**: Shared memory is divided proportionally among processes.
- **Uss (Unique Set Size)**: Memory used only by this process (equivalent to Private Clean + Private Dirty).
- **Rss (Resident Set Size)**: Total physical memory used, including all shared pages (tends to over-count).

**Why this matters:**

- **Stable App**: min/avg/max are close together.
- **Memory Leak**: max is significantly higher than min, and the average creeps up over time as sample count increases.
- **Spiky Usage**: max is much higher than avg, indicating transient heavy operations (like image processing) that might cause OOMs if they happen at the wrong time.

### Process states

`procstats` tracks apps across several states (often abbreviated):

- **Persist**: Critical system processes that are always running.
- **Top**: The app is currently in the foreground and visible to the user.
- **ImpFg** (Important Foreground): Critical background processes (like IMEs) or apps with a foreground service.
- **ImpBg** (Important Background): Background processes that are considered important to the system.
- **Fgs** / **BFgs**: Foreground Services or Bound Foreground Services.
- **Service** / **ServRst**: Background services or services currently restarting.
- **Cached** / **LastAct**: Apps that are cached in the background for quick restart. These are safe for the system to kill.

### Device memory state and run time stats

`procstats` also tracks how much time the *entire device* spent under memory
pressure. Look for the **Run time Stats** section:

    Run time Stats:
      SOff/Norm: +1h10m15s
       SOn/Norm: +15m20s
            Low: +2m10s
           Crit: +45s

- **SOff / SOn**: Screen Off versus Screen On.
- **Norm / Mod / Low / Crit**: Memory pressure levels (Normal, Moderate, Low, Critical).

If a device is spending significant time in **Low** or **Crit** states, it will
feel sluggish as the kernel aggressively reclaims memory and the Low Memory
Killer (LMK) starts terminating background processes. You can then look through
the per-package stats to see which apps have high memory usage specifically when
the device is in these stressed states.

*** ** * ** ***

**[← Concepts](https://developer.android.com/topic/performance/memory/guide/concepts) \| [↑ Up](https://developer.android.com/topic/performance/memory/guide) \| [Java →](https://developer.android.com/topic/performance/memory/guide/java-memory)**