---
title: Deeper Performance Considerations  |  Android Developers' Blog
url: https://developer.android.com/blog/posts/deeper-performance-considerations
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Developers' Blog](https://developer.android.com/)
* [Blog](https://developer.android.com/blog)

Stay organized with collections

Save and categorize content based on your preferences.



#### [How-tos](/blog/categories/how-tos)

# Deeper Performance Considerations

###### 8-min read

![](/static/blog/assets/performance_Week11_efe6dd10be_Z1PApe6.webp)

19

Nov
2025

3
Authors

##### [Ben Weiss,](/blog/authors/ben-weiss) [Breana Tate,](/blog/authors/breana-tate) [Jossi Wolf](/blog/authors/jossi-wolf)

Compose yourselves and let us guide you through more background on performance.

Welcome to day 3 of Performance Spotlight Week. Today we're continuing to share details and guidance on important areas of app performance. We're covering Profile Guided Optimization, Jetpack Compose performance improvements and considerations on working behind the scenes. Let's dive right in.

## **Profile Guided Optimization**

[Baseline Profiles](/topic/performance/baselineprofiles/overview) and [Startup Profiles](/topic/performance/baselineprofiles/dex-layout-optimizations) are foundational to improve an Android app's startup and runtime performance. They are part of a group of performance optimizations called Profile Guided Optimization.

When an app is packaged, the d8 dexer takes classes and methods and populates your app's `classes.dex` files. When a user opens the app, these dex files are loaded, one after the other until the app can start. By providing a **Startup Profile** you let d8 know which classes and methods to pack in the first `classes.dex` files. This structure allows the app to load fewer files, which in turn improves startup speed.

Baseline Profiles effectively move the Just in Time (JIT) compilation steps away from user devices and onto developer machines. The generated Ahead Of Time (AOT) compiled code has proven to reduce startup time and rendering issues alike.

## **Trello and Baseline Profiles**

We asked engineers on the Trello app how Baseline Profiles affected their app's performance. After applying Baseline Profiles to their main user journey, Trello saw a significant 25 % reduction in app startup time.

![image.png](/static/blog/assets/image_be5bddd852_Q2Oe7.webp)

Trello was able to improve their app's startup time by 25 % by using baseline profiles.

## **Baseline Profiles at Meta**

Also, engineers at Meta recently published an article on how they are [accelerating their Android apps with Baseline Profiles](https://engineering.fb.com/2025/10/01/android/accelerating-our-android-apps-with-baseline-profiles/).

![image.png](/static/blog/assets/image_557c651300_QsKjS.webp)

Across Meta's apps the teams have seen various critical metrics improve by up to 40 % after applying Baseline Profiles.

**Technical improvements like these help you improve user satisfaction and business success as well. Sharing this with your product owners, CTOs and decision makers can also help speed up your app's performance.**

## **Get started with Baseline Profiles**

To generate either a Baseline or Startup Profile, you write a [macrobenchmark](/topic/performance/benchmarking/macrobenchmark-overview) test that exercises the app. During the test profile data is collected which will be used during app compilation. The tests are written using the new [UiAutomator API](/training/testing/other-components/ui-automator), which we'll cover tomorrow.

Writing a benchmark like this is straightforward and you can see the full sample on [GitHub](https://github.com/android/performance-samples/tree/main/MacrobenchmarkSample).

```
  @Test

fun profileGenerator() {

    rule.collect(

        packageName = TARGET_PACKAGE,

        maxIterations = 15,

        stableIterations = 3,

        includeInStartupProfile = true

    ) {

        uiAutomator {

            startApp(TARGET_PACKAGE)

        }

    }


}
```

## Considerations

Start by writing a macrobenchmark tests Baseline Profile and a Startup Profile for the path most traveled by your users. This means the main entry point that your users take into your app which usually is *after they logged in*. Then continue to write more test cases to capture a more complete picture only for Baseline Profiles. You do not need to cover everything with a Baseline Profile. Stick to the most used paths and measure performance in the field. More on that in tomorrow's post.

## Get started with Profile Guided Optimization

To learn how Baseline Profiles work under the hood, watch this video from the Android Developers Summit:

And check out the Android Build Time episode on Profile Guided Optimization for another in-depth look:

We also have extensive guidance on [Baseline Profiles](/topic/performance/baselineprofiles/overview) and [Startup Profiles](/topic/performance/baselineprofiles/dex-layout-optimizations) available for further reading.

## **Jetpack Compose performance improvements**

The UI framework for Android has seen the performance investment of the engineering team pay off. From version 1.9 of Jetpack Compose, scroll jank has dropped to 0.2 % during an internal long scrolling benchmark test.

![jankyFrames.png](/static/blog/assets/janky_Frames_69aa7bc2c6_Z11r8x3.webp)

These improvements were made possible because of several features packed into the most recent releases.

## Customizable cache window

By default, lazy layouts only compose one item ahead of time in the direction of scrolling, and after something scrolls off screen it is discarded. You can now customize the amount of items to retain through a fraction of the viewport or dp size. This helps your app perform more work upfront, and after enabling pausable composition in between frames, using the available time more efficiently.

To start using customizable cache windows, instantiate a `LazyLayoutCacheWindow` and pass it to your lazy list or lazy grid. Measure your app's performance using different cache window sizes, for example 50% of the viewport. The optimal value will depend on your content's structure and item size.

```
  val dpCacheWindow = LazyLayoutCacheWindow(ahead = 150.dp, behind = 100.dp)

val state = rememberLazyListState(cacheWindow = dpCacheWindow)

LazyColumn(state = state) {

    // column contents

}
```

## Pausable composition

This feature allows compositions to be paused, and their work split up over several frames. The APIs landed in 1.9 and it is now used by default in 1.10 in lazy layout prefetch. You should see the most benefit with complex items with longer composition times.

![image.png](/static/blog/assets/image_d2fb84104a_KYPwr.webp)

## More Compose performance optimizations

In the versions 1.9 and 1.10 of Compose the team also made several optimizations that are a bit less obvious.

Several APIs that use coroutines under the hood have been improved. For example, when using `Draggable` and `Clickable`, developers should see faster reaction times and improved allocation counts.

Optimizations in layout rectangle tracking have improved performance of Modifiers like `onVisibilityChanged()` and `onLayoutRectChanged()`. This speeds up the layout phase, even when not explicitly using these APIs.

Another performance improvement is using cached values when observing positions via `onPlaced()`.

## Prefetch text in the background

Starting with version 1.9, Compose adds the ability to prefetch text on a background thread. This enables you to pre-warm caches to enable faster text layout and is relevant for app rendering performance. During layout, text has to be passed into the Android framework where a word cache is populated. By default this runs on the Ui thread. Offloading prefetching and populating the word cache onto a background thread can speed up layout, especially for longer texts. To prefetch on a background thread you can pass a custom executor to any composable that's using `BasicText` under the hood by passing a `LocalBackgroundTextMeasurementExecutor` to a `CompositionLocalProvider` like so.

```
  val defaultTextMeasurementExecutor = Executors.newSingleThreadExecutor()

CompositionLocalProvider(

    LocalBackgroundTextMeasurementExecutor provides DefaultTextMeasurementExecutor

) {

    BasicText("Some text that should be measured on a background thread!")


}
```

Depending on the text, this can provide a performance boost to your text rendering. To make sure that it improves your app's rendering performance, benchmark and compare the results.

## **Background work performance considerations**

Background Work is an essential part of many apps. You may be using libraries like WorkManager or JobScheduler to perform tasks like:

* Periodically uploading analytical events
* Syncing data between a backend service and a database
* Processing media (i.e. resizing or compressing images)

A key challenge while executing these tasks is balancing performance and power efficiency. WorkManager allows you to achieve this balance. It's designed to be power-efficient, and allow work to be deferred to an optimal execution window influenced by a number of factors, including constraints you specify or constraints imposed by the system.

WorkManager is not a one-size-fits-all solution, though. Android also has a number of power-optimized APIs that are designed specifically with certain common Core User Journeys (CUJs) in mind.

Reference the [Background Work landing page](/develop/background-work) for a list of just a few of these,  including updating a widget and getting location in the background.

## Local Debugging tools for Background Work: Common Scenarios

To debug Background Work and understand why a task may have been delayed or failed, you need visibility into how the system has scheduled your tasks.

To help with this, WorkManager has several related [tools to help you debug locally](/develop/background-work/background-tasks/testing/persistent/debug) and optimize performance (some of these work for JobScheduler as well)! Here are some common scenarios you might encounter when using WorkManager, and an explanation of tools you can use to debug them.

## Debugging why scheduled work is not executing

Scheduled work being delayed or not executing at all can be due to a number of factors, including specified constraints not being met or constraints having been [imposed by the system](/topic/performance/power/power-details).

The first step in investigating why scheduled work is not running is to **confirm the work was successfully scheduled**.  After confirming the scheduling status, determine whether there are any unmet constraints or preconditions preventing the work from executing.

There are several tools for debugging this scenario.

### **Background Task Inspector**

The Background Task Inspector is a powerful tool integrated directly into Android Studio. It provides a visual representation of all WorkManager tasks and their associated states (Running, Enqueued, Failed, Succeeded).

To debug why scheduled work is not executing with the Background Task Inspector, consult the listed Work status(es). An ‘Enqueued' status indicates your Work was scheduled, but is still waiting to run.

**Benefits:** Aside from providing an easy way to view all tasks, this tool is especially useful if you have chained work. The Background Task inspector offers a graph view that can visualize if a previous task failing may have impacted the execution of the following task.

![image.png](/static/blog/assets/image_33bce8e74c_xt83U.webp)

*Background Task Inspector list view*

![image.png](/static/blog/assets/image_2ae46bdf75_ZphdIK.webp)

*Background Task Inspector graph view*

### **adb shell dumpsys jobscheduler**

This [command](/develop/background-work/background-tasks/testing/persistent/debug#use-alb-shell0dumpsys-jobscheduler) returns a list of all active JobScheduler jobs (which includes WorkManager Workers) along with specified constraints, and system-imposed constraints. It also returns job history.

Use this if you want a different way to view your scheduled work and associated constraints. For WorkManager versions earlier than WorkManager 2.10.0, `adb shell dumpsys jobscheduler` will return a list of Workers with this name:

```
  [package name]/androidx.work.impl.background.systemjob.SystemJobService
```

If your app has multiple workers, updating to WorkManager 2.10.0 will allow you to see Worker names and easily distinguish between workers:

```
  #WorkerName#@[package name]/androidx.work.impl.background.systemjob.SystemJobService
```

**Benefits:**This command is useful for understanding if there were any *system-imposed constraints,*which you cannot determine with the Background Task Inspector. For example, this will return your [app's standby bucket](/topic/performance/power/power-details#app-stdby-bucket), which can affect the window in which scheduled work completes.

### **Enable Debug logging**

You can enable [custom logging](/develop/background-work/background-tasks/testing/persistent/debug#enable-logging) to see verbose WorkManager logs, which will have `WM—` attached.

**Benefits:** This allows you to gain visibility into when work is scheduled, constraints are fulfilled, and lifecycle events, and you can consult these logs while developing your app.

### **WorkInfo.StopReason**

If you notice unpredictable performance with a specific worker, you can programmatically observe the reason your worker was stopped on the previous run attempt with [`WorkInfo.getStopReason`](/reference/androidx/work/WorkInfo).

It's a good practice to configure your app to observe WorkInfo using getWorkInfoByIdFlow to identify if your work is being affected by background restrictions, constraints, frequent timeouts, or even stopped by the user.

**Benefits:** You can use WorkInfo.StopReason to collect field data about your workers' performance.

## Debugging WorkManager-attributed high wake lock duration flagged by Android vitals

Android vitals features an excessive partial wake locks metric, which highlights wake locks contributing to battery drain. You may be surprised to know that [WorkManager acquires wake locks to execute tasks](/develop/background-work/background-tasks/awake/wakelock/identify-wls#workmanager), and if the wake locks exceed the threshold set by Google Play, can have impacts to your app's visibility. How can you debug why there is so much wake lock duration attributed to your work? You can use the following tools.

### **Android vitals dashboard**

First confirm in the [Android vitals excessive wake lock dashboard](https://play.google.com/console/developers/app/vitals/metrics/details?metric=EXCESSIVE_BACKGROUND_WAKELOCKS&days=28) that the high wake lock duration *is* from WorkManager and not an alarm or other wake lock. You can use the [Identify wake locks created by other APIs](/develop/background-work/background-tasks/awake/wakelock/identify-wls) documentation to understand which wake locks are held due to WorkManager.

### **Perfetto**

[Perfetto](http://ui.perfetto.dev/) is a tool for analyzing system traces. When using it for debugging WorkManager specifically, you can view the “Device State” section to see when your work started, how long it ran, and how it contributes to power consumption.

Under “Device State: Jobs” track,  you can see any workers that have been executed and their associated wake locks.

![deviceState.png](/static/blog/assets/device_State_08fad1075f_1djS9E.webp)

*Device State section in Perfetto, showing CleanupWorker and BlurWorker execution.*

### **Resources**

Consult the [Debug WorkManager page](/develop/background-work/background-tasks/testing/persistent/debug) for an overview of the available debugging methods for other scenarios you might encounter.

And to try some of these methods hands on and learn more about debugging WorkManager, check out the [Advanced WorkManager and Testing](/codelabs/basic-android-kotlin-compose-verify-background-work#0) codelab.

## **Next steps**

Today we moved beyond code shrinking and explored how the Android Runtime and Jetpack Compose actually render your app. Whether it’s pre-compiling critical paths with Baseline Profiles or smoothing out scroll states with the new Compose 1.9 and 1.10 features, these tools focus on the *feel* of your app. And we dove deep into best practices on debugging background work.

## Ask Android

On Friday we're hosting a live AMA on performance. Ask your questions now using #AskAndroid and get them answered by the experts.

## The challenge

We challenged you on Monday to enable R8. Today, we are asking you to **generate one Baseline Profile** for your app.

With **Android Studio Otter**, the Baseline Profile Generator module wizard makes this easier than ever. Pick your most critical user journey—even if it’s just your app startup and login—and generate a profile.

Once you have it, run a Macrobenchmark to compare `CompilationMode.None` vs. `CompilationMode.Partial`.

Share your startup time improvements on social media using **#optimizationEnabled**.

## Tune in tomorrow

You have shrunk your app with R8 and optimized your runtime with Profile Guided Optimization. But how do you *prove* these wins to your stakeholders? And how do you catch regressions before they hit production?

Join us tomorrow for **Day 4: The Performance Leveling Guide**, where we will map out exactly how to measure your success, from field data in Play Vitals to deep local tracing with Perfetto.

###### Written by:

* ## [Ben Weiss](/blog/authors/ben-weiss)

  ###### Developer Relations Engineer

  [read\_more
  View profile](/blog/authors/ben-weiss)

  ![](/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)

  ![](/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)
* ## [Breana Tate](/blog/authors/breana-tate)

  ###### Developer Relations Engineer

  [read\_more
  View profile](/blog/authors/breana-tate)

  ![](/static/blog/assets/Breana_Tate_24c1d03bf2_Z1NRigS.webp)

  ![](/static/blog/assets/Breana_Tate_24c1d03bf2_Z1NRigS.webp)
* ## [Jossi Wolf](/blog/authors/jossi-wolf)

  ###### Software Engineer

  [read\_more
  View profile](/blog/authors/jossi-wolf)

  ![](/static/blog/assets/Jossi_Wolf_d703979815_1D5j3e.webp)

  ![](/static/blog/assets/Jossi_Wolf_d703979815_1D5j3e.webp)

## Continue reading

* [![](/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)](/blog/authors/ben-weiss)

  17

  Nov
  2025

  17

  Nov
  2025

  ![](/static/blog/assets/performance_Week9_2c643934fa_p8Pb2.webp)

  #### [How-tos](/blog/categories/how-tos)

  ## [Get your app on the fast track with Android Performance Spotlight Week!](/blog/posts/get-your-app-on-the-fast-track-with-android-performance-spotlight-week)

  [arrow\_forward](/blog/posts/get-your-app-on-the-fast-track-with-android-performance-spotlight-week)

  When working on new features, app performance often takes a back seat. However, while it's not always top of mind for developers, users can see exactly where your app's performance lags behind.

  ###### [Ben Weiss](/blog/authors/ben-weiss) • 3 min read

  + [#Performance](/blog/topics/performance)
  + [#R8](/blog/topics/r8)
* [![](/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)](/blog/authors/alice-yuan)

  04

  Mar
  2026

  04

  Mar
  2026

  ![](/static/blog/assets/battery_Performance_08d6713f94_Z1IAO0P.webp)

  #### [How-tos](/blog/categories/how-tos)

  ## [Battery Technical Quality Enforcement is Here: How to Optimize Common Wake Lock Use Cases](/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases)

  [arrow\_forward](/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases)

  In recognition that excessive battery drain is top of mind for Android users, Google has been taking significant steps to help developers build more power-efficient apps.

  ###### [Alice Yuan](/blog/authors/alice-yuan) • 8 min read
* [![](/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](/blog/authors/thomas-ezan)[![](/static/blog/assets/Ivy_Knight_3071ce592d_2j4ER1.webp)](/blog/authors/ivy-knight)

  02

  Dec
  2025

  02

  Dec
  2025

  ![](/static/blog/assets/sample_readme_bazel_9348d9f325_Z57CJe.webp)

  #### [How-tos](/blog/categories/how-tos)

  ## [Explore AI on Android with Our Sample Catalog App](/blog/posts/explore-ai-on-android-with-our-sample-catalog-app)

  [arrow\_forward](/blog/posts/explore-ai-on-android-with-our-sample-catalog-app)

  We wanted to provide you with examples of AI-enabled features using both on-device and Cloud models and inspire you to create delightful experiences for your users.

  ###### [Thomas Ezan](/blog/authors/thomas-ezan), [Ivy Knight](/blog/authors/ivy-knight) • 2 min read

# Stay in the loop

Get the latest Android development insights delivered to your inbox
weekly.

[mail
Subscribe](/subscribe)

![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)