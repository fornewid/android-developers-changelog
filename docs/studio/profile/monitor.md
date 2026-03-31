---
title: Android Device Monitor  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/profile/monitor
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Studio](https://developer.android.com/studio)

# Android Device Monitor Stay organized with collections Save and categorize content based on your preferences.



Android Device Monitor was **deprecated in Android Studio
3.1 and removed from Android Studio 3.2**. The features that you could use
through the Android Device Monitor have been replaced by new features. The table
below helps you decide which features you should use instead of these deprecated
and removed features.

| Android Device Monitor component | What you should use |
| **Dalvik Debug Monitor Server (DDMS)** | This tool is deprecated. Instead, use [**Android Profiler**](/studio/profile) in Android Studio 3.0 and higher to profile your app's CPU, memory, and network usage.  If you want to perform other debugging tasks, such as sending commands to a connected device to set up port-forwarding, transfer files, or take screenshots, then use the [**Android Debug Bridge (`adb`)**](/studio/command-line/adb), [**Android Emulator**](/studio/run/emulator), [**Device Explorer**](/studio/debug/device-file-explorer), or [**Debugger window**](/studio/debug). |
| **Traceview** | This tool is deprecated. To inspect `.trace` files captured by [instrumenting your app](/studio/profile/generate-trace-logs) with the `Debug` class, record new method traces, export `.trace` files, and inspect real-time CPU usage of your app's processes, use the Android Studio [**CPU profiler**](/studio/profile/cpu-profiler). |
| **Systrace** | If you need to inspect native system processes and address UI jank caused by dropped frames, use [**`systrace`**](/topic/performance/tracing/command-line) from the command line or the simplified **System Trace** in the [**CPU Profiler**](/studio/profile/cpu-profiler). The **CPU Profiler** provides many features for profiling your app's processes. |
| **Tracer for OpenGL ES** | Use the **[Android GPU Inspector](/agi)**. |
| **Hierarchy Viewer** | If you want to inspect your app's view hierarchy at runtime, use [**Layout Inspector**](/studio/debug/layout-inspector).  If you want to profile the rendering speed of your app's layout, use **[Window.OnFrameMetricsAvailableListener](/reference/android/view/Window.OnFrameMetricsAvailableListener)** as described in [this blog post](https://android-developers.googleblog.com/2017/08/understanding-performance-benefits-of.html). |
| **Pixel Perfect** | Use **[Layout Inspector](/studio/debug/layout-inspector)**. |
| **Network Traffic tool** | If you need to view how and when your app transfers data over a network, use the [**Network Profiler**](/studio/profile/network-profiler). |

## Start Android Device Monitor

To start the standalone Device Monitor application in Android Studio 3.1 and
lower, enter the following on the command line in the
`android-sdk/tools/` directory:

```
monitor
```

You can then link the tool to a connected device by selecting the device
from the **Devices** pane. If you have trouble viewing panes or windows,
select **Window > Reset Perspective** from the menu bar.

**Note:** Each device can be attached to only one debugger
process at a time. So, for example, if you are using Android Studio to debug
your app on a device, you need to disconnect the Android Studio debugger from
the device before you attach a debugger process from the Android Device
Monitor.