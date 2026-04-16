---
title: https://developer.android.com/blog/posts/leveling-guide-for-your-performance-journey
url: https://developer.android.com/blog/posts/leveling-guide-for-your-performance-journey
source: md.txt
---

#### [How-tos](https://developer.android.com/blog/categories/how-tos)

# Leveling Guide for your Performance Journey

###### 9-min read

![](https://developer.android.com/static/blog/assets/performance_Week8_4d6efcacbe_ZI6a5e.webp) 20 Nov 2025 [![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)](https://developer.android.com/blog/authors/alice-yuan) [##### Alice Yuan](https://developer.android.com/blog/authors/alice-yuan)

###### Developer Relations Engineer

**Leveling Guide for your Performance Journey**

Welcome to day 4 of Performance Spotlight Week. Now that you've learned about some of the awesome tools and best practices we've introduced recently such as the [R8 Optimizer](http://d.android.com/r8), and Profile Guided Optimization with [Baseline Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview) and [Startup Profiles](https://developer.android.com/topic/performance/baselineprofiles/dex-layout-optimizations), you might be wondering where to start your performance improvement journey.

We've come up with a step-by-step performance leveling guide to meet your mobile development team where you are---whether you're an app with a single developer looking to get started with performance, or you have an entire team dedicated to improving Android performance.

The performance leveling guide features 5 levels. We'll start with level 1, which introduces minimal adoption effort performance tooling, and we'll go up to level 5, ideal for apps that have the resourcing to maintain a bespoke performance framework.

<br />

Feel free to jump to the level that resonates most with you:

- [Level 1: Use Play Console provided field monitoring](https://docs.google.com/document/d/1KU461XfG9MX6rbyL5dEu81oyuwhugeMSx0qgM7t98_8/edit?resourcekey=0-rS4v80rH-CsHHON3i7TxAw&tab=t.9545yu9a8hu#heading=h.q7g5xad1u72f)
- [Level 2: Follow the App Performance Score action items](https://docs.google.com/document/d/1KU461XfG9MX6rbyL5dEu81oyuwhugeMSx0qgM7t98_8/edit?resourcekey=0-rS4v80rH-CsHHON3i7TxAw&tab=t.9545yu9a8hu#heading=h.bmmrmlrl1cx)
- [Level 3: Leverage local performance test frameworks](https://docs.google.com/document/d/1KU461XfG9MX6rbyL5dEu81oyuwhugeMSx0qgM7t98_8/edit?resourcekey=0-rS4v80rH-CsHHON3i7TxAw&tab=t.9545yu9a8hu#heading=h.ol5g0pdijonl)
- [Level 4: Use trace analysis tools like Perfetto](https://docs.google.com/document/d/1KU461XfG9MX6rbyL5dEu81oyuwhugeMSx0qgM7t98_8/edit?resourcekey=0-rS4v80rH-CsHHON3i7TxAw&tab=t.9545yu9a8hu#heading=h.dkfldbvxyw0j)
- [Level 5: Build your own performance tracking framework](https://docs.google.com/document/d/1KU461XfG9MX6rbyL5dEu81oyuwhugeMSx0qgM7t98_8/edit?resourcekey=0-rS4v80rH-CsHHON3i7TxAw&tab=t.9545yu9a8hu#heading=h.uimonjgw1jv3)

## **Level 1: Use Play Console provided field monitoring**

We recommend first leveraging Android vitals within the Play Console for viewing automatically collected field monitoring data, giving you insights about your application with minimal effort.

Android vitals is Google's initiative to automatically collect and surface this field data for you.

Here's an explanation of how we deliver this data:

1. **Collect Data:**When a user opts-in, their Android device automatically logs key performance and stability events from all apps, including yours.
2. **Aggregate Data:** Google Play collects and anonymizes this data from your app's users.
3. **Surface Insights:** The data is presented to you in the [Android vitals dashboard](https://play.google.com/console/developers/app/vitals/metrics/overview) within your Google Play Console.

The Android vitals dashboard tracks many metrics, but a few are designated as **Core Vitals**. These are the most important because they can affect your app's visibility and ranking on the Google Play Store.

## The Core Vitals

|---|---|
| **GOOGLE PLAY'S CORE TECHNICAL QUALITY METRICS** To maximize visibility on Google Play, keep your app below the bad behavior thresholds for these metrics. ||
| User-perceived crash rate | The percentage of daily active users who experienced at least one crash that is likely to have been noticeable |
| User-perceived ANR rate | The percentage of daily active users who experienced at least one ANR that is likely to have been noticeable |
| Excessive battery usage | The percentage of watch face sessions where battery usage exceeds 4.44% per hour |
| New: Excessive partial wake locks | The percentage of user sessions where cumulative, non-exempt wake lock usage exceeds 2 hours |

The core vitals include user-perceived crash rate, ANR rate, excessive battery usage and the newly introduced metric on excessive partial wake locks.

## User-Perceived ANR Rate

You can use the [Android Vitals ANR dashboard](https://play.google.com/console/developers/app/vitals/metrics/details?metric=USER_PERCEIVED_ANRS&days=28), to see stack traces of issues that occur in the field and get insights and recommendations on how to fix the issue.
![crashesAnrs.png](https://developer.android.com/static/blog/assets/crashes_Anrs_3436f1007a_Z2uRNHL.webp)

You can drill down into a specific ANR that occurred, to see the stack trace as well as insights on what might be causing the issue.
![insights.png](https://developer.android.com/static/blog/assets/insights_d96436488b_Z2hT5n8.webp)

Also, check out our [ANR guidance](http://goo.gle/fix-anr) to help you diagnose and fix the common scenarios where ANRs might occur.

## User-Perceived Crash Rate

Use the [Android vitals crash dashboard](https://play.google.com/console/developers/app/vitals/metrics/details?metric=USER_PERCEIVED_CRASHES&days=28) to further debug crashes and view a sample of stack traces that occur within your app.

Our documentation also has guidance around troubleshooting specific crashes. For example, the [Troubleshoot foreground services guide](https://developer.android.com/develop/background-work/services/fgs/troubleshooting) discusses ways to identify and fix common scenarios where crashes occur.

## Excessive Battery Usage

To decrease watch face sessions with excessive battery usage on Wear OS, check out the [Wear guide on how to improve and conserve battery](https://developer.android.com/training/wearables/apps/power).

## \[new\] Excessive Partial Wake Locks

[Video](https://www.youtube.com/watch?v=-6mEvkLOlno)

We recently announced that apps that exceed the excessive partial wake locks threshold may see additional treatment starting on **March 1st 2026**.

For mobile devices, the Android vitals metric applies to non-exempted wake locks acquired while the screen is off and the app is in the background or running a foreground service. Android vitals considers partial wake lock usage excessive if wake locks are held for at least two hours within a 24-hour period and it affects more than 5% of your app's sessions, averaged over 28 days.

To debug and fix excessive wake lock issues, check out our [technical blog post](https://android-developers.googleblog.com/2025/09/guide-to-excessive-wake-lock-usage.html).

Consult our [Android vitals documentation](https://developer.android.com/topic/performance/vitals) and continue your journey to better leverage Android vitals.

## **Level 2: Follow the App Performance Score action items**

Next, move onto using the [App Performance Score](https://developer.android.com/topic/performance/app-score) to find the high leverage action items to uplevel your app performance.

The Android App Performance Score is a standardized framework to measure your app's technical performance. It gives you a score between 0 and 100, where a lower number indicates more room for improvement.

To get easy wins, you should first start with the **Static Performance Score** first. These are often configuration changes or tooling updates that provide significant performance boosts.

## Step 1: Perform the Static Assessment

The static assessment evaluates your project's configuration and tooling adoption. These are often the quickest ways to improve performance.

Navigate to the [Static Score section](https://developer.android.com/topic/performance/app-score#static-score) of the scoreboard page and do the following:

1. Assess Android Gradle Plugin (AGP) Version.
2. Adopt R8 Minification [incrementally](https://developer.android.com/topic/performance/app-optimization/adopt-optimizations-incrementally) or ideally, use [R8 in full mode](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization?_gl=1*wgy2ut*_up*MQ..*_ga*ODc2OTYyOTY0LjE3NjI4OTk2NjI.*_ga_6HH9YJMN9M*czE3NjI4OTk2NjIkbzEkZzAkdDE3NjI4OTk2NjIkajYwJGwwJGgxNTU3NzkxNDUz#r8-optimization-settings) to minify and optimize the app code.
3. Adopt [Baseline](https://developer.android.com/topic/performance/baselineprofiles/overview) Profiles which improves code execution speed from the first launch providing performance enhancements for every new app install and every app update.
4. Adopt [Startup Profiles](https://developer.android.com/topic/performance/baselineprofiles/dex-layout-optimizations) to improve Dex Layout. Startup Profiles are used by the build system to further optimize the classes and methods they contain by improving the layout of code in your APK's DEX files.
5. Upgrade to the newest version of Jetpack Compose

## Step 2: Perform the Dynamic Assessment

Once you have applied the static easy wins, use the dynamic assessment to validate the improvements on a real device. You can first do this manually with a physical device and a stop watch.

Navigate to the [Dynamic Score section](https://developer.android.com/topic/performance/app-score%23dynamic-score) of the scoreboard page and do the following:

1. Set up your test environment with a physical device. Consider using a lower-end device to exaggerate performance issues, making them easier to spot.
2. Measure startup time from the launcher. Cold start your app from the launcher icon and measure the time until it is interactive.
3. Measure app startup time from a notification, with the goal to reduce notification startup time to be below a couple seconds.
4. Measure rendering performance by scrolling through your core screens and animations.

Once you've completed these steps, you will receive a score between 1 - 100 for the static and dynamic scores, giving you an understanding of your app's performance and where to focus on.

## **Level 3: Leverage local performance test frameworks**

Once you've started to assess dynamic performance, you may find it too tedious to measure performance manually. Consider automating your performance testing using performance test frameworks such as Macrobenchmarks and UiAutomator.

## Macrobenchmark 💚 UiAutomator

Think of Macrobenchmark and UiAutomator as two tools that work together: Macrobenchmark is the measurement tool. It's like a stopwatch and a frame-rate counter that runs outside your app. It is responsible for starting your app, recording metrics (like startup time or dropped frames), and stopping the app. UiAutomator is the robot user. The library lets you write code to interact with the device's screen. It can find an icon, tap a button, scroll on a list and more.

### **How to write a test**

When you write a test, you wrap your UiAutomator code inside a Macrobenchmark block.

1. **Define the Test:** Use the `@MacrobenchmarkRule`
2. **Start Measuring:** Call `benchmarkRule.measureRepeated`.
3. **Drive the UI:** Inside that block, use UiAutomator code to launch your app, find UI elements, and interact with them.

Here's an example code snippet of what it looks like to test a compose list for scrolling jank.

```
benchmarkRule.measureRepeated(

    // ...

    metrics = listOf(

        FrameTimingMetric(),

    ),

    startupMode = StartupMode.COLD,

    iterations = 10,

) {

    // 1. Launch the app's main activity

    startApp()

    // 2. Find the list using its resource ID and scroll down

    onElement { viewIdResourceName == "$packageName.my_list" }

        .fling(Direction.DOWN)

}
```

4. **Review the results**: Each test run provides you with precisely measured information to give you the best data on your app's performance.

```
timeToInitialDisplayMs  min  1894.4,   median 2847.4,   max  3355.6


frameOverrunMs          P50 -3.2,  P90  6.2, P95  10.4, P99  119.5
```

### **Common use cases**

Macrobenchmark provides several core metrics out of the box. `StartupTimingMetric` allows you to accurately measure app startup. The `FrameTimingMetric` enables you to understand an app's rendering performance during the test.

We have a detailed and complete guide to using [Macrobenchmarks](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview) and [UiAutomator](https://developer.android.com/training/testing/other-components/ui-automator) alongside [code samples](https://developer.android.com/training/testing/other-components/ui-automator) available for you to continue learning.

## **Level 4: Use trace analysis tools like Perfetto**

Trace analysis tools like Perfetto are used when you need to see beyond your own application code. Unlike standard debuggers or profilers that only see your process, Perfetto captures the entire device state---kernel scheduling, CPU frequency, other processes, and system services---giving you complete context for performance issues.

Check our [Performance Debugging youtube playlist](https://www.youtube.com/watch?v=phhLFicMacY) for video instructions on performance debugging using system traces, Android Studio Profiler and Perfetto.

## How to use Perfetto to debug performance

The general workflow for debugging performance using trace analysis tools is to record, load and analyze the trace.

### **Step 1: Record a trace**

You can record a system trace using several methods:

- Recording a trace manually on the device [directly from the developer options](https://developer.android.com/topic/performance/tracing/on-device).
- Using the [Android Studio CPU Profiler](https://developer.android.com/studio/profile)
- Using the [Perfetto UI](https://perfetto.dev/docs/getting-started/system-tracing)

### **Step 2: Load the trace**

Once you have the trace file, you need to load it into the analysis tool.

1. Open Chrome and navigate to [ui.perfetto.dev](https://ui.perfetto.dev/).
2. Drag and drop your `.perfetto-trace` (or `.pftrace`) file directly into the browser window.
3. The UI will process the file and display the timeline.

### **Step 3: Analyze the trace**

[Video](https://www.youtube.com/watch?v=phhLFicMacY)

You can use Perfetto UI or Android Studio Profiler to investigate performance issues. Check out this episode of the MAD Skills series on Performance, where our performance engineer Carmen Jackson discusses the Perfetto traceviewer.

## Scenarios for inspecting system traces using Perfetto

Perfetto is an expert tool and can provide information about everything that happened on the Android device while a trace was captured. This is particularly helpful when you cannot identify the root cause of a slowdown using standard logs or basic profilers.

### **Debugging Jank (Dropped Frames)**

If your app stutters while scrolling, Perfetto can show you exactly why a specific frame missed its deadline.

If it's due to the app, you might see your main thread running for a long duration doing heavy parsing; this indicates scenarios where you should move the work into asynchronous processing.

If it's due to the system, you might see your main thread ready to run, but the CPU kernel scheduler gave priority to a different system service, leaving your app waiting (CPU contention). This indicates scenarios where you may need to optimize usage of platform APIs.

### **Analyzing Slow App Startup**

Startup is complex, involving system init, process forking, and resource loading. Perfetto visualizes this timeline precisely.

You can see if you are waiting on Binder calls (inter-process communication). If your `onCreate` waits a long time for a response from the system `PackageManager`, Perfetto will show that blocked state clearly.

You can also see if your app is doing more work than necessary during the app startup. For example, if you are creating and laying out more views than the app needs to show, you can see these operations in the trace.

### **Investigating Battery Drain \& CPU Usage**

Because Perfetto sees the whole system, it's perfect for finding invisible power drains.

You can identify which processes are holding wake locks, preventing the device from sleeping under the "Device State" tracks. Learn more in our [wake locks blog post](https://android-developers.googleblog.com/2025/09/guide-to-excessive-wake-lock-usage.html). Also, use Perfetto to see if your background jobs are running too frequently or waking up the CPU unnecessarily.

## **Level 5: Build your own performance tracking framework**

The final level is for apps that have teams with resourcing to maintain a performance tracking framework.

Building a custom performance tracking framework on Android involves leveraging several system APIs to capture data throughout the application lifecycle, from startup to exit, and during specific high-load scenarios.

By using `ApplicationStartInfo`, `ProfilingManager`, and `ApplicationExitInfo`, you can create a robust telemetry system that reports on how your app started, detailed info on what it did while running, and why it died.

## ApplicationStartInfo: Tracking how the app started

Available from Android 15 (API 35), [ApplicationStartInfo](https://developer.android.com/reference/android/app/ApplicationStartInfo) provides detailed metrics about app startup in the field. The data includes whether it was a cold, warm, or hot start, and the duration of different startup phases.

This helps you develop a baseline startup metric using production data to further optimize that might be hard to reproduce locally. You can use these metrics to run A/B tests optimizing the startup flow.

The goal is to accurately record launch metrics without manually instrumenting every initialization phase.

You can query this data lazily some time after application launch.

## ProfilingManager: Capturing why it was slow

[ProfilingManager](https://developer.android.com/reference/android/os/ProfilingManager) (API 35) allows your app to programmatically trigger system traces on user devices. This is powerful for catching transient performance issues in the wild that you can't reproduce locally.

The goal is to automatically record a trace when a specific highly critical user journey is detected as running slowly or experiencing performance issues.

You can register a listener that triggers when specific conditions are met or trigger it manually when you detect a performance issue such as jank, excessive memory, or battery drain.

Check our documentation on [how to capture a profile](https://developer.android.com/topic/performance/tracing/profiling-manager/how-to-capture), [retrieve and analyze profiling data](https://developer.android.com/topic/performance/tracing/profiling-manager/retrieve-and-analyze) and use [debug commands.](https://developer.android.com/topic/performance/tracing/profiling-manager/debug-mode)

## ApplicationExitInfo: Tracking why the app died

[ApplicationExitInfo](https://developer.android.com/reference/android/app/ApplicationExitInfo) (API 30) tells you why your previous process died. This is crucial for finding native crashes, ANRs, or system kills due to excessive memory usage (OOM). You'll also be able to get a detailed tombstone trace by using the API [getTraceInputStream](https://developer.android.com/reference/android/app/ApplicationExitInfo#getTraceInputStream()).

The goal of the API is to understand stability issues that don't trigger standard Java crash reporters (like Low Memory Kills).

You should trigger this API on* *the next app launch.

## **Next Steps**

Improving Android performance is a step-by-step journey. We're so excited to see how you level up your performance using these tools!

## Tune in tomorrow for Ask Android

You have shrunk your app with R8 and optimized your runtime with Profile Guided Optimization. And measure your app's performance.

Join us tomorrow for the live Ask Android session. Ask your questions now using #AskAndroid and get them answered by the experts.

###### Written by:

-

  ## [Alice Yuan](https://developer.android.com/blog/authors/alice-yuan)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/alice-yuan) ![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp) ![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)](https://developer.android.com/blog/authors/alice-yuan) 04 Mar 2026 04 Mar 2026 ![](https://developer.android.com/static/blog/assets/battery_Performance_08d6713f94_Z1IAO0P.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Battery Technical Quality Enforcement is Here: How to Optimize Common Wake Lock Use Cases](https://developer.android.com/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases)

  [arrow_forward](https://developer.android.com/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases) In recognition that excessive battery drain is top of mind for Android users, Google has been taking significant steps to help developers build more power-efficient apps.

  ###### [Alice Yuan](https://developer.android.com/blog/authors/alice-yuan) •
  8 min read

- [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan)[![](https://developer.android.com/static/blog/assets/Ivy_Knight_3071ce592d_2j4ER1.webp)](https://developer.android.com/blog/authors/ivy-knight) 02 Dec 2025 02 Dec 2025 ![](https://developer.android.com/static/blog/assets/sample_readme_bazel_9348d9f325_Z57CJe.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Explore AI on Android with Our Sample Catalog App](https://developer.android.com/blog/posts/explore-ai-on-android-with-our-sample-catalog-app)

  [arrow_forward](https://developer.android.com/blog/posts/explore-ai-on-android-with-our-sample-catalog-app) We wanted to provide you with examples of AI-enabled features using both on-device and Cloud models and inspire you to create delightful experiences for your users.

  ###### [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan), [Ivy Knight](https://developer.android.com/blog/authors/ivy-knight) •
  2 min read

- 3 Authors 19 Nov 2025 19 Nov 2025 ![](https://developer.android.com/static/blog/assets/performance_Week11_efe6dd10be_Z1PApe6.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Deeper Performance Considerations](https://developer.android.com/blog/posts/deeper-performance-considerations)

  [arrow_forward](https://developer.android.com/blog/posts/deeper-performance-considerations) We're covering Profile Guided Optimization, Jetpack Compose performance improvements and considerations on working behind the scenes.

  ###### [Ben Weiss](https://developer.android.com/blog/authors/ben-weiss), [Breana Tate](https://developer.android.com/blog/authors/breana-tate), [Jossi Wolf](https://developer.android.com/blog/authors/jossi-wolf) •
  8 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)