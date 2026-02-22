---
title: https://developer.android.com/topic/performance/baselineprofiles/measure-baselineprofile
url: https://developer.android.com/topic/performance/baselineprofiles/measure-baselineprofile
source: md.txt
---

We recommend using [Jetpack Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview) to test how an app performs when
Baseline Profiles are enabled, and then compare those results to a benchmark
with Baseline Profiles disabled. With this approach, you can measure app startup
time---both time to initial and full display---or runtime rendering
performance to see if the frames produced can cause jank.

Macrobenchmarks let you control pre-measurement compilation using the
[`CompilationMode`](https://developer.android.com/reference/androidx/benchmark/macro/CompilationMode) API. Use different `CompilationMode` values to compare
performance with different compilation states. The following code snippet shows
how to use the `CompilationMode` parameter to measure the benefit of Baseline
Profiles:  

```kotlin
@RunWith(AndroidJUnit4ClassRunner::class)
class ColdStartupBenchmark {
    @get:Rule
    val benchmarkRule = MacrobenchmarkRule()

    // No ahead-of-time (AOT) compilation at all. Represents performance of a
    // fresh install on a user's device if you don't enable Baseline Profiles---
    // generally the worst case performance.
    @Test
    fun startupNoCompilation() = startup(CompilationMode.None())

    // Partial pre-compilation with Baseline Profiles. Represents performance of
    // a fresh install on a user's device.
    @Test
    fun startupPartialWithBaselineProfiles() =
        startup(CompilationMode.Partial(baselineProfileMode = BaselineProfileMode.Require))

    // Partial pre-compilation with some just-in-time (JIT) compilation.
    // Represents performance after some app usage.
    @Test
    fun startupPartialCompilation() = startup(
        CompilationMode.Partial(
            baselineProfileMode = BaselineProfileMode.Disable,
            warmupIteration = 3
        )
    )

    // Full pre-compilation. Generally not representative of real user
    // experience, but can yield more stable performance metrics by removing
    // noise from JIT compilation within benchmark runs.
    @Test
    fun startupFullCompilation() = startup(CompilationMode.Full())

    private fun startup(compilationMode: CompilationMode) = benchmarkRule.measureRepeated(
        packageName = "com.example.macrobenchmark.target",
        metrics = listOf(StartupTimingMetric()),
        compilationMode = compilationMode,
        iterations = 10,
        startupMode = StartupMode.COLD,
        setupBlock = {
            pressHome()
        }
    ) {
        uiAutomator {
            startApp(packageName)
            onElement(5_000) { viewIdResourceName == "my-content"}
        }
    }
}
```
| **Caution:** Run the benchmarks on a physical device to measure real world performance. Measuring performance on an Android emulator likely provides incorrect results, because resources are shared with its hosting machine.

In the following screenshot, you can see the results directly in Android Studio
for the [Now in Android sample](https://goo.gle/nia) app ran on Google Pixel 7. The
results show that app startup is fastest when using Baseline Profiles
(**229.0ms** ) in contrast with no compilation (**324.8ms**).
![results of ColdstartupBenchmark](https://developer.android.com/static/topic/performance/images/benchmark_images/baselineprofile_measure_effectiveness.jpg) **Figure 1.** Results of `ColdStartupBenchmark` showing time to initial display for no compilation (324ms), full compilation (315ms), partial compilation (312ms), and Baseline Profiles (229ms). **Tip:** You can also retrieve the results as a JSON file to parse them as part of your CI pipeline. For more information, see [Benchmarking in CI](https://developer.android.com/topic/performance/benchmarking/benchmarking-in-ci).

While the previous example shows app startup results captured with
[`StartupTimingMetric`](https://developer.android.com/reference/androidx/benchmark/macro/StartupTimingMetric), there are other important metrics worth considering,
such as [`FrameTimingMetric`](https://developer.android.com/reference/androidx/benchmark/macro/FrameTimingMetric). For more information about all the types of
metrics, see [Capture Macrobenchmark metrics](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics).

## Time to full display

The previous example measures the [time to initial display](https://developer.android.com/topic/performance/vitals/launch-time#time-initial) (TTID), which is
the time taken by the app to produce its first frame. However, this doesn't
necessarily reflect the time until the user can start interacting with your app.
The [time to full display](https://developer.android.com/topic/performance/vitals/launch-time#time-full) (TTFD) metric is more useful in measuring and
optimizing the code paths necessary to have a fully useable app state.

We recommend optimizing for both TTID and TTFD, as both are important. A low
TTID helps the user see that the app is actually launching. Keeping the TTFD
short is important to help ensure that the user can interact with the app
quickly.

For strategies on reporting when the app UI is fully drawn, see [Improve
startup timing accuracy](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics#startup-accuracy).

## Recommended for you

- Note: link text is displayed when JavaScript is off
- \[Write a Macrobenchmark\]\[11\]
- \[Capture Macrobenchmark metrics\]\[12\]
- [Write automated tests with UI Automator](https://developer.android.com/training/testing/other-components/ui-automator)
- \[App startup analysis and optimization {:#app-startup-analysis-optimization}\]\[14\]