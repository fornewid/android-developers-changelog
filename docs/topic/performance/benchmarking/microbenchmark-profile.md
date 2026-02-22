---
title: https://developer.android.com/topic/performance/benchmarking/microbenchmark-profile
url: https://developer.android.com/topic/performance/benchmarking/microbenchmark-profile
source: md.txt
---

By default, Microbenchmarks give you information about the timing and
allocations of the executed code. If you want to investigate why the measured
code is running slowly, inspect the method trace---captured by default on
[supported OS versions](https://developer.android.com/topic/performance/benchmarking/microbenchmark-profile#method-tracing-default-support)---or select other
profiling configurations.

To select the profiler configuration, add the instrumentation runner argument
`androidx.benchmark.profiling.mode` with one of
[`MethodTracing`](https://developer.android.com/topic/performance/benchmarking/microbenchmark-profile#method-tracing) (default),
[`StackSampling`](https://developer.android.com/topic/performance/benchmarking/microbenchmark-profile#stack-sampling), or [`None`](https://developer.android.com/topic/performance/benchmarking/microbenchmark-profile#none) argument, as shown in the
following snippet.

For more information about the options, see [Record Java/Kotlin methods](https://developer.android.com/studio/profile/record-java-kotlin-methods).
`MethodTracing` is the equivalent of tracing, and `StackSampling` is the
equivalent of sampling as defined in that document.  

### Groovy

```groovy
android {
    defaultConfig {
        // must be one of: 'None', 'StackSampling', or 'MethodTracing'
        testInstrumentationRunnerArguments["androidx.benchmark.profiling.mode"]= 'StackSampling'
    }
}
```

### Kotlin

```kotlin
android {
    defaultConfig {
        // must be one of: 'None', 'StackSampling', or 'MethodTracing'
        testInstrumentationRunnerArguments["androidx.benchmark.profiling.mode"] = "StackSampling"
    }
}
```

When you profile a benchmark, an output `.trace` file is copied to the host in
the directory [alongside JSON results](https://developer.android.com/topic/performance/benchmarking/microbenchmark-write#benchmark-results). To inspect profiling results in
Android Studio, select the **Method Trace** or **Stack Sampling Trace** link
in the microbenchmark results.
| **Note:** The Microbenchmark library automatically captures system tracing, but with custom tracing sections disabled---it ignores calls to `Trace.beginSection and endSection`---to prevent interference from tracing overhead.

## MethodTracing

Method tracing is useful when you are trying to optimize your code because it
can help you identify the methods that take longer to run than others. You can
then focus on optimizing the methods that have the most impact on performance.

Profiling occurs in sequence after code measurement, so your test outputs both
accurate timing and profiling results.

Method tracing is on by default.  
**Note:** On some Android OS and ART versions, method tracing is off by default. In these cases, Android Studio outputs a warning.

## StackSampling

Sample tracing can also help identify expensive methods without the
performance overhead of method tracing. However, if your app enters a method
after a call stack has been captured and the method exits before the next
capture, then the method call is not logged. To properly track methods with
short life cycles, use method tracing instead of sample tracing.

With stack sampling, the benchmark samples call stacks after the warmup is
complete. You can control sampling behavior such as the
[sample frequency](https://developer.android.com/topic/performance/benchmarking/microbenchmark-profile#profiling-samplefrequency)
and [duration of sampling](https://developer.android.com/topic/performance/benchmarking/microbenchmark-profile#profiling-sampleduration) using instrumentation
arguments.

On Android 10 (API 29) and higher, stack sampling uses [Simpleperf](https://developer.android.com/ndk/guides/simpleperf) to sample
app callstacks, including C++ code. On Android 9 (API 28) and lower, it uses
[`Debug.startMethodTracingSampling`](https://developer.android.com/reference/kotlin/android/os/Debug#startMethodTracingSampling(kotlin.String,%20kotlin.Int,%20kotlin.Int)) to capture stack samples.

You can configure this profiling mode by adding another instrumentation
arguments:

- `androidx.benchmark.profiling.sampleFrequency`

  - Number of stack samples to capture per second.
  - Argument type: integer
  - Defaults to 1000 samples per second.
- `androidx.benchmark.profiling.sampleDurationSeconds`

  - Duration of benchmark to run.
  - Argument type: integer
  - Defaults to 5 seconds.
- `androidx.benchmark.profiling.skipWhenDurationRisksAnr`

  - Skips method tracing when it's likely to cause an ANR. You should keep this enabled for CI runs, since ANRs can cause problems during long CI runs.
  - Argument type: boolean
  - Defaults to `true`

## None

This argument doesn't capture a profiling file. Information about timing and
allocations are still measured.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Microbenchmark Instrumentation Arguments](https://developer.android.com/topic/performance/benchmarking/microbenchmark-instrumentation-args)
- [Run benchmarks in Continuous Integration](https://developer.android.com/topic/performance/benchmarking/benchmarking-in-ci)