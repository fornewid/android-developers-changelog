---
title: https://developer.android.com/games/optimize/memory-allocation
url: https://developer.android.com/games/optimize/memory-allocation
source: md.txt
---

# Manage memory effectively in games

On the Android platform, the system tries to use as much system memory (RAM) as possible and performs various memory optimizations to free up space when needed. These optimizations can have a negative effect on your game, either by slowing it down or killing it altogether. You can learn more about these optimizations in the topic[Memory allocation among processes](https://developer.android.com/topic/performance/memory-management).

This page explains the steps you can take to avoid low memory conditions affecting your game.

## Respond to onTrimMemory()

The system uses[`onTrimMemory()`](https://developer.android.com/reference/android/content/ComponentCallbacks2#onTrimMemory(int))to notify your app of lifecycle events that present a good opportunity for your app to voluntarily reduce its memory usage and avoid being killed by the[low-memory killer (LMK)](https://developer.android.com/topic/performance/memory-management#low-memory_killer)to release memory for other apps to use.

If your app is killed in the background, then the next time the user launches your app they will experience a slow[cold start](https://developer.android.com/topic/performance/vitals/launch-time#cold). Apps that reduce their memory usage when going to the background are less likely to be killed in the background.

When responding to trim events, it's best to release large memory allocations that are not immediately needed and could be reconstructed on demand. For example, if your app has a cache of bitmaps that were decoded from locally stored compressed images, then it's often a good idea to trim or purge this cache in response to[`TRIM_MEMORY_UI_HIDDEN`](https://developer.android.com/reference/android/content/ComponentCallbacks2#TRIM_MEMORY_UI_HIDDEN).  

### Kotlin

```kotlin
class MainActivity : AppCompatActivity(), ComponentCallbacks2 {
    override fun onTrimMemory(level: Int) {
        if (level >= ComponentCallbacks2.TRIM_MEMORY_UI_HIDDEN) {
            // Release memory related to UI elements, such as bitmap caches.
        }
        if (level >= ComponentCallbacks2.TRIM_MEMORY_BACKGROUND) {
            // Release memory related to background processing, such as by
            // closing a database connection.
        }
    }
}
```

### Java

```java
public class MainActivity extends AppCompatActivity implements ComponentCallbacks2 {
    public void onTrimMemory(int level) {
        switch (level) {
            if (level >= ComponentCallbacks2.TRIM_MEMORY_UI_HIDDEN) {
                // Release memory related to UI elements, such as bitmap caches.
            }
            if (level >= ComponentCallbacks2.TRIM_MEMORY_BACKGROUND) {
                // Release memory related to background processing, such as by
                // closing a database connection.
            }
        }
    }
}
```

### C#

```c#
using UnityEngine;
using System.Collections;
using System.Collections.Generic;

class LowMemoryTrigger : MonoBehaviour
{
    private void Start()
    {
        Application.lowMemory += OnLowMemory;
    }
    private void OnLowMemory()
    {
        // Respond to low memory condition (e.g., Resources.UnloadUnusedAssets())
    }
}
```

## Be conservative with memory budgets

Budget memory conservatively to avoid running out of memory. Some items to consider include the following:

- **Size of physical RAM**: Games often use between ¼ and ½ of the physical RAM amount on the device.
- **Maximum zRAM size** : More zRAM means the game potentially has more memory to allocate. This amount can vary based on device; look for`SwapTotal`in`/proc/meminfo`to find this value.
- **Memory usage of the OS**: Devices that designate more RAM to system processes leave less memory for your game. The system kills your game's process before it kills system processes.
- **Memory usage of installed apps**: Test your game on devices that have many apps installed. Social media and chat apps need to run constantly and affect the amount of free memory.

If you can't commit to a conservative memory budget, take a more flexible approach. If the system runs into low memory issues, reduce the amount of memory that the game is using. For example, allocate lower-resolution textures or store fewer shaders in response to`onTrimMemory()`. This dynamic approach to memory allocation requires more work from the developer, especially in the game design phase.

## Avoid thrashing

*Thrashing* occurs when free memory is low, but not low enough to kill the game. In this situation,`kswapd`has reclaimed pages that the game still needs, so it tries to reload the pages from memory. There isn't enough space, so the pages keep getting swapped out (continuous swapping).[System tracing](https://developer.android.com/topic/performance/tracing)reports this situation as a thread where`kswapd`runs continuously.

One symptom of thrashing is long frame times - possibly a second or more. Reduce the memory footprint of the game to resolve this situation.

## Use available tools

Android has a collection of tools to assist in understanding how the system manages memory.

### Meminfo

This tool collects memory statistics to show how much[PSS memory](https://developer.android.com/topic/performance/memory-management#calculating_memory_footprint)was allocated and the categories for which it was used.

Print the[meminfo](https://developer.android.com/studio/command-line/dumpsys#meminfo)statistics in one of the following ways:

- Use the command`adb shell dumpsys meminfo
  `<var translate="no">package-name</var>.
- Use the[`MemoryInfo`](https://developer.android.com/reference/android/os/Debug.MemoryInfo)call from the Android Debug API.

The[`PrivateDirty`](https://developer.android.com/studio/command-line/dumpsys#meminfo)statistic shows the amount of RAM inside the process that can not be paged to disk and is not shared with any other processes. The bulk of this amount becomes available to the system when that process is killed.

### Memory tracepoints

Memory tracepoints track the amount of[RSS memory](https://developer.android.com/topic/performance/memory-management#calculating_memory_footprint)your game is using. Calculating RSS memory usage is much faster than calculating PSS usage. Because it's faster to calculate, RSS shows finer granularity on changes in the memory size for more accurate measurements of peak memory usage. Therefore, it's easier to notice peaks that could cause the game to run out of memory.

#### Perfetto and long traces

[Perfetto](https://docs.perfetto.dev)is a suite of tools for collecting performance and memory information on a device and displaying in a web-based UI. It supports arbitrarily long traces so you can view how RSS changes over time. You can also issue SQL queries on the data it produces for offline processing. Enable long traces from the[System Tracing app](https://developer.android.com/topic/performance/tracing/on-device). Make sure the**memory:Memory**category is enabled for the trace.

### heapprofd

[`heapprofd`](https://docs.perfetto.dev/#/heapprofd)is a memory tracking tool that's part of Perfetto. This tool can help you find memory leaks by showing where memory was allocated using`malloc`.`heapprofd`can be started using a Python script, and because the tool has low overhead, it doesn't affect performance like other tools such as Malloc Debug.
| **Note:** Since game engines use`mmap`with the`MAP_ANONYMOUS`flag to create memory pools, most allocations are not tracked. If you have access to the game engine source code, replace the memory pool`mmap`calls with`malloc`. Some game engines have an option to use`malloc`instead of`mmap`.

### bugreport

`bugreport`is a logging tool for finding out whether or not your game crashed because it ran out of memory. The tool's output is much more detailed than using logcat. It's useful for memory debugging because it shows if your game crashed because it ran out of memory or if it was killed by the LMK.

For more information, see[Capture and read bug reports](https://developer.android.com/studio/debug/bug-report).