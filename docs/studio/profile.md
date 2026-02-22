---
title: https://developer.android.com/studio/profile
url: https://developer.android.com/studio/profile
source: md.txt
---

# Profile your app performance

An app has poor performance if it responds slowly, shows choppy animations, freezes, or consumes too much power. Fixing performance problems involves*profiling*your app, or identifying areas in which your app makes inefficient use of resources such as the CPU, memory, graphics, or the device battery. This topic describes the Android Studio tools and techniques to use to fix common performance problems.

To learn how to run standalone profilers without running the entire Android Studio IDE (Windows or Linux only), see[Run the standalone profiler](https://developer.android.com/studio/profile/standalone-profiler).

## Requirements

To profile your app, we recommend having the following:

- An app with a release build variant that has the`profileable`manifest configuration enabled, also known as a profileable app. By default, apps have this configuration set to true. To check or change this configuration open your app's manifest or`AndroidManifest.xml`file and look in the`<application>`section for the[`profileable`](https://developer.android.com/guide/topics/manifest/profileable-element)manifest configuration:

      <profileable android:shell="true" />

  | **Note:** Use a[debuggable](https://developer.android.com/studio/debug)app instead of a profileable app if you need to record Java/Kotlin allocations, capture a heap dump, or see the**Interaction**timeline in task views that provide it.
- A virtual or physical test device that runs API level 29 or higher and has Google Play.

- Android Gradle Plugin 7.3 or higher.

### Profileable v. debuggable apps

A profileable app lets you do most common profiling tasks, but you should use a[debuggable](https://developer.android.com/studio/debug)app instead if you need to record Java/Kotlin allocations or capture a heap dump. A debuggable app process and device running API level 26 or higher also lets you see the**Interaction**timeline, which shows user interaction and app lifecycle events, in task views that provide it.

A debuggable app is based on the`debug`build variant of your app and lets you use development tools such as the[debugger](https://developer.android.com/studio/debug); however, it comes with some performance costs. A profileable app is based on the`release`build variant of your app and enables a subset of common profiling tasks without the performance overhead of the debug build.
| **Note:** In Android Studio, click**Profile 'app' with low overhead** ![](https://developer.android.com/static/studio/images/buttons/profiler-low-overhead.png)to use a profileable app and click**Profile 'app' with complete data** ![](https://developer.android.com/static/studio/images/buttons/profiler-complete-data.png)to use a debuggable app.

## Build and run a profileable app

To build and run a profileable app in Android Studio, follow these steps:

1. [Create a run/debug configuration](https://developer.android.com/studio/run/rundebugconfig)if you don't already have one.
2. Select your release build variant (**Build \> Select Build Variant**).
3. Click**More actions![](https://developer.android.com/static/studio/images/buttons/profiler-more-actions.png)\> Profile 'app' with low overhead** ![](https://developer.android.com/static/studio/images/buttons/profiler-low-overhead.png)or**Profile 'app' with complete data** ![](https://developer.android.com/static/studio/images/buttons/profiler-complete-data.png)("app" is the name of the run configuration, so it might be different for you). To choose between the two options, see[Requirements](https://developer.android.com/studio/profile#requirements). The app opens on your test device and the**Profiler**pane opens in Android Studio.

If these instructions don't work for you, see[Build and run a profileable app manually](https://developer.android.com/studio/profile/build-run-manually).

## Start profiling

To start a profiling task, follow these steps:

1. Select a process from the list in the**Home** tab within the**Profiler**pane. In most cases, you'll want to select the top process that represents your app.

   ![Profiler home tab](https://developer.android.com/static/studio/images/profiler-home.png)
2. Select a profiling task from the**Tasks** section. For more info about the tasks, see the other pages in this section. Not all profiling tasks are available for every process. If you don't know where to start, get an overall view of performance activity by[inspecting your app live](https://developer.android.com/studio/profile/inspect-app-live).

3. Use the**Start profiler task from**drop-down to select whether to start the profiler task from startup or attach to the process as it's running. If you're trying to improve your app startup time or capture a process that happens during app startup, you should include startup; otherwise, you can start profiling at your app's current state.

4. Click**Start profiler task**. The task starts in its own tab.

5. Interact with your app so activities are triggered.

6. Stop the recording (if applicable), wait for it to parse, and see the results.

## Compare, export, and import traces

When you stop a profiling task, it's automatically saved in the**Past Recordings** tab within the**Profiler** pane. You can use these saved recordings to compare resource usage in different scenarios. The recordings are saved for the duration of the current Android Studio session; if you want to keep them for longer, export them by clicking**Export recording** ![](https://developer.android.com/static/studio/images/buttons/profiler-export-recording.png). Not all trace types can be exported.

To import a trace, for example from a previous run of Android Studio, click**Import recording** ![](https://developer.android.com/static/studio/images/buttons/profiler-import-recording.png)in the**Past Recordings**tab and select your trace file. You can also import a file by dragging it into the Android Studio editor window.

## Edit the recording configuration

To edit your profiler task recording configuration, click the profiler settings![](https://developer.android.com/static/studio/images/buttons/profiler-settings.png). There are two main settings you can toggle:

- For tasks that involve sampling, the**Sample interval**represents the time between each sample. The shorter the interval you specify, the faster you reach the file size limit for the recorded data.
- The**File size limit**represents the amount of data that can be written to the connected device. When you stop recording, Android Studio parses this data and displays it in the profiler window. If you increase the limit and record a large amount of data, Android Studio takes much longer to parse the file and might become unresponsive.

| **Note:** If you use a connected device running Android 8.0 (API level 26) or higher, there isn't a limit on the file size of the trace data, and the**File size limit**value is ignored. However, you still need to be careful about how much data the device collects after each recording because large trace files are difficult to parse. For example, if you're recording either a sampled trace with a short sampling interval or an instrumented trace while your app calls many methods in a short time, you'll generate large trace files quickly.