---
title: https://developer.android.com/topic/performance/appstartup/analysis-optimization
url: https://developer.android.com/topic/performance/appstartup/analysis-optimization
source: md.txt
---

# App startup analysis and optimization

During app startup, your app makes the first impression on users. App startup must be quick to load and display information the user needs to use your app. If your app takes too long to start up, users might exit your app because they are waiting too long.

We recommend using the Macrobenchmark library to[measure startup](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics#startup-timing). The library provides an overview and detailed system traces to see exactly what's happening during startup.

System traces provide useful information about what's happening on your device, which helps you understand what your app is doing during startup and identify potential areas for optimization.

To analyze your app startup, do the following:

- [Set up an environment](https://developer.android.com/topic/performance/appstartup/setup-env)to record traces for app startup.
- Understand[system traces](https://developer.android.com/topic/performance/tracing).
- Navigate a trace report using[Android Studio Profilers](https://developer.android.com/studio/profile)or[Perfetto](https://perfetto.dev/docs/visualization/perfetto-ui).

## Steps to analyze and optimize startup

Apps often need to load specific resources during startup that are critical to end users. Non-essential resources can wait to load until after startup completes.

To make performance tradeoffs, consider the following:

- Use the Macrobenchmark library to measure the time taken by each operation, and identify blocks that take a long time to complete.

- Confirm that the resource-intensive operation is critical to app startup. If the operation can wait until the app is fully drawn, it can help minimize resource constraints at startup.

- Ensure that you expect this operation to run at app startup. Often, unnecessary operations can be called from legacy code or third-party libraries.

- Move long-running operations to the background, if possible. Background processes can still affect CPU usage during startup.

After you fully investigate the operation, you can decide on the tradeoff between the time it takes to load and the necessity of including it in app startup. Remember to include the potential for regression or breaking changes when altering the workflow of your app.

Optimize and re-measure until you're satisfied with the startup time for your app. For more information, see[Use metrics to detect and diagnose problems](https://developer.android.com/topic/performance/vitals/launch-time#ddp).

## Measure and analyze time spent in major operations

When you have a complete app startup trace, look at the trace and measure time taken for major operations like`bindApplication`or`activityStart`. We recommend using[Perfetto](https://ui.perfetto.dev/)or the[Android Studio Profilers](https://developer.android.com/studio/profile)to analyze these traces.

Look at the overall time spent during app startup to identify any operations that do the following:

- Occupy large time frames and can be optimized. Every millisecond counts in performance. For example, look for[`Choreographer`](https://developer.android.com/reference/android/view/Choreographer)draw times, layout inflation times, library load times,[`Binder`](https://developer.android.com/reference/android/os/Binder)transactions, or resource load times. For a general start, look at all operations that take longer than 20ms.
- Block the main thread. For more information, see[Navigate a Systrace report](https://developer.android.com/topic/performance/tracing/navigate-report).
- Don't need to run during startup.
- Can wait until after your first frame is drawn.

Investigate each of these traces further to find performance gaps.

### Identify expensive operations on the main thread

It's best practice to keep expensive operations such as file I/O and network access off the main thread. This is equally important during app startup, because expensive operations on the main thread can make the app unresponsive and delay other critical operations.[`StrictMode.ThreadPolicy`](https://developer.android.com/reference/android/os/StrictMode.ThreadPolicy)can help identify cases where expensive operations are happening on the main thread. It's good practice to enable[`StrictMode`](https://developer.android.com/reference/android/os/StrictMode)on debug builds to identify problems as early as possible, as shown in the following example:  

### Kotlin

```kotlin
class MyApplication : Application() {

    override fun onCreate() {
        super.onCreate()

        ...
        if (BuildConfig.DEBUG)
            StrictMode.setThreadPolicy(
                StrictMode.ThreadPolicy.Builder()
                    .detectAll()
                    .penaltyDeath()
                    .build()
            )
        ...
    }
}
```

### Java

```java
public class MyApplication extends Application {

    @Override
    public void onCreate() {
        super.onCreate();

        ...
        if(BuildConfig.DEBUG) {
            StrictMode.setThreadPolicy(
                    new StrictMode.ThreadPolicy.Builder()
                            .detectAll()
                            .penaltyDeath()
                            .build()
            );
        }
        ...
    }
}
```

Using`StrictMode.ThreadPolicy`enables the thread policy on all debug builds and crashes the app whenever violations of the thread policy are detected, which makes it difficult to miss thread policy violations.

### TTID and TTFD

To see the time it takes the app to produce its first frame, measure the[time to initial display](https://developer.android.com/topic/performance/vitals/launch-time#time-initial)(TTID). However, this metric doesn't necessarily reflect the time until the user can start interacting with your app. The[time to full display](https://developer.android.com/topic/performance/vitals/launch-time#time-full)(TTFD) metric is more useful in measuring and optimizing the code paths necessary to have a fully useable app state.

For strategies on reporting when the app UI is fully drawn, see[Improve startup timing accuracy](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics#startup-accuracy).

Optimize for both TTID and TTFD, because both are important in their own areas. A short TTID helps the user see that the app is actually launching. Keeping the TTFD short is important to help ensure that the user can start interacting with the app quickly.

## Analyze overall thread state

Select the app startup time and look at overall thread slices. The main thread needs to be responsive at all times.

Tools such as the[Android Studio Profiler](https://developer.android.com/studio/profile)and[Perfetto](https://perfetto.dev/docs/visualization/perfetto-ui)provide a detailed overview of the main thread and how much time is spent in each stage. For more information about visualizing perfetto traces, see the[Perfetto UI](https://perfetto.dev/docs/visualization/perfetto-ui)documentation.

### Identify major chunks of main thread sleeping state

If there's a lot of time spent sleeping, it's likely a result of your app's main thread waiting for work to complete. If you have a multithreaded app, identify the thread that your main thread is waiting on and consider optimizing these operations. It can also be useful to ensure there's no unnecessary lock contention causing delays in your critical path.

### Reduce main thread blocking and uninterruptible sleep

Look for every instance of the main thread going into a blocked state. Perfetto and Studio Profiler show this with an orange indicator on the thread state timeline. Identify the operations, explore if these are expected or can be avoided, and optimize where necessary.

IO-related interruptible sleep can be a really good opportunity for improvement. Other processes doing IO, even if they're unrelated apps, can contend with the IO that the top app is doing.

### Improve startup time

After you identify an opportunity for optimization, explore possible solutions to help improve startup times:

- Load content lazily and asynchronously to speed up[TTID](https://developer.android.com/topic/performance/vitals/launch-time#time-initial).
- Minimize calling functions that make binder calls. If they're unavoidable, ensure that you're optimizing those calls by caching values instead of repeating calls or moving non-blocking work to background threads.
- To make your app startup appear faster, you can display something that requires minimal rendering to the user as quickly as possible until the rest of the screen is finished loading.
- Create and add add a[startup profile](https://developer.android.com/topic/performance/baselineprofiles/overview#startup-profiles)to your app.
- Use the Jetpack[App Startup library](https://developer.android.com/topic/libraries/app-startup)to streamline the initialization of components during app startup.

## Analyze UI performance

App startup includes a splash screen and the loading time of your home page. To optimize app startup, inspect traces to understand the time taken for your UI to be drawn.

### Limit work on initialization

Certain frames might take more time to load than others. These are considered expensive draws for the app.

To optimize initialization, do the following:

- Prioritize slow layout passes and pick these for improvements.
- Investigate each warning from Perfetto and alert from Systrace by adding[custom trace events](https://developer.android.com/topic/performance/tracing/custom-events)to reduce expensive draws and delays.

### Measure frame data

There are multiple ways to measure frame data. The five main collection methods are:

- **Local collection using`dumpsys gfxinfo`:** Not all frames observed in the dumpsys data are responsible for the slow rendering of your app or have any impact to end users. However, this is a good measure to look at across different release cycles to understand the general trend of performance. To learn more about using`gfxinfo`and`framestats`to integrate UI performance measurements into your testing practices, see[Fundamentals of testing Android apps](https://developer.android.com/training/testing/performance).
- **Field collection using[JankStats](https://developer.android.com/topic/performance/jankstats):** Collect frame render times from specific parts of your app with[JankStats library](https://developer.android.com/studio/profile/jankstats)and record and analyze the data.
- **In tests using Macrobenchmark (Perfetto under the hood)**
- **[Perfetto FrameTimeline](https://perfetto.dev/docs/data-sources/frametimeline):** On Android 12 (API level 31), you can collect[Frame timeline metrics](https://perfetto.dev/docs/data-sources/frametimeline)from a Perfetto trace to which work is causing the frame drop. This can be the first step to diagnosing why frames are dropped.
- **Android Studio Profiler for[jank detection](https://developer.android.com/studio/profile/jank-detection)**

### Check main activity load time

Your app's main activity might contain a large amount of information that is loaded from multiple sources. Check the home`Activity`layout, and specifically look at the[`Choreographer.onDraw`](https://developer.android.com/reference/android/view/Choreographer)method of the home activity.

- Use[`reportFullyDrawn`](https://developer.android.com/reference/android/app/Activity#reportFullyDrawn())to report to the system that your app is now fully drawn for optimization purposes.
- Measure activity and app launches using[`StartupTimingMetric`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/StartupTimingMetric)with the Macrobenchmark library.
- Look at frame drops.
- Identify layouts taking a long time to render or measure.
- Identify assets taking a long time to load.
- Identify unnecessary layouts that are inflated during startup.

Consider these possible solutions to optimize main activity load time:

- Make your initial layout as basic as possible. For more information, see[Optimize layout hierarchies](https://developer.android.com/training/improving-layouts/optimizing-layouts).
- Add custom tracepoints to provide more information about dropped frames and complex layouts.
- Minimize the number and size of bitmap resources loaded during startup.
- Use[`ViewStub`](https://developer.android.com/reference/android/view/ViewStub)where layouts aren't immediately`VISIBLE`. A`ViewStub`is an invisible, zero-sized View that can be used to lazily inflate layout resources at runtime. For more information, see[`ViewStub`](https://developer.android.com/reference/android/view/ViewStub).

  If you are using[Jetpack Compose](https://developer.android.com/jetpack/compose), you can get similar behavior to`ViewStub`using state to defer loading some components:  

      var shouldLoad by remember {mutableStateOf(false)}

      if (shouldLoad) {
       MyComposable()
      }

  Load the composeables inside the conditional block by modifying`shouldLoad`:  

      LaunchedEffect(Unit) {
       shouldLoad = true
      }

  This triggers a recomposition that includes the code inside the conditional block in the first snippet.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Capture Macrobenchmark metrics](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics)
- [Overview of measuring app performance](https://developer.android.com/topic/performance/measuring-performance)\*[Frozen frames](https://developer.android.com/topic/performance/vitals/frozen)