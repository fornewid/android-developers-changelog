---
title: https://developer.android.com/topic/performance/tracing/profiling-manager/will-my-profile-always-be-collected
url: https://developer.android.com/topic/performance/tracing/profiling-manager/will-my-profile-always-be-collected
source: md.txt
---

A profile request might not complete or deliver results immediately in the
following situations:

- **Rate limiting** : Collection is throttled to protect device performance (see [How rate limiting works](https://developer.android.com/topic/performance/tracing/profiling-manager/will-my-profile-always-be-collected#how-rate-limiting-works)).
- **App termination before delivery** : If your app closes or crashes during
  capture, the system stops and saves the profile in the background and
  [delivers the queued result](https://developer.android.com/topic/performance/tracing/profiling-manager/trigger-based-capture#callback-lifecycle) the next time your app runs (in the
  foreground or background) and registers a global listener. The system
  retains undelivered queued results for up to 7 days awaiting listener
  registration; if your app doesn't register a listener within 7 days, the
  queued result is discarded.

  > [!NOTE]
  > **Note:** Once delivered to your app's storage directory, files not deleted by your app are [automatically cleaned up after 5 days](https://developer.android.com/topic/performance/tracing/profiling-manager/upload-worker#storage-and-cleanup) on recent `Profiling` module versions.

- **Other errors** : If collection fails (for example, due to an invalid
  request or an internal error), [`ProfilingResult`](https://developer.android.com/reference/android/os/ProfilingResult) reports the error
  code and message.

## How rate limiting works

Because capturing profiles is resource-intensive, `ProfilingManager` enforces
rate limiting at both the process level and the system level to protect device
performance and battery life. Different profile types carry different resource
costs, and the system tracks quotas over rolling time windows at two levels:

- **Process rate limiting** : Tracks the resource cost of profiles collected by your individual app against a per-app quota. Each app receives the same quota, and profiling activity from other apps on the device doesn't affect your app's limit. If your app reaches its quota for any time window, requests fail with [`ERROR_FAILED_RATE_LIMIT_PROCESS`](https://developer.android.com/reference/android/os/ProfilingResult#ERROR_FAILED_RATE_LIMIT_PROCESS).
- **System rate limiting** : Tracks the combined resource cost of profiles collected across all apps on the device against a shared global quota. Because all apps contribute to this device-wide limit, a request can fail with [`ERROR_FAILED_RATE_LIMIT_SYSTEM`](https://developer.android.com/reference/android/os/ProfilingResult#ERROR_FAILED_RATE_LIMIT_SYSTEM) even when your app hasn't exhausted its own process quota.

> [!IMPORTANT]
> **Key Point:** For app-driven [`requestProfiling`](https://developer.android.com/topic/performance/tracing/profiling-manager/how-to-capture) calls, inspect the `ProfilingResult` error code for `ERROR_FAILED_RATE_LIMIT_PROCESS` or `ERROR_FAILED_RATE_LIMIT_SYSTEM` to check whether a request was throttled by your app's quota or by device-wide activity. When a [trigger](https://developer.android.com/topic/performance/tracing/profiling-manager/trigger-based-capture) is throttled by a per-trigger cooldown or system rate limits (or when no background trace is active), the system drops the trigger silently without invoking `registerForAllProfilingResults` (when testing locally, check [`adb shell dumpsys profiling_service`](https://developer.android.com/topic/performance/tracing/profiling-manager/debug-mode#introspect-service-state)).

## Manage profile volume in production

Because device-level rate limits depend on profile type and overall system
activity, don't try to track or predict exact local rate-limit quotas inside
your app. Instead, focus on making the profiling request when a relevant user
journey or anomaly occurs and let `ProfilingManager` handle on-device
throttling.

To maximize coverage in the field while keeping upload bandwidth and storage
costs manageable, control your overall profile volume using **population
segmentation and experimentation platforms** (such as remote configuration or
A/B testing flags):

- **Sample across your user base**: Enable profiling for a small, random percentage of user sessions rather than requesting profiles from every user on every run.
- **Segment by cohort**: Target specific app versions, device tiers, OS releases, or regions where you're investigating a regression (for example, enabling Java heap dump collection on low-RAM devices experiencing elevated OOM rates).
- **Segment triggers and direct requests across users** : Assign different [profiling triggers](https://developer.android.com/topic/performance/tracing/profiling-manager/trigger-based-capture) and [direct profiling requests](https://developer.android.com/topic/performance/tracing/profiling-manager/how-to-capture) to separate user segments so that some users record one profile while others record a different one. Because all captures on a device share the same per-app quota, isolating them across user segments prevents higher-frequency triggers or requests from exhausting the quota needed by lower-frequency captures on a single device.

> [!TIP]
> **Tip:** When testing and debugging on a local device, you can [disable the rate
> limiter](https://developer.android.com/topic/performance/tracing/profiling-manager/debug-mode#disable-rate-limiter) so every profiling request is fulfilled.