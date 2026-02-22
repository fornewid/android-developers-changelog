---
title: https://developer.android.com/topic/performance/benchmarking/microbenchmark-instrumentation-args
url: https://developer.android.com/topic/performance/benchmarking/microbenchmark-instrumentation-args
source: md.txt
---

# Microbenchmark instrumentation arguments

Configure the behavior of Microbenchmark with the following instrumentation arguments. You can either add these to your Gradle configuration or apply them directly when running instrumentation from the command line. To set these arguments for all Android Studio and command line test runs, add them to`testInstrumentationRunnerArguments`:  

    android {
        defaultConfig {
            // ...
            testInstrumentationRunnerArguments["androidx.benchmark.dryRunMode.enable"] = "true"
        }
    }

You can also set up instrumentation arguments when running the benchmarks from Android Studio. To change the arguments, do the following:  
1. Edit the run configuration by clicking**Edit** and selecting the configuration you want to edit.![](https://developer.android.com/static/topic/performance/images/benchmark_images/bench_instr_arg_1.png)**Figure 1.**Edit the run configuration.
2. Edit instrumentation arguments by clickingmore_horiznext to the**Instrumentation arguments** field.![](https://developer.android.com/static/topic/performance/images/benchmark_images/bench_instr_arg_2.png)**Figure 2.**Edit the instrumentation argument.
3. Clickaddand add the required instrumentation argument.![](https://developer.android.com/static/topic/performance/images/benchmark_images/bench_instr_arg_3.png)**Figure 3.**Add the instrumentation argument.

<br />

If you're running the benchmark from the command line, use`-P
android.testInstrumentationRunnerArguments.[name of the argument]`:  

    ./gradlew :benchmark:connectedAndroidTest -P android.testInstrumentationRunnerArguments.androidx.benchmark.profiling.mode=StackSampling

If you're invoking am instrument command directly (which may be the case in CI testing environments), pass the argument to`am instrument`with`-e`:  

    adb shell am instrument -e androidx.benchmark.profiling.mode StackSampling -w com.example.macrobenchmark/androidx.benchmark.junit4.AndroidBenchmarkRunner

For more information about configuring benchmarks in CI, see[Benchmarking in CI](https://developer.android.com/topic/performance/benchmarking/benchmarking-in-ci#install-and)

## androidx.benchmark.cpuEventCounter.enable (experimental)

Counts the CPU events specified in`androidx.benchmark.cupEventCounter.events`. Requires root access.

- **Argument type:**boolean
- **Defaults to:**false

## androidx.benchmark.cpuEventCounter.events (experimental)

Specifies which types of CPU events to count. To use this argument`androidx.benchmark.cpuEventCounter.enable`must be set to`true`.

- **Argument type:**comma-separated list of strings
- Available options:
  - `Instructions`
  - `CPUCycles`
  - `L1DReferences`
  - `L1DMisses`
  - `BranchInstructions`
  - `BranchMisses`
  - `L1IReferences`
  - `L1IMisses`
- **Defaults to:** `Instructions`,`CpuCycles`,`BranchMisses`

## androidx.benchmark.dryRunMode.enable

Lets you run benchmarks in single loop to verify that they work properly.

This means:

- [Configuration errors](https://developer.android.com/topic/performance/benchmarking/microbenchmark-write#configuration-errors)aren't enforced (for example, to make it easier to run with regular correctness tests on emulators)
- Benchmark runs only a single loop, with no warmup
- Measurements and traces aren't captured to reduce runtime

This optimizes for test throughput and validating benchmark logic over build and measurement correctness.

- **Argument type:**boolean
- **Defaults to:** `false`

## androidx.benchmark.killExistingPerfettoRecordings

Benchmark by default kills any existing Perfetto (System Trace) recordings when starting a new trace to reduce interference. To disable this behavior, pass`false`.

- **Argument type:**boolean
- **Defaults to:** `true`

## androidx.benchmark.output.enable

Enables writing the result JSON file to external storage.

- **Argument type:**boolean
- **Defaults to:** `true`

## androidx.benchmark.profiling.mode

Allows capturing trace files while running the benchmarks. See[Profile a Microbenchmark](https://developer.android.com/studio/profile/microbenchmark-profile)for available options.

Note that some Android OS versions don't support method tracing without subsequent measurements being affected. Microbenchmark throws an exception to prevent this, so use the default argument to capture method traces only when it's safe to do so. See[Issue #316174880](https://issuetracker.google.com/issues/316174880).

- **Argument type:**string
- Available options:
  - `MethodTracing`
  - `StackSampling`
  - `None`
- **Defaults to:** Safe version of`MethodTracing`which only captures a method trace if the device can do so without affecting measurements.

## androidx.benchmark.suppressErrors

Accepts a comma-separated list of errors to turn into warnings.

- **Argument type:**list of strings
- Available options:
  - `DEBUGGABLE`
  - `LOW-BATTERY`
  - `EMULATOR`
  - `CODE-COVERAGE`
  - `UNLOCKED`
  - `SIMPLEPERF`
  - `ACTIVITY-MISSING`
- **Defaults to:**an empty list

## additionalTestOutputDir

Configures where JSON benchmark reports and profiling results are saved on device.

- **Argument type:**file path string
- **Defaults to:**test APK's external directory

## listener

You might get inconsistent benchmark results if unrelated background work gets executed while the benchmark is running.

To disable background work during benchmarking set the`listener`instrumentation argument type to`androidx.benchmark.junit4.SideEffectRunListener`.

- **Argument type:**string
- Available options:
  - `androidx.benchmark.junit4.SideEffectRunListener`
- **Defaults to:**not specified

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Macrobenchmark instrumentation arguments](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-instrumentation-args)
- [Profile a Microbenchmark](https://developer.android.com/topic/performance/benchmarking/microbenchmark-profile)
- [Create Baseline Profiles {:#creating-profile-rules}](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile)