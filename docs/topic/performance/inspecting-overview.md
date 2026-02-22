---
title: https://developer.android.com/topic/performance/inspecting-overview
url: https://developer.android.com/topic/performance/inspecting-overview
source: md.txt
---

# Inspect performance to help you understand what is happening in your app and ensure it meets your expectations.

Android provides several tools you can use to inspect your app's performance. When getting started, we recommend you focus on one area at a time during inspection. These areas can include the following:

- App startup
- Slow rendering (jank)
- Screen transitions and navigation events
- Long running work
- Operations in the background, such as I/O and networking

Alternatively, you can inspect critical user journeys of your app's workflow. This can help you gain a holistic understanding of where performance and expectations don't align.

There are two main approaches when inspecting performance, manual and automated. It's likely that you start with manual debugging when inspecting a new area.

## Manual inspection

After deciding which area of your app to inspect, you can use a variety of tools to identify what exactly is happening.

The most comprehensive tool to inspect performance on devices running Android 9 and higher is[Perfetto](https://perfetto.dev/). Perfetto provides the highest possible detail of tracing information. By using powerful filters, you can adjust the level of detail for your needs. For more information about how to capture traces from Android devices, see the[Quickstart: Record traces on Android](https://perfetto.dev/docs/quickstart/android-tracing)guide.

The[Android profilers](https://developer.android.com/studio/profile)built into Android Studio can also provide valuable insights into your app's performance, where you can limit the level of detail to your app, or when running on devices earlier than Android 9.

For more information, see[Overview of system tracing](https://developer.android.com/topic/performance/tracing)or watch the in-depth series on[performance debugging](https://www.youtube.com/playlist?list=PLWz5rJ2EKKc-xjSI-rWn9SViXivBhQUnp).

## Automated testing

In addition to manual inspection, you can set up automated tests to collect and aggregate performance data. This helps you understand what users are actually seeing and identify when regressions might occur. For more information about setting up automated performance tests for your app, see[Benchmark your app](https://developer.android.com/topic/performance/benchmarking/benchmarking-overview).

## App startup performance

There are multiple tools you can use to inspect and monitor performance to help improve your app.

### Understand performance locally with Benchmark libraries

- The[Macrobenchmark library](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)helps you measure larger end-user interactions, such as startup, interacting with the UI, and animations.
- The[Microbenchmark library](https://developer.android.com/topic/performance/benchmarking/microbenchmark-overview)helps analyze performance of more granular, app-specific situations.

### Understand performance in production

- [Android vitals](https://developer.android.com/topic/performance/vitals)can help improve your app's performance by alerting you when various performance metrics exceed predetermined thresholds.
- The[Firebase performance SDK](https://firebase.google.com/docs/perf-mon/get-started-android)collects various metrics about your app's performance. For example, you can use the SDK to measure the time between when the user opens the app and when the app becomes responsive, helping identify potential startup bottlenecks.

### Profile locally with Android Studio

- Use[Android Studio](https://developer.android.com/studio/profile)to record and view system traces or stack sampling traces.
- [Record traces](https://developer.android.com/studio/profile/record-traces)using Android Studio. For additional information, see the[Performance Debugging video series](https://www.youtube.com/playlist?list=PLWz5rJ2EKKc-xjSI-rWn9SViXivBhQUnp).
- Use[Simpleperf](https://android.googlesource.com/platform/system/extras/+/master/simpleperf/doc/README.md), a native stack sampling tool for Android, to profile both Android apps and native processes running on Android. It can profile both Java and C++ code on Android.

### Advanced profiling tools: Perfetto tracing

- [Perfetto](https://perfetto.dev/): a platform-wide tracing tool available on Android 10 (API level 29) and higher. For more information, see the[overview of Perfetto traces](https://perfetto.dev/docs/).
- [Run Perfetto using`adb`](https://developer.android.com/studio/command-line/perfetto): describes how to run the`perfetto`command-line tool to capture traces.
- [Recording a trace through the cmdline](https://perfetto.dev/docs/quickstart/android-tracing#recording-a-trace-through-the-cmdline): describes how to build and run the`perfetto`command-line tool to capture traces.
- [Perfetto web-based trace viewer](https://perfetto.dev/docs/quickstart/android-tracing#recording-a-trace-through-the-perfetto-ui): opens Perfetto traces and displays a complete report. You can also open[Systrace](https://developer.android.com/topic/performance/tracing)traces in this viewer using the legacy UI option.

## Additional resources

- [Performance debugging - MAD skills series](https://www.youtube.com/playlist?list=PLWz5rJ2EKKc-xjSI-rWn9SViXivBhQUnp)
- [Profile your app performance](https://developer.android.com/studio/profile)
- [Write a Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)
- [Microbenchmark](https://developer.android.com/topic/performance/benchmarking/microbenchmark-overview)