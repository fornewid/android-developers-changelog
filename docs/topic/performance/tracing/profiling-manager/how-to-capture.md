---
title: https://developer.android.com/topic/performance/tracing/profiling-manager/how-to-capture
url: https://developer.android.com/topic/performance/tracing/profiling-manager/how-to-capture
source: md.txt
---

On Android 15 (API level 35) and higher, app-driven profiling lets your app
explicitly start and stop [supported profile recordings](https://developer.android.com/topic/performance/tracing/profiling-manager/overview#supported-profile-types) in code using the
[`ProfilingManager`](https://developer.android.com/reference/android/os/ProfilingManager) API or AndroidX Core (`androidx.core:core` 1.15.0 or
higher) builders. Use direct profiling when you want to control profile timing
or session parameters---such as durations, buffer policies, and sampling rates---or
target a specific user journey or runtime condition.

> [!TIP]
> **Tip:** When testing locally, [disable the rate limiter](https://developer.android.com/topic/performance/tracing/profiling-manager/debug-mode#disable-rate-limiter) so `ProfilingManager` captures every request without throttling.

## Add dependencies

For the best experience with the `ProfilingManager` API, add the following
Jetpack libraries to your `build.gradle.kts` file.

### Kotlin

```kotlin
   dependencies {
       implementation("androidx.tracing:tracing-ktx:2.0.5")
       implementation("androidx.core:core:1.19.1")
   }
   
```

### Groovy

```groovy
   dependencies {
       implementation 'androidx.tracing:tracing-ktx:2.0.5'
       implementation 'androidx.core:core:1.19.1'
   }
   
```

> [!NOTE]
> **Note:** You can use `ProfilingManager` directly without Jetpack libraries. However, Jetpack wrappers simplify usage, provide a compatibility layer, and reduce the effort needed to manage behavior across Android releases.

## Record a system trace

After adding the required dependencies, use the following code to record a
system trace. This example shows how to start a profiling session while safely
managing heavy operations off the main thread.


### Kotlin

```kotlin
@RequiresApi(Build.VERSION_CODES.VANILLA_ICE_CREAM)
@Composable
fun ProfiledScreen(modifier: Modifier = Modifier) {
    // Use the application context: requestProfiling resolves the ProfilingManager
    // system service from it, so there's no reason to hand it a short-lived Activity.
    val appContext = LocalContext.current.applicationContext
    val scope = rememberCoroutineScope()

    Button(
        onClick = {
            // Run the orchestration off the main thread. Profiling a heavy operation
            // on the UI thread would freeze the UI (ANR) and distort the very metrics
            // you're trying to capture.
            //
            // Note: this scope is tied to composition. If the user leaves this screen
            // mid-session, the coroutine is cancelled and stopSignal.cancel() might not
            // run, but setDurationMs() acts as a safety net and ends the profile.
            scope.launch(Dispatchers.Default) {
                val callbackExecutor = Dispatchers.IO.asExecutor()
                val resultCallback = Consumer<ProfilingResult> { profilingResult ->
                    if (profilingResult.errorCode == ProfilingResult.ERROR_NONE) {
                        Log.d("ProfileTest", "Result file: ${profilingResult.resultFilePath}")
                    } else {
                        // errorMessage explains the failure (e.g., rate limiting); keep it.
                        Log.e(
                            "ProfileTest",
                            "Profiling failed errorCode=${profilingResult.errorCode} " +
                                "errorMessage=${profilingResult.errorMessage}"
                        )
                    }
                }

                val stopSignal = CancellationSignal()
                val requestBuilder = SystemTraceRequestBuilder().apply {
                    setCancellationSignal(stopSignal)
                    setTag("FOO") // Caller-supplied tag for identification.
                    setDurationMs(60000) // Hard cap: ends the session if cancel() never fires.
                    setBufferFillPolicy(BufferFillPolicy.RING_BUFFER)
                    setBufferSizeKb(32768)
                }

                // 1. Start the session. This is asynchronous system IPC. The tracing
                //    engine takes a moment to start and allocate buffers.
                requestProfiling(appContext, requestBuilder.build(), callbackExecutor, resultCallback)

                // 2. The API exposes no "profiling started" signal, so pad with a short,
                //    best-effort delay before running the code you care about. This is
                //    approximate. Increase it on slower or heavily loaded devices.
                delay(STARTUP_PADDING_MS)

                // 3. The session is already recording every thread in your app. This slice
                //    doesn't scope what's captured. It just labels this region of the
                //    timeline so heavyOperation() is easier to find. trace { } closes the
                //    section even if the block throws.

                trace("MyApp:HeavyOperation") {
                    heavyOperation()
                }

                // 4. Stop recording. Until this fires or the setDurationMs() cap is
                //    reached (whichever comes first), the session keeps capturing app-wide
                //    activity.

                stopSignal.cancel()
            }
        }
    ) {
        Text("Run & Profile Heavy Operation")
    }
}

// Best-effort wait for the system trace engine to initialize before profiling.
// There is no deterministic start callback; tune this for your target devices.
private const val STARTUP_PADDING_MS = 100L

fun heavyOperation() {
    // Background computations to profile.
}
```

### Java

```java
void sampleRecordSystemTrace(Context context) {
  // Use the application context: requestProfiling resolves the ProfilingManager
  // system service from it, so there's no reason to hand it a short-lived Activity.
  Context appContext = context.getApplicationContext();

  // Run the orchestration off the main thread. Profiling a heavy operation
  // on the UI thread would freeze the UI (ANR) and distort the very metrics
  // you're trying to capture.
  profilingExecutor.execute(() -> {
    Executor callbackExecutor = Executors.newSingleThreadExecutor();
    Consumer<ProfilingResult> resultCallback = profilingResult -> {
      if (profilingResult.getErrorCode() == ProfilingResult.ERROR_NONE) {
        Log.d("ProfileTest", "Result file: " + profilingResult.getResultFilePath());
      } else {
        // errorMessage explains the failure (e.g., rate limiting); keep it.
        Log.e(
            "ProfileTest",
            "Profiling failed errorCode=" + profilingResult.getErrorCode()
                + " errorMessage=" + profilingResult.getErrorMessage());
      }
    };

    CancellationSignal stopSignal = new CancellationSignal();
    SystemTraceRequestBuilder requestBuilder = new SystemTraceRequestBuilder();
    requestBuilder.setCancellationSignal(stopSignal);
    requestBuilder.setTag("FOO"); // Caller-supplied tag for identification.
    requestBuilder.setDurationMs(60000); // Hard cap: ends the session if cancel() never fires.
    requestBuilder.setBufferFillPolicy(BufferFillPolicy.RING_BUFFER);
    requestBuilder.setBufferSizeKb(32768);

    // 1. Start the session. This is asynchronous system IPC. The tracing
    //    engine takes a moment to start and allocate buffers.
    Profiling.requestProfiling(
        appContext, requestBuilder.build(), callbackExecutor, resultCallback);

    // 2. The API exposes no "profiling started" signal, so pad with a short,
    //    best-effort delay before running the code you care about. This is
    //    approximate. Increase it on slower or heavily loaded devices.
    try {
      Thread.sleep(STARTUP_PADDING_MS);
    } catch (InterruptedException e) {
      Thread.currentThread().interrupt();
      stopSignal.cancel();
      return;
    }

    // 3. The session is already recording every thread in your app. This slice
    //    doesn't scope what's captured. It just labels this region of the
    //    timeline so heavyOperation() is easier to find. try/finally closes the
    //    section even if heavyOperation() throws.
    Trace.beginSection("MyApp:HeavyOperation");
    try {
      heavyOperation();
    } finally {
      Trace.endSection();
    }

    // 4. Stop recording. Until this fires or the setDurationMs() cap is
    //    reached (whichever comes first), the session keeps capturing app-wide
    //    activity.
    stopSignal.cancel();
  });
}

// Best-effort wait for the system trace engine to initialize before profiling.
// There is no deterministic start callback; tune this for your target devices.
private static final long STARTUP_PADDING_MS = 100L;

// Single background thread that runs the profiling orchestration.
private final ExecutorService profilingExecutor = Executors.newSingleThreadExecutor();

void heavyOperation() {
  // Background computations to profile.
}
```

<br />

The sample code sets up and manages the profiling session in the following
steps:

1. **Set up the executor** : Create a non-UI `Executor` to receive profiling results off the main thread.
2. **Handle profiling results** : Create a `Consumer<ProfilingResult>` callback to receive the completed result or error from `ProfilingManager`.
3. **Build the profiling request** : Create a [`SystemTraceRequestBuilder`](https://developer.android.com/reference/kotlin/androidx/core/os/SystemTraceRequestBuilder)
   to customize session settings (or omit customizations to use system
   defaults):

   - `setTag()`: Attaches a caller-supplied tag that is returned by [`ProfilingResult.getTag`](https://developer.android.com/reference/android/os/ProfilingResult#getTag()) and appended to the output filename (up to the first 20 lowercase alphanumeric characters and hyphens).
   - `setDurationMs()`: Sets the maximum recording duration in milliseconds (for example, `60000` for 60 seconds).
   - `setBufferFillPolicy()`: Defines how the buffer handles capacity limits: `BufferFillPolicy.RING_BUFFER` overwrites the oldest data when full, whereas `BufferFillPolicy.DISCARD` stops recording new data once the buffer is full.
   - `setBufferSizeKb()`: Sets the recording buffer size in kilobytes.

   > [!NOTE]
   > **Note:** Not all Perfetto configurations are available for `ProfilingManager`.

4. **Optional: Stop the recording early** : Pass a [`CancellationSignal`](https://developer.android.com/reference/android/os/CancellationSignal)
   (`stopSignal`) to stop the session as soon as the target operation finishes,
   saving the data recorded so far and delivering the `ProfilingResult` to your
   callback. See [Stop an active recording](https://developer.android.com/topic/performance/tracing/profiling-manager/how-to-capture#stop-active-recording) for details.

5. **Start and receive results** : Call `requestProfiling()` to start recording
   in the background. When the session ends, `resultCallback.accept()` receives
   a [`ProfilingResult`](https://developer.android.com/reference/android/os/ProfilingResult):

   - On success (`ERROR_NONE`), call `getResultFilePath()` to get the on-device path. For instructions on pulling files with `adb` or uploading them with `WorkManager`, see [Retrieve and upload
     profiles](https://developer.android.com/topic/performance/tracing/profiling-manager/upload-worker).
   - On failure, inspect `getErrorCode()` and `getErrorMessage()`. Requests can fail due to [rate limiting](https://developer.android.com/topic/performance/tracing/profiling-manager/will-my-profile-always-be-collected) as well as several other reasons.
   - If your app terminates before the result is delivered, the system queues the result and delivers it the next time your app registers a global listener with [`registerForAllProfilingResults`](https://developer.android.com/reference/android/os/ProfilingManager#registerForAllProfilingResults(java.util.concurrent.Executor,%20java.util.function.Consumer%3Candroid.os.ProfilingResult%3E)).
6. **Add custom trace points** : Wrap operations in `trace("...") { ... }` (or
   `Trace.beginSection()` / `Trace.endSection()`) to label regions of the
   timeline.

> [!TIP]
> **Tip:** In Jetpack Compose apps, combine custom trace points with [composition
> tracing](https://developer.android.com/develop/ui/compose/tooling/tracing) to inspect recompositions in the same trace.

### Stop an active recording

To stop a capture as soon as an interaction completes rather than waiting for
`setDurationMs()` to expire, pass a `CancellationSignal` to
`setCancellationSignal()` or `requestProfiling()`. If you specify both
`CancellationSignal` and `setDurationMs()`, whichever happens first ends the
session; if you specify neither, the system applies a default duration.

Calling `cancel()` doesn't discard the recording. The system stops the capture,
redacts and saves the data collected up to that point, and delivers the
`ProfilingResult` to your listener with `ERROR_NONE`.

> [!NOTE]
> **Note:** Recording doesn't begin instantaneously when you call `requestProfiling()`, and `ProfilingManager` doesn't emit a callback when recording starts. Account for a brief startup delay when timing your request, or start a `RING_BUFFER` trace ahead of time and cancel it after the event occurs. On Android 16 QPR2 (API level 36.1) and higher, if it's difficult to predict when to start a trace in advance, you can also register [`TRIGGER_TYPE_APP_REQUEST_RUNNING_TRACE`](https://developer.android.com/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_APP_REQUEST_RUNNING_TRACE) and call [`requestRunningSystemTrace()`](https://developer.android.com/reference/android/os/ProfilingManager#requestRunningSystemTrace(java.lang.String)) to save a snapshot of an active [background
> trace](https://developer.android.com/topic/performance/tracing/profiling-manager/trigger-based-capture#background-trace-triggers), if one is running.

## Record system traces with call stack sampling

On devices running Android 17 (API level 37) and higher (or Android 16 with an
updated `Profiling` mainline module), `ProfilingManager` supports collecting
sampled call stacks alongside a system trace in a single session so you can see
timeline events, such as thread states, frames, and custom trace slices,
together with CPU call stacks for methods without explicit trace
instrumentation.

This example also shows how to call [`ProfilingManager.requestProfiling`](https://developer.android.com/reference/android/os/ProfilingManager#requestProfiling(int,%20android.os.Bundle,%20java.lang.String,%20android.os.CancellationSignal,%20java.util.concurrent.Executor,%20java.util.function.Consumer%3Candroid.os.ProfilingResult%3E))
directly without Jetpack builders by specifying one of the [supported profile
types](https://developer.android.com/topic/performance/tracing/profiling-manager/overview#supported-profile-types) ([`PROFILING_TYPE_SYSTEM_TRACE`](https://developer.android.com/reference/android/os/ProfilingManager#PROFILING_TYPE_SYSTEM_TRACE)) and passing a configuration
`Bundle`:


### Kotlin

```kotlin
val profilingManager = context.getSystemService(ProfilingManager::class.java)

// Pass a Bundle to customize the capture, or pass null for default settings.
val config = Bundle().apply {
    putInt("KEY_DURATION_MS", 15000) // 15 seconds
    putInt("KEY_SIZE_KB", 20480) // 20 MB buffer size

    // Collect sampled CPU call stacks alongside the system trace.
    putBoolean("KEY_COLLECT_STACK_SAMPLING", true)
    putInt("KEY_FREQUENCY_HZ", 100) // Sampling frequency in Hz
    // Optional: Set KEY_SAMPLE_BINDER_ONLY to true to sample only binder calls.
}
profilingManager?.requestProfiling(
    ProfilingManager.PROFILING_TYPE_SYSTEM_TRACE,
    config,
    "trace-with-callstacks",
    null,
    callbackExecutor,
    resultCallback
)
```

### Java

```java
ProfilingManager profilingManager = context.getSystemService(ProfilingManager.class);
if (profilingManager == null) return;

// Pass a Bundle to customize the capture, or pass null for default settings.
Bundle config = new Bundle();
config.putInt("KEY_DURATION_MS", 15000); // 15 seconds
config.putInt("KEY_SIZE_KB", 20480); // 20 MB buffer size

// Collect sampled CPU call stacks alongside the system trace.
config.putBoolean("KEY_COLLECT_STACK_SAMPLING", true);
config.putInt("KEY_FREQUENCY_HZ", 100); // Sampling frequency in Hz
// Optional: Set KEY_SAMPLE_BINDER_ONLY to true to sample only binder calls.

profilingManager.requestProfiling(
    ProfilingManager.PROFILING_TYPE_SYSTEM_TRACE,
    config,
    "trace-with-callstacks",
    null,
    callbackExecutor,
    resultCallback
);
```

<br />

When you open the resulting profile in the [Perfetto UI](https://ui.perfetto.dev/), the sampled call
stacks appear as dedicated **Callstacks** tracks alongside your app's regular
trace slices. Select a region of a call stack track to view a flame graph of the
sampled call stacks for that time range, as shown in Figure 1.
![Perfetto UI showing a system trace with sampled call stack tracks, trace
slices on the RenderThread, and a call stack flame graph for the selected
area.](https://developer.android.com/static/topic/performance/images/tracing/profilingmanager-system-trace-with-callstacks.png) **Figure 1.** A system trace combined with call stack sampling in the Perfetto UI.

## Capture a Java heap dump

You can request a snapshot of your app's Java memory using
[`JavaHeapDumpRequestBuilder`](https://developer.android.com/reference/kotlin/androidx/core/os/JavaHeapDumpRequestBuilder) (or [`PROFILING_TYPE_JAVA_HEAP_DUMP`](https://developer.android.com/reference/android/os/ProfilingManager#PROFILING_TYPE_JAVA_HEAP_DUMP)).
Unlike standard `.hprof` heap dumps captured with [`Debug.dumpHprofData`](https://developer.android.com/reference/android/os/Debug#dumpHprofData(java.lang.String)),
`ProfilingManager` heap dumps are designed for safe, low-overhead collection in
production:

- **Non-freezing collection**: The system forks a copy-on-write clone of your app's process and collects the heap snapshot from the cloned process, so your app doesn't freeze while the dump is written to disk.
- **Reference graph only (no raw object data)** : Instead of dumping raw memory contents like an `.hprof` file, `ProfilingManager` records a `.perfetto-java-heap-dump` protobuf graph containing classes, object sizes, reference chains, and garbage collection (GC) roots while omitting primitive values, string contents, and array payloads. This protects user privacy and reduces file size. For a full breakdown, see [How ProfilingManager heap
  dumps differ from HPROF dumps](https://developer.android.com/topic/performance/tracing/profiling-manager/retrieve-and-analyze#heap-dump-differences).

> [!NOTE]
> **Note:** Capturing Java heap dumps, heap profiles, and call stack samples on a release build requires your app to be [profileable](https://developer.android.com/guide/topics/manifest/profileable-element) by the system, which is enabled by default unless your `AndroidManifest.xml` file explicitly sets `<profileable android:enabled="false" />`.

Using the same `Context`, `Executor`, and `resultCallback` setup shown in
[Record a system trace](https://developer.android.com/topic/performance/tracing/profiling-manager/how-to-capture#record-system-trace), build a request with
[`JavaHeapDumpRequestBuilder`](https://developer.android.com/reference/kotlin/androidx/core/os/JavaHeapDumpRequestBuilder):


### Kotlin

```kotlin
val heapDumpRequest = JavaHeapDumpRequestBuilder()
    .setTag("memory-leak-check")
    .build()

requestProfiling(
    appContext,
    heapDumpRequest,
    callbackExecutor,
    resultCallback
)
```

### Java

```java
ProfilingRequest heapDumpRequest = new JavaHeapDumpRequestBuilder()
    .setTag("memory-leak-check")
    .build();

Profiling.requestProfiling(
    getApplicationContext(),
    heapDumpRequest,
    callbackExecutor,
    resultCallback
);
```

<br />

For a complete end-to-end walkthrough of analyzing a Java heap dump to diagnose
a memory leak, see [Case study: Debug an OOM crash](https://developer.android.com/topic/performance/tracing/profiling-manager/debugging-oom-example).

## Next steps

After capturing profiles, [retrieve them locally with `adb` or upload them to
your backend with `WorkManager`](https://developer.android.com/topic/performance/tracing/profiling-manager/upload-worker).