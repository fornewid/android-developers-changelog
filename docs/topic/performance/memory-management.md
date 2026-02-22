---
title: https://developer.android.com/topic/performance/memory-management
url: https://developer.android.com/topic/performance/memory-management
source: md.txt
---

# Memory allocation among processes

The Android platform runs on the premise that free memory is wasted memory. It tries to use all of the available memory at all times. For example, the system keeps apps in memory after they've been closed so the user can quickly switch back to them. For this reason, Android devices often run with very little free memory. Memory management is vital to properly allocate memory among important system processes and many user applications.

This page discusses the basics of how Android allocates memory for the system and for user applications. It also explains how the operating system reacts to low memory situations.

## Types of memory

Android devices contain three different types of memory: RAM, zRAM, and storage. Note that both the CPU and GPU access the same RAM.

![Types of memory](https://developer.android.com/static/images/games/memory-types.svg)

**Figure 1.**Types of memory - RAM, zRAM, and storage

- RAM is the fastest type of memory, but is usually limited in size. High-end devices typically have the largest amounts of RAM.

- zRAM is a partition of RAM used for swap space. Everything is compressed when placed into zRAM, and then decompressed when copied out of zRAM. This portion of RAM grows or shrinks in size as pages are moved into or taken out of zRAM. Device manufacturers can set the maximum size.

- Storage contains all of the persistent data such as the file system and the included object code for all apps, libraries, and the platform. Storage has much more capacity than the other two types of memory. On Android, storage isn't used for swap space like it is on other Linux implementations since frequent writing can cause wear on this memory, and shorten the life of the storage medium.

## Memory pages

RAM is broken up into*pages*. Typically each page is 4KB of memory.

Pages are considered either*free* or*used*. Free pages are unused RAM. Used pages are RAM that the system is actively using, and are grouped into the following categories:

- Cached: Memory backed by a file on storage (for example, code or memory-mapped files). There are two types of cached memory:
  - Private: Owned by one process and not shared
    - Clean: Unmodified copy of a file on storage, can be deleted by[`kswapd`](https://developer.android.com/topic/performance/memory-management#kswapd)to increase free memory
    - Dirty: Modified copy of the file on storage; can be moved to, or compressed in, zRAM by`kswapd`to increase free memory
  - Shared: Used by multiple processes
    - Clean: Unmodified copy of the file on storage, can be deleted by`kswapd`to increase free memory
    - Dirty: Modified copy of the file on storage; allows changes to be written back to the file in storage to increase free memory by`kswapd`, or explicitly using[`msync()`](https://developer.android.com/reference/android/system/Os#msync(long,%2520long,%2520int))or[`munmap()`](https://developer.android.com/reference/android/system/Os#munmap(long,%2520long))
- Anonymous: Memory**not** backed by a file on storage (for example, allocated by[`mmap()`](https://developer.android.com/reference/android/system/Os#mmap(long,%2520long,%2520int,%2520int,%2520java.io.FileDescriptor,%2520long))with the`MAP_ANONYMOUS`flag set)
  - Dirty: Can be moved/compressed in zRAM by`kswapd`to increase free memory

| **Note:** Clean pages contain an exact copy of a file (or portion of a file) that exists in storage. A clean page becomes a dirty page when it no longer contains an exact copy of the file (for example, from the result of an application operation). Clean pages can be deleted because they can always be regenerated using the data from storage; dirty pages cannot be deleted or else data would be lost.

The proportions of free and used pages vary over time as the system actively manages RAM. The concepts introduced in this section are key to managing low-memory situations. The next section of this document explains them in greater detail.

## Low memory management

Android has two main mechanisms to deal with low memory situations: the kernel swap daemon and low-memory killer.

### kernel swap daemon

The kernel swap daemon (`kswapd`) is part of the Linux kernel, and converts used memory into free memory. The daemon becomes active when free memory on the device runs low. The Linux kernel maintains low and high free memory thresholds. When free memory falls below the low threshold,`kswapd`starts to reclaim memory. Once the free memory reaches the high threshold,`kswapd`stops reclaiming memory.

`kswapd`can reclaim clean pages by deleting them because they're backed by storage and have not been modified. If a process tries to address a clean page that has been deleted, the system copies the page from storage to RAM. This operation is known as*demand paging*.

![Clean page backed by storage deleted](https://developer.android.com/static/images/games/delete-clean-page.svg)

**Figure 2.**Clean page, backed by storage, deleted

`kswapd`can move cached private dirty pages and anonymous dirty pages to zRAM, where they are compressed. Doing so frees up available memory in RAM (free pages). If a process tries to touch a dirty page in zRAM, the page is uncompressed and moved back into RAM. If the process associated with a compressed page is killed, then the page is deleted from zRAM.

If the amount of free memory falls below a certain threshold, the system starts killing processes.

![Dirty page moved to zRAM and compressed](https://developer.android.com/static/images/games/compressed-dirty-page.svg)

**Figure 3.**Dirty page moved to zRAM and compressed

### Low-memory killer

Many times,`kswapd`cannot free enough memory for the system. In this case, the system uses[`onTrimMemory()`](https://developer.android.com/reference/android/content/ComponentCallbacks2#onTrimMemory(int))to notify an app that memory is running low and that it should reduce its allocations. If this is not sufficient, the kernel starts killing processes to free up memory. It uses the low-memory killer (LMK) to do this.

To decide which process to kill, LMK uses an "out of memory" score called[`oom_adj_score`](https://android.googlesource.com/platform/system/memory/lmkd/+/master/README.md)to prioritize the running processes. Processes with a high score are killed first. Background apps are first to be killed, and system processes are last to be killed. The following table lists the LMK scoring categories from high-to-low. Items in the highest-scoring category, in row one, will be killed first:

![Android processes, high scores at the top](https://developer.android.com/static/images/games/lmk-process-order.svg)

**Figure 4.**Android processes, with high scores at the top and low scores at the bottom

These are descriptions for the various categories in the table above:

- Background apps: Apps that were run previously and are not currently active. LMK will first kill background apps starting with the one with the highest`oom_adj_score`.

- Previous app: The most recently-used background app. The previous app has higher priority (a lower score) than the background apps because it is more likely the user will switch to it than one of the background apps.

- Home app: This is the launcher app. Killing this will make the wallpaper disappear.

- Services: Services are started by applications and may include syncing or uploading to the cloud.

- Perceptible apps: Non-foreground apps that are perceptible to the user in some way, such as running a search process that displays a small UI or listening to music.

- Foreground app: The app currently being used. Killing the foreground app looks like an application crash which might indicate to the user that something is going wrong with the device.

- Persistent (services): These are core services for the device, such as telephony and wifi.

- System: System processes. As these processes are killed, the phone may appear to reboot.

- Native: Very low-level processes used by the system (for example,`kswapd`).

Device manufacturers can change the behavior of LMK.

## Calculating memory footprint

The kernel tracks all memory pages in the system.

![Pages used by different processes](https://developer.android.com/static/images/games/pages-processes.svg)

**Figure 5.**Pages used by different processes

When determining how much memory is being used by an app, the system must account for shared pages. Apps that access the same service or library will be sharing memory pages. For example, Google Play Services and a game app may be sharing a location service. This makes it difficult to determine how much memory belongs to the service at large versus each application.

![Pages shared by two apps](https://developer.android.com/static/images/games/pages-shared-apps.svg)

**Figure 6.**Pages shared by two apps (middle)

To determine the memory footprint for an application, any of the following metrics may be used:

- Resident Set Size (RSS): The number of shared and non-shared pages used by the app
- Proportional Set Size (PSS): The number of non-shared pages used by the app and an even distribution of the shared pages (for example, if three processes are sharing 3MB, each process gets 1MB in PSS)
- Unique Set Size (USS): The number of non-shared pages used by the app (shared pages are not included)

PSS is useful for the operating system when it wants to know how much memory is used by all processes since pages don't get counted multiple times. PSS takes a long time to calculate because the system needs to determine which pages are shared and by how many processes. RSS doesn't distinguish between shared and non-shared pages (making it faster to calculate) and is better for tracking changes in memory allocation.

## Additional resources

- [Overview of memory management](https://developer.android.com/topic/performance/memory-overview)
- [Processes and Application Lifecycle](https://developer.android.com/guide/components/activities/process-lifecycle)
- [Understanding Android memory usage - Google I/O presentation](https://www.youtube.com/watch?v=w7K0jio8afM)
- [Android Memory and Games - Google I/O presentation](https://www.youtube.com/watch?v=Do7oYWwOXTk&t=314s)
- [Android low memory killer daemon](https://source.android.com/docs/core/perf/lmkd)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [App startup time](https://developer.android.com/topic/performance/vitals/launch-time)