---
title: https://developer.android.com/topic/performance/benchmarking/microbenchmark-overview
url: https://developer.android.com/topic/performance/benchmarking/microbenchmark-overview
source: md.txt
---

# Microbenchmark

The Jetpack Microbenchmark library lets you benchmark your Android native
code---Kotlin or Java---from within Android Studio. The library handles warmup,
measures your code performance and allocation counts, and outputs benchmarking
results to both the [Android Studio console](https://developer.android.com/studio/profile/microbenchmark-write#benchmark-results) and a [JSON file](https://developer.android.com/studio/profile/benchmarking-in-ci#benchmark-data-example) with more
detail.

We recommend you [profile your code](https://developer.android.com/studio/profile) before writing a benchmark. This helps
you find expensive operations that are worth optimizing. It can also show why
the operations are slow by showing what is happening while they run, such as
running on a low-priority thread, sleeping due to disk access, or unexpectedly
calling into an expensive function, like bitmap decoding.

Microbenchmarks are most useful for CPU work that is run many times in your app,
also known as *hot code paths* . Good examples are `RecyclerView` scrolling with
one item shown at a time, data conversions or processing, and other pieces of
code that get used repeatedly.

Other types of code are more difficult to measure with the Microbenchmark
library. Because benchmarks run in a loop, any code that isn't run frequently or
performs differently when called multiple times might not be a good fit for
benchmarking.

To learn how to use the library in a Continuous Integration (CI) environment,
see [Run benchmarks in Continuous Integration](https://developer.android.com/studio/profile/benchmarking-in-ci).

## Avoid measuring cache

Try to avoid measuring just the cache. For example, a custom view's layout
benchmark might measure only the performance of the layout cache. To avoid this,
you can pass different layout parameters in each loop. In other cases, such as
when measuring file system performance, this might be difficult because the OS
caches the file system while in a loop.

## Obtain consistent benchmarks

Clocks on mobile devices dynamically change from high state, for performance, to
low state, to save power or when the device gets hot. These varying clocks can
make your benchmark numbers vary widely, so the library provides ways to deal
with this issue.

### Lock clocks (requires rooted device)

Locking clocks is the best way to get stable performance. It helps ensure that
clocks never get high enough to heat up the device, or low if a benchmark isn't
fully utilizing the CPU. It can be applied with a Gradle task
(`gradlew lockClocks`), or [manually in CI](https://developer.android.com/studio/profile/benchmarking-in-ci#clock-locking). While this is the best way to
help ensure stable performance, it isn't supported on most devices, due to
requiring a rooted Android-powered device.

### Sustained performance mode

[`Window.setSustainedPerformanceMode()`](https://developer.android.com/reference/android/view/Window#setSustainedPerformanceMode(boolean)) is a feature supported by devices
that let an app opt for a lower max CPU frequency. When running on supported
devices, the Microbenchmark library uses a combination of this API and launching
its own activity to both prevent thermal throttling and stabilize results.

This feature is enabled by default by the [`testInstrumentationRunner`](https://developer.android.com/training/testing/espresso/setup#set-instrumentation-runner) set
by the Android Gradle plugin. If you want to use a custom runner, you can
subclass the [`AndroidBenchmarkRunner`](https://developer.android.com/reference/kotlin/androidx/benchmark/junit4/AndroidBenchmarkRunner) and use it as your
`testInstrumentationRunner`.

The runner launches an opaque, fullscreen activity to ensure that the benchmark
runs in the foreground and without any other app drawing.

### Automatic execution pausing

If you don't use clock-locking or sustained performance, the library performs
automatic thermal throttling detection. When enabled, the internal benchmark
periodically runs to determine when the device temperature gets high enough to
lower CPU performance. When it detects lowered CPU performance, the library
pauses execution to let the device cool down and then retries the current
benchmark.

### AOT Compilation

Complex microbenchmarks can take a long time to stabilize, and make
stabilization very difficult to detect. As consistent measurement and fast
iteration speed are top priorities, the `androidx.benchmark` plugin fully
compiles your microbenchmark apk by default, similar to
[`CompilationMode.Full`](https://developer.android.com/reference/androidx/benchmark/macro/CompilationMode.Full) in Macrobenchmarks. This behavior requires Benchmark
`1.3.0-beta01+`, and Android Gradle Plugin `8.4.0+`. You can opt out of this
behavior by setting `androidx.benchmark.forceaotcompilation=false` in your
`gradle.properties` file.

## Samples

See the following samples in the GitHub repository:

- [Performance samples](https://github.com/android/performance-samples)
- [PagingWithNetworkSample](https://github.com/android/architecture-components-samples/tree/main/PagingWithNetworkSample/benchmark)
- [WorkManagerSample](https://github.com/android/architecture-components-samples/tree/main/WorkManagerSample/benchmark)

## Additional resources

- [Fighting regressions with Benchmarks in CI](https://medium.com/androiddevelopers/fighting-regressions-with-benchmarks-in-ci-6ea9a14b5c71)

## Provide feedback

To report issues or submit feature requests when using benchmarking, see the
[public issue
tracker](https://issuetracker.google.com/issues/new?component=585351).

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Benchmark your app](https://developer.android.com/topic/performance/benchmarking/benchmarking-overview)
- [Create Baseline Profiles {:#creating-profile-rules}](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile)
- [JankStats Library](https://developer.android.com/topic/performance/jankstats)