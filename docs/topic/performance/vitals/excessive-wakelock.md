---
title: https://developer.android.com/topic/performance/vitals/excessive-wakelock
url: https://developer.android.com/topic/performance/vitals/excessive-wakelock
source: md.txt
---

# Excessive partial wake locks

Partial wake locks are a mechanism in the[`PowerManager`](https://developer.android.com/reference/android/os/PowerManager)API that lets developers keep the CPU running after a device's display turns off (whether due to system timeout or the user pressing the power button). Your app acquires a partial wake lock by calling[`acquire()`](https://developer.android.com/reference/android/os/PowerManager.WakeLock#acquire())with the[`PARTIAL_WAKE_LOCK`](https://developer.android.com/reference/android/os/PowerManager#PARTIAL_WAKE_LOCK)flag, or by using[other APIs that acquire wake locks](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls). Excessive use of partial wake locks drains the device's battery because it prevents the device from entering lower power states. Partial wake locks should be used only when necessary and released as soon as no longer needed.

If your app uses partial wake locks excessively, you can use the guidance in this page to diagnose and fix the problem.

## Detect the problem

Android vitals can help you find out when your app's use of partial wake locks is excessive.

### Android vitals

Android vitals can help improve your app's performance by[alerting you via the Play Console](https://support.google.com/googleplay/android-developer/answer/9844486)when your app's use of partial wake locks is excessive.

Android vitals reports partial wake lock use as**excessive** when**all of the partial wake locks** , added together, run for 2 or more hours in a 24-hour period. Android vitals tracks wake lock duration only if the wake lock is held when the app is in the background or is running a foreground service. Currently, Android vitals exempts wake locks created by[audio](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#audio),[location](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#location), and[JobScheduler](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls#job)user-initiated APIs from the wake lock calculation.

The Android vitals excessive partial wake lock dashboard provides breakdowns of non-exempted wake lock names associated with your app, showing affected sessions and durations.
| **Note:** Android vitals gives some exemptions to partial wake lock usage in scenarios where there is a clear user benefit of the partial wake lock, and there's no better way to achieve that result without the partial wake lock. For example, if an app is playing audio for the user, there's a clear benefit to keeping the device awake and there's no way to play the audio without keeping the device awake. In that case, the partial wake lock time is not counted against the Android vitals.

If excessive partial wake locks occur in more than 5% of app sessions across all devices in a 28-day period, it can affect your app's visibility on Play once the metric is out of beta.

Once you're aware that your app has excessive partial wake locks, your next step is to address the issue.

## Fix the problem

Because wake locks can drain the device battery, you shouldn't use wake locks if there's an alternative. The[Choose the right API to keep the device awake](https://developer.android.com/develop/background-work/background-tasks/awake)documentation can help you find the best solution for your app.

If you do need to use a wake lock,[follow wake lock best practices](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/best-practices)to make sure your wake locks don't hurt device efficiency. In particular, make sure every device you acquire is released, and release the lock as quickly as possible.

Your app might also be using wake locks even if you aren't acquiring the wake lock explicitly. If you see wake locks attributed to the app that you don't recognize,[identify wake locks created by other APIs](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls)can help you identify the APIs that might have created them.

After fixing the problem in code, you can verify your fixes by using[local wake lock debugging tools](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/debug-locally).

## See also

- [Stuck partial wake locks](https://developer.android.com/topic/performance/vitals/stuck-wakelock)
- [Choose the right API to keep the device awake](https://developer.android.com/develop/background-work/background-tasks/awake)
- [Wake lock documentation](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Frozen frames](https://developer.android.com/topic/performance/vitals/render#frozen-frames)
- [Run benchmarks in Continuous Integration](https://developer.android.com/topic/performance/benchmarking/benchmarking-in-ci)
- [Create and measure Baseline Profiles without Macrobenchmark](https://developer.android.com/topic/performance/baselineprofiles/manually-create-measure)