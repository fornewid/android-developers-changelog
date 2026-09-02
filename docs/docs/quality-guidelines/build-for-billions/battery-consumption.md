---
title: https://developer.android.com/docs/quality-guidelines/build-for-billions/battery-consumption
url: https://developer.android.com/docs/quality-guidelines/build-for-billions/battery-consumption
source: md.txt
---

# Battery consumption for billions

Access to reliable power supplies varies, and outages can disrupt planned charges. Defend your users' batteries against unnecessary drain by benchmarking your battery use, avoiding wakelocks, scheduling tasks, and monitoring sensor requests.

## Reduce battery consumption

There are several steps you can take to help make sure that your app is only consuming battery power when it needs to, and that it's not consuming more power than necessary.

- Your app should minimize its activity when in the background and when the device is running on battery power.
- Sensors, such as GPS sensors, can drain battery significantly. Avoid issues by using the[`FusedLocationProvider`](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderApi)API to manage the underlying location technology. It provides a simple API so that you can specify requirements---such as high accuracy or low power---at a high level. It also optimizes the device's use of battery power by caching locations and batching requests across apps. For more information about the ideal ways to request location, see the[Getting the Last Known Location](https://developer.android.com/training/location/retrieve-current)training guide.
- [Wake locks](https://developer.android.com/reference/android/os/PowerManager.WakeLock)are mechanisms to keep devices on so that they can perform background activities. Avoid using wake locks because they prevent the device from going into low-power states.
- To reduce the number of device wake-ups, batch network activity. For more information on batching, see the Android training on[Optimizing Downloads for Efficient Network Access](https://developer.android.com/training/efficient-downloads/efficient-network-access).
- [WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager)schedules tasks and lets the system batch operations. This greatly simplifies the implementation of common patterns, such as waiting for network connectivity, device charging state, retries, and backoff. Use WorkManager to perform non-essential background activity when the device is charging and is connected to an unmetered network.
- For more information on how network activity can drain the battery, and how to tackle this issue, see[Reducing Network Battery Drain](https://developer.android.com/topic/performance/power/network).

## Benchmark battery use

Benchmarking your app's battery use in a controlled environment helps you understand the battery-heavy tasks in your app. It's a good practice to benchmark your app's battery use to gauge efficiency and track changes over time.[Batterystats](https://developer.android.com/tools/performance/batterystats-battery-historian)collects battery data about your apps, and[Battery Historian](https://developer.android.com/tools/performance/batterystats-battery-historian)converts that data into an HTML visualization.

For more information on reducing battery use, see the Android training on[Optimizing Battery Life](https://developer.android.com/training/monitoring-device-state).

## Related