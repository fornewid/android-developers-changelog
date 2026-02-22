---
title: https://developer.android.com/topic/performance/tracing/profiling-manager/will-my-profile-always-be-collected
url: https://developer.android.com/topic/performance/tracing/profiling-manager/will-my-profile-always-be-collected
source: md.txt
---

There are multiple situations where the profile collection might not go as expected:

- The profile collection fails due to an internal error. If this happens, the[`ProfilingResult`](https://developer.android.com/reference/android/os/ProfilingResult)API tells you about the errors.
- The profile collection fails due to rate limiting. For more information, see[How rate limiting works](https://developer.android.com/topic/performance/tracing/profiling-manager/will-my-profile-always-be-collected#how-rate-limiting-works)
- The profile collection succeeds, but the app isn't immediately notified. This can happen if the app crashes during long profile collections. If the app closes, the system automatically stops and saves the profile. The app is informed about the collected profile when it restarts and registers a general listener with`ProfilingManager`.

## How rate limiting works

`ProfilingManager`includes a rate limiter for both individual apps and the entire system. The rate limiter prevents apps from using too many system resources by recording too many profiles, because a full profiling session uses a lot of resources.
| **Key Point:** You can tell if your app has been rate-limited by checking the`ProfilingResult`. You will see either the`ERROR_FAILED_RATE_LIMIT_PROCESS`or`ERROR_FAILED_RATE_LIMIT_SYSTEM`error.

Both the app and system rate limiters assign a cost to each type of profile collected, because some profiles are more resource-intensive than others. The app limiter controls how much an individual app can record based on its total cost. The system limiter, however, controls the total cost of all profiles recorded by all apps.

The rate limiter sets a total cost that each app can use (this cost is the same for all apps). Each profile uses a part of this total cost, depending on its type.

The rate limiter uses three time periods:

- **Per Hour:**There's a maximum cost allowed per hour.
- **Per Day:**There's a maximum cost allowed per day.
- **Per Week:**There's a maximum cost allowed per week.

The rate limiter sets a total cost that can be used within each of these periods. For example, an app might be allowed to record X profiles per hour, Y per day, and Z per week. If your app reaches its limit in any of these periods, future profile requests will result in an`ERROR_FAILED_RATE_LIMIT_PROCESS`error.

These time periods work similarly for system-level rate limiting. However, the system rate limiter is a global limit shared by all apps. This limit is set separately from the individual app quotas, but every profile contributes to it, using the same hourly, daily, and weekly periods. If this global limit is reached, you will receive the`ERROR_FAILED_RATE_LIMIT_SYSTEM`error.
| **Tip:** For local profiling, you can[disable the rate limiter](https://developer.android.com/topic/performance/tracing/profiling-manager/debug-mode#disable-rate-limiter).