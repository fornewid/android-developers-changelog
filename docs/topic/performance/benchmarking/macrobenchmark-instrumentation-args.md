---
title: https://developer.android.com/topic/performance/benchmarking/macrobenchmark-instrumentation-args
url: https://developer.android.com/topic/performance/benchmarking/macrobenchmark-instrumentation-args
source: md.txt
---

# Macrobenchmark instrumentation arguments

Configure the behavior of the library with the following instrumentation arguments. You can either add these to your Gradle configuration or apply them directly when running instrumentation from the command line. To set these arguments for all Android Studio and command line test runs, add them to`testInstrumentationRunnerArguments`:  

    android {
        defaultConfig {
            // ...
            testInstrumentationRunnerArguments["androidx.benchmark.dryRunMode.enable"] = "true"
        }
    }

You can also set up instrumentation arguments when running the benchmarks from Android Studio. To change the arguments, do the following:  
1. Edit the run configuration by clicking**Edit** and then clicking the configuration.![edit run configuration](https://developer.android.com/static/topic/performance/images/benchmark_images/bench_instr_arg_1.png)**Figure 1.**Edit the run configuration.
2. Edit the instrumentation arguments by clickingmore_horiz**More** by**Instrumentation arguments** .![edit the instrumentation arguments](https://developer.android.com/static/topic/performance/images/benchmark_images/bench_instr_arg_2.png)**Figure 2.**Edit the instrumentation arguments.
3. Add the required instrumentation argument by clickingadd**Add** under**Instrumentation Extra Params** .![add required instrumentation argument](https://developer.android.com/static/topic/performance/images/benchmark_images/bench_instr_arg_3.png)**Figure 3.**Add the required instrumentation argument.

<br />

If you're running the macrobenchmark from the command line, use`-P
android.testInstrumentationRunnerArguments.[name of the argument]`:  

    ./gradlew :benchmark:connectedAndroidTest -P android.testInstrumentationRunnerArguments.androidx.benchmark.enabledRules=BaselineProfile

If you're invoking the`am instrument`command directly (which may be the case in CI testing environments), pass the argument to`am instrument`with`-e`:  

    adb shell am instrument -e androidx.benchmark.enabledRules BaselineProfile -w com.example.macrobenchmark/androidx.test.runner.AndroidJUnitRunner

For more information about configuring benchmarks in CI, see[Benchmarking in CI](https://developer.android.com/topic/performance/benchmarking/benchmarking-in-ci#install-and)

## androidx.benchmark.compilation.enabled

Lets you disable compilation between each iteration of the benchmark. By default, the target application is re-installed and re-compiled between each benchmark, to respect the[`CompilationMode`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/CompilationMode)passed into[`measureRepeated`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/junit4/MacrobenchmarkRule#measurerepeated). Disabling this lets you to skip both reinstall and compilation if, for example, you want to fully compile the target app once before running the test suite and run all benchmarks against that fully compiled target.

- **Argument type:**boolean
- **Defaults to:** `true`

## androidx.benchmark.dryRunMode.enable

Lets you run benchmarks in a single loop to verify whether they work properly. You can use it with regular tests as part of verification.

- **Argument type:**boolean
- **Defaults to:** `false`

## androidx.benchmark.enabledRules

Allows filtering runs to just one type of test: Baseline Profile generation or Macrobenchmark test. Comma-separated lists are also supported.

- **Argument type**: string
- Available options:
  - `Macrobenchmark`
  - `BaselineProfile`
- **Defaults to:**Not specified

## androidx.benchmark.fullTracing.enable

| **Note:** This argument was previously named`perfettoSdkTracing`.

Enables`androidx.tracing.perfetto`tracepoints such as Jetpack Compose composition tracing.

You need to set up your project to be able to capture composition tracing from benchmarks. For more information, see[Capture a trace with Jetpack Macrobenchmark](https://developer.android.com/jetpack/compose/tooling/tracing#macrobenchmark).

- **Argument type**: boolean
- **Defaults to** :`false`

## androidx.benchmark.killExistingPerfettoRecordings

Benchmark by default kills any existing Perfetto (System Trace) recordings when starting a new trace to reduce interference. To disable this behavior, pass`false`.

- **Argument type:**boolean
- **Defaults to:** `true`

## androidx.benchmark.profiling.mode

Allows capturing trace files while running the benchmarks. The available options are the same as those for the Microbenchmark library---for more information, see the descriptions at[Profile a Microbenchmark](https://developer.android.com/topic/performance/benchmarking/microbenchmark-profile).

- **Argument type:**string
- Available options:
  - `MethodTracing`
  - `StackSampling`
  - `None`
- **Defaults to:** `None`

## androidx.benchmark.startupProfiles.enable

Lets you disable the generation of startup profiles during benchmarking.

- **Argument type**: boolean
- **Defaults to:** `true`

## androidx.benchmark.suppressErrors

Accepts comma-separated list of errors to turn into warnings.

- **Argument type**: list of strings
- Available options:

  - `DEBUGGABLE`

    The`DEBUGGABLE`error indicates that the target package is running with`debuggable=true`in its manifest, which drastically reduces runtime performance to support debugging features. To avoid this error, run benchmarks with`debuggable=false`. The debuggable argument affects execution speed in ways that mean benchmark improvements might not carry over to a real user's experience or might regress release performance.
  - `LOW-BATTERY`

    When battery is low, devices often reduce performance to save remaining battery, for example by disabling big cores. This occurs even when the devices are plugged in. Only suppress this error if you are deliberately profiling the app with reduced performance.
  - `EMULATOR`

    The`EMULATOR`error tells you that the benchmark is running on an emulator, which isn't representative of real user devices. Emulator benchmark improvements might not carry over to a real user's experience or might regress real device performance. You should use a physical device to benchmark instead. Suppress this error with extreme caution.
  - `NOT-PROFILEABLE`

    Target package`$packageName`is running without`<profileable shell=true>`. Profileable is required on Android 10 and 11 to let Macrobenchmark capture detailed trace information from the target process, such as system tracing sections defined in the app or libraries. Suppress this error with extreme caution.
  - `METHOD-TRACING-ENABLED`

    The Macrobenchmark run for the app being benchmarked has method tracing enabled. This causes the VM to run slower than usual, so only consider the metrics from the trace files in relative terms---for example, comparing how fast the first run is to the second run. Suppressing this error can result in inaccurate results if you compare benchmarks for builds with different method tracing options.
- **Defaults to**: an empty list

## additionalTestOutputDir

Configures where JSON benchmark reports and profiling results are saved on device.

- **Argument type:**path string
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
- [Microbenchmark Instrumentation Arguments](https://developer.android.com/topic/performance/benchmarking/microbenchmark-instrumentation-args)
- [Create Baseline Profiles](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile)
- [JankStats Library](https://developer.android.com/topic/performance/jankstats)