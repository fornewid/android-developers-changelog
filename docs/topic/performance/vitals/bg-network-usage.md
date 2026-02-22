---
title: https://developer.android.com/topic/performance/vitals/bg-network-usage
url: https://developer.android.com/topic/performance/vitals/bg-network-usage
source: md.txt
---

# Excessive Mobile Network Usage in Background

When an app connects to the mobile network in the background, the app wakes up the CPU and turns on the radio. Doing so repeatedly can run down a device's battery. An app is considered to be running in the background if it is in the`PROCESS_STATE_BACKGROUND`or`PROCESS_STATE_CACHED`state.

This page explains how to determine why your app is excessively using the mobile network while running in the background, and what to do about it.

## Detect the problem

You may not always know that your app is making inordinate use of the network while running in the background. If you have already published your app, Android vitals can make you aware of the problem so that you can fix it.

### Android vitals

Android vitals can help improve your app's performance by alerting you via the[Play Console](https://play.google.com/console/)when your app is using the mobile network excessively in the background.

Android vitals considers background network usage excessive when an app is sending and receiving a combined total of 50 MB per day while running in the background. In Play Console you can check percentage of*battery sessions*that exhibit this behavior.

The definition of*battery session*depends on the platform version.

- In Android 10, a battery session is the aggregation of all battery reports received within a given 24-hour period. A*battery report*refers to the interval between two battery charges either from below 20% to above 80% or from any charge level to 100%.
- In Android 11, a battery session is a fixed 24-hour period.

For information on how Google Play collects Android vitals data, see the[Play Console](https://support.google.com/googleplay/android-developer/answer/7385505)documentation.

## Investigate mobile-network-usage behavior

| **Warning:** Battery Historian is no longer actively maintained; if possible, consider using[system tracing](https://developer.android.com/topic/performance/tracing), the[Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)power metric, or the[Power Profiler](https://developer.android.com/studio/profile/power-profiler)to get insights into battery performance.

Tools such as Battery Historian can help you gain more insight into your app's mobile-network usage. Battery Historian provides a visualization of mobile-radio use on a per-app basis, which can help you gain a clearer picture of what's happening with your app. For more information about Battery Historian, see[Analyzing Power Use with Battery Historian](https://developer.android.com/topic/performance/power/battery-historian#asd). In investigating your app's mobile-network-usage behavior, you should take particular note of the*Mobile network use*line.

For information about the mechanics of using Battery Historian, see[Batterystats and Battery Historian Walkthrough](https://developer.android.com/topic/performance/power/setup-battery-historian).

## Reduce mobile network usage

You can move your app's mobile-network usage to the foreground, alerting the user to the fact that a download is in progress, and providing them with controls to pause or stop the download. To do so, call[`DownloadManager`](https://developer.android.com/reference/android/app/DownloadManager), and set[`setNotificationVisibility(int)`](https://developer.android.com/reference/android/app/DownloadManager.Request#setNotificationVisibility(int))as appropriate.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Excessive Wi-Fi Scanning in the Background](https://developer.android.com/topic/performance/vitals/bg-wifi)