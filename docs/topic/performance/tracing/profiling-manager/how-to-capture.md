---
title: https://developer.android.com/topic/performance/tracing/profiling-manager/how-to-capture
url: https://developer.android.com/topic/performance/tracing/profiling-manager/how-to-capture
source: md.txt
---

This page shows how to record a system trace using the `ProfilingManager` API.

`ProfilingManager` can also record other profile types. This process is similar
to recording a system trace, but each type uses a different builder. The
supported profiles and their builders are:

- **System Traces:** Recorded using [`SystemTraceRequestBuilder`](https://developer.android.com/reference/androidx/core/os/SystemTraceRequestBuilder), which
  are useful for latency analysis and general performance debugging.

- **Heap dumps:** Recorded using [`JavaHeapDumpRequestBuilder`](https://developer.android.com/reference/androidx/core/os/JavaHeapDumpRequestBuilder), which are
  helpful for memory leak detection and optimization.

- **Heap profiles:** Recorded using [`HeapProfileRequestBuilder`](https://developer.android.com/reference/androidx/core/os/HeapProfileRequestBuilder), which
  are useful for memory optimization.

- **Call stack profiles:** Recorded using [`StackSamplingRequestBuilder`](https://developer.android.com/reference/androidx/core/os/StackSamplingRequestBuilder),
  which are useful for understanding code execution and latency analysis.

> [!TIP]
> **Tip:** `ProfilingManager` contains a rate limiter that is set up to reduce the impact of repeated profiling requests on device performance. When you're using this tool locally, you want to see every request so we recommend keeping the [rate limiter disabled](https://developer.android.com/topic/performance/tracing/profiling-manager/debug-mode#disable-rate-limiter).

## Add dependencies

For the best experience with the `ProfilingManager` API, add the following
Jetpack libraries to your `build.gradle.kts` file.

### Kotlin

```kotlin
   dependencies {
       implementation("androidx.tracing:tracing:1.3.0")
       implementation("androidx.core:core:1.17.0")
   }
   
```

### Groovy

```groovy
   dependencies {
       implementation 'androidx.tracing:tracing:1.3.0'
       implementation 'androidx.core:core:1.17.0'
   }
   
```

> [!NOTE]
> **Note:** You can use `ProfilingManager` directly without Jetpack libraries. However, Jetpack wrappers simplify usage, provide a compatibility layer, and reduce the effort needed to manage behavior across Android releases.

## Record a system trace

After adding the required dependencies, use the following code to record a
system trace. This example shows a basic setup within an `Activity` to start and
manage a profiling session.


### Kotlin

```kotlin
@RequiresApi(Build.VERSION_CODES.VANILLA_ICE_CREAM)
fun sampleRecordSystemTrace() {
    val mainExecutor: Executor =
        Dispatchers.IO.asExecutor() // Your choice of executor for the callback to occur on.
    val resultCallback = Consumer<ProfilingResult> { profilingResult ->
        if (profilingResult.errorCode == ProfilingResult.ERROR_NONE) {
            Log.d(
                "ProfileTest",
                "Received profiling result file=" + profilingResult.resultFilePath
            )
        } else {
            Log.e(
                "ProfileTest",
                "Profiling failed errorcode=" + profilingResult.errorCode + " errormsg=" + profilingResult.errorMessage
            )
        }
    }
    val stopSignal = CancellationSignal()

    val requestBuilder = SystemTraceRequestBuilder()
    requestBuilder.setCancellationSignal(stopSignal)
    requestBuilder.setTag("FOO") // Caller supplied tag for identification
    requestBuilder.setDurationMs(60000)
    requestBuilder.setBufferFillPolicy(BufferFillPolicy.RING_BUFFER)
    requestBuilder.setBufferSizeKb(20971520)
    requestProfiling(applicationContext, requestBuilder.build(), mainExecutor, resultCallback)

    // Wait some time for profiling to start.

    Trace.beginSection("MyApp:HeavyOperation")
    heavyOperation()
    Trace.endSection()

    // Once the interesting code section is profiled, stop profile
    stopSignal.cancel()
}

fun heavyOperation() {
    // Computations you want to profile
}
```

### Java

```java
void heavyOperation() {
  // Computations you want to profile
}

void sampleRecordSystemTrace() {
  Executor mainExecutor = Executors.newSingleThreadExecutor();
  Consumer<ProfilingResult> resultCallback =
      new Consumer<ProfilingResult>() {
        @Override
        public void accept(ProfilingResult profilingResult) {
          if (profilingResult.getErrorCode() == ProfilingResult.ERROR_NONE) {
            Log.d(
                "ProfileTest",
                "Received profiling result file=" + profilingResult.getResultFilePath());
            setupProfileUploadWorker(profilingResult.getResultFilePath());
          } else {
            Log.e(
                "ProfileTest",
                "Profiling failed errorcode="

                    + profilingResult.getErrorCode()
                    + " errormsg="
                    + profilingResult.getErrorMessage());
          }
        }
      };
  CancellationSignal stopSignal = new CancellationSignal();

  SystemTraceRequestBuilder requestBuilder = new SystemTraceRequestBuilder();
  requestBuilder.setCancellationSignal(stopSignal);
  requestBuilder.setTag("FOO");
  requestBuilder.setDurationMs(60000);
  requestBuilder.setBufferFillPolicy(BufferFillPolicy.RING_BUFFER);
  requestBuilder.setBufferSizeKb(20971520);
  Profiling.requestProfiling(getApplicationContext(), requestBuilder.build(), mainExecutor,
      resultCallback);

  // Wait some time for profiling to start.

  Trace.beginSection("MyApp:HeavyOperation");
  heavyOperation();
  Trace.endSection();

  // Once the interesting code section is profiled, stop profile
  stopSignal.cancel();
}
```

<br />

The sample code sets up and manages the profiling session by going through the
following steps:

1. **Set up the executor.** Create an `Executor` to define the thread that will
   receive the profiling results. Profiling happens in the background. Using a
   non-UI thread executor helps prevent Application Not Responding (ANR) errors
   if you add more processing to the callback later.

2. **Handle profiling results.** Create a `Consumer<ProfilingResult>` object.
   The system uses this object to send profiling results from
   `ProfilingManager` back to your app.

3. **Build the profiling request.** Create a `SystemTraceRequestBuilder` to set
   up your profiling session. This builder lets you customize
   `ProfilingManager` trace settings. Customizing the builder is optional; if
   you don't, the system uses default settings.

   - **Define a tag.** Use `setTag()` to add a tag to the trace name. This tag helps you identify the trace.
   - **Optional: Set the duration.** Use `setDurationMs()` to specify how long to profile in milliseconds. For example, `60000` sets a 60-second trace. The trace automatically ends after the specified duration if `CancellationSignal` isn't triggered before that.
   - **Choose a buffer policy.** Use `setBufferFillPolicy()` to define how trace data is stored. `BufferFillPolicy.RING_BUFFER` means that when the buffer is full, new data overwrites the oldest data, keeping a continuous record of recent activity.
   - **Set a buffer size.** Use `setBufferSizeKb()` to specify a buffer size for tracing which you can use to control the size of the output trace file.

   > [!NOTE]
   > **Note:** Not all the Perfetto configurations are available for `ProfilingManager`.

4. **Optional: Manage the session lifecycle.** Create a `CancellationSignal`.
   This object lets you stop the profiling session whenever you want, giving
   you precise control over its length.

   > [!NOTE]
   > **Note:** If you use neither `CancellationSignal` nor `setDurationMs()`, the system applies a default duration. If you define both, whichever happens first ends the session.

5. **Start and receive results.** When you call `requestProfiling()`,
   `ProfilingManager` starts a profiling session in the background. Once
   profiling is done, it sends the `ProfilingResult` to your
   `resultCallback#accept` method. If profiling finishes successfully, the
   `ProfilingResult` provides the path where the trace was saved on your device
   through `ProfilingResult#getResultFilePath`. You can get this file
   programmatically or, for local profiling, by running `adb pull <trace_path>`
   from your computer.

   > [!NOTE]
   > **Note:** If an error occurs during profiling, the `ProfilingResult` provides an error description through `profilingResult.getErrorMessage()` and an error code through `profilingResult.getErrorCode()`. A common reason for failure is if your app gets rate limited due to excessive requests.

   > [!NOTE]
   > **Note:** If the app dies before this result is delivered, delivery will be attempted again once the app starts and registers a general listener.

6. **Add custom trace points.** You can add custom trace points in your app's
   code. In the previous code example, a trace slice named
   `MyApp:HeavyOperation` is added using `Trace.beginSection()` and
   `Trace.endSection()`. This custom slice appears in the generated profile,
   highlighting specific operations within your app.