---
title: https://developer.android.com/topic/performance/vitals/launch-time
url: https://developer.android.com/topic/performance/vitals/launch-time
source: md.txt
---

# App startup time

Users expect apps to load fast and be responsive. An app with a slow start time doesn't meet this expectation and can disappoint users. This sort of poor experience can cause a user to rate your app poorly on the Play store or even abandon your app altogether.

This page provides information to help optimize your app's launch time, including an overview of the internals of the launch process, how to profile startup performance, and some common start-time issues with tips on how to address them.

## Understand the different app startup states

App launch can take place in one of three states: cold start, warm start, or hot start. Each state affects how long it takes for your app to become visible to the user. In a cold start, your app starts from scratch. In the other states, the system needs to bring the running app from the background to the foreground.

We recommend that you always optimize based on an assumption of a cold start. Doing so can improve the performance of warm and hot starts as well.

To optimize your app for fast startup, it's useful to understand what's happening at the system and app levels and how they interact in each of these states.

Two important metrics for determining app startup are[time to initial display (TTID)](https://developer.android.com/topic/performance/vitals/launch-time#time-initial)and[time to fully drawn (TTFD)](https://developer.android.com/topic/performance/vitals/launch-time#time-full). TTID is the time it takes to display the first frame, and TTFD is the time it takes for the app to become fully interactive. Both are equally important, because TTID lets the user know that the app is loading, and TTFD is when the app is actually useable. If either of these is too long, the user might exit your app before it even fully loads.

### Cold start

A cold start refers to an app's starting from scratch. This means that until this start, the system's process creates the app's process. Cold starts happen in cases such as your app launching for the first time since the device booted or since the system killed the app.

This type of start presents the greatest challenge to minimizing startup time, because the system and app have more work to do than in the other launch states.

At the beginning of a cold start, the system has the three following tasks:

1. Load and launch the app.
2. Display a blank starting window for the app immediately after launch.
3. Create the app[process](https://developer.android.com/guide/components/processes-and-threads#Processes).

As soon as the system creates the app process, the app process is responsible for the next stages:

1. Create the app object.
2. Launch the main thread.
3. Create the main activity.
4. Inflate views.
5. Layout the screen.
6. Perform the initial draw.

When the app process completes the first draw, the system process swaps out the displayed background window, replacing it with the main activity. At this point, the user can start using the app.

Figure 1 shows how the system and app processes hand off work between each other.
![](https://developer.android.com/static/topic/performance/images/cold-launch.png)**Figure 1.**A visual representation of the important parts of a cold app launch.

Performance issues can arise during creation of the app and creation of the activity.

#### App creation

When your app launches, the blank starting window remains on the screen until the system finishes drawing the app for the first time. At this point, the system process swaps the starting window for your app, letting the user interact with the app.

If you override[`Application.onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate())in your own app, the system invokes the`onCreate()`method on your app object. Afterwards, the app spawns the main thread, also known as the*UI thread*, and tasks it with creating your main activity.

From this point, system- and app-level processes proceed in accordance with the[app lifecycle stages](https://developer.android.com/guide/topics/processes/process-lifecycle).

#### Activity creation

After the app process creates your activity, the activity performs the following operations:

1. Initializes values.
2. Calls constructors.
3. Calls the callback method, such as[`Activity.onCreate()`](https://developer.android.com/reference/android/content/ComponentCallbacks2#onTrimMemory(int)), appropriate to the current lifecycle state of the activity.

Typically, the[`onCreate()`](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle))method has the greatest impact on load time, because it performs the work with the highest overhead: loading and inflating views and initializing the objects needed for the activity to run.

### Warm start

A warm start encompasses a subset of the operations that take place during a cold start. At the same time, it represents more overhead than a hot start. There are many potential states that can be considered warm starts, such as the following:

- The user backs out of your app but then re-launches it. The process might continue to run, but the app must recreate the activity from scratch using a call to`onCreate()`.

- The system evicts your app from memory and then the user re-launches it. The process and the activity needs to restart, but the task can benefit somewhat from the saved instance state bundle passed into`onCreate()`.

### Hot start

A hot start of your app has lower overhead than a cold start. In a hot start, the system brings your activity to the foreground. If all of your app's activities are still resident in memory, then the app can avoid repeating object initialization, layout inflation, and rendering.

However, if some memory is purged in response to memory trimming events, such as[`onTrimMemory()`](https://developer.android.com/reference/android/content/ComponentCallbacks2#onTrimMemory(int)), then these objects need to be recreated in response to the hot start event.

A hot start displays the same on-screen behavior as a cold start scenario. The system process displays a blank screen until the app finishes rendering the activity.

<br />

![](https://developer.android.com/static/topic/performance/vitals/images/startup-modes-r1.png)**Figure 2.**A diagram with the various startup states and their respective processes, each state beginning from the first frame drawn.

<br />

## How to identify app startup in Perfetto

To debug app startup issues, it's helpful to determine what exactly is included in the app startup phase. To identify the entire app startup phase in[Perfetto](https://perfetto.dev/docs/), follow these steps:

1. In Perfetto, find the row with the Android App Startups derived metric. If you don't see it, try capturing a trace using the[on-device system tracing app](https://developer.android.com/topic/performance/tracing/on-device).

   ![](https://developer.android.com/static/topic/performance/images/app-startup-perfetto.png)**Figure 3.**The Android App Startups derived metric slice in Perfetto.
2. Click the associated slice and press<kbd>m</kbd>to select the slice. Brackets appear around the slice and denote how long it took. The duration is also shown in the**Current selection**tab.

3. Pin the Android App Startups row by clicking on the pin icon, which is visible when you hold the pointer over the row.

4. Scroll to the row with the app in question and click the first cell to expand the row.

5. Zoom into the main thread, usually at the top, by pressing<kbd>w</kbd>(press<kbd>s, a, d</kbd>to zoom out, move left, and move right, respectively).

   ![](https://developer.android.com/static/topic/performance/images/app-startup-perfetto-zoomed.png)**Figure 4.**The Android App Startups derived metric slice next to the main thread of the app.
6. The derived metrics slice makes it easier to see what exactly is included in the app startup, so you can continue to debug in more detail.

## Use metrics to inspect and improve startups

To properly diagnose startup time performance, you can track metrics that show how long it takes your app to start. Android provides several means of showing you that your app has a problem and helps you diagnose it. Android vitals can alert you that a problem is occurring, and diagnostic tools can help you diagnose the problem.

### Benefits of utilizing startup metrics

Android uses the[time to initial display (TTID)](https://developer.android.com/topic/performance/vitals/launch-time#time-initial)and[time to full display (TTFD)](https://developer.android.com/topic/performance/vitals/launch-time#time-full)metrics to optimize cold and warm app startups. Android Runtime (ART) uses the data from these metrics to efficiently precompile code for optimization of future startups.

Faster startups lead to more sustained user interaction with your app, which reduces instances of early exiting, restarting the instance, or navigating away to a different app.

### Android vitals

Android vitals can help improve your app's performance by alerting you on the[Play Console](https://play.google.com/console/)when your app's startup times are excessive.

Android vitals considers the following startup times for your app excessive:

- [Cold](https://developer.android.com/topic/performance/vitals/launch-time#cold)startup takes 5 seconds or longer.
- [Warm](https://developer.android.com/topic/performance/vitals/launch-time#warm)startup takes 2 seconds or longer.
- [Hot](https://developer.android.com/topic/performance/vitals/launch-time#hot)startup takes 1.5 seconds or longer.

Android vitals uses the[time to initial display (TTID)](https://developer.android.com/topic/performance/vitals/launch-time#time-initial)metric. For information about how Google Play collects Android vitals data, see the[Play Console documentation](https://support.google.com/googleplay/android-developer/answer/7385505).

### Time to initial display

Time to initial display (TTID) is the time it takes to display the first frame of the app's UI. This metric measures the time it takes for an app to produce its first frame, including process initialization during a cold start, activity creation during a cold or warm start, and displaying the first frame. Keeping your app's TTID low helps improve the user experience by letting users see your app launch quickly. TTID is reported automatically for every app by the Android Framework. When optimizing for app startup we recommend implementing[`reportFullyDrawn`](https://developer.android.com/reference/android/app/Activity#reportFullyDrawn())to get information up to[TTFD](https://developer.android.com/topic/performance/vitals/launch-time#time-full).

TTID is measured as a time value that represents the total elapsed time that includes the following sequence of events:

- Launching the process.
- Initializing the objects.
- Creating and initializing the activity.
- Inflating the layout.
- Drawing the app for the first time.

#### Retrieve TTID

To find TTID, search in the[Logcat command-line tool](https://developer.android.com/tools/logcat)for an output line containing a value called`Displayed`. This value is the TTID and looks similar to the following example, in which TTID is 3s534ms:  

    ActivityManager: Displayed com.android.myexample/.StartupTiming: +3s534ms

To find TTID in Android Studio, disable the filters in your Logcat view from the filter drop-down, and then find the`Displayed`time, as shown in figure 5. Disabling the filters is necessary because the system server, not the app itself, serves this log.
![](https://developer.android.com/static/topic/performance/images/displayed-logcat.png)**Figure 5.** Disabled filters and the`Displayed`value in logcat.

The`Displayed`metric in the Logcat output doesn't necessarily capture the amount of time until all resources are loaded and displayed. It leaves out resources that aren't referenced in the layout file or that the app creates as part of object initialization. It excludes these resources because loading them is an inline process and it doesn't block the app's initial display.

Sometimes the`Displayed`line in the Logcat output contains an additional field for total time. For example:  

    ActivityManager: Displayed com.android.myexample/.StartupTiming: +3s534ms (total +1m22s643ms)

In this case, the first time measurement is only for the activity that is first drawn. The`total`time measurement begins at the app process start and can include another activity that is started first but doesn't display anything to the screen. The`total`time measurement is only shown when there is a difference between the single activity and total startup times.

We recommend using Logcat in Android Studio, but If you're not using Android Studio, you can also measure TTID by running your app with the[`adb`shell activity manager command](https://developer.android.com/tools/adb#am). Here's an example:  

    adb [-d|-e|-s <serialNumber>] shell am start -S -W
    com.example.app/.MainActivity
    -c android.intent.category.LAUNCHER
    -a android.intent.action.MAIN

The`Displayed`metric appears in the Logcat output as before. Your terminal window displays the following:  

    Starting: Intent
    Activity: com.example.app/.MainActivity
    ThisTime: 2044
    TotalTime: 2044
    WaitTime: 2054
    Complete

The`-c`and`-a`arguments are optional and let you specify[`<category>`](https://developer.android.com/guide/topics/manifest/category-element)and[`<action>`](https://developer.android.com/guide/topics/manifest/action-element).

### Time to full display

Time to full display (TTFD) is the time it takes for an app to become interactive for the user. It is reported as the time it takes to display the first frame of the app's UI, as well as the content that loads asynchronously after the initial frame is displayed. Generally, this is primary content loaded from the network or disk, as reported by the app. In other words, TTFD includes TTID as well as the time it takes for the app to be usable. Keeping your app's TTFD low helps improve the user experience by letting users interact with your app quickly.

The system determines TTID when[`Choreographer`](https://developer.android.com/reference/android/view/Choreographer)calls the activity's[`onDraw()`](https://developer.android.com/reference/android/view/View#onDraw(android.graphics.Canvas))method, and when it knows it calls this for the first time. However, the system doesn't know when to determine TTFD because every app behaves differently. To determine TTFD, the app needs to signal to the system when it reaches the fully drawn state.

#### Retrieve TTFD

To find TTFD, signal the fully drawn state by calling the[`reportFullyDrawn()`](https://developer.android.com/reference/androidx/activity/ComponentActivity#reportFullyDrawn())method of the[`ComponentActivity`](https://developer.android.com/reference/androidx/activity/ComponentActivity). The`reportFullyDrawn`method reports when the app is fully drawn and in a usable state. The TTFD is the time elapsed from when the system receives the app launch intent to when`reportFullyDrawn()`is called. If you don't call`reportFullyDrawn()`, no TTFD value is reported.

To measure TTFD, call`reportFullyDrawn()`after you completely draw the UI and all of the data. Don't call`reportFullyDrawn()`before the first activity's window is first drawn and displayed as measured by the system, because then the system reports the system measured time. In other words, if you call`reportFullyDrawn()`before the system detects TTID, the system reports both TTID and TTFD as the same value, and this value is the TTID value.

When you use`reportFullyDrawn()`, Logcat displays an output like the following example, in which the TTFD is 1s54ms:  

    system_process I/ActivityManager: Fully drawn {package}/.MainActivity: +1s54ms

The Logcat output sometimes includes a`total`time, as discussed in[Time to initial display](https://developer.android.com/topic/performance/vitals/launch-time#time-initial).

If your display times are slower than you want, you can try to identify the bottlenecks in the startup process.

You can use`reportFullyDrawn()`to signal the fully drawn state in basic cases where you're aware that the fully drawn state is achieved. However, in cases where background threads must complete background work before the fully drawn state is achieved, you need to delay`reportFullyDrawn()`for a more accurate TTFD measurement. To learn how to delay`reportFullyDrawn()`, see the following section.

##### Improve startup timing accuracy

If your app is performing lazy loading and the initial display doesn't include all resources, such as when your app is fetching images from the network, you might want to delay calling`reportFullyDrawn`until after your app becomes usable so that you can include the list population as part of your benchmark timing.

For example, if the UI contains a dynamic list, such as a[`RecyclerView`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)or lazy list, this might be populated by a background task that completes after the list is first drawn and, therefore, after the UI is marked as fully drawn. In such cases, the list population isn't included in the benchmarking.

To include the list population as part of your benchmark timing, get the[`FullyDrawnReporter`](https://developer.android.com/reference/androidx/activity/FullyDrawnReporter)by using[`getFullyDrawnReporter()`](https://developer.android.com/reference/androidx/activity/ComponentActivity#getFullyDrawnReporter()), and add a reporter to it in your app code. Release the reporter after the background task finishes populating the list.

`FullyDrawnReporter`doesn't call the`reportFullyDrawn()`method until all added reporters are released. By adding a reporter until the background process completes, the timings also include the amount of time it takes to populate the list in the startup timing data. This doesn't change the app's behavior for the user, but it lets the timing startup data include the time it takes to populate the list.`reportFullyDrawn()`isn't called until all of the tasks are completed, regardless of the order.

The following example shows how you can run multiple background tasks concurrently, with each registering its own reporter:  

### Kotlin

    class MainActivity : ComponentActivity() {

        sealed interface ActivityState {
            data object LOADING : ActivityState
            data object LOADED : ActivityState
        }

        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)

            setContent {
                var activityState by remember {
                    mutableStateOf(ActivityState.LOADING as ActivityState)
                }
                fullyDrawnReporter.addOnReportDrawnListener {
                    activityState = ActivityState.LOADED
                }
                ReportFullyDrawnTheme {
                    when(activityState) {
                        is ActivityState.LOADING -> {
                            // Display the loading UI.
                        }
                        is ActivityState.LOADED -> {
                            // Display the full UI.
                        }
                    }
                }
                SideEffect {
                    fullyDrawnReporter.addReporter()
                    lifecycleScope.launch(Dispatchers.IO) {
                        // Perform the background operation.
                        fullyDrawnReporter.removeReporter()
                    }
                    fullyDrawnReporter.addReporter()
                    lifecycleScope.launch(Dispatchers.IO) {
                        // Perform the background operation.
                        fullyDrawnReporter.removeReporter()
                    }
                }
            }
        }
    }

### Java

    public class MainActivity extends ComponentActivity {
        private FullyDrawnReporter fullyDrawnReporter;

        @Override
        protected void onCreate(@Nullable Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);

            fullyDrawnReporter = getFullyDrawnReporter();
            fullyDrawnReporter.addOnReportDrawnListener(() -> {
                // Trigger the UI update.
                return Unit.INSTANCE;
            });

            new Thread(new Runnable() {
                @Override
                public void run() {
                    fullyDrawnReporter.addReporter();
                    // Do the background work.
                    fullyDrawnReporter.removeReporter();
                }
            }).start();
            new Thread(new Runnable() {
                @Override
                public void run() {
                    fullyDrawnReporter.addReporter();
                    // Do the background work.
                    fullyDrawnReporter.removeReporter();
                }
            }).start();
        }
    }

If your app uses Jetpack Compose, you can use the following APIs to indicate fully drawn state:

- [`ReportDrawn`](https://developer.android.com/reference/kotlin/androidx/activity/compose/package-summary#ReportDrawn()): indicates that your composable is immediately ready for interaction.
- [`ReportDrawnWhen`](https://developer.android.com/reference/kotlin/androidx/activity/compose/package-summary#ReportDrawnWhen(kotlin.Function0)): takes a predicate, such as`list.count > 0`, to indicate when your composable is ready for interaction.
- [`ReportDrawnAfter`](https://developer.android.com/reference/kotlin/androidx/activity/compose/package-summary#ReportDrawnAfter(kotlin.coroutines.SuspendFunction0)): takes a suspending method that, once completed, indicates that your composable is ready for interaction.

##### Identify bottlenecks

To look for bottlenecks, you can use the Android Studio CPU Profiler. For more information, see[Inspect CPU activity with CPU Profiler](https://developer.android.com/studio/profile/cpu-profiler).

You can also gain insight into potential bottlenecks through inline tracing inside of your apps' and activities'`onCreate()`methods. To learn about inline tracing, see the documentation for the[`Trace`](https://developer.android.com/reference/android/os/Trace)functions and the[overview of system tracing](https://developer.android.com/topic/performance/tracing).

## Solve common issues

This section discusses several issues that often affect app startup performance. These issues mainly concern initializing app and activity objects, as well as the loading of screens.

### Heavy app initialization

Launch performance can suffer when your code overrides the`Application`object and executes heavy work or complex logic when initializing that object. Your app might waste time during startup if your`Application`subclasses perform initializations that don't need to be done yet.

Some initializations might be completely unnecessary, such as when initializing state information for the main activity when the app is actually started up in response to an intent. With an intent, the app uses only a subset of the previously initialized state data.

Other challenges during app initialization include garbage collection events that are impactful or numerous, or disk I/O happening concurrently with initialization, which further blocks the initialization process. Garbage collection is especially a consideration with the Dalvik runtime; the Android Runtime (ART) performs garbage collection concurrently, minimizing that operation's impact.

#### Diagnose the problem

You can use method tracing or inline tracing to try to diagnose the problem.

##### Method tracing

Running the CPU Profiler reveals that the[`callApplicationOnCreate()`](https://developer.android.com/reference/android/content/ComponentCallbacks2#onTrimMemory(int))method eventually calls your`com.example.customApplication.onCreate`method. If the tool shows that these methods are taking a long time to finish executing, explore further to see what work is occurring there.

##### Inline tracing

Use inline tracing to investigate likely culprits, including the following:

- Your app's initial[`onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate())function.
- Any global singleton objects your app initializes.
- Any disk I/O, deserialization, or tight loops that might be occurring during the bottleneck.

#### Solutions to the problem

Whether the problem lies with unnecessary initializations or with disk I/O, the solution is lazy initialization. In other words, only initialize objects that are immediately needed. Instead of creating global static objects, move to a singleton pattern where the app initializes objects only the first time it needs them.

Also, consider using a dependency injection framework like[Hilt](https://developer.android.com/training/dependency-injection/hilt-android)that creates objects and dependencies when they are injected for the first time.

If your app uses content providers to initialize app components at startup, consider using the[App Startup library](https://developer.android.com/topic/libraries/app-startup)instead.

### Heavy activity initialization

Activity creation often entails a lot of high-overhead work. Often, there are opportunities to optimize this work to achieve performance improvements. Such common issues include the following:

- Inflating large or complex layouts.
- Blocking screen drawing on disk, or network I/O.
- Loading and decoding bitmaps.
- Rasterizing[`VectorDrawable`](https://developer.android.com/reference/android/graphics/drawable/VectorDrawable)objects.
- Initialization of other subsystems of the activity.

#### Diagnose the problem

In this case, as well, both method tracing and inline tracing can be useful.

##### Method tracing

When using the CPU Profiler, pay attention to your app's[`Application`](https://developer.android.com/reference/android/app/Application)subclass constructors and`com.example.customApplication.onCreate()`methods.

If the tool shows that these methods are taking a long time to finish executing, explore further to see what work is occurring there.

##### Inline tracing

Use inline tracing to investigate likely culprits, including the following:

- Your app's initial`onCreate()`function.
- Any global singleton objects it initializes.
- Any disk I/O, deserialization, or tight loops that might be occurring during the bottleneck.

#### Solutions to the problem

There are many potential bottlenecks, but two common problems and remedies are as follows:

- The larger your view hierarchy, the more time the app takes to inflate it. Two steps you can take to address this issue are the following:
  - Flatten your view hierarchy by reducing redundant or nested layouts.
  - Don't inflate parts of the UI that don't need to be visible during launch. Instead, use a[`ViewStub`](https://developer.android.com/reference/android/view/ViewStub)object as a placeholder for sub-hierarchies that the app can inflate at a more appropriate time.
- Having all of your resource initialization on the main thread can also slow down startup. You can address this issue as follows:
  - Move all resource initialization so that the app can perform it lazily on a different thread.
  - Let the app load and display your views, and then later update visual properties that are dependent on bitmaps and other resources.

### Custom splash screens

You might see extra time added during startup if you previously used one of the following methods to implement a custom splash screen in Android 11 (API level 30) or earlier:

- Using the[`windowDisablePreview`](https://developer.android.com/reference/android/R.attr#windowDisablePreview)theme attribute to turn off the initial blank screen drawn by the system during launch.
- Using a dedicated`Activity`.

Starting with Android 12, migrating to the[`SplashScreen`](https://developer.android.com/reference/android/window/SplashScreen)API is required. This API enables a faster startup time and lets you tweak your splash screen in the following ways:

- [Set a theme](https://developer.android.com/guide/topics/ui/splash-screen#set-theme)to change the splash screen's appearance.
- Control how long the splash screen is displayed with[`windowSplashScreenAnimationDuration`](https://developer.android.com/guide/topics/ui/splash-screen#suspend-drawing).
- Customize the[splash screen animation](https://developer.android.com/develop/ui/views/launch/splash-screen#customize-animation), and gracefully handle the animation for dismissing the splash screen.

Furthermore, the compat library backports the[`SplashScreen`API](https://developer.android.com/reference/kotlin/androidx/core/splashscreen/SplashScreen)to enable backward-compatibility and to create a consistent look and feel for splash screen display across all Android versions.

See the[Splash screen migration guide](https://developer.android.com/guide/topics/ui/splash-screen/migrate)for details.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Slow rendering](https://developer.android.com/topic/performance/vitals/render)
- [Capture Macrobenchmark metrics](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics)
- [Create Baseline Profiles{:#creating-profile-rules}](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile)