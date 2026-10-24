---
title: https://developer.android.com/topic/performance/memory/guide/page-advice
url: https://developer.android.com/topic/performance/memory/guide/page-advice
source: md.txt
---

Freeing an object in your app's code or closing a temporary stream doesn't
always return physical RAM to the operating system. Custom native allocators,
garbage-collected runtimes, and open-addressed hash tables frequently retain
virtual memory arenas that stay backed by physical pages long after the logical
data inside them is gone. Similarly, reading or memory-mapping large asset
archives populates the kernel page cache, which remains charged to your app's
[memory control group (memcg)](https://developer.android.com/topic/performance/memory/guide/reclaim#memory-control-groups-memcg).

This page explains how to use the `madvise` and `posix_fadvise` system calls to
return unused anonymous and file-backed pages to the OS while keeping virtual
address reservations and file descriptors intact, and how to verify the impact
in `adb shell` and Perfetto.

## Why logical deallocation retains physical RAM

The Linux kernel tracks physical memory at the granularity of hardware pages,
which are 4 KB or [16 KB](https://developer.android.com/guide/practices/page-sizes) on Android devices. When a
process reserves a region of virtual address space with `mmap`, the kernel
creates a virtual memory area (VMA) without allocating physical RAM. The kernel
allocates and charges a physical page only when the process first touches that
page. For anonymous memory, a first read maps a shared zero page, so only a
write allocates RAM.

Once a page is faulted into RAM, the kernel doesn't know whether the bytes
inside that page still represent live objects in your app's runtime. Two common
patterns keep physical pages resident after your app finishes using them:

- **Anonymous arenas and pools** : Custom native allocators (such as slab, pool, or frame-arena allocators), managed runtimes with non-moving heap spaces, and large hash tables reserve contiguous virtual address ranges with `mmap` using `MAP_PRIVATE | MAP_ANONYMOUS`. When your app resets an arena, frees a block back to a custom pool, or clears a hash table by zeroing its metadata, the underlying pages remain dirty. Without an explicit hint to the kernel, those pages continue to count toward your process's anonymous [resident set size (RSS) and proportional set size (PSS)](https://developer.android.com/topic/performance/memory/guide/concepts#rss-pss-uss) and its `memory.current` cgroup charge. Under memory pressure, the kernel compresses them into ZRAM, where they still occupy swap space charged to `memory.swap.current`.
- **File-backed page cache from asset streaming** : When your app reads large asset bundles, level archives, media containers, or machine learning models using `read`, `pread`, or file-backed `mmap`, the kernel caches every read page in the page cache and charges those pages to the `file` counter in the `memory.stat` file of your process's cgroup. If your app decompresses or copies that asset into an anonymous runtime buffer or uploads it to the GPU, keeping the raw file pages in the page cache duplicates the asset in RAM.

![Dirty arena pages released with madvise and cached asset pages
evicted with posix_fadvise, while the virtual range and the file
descriptor stay intact.](https://developer.android.com/static/topic/performance/memory/guide/images/page-advice/flow.png) **Figure 1.** Reclaiming physical pages from virtual arenas and the page cache.

## Release anonymous pages

The `madvise` system call gives the kernel advice about how your process expects
to use a virtual address range. For private anonymous mappings (`MAP_PRIVATE |
MAP_ANONYMOUS`), passing `MADV_DONTNEED` instructs the kernel to immediately
discard the physical pages and any swapped ZRAM entries backing the specified
page-aligned range.

After `madvise` with `MADV_DONTNEED` returns:

- The virtual address range remains reserved and valid in your process's address space (`VmSize` doesn't change), so pointers and arena bounds stay intact without calling `munmap` or `mmap`.
- The physical pages are immediately unmapped and freed, reducing `RssAnon`, `Pss`, the `anon` counter in `memory.stat`, and `memory.swap.current` for any pages that were in ZRAM.
- Any subsequent read or write to an address in that range faults in a fresh zero-filled page on demand.

| Advice flag | Target mapping | Kernel behavior on Android |
|---|---|---|
| `MADV_DONTNEED` | Private anonymous (`MAP_PRIVATE | MAP_ANONYMOUS`) | Immediately discards physical pages and ZRAM swap slots. Subsequent accesses fault in zero-filled pages. Deterministic drop in `RssAnon` and `memory.current`. |
| `MADV_DONTNEED` | File-backed (`MAP_PRIVATE` or `MAP_SHARED`) | Unmaps pages from the process page tables (`RssFile` drops). Private copy-on-write pages in a `MAP_PRIVATE` mapping are discarded, so modifications are lost and the next access rereads the file. Dirty `MAP_SHARED` pages are written back to storage later. Clean pages stay in the page cache until they're evicted. |
| `MADV_FREE` | Private anonymous (`MAP_PRIVATE | MAP_ANONYMOUS`) | Marks pages as lazily reusable. The kernel retains the pages in `RssAnon` if no memory pressure exists and reclaims them only when global or memcg reclaim runs. |
| `MADV_WILLNEED` | File-backed or swapped anonymous | Starts asynchronous readahead for file-backed mappings, or reads swapped anonymous pages back from ZRAM into the swap cache ahead of time. |

> [!NOTE]
> **Note:** When releasing memory in response to lifecycle transitions such as `onStop` or [`TRIM_MEMORY_UI_HIDDEN`](https://developer.android.com/topic/performance/memory/manage-app-memory#release), prefer `MADV_DONTNEED` over `MADV_FREE` so that your process's `RssAnon` and `memory.current` drop immediately rather than waiting for page reclaim.

### Align interior ranges to the runtime page size

`madvise` operates on whole pages. It requires a page-aligned start address and
rounds the length up to the next page boundary. If you release a span inside a
shared arena where neighboring bytes still hold live objects, rounding the range
outward can zero out live allocations that share the boundary pages.

Always query the runtime page size with `sysconf(_SC_PAGESIZE)` to support both
4 KB and 16 KB page devices, and round the interior start address
up to the next page boundary and the interior end address down to the
previous page boundary. For more guidance on page-size-agnostic allocators, see
[Optimize custom memory allocators](https://developer.android.com/guide/practices/page-sizes#custom-allocators).

    #include <sys/mman.h>
    #include <unistd.h>
    #include <cstdint>

    // Reclaims physical pages strictly inside [region_start, region_start + length)
    // without disturbing live objects on partially occupied boundary pages.
    void ReleaseUnusedArenaSpan(void* region_start, size_t length) {
      const uintptr_t page_size = static_cast<uintptr_t>(sysconf(_SC_PAGESIZE));
      const uintptr_t page_mask = ~(page_size - 1);

      const uintptr_t raw_start = reinterpret_cast<uintptr_t>(region_start);
      const uintptr_t raw_end = raw_start + length;

      // Round start UP and end DOWN so only fully unused pages are discarded.
      const uintptr_t aligned_start = (raw_start + page_size - 1) & page_mask;
      const uintptr_t aligned_end = raw_end & page_mask;

      if (aligned_end > aligned_start) {
        madvise(reinterpret_cast<void*>(aligned_start),
                aligned_end - aligned_start,
                MADV_DONTNEED);
      }
    }

When creating custom anonymous mappings with `mmap`, label the VMA with `prctl`
using `PR_SET_VMA_ANON_NAME` so that you can track its residency by name in
[`showmap`](https://developer.android.com/topic/performance/memory/guide/tools-overview#showmap) and `/proc/<pid>/smaps`. [`dumpsys
meminfo`](https://developer.android.com/topic/performance/memory/guide/tools-overview#dumpsys-meminfo) counts custom-named anonymous regions under `Unknown`.
Some older kernels keep a pointer to the name instead of copying it, so pass a
string that stays valid for the lifetime of the mapping, such as a string
literal:

    #include <sys/mman.h>
    #include <sys/prctl.h>

    #ifndef PR_SET_VMA
    #define PR_SET_VMA 0x53564d41
    #define PR_SET_VMA_ANON_NAME 0
    #endif

    void* ReserveNamedArena(size_t capacity_bytes, const char* arena_name) {
      void* ptr = mmap(nullptr, capacity_bytes, PROT_READ | PROT_WRITE,
                       MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
      if (ptr != MAP_FAILED) {
        prctl(PR_SET_VMA, PR_SET_VMA_ANON_NAME,
              reinterpret_cast<unsigned long>(ptr), capacity_bytes,
              reinterpret_cast<unsigned long>(arena_name));
      }
      return ptr;
    }

## Evict file cache pages

When your app reads data from a file descriptor, the kernel caches the file's
pages in the page cache in anticipation of future reads. While this speeds up
repeated accesses to small configuration files or shared libraries, it works
against you when streaming large asset archives, texture packages, or audio and
video chunks that are parsed once and stored in decoded form elsewhere.

The `posix_fadvise` system call lets your app inform the kernel about its
expected file access pattern on an open file descriptor:

- `POSIX_FADV_DONTNEED`: Instructs the kernel that the specified byte range won't be accessed in the near future. The kernel immediately evicts clean, unmapped cached pages in that page-aligned range from the page cache, reducing the `file` counter in `memory.stat` and the `memory.current` charge of your cgroup.
- `POSIX_FADV_SEQUENTIAL`: Doubles the kernel's readahead window for the file descriptor, improving throughput when streaming a large archive from start to finish. Pair this with `POSIX_FADV_DONTNEED` on trailing chunks as you consume them so the page cache footprint stays bounded to a small sliding window.
- `POSIX_FADV_RANDOM`: Disables speculative kernel readahead on the file descriptor. Use this when performing sparse, non-contiguous lookups by byte offset into a large archive or database file so that each small read doesn't pull adjacent unused pages into the page cache. For memory-mapped files, call `madvise` with `MADV_RANDOM` on the mapping instead.

The following example streams a large asset archive in chunks, enabling
sequential readahead upfront and evicting each processed page-aligned span from
the page cache:

    #include <fcntl.h>
    #include <unistd.h>
    #include <cstdint>
    #include <vector>

    void StreamAssetArchive(int fd, size_t total_size) {
      const size_t page_size = static_cast<size_t>(sysconf(_SC_PAGESIZE));
      constexpr size_t kChunkSize = 4 * 1024 * 1024;  // 4 MB streaming window
      std::vector<uint8_t> buffer(kChunkSize);

      // Hint sequential access so the kernel prefetches upcoming chunks.
      posix_fadvise(fd, 0, total_size, POSIX_FADV_SEQUENTIAL);

      off_t offset = 0;
      while (offset < static_cast<off_t>(total_size)) {
        ssize_t bytes_read = pread(fd, buffer.data(), buffer.size(), offset);
        if (bytes_read <= 0) break;

        // Decode or upload buffer[0 .. bytes_read) into runtime structures here.

        // Evict full pages that have been completely consumed.
        const size_t aligned_len =
            (static_cast<size_t>(bytes_read) / page_size) * page_size;
        if (aligned_len > 0) {
          posix_fadvise(fd, offset, static_cast<off_t>(aligned_len),
                        POSIX_FADV_DONTNEED);
        }
        offset += bytes_read;
      }
    }

### Reclaim file-backed mmap regions

If your app memory-maps a large asset file with `mmap` instead of reading it
with `pread`, calling `posix_fadvise` with `POSIX_FADV_DONTNEED` alone doesn't
evict pages that are still mapped into your process's page tables. To drop a
consumed span of a read-only file mapping without unmapping the entire VMA:

1. Call `madvise(addr, length, MADV_DONTNEED)` on the mapped virtual address range to unmap those pages from your process's page tables (`RssFile` drops).
2. Call `posix_fadvise(fd, offset, length, POSIX_FADV_DONTNEED)` on the corresponding file offset so the kernel also evicts the unmapped clean pages from the page cache (`file` in `memory.stat` drops).

## Follow page advice guidelines

Apply these practices when integrating `madvise` and `posix_fadvise` into
allocators, asset loaders, and lifecycle handlers:

- **Batch calls into coarse regions** : Each `madvise` call takes your process's memory map lock (`mmap_lock`), walks page tables, and invalidates the matching translation lookaside buffer (TLB) entries on other CPU cores (with broadcast TLB maintenance instructions on Arm and inter-processor interrupts on x86). Don't call `madvise` on every small deallocation. Coalesce free spans and advise the kernel in chunks of 64 KB to 1 MB or larger, or sweep free spans during frame boundaries and background transitions (`onStop` and `TRIM_MEMORY_UI_HIDDEN`).
- **Reclaim empty capacity in hash tables and pools** : When a large hash table, object pool, or staging buffer is cleared after a scene transition or data sync, either shrink its backing allocation or issue `MADV_DONTNEED` across the cleared backing array. Keeping a 32 MB open-addressed table allocated with tombstones keeps all 32 MB of physical pages charged to your process.
- **Flush dirty file data before evicting it** : `POSIX_FADV_DONTNEED` only evicts clean page cache pages. If your app writes a large temporary or cache file that it won't read back immediately, call `fdatasync` before `posix_fadvise(fd, 0, 0, POSIX_FADV_DONTNEED)` so the dirty pages are written to storage and then dropped from RAM.
- **Don't evict hot shared code or assets** : Avoid calling `POSIX_FADV_DONTNEED` on DEX, ODEX, VDEX, shared libraries (`.so`), or UI assets that are accessed repeatedly. Evicting active code or asset pages forces synchronous storage refaults that stall threads and raise I/O pressure, as reported by [pressure stall information (PSI)](https://developer.android.com/topic/performance/memory/guide/kswapd-lmkd-interaction#what-is-psi).

## Verify page reclamation in the shell

Verify that `madvise` and `posix_fadvise` reclaim physical RAM using `showmap`
and your app's cgroup v2 accounting files.

> [!NOTE]
> **Note:** To run `showmap` on your app, make it [profileable or debuggable](https://developer.android.com/topic/performance/memory/guide/tools-overview#showmap). Reading cgroup files and running `find` across `/data` require `adb root` on a userdebug build or an emulator.

### Inspect virtual versus physical size with showmap

When you name an anonymous arena with `PR_SET_VMA_ANON_NAME`, `showmap` displays
both its virtual reservation (`virtual size`) and its resident physical pages
(`RSS` and `PSS`). The following sample output comes from the MemoryLab sample
app in AOSP, which names its arena `memorylab-arena`. Replace `com.example.app`
and `memorylab-arena` with your package name and arena name. Before calling
`madvise` with `MADV_DONTNEED` on a touched 64 MB arena, run:

    adb shell "showmap \$(pidof com.example.app) | grep -E '^ +virtual|^ +size|memorylab-arena' | head -3"

     virtual                     shared   shared  private  private                   Anon      Shmem     File      Shared   Private
        size      RSS      PSS    clean    dirty    clean    dirty     swap  swapPSS HugePages PmdMapped PmdMapped Hugetlb  Hugetlb    Locked    # object
       65536    65536    65536        0        0        0    65536        0        0         0         0         0        0        0        0    1 [anon:memorylab-arena]

After calling `madvise(arena_ptr, 64 * 1024 * 1024, MADV_DONTNEED)`, run
`showmap` again:

     virtual                     shared   shared  private  private                   Anon      Shmem     File      Shared   Private
        size      RSS      PSS    clean    dirty    clean    dirty     swap  swapPSS HugePages PmdMapped PmdMapped Hugetlb  Hugetlb    Locked    # object
       65536        0        0        0        0        0        0        0        0         0         0         0        0        0        0    1 [anon:memorylab-arena]

The `virtual size` stays at 65536 KB (64 MB), confirming that the
virtual address range is still reserved, while `RSS`, `PSS`, and `private dirty`
drop to 0 KB.

### Inspect cgroup memory.current and memory.stat

To verify both anonymous page reclamation and unmapped page cache eviction
(which doesn't appear in process page tables if read with `pread`), inspect the
process's cgroup v2 directory. On Android, each app process has its own cgroup
(such as `/sys/fs/cgroup/apps/uid_<UID>/pid_<PID>/`, depending on the device).
The following command finds the directory from the `0::` line of
`/proc/<PID>/cgroup` and prints the counters:

    adb shell '
      PID=$(pidof com.example.app)
      CG=/sys/fs/cgroup$(sed -n "s/^0:://p" /proc/$PID/cgroup)
      echo "memory.current: $(cat $CG/memory.current)"
      echo "memory.swap.current: $(cat $CG/memory.swap.current)"
      grep -E "^(anon|file) " $CG/memory.stat
    '

Before releasing a 64 MB anonymous arena and evicting a 128 MB
memory-mapped asset file from the page cache:

    memory.current: 242962432
    memory.swap.current: 16633856
    anon 100671488
    file 140009472

Immediately after calling `madvise` with `MADV_DONTNEED` on the arena and on
the asset file mapping, and then `posix_fadvise` with `POSIX_FADV_DONTNEED` on
the asset file descriptor:

    memory.current: 41766912
    memory.swap.current: 16502784
    anon 33722368
    file 5914624

`anon` drops by 64 MB and `file` drops by 128 MB, reducing
`memory.current` by about 192 MB without closing the file descriptor or
unmapping the arena's virtual address space. `memory.swap.current` barely
changes, because almost none of the arena pages had been swapped to ZRAM. Your
values depend on the device and on how much of the file the kernel already
evicted on its own. For more about how the kernel charges and reclaims
memory per cgroup, see [Memory reclaim: eviction and swap](https://developer.android.com/topic/performance/memory/guide/reclaim).

## Analyze page reclamation in Perfetto

Perfetto lets you correlate `madvise` and `posix_fadvise` calls with kernel
page-table and page-cache counters on a unified timeline.

### Record a trace

Capture a trace with `linux.process_stats` for periodic process counters and
`linux.ftrace` for real-time RSS and page-cache events, and then pull it to
your computer:

    adb shell perfetto -c - --txt -o /data/misc/perfetto-traces/page_advice.perfetto-trace <<EOF
    buffers: {
        size_kb: 65536
        fill_policy: RING_BUFFER
    }
    data_sources: {
        config {
            name: "linux.process_stats"
            process_stats_config {
                scan_all_processes_on_start: true
                proc_stats_poll_ms: 100
            }
        }
    }
    data_sources: {
        config {
            name: "linux.ftrace"
            ftrace_config {
                ftrace_events: "kmem/rss_stat"
                ftrace_events: "filemap/mm_filemap_add_to_page_cache"
                ftrace_events: "filemap/mm_filemap_delete_from_page_cache"
            }
        }
    }
    duration_ms: 20000
    EOF
    adb pull /data/misc/perfetto-traces/page_advice.perfetto-trace

### Inspect tracks in the Perfetto UI

Open the trace in the [Perfetto UI](https://ui.perfetto.dev), expand your app's process
group, and pin the following counter tracks so they stay at the top of the
timeline:

- `mem.virt`: Remains flat across `MADV_DONTNEED` calls, confirming that the virtual address reservation (`mmap`) is unchanged.
- `mem.rss.anon`: Steps down sharply at the exact timestamp where your app calls `madvise` with `MADV_DONTNEED` on dirty anonymous arenas or heap regions.
- `mem.rss.file`: Steps down when your app calls `madvise` with `MADV_DONTNEED` on a file-backed `mmap` region, accompanied by a burst of `mm_filemap_delete_from_page_cache` ftrace events when `posix_fadvise` with `POSIX_FADV_DONTNEED` evicts the clean pages from the page cache.
- `mem.swap`: Drops when `MADV_DONTNEED` discards anonymous pages that had previously been compressed into ZRAM.

![Perfetto counter tracks for one process. mem.rss.anon and
mem.rss.file step up when an arena and an asset file are populated and
step back down after madvise and posix_fadvise, while mem.swap and
mem.virt stay flat.](https://developer.android.com/static/topic/performance/memory/guide/images/page-advice/perfetto-rss.png) **Figure 2.** RSS dropping after page advice calls.

Figure 2 shows these tracks for the MemoryLab sample app. To explore the same
view, open the [sample trace in the Perfetto UI](https://ui.perfetto.dev/#!/?s=972b9982e74cd3a61c07726863afa083d29dd054).

### Query peak and final memory with PerfettoSQL

Run the following PerfettoSQL query in the Perfetto UI (**Query (SQL)** tab) to
compare the peak and final values of `mem.virt`, `mem.rss.anon`,
`mem.rss.file`, and `mem.swap` for your target process:

    WITH counters AS (
      SELECT t.name AS counter_name, c.ts, c.value
      FROM counter c
      JOIN process_counter_track t ON c.track_id = t.id
      JOIN process p USING (upid)
      WHERE p.name = 'com.example.app'
        AND t.name IN ('mem.virt', 'mem.rss.anon', 'mem.rss.file', 'mem.swap')
    )
    SELECT
      counter_name,
      CAST(MAX(value) / 1048576 AS INT) AS peak_mb,
      CAST((
        SELECT value FROM counters AS last
        WHERE last.counter_name = counters.counter_name
        ORDER BY ts DESC LIMIT 1
      ) / 1048576 AS INT) AS final_mb
    FROM counters
    GROUP BY counter_name
    ORDER BY counter_name;

Sample output for the trace in Figure 2:

    counter_name  peak_mb  final_mb
    mem.rss.anon      111        48
    mem.rss.file      212        84
    mem.swap           36        36
    mem.virt        13952     13952

`mem.rss.anon` drops by 63 MB and `mem.rss.file` drops by 128 MB from
their peaks, while `mem.virt` ends at its peak because the virtual
reservations are unchanged.

### Resolve evicted pages to files

The `mm_filemap_add_to_page_cache` and `mm_filemap_delete_from_page_cache`
events identify files by inode number (`i_ino`) rather than by path. To confirm
that the evicted pages belong to the file you advised, count the evictions per
inode:

    SELECT
      EXTRACT_ARG(arg_set_id, 'i_ino') AS inode,
      COUNT(*) AS evicted_pages
    FROM ftrace_event
    WHERE name = 'mm_filemap_delete_from_page_cache'
    GROUP BY inode
    ORDER BY evicted_pages DESC
    LIMIT 5;

Sample output for the trace in Figure 2:

    inode     evicted_pages
    9761              35781
    76792192            767
    126                 668
    0                   612
    11587712            514

While the device that recorded the trace is still connected, resolve each inode
to a path. Inode numbers are unique only within one file system, so limit the
search to the file system that holds your app's data:

    INODE=<inode from the query>
    adb shell "find /data -xdev -inum $INODE 2>/dev/null"

Sample output for inode `9761`:

    /data/user/0/com.android.memorylab/files/asset_pack.bin
    /data/data/com.android.memorylab/files/asset_pack.bin

Both paths refer to the same file, because `/data/user/0` and `/data/data` are
two names for the same app data directory. The eviction count for the asset
file (35,781 pages) is larger than the file itself (32,768 pages at
4 KB), because `kswapd` had already evicted part of the file under memory
pressure before the app read it back and called `posix_fadvise`.

For a script that resolves many inodes at once, see
[Resolving faults to inodes, then to files](https://developer.android.com/topic/performance/memory/guide/system-wide-memory#resolve-faults-inodes).

*** ** * ** ***

**[← kswapd and lmkd interaction](https://developer.android.com/topic/performance/memory/guide/kswapd-lmkd-interaction) \| [↑ Up](https://developer.android.com/topic/performance/memory/guide) \|
[Lean background process →](https://developer.android.com/topic/performance/memory/guide/process-splitting)**