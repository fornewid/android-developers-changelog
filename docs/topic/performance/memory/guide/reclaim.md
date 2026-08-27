---
title: https://developer.android.com/topic/performance/memory/guide/reclaim
url: https://developer.android.com/topic/performance/memory/guide/reclaim
source: md.txt
---

In previous sections, we saw how the kernel manages memory system-wide. In this
chapter, we dive deeper into **Memory Control Groups (memcg)**, the mechanism
Android uses to partition and control memory usage for individual apps.

Understanding memcg is crucial because it's the level at which the system can
target individual apps for reclaim or set memory limits on them, allowing
proactive management of app memory footprints.

## Memory control groups (memcg)

Control Groups (cgroups) are a Linux kernel feature that allows organizing
processes into hierarchical groups and distributing system resources (like CPU,
memory, and I/O) among them. **memcg** is the cgroup controller specifically for
memory.

### Key memcg concepts

- **Memcg Charge**: When a process in a memcg allocates a page of memory (either anonymous or file-backed), that page is "charged" to the memcg. The total charge of a memcg is the sum of all pages used by all processes within it.
- **Hierarchical Accounting**: Memory usage is accounted for up the tree. A charge in a child cgroup also counts towards the usage of its parent.
- **Memory Limits** : Each memcg can have limits (like `memory.max` or `memory.high`) that trigger reclaim or even the OOM killer if exceeded, independent of global system memory.
- **Per-memcg Reclaim**: When a memcg is over its limit, or when the system needs memory, the kernel can target a specific memcg for reclaim. This means evicting its file pages or swapping its anonymous pages to ZRAM.

## The Android memcg hierarchy

Android uses a specific hierarchy to manage app processes. This structure allows
the system to apply different policies to different types of apps (e.g.,
foreground vs. background).

![Android memcg Hierarchy](https://developer.android.com/static/topic/performance/memory/guide/images/reclaim/memcg_hierarchy.png)

- **`/sys/fs/cgroup/apps/`**: The root for all Android applications.
- **`uid_<UID>/`**: A directory for each app's User ID. All processes belonging to the same app package share this group.
- **`pid_<PID>/`**: A directory for each individual process and any children forked from it. This allows fine-grained control and accounting for apps with multiple processes.

## Hands-on exercise: exploring memcg

In this exercise, you will find the memcg directory for **MemoryLab** and
observe its memory charge in real-time.

### 1. Launch MemoryLab

Ensure **MemoryLab** is running on your device.

### 2. Find MemoryLab's memcg

First, get the PID of the running MemoryLab app:

    adb shell pidof com.android.memorylab
    # Example output: 11672

Now, locate its cgroup directory. You can find this in `/proc/<PID>/cgroup`:

    adb shell cat /proc/11672/cgroup
    # Example output: 0::/apps/uid_10274/pid_11672

In cgroup v2, the path after the `0::` represents the memcg hierarchy relative
to `/sys/fs/cgroup`. So the full path is
`/sys/fs/cgroup/apps/uid_10274/pid_11672/`.

### 3. Read memcg stats

Go into that directory and look at the key files:

    # Current memory usage (in bytes)
    adb shell cat /sys/fs/cgroup/apps/uid_10274/pid_11672/memory.current
    # Example output:
    # 1591324672

`memory.current` shows the total amount of memory (in bytes) currently charged
to this cgroup.

    # Detailed statistics
    adb shell cat /sys/fs/cgroup/apps/uid_10274/pid_11672/memory.stat | head -n 10
    # Example output:
    # anon 1585098752
    # file 741376
    # kernel 5484544
    # kernel_stack 393216
    # pagetables 4583424
    # sec_pagetables 0
    # percpu 216
    # sock 0
    # vmalloc 4096
    # shmem 20480

`memory.stat` provides a breakdown: \* **`anon`** : Amount of anonymous memory
(heaps, stacks). \* **`file`** : Amount of file-backed memory (page cache). \*
**`swap`**: Amount of memory swapped out to ZRAM.

### 4. Observe changes

1. Open **MemoryLab**.
2. Note the value of `memory.current`.
3. Tap **Allocate Java Memory (10MB)** several times.
4. Read `memory.current` again. You should see it increase by approximately 10MB for each tap.
5. Tap **Allocate Bitmaps** . Check `memory.stat` to see `anon` increase.

## Proactive reclaim with `memory.reclaim`

A powerful feature of memcg (v2) is the `memory.reclaim` file. Writing a value
to this file instructs the kernel to immediately attempt to reclaim that amount
of memory from this **memcg and any memcgs under it**.

### How Android uses `memory.reclaim`

Android's **CachedAppOptimizer** uses this feature to maximally reclaim memory
from apps after they are **frozen** . The Android **App Freezer** ensures that
cached apps consume as little RAM as possible while they are not running. When
an app moves to the background and is frozen, the system writes the app's
current memory usage into its `memory.reclaim` file. This forces the kernel to
evict all possible file pages and swap all anonymous pages to ZRAM, minimizing
the app's resident footprint.

You can achieve the same "maximal reclaim" manually by reading `memory.current`
and writing it back into `memory.reclaim`:

    # Force reclaim of everything
    adb shell "cat /sys/fs/cgroup/apps/uid_10274/pid_11672/memory.current > /sys/fs/cgroup/apps/uid_10274/pid_11672/memory.reclaim"

### Exercise: force reclaim and trace

We will now force the kernel to reclaim memory from MemoryLab and capture the
activity in a Perfetto trace.

> [!NOTE]
> **Note:** Forcing memory reclaim requires your device be running a userdebug build with root access.

1. **Prepare**: Ensure MemoryLab has some allocations (Java and Bitmaps).
2. **Start Tracing**: Use this inline trace configuration to capture
   scheduling, reclaim, and page cache events.

   > [!NOTE]
   > **Note:** `vmscan` requires your device be running a userdebug build with root access.

       # Use a config that captures scheduling, reclaim and page cache events
       adb shell perfetto -c - --txt -o /data/misc/perfetto-traces/reclaim.perfetto-trace <<EOF
       buffers: {
           size_kb: 131072
           fill_policy: RING_BUFFER
       }
       data_sources: {
           config {
               name: "linux.ftrace"
               ftrace_config {
                   ftrace_events: "sched/sched_switch"
                   ftrace_events: "sched/sched_wakeup"
                   ftrace_events: "kmem/rss_stat"
                   ftrace_events: "mm_filemap_add_to_page_cache"
                   ftrace_events: "mm_filemap_delete_from_page_cache"
                   ftrace_events: "vmscan/mm_vmscan_direct_reclaim_begin"
                   ftrace_events: "vmscan/mm_vmscan_direct_reclaim_end"
                   ftrace_events: "vmscan/mm_vmscan_memcg_reclaim_begin"
                   ftrace_events: "vmscan/mm_vmscan_memcg_reclaim_end"
                   symbolize_ksyms: true
               }
           }
       }
       data_sources: {
           config {
               name: "linux.process_stats"
               process_stats_config {
                   scan_all_processes_on_start: true
               }
           }
       }
       EOF

3. **Trigger Pressure and Reclaim**:

   - In MemoryLab, tap **Allocate Native Memory (1GB)**. This will trigger system-wide pressure.
   - In a separate terminal, reclaim 200MB:

         adb shell "echo 200M > /sys/fs/cgroup/apps/uid_10274/pid_11672/memory.reclaim"

4. **Fault Back In** : Switch back to **MemoryLab** . Tap **Thrash Pagecache
   (Refault test)**.

5. **Stop Trace**: Press Ctrl+C in the trace terminal.

### Analyzing reclaim in Perfetto

When you open the trace, you can see both system-wide and per-app reclaim in
action:

![Perfetto showing direct and memcg reclaim](https://developer.android.com/static/topic/performance/memory/guide/images/reclaim/perfetto_reclaim_activity.png)

Look for the following in the trace:

- **kswapd** : Search for `kswapd0` under **Kernel threads** (in the screenshot above it was manually pinned at the top). You'll see it waking up and running (green slices) as the system struggles to find free pages.
- **Direct Reclaim** : Look at the `com.android.memorylab` process threads. You'll see purple ftrace event slices (like `mm_vmscan_direct_reclaim_begin`) appearing directly under the thread's scheduling track. This indicates the app thread itself is stalled waiting for the kernel to free up pages.
- **RSS and Swap Counters** :
  - `mem.rss.anon`: Increases as you tap the allocation buttons.
  - `mem.swap`: Increases steadily as `kswapd` and the app's own threads (subject to direct reclaim) compress those anonymous pages into ZRAM.
- **memcg Reclaim** : If you zoom in on the moment you triggered the manual reclaim, you'll see a sharp drop in both `rss.anon` and `rss.file`, accompanied by `mm_vmscan_memcg_reclaim` events.

*** ** * ** ***

**[← System-wide](https://developer.android.com/topic/performance/memory/guide/system-wide-memory) \| [↑ Up](https://developer.android.com/topic/performance/memory/guide) \|
[kswapd and lmkd interaction →](https://developer.android.com/topic/performance/memory/guide/kswapd-lmkd-interaction)**