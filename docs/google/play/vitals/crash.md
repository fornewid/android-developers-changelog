---
title: https://developer.android.com/google/play/vitals/crash
url: https://developer.android.com/google/play/vitals/crash
source: md.txt
---

An Android app crashes whenever there's an unexpected exit caused by an
unhandled exception or signal. An app that is written using Java or Kotlin
crashes if it throws an unhandled exception, represented by the
[`Throwable`](https://developer.android.com/reference/java/lang/Throwable) class. An app that is written using machine code or C++ crashes
if there's an unhandled signal, such as `SIGSEGV`, during its execution.

> [!NOTE]
> **Note:** For information on how to diagnose and resolve this issue, see [Crashes](https://developer.android.com/topic/performance/issues/crash).

## Android vitals metrics and thresholds

Android vitals can help you monitor and improve your app's crash rate.
Android vitals measures several crash rates:

- **Crash rate:** The percentage of your daily active users who experienced any type of crash.
- **User-perceived crash rate:** The percentage of your daily active users
  who experienced at least one crash while they were actively using your app
  (a user-perceived crash). An app is considered to be in active use
  if it is displaying any activity or executing any [foreground service](https://developer.android.com/develop/background-work/services/fgs).

  > [!NOTE]
  > **Note:** For Wear OS apps, user-perceived crash rates include both foreground and background crashes. Wear OS devices always have watch faces running in the background, and users frequently move Wear OS apps to the background, even during active usage, because of the small screen size.

- **Multiple crash rate:** The percentage of your daily active users who
  experienced at least two crashes.

A *daily active user* is a unique user who uses your app on a single day on a
single device, potentially over multiple sessions. If a user uses your app on
more than one device in a single day, each device will contribute to the number
of active users for that day. If multiple users use the same device in a single
day, this is counted as one active user.

User-perceived crash rate is a *core vital* meaning that it affects the
discoverability of your app on Google Play. It is important because the crashes
it counts always occur when the user is engaged with the app, causing the most
disruption.

Play has defined two **bad behavior thresholds** on this metric:

- **Overall bad behavior threshold:** At least 1.09% of daily active users experience a user-perceived crash, across all device models.
- **Per-device bad behavior threshold:** At least 8% of daily active users experience a user-perceived crash, **for a single device model**.

If your app exceeds the overall bad behavior threshold, it is likely to be less
discoverable on all devices. If your app exceeds the per-device bad behavior
threshold on some devices, it is likely to be less discoverable on those
devices, and a warning may be shown on your store listing.

Android vitals can alert you in the [Play Console](https://play.google.com/console/) when your app is
exhibiting excessive crashes. You can also view crash stack traces in
[Android vitals](https://support.google.com/googleplay/android-developer/answer/9859174).

For information on how Google Play collects Android vitals data, see the
[Play Console](https://support.google.com/googleplay/android-developer/answer/7385505) documentation.