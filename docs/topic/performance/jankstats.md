---
title: https://developer.android.com/topic/performance/jankstats
url: https://developer.android.com/topic/performance/jankstats
source: md.txt
---

The JankStats library helps you track and analyze performance problems in your
applications. Jank refers to application frames that take too long to render,
and the JankStats library provides reports on the jank statistics of your app.

## Capabilities

JankStats builds on top of the existing Android platform capabilities, including
the [FrameMetrics API](https://developer.android.com/reference/android/view/FrameMetrics)
on Android 7 (API level 24) and higher or [OnPreDrawListener](https://developer.android.com/reference/android/view/ViewTreeObserver.OnPreDrawListener) on earlier
versions. These mechanisms can help applications track how long frames take to
complete. The JanksStats library offers two additional capabilities that make it
more dynamic and easier to use: jank heuristics and UI state.

### Jank heuristics

While you can use FrameMetrics to track frame durations, FrameMetrics doesn't
offer any assistance in determining actual jank. JankStats, however, has
configurable, internal mechanisms to determine when jank occurs, making the
reports more immediately useful.

### UI state

It's often necessary to know the context of performance problems in your app.
For example, if you develop a complex, multi-screen app that uses FrameMetrics
and you discover that your app often has extremely janky frames, you'll want
to contextualize that information by knowing where the problem occurred, what
the user was doing, and how to replicate it.

JankStats solves this problem by introducing a `state` API that lets you
communicate with the library to provide information about app Activity. When
JankStats logs information about a janky frame, it includes the current state of
the application in jank reports.

## Usage

To begin using JankStats, instantiate and enable the library for each
[`Window`](https://developer.android.com/reference/android/view/Window). Each JankStats object tracks data
only within a `Window`. Instantiating the library requires a `Window` instance
along with an [`OnFrameListener`](https://developer.android.com/reference/androidx/metrics/performance/JankStats.OnFrameListener)
listener, both of which are used to send metrics to the client. The listener is called with
[`FrameData`](https://developer.android.com/reference/androidx/metrics/performance/FrameData) on every frame
and details the:

- Frame start time
- Duration values
- Whether or not the frame should be considered jank
- A set of String pairs containing information about the application state during the frame

To make JankStats more useful, applications should populate the library with
relevant UI state information for reporting in the FrameData. You can do this
through the
[`PerformanceMetricsState`](https://developer.android.com/reference/androidx/metrics/performance/PerformanceMetricsState)
API (not JankStats directly), where all of the state management logic and APIs
live.

### Initialization

To begin using the JankStats library, first add the JankStats dependency to your
Gradle file:  

    implementation "androidx.metrics:metrics-performance:1.0.0"

Next, initialize and enable JankStats for each `Window`. You should also pause
JankStats tracking when an Activity goes into the background. Create and enable
the JankStats object in your Activity overrides:  

    class JankLoggingActivity : AppCompatActivity() {

        private lateinit var jankStats: JankStats


        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            // ...
            // metrics state holder can be retrieved regardless of JankStats initialization
            val metricsStateHolder = PerformanceMetricsState.getHolderForHierarchy(binding.root)

            // initialize JankStats for current window
            jankStats = JankStats.createAndTrack(window, jankFrameListener)

            // add activity name as state
            metricsStateHolder.state?.putState("Activity", javaClass.simpleName)
            // ...
        }  
    https://github.com/android/performance-samples/blob/cae5530b13ce3adf7bd54ea5bd92fe9b4fb8c585/JankStatsSample/app/src/main/java/com/example/jankstats/JankLoggingActivity.kt#L38-L73

The example above injects state information about the current
Activity after it constructs the JankStats object. All future FrameData reports
created for this JankStats object now also includes Activity information.

The `JankStats.createAndTrack` method takes a reference to a `Window`
object, which is a proxy for the View hierarchy inside that `Window` as well as
for the `Window` itself. `jankFrameListener` is called on the same thread used
to deliver that information from the platform to JankStats internally.
| **Note:** The window must be active with a non-null DecorView, otherwise it returns an `IllegalStateException`.

To enable tracking and reporting on any JankStats object,
call `isTrackingEnabled = true`. Although it's enabled by default,
pausing an activity disables tracking. In this case, make sure to re-enable
tracking before proceeding. To stop tracking, call `isTrackingEnabled = false`.  

    override fun onResume() {
        super.onResume()
        jankStats.isTrackingEnabled = true
    }

    override fun onPause() {
        super.onPause()
        jankStats.isTrackingEnabled = false
    }  
    https://github.com/android/performance-samples/blob/cae5530b13ce3adf7bd54ea5bd92fe9b4fb8c585/JankStatsSample/app/src/main/java/com/example/jankstats/JankLoggingActivity.kt#L77-L85

### Reporting

The JankStats library reports all of your data tracking, for every frame, to the
[`OnFrameListener`](https://developer.android.com/reference/androidx/metrics/performance/JankStats.OnFrameListener)
for enabled JankStats objects. Apps can store and aggregate this
data for uploading at a later time. For more information, take
a look at the examples provided in the [Aggregation](https://developer.android.com/topic/performance/jankstats#aggregating) section.

You'll need to create and supply the `OnFrameListener` for your app to receive
the per-frame reports. This listener is called on every frame to supply ongoing
jank data to apps.  

    private val jankFrameListener = JankStats.OnFrameListener { frameData ->
        // A real app could do something more interesting, like writing the info to local storage and later on report it.
        Log.v("JankStatsSample", frameData.toString())
    }  
    https://github.com/android/performance-samples/blob/cae5530b13ce3adf7bd54ea5bd92fe9b4fb8c585/JankStatsSample/app/src/main/java/com/example/jankstats/JankLoggingActivity.kt#L48-L51

The listener provides per-frame information about jank with the
[`FrameData`](https://developer.android.com/reference/androidx/metrics/performance/FrameData) object. This
contains the following information about the requested frame:

- **[`isjank`](https://developer.android.com/reference/androidx/metrics/performance/FrameData#isJank())**: A boolean flag that indicates whether jank occurred in the frame.
- **[`frameDurationUiNanos`](https://developer.android.com/reference/androidx/metrics/performance/FrameData#frameDurationUiNanos())**: Duration of the frame (in nanoseconds).
- **[`frameStartNanos`](https://developer.android.com/reference/androidx/metrics/performance/FrameData#frameStartNanos())**: Time at which the frame began (in nanoseconds).
- **[`states`](https://developer.android.com/reference/androidx/metrics/performance/FrameData#states())**: State of your app during the frame.

If you are on Android 12 (API level 31) or higher, you can
use the following to expose more data about frame durations:

- [`FrameDataApi24`](https://developer.android.com/reference/androidx/metrics/performance/FrameDataApi24) provides [`frameDurationCpuNanos`](https://developer.android.com/reference/androidx/metrics/performance/FrameDataApi24#frameDurationCpuNanos()) to display the time spent in the non-GPU portions of the frame.
- [`FrameDataApi31`](https://developer.android.com/reference/androidx/metrics/performance/FrameDataApi31) provides [`frameOverrunNanos`](https://developer.android.com/reference/androidx/metrics/performance/FrameDataApi31#frameOverrunNanos()) to display the amount of time past the frame deadline that the frame took to complete.

Use [`StateInfo`](https://developer.android.com/reference/androidx/metrics/performance/StateInfo) in the
listener to store information about the application state.

Note that `OnFrameListener` is called on the same thread used internally to
deliver the per-frame information to JankStats.
On Android version 6 (API level 23) and lower, that is the Main (UI) thread.
On Android version 7 (API level 24) and higher, it is the
thread created for and used by FrameMetrics. In either case, it is important to
handle the callback and return quickly to prevent performance problems on
that thread.

Also, note that the FrameData object sent in the callback is reused on every
frame to prevent having to allocate new objects for data reporting. This means
that you must copy and cache that data elsewhere since that object should be
considered statle and obsolete as soon as the callback returns.

### Aggregating

You'll likely want your app code to aggregate the per-frame data, which allows
you to save and upload the information at your own discretion. Although details
around saving and uploading are beyond the scope of the alpha JankStats API
release, you can view a preliminary Activity for aggregating per-frame data
into a larger collection using `JankAggregatorActivity` available in our
[GitHub repository](https://github.com/android/performance-samples/tree/main/JankStatsSample).

[`JankAggregatorActivity`](https://github.com/android/performance-samples/blob/main/JankStatsSample/app/src/main/java/com/example/jankstats/JankAggregatorActivity.kt)
uses the `JankStatsAggregator` class to layer its own reporting
mechanism on top of the JankStats `OnFrameListener` mechanism to provide a
higher level abstraction for reporting only a collection of information that
spans many frames.

Instead of creating a JankStats object directly, `JankAggregatorActivity`
creates a [JankStatsAggregator](https://github.com/android/performance-samples/blob/main/JankStatsSample/app/src/main/java/com/example/jankstats/JankStatsAggregator.kt)
object, which creates its own JankStats object internally:  

    class JankAggregatorActivity : AppCompatActivity() {

        private lateinit var jankStatsAggregator: JankStatsAggregator


        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            // ...
            // Metrics state holder can be retrieved regardless of JankStats initialization.
            val metricsStateHolder = PerformanceMetricsState.getHolderForHierarchy(binding.root)

            // Initialize JankStats with an aggregator for the current window.
            jankStatsAggregator = JankStatsAggregator(window, jankReportListener)

            // Add the Activity name as state.
            metricsStateHolder.state?.putState("Activity", javaClass.simpleName)
        }  
    https://github.com/android/performance-samples/blob/cae5530b13ce3adf7bd54ea5bd92fe9b4fb8c585/JankStatsSample/app/src/main/java/com/example/jankstats/JankAggregatorActivity.kt#L38-L81

A similar mechanism is used in `JankAggregatorActivity` to pause and
resume tracking, with the addition of the `pause()` event as a signal to issue
a report with a call to `issueJankReport()`, as lifecycle changes seem like an
appropriate time to capture the state of jank in the application:  

    override fun onResume() {
        super.onResume()
        jankStatsAggregator.jankStats.isTrackingEnabled = true
    }

    override fun onPause() {
        super.onPause()
        // Before disabling tracking, issue the report with (optionally) specified reason.
        jankStatsAggregator.issueJankReport("Activity paused")
        jankStatsAggregator.jankStats.isTrackingEnabled = false
    }  
    https://github.com/android/performance-samples/blob/cae5530b13ce3adf7bd54ea5bd92fe9b4fb8c585/JankStatsSample/app/src/main/java/com/example/jankstats/JankAggregatorActivity.kt#L85-L95

The example code above is all that an app needs to enable JankStats and receive
frame data.

### Manage the state

It's possible that you may want to call other APIs to customize JankStats. For
instance, injecting app state information makes frame data more helpful by
providing context for those frames in which jank occurs.

This static method retrieves the current
[`MetricsStateHolder`](https://developer.android.com/reference/androidx/metrics/performance/PerformanceMetricsState.Holder)
object for a given View hierarchy.  

    PerformanceMetricsState.getHolderForHierarchy(view: View): MetricsStateHolder

Any view in an active hierarchy may be used. Internally, this checks to see
whether there's an existing `Holder` object associated with that
view hierarchy. This information is cached in a view at the top of that
hierarchy. If no such object exists, `getHolderForHierarchy()` creates one.

The static `getHolderForHierarchy()` method allows you to avoid having to cache
the holder instance somewhere for later retrieval, and makes it easier to retrieve
an existing state object from anywhere in the code (or even library code, which
would not otherwise have access to the original instance).

Note that the return value is a holder object, not the state object itself. The
value of the state object inside of the holder is set only by JankStats. That
is, if an application creates a JankStats object for the window containing that
view hierarchy, then the state object is
created and set. Otherwise, without JankStats tracking the information, there is
no need for the state object, and it's not necessary for app or library
code to inject state.

This approach makes it possible to
retrieve a holder that JankStats can then populate. External code
can ask for the holder at any time. Callers can cache the lightweight `Holder`
object and use it at any time to set state, depending on the value of its
internal `state` property, as in the example code below, where state is only set
when the holder's internal state property is non-null:  

    val metricsStateHolder = PerformanceMetricsState.getHolderForHierarchy(binding.root)
    // ...
    metricsStateHolder.state?.putState("Activity", javaClass.simpleName)

To control the UI/app state, an app can inject (or remove) a state
with the `putState` and `removeState` methods. JankStats logs the timestamp for
these calls. If a frame overlaps the start and end time of the state,
JankStats reports that state information along with the timing data for the
frame.

For any state, add two pieces of information: `key`
(a category of state, such as "RecyclerView") and `value` (information about
what was happening at the time, such as "scrolling").

Remove states using the `removeState()` method when that state is no
longer valid, to ensure that wrong or misleading information is not reported
with frame data.

Calling `putState()` with a `key` that was added previously replaces the
existing `value` of that state with the new one.

The `putSingleFrameState()` version of the state API adds a state that is
logged only once, on the next reported frame. The system automatically
removes it after that, ensuring you don't accidentally have obsolete state in
your code. Note that there is no singleFrame equivalent of
`removeState()`, since JankStats removes single-frame states automatically.  

    private val scrollListener = object : RecyclerView.OnScrollListener() {
        override fun onScrollStateChanged(recyclerView: RecyclerView, newState: Int) {
            // check if JankStats is initialized and skip adding state if not
            val metricsState = metricsStateHolder?.state ?: return

            when (newState) {
                RecyclerView.SCROLL_STATE_DRAGGING -> {
                    metricsState.putState("RecyclerView", "Dragging")
                }
                RecyclerView.SCROLL_STATE_SETTLING -> {
                    metricsState.putState("RecyclerView", "Settling")
                }
                else -> {
                    metricsState.removeState("RecyclerView")
                }
            }
        }
    }  
    https://github.com/android/performance-samples/blob/cae5530b13ce3adf7bd54ea5bd92fe9b4fb8c585/JankStatsSample/app/src/main/java/com/example/jankstats/MessageListFragment.kt#L42-L59

Note that the key used for states should be meanigful enough to allow for
later analysis. In particular, since a state with the same `key` as one that
was added previously will replace that earlier value, you should try to use
unique `key` names for objects that may have different instances in your
app or library. For example, an app with five different RecyclerViews may
want to provide identifable keys for each of them instead of simply using
`RecyclerView` for each one and then not being able to easily tell in the
resulting data which instance the frame data refers to.

### Jank heuristics

To adjust the internal algorithm for determining what is considered jank, use
the `jankHeuristicMultiplier` property.

By default, the system defines jank as a frame taking twice as long to render as
the current refresh rate. It doesn't treat jank as anything over the
refresh rate because the information around app rendering time isn't entirely
clear. Therefore, it's considered better to add a buffer and only report
problems when they cause noticeable performance issues.

Both of these values can be changed through these methods to suit the situation
of the app more closely, or in testing to force jank to occur or not occur, as
necessary for the test.

### Usage in Jetpack Compose

Currently there is very little setup required to use JankStats in Compose.
To hold on to the `PerformanceMetricsState` across configuration changes,
remember it like so:  

    /**
     * Retrieve MetricsStateHolder from compose and remember until the current view changes.
     */
    @Composable
    fun rememberMetricsStateHolder(): PerformanceMetricsState.Holder {
        val view = LocalView.current
        return remember(view) { PerformanceMetricsState.getHolderForHierarchy(view) }
    }  
    https://github.com/android/performance-samples/blob/cae5530b13ce3adf7bd54ea5bd92fe9b4fb8c585/JankStatsSample/app/src/main/java/com/example/jankstats/compose/rememberMetricsStateHolder.kt#L9-L16

And to use JankStats, add the current state to the `stateHolder` as shown here:  

    val metricsStateHolder = rememberMetricsStateHolder()

    // Reporting scrolling state from compose should be done from side effect to prevent recomposition.
    LaunchedEffect(metricsStateHolder, listState) {
        snapshotFlow { listState.isScrollInProgress }.collect { isScrolling ->
            if (isScrolling) {
                metricsStateHolder.state?.putState("LazyList", "Scrolling")
            } else {
                metricsStateHolder.state?.removeState("LazyList")
            }
        }
    }  
    https://github.com/android/performance-samples/blob/cae5530b13ce3adf7bd54ea5bd92fe9b4fb8c585/JankStatsSample/app/src/main/java/com/example/jankstats/compose/ComposeListFragment.kt#L74-L85

For full details on using JankStats in your Jetpack Compose application, check
out our [performance sample app](https://github.com/android/performance-samples/tree/main/JankStatsSample/app/src/main/java/com/example/jankstats/compose).

## Provide feedback

Share your feedback and ideas with us through these resources:

[Issue tracker](https://issuetracker.google.com/issues/new?component=1109743&template=1621342) :bug:
:   Report issues so we can fix bugs.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Create Baseline Profiles {:#creating-profile-rules}](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile)
- [Microbenchmark Instrumentation Arguments](https://developer.android.com/topic/performance/benchmarking/microbenchmark-instrumentation-args)
- [Macrobenchmark Instrumentation Arguments](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-instrumentation-args)