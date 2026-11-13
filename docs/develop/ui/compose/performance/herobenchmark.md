---
title: https://developer.android.com/develop/ui/compose/performance/herobenchmark
url: https://developer.android.com/develop/ui/compose/performance/herobenchmark
source: md.txt
---

> Documentation index: https://developer.android.com/develop/ui/compose/performance/llms.txt

Hero benchmarks are a set of benchmarks that cover high-level app user journeys,
such as app startup or scrolling in the open-source Pokedex app.

- **Startup hero benchmarks**: Tracking the time from opening the app to content being displayed.
- **Scroll hero benchmarks**: Measuring scrolling performance of a lazy grid with images.

## Test setup

- **App selection** : We conducted these tests using the open-source Pokedex app, comparing its [View-based](https://github.com/skydoves/Pokedex) and [Compose-based](https://github.com/skydoves/pokedex-compose) versions. The app was selected to represent real-world scenarios, and was not developed by the Compose team.
- **Hardware setup** : Benchmarks were run on a Pixel 6 running Android 17 (API level 37) [with locked CPUs and GPUs](https://developer.android.com/topic/performance/benchmarking/microbenchmark-overview.md.txt#lock-clocks). Prior to Compose 1.12, benchmarks were conducted on a Pixel 3a. As of Compose 1.12, Pixel 6 is used as the standard performance baseline for hero benchmarks, and Compose 1.11 was also measured on Pixel 6 for comparison.
- **Build setup** : The benchmarks use the app built in release mode with [R8
  enabled](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/integration-tests/hero/pokedex/pokedex-macrobenchmark-target/build.gradle). The app is fully pre-compiled to reduce instability from just-in-time (JIT) compilation.
- **Result selection**: To ensure worst-case analysis, extreme outliers and non-representative noise were excluded from the benchmark results. A baseline was then established by selecting the median values of the upper-bound performance data.

> [!NOTE]
> **Note:** Since the Compose 1.12 release, incremental improvements in the Views benchmark have reduced Views time to full display from 193 ms to 180.32 ms.

## Startup hero benchmarks

To measure startup, we used [`PokedexStartupBenchmark`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/integration-tests/hero/pokedex/pokedex-macrobenchmark/src/main/java/androidx/compose/integration/hero/pokedex/macrobenchmark/PokedexStartupBenchmark.kt). The
`PokedexStartupBenchmark` measures the time it takes for the Pokedex app to be
visible to the user.

App launch can take place in one of [three states](https://developer.android.com/topic/performance/issues/launch-time.md.txt#startup-state): cold start, warm start,
or hot start. Each state affects how long it takes for an app to become visible
to the user. In a cold start, the app starts from scratch. In this benchmark, we
measure the app launch performance in cold start state. We recommend that you
always optimize the app based on an assumption of a cold start. Doing so can
improve the performance of warm and hot starts as well.

The metrics we use to measure the app startup time are [time to initial
display](https://developer.android.com/topic/performance/issues/launch-time#time-initial) and the [time to full display](https://developer.android.com/topic/performance/issues/launch-time.md.txt#time-full).

### Time to initial display

Time to initial display (TTID) measures the time it takes for an app to produce
its first frame, including process initialization during a cold start, activity
creation during a cold or warm start, and displaying the first frame.

In the `PokedexStartupBenchmark`, Compose 1.13 reaches initial display in
147.65 ms on a cold start. This result is within normal run-to-run noise of
Compose 1.12.1 (145.51 ms) and Compose 1.11.4 (147.78 ms), and 3.4% faster than
Views (152.87 ms).

| Version | Time to initial display (ms) |
| Compose 1.11 | 147.78 |
| Compose 1.12 | 145.51 |
| Compose 1.13 | 147.65 |
| Views | 152.87 |
|---|---|
[Time to initial display in milliseconds, tested on Pixel 6]

**Figure 1.** This chart compares TTID for Compose 1.11, 1.12, and 1.13 with Views.

### Time to full display

Time to full display (TTFD) measures the time until the app becomes interactive.
This means that all data has been loaded and has been drawn. For more
information about time to full display, see [App Startup Time](https://developer.android.com/topic/performance/issues/launch-time.md.txt#time-full).

In the `PokedexStartupBenchmark`, Compose 1.13 reaches full display in
202.79 ms on a cold start. This result is within normal run-to-run noise of
Compose 1.12.1 (201.96 ms) and Compose 1.11.4 (203.33 ms). Views reaches full
display in 180.32 ms, so Compose 1.13 is 12.5% slower than Views for TTFD.

| Version | Time to full display (ms) |
| Compose 1.11 | 203.33 |
| Compose 1.12 | 201.96 |
| Compose 1.13 | 202.79 |
| Views | 180.32 |
|---|---|
[Time to full display in milliseconds, tested on Pixel 6]

**Figure 2.** This chart compares TTFD for Compose 1.11, 1.12, and 1.13 with Views.

> [!NOTE]
> **Note:** The Compose team is actively working to improve the startup latency. For more details about upcoming improvements in Compose performance, see the [Compose roadmap](https://developer.android.com/jetpack/androidx/compose-roadmap.md.txt).

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

In the `PokedexScrollBenchmark`, Compose matches Views performance with 0
percentage points of excess jank since Compose 1.9.0. On Pixel 6, Views and
Compose both hold 0.00% jank across Compose 1.11.4, 1.12.1, and 1.13.

| Compose version | Device | Excess jank over Views (pp) |
| 1.3.3 | Pixel 3a | +0.35 |
| 1.4.3 | Pixel 3a | +0.41 |
| 1.5.4 | Pixel 3a | +0.42 |
| 1.6.8 | Pixel 3a | +0.21 |
| 1.7.8 | Pixel 3a | +0.36 |
| 1.8.0 | Pixel 3a | +0.38 |
| 1.9.0 | Pixel 3a | 0 |
| 1.10.0 | Pixel 3a | 0 |
| 1.11 | Pixel 6 | 0 |
| 1.12 | Pixel 6 | 0 |
| 1.13 | Pixel 6 | 0 |
|---|---|---|
[Compose excess jank over Views in percentage points, by Compose version (lower is better)]

**Figure 3.** Since Compose 1.9.0, Compose matches Views scroll jank.

## Run hero benchmarks

To validate the performance results and run the benchmarks locally:

1. Follow the [AndroidX guide](https://github.com/androidx/androidx/blob/androidx-main/docs/onboarding.md) to check out the source code.
2. Follow the instructions in the [Hero Benchmarks source code README](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/integration-tests/hero/README.md) to build the benchmark and target APKs (`pokedex-macrobenchmark` and `pokedex-macrobenchmark-target`), install them on a test device, and run the `PokedexStartupBenchmark` and `PokedexScrollBenchmark` suites using `adb` or Android Studio.

You can run these benchmarks on any supported device, such as a specific device
that you are optimizing your app for. However, to validate the official results,
use the same [hardware setup](https://developer.android.com/develop/ui/compose/performance/herobenchmark.md.txt#test-setup).