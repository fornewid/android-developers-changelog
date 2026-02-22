---
title: https://developer.android.com/training/testing/instrumented-tests/performance
url: https://developer.android.com/training/testing/instrumented-tests/performance
source: md.txt
---

# Performance tests

App runtime performance can be divided into local testing and field testing. Keep in mind that both of these areas provide different results and metrics. As long as the results are in itself conclusive, that divergence is acceptable.

## Field testing

Field testing helps you to understand how an app performs with real users under real world conditions. It is an important area and helps to understand how an app performs in the field. You can use tools such as[Google Play Vitals](https://developer.android.com/topic/performance/vitals)and[Firebase Performance Monitoring](https://firebase.google.com/docs/perf-mon)to get field metrics from users.

You can use the[AndroidX Tracing](https://developer.android.com/jetpack/androidx/releases/tracing)library to add trace points which provides more context and insights to field metrics.

You can also use[`ApplicationStartInfo`](https://developer.android.com/reference/android/app/ApplicationStartInfo)and[`ApplicationExitInfo`](https://developer.android.com/reference/android/app/ApplicationExitInfo)to get more detailed information on application start and exit from users.

The[AndroidX JankStats](https://developer.android.com/topic/performance/jankstats)library enables aggregating and reporting of slow and dropped frames for further analysis.

## Local testing

To locally test the runtime performance of an app we provide the benchmarking library. It is divided into the[macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)library, which can be used to test the performance of entire user flows and the[microbenchmark](https://developer.android.com/topic/performance/benchmarking/microbenchmark-overview)library, which is used to analyze hot loop performance of an application or library.

All performance tests should run on a physical device. This is the only way to ensure that the performance you're measuring is the actual performance occurring on a device. Runtime performance tests will produce different results depending on the device they run on and how busy the device is.

Application performance can regress. To avoid regressions it's important to run performance tests frequently. In an ideal scenario an app is benchmarked every time a new feature is added or code is merged into the main branch. The bare minimum of performance monitoring is to benchmark release candidates and verify that startup time and frame timing does not regress for major user journeys. We recommend you run benchmarks whenever possible, such as before merging a feature to the main branch or for nightly builds.

## Use the results

Performance testing is an ongoing process. We recommend that you store results of performance tests in a way that they can be compared over time.

You can use results of performance tests in several ways.

- Performance improvement - Use measurement results to prioritize performance improvement
- Regression avoidance - Ensure there are no performance regressions with new releases
- Production monitoring - Understand whether there are issues you're not seeing during development

To learn more about Android runtime performance testing, see the[guide to app performance](https://developer.android.com/performance).