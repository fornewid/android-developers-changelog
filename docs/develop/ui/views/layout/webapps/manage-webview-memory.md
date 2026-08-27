---
title: https://developer.android.com/develop/ui/views/layout/webapps/manage-webview-memory
url: https://developer.android.com/develop/ui/views/layout/webapps/manage-webview-memory
source: md.txt
---

[`WebView`](https://developer.android.com/reference/android/webkit/WebView) runs native code across multiple processes to render web content
in your Android app. Leaving `WebView` instances unmanaged can lead to memory
leaks, out-of-memory (OOM) crashes, and degraded app performance.

This document explains the `WebView` multi-process memory model, describes how
to properly manage its lifecycle to prevent leaks, and provides practical
workflows for diagnosing memory issues.

## Understand WebView memory architecture

To effectively manage `WebView` memory, understand how Android allocates
resources for web content:

- **Multi-process execution:** On Android 8.0 (API level 26) and higher,
  `WebView` separates web content from your app's core functions across
  multiple processes (on low-RAM devices, it might fall back to a single
  process):

  - **Host (Browser) process:** The main app process where your `Activity` and Java or Kotlin code run.
  - **Isolated Renderer process:** A separate sandboxed process (`SandboxedProcessService`) that parses HTML and CSS, executes JavaScript, and renders web pages.
- **Native memory footprint:** Most `WebView` memory, including rendered
  graphics, the DOM tree, and JavaScript runtime memory, is allocated in
  native memory, not on the Java heap. A Java heap dump (`.hprof`) only shows
  a lightweight Java wrapper object and doesn't capture the true memory used
  by web content.

- **System impact of native memory:** Unlike Java heap allocations, which are
  capped by the app's `maxHeap` limit and fail fast with an
  `OutOfMemoryError`, native memory can silently grow to gigabytes. As
  unreleased native memory fills physical RAM and swap space (zRAM), Android's
  Low Memory Killer (LMK) begins terminating background processes to reclaim
  memory. This degrades overall device multitasking before eventually killing
  the foreground app.

## Manage the WebView lifecycle

Proper lifecycle management is critical for preventing memory leaks. A common
mistake is assuming that removing a `WebView` from your layout or letting an
`Activity` finish automatically frees its memory.

To ensure complete cleanup of both Java context references and native render
resources, you must explicitly orchestrate a teardown sequence in your host
component's lifecycle (such as `onDestroy()`), stopping active page execution,
detaching the view from its container, and releasing native bindings.

> [!CAUTION]
> **Caution:** `WebView` instances retain references to their host `Activity` context even after being removed from the view hierarchy. To prevent `Activity` memory leaks, you must explicitly remove the `WebView` from its parent container and invoke `destroy()`.

### Clean up WebView instances

To ensure a clean shutdown and release resources when your `Activity` or
`Fragment` is destroyed, do the following:

1. Remove the `WebView` from its parent container (`ViewGroup`).
2. Stop active loading and clear navigation history.
3. Call `destroy()`.
4. Clear the reference to `null`.

The following example demonstrates how to properly clean up a `WebView`:

### Kotlin

    override fun onDestroy() {
        myWebView?.let {
            // Remove the WebView from its parent ViewGroup.
            (it.parent as? ViewGroup)?.removeView(it)
            // Stop active loading and clear history.
            it.stopLoading()
            it.clearHistory()
            // Destroy the instance.
            it.destroy()
        }
        myWebView = null
        super.onDestroy()
    }

### Java

    @Override
    protected void onDestroy() {
        if (myWebView != null) {
            // Remove the WebView from its parent ViewGroup.
            if (myWebView.getParent() instanceof ViewGroup) {
                ((ViewGroup) myWebView.getParent()).removeView(myWebView);
            }
            // Stop active loading and clear history.
            myWebView.stopLoading();
            myWebView.clearHistory();
            // Destroy the instance.
            myWebView.destroy();
        }
        myWebView = null;
        super.onDestroy();
    }

### Understand post-destruction memory

When you call `destroy()`, the system releases the `Activity` context, cleans up
view hierarchies, and stops web background work. However, you might observe that
the process's physical memory (Resident Set Size) doesn't immediately drop to
its pre-WebView baseline.

This behavior is normal. Native runtime caches, shared libraries, and allocated
memory pages remain resident in the process until the operating system reclaims
them or the process terminates. The primary goal of `destroy()` is to prevent
cumulative `Activity` memory leaks when users navigate in and out of web-powered
screens.

## Key debugging metrics

When analyzing `WebView` memory consumption, focus on the following metrics:

- **Resident Set Size (RSS):** The total physical RAM mapped into the process,
  including shared code and libraries (labeled as **Total** in the Android
  Studio Profiler).

- **Anonymous RSS (RssAnon):** Memory allocated directly by the process that
  is not backed by a file on disk (such as native heap and JavaScript runtime
  allocations). This represents the primary memory cost of your web content
  (labeled as **Allocated** in the Android Studio Profiler).

- **Private Memory Footprint (PMF):** The sum of Anonymous RSS and swap
  (zRAM). PMF reflects the actual unevictable memory burden your app imposes
  on the system.

- **Browser PMF versus Renderer PMF:** Memory used by your app's main process
  versus memory used by the isolated renderer process. Heavy web content
  causes spikes primarily in the renderer process.

- **Live Object Counts (`WebViews`, `Activities`, `Views`):** The number of
  active UI, Context, and `WebView` instances held in memory. Tracking these
  identifies whether memory growth is caused by retained Java references or
  native-only allocations.

- **Private Other and Native Heap:** In `dumpsys meminfo`, native C/C++
  allocations and custom memory mappings (such as Chromium `PartitionAlloc` or
  embedded JavaScript runtime heaps) appear under Native Heap and Private
  Other rather than Java Heap.

For more information about process memory counters and their categories, see
the [Process memory glossary](https://developer.android.com/studio/profile/chart-glossary/process-memory).

## Practical diagnostic workflows

Because `WebView` operates across multiple processes and allocates native
memory, use the following tools and techniques to inspect its footprint:

### Profiling and diagnostic tools

To inspect memory allocations and diagnose leaks, use the following tools:

- **Android Studio Memory Profiler:** Use the [Memory Profiler](https://developer.android.com/studio/profile/memory-profiler) to
  visualize native allocations, track memory categories over time, and detect
  `Activity` leaks across screen transitions.

- **Memory tracking with Perfetto:** Use [Perfetto](https://perfetto.dev/docs/data-sources/memory-counters) to record system-level
  memory counters (such as RSS and Anonymous RSS) to observe overall memory
  growth. Note that `WebView` native engine allocations don't produce
  callstacks in Perfetto's [heap profiling tool](https://perfetto.dev/docs/case-studies/memory#heapprofd). Use
  [Chrome DevTools](https://developer.android.com/develop/ui/views/layout/webapps/debugging) to inspect JavaScript heap snapshots and DOM
  allocations inside the web content.

### Inspect live object counts

To determine whether memory growth is caused by retained Java framework
objects (such as UI components) or native allocations, inspect the `Objects`
section of [`dumpsys meminfo`](https://developer.android.com/tools/dumpsys):

    adb shell dumpsys meminfo -a <var>PACKAGE_NAME</var> | grep -A 10 "Objects"

The output displays live object counts:

     Objects
                   Views:     142         ViewRootImpl:        1
             AppContexts:       3           Activities:        1
                  Assets:      12        AssetManagers:        0
           Local Binders:      32        Proxy Binders:       45
           Parcel memory:      15         Parcel count:       30
        Death Recipients:       2             WebViews:        1

This section displays counts of active framework objects, IPC handles, and
Parcel allocations. For `WebView` diagnostics, focus primarily on `Activities`
and `WebViews`.

Perform the target user interaction (such as opening and closing a web screen)
repeatedly and compare the counts:

- **Instance leak:** If `WebViews` or `Activities` increments on each
  navigation and doesn't return to baseline, your app is leaking the Java
  `WebView` instance or host `Activity` (for example, due to a missing
  `ViewGroup.removeView()` or retained listener references). Because a leaked
  `Activity` pins its entire view tree and decoded image resources in memory,
  repeated visits will rapidly exhaust the Java heap and cause
  `OutOfMemoryError` crashes.

- **Native or DOM leak:** If `WebViews` and `Activities` remain constant
  while total process RSS and **Private Other** continue to climb, the leak
  originates in unreleased native resources, DOM elements, or JavaScript
  engine bindings. Because these allocations reside in native memory and
  bypass the ART garbage collector, they remain invisible to standard Java
  leak detection tools and continue accumulating until the operating system
  terminates the app.

### Profile the isolated renderer process using CLI

Running `dumpsys meminfo` with your app's package name only outputs memory for
the main host process. To inspect the isolated renderer process where web pages
are rendered:

1. Find the process ID (PID) of the isolated renderer service:

       adb shell dumpsys activity processes <var>PACKAGE_NAME</var> | grep "Isolated.*SandboxedProcessService"

   The output displays the isolated process record and its PID
   <var translate="no">RENDERER_PID</var> (for example, `22155`):

       Isolated #5: ProcessRecord{... 22155:com.google.android.webview.debug:sandboxed_process0:...}

2. Inspect the memory breakdown of the renderer process using its PID:

       adb shell dumpsys meminfo <var>RENDERER_PID</var>

3. Inspect the host app process to evaluate the browser-side footprint:

       adb shell dumpsys meminfo <var>PACKAGE_NAME</var>

### Inspect memory maps and allocations

To see which native subsystems or allocators occupy anonymous memory, inspect
the process memory maps:

    adb shell "cat /proc/$(pidof <var>PACKAGE_NAME</var>)/maps" | grep "anon:"

The following table lists common anonymous memory tags and their relevance to
memory growth:

| Memory Tag | Subsystem | Relevance to app and web content | Common memory increase cause? |
|---|---|---|---|
| `[anon:partition_alloc]` | Chromium PartitionAlloc | Allocations for DOM trees, rendering buffers, V8 JavaScript heap, and WebAssembly execution in `WebView`. | **Yes (High):** Loading heavy web pages, media-rich DOMs, or failing to call `destroy()` on discarded `WebView` instances directly inflates this tag. |
| `[anon:scudo...]` or `[anon:libc_malloc]` | Android native heap allocators ([Scudo](https://source.android.com/docs/security/test/scudo) / jemalloc) | General C/C++ native allocations used by NDK libraries, JNI bridges, and native graphics pipelines. | **Yes (Moderate to High):** Growth occurs when native JNI wrappers or third-party C++ dependencies retain unreleased allocations across navigations. |
| `[anon:...]` (for example, `[anon:quickjs_heap...]`) | Custom scripting or native runtimes | Embedded JavaScript engines, custom WebAssembly runtimes, or custom native buffer pools. | **Yes (Context-dependent):** Common in hybrid apps that execute scripting engines alongside native views and fail to clean up runtime bindings. |

### Limitations of in-app memory APIs

In-app memory APIs (such as [`Debug.getMemoryInfo`](https://developer.android.com/reference/android/os/Debug#getMemoryInfo(android.os.Debug.MemoryInfo)) or
[`ActivityManager.getProcessMemoryInfo`](https://developer.android.com/reference/android/app/ActivityManager#getProcessMemoryInfo(int%5B%5D))) only measure the calling process.
In multi-process mode, these APIs can't capture the memory consumed by the
isolated renderer process. For an accurate total memory assessment, rely on
system tools like `dumpsys meminfo`, Perfetto, or Android Studio Profiler.

## Triaging high memory in a hybrid app

When diagnosing unexplained memory growth during recurring `WebView`
interactions (such as opening web links or navigating web-powered feeds), use
the following triage workflow to isolate whether the leak originates in the
Java layer or the native engine:

1. **Isolate the leak type (Java versus native):**
   Run `dumpsys meminfo -a <var>PACKAGE_NAME</var> | grep -A 10 "Objects"`
   before and after repeated user transitions (such as opening and closing web
   articles or swiping through feeds).

   - *Observation:* If `Activities` and `WebViews` counts remain steady (for example, 1--2 active instances), the app isn't leaking `Activity` contexts or Java `WebView` instances.
2. **Measure memory delta across interactions (Time-series tracking):**
   Capture `dumpsys meminfo` snapshots across multiple user interactions to
   calculate the allocation rate per transition:

   - *Observation:* Java heap stays capped and healthy (spiking during use and dropping after garbage collection), but **Private Other** and **Native Heap** steadily climb by several megabytes per transition. This proves the leak is entirely in native memory outside the ART runtime. Standard Java heap dumps (`.hprof`) won't show any issues.
3. **Inspect Anonymous Memory Maps:** Examine the process memory maps using ADB
   (see [Inspect memory maps and allocations](https://developer.android.com/develop/ui/views/layout/webapps/manage-webview-memory#inspect-memory-maps)):

       adb shell "cat /proc/$(pidof <var>PACKAGE_NAME</var>)/maps" | grep "anon:"

   - *Observation:* Memory growth is concentrated in `[anon:partition_alloc]` or embedded scripting engine heaps, accompanied by a slow climb in JNI global references. This indicates that while the Java views were replaced, the underlying native page objects or JavaScript bindings weren't released.
4. **Remediation:**

   - Ensure that every recycled or discarded `WebView` explicitly stops active scripts (`stopLoading()`), clears history, and calls `destroy()`.
   - Tear down custom JavaScript bridge callbacks or JNI global references associated with dismissed views.
   - Confirm that `Private Other` and process RSS stabilize after navigation transitions.

## Additional resources

To learn more about debugging and profiling memory and `WebView` performance,
see the following resources:

- [Manage your app's memory](https://developer.android.com/topic/performance/memory)
- [Overview of memory management](https://developer.android.com/topic/performance/memory-overview)
- [Debug web apps](https://developer.android.com/develop/ui/views/layout/webapps/debugging)