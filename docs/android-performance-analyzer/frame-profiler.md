---
title: https://developer.android.com/android-performance-analyzer/frame-profiler
url: https://developer.android.com/android-performance-analyzer/frame-profiler
source: md.txt
---

You can use the Frame Profiler in Android Performance Analyzer to analyze your app's GPU performance when rendering
a single, specific frame.

> [!NOTE]
> **Note:** The Frame Profiler is an experimental feature that's only available in canary versions of Android Performance Analyzer.

## What is a frame profiler?

A *frame profiler* is a tool for measuring time spent and other performance
metrics for each render pass that goes into a single frame. Where a system
profiler focuses on an app's impact on the entire system over a given period of
time, a frame profiler is concerned with just one frame.

A frame profiler is also distinct from a *frame debugger* , which extracts
information about all of the constituent parts of a frame and how it was
rendered, providing a microscopic view of the rendering process. For frame
debugging, you can [export results from the Frame Profiler to
RenderDoc](https://developer.android.com/android-performance-analyzer/frame-profiler/export#export-renderdoc).

## Profiling process

When you [capture a frame profile](https://developer.android.com/android-performance-analyzer/frame-profiler/capture), the Frame Profiler in Android Performance Analyzer records the sequence
of API calls, the parameters passed, and relevant GPU memory contents in a [GFXR
file](https://github.com/LunarG/gfxreconstruct). This lets the Frame Profiler accurately repeat the
frame as many times as necessary to [complete the profiling tasks](https://developer.android.com/android-performance-analyzer/frame-profiler/view#task-details) and
collect data for the frame profile.

Before measuring frame and render pass duration, the tool runs a compute shader
workload to force the GPU to maximum frequency. This establishes a stable
baseline for comparison, ensuring that transient frequency variations don't skew
the data across multiple frame profiles.

To ensure greater accuracy and consistency, the Frame Profiler loops the frame
up to 100 times and averages the results, filtering out any samples that are
contaminated by another app's GPU activity.

## User guides

To learn more about the Frame Profiler in Android Performance Analyzer, see the following guides:

- [Quickstart](https://developer.android.com/android-performance-analyzer/frame-profiler/quickstart). Get started with running and viewing frame profiles right away if you're already familiar with GPU profiling.
- [Verify compatibility](https://developer.android.com/android-performance-analyzer/frame-profiler/compatibility). Learn how to get the most reliable results for your test device, game engine, and graphics API.
- [Capture a frame profile](https://developer.android.com/android-performance-analyzer/frame-profiler/capture). Learn how to configure and run a frame profile.
- [View a frame profile](https://developer.android.com/android-performance-analyzer/frame-profiler/view). Learn about the data included in a frame profile and how to navigate it.
- [Export and analyze results](https://developer.android.com/android-performance-analyzer/frame-profiler/export). Learn how to export your frame profiles to RenderDoc for further analysis.