---
title: https://developer.android.com/android-performance-analyzer/frame-profiler/compatibility
url: https://developer.android.com/android-performance-analyzer/frame-profiler/compatibility
source: md.txt
---

This guide contains information about which devices, GPU families, game engines,
and graphics APIs are compatible with Android Performance Analyzer, as well as guidance on how
to handle instances where your device or app under test is only partially
supported.

## Device and GPU compatibility

The Frame Profiler in Android Performance Analyzer supports most Pixel devices starting with Pixel 6, as long as
they're running Android 12 or higher. There may be compatibility issues with
other devices, even if they pass [device validation](https://developer.android.com/android-performance-analyzer/quickstart#device-reqs).

## Engine compatibility

The Frame Profiler in Android Performance Analyzer supports most major game engines such as Unity and the Unreal
Engine. There may be compatibility issues with custom engines.

## API compatibility

The Frame Profiler in Android Performance Analyzer supports Vulkan for graphics. OpenGL is unsupported unless you
use an [ANGLE layer](https://developer.android.com/games/develop/vulkan/overview#about-angle) to run it on top of Vulkan.

### Set the debuggable attribute

Set the [debuggable attribute](https://developer.android.com/guide/topics/manifest/application-element#debug) in the Android manifest in accordance
with the following guidelines:

- If you're profiling an app that uses [Vulkan](https://developer.android.com/games/develop/vulkan/overview) for graphics, set the debuggable attribute to *true*. This allows Vulkan-specific data to be included in traces.
- For Java and Kotlin applications, set the debuggable attribute to *false* to allow the Android Runtime to run at maximum optimized efficiency. This helps your traces mirror real-world performance. It doesn't make as much of a difference for pure C/C++ apps or native game loops, but managed-code apps need it in order to yield accurate profiling data.