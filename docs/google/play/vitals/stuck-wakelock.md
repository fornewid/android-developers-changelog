---
title: https://developer.android.com/google/play/vitals/stuck-wakelock
url: https://developer.android.com/google/play/vitals/stuck-wakelock
source: md.txt
---

> Documentation index: https://developer.android.com/google/play/vitals/llms.txt

Partial wake locks are a mechanism in the [`PowerManager`](https://developer.android.com/reference/android/os/PowerManager.md.txt) API that lets
developers keep the CPU running after a device's display turns off. A partial
wake lock becomes *stuck* if it is held for a long time while your app is
running in the background (no part of your app is visible to the user).

> [!NOTE]
> **Note:** For information on how to diagnose and resolve this issue, see [Stuck partial wake locks](https://developer.android.com/topic/performance/issues/stuck-wakelock.md.txt).

## Detect the problem

### Android vitals

Android vitals can help improve your app's performance by alerting you in the
[Play Console](https://play.google.com/console/) when your app exhibits stuck partial wake locks. Android
vitals reports a partial wake lock as stuck when it lasts at least one hour in
the background within a 24-hour period.

The number of battery sessions displayed is an aggregate for all measured users
of the app. For information on how Google Play collects Android vitals data, see
the [Play Console documentation](https://support.google.com/googleplay/android-developer/answer/7385505).