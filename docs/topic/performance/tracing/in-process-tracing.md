---
title: https://developer.android.com/topic/performance/tracing/in-process-tracing
url: https://developer.android.com/topic/performance/tracing/in-process-tracing
source: md.txt
---

The new [`androidx.tracing:tracing:2.0.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/tracing) library is a low-overhead
Kotlin API that allows capturing in-process trace events. These events can
capture time slices and their context. The library additionally supports context
propagation for Kotlin Coroutines.

The library uses the same [Perfetto](https://perfetto.dev) trace packet format that Android
developers are familiar with. Also, Tracing `2.0` (unlike the `1.0.0-*` APIs)
supports the notion of **pluggable tracing backends** and **sinks** , so other
tracing libraries can **customize** the output tracing format, and how context
propagation works in their implementation.

> [!NOTE]
> **Note:** During the `alpha` period, we initially suggest experimenting with this library host-side (given it supports the JVM target), and self contained tracing scenarios on device. The library does not integrate with [Android Studio profilers](https://developer.android.com/studio/profile/android-profiler), and [Benchmarking libraries](https://developer.android.com/topic/performance/benchmarking) yet. Merging with system tracing while possible and trivial does not work out of the box yet. There are [instructions](https://developer.android.com/topic/performance/tracing/in-process-tracing#combine-with-system-traces) on how to accomplish that for those interested, but these workflows should get a lot easier in subsequent releases of the library.

## Dependencies

To start tracing, you need to define the following dependencies in your
`build.gradle.kts`.

    kotlin {
      androidLibrary {
        namespace = "com.example.library"
        // ...
      }
      sourceSets {
        androidMain {
          dependencies {
            api("androidx.tracing:tracing-wire:2.0.0-alpha01")
            // ...
          }
        }
        jvmMain {
          dependencies {
            api("androidx.tracing:tracing-wire:2.0.0-alpha01")
            // ...
          }
        }
      }
    }

Declare a dependency on `androidx.tracing:tracing-wire:2.0.0-alpha01` if
you are targeting an Android library, an Android application, or if you are
targeting the JVM.

> [!NOTE]
> **Note:** The JVM dependency targets JDK 11 or later.

## Basic usage

A `TraceSink` defines how trace packets are serialized. Tracing 2.0.0 comes with
an implementation of a Sink that uses the `Perfetto` trace packet format. A
`TraceDriver` provides a handle to the `Tracer` and can be used to finalize a
trace.

You can also use the `TraceDriver` to disable all trace points in the
application, if you choose not to trace at all in some application variants.
Future APIs in the TraceDriver will also allow developers to control which trace
categories they are interested in capturing (or disabling when a category is
noisy).

To get started, create an instance of a `TraceSink` and a `TraceDriver`.

    /**
     * A [TraceSink] defines how traces are serialized.
     *
     * [androidx.tracing.wire.TraceSink] uses the `Perfetto` trace packet format.
     */
    fun createSink(): TraceSink {
        val outputDirectory = File(/* path = */ "/tmp/perfetto")
        if (!outputDirectory.exists()) {
            outputDirectory.mkdirs()
        }
        // We are using the factory function defined in androidx.tracing.wire
        return TraceSink(
            sequenceId = 1,
            directory = outputDirectory
        )
    }
    /**
     * Creates a new instance of [androidx.tracing.TraceDriver].
     */
    fun createTraceDriver(): TraceDriver {
        // We are using a factory function from androidx.tracing.wire here.
        // `isEnabled` controls whether tracing is enabled for the application.
        val driver = TraceDriver(sink = createSink(), isEnabled = true)
        return driver
    }

After you have an instance of `TraceDriver`, obtain the `Tracer` which defines
the entry point for all tracing APIs.

    // Tracing Categories identify subsystems that are responsible
    // in generating trace sections. Future APIs in `TraceDriver` will allow the
    // application to specify which categories they are interested in tracing.
    // This lets the application disable entire trace categories, without
    // needing to disable trace instrumentation at the call sites for those
    // categories.

    internal const val CATEGORY_MAIN = "main"

    fun main() {
        val driver = createTraceDriver()
        driver.use {
            driver.tracer.trace(category = CATEGORY_MAIN, name = "basic") {
                Thread.sleep(100L)
            }
        }
    }

This generates the following trace.
![Screen capture of a basic Perfetto trace](https://developer.android.com/static/topic/performance/images/in-process-tracing/basic.png)
**Figure 1.**
Screen capture of a basic Perfetto trace.

You can see that the correct process and thread tracks are populated,
and produced a single trace section `basic`, which ran for `100ms`.

Trace sections (or slices) can be nested on the same track to represent
overlapping events. Here is an example.

    fun main() {
        // Initialize the tracing infrastructure to monitor app performance
        val driver = createTraceDriver()
        val tracer = driver.tracer
        driver.use {
            tracer.trace(
                category = CATEGORY_MAIN,
                name = "processImage",
            ) {
                // Load the data first, then apply the sharpen filter
                sharpen(tracer = tracer, output = loadImage(tracer))
            }
        }
    }

    internal fun loadImage(tracer: Tracer): ByteArray {
        return tracer.trace(CATEGORY_MAIN, "loadImage") {
            // Loads an image
            // ...
            // A placeholder
            ByteArray(0)
        }
    }

    internal fun sharpen(tracer: Tracer, output: ByteArray) {
        // ...
        tracer.trace(CATEGORY_MAIN, "sharpen") {
            // ...
        }
    }

This generates the following trace.
![Screen capture of a basic Perfetto trace with nested sections](https://developer.android.com/static/topic/performance/images/in-process-tracing/basic_nested.png)
**Figure 2.**
Screen capture of a basic Perfetto trace with nested sections.

You can see that there are overlapping events in the main thread track. It is
very clear that `processImage` calls `loadImage` and `sharpen` on the same
thread.

## Add additional metadata in trace sections

Sometimes, it can be useful to attach additional contextual metadata to a trace
slice, to get more details. Some examples of such metadata could include the
`nav destination` that the user is on, or `input arguments` that might end up
determining how long a function takes.

    fun main() {
        val driver = createTraceDriver()
        driver.use {
            driver.tracer.trace(
                category = CATEGORY_MAIN,
                name = "basicWithContext",
                // Add additional metadata
                metadataBlock = {
                    // Add key value pairs.
                    addMetadataEntry("key", "value")
                    addMetadataEntry("count", 1L)
                }
            ) {
                Thread.sleep(100L)
            }
        }
    }

This produces the following result. Note the `Arguments` section contains key
value pairs added when producing the `slice`.
![Screen capture of a basic Perfetto trace with additional metadata](https://developer.android.com/static/topic/performance/images/in-process-tracing/basic_with_context.png)
**Figure 3.**
Screen capture of a basic Perfetto trace with additional metadata.

## Context propagation

When using Kotlin Coroutines (or other similar frameworks that help with
concurrent workloads) Tracing 2.0 supports the notion of context propagation.
This is best explained by an example.

    suspend fun taskOne(tracer: Tracer) {
        tracer.traceCoroutine(category = CATEGORY_MAIN, "taskOne") {
            delay(timeMillis = 100L)
        }
    }

    suspend fun taskTwo(tracer: Tracer) {
        tracer.traceCoroutine(category = CATEGORY_MAIN, "taskTwo") {
            delay(timeMillis = 50L)
        }
    }

    fun main() = runBlocking(context = Dispatchers.Default) {
        val driver = createTraceDriver()
        val tracer = driver.tracer
        driver.use {
            tracer.traceCoroutine(category = CATEGORY_MAIN, name = "main") {
                coroutineScope {
                    launch { taskOne(tracer) }
                    launch { taskTwo(tracer) }
                }
            }
            println("All done")
        }
    }

This produces the following result.
![Screen capture of a Perfetto trace with context propagation](https://developer.android.com/static/topic/performance/images/in-process-tracing/context_propagation.png)
**Figure 4.**
Screen capture of a basic Perfetto trace with context propagation.

Context Propagation makes it a lot simpler to **visualize the flow of
execution** . You can see exactly which tasks were related (connected to others),
and exactly when `Threads` were *suspended* and *resumed*.

For example, you can see that the slice `main` spawned `taskOne` and `taskTwo`.
After that both threads were inactive (given that the coroutines were
suspended - because of the use of `delay`).

> [!NOTE]
> **Note:** The `traceCoroutine` API uses `PropagationToken`s under the hood that are attached to the underlying `coroutineContext` responsible for overseeing execution. The core `Tracer` API also makes it possible to **bring your own
> implementation of context propagation** if you choose.

> [!NOTE]
> **Note:** In `alpha01` context propagation uses Perfetto flows to represent the flow of execution. This is an imperfect representation, given it presents the developer with a `Thread` centric view. The `Tracer` therefore, keeps track of **when coroutines are suspended and resumed** . This is also why you might see multiple slices that correspond to a single `suspend` function, as it suspends and resumes.

> [!NOTE]
> **Note:** We are improving how context propagation can be visualized in Perfetto UI, to better represent fan-outs for example.

## Manual propagation

Sometimes when you are mixing concurrent workloads using Kotlin coroutines with
instances of Java `Executor` it might be useful to propagate the context from
one to the other. Here is an example:

    fun executorTask(
        tracer: Tracer,
        token: PropagationToken,
        executor: Executor,
        callback: () -> Unit
    ) {
        executor.execute {
            tracer.trace(
                category = CATEGORY_MAIN,
                name = "executeTask",
                token = token,
            ) {
                // Do something
                Thread.sleep(100)
                callback()
            }
        }
    }

    @OptIn(DelicateTracingApi::class)
    fun main() = runBlocking(context = Dispatchers.Default) {
        val driver = createTraceDriver()
        val executor = Executors.newSingleThreadExecutor()
        val tracer = driver.tracer
        driver.use {
            tracer.traceCoroutine(category = CATEGORY_MAIN, name = "main") {
                coroutineScope {
                    val deferred = CompletableDeferred<Unit>()
                    executorTask(
                        tracer = tracer,
                        // Obtain the propagation token from the CoroutineContext
                        token = tracer.tokenFromCoroutineContext(),
                        executor = executor,
                        callback = {
                            deferred.complete(Unit)
                        }
                    )
                    deferred.await()
                }
            }
            executor.shutdownNow()
        }
    }

This produces the following result.
![Screen capture of a Perfetto trace with manual context propagation](https://developer.android.com/static/topic/performance/images/in-process-tracing/manual_context_propagation.png)
**Figure 5.**
Screen capture of a basic Perfetto trace with manual context propagation.

You can see that execution started in a `CoroutineContext`, and subsequently
switched to a Java `Executor`, but we were still able to use context
propagation.

> [!NOTE]
> **Note:** You can also use the `Tracer.tokenForManualPropagation()` API if you want complete control over how context propagation works. This is especially useful when your async workflow is convoluted (such as, when you chain operators on a Kotlin `Flow`).

## Combine with system traces

The new `androidx.tracing` does not capture information like CPU scheduling,
Memory usage, and the applications interaction with the operating system in
general. This is because the library provides a way to perform very **low
overhead in-process tracing**.

However, it is extremely trivial to merge system traces with in-process traces
and visualize them as a single trace if needed. This is because `Perfetto UI`
supports visualizing multiple trace files from a device on a unified timeline.

To do this, you can start a system tracing session using `Perfetto UI` by
following [instructions here](https://perfetto.dev/docs/getting-started/system-tracing#recording-your-first-system-trace).

You can also record in-process trace events using the `Tracing 2.0` API, while
system tracing is turned on. Once you have **both** trace files you can use the
`Open Multiple Trace Files` option in Perfetto.
![Opening multiple trace files in Perfetto UI](https://developer.android.com/static/topic/performance/images/in-process-tracing/multiple_trace_files.png)
**Figure 6.**
Opening multiple trace files in Perfetto UI.

> [!NOTE]
> **Note:** The reason why this just works out of the box is because the identifiers used by the in-process tracer (for `processes` and `threads`) are identical. Additionally, the `clock` used for the in-process tracing and system tracing are also in sync. Therefore these events automatically line up.

## Advanced workflows

### Correlate slices

Sometimes, it is useful to attribute slices in a trace to a more high level user
action or a system event. For example to attribute all the slices that
correspond to some background work as part of a notification, you could do
something like:

    fun main() {
        val driver = createTraceDriver()
        onEvent(driver, eventId = EVENT_ID)
    }

    fun onEvent(driver: TraceDriver, eventId: Long) {
        driver.use {
            driver.tracer.trace(
                category = CATEGORY_MAIN,
                name = "step-1",
                metadataBlock = {
                    addCorrelationId(eventId)
                }
            ) {
                Thread.sleep(100L)
            }

            Thread.sleep(20)

            driver.tracer.trace(
                category = CATEGORY_MAIN,
                name = "step-2",
                metadataBlock = {
                    addCorrelationId(eventId)
                }
            ) {
                Thread.sleep(180)
            }
        }
    }

This produces the following result.
![Screen capture of a Perfetto trace with correlated slices](https://developer.android.com/static/topic/performance/images/in-process-tracing/correlating_slices.png)
**Figure 7.**
Screen capture of a Perfetto trace with correlated slices.

> [!NOTE]
> **Note:** Note the `Arguments` section, and that Perfetto chooses a consistent color scheme for slices when they share a `correlationId`.

### Add call stack information

Host side tools (compiler plugins, annotation processors etc.) can additionally
choose to embed call stack information into a trace, to make it convenient
to locate the file, class, or method responsible for producing a trace section in
a trace.

    fun main() {
        val driver = createTraceDriver()
        driver.use {
            driver.tracer.trace(
                category = CATEGORY_MAIN,
                name = "callStackEntry",
                metadataBlock = {
                    addCallStackEntry(
                        name = "main",
                        lineNumber = 14,
                        sourceFile = "Basic.kt"
                    )
                }
            ) {
                Thread.sleep(100L)
            }
        }
    }

This produces the following result.
![Screen capture of a Perfetto trace with call stack information](https://developer.android.com/static/topic/performance/images/in-process-tracing/call_stack_entry.png)
**Figure 8.**
Screen capture of a Perfetto trace with call stack information.

> [!NOTE]
> **Note:** Note the `Arguments` section, which contains the call stack information.