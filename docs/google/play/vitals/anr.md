---
title: https://developer.android.com/google/play/vitals/anr
url: https://developer.android.com/google/play/vitals/anr
source: md.txt
---

When the UI thread of an Android app is blocked for too long, an "Application
Not Responding" (ANR) error is triggered. Android vitals tracks and reports ANR
metrics in the Google Play Console to help you monitor your app's stability and
responsiveness across devices.

> [!NOTE]
> **Note:** For information on how to diagnose and resolve this issue, see [ANRs](https://developer.android.com/topic/performance/issues/anr).

## Android vitals metrics and thresholds

Android vitals can help you monitor and improve your app's ANR rate. Android
vitals measures several ANR rates:

- **ANR rate:** The percentage of your daily active users who experienced any type of ANR.
- **User-perceived ANR rate:** The percentage of your daily active users who experienced at least one *user-perceived ANR* . Currently only ANRs of type `Input dispatching timed out` are considered user-perceived.
- **Multiple ANR rate:** The percentage of your daily active users who experienced at least two ANRs.

A *daily active user* is a unique user who uses your app on a single day on a
single device, potentially over multiple sessions. If a user uses your app on
more than one device in a single day, each device will contribute to the number
of active users for that day.

User-perceived ANR rate is a *core vital*, meaning that it affects the
discoverability of your app on Google Play. It is important because the ANRs it
counts always occur when the user is engaged with the app, causing the most
disruption.

Play has defined two **bad behavior thresholds** on this metric:

- **Overall bad behavior threshold:** At least 0.47% of daily active users experience a user-perceived ANR, across all device models.
- **Per-device bad behavior threshold:** At least 8% of daily users experience a user-perceived ANR, **for a single device model**.

If your app exceeds the overall bad behavior threshold, it is likely to be less
discoverable on all devices. If your app exceeds the per-device bad behavior
threshold on some devices, it is likely to be less discoverable on those
devices, and a warning may be shown on your store listing.

Android vitals can alert you through the [Play Console](https://play.google.com/console/) when your app is
exhibiting excessive ANRs.

For information on how Google Play collects Android vitals data, see the [Play
Console](https://support.google.com/googleplay/android-developer/answer/7385505) documentation.