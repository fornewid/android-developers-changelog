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

It guides engineering and product teams to assess technical performance of any
given Android app. After the assessment is complete, an evaluation and
recommended actions help to identify and prioritize the most important areas for
performance improvement.

> [!WARNING]
> **Preview:** This page contains the first iteration of the App Performance Score.
>
> - Scoring, evaluation and recommendations are likely to change in the future.
> - Recommendations and guidance provided has curated with performance impact in mind.
> - Tools and guidance in the recommendations are stable and can help to improve app startup and rendering performance.

*** ** * ** ***

### Introduction

The App Performance Score provides app developers with static and dynamic
assessments. Both can be conducted individually and provide unique insights into
an app's performance behavior. These insights are coupled with actionable
recommendations which can help to improve the status quo and elevate the app's
performance.

A score between 0 and 100 is provided to help gauge the overall performance.
A lower number means more room to improve.

Use the score and recommendations for each item to direct engineering efforts
into areas where high performance gains can be achieved. When recommendations
have been applied, take the assessment again and see how the score has improved.

| Dynamic score | Static score |
|---|---|
| The application's runtime behavior is used to assess performance characteristics. The dynamic performance score is a direct reflection of how well an app performs on a specific device. | The application is statically assessed to evaluate performance predictors based on use of best practices and tooling adoption. The static performance score highlights tools with high impact on app performance. No runtime evaluation is needed for this score. |
| [Jump to dynamic score](https://developer.android.com/topic/performance/app-score#dynamic-score) | [Jump to static score](https://developer.android.com/topic/performance/app-score#static-score) |

<br />

*** ** * ** ***

<br />

![](https://developer.android.com/static/images/picto-icons/lightning.svg)

## Dynamic App Performance Score

During dynamic assessment of the App Performance Score, runtime data are used to
evaluate an app's performance on a specific device.

The dynamic assessment requires a physical device for a realistic performance
evaluation. The score will vary depending on the device's capabilities. Assess
the performance on multiple devices to get a better understanding how users are
impacted by performance shortcomings.

> [!TIP]
> **Tip:** Use lower end devices to exaggerate performance issues. This will result in an overall lower score and emphasize areas that can be improved.

The current dynamic app score categories and assessment criteria are outlined in
the following table.

| Category | Assessment criteria |
|---|---|
| Application startup | Measured duration between app startup and the app becoming interactive [TTFD](https://developer.android.com/topic/performance/vitals/launch-time#time-full). |
| Rendering performance | Percentage of slow and frozen frames for scrolling, animating and full screen renders. |

<iframe src="https://android.devsite.google/frame/topic/performance/app-score/index_86cbf7b7ec0571249b2c940e15686064b55ced06420d17f36f8a448a284885ed.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

<br />

*** ** * ** ***

<br />

![](https://developer.android.com/static/images/picto-icons/layout.svg)

## Static App Performance Score

The static App Performance Score is calculated based on the usage of highly
impactful tools and best practices. To correctly score an app's static
performance indicators, access to the project's source code is required.

The criteria listed in the following table are used to assess and generate the
static App Performance Score.

| Category | Assessment criteria |
|---|---|
| Build time improvements | - App uses latest version of the [Android Gradle Plugin](https://developer.android.com/build/gradle-build-overview) to unlock access to performance enhancing tools - [Minification and optimizations](https://developer.android.com/build/shrink-code) enabled with full mode R8. Exceptions are minimal and limited to necessary areas. |
| Startup performance | - [Baseline Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview) are found in the app and applied correctly for app startup - Baseline Profiles cover one or more user journeys - Startup Profiles applied to apply [Dex Layout Optimizations](https://developer.android.com/topic/performance/baselineprofiles/dex-layout-optimizations) |
| Compose adoption | App uses latest stable version of [Compose](https://developer.android.com/compose) |
| Monitoring and optimization | [`FullyDrawnReporter`](https://developer.android.com/reference/kotlin/androidx/activity/FullyDrawnReporter) or [`reportFullyDrawn`](https://developer.android.com/reference/android/app/Activity#reportFullyDrawn()) is used at an appropriate time |

<iframe src="https://android.devsite.google/frame/topic/performance/app-score/index_3ec0a43d964314b4650ab5c7747e18a4b336731bf434006da1719afa4c2d8dd0.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Tips for evaluating your app

Here are some tips when measuring your App Performance Score.

### Choose a representative device

When measuring your dynamic score, we recommend using the same type of device as
your user base. Unlike the static score, a dynamic score will vary based
on the device specs. If you don't know where to start, use a low-end device and
work on improvements from there.

### Assess dynamic score variability

It's possible that your dynamic score changes across multiple observation
periods, without you changing your code. This could be due to inherent
variability in the app performance or other system activities happening on your
device. If you notice that your score is highly variable, we recommend testing
multiple times in sequence and noting the most common behavior.

Your static score should remain stable unless you change your code.

### Use scores separately if needed

If you don't have the time or capacity to calculate both the dynamic and static
score, you can use each alone as well. Any improvement to your dynamic or static
score will still benefit your users.

### Supplement with other monitoring metrics

The App Performance Score is a quick, high-level way to assess app performance.
To get more detailed performance insights, consider exploring other data sources
such as [Android Vitals](https://play.google.com/console/about/vitals/),
[Firebase Performance Monitoring](https://firebase.google.com/docs/perf-mon),
and [benchmarks](https://developer.android.com/topic/performance/benchmarking/benchmarking-overview).

## How to improve your score

In general, if both your static and dynamic scores are subpar we recommend
taking actions to maximize your static score before troubleshooting the dynamic
one. Addressing shortcomings in the static score will likely improve the dynamic
score as well, so it's helpful to optimize the former as a first step to
improving your app performance. The static score is based on concrete values or
settings in your app code, whereas the dynamic metrics usually take longer to
investigate and identify the root cause of.

Within each segment, the App Performance Score provides actionable steps to
improve your app.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Capture Macrobenchmark metrics](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics)
- [Get started with Baseline Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview)
- [Create Startup Profiles](https://developer.android.com/topic/performance/baselineprofiles/dex-layout-optimizations)
- [Overview of measuring app performance](https://developer.android.com/topic/performance/measuring-performance)
- [Frozen frames](https://developer.android.com/topic/performance/vitals/frozen)