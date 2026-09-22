---
title: https://developer.android.com/topic/performance/issues/bg-wifi
url: https://developer.android.com/topic/performance/issues/bg-wifi
source: md.txt
---

When an app performs Wi-Fi scans in the background, it wakes up the CPU,
causing rate of battery drain. When too many scans occur, the device's
battery life may be noticeably shortened. An app is considered to be running in
the background if it is in the `PROCESS_STATE_BACKGROUND` or
`PROCESS_STATE_CACHED` state.

This document provides tips about diagnosing and addressing excessive Wi-Fi
scans in the background.

> [!NOTE]
> **Note:** For information on how Android Play Vitals tracks and reports this issue, see [Excessive Wi-Fi Scanning in the Background in Android vitals](https://developer.android.com/google/play/vitals/bg-wifi).

## Investigate the Wi-Fi scans

Tools such as Battery Historian can help you gain more insight into your
app's scanning behavior. Battery Historian provides a visualization of Wi-Fi
scanning behavior on a per-app basis, which can help you gain a clearer
picture of what's happening with your app. For more information about Battery
Historian, see
[Analyzing Power Use with Battery Historian](https://developer.android.com/topic/performance/power/battery-historian#asd).

For information about the mechanics of using Battery Historian, see
[Batterystats and Battery Historian Walkthrough](https://developer.android.com/topic/performance/power/setup-battery-historian).

## Reduce the scans

If possible, your app should be performing Wi-Fi scans while the app is running
in the foreground. Foreground services automatically present notifications;
performing Wi-Fi scans in the foreground thus makes the user aware of the
why and when Wi-Fi scans take place on their device.

For information on how to scan while in the foreground,
see the documentation for the
[`WifiManager`](https://developer.android.com/reference/android/net/wifi/WifiManager#startScan()) class.

If your app cannot avoid performing Wi-Fi scans while the app is running in
the background, it may benefit from applying
a [Lazy First](https://developer.android.com/topic/performance/power#lazy) strategy. Lazy First
encompasses three techniques that you can use to cut down on Wi-Fi scans:
*reduce* , *defer* , and *coalesce* .
For information about these techniques, see
[Optimizing for Battery Life](https://developer.android.com/topic/performance/power).

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Excessive Mobile Network Usage in Background](https://developer.android.com/topic/performance/issues/bg-network-usage)