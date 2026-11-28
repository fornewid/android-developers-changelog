---
title: Trace WebView performance  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/layout/webapps/trace-webview
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Trace WebView performance Stay organized with collections Save and categorize content based on your preferences.





If your app relies heavily on web content and you want optimal performance, you
need to understand how WebView behaves *under the hood*. Most apps don't need
this level of detail, but for performance-focused apps, you can use
[Perfetto](https://perfetto.dev/), the system-wide performance tracing tool for Android,
to gather detailed performance data. This applies not only to `WebView` objects
themselves, but to any API your app calls in the [`android.webkit`](/reference/android/webkit/package-summary) and
[`androidx.webkit`](/reference/androidx/webkit/package-summary) packages.

Tracing WebView with Perfetto helps you diagnose performance bottlenecks, such
as slow startup times, jank, network latency, and the impact of specific
WebView APIs on your app's performance.

This document describes how to do the following:

* [Record a trace using the Perfetto UI](#record-trace)
* [Enable the recommended trace categories](#recommended-categories)
* [Analyze WebView startup](#analyze-startup)
* [Understand the trace](#understand-trace)

## Record a trace using the Perfetto UI

The most straightforward way to record and analyze a WebView trace is by using
the Perfetto UI.

### Prerequisites

Before you record a trace, make sure you have the following:

* An Android device connected to your workstation with USB debugging enabled.
* [ADB](/tools/adb) installed and working on your workstation.
* A Chromium-based browser on your workstation.

### Record the trace

To record a trace, do the following:

1. In a Chromium-based browser on your workstation, open the [Perfetto
   UI](https://ui.perfetto.dev/).
2. In the left navigation menu, click **Record new trace**.
3. Configure the trace categories to capture WebView data. See the
   [Recommended trace categories](#recommended-categories) section for the specific toggles to
   enable.
4. Click **Start tracing**. Don't rely on a fixed trace duration; instead,
   control the recording manually so that you capture the complete scenario.
5. While the trace is recording, interact with your app on the device to
   reproduce the performance issue.
6. When you have reproduced the issue, click **Stop**. The trace automatically
   loads in the Perfetto UI timeline for analysis.

## Recommended trace categories

To capture meaningful data about WebView performance, you must enable specific
trace categories in the Perfetto recording settings.

The categories in this section are a basic set that covers most WebView
investigations. Perfetto offers many more probes, such as CPU scheduling,
memory, and power, that can be helpful depending on what you're debugging.
Take a look at the full list of options in the Perfetto UI and enable any that
are relevant to your issue.

Under **Probes** in the Perfetto UI, configure the following:

1. Under **Android apps & svcs**, enable **Atrace userspace annotations** and
   select the following categories:

   * **Activity Manager** (`am`)
   * **AIDL calls** (`aidl`)
   * **System Server** (`ss`)
   * **View System** (`view`)
   * **WebView** (`webview`)
   * **Window Manager** (`wm`)

   The `aidl`, `view`, and `wm` categories help you correlate WebView events
   with cross-process calls, view layout and drawing, and window changes.
2. In the same probe, turn on **Record events from all Android apps and
   services**. This captures custom trace events emitted by your app and by
   the system services that WebView interacts with.
3. Under **Chrome browser**, enable **Chrome browser tracing**.
4. Under **Additional Categories**, select the following categories:
   `android_webview.timeline, android_webview, base, blink, benchmark,
   blink.worker, blink.user_timing, blink.resource, blink.net, blink.console,
   blink.bindings, browser, Java, startup, navigation, interactions, loading,
   net, netlog, v8`.
5. Under **High Overhead Categories**, select
   `disabled-by-default-histogram_samples`.

## Analyze WebView startup

A common use case for tracing is analyzing WebView startup latency. To ensure
you capture the complete initialization process, follow these tips:

* **Force stop the app before recording:** If the app is already running or in
  the background, you won't capture the cold start performance of WebView.
  Force stop the app process using ADB:

  ```
  adb
  shell am force-stop YOUR_PACKAGE_NAME
  ```
* **Start the trace first:** Make sure you click **Start tracing** in the
  Perfetto UI before launching your app on the device.

## Understand the trace

After your trace loads in the Perfetto UI, you can search for specific events
and inspect the timeline. Because internal trace markers can change between
Android releases, focus your analysis on the higher-level categories you
enabled:

* **`android_webview` and `android_webview.timeline`:** These events show
  the lifecycle of WebView initialization and rendering.
* **`blink` and `v8`:** Look for bottlenecks in HTML parsing, layout
  calculation, and JavaScript execution.
* **`net` and `netlog`:** Examine these events for network requests, response
  latencies, and resource loading delays.
* **`navigation` and `startup`:** These events correspond to page loading
  phases and the initial setup of the browser engine.

## Additional resources

For general guidance on capturing system traces on Android, navigating the
Perfetto UI, and interpreting non-WebView events, see the following resources:

* [Overview of system tracing](/topic/performance/tracing): An introduction to the system tracing
  tools available on Android, including Perfetto.
* [App startup analysis and optimization](/topic/performance/appstartup/analysis-optimization): How to use Perfetto traces to
  analyze and improve app startup.
* [Tracing 101](https://perfetto.dev/docs/tracing-101): An overview of tracing concepts from the
  Perfetto documentation.
* [Perfetto UI](https://perfetto.dev/docs/visualization/perfetto-ui): How to navigate the timeline, search for
  events, and query a trace.
* [Android trace analysis](https://perfetto.dev/docs/getting-started/android-trace-analysis): A walkthrough of analyzing common
  Android performance problems with Perfetto.