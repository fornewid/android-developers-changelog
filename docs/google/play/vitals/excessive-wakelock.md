---
title: https://developer.android.com/google/play/vitals/excessive-wakelock
url: https://developer.android.com/google/play/vitals/excessive-wakelock
source: md.txt
---

Partial wake locks are a mechanism in the [`PowerManager`](https://developer.android.com/reference/android/os/PowerManager) API that lets
developers keep the CPU running after a device's display turns off (whether due
to system timeout or the user pressing the power button). Excessive use of
partial wake locks drains the device's battery because it prevents the device
from entering lower power states.

> [!NOTE]
> **Note:** For information on how to diagnose and resolve this issue, see [Excessive partial wake locks](https://developer.android.com/topic/performance/issues/excessive-wakelock).

## Detect the problem

### Android vitals

Android vitals can help improve your app's performance by [alerting you via the
Play Console](https://support.google.com/googleplay/android-developer/answer/9844486) when your app's use of partial wake locks is
excessive.

Android vitals reports partial wake lock use as **excessive** when **all of the
partial wake locks** , added together, run for 2 or more hours in a 24-hour
period. Android vitals tracks wake lock duration only if the wake lock
is held when the app is in the background or is running a foreground service.
Currently, Android vitals exempts wake locks created by [audio](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#audio),
[location](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#location), and [JobScheduler](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#job) user-initiated APIs
from the wake lock calculation.

The Android vitals excessive partial wake lock dashboard provides breakdowns of
non-exempted wake lock names associated with your app, showing affected
sessions and durations.

> [!NOTE]
> **Note:** Android vitals gives some exemptions to partial wake lock usage in scenarios where there is a clear user benefit of the partial wake lock, and there's no better way to achieve that result without the partial wake lock. For example, if an app is playing audio for the user, there's a clear benefit to keeping the device awake and there's no way to play the audio without keeping the device awake. In that case, the partial wake lock time is not counted against the Android vitals.

If excessive partial wake locks occur in more than 5% of app sessions across all
devices in a 28-day period, it can affect your app's visibility on Play.