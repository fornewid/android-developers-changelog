---
title: https://developer.android.com/google/play/vitals/bg-wifi
url: https://developer.android.com/google/play/vitals/bg-wifi
source: md.txt
---

When an app performs Wi-Fi scans in the background, it wakes up the CPU,
causing battery drain. When too many scans occur, the device's battery life may
be noticeably shortened. An app is considered to be running in the background
if it is in the `PROCESS_STATE_BACKGROUND` or `PROCESS_STATE_CACHED` state.

> [!NOTE]
> **Note:** For information on how to diagnose and resolve this issue, see [Excessive Wi-Fi Scanning in the Background](https://developer.android.com/topic/performance/issues/bg-wifi).

## Detect the problem

### Android vitals

Android vitals can help improve your app's performance by alerting you via the
[Play Console](https://play.google.com/console/) when your app is
performing excessive Wi-Fi scanning in the background. Android vitals considers
Wi-Fi scanning excessive when an app performs more than 4 scans per hour.
In Play Console you can check percentage of *battery sessions* that exhibit
this behavior.

The definition of *battery session* depends on the platform version.

- In Android 10, a battery session is the aggregation of all battery reports received within a given 24-hour period. A *battery report* refers to the interval between two battery charges either from below 20% to above 80% or from any charge level to 100%.
- In Android 11, a battery session is a fixed 24-hour period.

For information on how Google Play collects Android vitals data, see the [Play
Console](https://support.google.com/googleplay/android-developer/answer/7385505)
documentation.