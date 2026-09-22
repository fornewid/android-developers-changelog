---
title: https://developer.android.com/topic/performance/issues/excessive-wakelock
url: https://developer.android.com/topic/performance/issues/excessive-wakelock
source: md.txt
---

Partial wake locks are a mechanism in the [`PowerManager`](https://developer.android.com/reference/android/os/PowerManager) API that lets
developers keep the CPU running after a device's display turns off (whether due
to system timeout or the user pressing the power button). Your app acquires a
partial wake lock by calling [`acquire()`](https://developer.android.com/reference/android/os/PowerManager.WakeLock#acquire()) with the [`PARTIAL_WAKE_LOCK`](https://developer.android.com/reference/android/os/PowerManager#PARTIAL_WAKE_LOCK)
flag, or by using [other APIs that acquire wake locks](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls).
Excessive use of partial wake locks drains the device's battery because it
prevents the device from entering lower power states. Partial wake locks should
be used only when necessary and released as soon as no longer needed.

If your app uses partial wake locks excessively, you can use the guidance in
this page to diagnose and fix the problem.

> [!NOTE]
> **Note:** For information on how Android Play Vitals tracks and reports this issue, see [Excessive partial wake locks in Android vitals](https://developer.android.com/google/play/vitals/excessive-wakelock).

## Fix the problem

Because wake locks can drain the device battery, you shouldn't use wake
locks if there's an alternative. The
[Choose the right API to keep the device awake](https://developer.android.com/develop/background-work/background-tasks/awake)
documentation can help you find the best solution for your app.

If you do need to use a wake lock, [follow wake lock best practices](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/best-practices)
to make sure your wake locks don't hurt device efficiency. In particular,
make sure every device you acquire is released, and release the lock as quickly
as possible.

Your app might also be using wake locks even if you aren't acquiring
the wake lock explicitly.
If you see wake locks attributed to the app that you don't recognize,
[identify wake locks created by other APIs](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls)
can help you identify the APIs that might have created them.

After fixing the problem in code, you can verify your fixes by using [local
wake lock debugging tools](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/debug-locally).

## See also

- [Stuck partial wake locks](https://developer.android.com/topic/performance/issues/stuck-wakelock)
- [Choose the right API to keep the device awake](https://developer.android.com/develop/background-work/background-tasks/awake)
- [Wake lock documentation](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Frozen frames](https://developer.android.com/topic/performance/issues/render#frozen-frames)
- [Run benchmarks in Continuous Integration](https://developer.android.com/topic/performance/benchmarking/benchmarking-in-ci)
- [Create and measure Baseline Profiles without Macrobenchmark](https://developer.android.com/topic/performance/baselineprofiles/manually-create-measure)