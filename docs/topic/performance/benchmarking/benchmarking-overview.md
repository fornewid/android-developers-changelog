---
title: https://developer.android.com/topic/performance/benchmarking/benchmarking-overview
url: https://developer.android.com/topic/performance/benchmarking/benchmarking-overview
source: md.txt
---

Benchmarking is a way to inspect and monitor the performance of your app. You
can regularly run benchmarks to analyze and debug performance problems and help
ensure that you don't introduce regressions in recent changes.

Android offers two benchmarking libraries and approaches for analyzing and
testing different kinds of situations in your app: Macrobenchmark and
Microbenchmark.

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

## Microbenchmark

The [Microbenchmark](https://developer.android.com/studio/profile/benchmark) library lets you benchmark app code directly in a loop.
This is designed for measuring CPU work that assesses best-case performance---such
as warmed up Just in Time (JIT) and disk accesses cached---that you might see with
an inner-loop or a specific hot function. ​​The library can only measure the
code that you can call directly in isolation.

If your app needs to process a complex data structure, or have some specific
computation-heavy algorithm that is called multiple times during the app run,
these might be good cases for benchmarking. You can also measure parts of your
UI. For example, you can measure the cost of the `RecyclerView` item binding,
how long it takes to inflate a layout, or how demanding the layout-and-measure
pass of your `View` class is from a performance perspective.

However, you aren't able to measure how the benchmarked cases contribute to the
overall user experience. In some scenarios, benchmarking doesn't tell you if
you're improving a bottleneck like jank or app startup time. For this reason,
it's crucial to identify those bottlenecks first with the [Android Profiler](https://developer.android.com/studio/profile).
After you find the code you want to investigate and optimize, the benchmarked
loop can run repeatedly in a quick and easier fashion to create less noisy
results, which lets you focus on one area of improvement.

The Microbenchmark library only reports information about your app, not about
the system overall. Therefore, it's best at analyzing performance of situations
specific to the app, not ones that might relate to overall system issues.

## Benchmark library comparison

|   | Macrobenchmark | Microbenchmark |
|---|---|---|
| API version | 23 and later | 14 and later |
| Function | Measure high-level entry points or interactions, such as activity launch or scrolling a list. | Measure individual functions. |
| Scope | Out-of-process test of full app. | In-process test of CPU work. |
| Speed | Medium iteration speed. It can exceed a minute. | Fast iteration speed. Often less than 10 seconds. |
| Tracing | Results come with profiling traces. | Optional method sampling and tracing. |

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Create Baseline Profiles {:#creating-profile-rules}](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile)
- [JankStats Library](https://developer.android.com/topic/performance/jankstats)
- [Overview of measuring app performance](https://developer.android.com/topic/performance/measuring-performance)