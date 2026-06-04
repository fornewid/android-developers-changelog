---
title: https://developer.android.com/blog/posts/prioritizing-memory-efficiency-essential-steps-for-android-17
url: https://developer.android.com/blog/posts/prioritizing-memory-efficiency-essential-steps-for-android-17
source: md.txt
---

#### [How-tos](https://developer.android.com/blog/categories/how-tos)

# Prioritizing Memory Efficiency: Essential Steps for Android 17

###### 10-min read

![](https://developer.android.com/static/blog/assets/Engineering_Memory_Blog_Strapi_3_bfd74f43e5_Z2i8kF7.webp) 02 Jun 2026 3 Authors

##### [Alice Yuan,](https://developer.android.com/blog/authors/alice-yuan)
[Ajesh Pai,](https://developer.android.com/blog/authors/ajesh-pai)
[Fung Lam](https://developer.android.com/blog/authors/fung-lam)

While app performance is often equated with a smooth UI and fast start times, memory serves as the silent foundation upon which these visible metrics are built. It's no secret that we're seeing a shift where device memory is more important than ever. Not only have we made strides in Android memory optimizations with Android 17, we're providing the tooling and API support to help you stay ahead of stricter memory requirements later this year.

To ensure device stability, starting in Android 17, the system will begin enforcing app memory limits based on the device's total RAM. If an app exceeds those limits, Android will kill the process with no associated stack trace.

Beyond these forced terminations, unoptimized memory usage inevitably degrades the user experience. When the app approaches heap memory limits, it triggers frequent garbage collection---leading to noticeable UI stutters. Furthermore, when a device runs out of available memory, the system scrambles to reclaim pages, causing CPU strain, UI latency, and battery drain. If the memory shortage is too severe, it can cause Low Memory Killer (LMK) events that abruptly terminate background processes and force apps to have slow cold starts and lose user state.

To build highly performant apps and avoid these forced terminations, we recommend that you adopt the following memory optimization strategies:

1. Maximize bytecode optimization with R8
2. Optimize image loading
3. Detect and fix memory leaks with Android Studio
4. Trim memory when app leaves visible state
5. Advanced memory observability with ProfilingManager

[Video](https://www.youtube.com/watch?v=fOXJR5qLq54)

*A condensed version of this blog post is also available in video format, go check it out!*

## Understanding Android 17 app memory limits

App memory limits are being introduced in Android 17 to prevent "one bad actor" from destroying the multitasking experience and stability of the user's entire device.

Here is a breakdown of the reasons driving this architectural change:

- **Preventing cascading kills** : When an app becomes bloated or leaks memory while holding a privileged state (e.g. it's running a Foreground Service), it is initially shielded from the system's Low Memory Killer (LMK). As this single app grows unchecked and hoards RAM, the LMK is forced to compensate by killing off dozens of smaller, well-behaved cached apps and background jobs to reclaim space for the memory hog.  
- **Preserving multitasking and user state:** When the system is forced to purge cached apps to accommodate a single leaking process, the multitasking experience is severely degraded. Users returning to prior cached applications encounter sluggish cold starts instead of near-instant warm resumes. This inefficiency generates more CPU strain and accelerates battery depletion. It can also destroy the user's context in recently used apps, such as scroll positions, navigation stacks, and in-game progress.

To determine if your app session was impacted by these constraints in the field, you can call [getDescription()](https://developer.android.com/reference/android/app/ApplicationExitInfo#getDescription%28%29) within [ApplicationExitInfo](https://developer.android.com/reference/android/app/ApplicationExitInfo). If the system applied a limit, the exit reason is reported as [REASON_OTHER](https://developer.android.com/reference/android/app/ApplicationExitInfo#REASON_OTHER) and the description string will contain "MemoryLimiter:AnonSwap". You can also leverage [trigger-based profiling](https://developer.android.com/topic/performance/tracing/profiling-manager/trigger-based-capture) using [TRIGGER_TYPE_ANOMALY](https://developer.android.com/about/versions/17/features#anomaly-profiling-trigger) to automatically capture heap dumps when the memory limit is reached. Furthermore, Android is actively working to surface more in-field memory metrics to developers within the Google Play Console.

We have also expanded our [memory limits documentation](https://developer.android.com/about/versions/17/behavior-changes-all#app-memory-limits) to include local debugging commands, allowing you to simulate memory constraints in your local environment and validate your application's behavior under any memory limit enforcement.

## Maximize bytecode optimization with R8

A highly effective way to reduce your app's memory footprint is to enable the R8 optimizer. By shrinking classes, methods, and fields into shorter names and stripping out unused code and resources, R8 significantly reduces your app's memory footprint by minimizing the amount of resident code required during execution.

R8 minimizes resident code, shrinking the memory footprint and lowering LMK termination risk. This results in more frequent warm starts over slow cold starts. Additionally, streamlined bytecode reduces main-thread CPU overhead, directly cutting ANR rates for a more fluid user experience. For example, the digital bank [Monzo](https://developer.android.com/blog/posts/monzo-boosts-performance-metrics-by-up-to-35-with-a-simple-r8-update) enabled full R8 optimization and saw a 35% reduction in their ANR rate, a 30% improvement in cold start rate, and a 9% reduction in overall app size.
![pic1-IO26_113_TSV-monzo-casestudy.jpg](https://developer.android.com/static/blog/assets/pic1_IO_26_113_TSV_monzo_casestudy_dd704820ee_Z1oiKwQ.webp) The digital bank Monzo enabled full R8 optimization and boosted performance metrics by up to 35%.

To properly configure R8 in your `build.gradle` file:

- Set `isShrinkResources = true` and `isMinifyEnabled = true`.
- Use `proguard-android-optimize.txt` instead of the legacy `proguard-android.txt`, which actually prevents optimizations and is no longer supported in Android Gradle Plugin 9.
- Remove `android.enableR8.fullMode = false` from your `gradle.properties`.

If you are using reflection in your code base, then add [Keep rules](https://developer.android.com/topic/performance/app-optimization/keep-rules-overview#where-to-add-rules) to prevent R8 from optimizing those parts of the code. Make sure to scope the keep rules narrowly to get the maximum optimization.

To get the maximum optimization, make sure to follow these best practices in your keep rule file.

- Remove global options like `-dontoptimize`, `-dontshrink`, and `-dontobfuscate` that prevent R8 from optimizing the entire codebase
- Remove keep rules that prevent optimizing Android components like Activity, Services, Views or Broadcast receivers.
- Refine the broad package wide keep rules to target only specific classes or methods.

To see more best practices, view our [keep rules documentation](https://developer.android.com/topic/performance/app-optimization/keep-rules-best-practices).

## Library Developer R8 Best Practices

If you are a library developer, strictly place the rules your consumers need into your `consumer-rules file`, and keep your library's internal protection rules in your `proguard-rules.pro` file. For more information on how to optimize libraries, see [Optimization for library authors](https://developer.android.com/topic/performance/app-optimization/library-optimization).

## R8 Configuration Analyzer

To audit your R8 optimization, use the [**Configuration Analyzer**](http://developer.android.com/r8-analyzer).Configuration analyzer shows the current state of optimization withObfuscation, Optimization, and Shrinking scores. With configuration analyzer, you can also understand how many classes, methods or fields are prevented from optimization by each keep rule. Refine these broad package wide keep rules to unlock the maximum optimization.

Using configuration analyzer, you can also identify keep rules that are subsuming other keep rules, redundant keep rules and unused keep rules.
![pic2-r8-config-analyzer.png](https://developer.android.com/static/blog/assets/pic2_r8_config_analyzer_87a3feafc8_ZUSazT.webp) The Configuration Analyzer shows the current state of optimization with Obfuscation, Optimization, and Shrinking scores.

### R8 Agent Skill

You can also leverage the [**R8 Agent Skill**](https://github.com/android/skills/tree/main/performance/r8-analyzer) with Android Studio agent or other AI tools to resolve misconfigurations and refine your rules resulting in improved app performance.* (Insights from AI-driven skills will require technical verification)*

## Optimize image loading

Bitmaps are usually the largest common objects residing in your app's memory. They represent the final stage of the image loading process where compressed files, like JPEGs or PNGs, are decoded into raw pixel data for display. This means a tiny 100KB compressed image can balloon into several megabytes of RAM because memory consumption is determined by the image's pixel dimensions and color depth. Since bitmap operations are frequently on the critical path to drawing frames, unoptimized images cause severe memory bloat and UI jank.

Google recommends leveraging image loading libraries [**Coil**](https://github.com/coil-kt/coil) for Kotlin-first projects, particularly when developing with Jetpack Compose and [**Glide**](https://github.com/bumptech/glide) for Java-based applications.

### Adopt these five best practices

1. **Downsample images:** If you're loading bitmaps manually, avoid loading a massive image into a tiny thumbnail view; use [inSampleSize](https://developer.android.com/topic/performance/graphics/load-bitmap) to load a smaller version. Glide and Coil downsamples images by default and you can configure this downsample strategy using [DownsampleStrategy](https://bumptech.github.io/glide/javadocs/470/com/bumptech/glide/load/resource/bitmap/DownsampleStrategy.html) and [ImageLoader](https://coil-kt.github.io/coil/image_loaders/) respectively.
2. **Cropping:** Avoid embedding padding directly into an image file for letterboxing purposes (e.g., creating a transparent border to expand an image dimensions). Rather than baking in these borders, utilize [InsetDrawable](https://developer.android.com/reference/android/graphics/drawable/InsetDrawable) or apply padding directly within the View or Composable containing the bitmap.
3. **Config:** Balance memory and quality by choosing the right pixel format. Use `RGB_565` when transparency isn't needed, which uses half the memory of the default `ARGB_8888` format. In Glide you can configure this by using [DecodeFormat](https://bumptech.github.io/glide/javadocs/470/com/bumptech/glide/load/DecodeFormat.html) and in Coil you can use [bitmapConfig](https://coil-kt.github.io/coil/api/coil-core/coil3.request/-image-request/) property.
4. **Prioritize vector drawables:** For basic geometric assets, leverage [ShapeDrawable](https://developer.android.com/reference/android/graphics/drawable/ShapeDrawable) as a lightweight alternative to decoding rasterized bitmaps. By defining these assets once via XML, you ensure they scale seamlessly across all display densities while effectively eliminating resource-driven memory bloat.
5. **Reuse:** If your application manages Bitmaps manually then to minimize memory churn, when a bitmap is no longer required, the app should call `bitmap.recycle()` and immediately discard the `Bitmap` reference. If you use an image loading library like Glide or Coil, return the bitmap to the library's managed pool. By providing an existing buffer for future memory needs, the pool effectively avoids the overhead of new allocations.

Check out our documentation on [Optimizing performance for images](https://developer.android.com/develop/ui/compose/graphics/images/optimization) to learn more.

### Android Studio tooling

You can also eliminate redundant bitmaps using Android Studio Narwhal 4. Here is how to hunt them down in five simple steps:

1. Open the **Profiler** tab in Android Studio
2. Click **Heap Dump** (or "Analyze Memory Usage") and hit record to take a snapshot of your app's current memory state.
3. Scan the analysis results for the **yellow warning triangle** ⚠️, which Android Studio uses to flag duplicate bitmaps being stored multiple times. Alternatively, navigate to the profiler header, choose "Filter by:" and pick the "Duplicate Bitmaps" setting.
4. Click on any flagged entry to open the **Bitmap Preview** pane, allowing you to see exactly which image is the repeat offender.
5. Use that visual confirmation to track down the redundant loading logic in your code and implement a better caching strategy.

![pic3-IO26_113_TSV -dup-bitmaps-cropped.jpg](https://developer.android.com/static/blog/assets/pic3_IO_26_113_TSV_dup_bitmaps_cropped_0b5bed0efb_Z1vcMMk.webp) Look for the yellow warning triangle ⚠️ in heap dumps when using the Android Studio Profiler.

## Detect and fix memory leaks with Android Studio

Memory leaks in Android occur when your code holds onto an object's reference long after its lifecycle has ended. This prevents the Garbage Collector (GC) from reclaiming that memory, eventually leading to sluggish performance or OutOfMemoryError (OOM).

Android Studio Panda 3 features a dedicated [LeakCanary](https://square.github.io/leakcanary/) profiler task, allowing developers to analyze real-time memory leaks and map traces directly within the IDE.

The LeakCanary profiler task in Android Studio actively moves the memory leak analysis from your device to your development machine, resulting in a significant performance boost during the leak analysis phase as compared to on-device leak analysis.
![pic4-android-studio-leaks.png](https://developer.android.com/static/blog/assets/pic4_android_studio_leaks_b312cc5ab6_Z1B4c5f.webp) LeakCanary memory leak analysis contextualized with Go to declaration for debugging

Additionally, the leak analysis is now contextualized within the IDE and fully integrated with your source code, providing features like go to declaration and other helpful code connections that drastically reduce the friction and time required to investigate and fix memory leaks.

#### Examples of common memory leaks

Memory leaks occur when an object persists in memory beyond its intended lifespan. This typically happens due to:

- Retaining references to Fragments, Activities, or Views that are no longer in use.
- Mismanaging Context references.
- Failing to properly unregister observers, listeners, and receivers.
- Creating static references to objects that are bound to components with shorter lifecycles.

Here are a few example scenarios:

|---|---|---|
| Scenario | Compose-based example | View-based example |
| Leaking Context | Example: Passing LocalContext.current to a ViewModel Fix: Keep Context dependent logic within the UI layer. For non-UI layers, refactor to use [dependency injection](https://developer.android.com/training/dependency-injection) or observe UI state using [Kotlin flow](https://developer.android.com/kotlin/flow). | Example: Storing an `Activity` in a companion object or static variable. Fix: Don't hold static references to UI components. Refactor to use [dependency injection](https://developer.android.com/training/dependency-injection) or observe UI state using [Kotlin flow](https://developer.android.com/kotlin/flow). |
| Leaking Listeners | Example: Using `DisposableEffect` to start a listener but leaving `onDispose` empty. Fix: Perform the unregistration and [cleanup logic](https://developer.android.com/develop/ui/compose/side-effects#disposableeffect) inside the `onDispose` block. | Example: Registering for SensorManager updates and forgetting to unregister. Fix: Manually call `unregisterListener()` in `onStop()` or `onDestroy()` lifecycle. |
| Leaking Views | Example: Holding a reference to a legacy `View` inside an `AndroidView` without a release strategy. <br /> Fix: Use the `release` block of the `AndroidView` composable to clean up the legacy `View`. | Example: Keeping a reference to a view binding object after the `Fragment` is destroyed. Fix: Set the binding variable to `null` inside the `onDestroyView()` lifecycle method. |

## Trim memory when app leaves visible state

Android can reclaim memory from your app or stop your app entirely if necessary to free up memory for critical tasks, as explained in [Overview of memory management](https://developer.android.com/topic/performance/memory-overview). Android will usually reclaim memory from your app when it's not visible to the user, such as by discarding some of your app's code and data pages in memory or compressing your heap allocations. When the user resumes your app and your app tries to access some memory that's been reclaimed, the OS will swap that memory back in on demand. This swapping behavior can be slow, and cause unexpected jank or stutters in your app.

If you leave it to the OS to decide what memory to reclaim from your app, you may find that the OS reclaimed memory that you'll need shortly after resuming your app. Instead, your app can voluntarily discard memory allocations that it can regenerate later, on demand and at a low cost. To do so, you can implement the `ComponentCallbacks2` interface. You can implement `onTrimMemory` in your `Activity`, `Fragment`, `Service`, or even your custom `Application` class. Using it in the `Application` class is highly effective for global cache management.

The provided [onTrimMemory()](https://developer.android.com/reference/android/content/ComponentCallbacks2#onTrimMemory(int)) callback method notifies your app of lifecycle or memory-related events that present a good opportunity for your app to voluntarily reduce its memory usage.

In terms of memory lifecycle management, your implementation should focus **exclusively** on `TRIM_MEMORY_UI_HIDDEN` and `TRIM_MEMORY_BACKGROUND`. Since Android 14, the system has ceased delivering notifications for other legacy constants, which were formally deprecated in Android 15.

`TRIM_MEMORY_UI_HIDDEN`: This signal indicates that your application's UI has transitioned out of the user's view. This provides an opportunity to release substantial memory allocations tied strictly to the interface---such as Bitmaps, video playback buffers, or complex animation resources.

`TRIM_MEMORY_BACKGROUND`: At this level, your process is residing in the background and is now a candidate for termination to satisfy the system's global memory needs. To extend the duration your process remains in the cached state, and reduce the number of app cold starts, you should aggressively release any resources that can be easily reconstructed once the user resumes their session.

```kotlin
import android.content.ComponentCallbacks2
// Other import statements.

class MainActivity : AppCompatActivity(), ComponentCallbacks2 {

    /**
     * Release memory when the UI becomes hidden or when system resources become low.
     * @param level the memory-related event that is raised.
     */
    override fun onTrimMemory(level: Int) {

        if (level >= ComponentCallbacks2.TRIM_MEMORY_UI_HIDDEN) {
            // Release memory related to UI elements, such as bitmap caches.
        }

        if (level >= ComponentCallbacks2.TRIM_MEMORY_BACKGROUND) {
            // Release memory related to background processing, such as by
            // closing a database connection.
        }
    }
}
```

Note: The `onTrimMemory `integration may depend on SDK support. For instance, certain games rely on their game engine to enable this capability. Please check out the [game memory optimization documents](https://developer.android.com/games/optimize/memory-allocation).

## Advanced memory observability with ProfilingManager

To catch and diagnose memory issues in the field that cannot be reproduced locally, you should leverage the **ProfilingManager API**. Introduced in Android 15, this advanced observability API allows you to programmatically collect real-user Perfetto profiles.

For teams that lack a dedicated infrastructure to manage and host performance artifacts, Crashlytics is exploring a specialized solution to streamline this workflow. They are inviting developers to [provide feedback](https://docs.google.com/forms/d/1hVe2zr-_Bq8ZRHJfl-PPnxVwPB2OgaETYQM0W9pkEZI/preview?resourcekey=0-3jcJm5RrLOSxHtfLZInnpg).

**Android 17 introduces new event-driven triggers** , most notably `TRIGGER_TYPE_OOM` and `TRIGGER_TYPE_ANOMALY`:

- The **OOM trigger** automatically collects a Java heap dump at the exact moment an OutOfMemoryError crash occurs, providing precise allocation states. A collected OOM profile is provided the next time the app starts and registers the `registerForAllProfilingResults` callback.
- The **Anomaly trigger** detects severe performance issues, such as excessive binder spam or breached memory thresholds. The memory anomaly delivers a heap dump just prior to the system terminating the app.

```kotlin
    val profilingManager = 
applicationContext.getSystemService(ProfilingManager::class.java)
    val triggers = ArrayList<ProfilingTrigger>()  


    triggers.add(ProfilingTrigger.Builder(
                 ProfilingTrigger.TRIGGER_TYPE_ANOMALY))
    val mainExecutor: Executor = Executors.newSingleThreadExecutor()
    val resultCallback = Consumer<ProfilingResult> { profilingResult ->
        if (profilingResult.errorCode != ProfilingResult.ERROR_NONE) {
            // upload profile result to server for further analysis          
            setupProfileUploadWorker(profilingResult.resultFilePath)
        } 

    profilingManager.registerForAllProfilingResults(mainExecutor, resultCallback)
    profilingManager.addProfilingTriggers(triggers)
```

Once you've collected the heap dump, you can download the profile from the server, or locally via adb pull and drag and drop the file into the [Perfetto UI](http://ui.perfetto.dev/). To streamline your memory debugging workflow, use the [Heap Dump Explorer](https://perfetto.dev/docs/visualization/heap-dump-explorer), this is the new default view for heap dumps in Perfetto UI. This tool provides an intuitive interface for inspecting Java heap dumps, allowing you to visualize object allocation hierarchies, compute retained memory sizes, and identify the shortest path from garbage collection root. By leveraging the Heap Dump Explorer, you can rapidly pinpoint memory leaks, bloated retained objects such as excessive bitmap allocations, and analyze heap object allocations all in one place.
![pic5-perfettoheapdump-analyzer.png](https://developer.android.com/static/blog/assets/pic5_perfettoheapdump_analyzer_6e0de76fa1_ZLfxne.webp) Use the Heap Dump Explorer's embedded flamegraph to visually inspect and navigate through objects with the highest heap allocations.

## Conclusion

Optimizing bytecode with R8, adopting image loading best practices, and resolving memory leaks are critical steps toward delivering a high-quality user experience while managing resources effectively under pressure. Adopting these proactive measures helps maintain app stability and performance, preventing unexpected terminations while safeguarding user context. To further your performance expertise, explore our revised [memory guidance](https://developer.android.com/topic/performance/memory).
- [#Memory](https://developer.android.com/blog/topics/memory)
- [#Android](https://developer.android.com/blog/topics/android)
- [#Performance](https://developer.android.com/blog/topics/performance)

###### Written by:

-

  ## [Alice Yuan](https://developer.android.com/blog/authors/alice-yuan)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/alice-yuan) ![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp) ![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)
-

  ## [Ajesh Pai](https://developer.android.com/blog/authors/ajesh-pai)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/ajesh-pai) ![](https://developer.android.com/static/blog/assets/Ajesh_R_Pai_fc75c62777_Z1G5g2B.webp) ![](https://developer.android.com/static/blog/assets/Ajesh_R_Pai_fc75c62777_Z1G5g2B.webp)
-

  ## [Fung Lam](https://developer.android.com/blog/authors/fung-lam)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/fung-lam) ![](https://developer.android.com/static/blog/assets/Fung_Lam_profile_633041f048_Z1o4ef9.webp) ![](https://developer.android.com/static/blog/assets/Fung_Lam_profile_633041f048_Z1o4ef9.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)](https://developer.android.com/blog/authors/alice-yuan) 04 Mar 2026 04 Mar 2026 ![](https://developer.android.com/static/blog/assets/battery_Performance_08d6713f94_Z1IAO0P.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Battery Technical Quality Enforcement is Here: How to Optimize Common Wake Lock Use Cases](https://developer.android.com/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases)

  [arrow_forward](https://developer.android.com/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases) In recognition that excessive battery drain is top of mind for Android users, Google has been taking significant steps to help developers build more power-efficient apps.

  ###### [Alice Yuan](https://developer.android.com/blog/authors/alice-yuan) •
  8 min read

- [![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)](https://developer.android.com/blog/authors/alice-yuan) 20 Nov 2025 20 Nov 2025 ![](https://developer.android.com/static/blog/assets/performance_Week8_4d6efcacbe_ZI6a5e.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Leveling Guide for your Performance Journey](https://developer.android.com/blog/posts/leveling-guide-for-your-performance-journey)

  [arrow_forward](https://developer.android.com/blog/posts/leveling-guide-for-your-performance-journey) The performance leveling guide features 5 levels. We'll start with level 1, which introduces minimal adoption effort performance tooling, and we'll go up to level 5, ideal for apps that have the resourcing to maintain a bespoke performance framework.

  ###### [Alice Yuan](https://developer.android.com/blog/authors/alice-yuan) •
  9 min read

- [![](https://developer.android.com/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)](https://developer.android.com/blog/authors/ben-weiss) 17 Nov 2025 17 Nov 2025 ![](https://developer.android.com/static/blog/assets/performance_Week9_2c643934fa_p8Pb2.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Get your app on the fast track with Android Performance Spotlight Week!](https://developer.android.com/blog/posts/get-your-app-on-the-fast-track-with-android-performance-spotlight-week)

  [arrow_forward](https://developer.android.com/blog/posts/get-your-app-on-the-fast-track-with-android-performance-spotlight-week) When working on new features, app performance often takes a back seat. However, while it's not always top of mind for developers, users can see exactly where your app's performance lags behind.

  ###### [Ben Weiss](https://developer.android.com/blog/authors/ben-weiss) •
  3 min read

  - [#Performance](https://developer.android.com/blog/topics/performance)
  - [#R8](https://developer.android.com/blog/topics/r8)

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)