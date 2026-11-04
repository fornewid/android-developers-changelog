---
title: https://developer.android.com/topic/performance/tracing/profiling-manager/overview
url: https://developer.android.com/topic/performance/tracing/profiling-manager/overview
source: md.txt
---

The [`ProfilingManager`](https://developer.android.com/reference/android/os/ProfilingManager) API lets you collect real-user performance profiles,
such as [system traces](https://developer.android.com/topic/performance/tracing) and Java heap dumps, from production devices running
Android 15 (API level 35) and higher. It supports two collection mechanisms:
[app-driven profiles](https://developer.android.com/topic/performance/tracing/profiling-manager/how-to-capture) where your app controls the profile collection from
start to stop (Android 15 and higher) and [trigger-based profiles](https://developer.android.com/topic/performance/tracing/profiling-manager/trigger-based-capture) where the
system handles the capture in response to events that you register interest in
on Android 16 (API level 36) and higher.

This guide covers the following topics:

- **Capture profiles** : How to start and stop [app-driven](https://developer.android.com/topic/performance/tracing/profiling-manager/how-to-capture) profile recordings and how to register for [trigger-based](https://developer.android.com/topic/performance/tracing/profiling-manager/trigger-based-capture) profile recordings.
- **Retrieve and upload profiles** : How to [retrieve profiles](https://developer.android.com/topic/performance/tracing/profiling-manager/upload-worker) locally with `adb` or upload them in the background with `WorkManager`.
- **Analyze profiles** : How to [visualize profiles in the Perfetto UI](https://developer.android.com/topic/performance/tracing/profiling-manager/retrieve-and-analyze), [query profiles with PerfettoSQL](https://developer.android.com/topic/performance/tracing/profiling-manager/querying-profiles), [analyze traces in bulk](https://developer.android.com/topic/performance/tracing/profiling-manager/bulk-trace-analysis), and [analyze profiles with AI](https://developer.android.com/topic/performance/tracing/profiling-manager/analyze-profiles-with-ai).
- **Debugging case studies** : How to apply `ProfilingManager` end-to-end to [debug an ANR](https://developer.android.com/topic/performance/tracing/profiling-manager/debugging-anr-example) and [debug an OOM crash](https://developer.android.com/topic/performance/tracing/profiling-manager/debugging-oom-example).
- **Rate limiting and collection behavior** : How to understand [rate limiting
  and collection behavior](https://developer.android.com/topic/performance/tracing/profiling-manager/will-my-profile-always-be-collected) in production.
- **Local debugging** : How to use [debug commands for local profiling](https://developer.android.com/topic/performance/tracing/profiling-manager/debug-mode).

> [!IMPORTANT]
> **Key Point:** This guide is for developers who want to set up a way to collect end-user performance profiles.

## Supported profile types

`ProfilingManager` supports collecting several types of profiles so you can
target specific performance concerns in your app. You can configure requests
directly using platform APIs or using the AndroidX Core builders:

- **System traces** : Captured using [`PROFILING_TYPE_SYSTEM_TRACE`](https://developer.android.com/reference/android/os/ProfilingManager#PROFILING_TYPE_SYSTEM_TRACE) or [`SystemTraceRequestBuilder`](https://developer.android.com/reference/kotlin/androidx/core/os/SystemTraceRequestBuilder).
  - Useful for diagnosing jank, analyzing latency, and general performance debugging.
- **Java heap dumps** : Captured using [`PROFILING_TYPE_JAVA_HEAP_DUMP`](https://developer.android.com/reference/android/os/ProfilingManager#PROFILING_TYPE_JAVA_HEAP_DUMP) or [`JavaHeapDumpRequestBuilder`](https://developer.android.com/reference/kotlin/androidx/core/os/JavaHeapDumpRequestBuilder).
  - Captures a snapshot of your app's Java heap object graph and sizes for memory leak detection and memory optimization.
- **Heap profiles** : Captured using [`PROFILING_TYPE_HEAP_PROFILE`](https://developer.android.com/reference/android/os/ProfilingManager#PROFILING_TYPE_HEAP_PROFILE) or [`HeapProfileRequestBuilder`](https://developer.android.com/reference/kotlin/androidx/core/os/HeapProfileRequestBuilder).
  - Tracks native (or optionally Java) memory allocations over time to help optimize memory usage.
- **Stack sampling** : Captured using [`PROFILING_TYPE_STACK_SAMPLING`](https://developer.android.com/reference/android/os/ProfilingManager#PROFILING_TYPE_STACK_SAMPLING) or [`StackSamplingRequestBuilder`](https://developer.android.com/reference/kotlin/androidx/core/os/StackSamplingRequestBuilder).
  - Samples thread call stacks to help you understand code execution and analyze CPU usage.

## Integrate ProfilingManager with an AI agent

You can use an AI coding agent to integrate `ProfilingManager` into your app.
For example, run the following prompt in your AI coding agent to set up
Application Not Responding (ANR) trigger collection, replacing
`</path/to/codebase>` with the path to your app:

    Read https://developer.android.com/topic/performance/tracing/profiling-manager/trigger-based-capture
    and https://developer.android.com/topic/performance/tracing/profiling-manager/upload-worker
    and integrate ProfilingManager ANR trigger collection (TRIGGER_TYPE_ANR) into my
    app at </path/to/codebase>, including registering the result listener after app
    startup completes and scheduling a WorkManager upload job when a profile is
    received.

You can adapt this prompt to set up other [system triggers](https://developer.android.com/topic/performance/tracing/profiling-manager/trigger-based-capture) (such as
[`TRIGGER_TYPE_OOM`](https://developer.android.com/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_OOM)), or configure [app-driven profile captures](https://developer.android.com/topic/performance/tracing/profiling-manager/how-to-capture) using
the [app-driven profiling guide](https://developer.android.com/topic/performance/tracing/profiling-manager/how-to-capture). After integrating, test your setup locally
using the [debug commands for local profiling](https://developer.android.com/topic/performance/tracing/profiling-manager/debug-mode), and [analyze collected
profiles with an AI agent](https://developer.android.com/topic/performance/tracing/profiling-manager/analyze-profiles-with-ai).