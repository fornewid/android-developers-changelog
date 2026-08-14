---
title: https://developer.android.com/topic/performance/tracing/choose-right-method
url: https://developer.android.com/topic/performance/tracing/choose-right-method
source: md.txt
---

You can collect profiles using two primary methods: manual profile collection
and the `ProfilingManager` API.

- Manual profile collection involves manually running Perfetto on your local device to record profiles. You can do this using commands as described in [Recording system traces with Perfetto](https://perfetto.dev/docs/getting-started/system-tracing) or by using the Quick Settings tile, as explained in [Record using Quick Settings tile](https://developer.android.com/topic/performance/tracing/on-device#quick-settings).
- `ProfilingManager` lets apps collect profiles in production.

We recommend using `ProfilingManager` for collecting and analyzing data from
many users or for debugging rare issues. However, for issues that are easier to
reproduce, manual profiling might be a better choice.

The following table shows how these two methods for recording profiles differ:

|   | **ProfilingManager** | **Manual profile collection** |
|---|---|---|
| Profile timing control | More | Less |
| Profile source | Local device and public users | Local device only |
| Profile output | Redacted | Unredacted |
| Event based profiling | Yes | No |
| Profile customizability | Less | More |
| Scalability | High | Low |

The following sections briefly describe the differences between the profile
recording methods.

## Profile timing control

The `ProfilingManager` API provides more control over when an app starts or
stops a profile compared to manual profiling, where timing profile
initialization might be difficult. `ProfilingManager` also makes it easier to
profile unexpected behavior because you can collect a profile even if you cannot
reproduce the behavior locally.

## Profile source

With `ProfilingManager`, you can gather data from public users to find and fix
performance issues. In contrast, manual profiling only lets you reproduce issues
on your own device.

## Profile output

`ProfilingManager` and manual collection produce different types of profile
outputs:

- `ProfilingManager` produces redacted traces. Redacted traces show
  information about your app's process but hide data from other apps on the
  system. Because `ProfilingManager` collects and redacts before returning
  them, you can collect traces from public users while protecting their
  privacy by not showing data from other apps.

- Manual profile collection produces unredacted traces. When you manually
  record a system trace, the output might include all processes running on the
  system. While these unredacted traces offer more complete data for
  debugging, you can only access them locally due to privacy concerns.

## Event-based profiling

`ProfilingManager` can also collect profiles when specific events happen, such
as an Application Not Responding (ANR) error or app startup. `ProfilingManager`
will handle the starting and stopping of profiles for event-based collection.

## Profile customizability

Manual profiling provides the most customization, while `ProfilingManager`
offers fewer customization options.

## Scalability

`ProfilingManager` is the best way to scale tracing because it's the only option
that lets app developers record profiles from public users. With
`ProfilingManager`, you can set up large-scale trace collection and analysis.
Manual profiling is limited to local use.