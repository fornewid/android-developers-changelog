---
title: https://developer.android.com/develop/ui/compose/performance/herobenchmark
url: https://developer.android.com/develop/ui/compose/performance/herobenchmark
source: md.txt
---

Hero benchmarks are a set of benchmarks that cover high-level app user journeys,
such as app startup or scrolling in the open-source Pokedex app.

- **Startup hero benchmarks:** Tracking the time from opening the app to content being displayed.
- **Scroll hero benchmarks:** Measuring scrolling performance of a lazy grid with images.

## Test setup

- **App selection:** We conducted these tests using the open-source Pokedex app, comparing its [View-based](https://github.com/skydoves/Pokedex) and [Compose-based](https://github.com/skydoves/pokedex-compose) versions. The app was selected to represent real-world scenarios, and was not developed by the Compose team.
- **Hardware setup:** We ran benchmarks on a Pixel 3a running Android 12 (API 31) [with locked CPUs and GPUs](https://developer.android.com/topic/performance/benchmarking/microbenchmark-overview#lock-clocks). This device is used as the standard performance baseline for hero benchmarks.
- **Build setup:** The benchmarks use the app built in release mode with [R8
  enabled](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/integration-tests/hero/pokedex/pokedex-macrobenchmark-target/build.gradle). The app is fully pre-compiled to reduce instability from just-in-time (JIT) compilation.
- **Result selection**: To ensure worst-case analysis, extreme outliers and non-representative noise were excluded from the benchmark results. A baseline was then established by selecting the median values of the upper-bound performance data

## Startup hero benchmarks

To measure startup, we used [`PokedexStartupBenchmark`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/integration-tests/hero/pokedex/pokedex-macrobenchmark/src/main/java/androidx/compose/integration/hero/pokedex/macrobenchmark/PokedexStartupBenchmark.kt). The
`PokedexStartupBenchmark` measures the time it takes for the Pokedex app to be
visible to the user.

App launch can take place in one of [three states](https://developer.android.com/topic/performance/vitals/launch-time#startup-state): cold start, warm start,
or hot start. Each state affects how long it takes for an app to become visible
to the user. In a cold start, the app starts from scratch. In this benchmark, we
measure the app launch performance in cold start state. We recommend that you
always optimize the app based on an assumption of a cold start. Doing so can
improve the performance of warm and hot starts as well.

The metrics we use to measure the app startup time are [time to initial
display](https://developer.android.com/topic/performance/vitals/launch-time#time-initial) and the [time to full display](https://developer.android.com/topic/performance/vitals/launch-time#time-full).

> [!NOTE]
> **Note:** Because of significant changes to the `PokedexStartupBenchmark` methodology for Compose 1.11, the benchmark data is not shown for previous Compose versions.

### Time to initial display

Time to initial display (TTID) measures the time it takes for an app to produce
its first frame, including process initialization during a cold start, activity
creation during a cold or warm start, and displaying the first frame.

In the `PokedexStartupBenchmark`, Compose 1.11 is 2.5% slower than Views for
TTID with a cold start.
![Compose 1.11 is 2.5% slower than Views for TTID](https://developer.android.com/static/develop/ui/compose/performance/images/timetoinitialdisplay.svg) **Figure 1:**Compose 1.11 compared to Views for TTID.

### Time to full display

Time to full display (TTFD) measures the time until the app becomes interactive.
This means that all data has been loaded and has been drawn. For more
information about time to full display, see [App Startup Time](https://developer.android.com/topic/performance/vitals/launch-time#time-full).

In the `PokedexStartupBenchmark`, Compose 1.11 is 13.0% slower than Views for
TTFD with a cold start.
![Compose 1.11 is 13.0% slower than Views for TTFD](https://developer.android.com/static/develop/ui/compose/performance/images/timetofulldisplayms.svg) **Figure 2:**Compose 1.11 compared to Views for TTFD.

> [!NOTE]
> **Note:** The Compose team is actively working to improve the startup latency. For more details about upcoming improvements in Compose performance, see the [Compose roadmap](https://developer.android.com/jetpack/androidx/compose-roadmap).

## Scroll hero benchmarks

To measure the scrolling performance we used the [PokedexScrollBenchmark](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/integration-tests/hero/pokedex/pokedex-macrobenchmark/src/main/java/androidx/compose/integration/hero/pokedex/macrobenchmark/PokedexScrollBenchmark.kt).
It measures the scroll performance of the Pokedex app screen for a lazy grid
with images. In this benchmark, the entire screen is scrolled and flung multiple
times and new items are loaded. Scroll performance is measured by jank rate.

**Jank rate**

Android devices render at up to 60 or 120 frames per second (fps). This means
the system has a strict deadline (for example, 16.6ms for 60fps) to produce a
frame. If the app takes too long to do its work, this can cause a visible
stutter that we call jank.

In the `PokedexScrollBenchmark`, Compose and Views achieve the same performance
of
0.21% jank since Compose 1.9.0. In absolute terms, 1 out of 485 frames were
janky.

> [!NOTE]
> **Note:** To ensure conservative reporting, we used the scenario with the highest UI and frame-rendering complexity as our representative result.

These benchmarks show that Compose 1.9 and later match the Views performance for
jank while scrolling.
![Since Compose 1.9.0, Compose and Views have the same jank rate](https://developer.android.com/static/develop/ui/compose/performance/images/jank.svg) Since Compose 1.9.0, Compose and Views have the same jank rate.

## Run hero benchmarks

To validate the performance results and run the benchmarks locally:

1. Follow the [AndroidX guide](https://github.com/androidx/androidx/blob/androidx-main/docs/onboarding.md) to check out the source code.
2. Follow the instructions in the [Hero Benchmarks source code](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/integration-tests/hero/README.md).

You can run these benchmarks on any supported device, such as a specific device
that you are optimizing your app for. However, to validate the official results,
use the same [hardware setup](https://developer.android.com/develop/ui/compose/performance/herobenchmark#test-setup).