---
title: https://developer.android.com/topic/performance/benchmarking/benchmarking-overview
url: https://developer.android.com/topic/performance/benchmarking/benchmarking-overview
source: md.txt
---

Benchmarking is a way to inspect and monitor the performance of your app. You
can regularly run benchmarks to analyze and debug performance problems and help
ensure that you don't introduce regressions in recent changes.

Android offers the Macrobenchmark library for analyzing and
testing different kinds of situations in your app.

## Macrobenchmark

The [Macrobenchmark](https://developer.android.com/studio/profile/macrobenchmark) library measures larger end-user interactions, such as
startup, interacting with the UI, and animations. The library provides direct
control over the performance environment you're testing. It lets you control
compiling and lets you start and stop your app to directly measure actual app
startup or scrolling.

The Macrobenchmark library injects events and monitors results externally from a
test app that is built with your tests. Therefore, when writing the benchmarks,
you don't call your app code directly and instead navigate within your app as a
user.

## Additional resources

### Views content

- [Benchmark your app (Views)](https://developer.android.com/topic/performance/views/benchmarking/benchmarking-overview-views)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Create Baseline Profiles {:#creating-profile-rules}](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile)
- [JankStats Library](https://developer.android.com/topic/performance/jankstats)
- [Overview of measuring app performance](https://developer.android.com/topic/performance/measuring-performance)