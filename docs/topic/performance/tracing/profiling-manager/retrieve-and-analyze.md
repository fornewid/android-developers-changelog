---
title: https://developer.android.com/topic/performance/tracing/profiling-manager/retrieve-and-analyze
url: https://developer.android.com/topic/performance/tracing/profiling-manager/retrieve-and-analyze
source: md.txt
---

After you [retrieve a profile from a test device or download it from your
backend](https://developer.android.com/topic/performance/tracing/profiling-manager/upload-worker), you can open the file in the [Perfetto UI](https://ui.perfetto.dev/) to inspect timelines,
thread states, and memory retention graphs. This page describes how to navigate
redacted system traces and Java heap dumps captured with `ProfilingManager`.

## Visualize system traces

Open your `.perfetto-trace` file in the [Perfetto UI](https://perfetto.dev/docs/getting-started/system-tracing#viewing-your-first-trace) to inspect CPU and
thread activity over time.
![Timeline of a redacted system trace in Perfetto UI](https://developer.android.com/static/topic/performance/images/tracing/redacted-trace.png) **Figure 1.** Redacted trace example.

To protect user privacy, `ProfilingManager` redacts system traces by combining
CPU activity from all other processes into a single `OtherProcesses` track.
Inspecting this combined track still lets you determine whether slowness in your
app was caused by an internal bottleneck or overall device load.

Figure 2 highlights the main sections of a redacted system trace:
![Numbered sections of a redacted system trace in Perfetto UI](https://developer.android.com/static/topic/performance/images/tracing/redacted-trace-sections.png) **Figure 2.** Sections of a redacted trace.

1. **CPU list**: Displays all available processors on your device.
2. **CPU tasks**: Shows which threads each CPU was executing.
3. **Other processes view**: Displays CPU resources consumed by other processes.
4. **Process View**: Shows your app's process.
5. **Threads View**: Displays threads running within your process and their thread states (Runnable (R), Running (R), Sleeping (S), Uninterruptible Sleep (D)), which map directly to Linux Process States.
6. **Trace slices** : This section shows trace annotations added by app developers or the framework. These annotations encompass computations between [`Trace.beginSection`](https://developer.android.com/reference/kotlin/androidx/tracing/Trace#beginSection(kotlin.String)) and [`Trace.endSection`](https://developer.android.com/reference/kotlin/androidx/tracing/Trace#endSection()).

For more information on Perfetto UI and trace visualization, see the [Perfetto
docs](https://perfetto.dev/docs/visualization/perfetto-ui).

## Visualize Java heap dumps

Once you capture a Java heap dump using [`PROFILING_TYPE_JAVA_HEAP_DUMP`](https://developer.android.com/reference/android/os/ProfilingManager#PROFILING_TYPE_JAVA_HEAP_DUMP),
open the resulting `.perfetto-java-heap-dump` file in the [Perfetto UI](https://ui.perfetto.dev/) to
identify memory leaks or optimize memory usage. In the **Heapdump Explorer**,
you can explore the heap graph, inspect flame graphs of cumulative object sizes,
and browse classes, objects, and dominators, as shown in Figure 3.
![Perfetto UI Heapdump Explorer showing a flame graph of Java heap object sizes.](https://developer.android.com/static/topic/performance/images/tracing/profilingmanager-java-heap-dump-flamegraph.png) **Figure 3.** Java heap dump flame graph in the Perfetto UI.

### How ProfilingManager heap dumps differ from HPROF dumps

Unlike standard `.hprof` heap dumps (such as those captured with
[`Debug.dumpHprofData`](https://developer.android.com/reference/android/os/Debug#dumpHprofData(java.lang.String)) or in Android Studio), `ProfilingManager` captures a
[Perfetto ART heap dump](https://perfetto.dev/docs/data-sources/java-heap-profiler) (`.perfetto-java-heap-dump`). Rather than dumping
raw memory contents, `ProfilingManager` records the **object retention graph and
sizing metadata** while omitting the raw data stored inside objects:

- **What's collected** :
  - **Classes and types**: Class names, superclass hierarchies, classloaders, instance sizes, and reference types (such as normal classes, arrays, strings, or weak, soft, finalizer, and phantom references).
  - **Object instances and sizes** : Each object's shallow size (`self_size`), its heap region (`HEAP_TYPE_APP`, `HEAP_TYPE_ZYGOTE`, or `HEAP_TYPE_BOOT_IMAGE`), and associated native memory registered through `NativeAllocationRegistry`.
  - **References and GC roots**: Garbage collection roots (such as JNI globals and locals, Java stack frames, and thread objects) and field-level reference chains showing which object retains another object and through which field name.
  - **Select sizing metadata** : Non-sensitive metadata for specific framework types, such as `Bitmap` dimensions (`mWidth` and `mHeight`).
- **What's omitted** : Actual primitive field values, `String` character contents, and raw array payloads (`byte[]`, `char[]`, and other primitive arrays). Omitting raw object contents protects user privacy on production devices and keeps dump files significantly smaller.

## Next steps

Beyond visual inspection in the Perfetto UI, you can [query profiles with
PerfettoSQL](https://developer.android.com/topic/performance/tracing/profiling-manager/querying-profiles), [analyze traces in bulk](https://developer.android.com/topic/performance/tracing/profiling-manager/bulk-trace-analysis), or [analyze profiles with
AI](https://developer.android.com/topic/performance/tracing/profiling-manager/analyze-profiles-with-ai).