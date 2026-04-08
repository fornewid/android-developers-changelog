---
title: Improve performance  |  App quality  |  Android Developers
url: https://developer.android.com/topic/performance/improving-overview
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App quality](https://developer.android.com/quality)
* [Technical quality](https://developer.android.com/quality/technical)

# Improve performance Stay organized with collections Save and categorize content based on your preferences.




Users expect apps to be responsive and fast, from app startup and throughout the
entire app experience. After you [inspect](/topic/performance/inspecting-overview) your app for performance problems,
you can fix any issues and improve your app's performance.

## Tools and libraries

Android provides multiple tools and libraries to continually improve the
performance of your app in production, where it matters the most.

### R8: the Android app optimizer

R8 helps streamline your app by removing unused code and resources, rewriting
code to optimize runtime performance, and more. To learn how to enable it, see
[Enable app optimization](/topic/performance/app-optimization/enable-app-optimization).

For details of R8 behavior changes across Android Gradle Plugin (AGP) versions,
see [AGP and R8 version behavior changes](/topic/performance/app-optimization/enable-app-optimization#agp-r8-behavior-changes).

### Baseline Profiles

Implement Baseline Profiles into your app or library for the most efficient way
to improve performance. It can significantly optimize app startup time, reduce
slow rendering, and improve performance for end users. To learn more, see
[Baseline Profiles](/topic/performance/baselineprofiles).

### Startup profiles

Startup profiles is an experimental feature that is similar to Baseline
Profiles, but is applied differently and has distinct benefits. Whereas a
Baseline Profile optimizes performance as the app is installed on a device, a
startup profile is applied at compile-time. It gives the R8 shrinker hints to
group commonly used classes together within the DEX file. This can reduce page
faults during app startup, and therefore improve startup times. To learn more,
see [DEX layout optimizations and startup profiles](/topic/performance/baselineprofiles/dex-layout-optimizations).

### App Startup library

The [App Startup library](/topic/libraries/app-startup) lets you further optimize the app startup
experience. Both library developers and app developers can use the App Startup
library to streamline startup sequences and optimize startup operations.

## Optimize for low-RAM devices

Performance improvements begin from the ground-up. By optimizing for entry-level
devices, you can improve efficiency across all device categories. Users are more
likely to encounter issues such as app startup latency, application not
responding (ANRs), or app crashes when using memory-constrained devices.
Develop, test, and benchmark your app with this market segment in mind to create
a performant foundation for your app to build upon.

[Android (Go edition)](/guide/topics/androidgo) is a configuration of the Android platform OS, which
provides an optimized experience for low-RAM devices. To learn more about
improving stability and performance for entry-level devices, see [Optimize for
Android (Go edition)](/guide/topics/androidgo/optimize).

## Solve common problems

If the available tools or libraries don't resolve your performance issues, we
recommend checking for common problems and solutions in any of these categories:

* [App startup](/topic/performance/vitals/launch-time)
* [Slow rendering](/training/articles/perf-anr)
* [Memory](/topic/performance/memory-overview)
* [Battery and power](/training/monitoring-device-state/doze-standby)
* [App size](/topic/performance/reduce-apk-size)

## Additional resources

* [Use R8 to shrink, optimize, and fast-track your app](https://android-developers.googleblog.com/2025/11/use-r8-to-shrink-optimize-and-fast.html)
* [Background work overview](/guide/background)
* [Performance class](/topic/performance/performance-class)
* [App Standby Buckets](/topic/performance/appstandby)
* [App hibernation](/topic/performance/app-hibernation)