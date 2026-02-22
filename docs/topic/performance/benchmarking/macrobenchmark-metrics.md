---
title: https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics
url: https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics
source: md.txt
---

Metrics are the main type of information extracted from your benchmarks. They
are passed to the [`measureRepeated`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/junit4/MacrobenchmarkRule#measureRepeated(kotlin.String,kotlin.collections.List,androidx.benchmark.macro.CompilationMode,androidx.benchmark.macro.StartupMode,kotlin.Int,kotlin.Function1,kotlin.Function1))
function as a `List`, which lets you specify
multiple measured metrics at once. At least one type of metric is required for
the benchmark to run.

The following code snippet captures frame timing and custom trace section
metrics:  

### Kotlin

```kotlin
benchmarkRule.measureRepeated(
    packageName = TARGET_PACKAGE,
    metrics = listOf(
        FrameTimingMetric(),
        TraceSectionMetric("RV CreateView"),
        TraceSectionMetric("RV OnBindView"),
    ),
    iterations = 5,
    // ...
)
```

### Java

```java
benchmarkRule.measureRepeated(
    TARGET_PACKAGE,     // packageName
    Arrays.asList(      // metrics
        new StartupTimingMetric(),
        new TraceSectionMetric("RV CreateView"),
        new TraceSectionMetric("RV OnBindView"),
    ),
    5,                  // Iterations
    // ...
);
```

In this example, [`RV CreateView`](https://cs.android.com/search?q=TRACE_CREATE_VIEW_TAG&sq&ss=androidx/platform/frameworks/support)
and [`RV OnBindView`](https://cs.android.com/search?q=TRACE_BIND_VIEW_TAG)
are the IDs of traceable blocks that are defined in
[`RecyclerView`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView). The
[source code for the `createViewHolder()`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:recyclerview/recyclerview/src/main/java/androidx/recyclerview/widget/RecyclerView.java;l=7950-7964)
method is an example of how you can define traceable blocks within your own
code.

[`StartupTimingMetric`](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics#startup-timing), [`TraceSectionMetric`](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics#trace-section), [`FrameTimingMetric`](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics#frame-timing),
and [`PowerMetric`](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics#power), are covered in detail later in this document.
For a full list of metrics, check out subclasses of [`Metric`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/Metric).

Benchmark results are output to Android Studio, as shown in figure 1.
If multiple metrics are defined, all of them are combined in the output.
![Results of TraceSectionMetric and FrameTimingMetric.](https://developer.android.com/static/topic/performance/images/benchmark_images/macrobenchmark_results_frames_tracing.png) **Figure 1.** Results of `TraceSectionMetric` and `FrameTimingMetric`.

## StartupTimingMetric

[`StartupTimingMetric`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/StartupTimingMetric)
captures app startup timing metrics with the following values:

- `timeToInitialDisplayMs`: The amount of time from when the system receives a launch intent to when it renders the first frame of the destination [`Activity`](https://developer.android.com/reference/android/app/Activity).
- `timeToFullDisplayMs`: The amount of time from when the system receives a launch intent to when the app reports fully drawn using the [`reportFullyDrawn()`](https://developer.android.com/reference/android/app/Activity#reportFullyDrawn()) method. The measurement stops at the completion of rendering the first frame after---or containing---the `reportFullyDrawn()` call. This measurement might not be available on Android 10 (API level 29) and earlier.

`StartupTimingMetric` outputs the min, median, and max values from the startup
iterations. To assess startup improvement you should focus on median values,
since they provide the best estimate of the typical startup time. For more
information about what contributes to app startup time, see [App startup
time](https://developer.android.com/topic/performance/vitals/launch-time).
![StartupTimingMetric results](https://developer.android.com/static/topic/performance/images/benchmark_images/macrobenchmark_results_fully_drawn_startup.png) **Figure 2.** `StartupTimingMetric` results.

## FrameTimingMetric

[`FrameTimingMetric`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/FrameTimingMetric)
captures timing information from frames produced by a benchmark, such as a
scrolling or animation, and outputs the following values:

- `frameOverrunMs`: the amount of time a given frame misses its deadline by. Positive numbers indicate a dropped frame and visible jank or stutter. Negative numbers indicate how much faster a frame is than the deadline. Note: This is available only on Android 12 (API level 31) and higher.
- `frameDurationCpuMs`: the amount of time the frame takes to be produced on the CPU on both the UI thread and the `RenderThread`.

These measurements are collected in a distribution of 50th, 90th, 95th, and 99th
percentile.

For more information on how to identify and improve slow frames, see
[Slow rendering](https://developer.android.com/topic/performance/vitals/render).
![FrameTimingMetric results](https://developer.android.com/static/topic/performance/images/benchmark_images/macrobenchmark_results_frames.png) **Figure 3.** `FrameTimingMetric` results.

## TraceSectionMetric

| **Experimental:** This class is experimental.

[`TraceSectionMetric`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/TraceSectionMetric)
captures the number of times a trace section matching the provided `sectionName`
occurs and the amount of time it takes. For the time, it outputs the minimum,
median, and maximum times in milliseconds. The trace section is defined either
by the function call
[`trace(sectionName)`](https://developer.android.com/reference/kotlin/androidx/tracing/package-summary#trace(kotlin.String,kotlin.Function0))
or the code between
[`Trace.beginSection(sectionName)`](https://developer.android.com/reference/kotlin/androidx/tracing/Trace#beginSection(java.lang.String))
and
[`Trace.endSection()`](https://developer.android.com/reference/kotlin/androidx/tracing/Trace#endSection()) or
their async variants. It always selects the first instance of a trace section
captured during a measurement. It only outputs trace sections from your package
by default; to include processes outside your package, set
`targetPackageOnly = false`.

For more information about tracing, see [Overview of system
tracing](https://developer.android.com/topic/performance/tracing) and [Define custom
events](https://developer.android.com/topic/performance/tracing/custom-events).
![TraceSectionMetric](https://developer.android.com/static/topic/performance/images/benchmark_images/macrobenchmark_results_tracing.png) **Figure 4.** `TraceSectionMetric` results.

## PowerMetric

| **Experimental:** This class is experimental.

[`PowerMetric`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/PowerMetric) captures
the change in power or energy over the duration of your test for the provided
[power categories](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/PowerCategory).
Each selected category is broken down into its measurable subcomponents, and
unselected categories are added to the "unselected" metric.

These metrics measure
system-wide consumption, not the consumption on a per-app basis, and are limited
to Pixel 6, Pixel 6 Pro, and later devices:

- `power<category>Uw`: the amount of power consumed over the duration of your test in this category.
- `energy<category>Uws`: the amount of energy transferred per unit of time for the duration of your test in this category.

Categories include the following:

- `CPU`
- `DISPLAY`
- `GPU`
- `GPS`
- `MEMORY`
- `MACHINE_LEARNING`
- `NETWORK`
- `UNCATEGORIZED`

With some categories, like `CPU`, it might be difficult to separate work done by
other processes from work done by your own app. To minimize the interference,
remove or restrict unnecessary apps and accounts.
![PowerMetric results](https://developer.android.com/static/topic/performance/images/benchmark_images/macrobenchmark_results_power.png) **Figure 5.** `PowerMetric` results.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Create Baseline Profiles {:#creating-profile-rules}](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile)
- [Writing a Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)
- [App startup analysis and optimization {:#app-startup-analysis-optimization}](https://developer.android.com/topic/performance/appstartup/analysis-optimization)