---
title: https://developer.android.com/topic/performance/app-score
url: https://developer.android.com/topic/performance/app-score
source: md.txt
---

<br />

Use the App Performance Score to calculate your overall performance score
and discover opportunities for improvement. The App Performance Score provides a
standardized framework to measure performance with minimal in-depth technical
tasks.

It guides engineering and product teams to assess the technical performance of
any Android app. After you complete the assessment, the evaluation and
recommended actions help you identify and prioritize the most important areas
for performance improvement.

> [!WARNING]
> **Preview:** This page contains the App Performance Score assessment.
>
> - Scoring, evaluation, and recommendations update as performance guidance evolves.
> - Recommendations and guidance focus on performance impact and return on investment (ROI).
> - Tools and guidance in the recommendations are stable and help improve app startup and rendering performance.

*** ** * ** ***

### Introduction

The App Performance Score provides app developers with static and dynamic
assessments. You can run each assessment individually to get insights into your
app's performance behavior, along with actionable recommendations to improve
your app's performance.

The assessment provides a score between 0 and 100 to help you gauge overall
performance. A lower number means more room to improve.

Use the score and recommendations for each item to focus engineering efforts on
areas with high performance gains. Start with the **Static App Performance
Score** to apply foundational build and configuration optimizations first, then
use the **Dynamic App Performance Score** to validate runtime startup and
rendering improvements on physical devices. After you apply the
recommendations, retake the assessment to see how your score improves.

### Where the App Performance Score fits in your performance journey

Improving app performance follows a tiered, step-by-step progression from
low-effort, high-ROI foundational practices to advanced custom telemetry:

1. **Level 1 (Monitor field vitals)** : Track production health in Google Play Console using [Android vitals](https://developer.android.com/google/play/vitals.md.txt), including user-perceived crash rate, user-perceived ANR rate, excessive battery usage, excessive partial wake locks, low-memory killer (LMK) rate, and DEX optimization status.
2. **Level 2 (App Performance Score assessment)** : Apply high-ROI optimizations using this scorecard:
   - **Step 1 ([Static App Performance Score](https://developer.android.com/topic/performance/app-score.md.txt#static-score))** : Verify project configuration and tooling adoption, including Android Gradle Plugin (AGP), [R8 app optimization](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization.md.txt), [Baseline Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview.md.txt), [Startup Profiles](https://developer.android.com/topic/performance/baselineprofiles/dex-layout-optimizations), [Jetpack Compose](https://developer.android.com/compose), and [`reportFullyDrawn`](https://developer.android.com/reference/android/app/Activity.md.txt#reportFullyDrawn()).
   - **Step 2 ([Dynamic App Performance Score](https://developer.android.com/topic/performance/app-score.md.txt#dynamic-score))**: Measure cold startup and frame rendering performance on low-end physical devices.
3. **Level 3 (Automated local benchmarking)** : Prevent regressions and automate measurement using Jetpack [Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics.md.txt) (`StartupTimingMetric` and `FrameTimingMetric`) and [`UiAutomator`](https://developer.android.com/training/testing/other-components/ui-automator.md.txt).
4. **Level 4 (In-depth trace diagnosis)** : Diagnose complex startup and rendering bottlenecks using [Perfetto and the Android Studio System Trace
   Profiler](https://developer.android.com/topic/performance/tracing).
5. **Level 5 (Custom production telemetry)** : Collect targeted field diagnostics using [`ApplicationStartInfo`](https://developer.android.com/reference/android/app/ApplicationStartInfo.md.txt), [`ProfilingManager`](https://developer.android.com/topic/performance/tracing/profiling-manager/how-to-capture.md.txt), and [`ApplicationExitInfo`](https://developer.android.com/reference/android/app/ApplicationExitInfo.md.txt).

| Static score (Step 1) | Dynamic score (Step 2) |
|---|---|
| Statically assesses your app to evaluate performance predictors based on best practices and tooling adoption. The static performance score highlights tools with high impact on app performance and doesn't require runtime evaluation. | Uses your app's runtime behavior to assess performance characteristics. The dynamic performance score directly reflects how well your app performs on a specific device. |
| [Jump to static score](https://developer.android.com/topic/performance/app-score.md.txt#static-score) | [Jump to dynamic score](https://developer.android.com/topic/performance/app-score.md.txt#dynamic-score) |

<br />

*** ** * ** ***

<br />

![Static score icon](https://developer.android.com/static/images/picto-icons/layout.svg)

## Static App Performance Score

The static App Performance Score measures your adoption of high-impact tools and
best practices. Start with the static assessment before measuring your dynamic
score, because these configuration and build optimizations offer the highest
return on investment and directly improve runtime startup and rendering metrics.
To score an app's static performance indicators, you need access to the
project's source code.

The following table lists the criteria that generate the static App Performance
Score:

| Category | Assessment criteria |
|---|---|
| Build and optimization improvements | App uses a recent [Android Gradle Plugin](https://developer.android.com/build/gradle-build-overview.md.txt) (such as AGP 9.0 or higher, or AGP 9.3 or higher for simplified optimization configuration), and [R8 minification and optimization](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization.md.txt) are enabled in [full mode](https://developer.android.com/topic/performance/app-optimization/full-mode.md.txt) (or adopted [incrementally](https://developer.android.com/topic/performance/app-optimization/adopt-optimizations-incrementally.md.txt)) with minimal keep rules verified by the [R8 Configuration Analyzer](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer.md.txt). |
| Startup performance | [Baseline Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview.md.txt) are automated and cover startup and critical user journeys, and Startup Profiles apply [DEX layout optimizations](https://developer.android.com/topic/performance/baselineprofiles/dex-layout-optimizations). |
| Compose adoption | App uses a recent stable [Jetpack Compose BOM](https://developer.android.com/compose) (such as Compose BOM 2025.04.01 or higher). |
| Monitoring and optimization | App calls [`FullyDrawnReporter`](https://developer.android.com/reference/kotlin/androidx/activity/FullyDrawnReporter.md.txt) or [`reportFullyDrawn`](https://developer.android.com/reference/android/app/Activity.md.txt#reportFullyDrawn()) when it becomes interactive. |

<iframe src="https://android.devsite.google/frame/topic/performance/app-score/index_c36fb58dac5593531ced3fb3482d47efc4f26471bc9b61b93e4e5276cee40d98.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

<br />

*** ** * ** ***

<br />

![Dynamic score icon](https://developer.android.com/static/images/picto-icons/lightning.svg)

## Dynamic App Performance Score

After applying the static optimizations, use the dynamic assessment of the App
Performance Score to evaluate your app's runtime performance on a specific
device.

The dynamic assessment requires a physical device for a realistic performance
evaluation. The score varies depending on the device's capabilities. Assess
performance on multiple devices to better understand how performance
shortcomings affect users.

> [!TIP]
> **Tip:** Use lower-end devices to make performance issues more visible. Lower-end devices produce a lower overall score and highlight areas that you can improve.

The following table outlines the dynamic app score categories and assessment
criteria:

| Category | Assessment criteria |
|---|---|
| Application startup | Measured duration between app startup and the app becoming interactive ([TTFD](https://developer.android.com/topic/performance/issues/launch-time.md.txt#time-full)). |
| Rendering performance | Percentage of slow and frozen frames for scrolling, animating, and full-screen renders. |

<iframe src="https://android.devsite.google/frame/topic/performance/app-score/index_2315ade97e02150875d7b06cc2d1e48e1725b65b23641a5342b804bf7b05d4c9.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Tips for evaluating your app

Here are some tips when measuring your App Performance Score.

### Choose a representative device

When measuring your dynamic score, we recommend using the same type of device as
your user base. Unlike the static score, a dynamic score varies based on the
device specifications. If you don't know where to start, use a low-end device
and work on improvements from there.

### Assess dynamic score variability

Your dynamic score might change across multiple observation periods, even
without code changes. This variability can happen because of inherent
variability in app performance or other system activities on your device. If
your score varies significantly, test multiple times in sequence and note the
most common behavior.

Your static score remains stable unless you change your code.

### Use scores separately if needed

If you don't have the time or capacity to calculate both the static and dynamic
score, you can use each alone as well. Any improvement to your static or dynamic
score still benefits your users.

### Supplement with other monitoring metrics

The App Performance Score is a high-level way to assess app performance at
Level 2 of your performance journey. As your performance practices mature,
combine it with tools from the other tiers:

- **Field monitoring (Level 1)** : Monitor real-world stability and performance thresholds in [Android vitals](https://developer.android.com/google/play/vitals.md.txt) (or [Play Console vitals](https://google.play/business/vitals/)) and [Firebase Performance Monitoring](https://firebase.google.com/docs/perf-mon).
- **Automated benchmarking (Level 3)** : Automate startup and frame timing measurements in CI or locally with [Jetpack Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/benchmarking-overview.md.txt) and [`UiAutomator`](https://developer.android.com/training/testing/other-components/ui-automator.md.txt).
- **System trace analysis (Level 4)** : Capture and inspect system traces using [Perfetto and the Android Studio System Trace Profiler](https://developer.android.com/topic/performance/tracing.md.txt).
- **Custom production telemetry (Level 5)** : Track detailed startup states, production system traces, and process terminations using [`ApplicationStartInfo`](https://developer.android.com/reference/android/app/ApplicationStartInfo.md.txt), [`ProfilingManager`](https://developer.android.com/topic/performance/tracing/profiling-manager/how-to-capture.md.txt), and [`ApplicationExitInfo`](https://developer.android.com/reference/android/app/ApplicationExitInfo.md.txt).

## How to improve your score

To maximize engineering return on investment, follow the tiered performance
workflow when improving your score:

1. **Maximize your Static App Performance Score first (Level 2, Step 1)** : Start by upgrading AGP, enabling [R8 app optimization](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization.md.txt) in [full mode](https://developer.android.com/topic/performance/app-optimization/full-mode.md.txt) (or [adopting optimizations incrementally](https://developer.android.com/topic/performance/app-optimization/adopt-optimizations-incrementally.md.txt)), generating [Baseline Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview.md.txt) and [Startup Profiles](https://developer.android.com/topic/performance/baselineprofiles/dex-layout-optimizations), updating [Jetpack
   Compose](https://developer.android.com/compose), and calling [`reportFullyDrawn`](https://developer.android.com/reference/android/app/Activity.md.txt#reportFullyDrawn()). Because the static score is based on concrete build and configuration settings, these optimizations are faster to implement and directly improve runtime startup and rendering.
2. **Validate with the Dynamic App Performance Score (Level 2, Step 2)**: Measure cold startup and frame rendering on low-end physical devices to verify the effect of your static changes and identify remaining runtime bottlenecks.
3. **Automate and diagnose deeper bottlenecks (Levels 3-5)** : Convert manual dynamic checks into repeatable [Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics.md.txt) tests, use [system tracing with Perfetto](https://developer.android.com/topic/performance/tracing.md.txt) to isolate slow startup work or slow and frozen frames, and monitor field metrics with [Android vitals](https://developer.android.com/google/play/vitals.md.txt) and [`ProfilingManager`](https://developer.android.com/topic/performance/tracing/profiling-manager/how-to-capture.md.txt).

Within each segment, the App Performance Score provides actionable steps to
improve your app.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Enable app optimization with R8](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization.md.txt)
- [Capture Macrobenchmark metrics](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics.md.txt)
- [Get started with Baseline Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview.md.txt)
- [Create Startup Profiles](https://developer.android.com/topic/performance/baselineprofiles/dex-layout-optimizations)
- [Overview of measuring app performance](https://developer.android.com/topic/performance/measuring-performance.md.txt)
- [Frozen frames](https://developer.android.com/topic/performance/issues/render.md.txt#frozen-frames)