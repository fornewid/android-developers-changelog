---
title: https://developer.android.com/training/wearables/compose/performance
url: https://developer.android.com/training/wearables/compose/performance
source: md.txt
---

Performance on Wear OS is an essential consideration for apps, as many Wear OS
devices have limited CPU and GPU resources compared to larger mobile devices.
With the introduction of richer animations and dynamic effects in Material 3
Expressive, you should validate and improve the performance of your app's key
workflows.

Use the [Jetpack Compose Performance](https://developer.android.com/jetpack/compose/performance) guide to configure and develop your app
for optimal performance using Jetpack Compose. This document highlights some of
the techniques described in that guide.

Create and follow performance measurement strategies to validate that these
techniques work as expected for your app.

## Essential performance improvement techniques

Start with the most effective performance tool types: baseline profiles
(including startup profiles) and the R8 code optimizer.

Update your [Compose](https://developer.android.com/jetpack/androidx/releases/compose) dependency to version 1.8 or higher, which introduced
several significant new features and improved the overall stability of the
library. See the instructions in [Declaring dependencies](https://developer.android.com/jetpack/androidx/releases/compose#declaring_dependencies) to learn how to
update. To learn more, read our [blog about the 1.8 release](https://android-developers.googleblog.com/2025/04/whats-new-in-jetpack-compose-april-25.html) and the
[What's New in Compose](https://youtu.be/IaNpcrCSDiI?si=1BFiIF3OH91AEBE8&t=36) I/O talk.

### Baseline profiles

To improve your app's performance, use [baseline profiles](https://developer.android.com/jetpack/compose/performance#use-baseline). Group together
the classes and methods that represent your app's key workflows, which the
system can pre-compile using a baseline profile. This can reduce startup times,
cut down on janky frames, and offer additional performance improvements.

Each Jetpack Compose library ships with its own profile rules. When your app
depends on a library, the library profile rules are automatically merged and
distributed with your app's APK for precompilation.

Verify your baseline profiles using the following techniques:

- Use macrobenchmark tests.
- Use specific ADB commands to validate your app's profile configuration state. Steps for both of these techniques are explained in the [performance measurement and validation](https://developer.android.com/training/wearables/compose/performance#performance-measurement) guide.

#### Startup Profiles

As a subset of baseline profiles, [Startup Profiles](https://developer.android.com/topic/performance/baselineprofiles/dex-layout-optimizations) further optimize the
classes and methods they contain to reduce app startup latency.

Adding a startup profile will increase the APK size of your app, so before
adding one to your production release, be sure to assess the tradeoff between
APK size and startup latency.

To get started, read [Create a Startup Profile](https://developer.android.com/topic/performance/baselineprofiles/dex-layout-optimizations#create-startup).

### R8

Use the [R8 compiler](https://developer.android.com/studio/build/shrink-code) to shrink and optimize apps. R8 removes unused code and
resources, rewrites code to optimize runtime performance, and more.

In the [improve performance Overview](https://developer.android.com/topic/performance/improving-overview) guides, read the considerations for R8, including key steps for [removing unused resources](https://developer.android.com/studio/build/shrink-code#shrink-resources).

## Performance Measurement and Validation

To learn about general performance measurement strategies on Android,
see [Overview of measuring app performance](https://developer.android.com/topic/performance/measuring-performance). This section describes some of
the techniques discussed in that documentation.

### Choose a build variant for measurements

While debug mode is useful for spotting many problems, it imposes a
significant performance cost, doesn't use baseline profiles, and can make it
hard to spot code issues that might be affecting performance.

To accurately understand your app's performance, run your app in
[release mode](https://developer.android.com/studio/run#changing-variant).

Draw final conclusions on performance only from tests performed with apps
running with release build options and on real devices.

However, when benchmark testing, use the benchmark build variant, which has some
key differences from release debugging. See the [Macrobenchmark setup guide](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview#set-up-app)
for details.

### Validate your app's baseline profiles

Start by inspecting the status of your profile:  

    adb shell dumpsys package dexopt | grep -A 1 $PACKAGE_NAME

If the status is not `status=speed-profile`, profile rules have not yet been
applied to optimize the app.

Rules are applied using a background job that runs when the device is charged
and idle. To manually trigger this, run the following command after the app
launches and enough time passes for the profile installer to bootstrap the
profile in the background. This process typically takes about 40 seconds.  

    adb shell cmd package bg-dexopt-job

Then, re-run the previous command to verify that the status is `speed-profile`.

For situations where optimization occurs at install, see [Sideload the baseline
profile](https://developer.android.com/topic/performance/baselineprofiles#measuring-baseline).

### UI Automator API

The [UI Automator API](https://developer.android.com/training/testing/other-components/ui-automator) automates interactions programmatically. Use this API
to benchmark discrete pieces of UI when inspecting user journeys for potential
optimizations.

### Macrobenchmark tests

Macrobenchmarks test larger use cases of your app, especially app startup and
complex UI manipulations. To get started, see the [implementation guide](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview).

For an example of using macrobenchmarks to validate the performance of
baseline profiles, see the [performance samples](https://github.com/android/performance-samples/blob/main/MacrobenchmarkSample/baseBenchmarks/src/main/java/com/example/benchmark/macro/base/startup/StartupBenchmark.kt) on GitHub.

### JankStats Library

Use the [JankStats library](https://developer.android.com/topic/performance/jankstats) to track and analyze performance problems in
applications.

For an example, see the [JankStats sample](https://github.com/android/performance-samples/tree/main/JankStatsSample) on GitHub.

### System Trace

With the new animation types introduced by Material 3 Expressive, use the
[System Trace](https://developer.android.com/studio/profile/cpu-profiler) feature in Android Studio to inspect and diagnose latency in
potentially problematic user journeys. With this information, verify the content
of your baseline profiles, and identify potential inefficiencies in your code
logic.

## Additional tools

In addition to performance improvement tools, you can use other tools to improve your productivity and workflow.

### Android Studio Productivity Tools

Android Studio provides several tools that can reduce the amount of time you
spend identifying performance improvements.

For example, using tools like [Live Edit](https://developer.android.com/develop/ui/compose/tooling/iterative-development) and [Composable Previews](https://developer.android.com/develop/ui/compose/tooling/previews),
you can identify janky UI elements, along with the associated areas in your
app's code, for performance improvements.

Run all final performance tests on a suite of **physical Wear OS devices**
that accurately represents your target user base.

This is especially important when migrating to Material 3 Expressive, which
introduces features like flex fonts and shape morphing to your app.

If you are migrating from views, check out out [migration guide](https://developer.android.com/develop/ui/compose/migrate/strategy) and our
[best practices for Jetpack Compose performance](https://developer.android.com/develop/ui/compose/performance/bestpractices) to verify that your app's
UIs are performant when using Jetpack Compose.

## Other resources

To stay up to date with the latest in android performance, check out the
[Latest news and videos](https://developer.android.com/topic/performance/overview#latest-news-and-videos) in the App performance guide.