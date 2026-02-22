---
title: https://developer.android.com/topic/performance/tracing/profiling-manager/retrieve-and-analyze
url: https://developer.android.com/topic/performance/tracing/profiling-manager/retrieve-and-analyze
source: md.txt
---

This page describes how to retrieve traces and visualize them in the Perfetto
UI.

## Retrieve traces

After a profile is recorded, traces are saved on your device. Before you can
analyze these traces, you have to retrieve them.

Trace locations are provided by [`ProfilingResult.getResultFilePath()`](https://developer.android.com/reference/android/os/ProfilingResult#getResultFilePath()). To
learn how to get the trace location, see [How to capture a profile](https://developer.android.com/topic/performance/tracing/profiling-manager/how-to-capture). Once you
have the location of your trace, you can upload the trace to a server.
| **Note:** `ProfilingManager` saves recorded traces in your [app's directory within
| device storage](https://developer.android.com/training/data-storage/app-specific); you must manage these files afterwards.

### Local Testing: Retrieve traces using ADB

Using `adb` to get traces is helpful for checking performance and debugging
locally.

Redacted traces are saved in your device's files. A typical path for a saved
profile is:

    /data/user/0/<app>/files/profiling/profile_<tag>_<datetime>.perfetto-trace

Where:

- `<app>` is the app name.
- `<datetime>` is the date and time the trace was taken.
- `<tag>` is the user-provided tag configured using [`setTag`](https://developer.android.com/reference/kotlin/androidx/core/os/ProfilingRequestBuilder#setTag(kotlin.String))

| **Note:** To find the exact recording location, check the [`ProfilingResult.getResultFilePath`](https://developer.android.com/reference/android/os/ProfilingResult#getResultFilePath()) API.
| **Key Point:** For debugging purposes, you can enable a [debug command](https://developer.android.com/topic/performance/tracing/profiling-manager/debug-mode#enable-unredacted-traces) that instructs `ProfilingManager` to also store an unredacted version of the recorded traces. These unredacted traces are saved in the `/data/misc/perfetto-traces/profiling` directory.

If unredacted traces are enabled and saved, use the following `adb` command to
pull them from the device:

`adb pull
/data/misc/perfetto-traces/profiling/<trace-name>.perfetto-trace-unredacted`
| **Note:** The first 20 alphanumeric characters of the tag provided in `setTag()` are included in the `<trace-name>`, along with details like the profile type and date.

## Visualize traces

After retrieving your trace to your computer, you can then [view it in the
Perfetto UI](https://perfetto.dev/docs/getting-started/system-tracing#viewing-your-first-trace).
![Redacted trace example](https://developer.android.com/static/topic/performance/images/tracing/redacted-trace.png) **Figure 1.**: Redacted trace example.

In a redacted trace, the `OtherProcesses` section combines all CPU activity from
other processes. Combining processes keeps what those other processes were doing
private.

However, seeing this combined CPU activity still lets you check if the system
was overloaded during your recording. Checking the system activity helps you
figure out if your app was slow because of an internal issue or because the
system was generally slow.
| **Note:** Traces from `ProfilingManager` are different from those taken directly using Perfetto locally because redaction is applied.

The following image highlights and briefly describes the main parts you will see
in the trace:
![Sections of a redacted
trace](https://developer.android.com/static/topic/performance/images/tracing/redacted-trace-sections.png) **Figure 2.**: Sections of a redacted trace.

1. **CPU list**: Displays all available processors on your device.
2. **CPU tasks**: Shows which threads each CPU was executing.
3. **Other processes view**: Displays CPU resources consumed by other processes.
4. **Process View**: Shows your app's process.
5. **Threads View**: Displays threads running within your process and their thread states (Runnable (R), Running (R), Sleeping (S), Uninterruptible Sleep (D)), which map directly to Linux Process States.
6. **Trace slices** : This section shows trace annotations added by app developers or the framework. These annotations encompass computations between [`Trace.beginSection`](https://developer.android.com/reference/androidx/tracing/Trace#beginSection(kotlin.String)) and [`Trace.endSection`](https://developer.android.com/reference/androidx/tracing/Trace#endSection()).

For more information on Perfetto UI and trace visualization, see the [Perfetto
docs](https://perfetto.dev/docs/visualization/perfetto-ui).