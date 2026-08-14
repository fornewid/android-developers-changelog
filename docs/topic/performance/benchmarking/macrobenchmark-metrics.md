---
title: https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics
url: https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics
source: md.txt
---

Metrics are the main type of information extracted from your benchmarks. They
are passed to the [`measureRepeated`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/junit4/MacrobenchmarkRule#measureRepeated(kotlin.String,kotlin.collections.List,androidx.benchmark.macro.CompilationMode,androidx.benchmark.macro.StartupMode,kotlin.Int,kotlin.Function1,kotlin.Function1)) function as a `List`, which lets you
specify multiple measured metrics at once. At least one type of metric is
required for the benchmark to run.

The following code snippet captures frame timing and custom trace section
metrics for a Jetpack Compose lazy layout interface:

    @OptIn(ExperimentalMetricApi::class)
        @Test
        fun scrollComposeList() {
            benchmarkRule.measureRepeated(
                // [START_EXCLUDE]
                packageName = TARGET_PACKAGE,
                metrics = listOf(
                    FrameTimingMetric(),
                    // Measure power usage. This is supported on Pixel 6 and later.
                    PowerMetric(PowerMetric.Type.Power(
                        mapOf(
                            PowerCategory.CPU to PowerCategoryDisplayLevel.TOTAL,
                            PowerCategory.DISPLAY to PowerCategoryDisplayLevel.TOTAL,
                            PowerCategory.GPU to PowerCategoryDisplayLevel.TOTAL,
                            PowerCategory.NETWORK to PowerCategoryDisplayLevel.TOTAL,
                        )
                    )),
                    // Measure custom trace sections by name EntryRow (which is added to the EntryRow composable).
                    // Mode.Sum measures combined duration and also how many times it occurred in the trace.
                    // This way, you can estimate whether a composable recomposes more than it should.
                    TraceSectionMetric("EntryRowCustomTrace", TraceSectionMetric.Mode.Sum),
                    // This trace section takes into account the SQL wildcard character %,
                    // which can find trace sections without the full name.
                    // This way, you can measure composables produced by the composition tracing
                    // and measure how long they took and how many times they recomposed.
                    // WARNING: This metric only shows results when running with composition tracing, otherwise it won't be visible in the outputs.
                    TraceSectionMetric("%EntryRow%", TraceSectionMetric.Mode.Sum),
                ),
                // Try switching to different compilation modes to see the effect
                // it has on frame timing metrics.
                compilationMode = CompilationMode.None(),
                startupMode = StartupMode.WARM, // restarts activity each iteration
                iterations = DEFAULT_ITERATIONS,
                // [END_EXCLUDE]
                setupBlock = {
                    uiAutomator {
                        // Before starting to measure, navigate to the UI to be measured.
                        startIntent(Intent("$packageName.COMPOSE_ACTIVITY"))
                    }
                }
            ) {
                uiAutomator {
                    onElement { isScrollable }.fling(Direction.DOWN)
                }
            }
        }

In the following example, `EntryRowCustomTrace` represents a custom trace
section defined inside the composable item layers using the standard Kotlin
`trace(sectionName) { ... }` block wrapper. To provide data for
`TraceSectionMetric`, you must wrap the target UI components inside your
application's production codebase with the standard Jetpack runtime `trace`
block wrapper:

    @Composable
    private fun EntryRow(entry: Entry, modifier: Modifier = Modifier) = trace("EntryRowCustomTrace") {
        Card(modifier = modifier) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Text(
                    text = entry.contents,
                    modifier = Modifier
                        .padding(16.dp)
                        .wrapContentSize()
                )

                Spacer(modifier = Modifier.weight(1f))

                Checkbox(
                    checked = false,
                    onCheckedChange = {},
                    modifier = Modifier.padding(16.dp)
                )
            }
        }
    }

Benchmark results are output directly to the **Benchmark** terminal tab inside
Android Studio, as shown in Figure 1. If multiple metrics are defined, all their
computed data points are combined in the summary window.
![Results of TraceSectionMetric and FrameTimingMetric.](https://developer.android.com/static/topic/performance/images/benchmark_images/macrobenchmark_results_frames_tracing_rev.png) **Figure 1.** Combined console results of `TraceSectionMetric` and `FrameTimingMetric` for a modern Compose layout.

`StartupTimingMetric`, `FrameTimingMetric`, `TraceSectionMetric`, and
`PowerMetric` are covered in detail below. For a full list of available
benchmark metrics, see the subclasses of [`Metric`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/Metric) in the API
reference.

## StartupTimingMetric

[`StartupTimingMetric`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/StartupTimingMetric) captures app startup timing metrics with the
following values:

- `timeToInitialDisplayMs`: The amount of time from when the system receives a launch intent to when it renders the first frame of the destination screen.
- `timeToFullDisplayMs`: The amount of time from when the system receives a launch intent to when the app reports fully drawn using the internal platform reporting mechanisms. The measurement stops at the completion of rendering the first frame after---or containing---the fully drawn signal.

`StartupTimingMetric` outputs the minimum, median, and maximum values from the
startup iterations. To assess startup improvement, always focus on median
values, since they provide the best estimate of typical user startup times.

In a Compose-first architecture, don't attempt to invoke
`activity.reportFullyDrawn` manually. Instead, use the Compose-safe asynchronous
utilities [`ReportDrawn`](https://developer.android.com/reference/kotlin/androidx/activity/compose/ReportDrawn.composable#ReportDrawn()), [`ReportDrawnWhen`](https://developer.android.com/reference/kotlin/androidx/activity/compose/ReportDrawnWhen.composable), or [`ReportDrawnAfter`](https://developer.android.com/reference/kotlin/androidx/activity/compose/ReportDrawnAfter.composable)
inside your screen composables to automatically signal to Macrobenchmark when
your async network data or complex UI states have finished rendering.

For more information about analyzing and optimizing initialization performance,
see [App startup time](https://developer.android.com/topic/performance/vitals/launch-time).

## FrameTimingMetric

[`FrameTimingMetric`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/FrameTimingMetric) captures precise timing information from frames
produced by a benchmark journey, such as scrolling a list or a complex UI layout
animation, and outputs the following diagnostic values:

- `frameOverrunMs`: the amount of time a given frame misses its deadline by. Positive numbers indicate a dropped frame accompanied by visible jank or stutter. Negative numbers indicate how much faster a frame completed relative to the subsystem hardware deadline. Note: This metric is available only on Android 12 (API level 31) and later.
- `frameDurationCpuMs`: the amount of time the frame spent actively being produced on the CPU across both the main application UI thread and the Compose `RenderThread`.

These measurements are collected in a distribution of 50th, 90th, 95th, and 99th
percentiles:

    frameDurationCpuMs P50 3.5, P90 6.0, P95 6.4, P99 11.0
    frameOverrunMs P50 -11.6, P90 -7.2, P95 -7.1, P99 -1.2

When optimizing Jetpack Compose layout hierarchies, look at your
worst-performing frames (the P95 and P99 bounds). If `frameOverrunMs` spikes
into positive integers at the high percentiles, it indicates that recompositions
are stalling the main thread during heavy scroll animations.

For deeper insights into identifying and resolving slow frames, see [Jetpack
Compose Performance](https://developer.android.com/develop/ui/compose/performance).

## TraceSectionMetric

> [!WARNING]
> **Experimental:** This class is experimental.

[`TraceSectionMetric`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/TraceSectionMetric) captures the number of times a specific trace section
occurs and the absolute amount of time it takes to execute. For time tracking,
it outputs the minimum, median, and maximum times in milliseconds. The target
trace section is defined either by the function call [`trace(sectionName)`](https://developer.android.com/reference/kotlin/androidx/tracing/package-summary#trace(kotlin.String,kotlin.Function0))
or the lower-level block boundaries between
[`Trace.beginSection(sectionName)`](https://developer.android.com/reference/kotlin/androidx/tracing/Trace#beginSection(java.lang.String)) and [`Trace.endSection()`](https://developer.android.com/reference/kotlin/androidx/tracing/Trace#endSection()) or their
async variants.

    EntryRowCustomTraceCount min 20.0, median 28.0, max 50.0
    EntryRowCustomTraceSumMs min 34.9, median 44.4, max 66.6

By default, the metric only outputs trace sections compiled directly from your
own application package binaries. To include processes originating from outside
your app's package boundary, set the property `targetPackageOnly = false`.

When working on Jetpack Compose Runtime Tracing, you can surface individual
composable functions in your system trace graphs without writing manual trace
wrappers by enabling [composition tracing](https://developer.android.com/develop/ui/compose/tooling/tracing).

While adding the `androidx.compose.runtime:runtime-tracing` dependency to your
target application is sufficient for manual profiler traces, capturing these
traces programmatically within a Macrobenchmark run requires additional
configuration inside your benchmark module.

For complete setup instructions, see [Capture a trace with Jetpack
Macrobenchmark](https://developer.android.com/develop/ui/compose/tooling/tracing#macrobenchmark).

## PowerMetric

> [!WARNING]
> **Experimental:** This class is experimental.

[`PowerMetric`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/PowerMetric) captures the change in power or energy over the duration of
your Macrobenchmark run. Each selected category is broken down into its
measurable hardware components, while unselected categories are grouped into an
"unselected" bucket.

**Hardware Requirement**: These metrics measure system-wide consumption rather
than per-app calculations. Consequently, data collection is limited to physical
Google Pixel 6, Pixel 6 Pro, and newer physical devices.

The metric outputs two measurements per category:

- `power<category>Uw`: the amount of power consumed over the duration of your test in this category (measured in microwatts).
- `energy<category>Uws`: the total amount of energy transferred per unit of time for the duration of your test in this category (measured in microwatt-seconds).

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

    powerCategoryCpuUw min 300.2, median 346.1, max 519.6
    powerCategoryDisplayUw min 319.8, median 325.8, max 329.7
    powerCategoryGpuUw min 18.8, median 23.3, max 36.9
    powerCategoryNetworkUw min 97.3, median 123.3, max 681.3
    powerTotalUw min 1234.8, median 1316.6, max 2112.4
    powerUnselectedUw       min  483.3,  median  512.6,  max  561.7

## Analyzing core subsystems

[`PowerMetric`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/PowerMetric) captures the change in power or energy over the duration of
your test for the provided power categories. Each category you select is broken
down into its measurable subcomponents, and unselected categories are added to
the "unselected" metric.

The terminal outputs map to the configuration you request:

- **`powerCategoryCpuUw`**: The amount of power consumed by the CPU over the duration of your test.
- **`powerCategoryGpuUw`**: The amount of power consumed by the GPU over the duration of your test.
- **`powerUnselectedUw`** : The aggregate power consumed by all available hardware categories that were **not** explicitly requested in your initialization map.

To prevent erratic data spikes on the hardware rails during a run, lock screen
brightness to a fixed value, maintain a stable device temperature, and close
competing background processes before starting the Macrobenchmark loop.

## Additional resources

### Views content

- [Capture Macrobenchmark metrics (Views)](https://developer.android.com/topic/performance/views/benchmarking/macrobenchmark-metrics-views)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Create Baseline Profiles {:#creating-profile-rules}](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile)
- [Writing a Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)
- [App startup analysis and optimization {:#app-startup-analysis-optimization}](https://developer.android.com/topic/performance/appstartup/analysis-optimization)