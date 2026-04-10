---
title: https://developer.android.com/agi/sys-trace/system-profiler
url: https://developer.android.com/agi/sys-trace/system-profiler
source: md.txt
---

With Android GPU Inspector (AGI), you can perform system profiling that includes
a wide range of tracing options and GPU performance measurements for your
Android app. In comparison to the
[Android Studio profiling tools](https://developer.android.com/topic/performance/tracing),
AGI combines many of those capabilities into one tool, and then provides more
in-depth GPU coverage and analysis. The available system profiling data
includes the following:

- App trace data including [ATrace](https://perfetto.dev/docs/data-sources/atrace) markers
- CPU and process scheduling data
- GPU performance info such as counter, activity, and lifecycle data
- Trace data for Vulkan API calls
- Memory usage statistics
- Battery usage statistics

System Profiler is the AGI component that manages the UI and
instrumentation for system profiling over multiple app frames. It is built on
top of the [Perfetto](https://perfetto.dev) tracing system. For
information about the AGI component for profiling individual app frames, see the
[Frame profiler](https://developer.android.com/agi/frame-trace/frame-profiler) overview.

## Get started

The AGI [quickstart](https://developer.android.com/agi/start) describes how to set up AGI, capture a system
profile, and then open the resulting trace file. The next section describes the
configuration options in more detail.

## Profiling options

This sections describes the main options that are available when you
[profile an app](https://developer.android.com/agi/start#system-profile).

### Application settings

The **Application** settings identify the Android app to run and trace during
system profiling. Selecting an Android app to trace during system profiling is
optional but recommended because without it, the resulting trace file won't
include [ATrace](https://perfetto.dev/docs/data-sources/atrace)
markers and GPU activity for an application.

### Trace options

The **Trace Options** specify the profiling data to collect. The
**Configure** button displays the available data sources.

To minimize the performance impact on your Android device when you profile the
system, we recommend that you select fewer data sources if you set the trace
**Duration** to over a minute. However, for traces under a minute, you can
select all data sources with minimal impact.

#### CPU options

The **CPU** option enables the collection of CPU and
process scheduling data through
[ftrace](https://en.wikipedia.org/wiki/Ftrace). This
allows you to see what process and thread is running on each CPU
core. You can also enable these options:

- **Frequency and idle states**: Collects CPU core frequency and idle state change events, which allows you to inspect how the CPU is scaled up or down based on load.
- **Scheduling chains / latency**: Collects additional thread state data about thread scheduling delays and preemption.
- **Thread slices**: Collects ATrace markers in the process views.

#### GPU options

The **GPU** options enable profiling of your app's GPU usage, such as the
collection of GPU frequency and memory usage data. To collect this data, you
must specify an application to trace in the **Application** settings. The
options include the following:

- **Counters**: Collects GPU counter samples. This data is used to determine
  how busy the GPU is and locate bottlenecks, so we recommend that you configure
  these settings.

  The counters are hardware-specific. For example, the minimum frequency for
  sample collection (**Poll Rate** ) may differ based on the counter type. For
  information about supported counters, see
  [GPU performance counters](https://developer.android.com/agi/sys-trace/counters-arm).
- **Frame Lifecycle** : Traces
  [SufaceFlinger](https://source.android.com/devices/graphics/surfaceflinger-windowmanager)
  events, which help determine how frame buffers move through your application,
  the compositor, and window manager. These events allow you to locate missed
  app frames and identify sources of latency in your rendering pipeline.

- **Renderstage slices** Collects data that helps determine how your application
  is using the GPU.

#### Vulkan options

The **Vulkan** options enable tracing of Vulkan API calls, which can then be
enabled by function type. You can use this
data to determine the CPU overhead of Vulkan API calls. The trace records the
duration of each function call, which is displayed within your app's thread
slices when you analyze the data in the
[Vulkan event track](https://developer.android.com/agi/sys-trace/system-profiler-gui#vulkan_event_track).

#### Other options

The additional system profiling options include:

- **Memory**: Collect essential memory usage statistics, both globally and for
  each process.

- **Battery**: Collects battery statistics. This can give you a rough estimate
  of the power usage of your application.

- **Force Tracing into a File on the Device**: Trace data is typically streamed
  over USB while the trace is being captured, which has the least amount of
  overhead and allows for long traces. However, if you encounter problems
  or dropped profiling data due to USB latency, you can select this option to
  save the trace file on the device, which AGI then downloads after tracing
  concludes. This requires sufficient space on your device's internal storage
  to store the trace file.

#### Advanced mode

The **Switch to advanced mode** link launches advanced configuration mode, which
allows you to manually edit the
[Pefetto trace configuration](https://perfetto.dev/docs/concepts/config)
that stores your profiling options.

## View and analyze the results

When you open a trace file that contains system profiling data, AGI displays the
data in the System Profiler UI for analysis. For information
about viewing the data, see [View a system profile](https://developer.android.com/agi/sys-trace/system-profiler-gui).

These topics describe how to analyze system profiling data with AGI:

- [Analyze frame processing times](https://developer.android.com/agi/sys-trace/long)
- [Analyze memory efficiency](https://developer.android.com/agi/sys-trace/memory-efficiency)
- [Analyze texture memory bandwidth usage](https://developer.android.com/agi/sys-trace/texture-memory-bw)
- [Analyze vertex memory bandwidth usage](https://developer.android.com/agi/sys-trace/vertex-memory-bw)
- [Analyze thread scheduling](https://developer.android.com/agi/sys-trace/threads-scheduling)