---
title: https://developer.android.com/android-performance-analyzer/frame-profiler/export
url: https://developer.android.com/android-performance-analyzer/frame-profiler/export
source: md.txt
---

The Frame Profiler in Android Performance Analyzer makes it easier for you to export your frame profiles for
analysis beyond what's available in the Frame Profiler itself. This guide
explains how to export your frame profiles to RenderDoc for in-depth frame
debugging.

## Export to RenderDoc

Android Performance Analyzer can export your captured frames directly to RenderDoc for analysis.
This is helpful when you want to closely examine the constituent parts of a
frame and how it was rendered.

RenderDoc is also useful when you need to investigate CPU thread activity,
because the Frame Profiler doesn't reliably replicate the original application's
CPU workload.

To generate an `.rdc` file that you can import into RenderDoc, use the
![](https://developer.android.com/static/android-performance-analyzer/images/icon-export.png)
[**Export** button](https://developer.android.com/android-performance-analyzer/frame-profiler/view#export) in the frame profile view.