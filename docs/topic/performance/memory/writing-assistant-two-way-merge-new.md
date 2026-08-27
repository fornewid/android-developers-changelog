---
title: https://developer.android.com/topic/performance/memory/writing-assistant-two-way-merge-new
url: https://developer.android.com/topic/performance/memory/writing-assistant-two-way-merge-new
source: md.txt
---

The following pages provide information about improving your app's use of
memory.

## General memory guidance

[Memory overview](https://developer.android.com/topic/performance/memory-overview)
:   Explains core Android memory architecture, RAM constraints, and how the operating system balances processes using the Low Memory Killer (LMK).

[Memory management](https://developer.android.com/topic/performance/memory/manage-app-memory)
:   Outlines developer best practices for releasing resources across component lifecycles, avoiding leaks, and managing memory when transitioning between process states.

[Understanding and troubleshooting Android memory](https://developer.android.com/topic/performance/memory/guide)
:   Provides a comprehensive overview of Android memory architecture, the tools available for analysis, and hands-on exercises to help you identify and resolve memory-related issues.

## Area specific optimizations

[Games memory overview](https://developer.android.com/games/optimize/memory-overview)
:   Details memory budgeting, native allocation handling, and graphic asset management guidance tailored specifically for apps using game engines.

[Optimizing bitmap images](https://developer.android.com/develop/ui/compose/graphics/images/optimization)
:   Demonstrates how to size, decode, and cache bitmap assets efficiently within image libraries.

[Manage and diagnose WebView memory](https://developer.android.com/develop/ui/views/layout/webapps/manage-webview-memory)
:   Explains the WebView multi-process memory model, describes how to properly manage its lifecycle to prevent leaks, and provides practical workflows for diagnosing memory issues.

[R8 code optimization](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization)
:   Explains how to leverage R8 to reduce APK size, metadata overhead, and runtime memory consumption.

## Local memory debug tools

[Android Studio tools](https://developer.android.com/studio/profile)
:   Provides real-time heap inspection, memory allocation tracking, and leak detection workflows directly inside the IDE.

[Perfetto Heap Dump Explorer](https://perfetto.dev/docs/visualization/heap-dump-explorer)
:   Offers deep visual analysis of native and Java/Kotlin heap dumps to isolate retained object trees and anonymous memory allocations.

[Capture a system trace on device](https://developer.android.com/topic/performance/tracing/on-device)
:   Shows how to record on device system level traces to address performance-related bugs in your app.

[Debugging memory usage on Android](https://perfetto.dev/docs/case-studies/memory)
:   Teaches how to understand Linux memory management and use tools like dumpsys meminfo, Perfetto, native heap profiles, and heap dumps to track memory usage and identify leaks.

## Production level memory tools

[Android vitals: Memory usage (anonymous RSS + swap)](https://developer.android.com/topic/performance/vitals/memory-usage)
:   Android vitals shares your app's production memory usage broken down by the process states foreground, foreground service, background service.

[Android vitals: Bitmap memory usage](https://developer.android.com/topic/performance/vitals/bitmap-memory-usage)
:   Android vitals provides metrics on an app's bitmap memory footprint by aggregating data from Android devices

[Android vitals: DEX code optimization](https://developer.android.com/topic/performance/vitals/code-optimization)
:   Android vitals can alert you when your app's DEX code optimization levels are low. This includes obfuscation, shrinking, and optimization for apps and games that use R8

[Crashlytics](https://firebase.google.com/support/release-notes/android#crashlytics_v20-1-0)
:   Surfaces production Out-Of-Memory (OOM) exceptions and memory limiter kills with diagnostic context to prioritize and fix field crashes.

[ProfilingManager](https://developer.android.com/topic/performance/tracing/profiling-manager/overview)
:   Advanced API that enables apps to programmatically collect and upload production heap dumps and heap profiles from live user sessions.

## Additional resources

### Blog posts

- [Preparing your app for broader memory limits](https://android-developers.googleblog.com/2026/08/app-broader-memory-limits.html)
- [Prioritizing Memory Efficiency: Essential Steps for Android 17](https://android-developers.googleblog.com/2026/06/prioritizing-memory-efficiency-steps-for-android-17.html)

### Videos

[Engineering memory-performant Android apps](https://www.youtube.com/watch?v=fOXJR5qLq54)