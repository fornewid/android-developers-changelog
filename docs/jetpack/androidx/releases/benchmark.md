---
title: https://developer.android.com/jetpack/androidx/releases/benchmark
url: https://developer.android.com/jetpack/androidx/releases/benchmark
source: md.txt
---

# Benchmark

[User Guide](https://developer.android.com/topic/performance/benchmarking/benchmarking-overview) [Code Sample](https://github.com/android/performance-samples) [Codelab](https://developer.android.com/codelabs/android-macrobenchmark-inspect) API Reference  
[androidx.benchmark](https://developer.android.com/reference/kotlin/androidx/benchmark/package-summary)  
[androidx.benchmark.junit4](https://developer.android.com/reference/kotlin/androidx/benchmark/junit4/package-summary)  
[androidx.benchmark.macro](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/package-summary)  
[androidx.benchmark.macro.junit4](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/junit4/package-summary)  
Accurately measure your code's performance within Android Studio.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 11, 2026 | [1.4.1](https://developer.android.com/jetpack/androidx/releases/benchmark#1.4.1) | - | - | [1.5.0-alpha03](https://developer.android.com/jetpack/androidx/releases/benchmark#1.5.0-alpha03) |

## Declaring dependencies

To add a dependency on Benchmark, you must add the Google Maven repository to
your project. Read
[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven) for more
information.

### Macrobenchmark

To use [Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)
in your project, add the following dependencies to your `build.gradle` file for
your
[macrobenchmark module](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview#setup-macrobenchmark):

### Groovy

```groovy
dependencies {
  androidTestImplementation "androidx.benchmark:benchmark-macro-junit4:1.4.1"
}
```

### Kotlin

```kotlin
dependencies {
  androidTestImplementation("androidx.benchmark:benchmark-macro-junit4:1.4.1")
}
```

### Microbenchmark

To use [Microbenchmark](https://developer.android.com/topic/performance/benchmarking/microbenchmark-overview)
in your project, add the following dependencies to your `build.gradle` file for
your
[microbenchmark module](https://developer.android.com/topic/performance/benchmarking/microbenchmark-write#full-setup):

### Groovy

```groovy
dependencies {
    androidTestImplementation "androidx.benchmark:benchmark-junit4:1.4.1"
}

android {
    ...
    defaultConfig {
        ...
        testInstrumentationRunner "androidx.benchmark.junit4.AndroidBenchmarkRunner"
    }
}
```

### Kotlin

```kotlin
dependencies {
    androidTestImplementation("androidx.benchmark:benchmark-junit4:1.4.1")
}

android {
    ...
    defaultConfig {
        ...
        testInstrumentationRunner = "androidx.benchmark.junit4.AndroidBenchmarkRunner"
    }
}
```

The Microbenchmark library also provides a Gradle plugin to use with your microbenchmark module.
This plugin sets build configuration defaults for the module, sets up
[benchmark output copy to the host](https://developer.android.com/topic/performance/benchmarking/microbenchmark-overview),
and provides the [`./gradlew lockClocks` task](https://developer.android.com/performance/benchmarking/microbenchmark-overview#lock-clocks).

To use the plugin, include the following line in the \`plugins\` block in your top-level
`build.gradle` file:

### Groovy

```groovy
plugins {
  id 'androidx.benchmark' version '1.4.1' apply false
}
```

### Kotlin

```kotlin
plugins {
  id("androidx.benchmark") version "1.4.1" apply false
}
```

Then apply the plugin to your benchmark module's `build.gradle` file

### Groovy

```groovy
plugins {
  id 'androidx.benchmark'
}
```

### Kotlin

```kotlin
plugins {
    id("androidx.benchmark")
}
```

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:585351+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=585351&template=1235073)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.5

### Version 1.5.0-alpha03

February 11, 2026

`androidx.benchmark:benchmark-*:1.5.0-alpha03` is released. Version 1.5.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c26c6f088b95903b7b9cd5e6f2092988f1e64dc3..cdf076c6abd0f3125cb0302756fcb77fe981ab7c/benchmark).

- Updated to depend upon UiAutomator 2.4 beta.

### Version 1.5.0-alpha02

January 28, 2026

`androidx.benchmark:benchmark-*:1.5.0-alpha02` is released. Version 1.5.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ec985eed3cba8444e5aaa52a748333397a1298f3..715e22619094effc2ba1fd528cd9a07b1f5d0046/benchmark).

**Bug Fixes**

- Add partial support for baseline profile generation for Kotlin multi-platform modules. Typically dependencies on profiles can be defined using the `baselineProfile` Gradle configuration in the dependencies block, but this doesn't currently work for KMP modules.

      kotlin {
        androidLibrary {
          namespace = "com.example.namespace"
          compileSdk = 36
        }
        sourceSets {
          androidMain.dependencies {
            // THIS DOES NOT WORK
            // baselineProfile(":yourProducerProject")
          }
        }
      }

- Instead you should be defining your dependencies using the `baselineProfile` \*\*extension. ([Ie19c4](https://android-review.googlesource.com/#/q/Ie19c4535ebe25ead09e22d9a5e7654c2a5d0b627))

      plugins {
          id("org.jetbrains.kotlin.multiplatform")
          id("com.android.kotlin.multiplatform.library")
          id("androidx.baselineprofile.consumer")
      }

      kotlin {
        androidLibrary {
          namespace = "com.example.namespace"
          compileSdk = 36
        }
        sourceSets {
          androidMain.dependencies {
            // ...
          }
        }
      }
      // Define dependencies
      // This works !
      baselineProfile {
        variants {
          androidMain {
            from(project(":yourProducerProject"))
          }
        }
      }

### Version 1.5.0-alpha01

December 17, 2025

`androidx.benchmark:benchmark-*:1.5.0-alpha01` is released. Version 1.5.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/53b1ca0749c57eeb0aaab2bef8b2afaede083710..ec985eed3cba8444e5aaa52a748333397a1298f3/benchmark).

- Macrobenchmark 1.5 uses `UiAutomator` 2.4 to simplify interacting with the measured application. The [MacrobenchmarkScope](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/MacrobenchmarkScope) object now extends [UiAutomatorTestScope](https://developer.android.com/reference/kotlin/androidx/test/uiautomator/UiAutomatorTestScope), which allows you to use the modern `UiAutomator` APIs such as `onElement { ... }.click()`.
- For more information on `UiAutomator` 2.4, see [the docs](https://developer.android.com/training/testing/other-components/ui-automator).

**New Features**

- Baseline Profile Gradle Plugin no longer requires `newDsl=false` in AGP 9.0 ([Iaaac7](https://android-review.googlesource.com/#/q/Iaaac770074ef8177aec6c337a16b256467185bc9), [b/443311090](https://issuetracker.google.com/issues/443311090))
- Extend trace config to include core size (e.g. little/big) in benchmark captured system/perfetto traces. ([I8e397](https://android-review.googlesource.com/#/q/I8e39736b28b1ddd48aa5509fd71e9cecdfa1dc87), [b/457469959](https://issuetracker.google.com/issues/457469959))

**API Changes**

- (In UiAutomator) Changed `startActivity` wait to wait for new window. ([I35da6](https://android-review.googlesource.com/#/q/I35da611a69d95bdbd58830387f4fe423bbb17f84), [b/440021797](https://issuetracker.google.com/issues/440021797))
- Stabilize `BlackHole` APIs in androidx.benchmark. ([I2b67e](https://android-review.googlesource.com/#/q/I2b67e946c722511244434954a53e9b2f06b631db), [b/451749438](https://issuetracker.google.com/issues/451749438))
- Add `@JvmOverloads` for convenience constructors for `PerfettoTraceRule`. ([I1510a](https://android-review.googlesource.com/#/q/I1510a7f13a1ed0e86533ed2d8dfc9aede0ccd0c1), [b/443763207](https://issuetracker.google.com/issues/443763207))

## Version 1.4

### Version 1.4.1

September 10, 2025

`androidx.benchmark:benchmark-*:1.4.1` is released. Version 1.4.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0c118ebfe8fc41499ab4d4e18d71dd72e2126568..53b1ca0749c57eeb0aaab2bef8b2afaede083710/benchmark).

**Bug Fixes**

- Fixed `perfettoSdkTracing=true` (e.g. when tracing Compose in a microbenchmark) would kill the target process if it was already running, and a StartupMode wasn't specified. ([Ib2c1f](https://android-review.googlesource.com/#/q/Ib2c1fc5472c6ca9b0917676a3c04f877a3310d8d))

### Version 1.4.0

July 30, 2025

`androidx.benchmark:benchmark-*:1.4.0` is released. Version 1.4.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d0f745a0177b6e9fb28e2bf5e4d8f36c12de9181..0c118ebfe8fc41499ab4d4e18d71dd72e2126568/benchmark).

**Important changes since 1.3.0**

**Microbenchmark**

- Moved Gradle tasks `lockClocks` and `unlockClocks` to be on benchmark projects, instead of at the top level to respect Gradle project isolation.
- Refactored `BenchmarkRule` to be built on top of coroutines, and support better `yield()` behavior. This should significantly reduce the risk of ANRs during benchmark runs, especially long CI runs. Note: UI Benchmarks should run with [`measureRepeatedOnMainThread`](https://developer.android.com/reference/kotlin/androidx/benchmark/junit4/BenchmarkRule#(androidx.benchmark.junit4.BenchmarkRule).measureRepeatedOnMainThread(kotlin.Function1))

**Macrobenchmark**

- Added workaround on API 34+ for `CompilationMode.None()` would have inconsistent performance due to ART's verify now partly compiling apps after first launch.
- Experimental feature - Startup Insights can highlight certain common issues in a startup Macrobenchmark by passing `MacrobenchmarkRule(..., experimentalConfig = ExperimentalConfig(StartupInsightsConfig(isEnabled = true)))`.
- Added [ArtMetric](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/ArtMetric) which can be used to detect JIT Compilation, and unoptimized class loading - both useful for validating Baseline Profile optimizations.

**Baseline Profiles**

- `BaselineProfileRule` now collects profiles for multi-process apps.

**Other Changes**

- [TraceProcessor](https://developer.android.com/reference/androidx/benchmark/traceprocessor/TraceProcessor) has been pulled out into its own library (`androidx.benchmark:benchmark-traceprocessor`) so that it can be used outside of `Macrobenchmark` metrics, in other cases. It can also be run on Desktop JVM by defining your own [ServerLifecycleManager](https://developer.android.com/reference/androidx/benchmark/traceprocessor/ServerLifecycleManager).

### Version 1.4.0-rc01

June 18, 2025

`androidx.benchmark:benchmark-*:1.4.0-rc01` is released. Version 1.4.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/786176dc2284c87a0e620477608e0aca9adeff15..d0f745a0177b6e9fb28e2bf5e4d8f36c12de9181/benchmark).

**Bug Fixes**

- Added workaround for runtime images causing `CompilationMode.None()` to not measure worst case performance after first iteration. Unfortunately this workaround requires a delay of 5 seconds to intentionally corrupt the runtime image at the beginning of each macrobenchmark suite ([I4a4f1](https://android-review.googlesource.com/#/q/I4a4f16ef87282a3e5a183b6f5517f74bcec25a1e)).

### Version 1.4.0-beta02

June 4, 2025

`androidx.benchmark:benchmark-*:1.4.0-beta02` is released. Version 1.4.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/44ffa166a34fac89733f1cfb97ccd5b40b7d6d3d..786176dc2284c87a0e620477608e0aca9adeff15/benchmark).

**API Changes**

- Added a `BaselineProfileConfig.Builder` to make it easier to call `BaselineProfileRule.collectWithResults()` for Java developers. ([I94905](https://android-review.googlesource.com/#/q/I9490595dee3820ef8a3d003a6ef8a146d8f1635a))

### Version 1.4.0-beta01

May 7, 2025

`androidx.benchmark:benchmark-*:1.4.0-beta01` is released. Version 1.4.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c37298a97c16270c139eb812ddadaba03e23a52..44ffa166a34fac89733f1cfb97ccd5b40b7d6d3d/benchmark).

**API Changes**

- Added `PerfettoTraceRule` constructor variant which accepts a `PerfettoConfig` ([Ie53ba](https://android-review.googlesource.com/#/q/Ie53ba110e14ca0c744e29a489e9c683c2b5760d7))

**Bug Fixes**

- Updated `TraceProcessor` startup insight link format to use correct plugin, and clearer delimeter (`:` is shorter than `%3A`, and both are supported) ([Ie18ef](https://android-review.googlesource.com/#/q/Ie18ef0ea0c5df471b7421f86a702496605d66b31))
- Always use force-stop to kill processes, even when rooted and killing system apps. Fixes exceptions of the form: `Expected no stdout/stderr from killall ... No such process`. ([Idca2c](https://android-review.googlesource.com/#/q/Idca2cd6967fde8c24390e572459aa168bf396b24))

**External Contribution**

- Added proxy exception handler for `TraceProcessorHttpServer` ([I480f5](https://android-review.googlesource.com/#/q/I480f5d089d256e2895e8dda2bfd138aff1b54255))

### Version 1.4.0-alpha11

April 9, 2025

`androidx.benchmark:benchmark-*:1.4.0-alpha11` is released. Version 1.4.0-alpha11 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/78132378b67c86698d1ade3dc368c9f15d738a71..4c37298a97c16270c139eb812ddadaba03e23a52/benchmark).

**API Changes**

- Changed `TraceProcessor`'s argument timeout: Duration to timeoutMs long for Java caller usability. ([I9fbb5](https://android-review.googlesource.com/#/q/I9fbb54a6430f0f8cd020a06bc8d1fd6475553e0a))
- Mark `TraceProcessor` constructor as internal. Callers should use `TraceProcessor.startServer` or `TraceProcessor.runServer`. ([Ia8c5b](https://android-review.googlesource.com/#/q/Ia8c5b53db7075253ccaec6f2869b89c3a95da98f))

**Bug Fixes**

- When killing the application with `MacrobenchmarkScope.killProcess`, validate the kill command results to prevent silent failure, and timeout error. ([I84555](https://android-review.googlesource.com/#/q/I845559d616e821ff48d58cc81498f13d7160e491))

**Dependency Updates**

- This library now targets Kotlin 2.0 language level and requires KGP 2.0.0 or newer. ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))

### Version 1.4.0-alpha10

March 26, 2025

`androidx.benchmark:benchmark-*:1.4.0-alpha10` is released. Version 1.4.0-alpha10 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c4e614557adf2d01e2d5661255e947d10a6fcfad..78132378b67c86698d1ade3dc368c9f15d738a71/benchmark).

**API Changes**

- Increased default timeout for `TraceProcessor` server load and querying to 120 seconds (from 60/30 previously), and made both configurable with one timeout parameter. ([Ifec87](https://android-review.googlesource.com/#/q/Ifec871e8ef946d3ff6b56fe8c7779f14548cf391))

**Bug Fixes**

- Fixed a few issues that would occur when benchmarking or capturing profiles of an app without `profileinstaller`, and it's included `BroadcastReciever`. This only affects runs on rooted devices. ([Ied308](https://android-review.googlesource.com/#/q/Ied308f69870b290f5947a46540b5cfae31aadabf))

### Version 1.4.0-alpha09

March 12, 2025

`androidx.benchmark:benchmark-*:1.4.0-alpha09` is released. Version 1.4.0-alpha09 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f5b23e167495c326c77bb21a1cdada0298ed5599..c4e614557adf2d01e2d5661255e947d10a6fcfad/benchmark).

**API Changes**

- Added `TraceProcessor` and Session API with closable Handles, for easier usage with custom lifecycles. This is also a step towards enabling easier Coroutine and Java API usage. The extension functions to `TraceProcessor.runServer {}` are now marked experimental, as they're likely to move, and be made non-experimental in the future. ([I358b4](https://android-review.googlesource.com/#/q/I358b4256110d2b0c4b35bb9f0be4ae2f407f0791))

**Bug Fixes**

- Fixed Benchmark and Baseline Profile capture not working with API 36 due to a change in `pgrep` toybox that now requires `-a` to print the full command line. ([Idc991](https://android-review.googlesource.com/#/q/Idc991b87153516d5412d1086a74ba55463946b9d))
- Filter default tracing config to reduce risk of data loss in traces on newer API levels. ([I54e8a](https://android-review.googlesource.com/#/q/I54e8a0b3894bc4f209a772933e51fc36233ffcd3))
- Added experimental `androidx.benchmark.killExistingPerfettoRecordings` instrumentation argument, which can be set to `false` to allow pre existing perfetto trace capture to continue. By default pre existing perfetto trace captures on device are killed to prevent interference. ([I02a3c](https://android-review.googlesource.com/#/q/I02a3c2ec686669715ebc6fb01f00555abde3401a))
- The JSON field `context.osCodenameAbbreviated` will now be `REL` for released OS versions at and above API 35, as non-numeric code names are no longer supported by the underlying platform. ([Ib17fd](https://android-review.googlesource.com/#/q/Ib17fda257618b373446bb87f7eb3d871e516d8f0))
- Fixes crash in `FrameTimingMetric` when resynced frames occur. ([I7c6f4](https://android-review.googlesource.com/#/q/I7c6f414e263eca6b6085b76e8801f64fa50586f0), [b/394610806](https://issuetracker.google.com/issues/394610806))
- No longer assume `Choreographer#doFrame` is the top of the stack frame on the main thread for `FrameTimingQuery`. ([Iee0e0](https://android-review.googlesource.com/#/q/Iee0e0bec02e2af6f675b48384d14a59569b3dc57), [b/340206285](https://issuetracker.google.com/issues/340206285))

### Version 1.4.0-alpha08

February 12, 2025

`androidx.benchmark:benchmark-*:1.4.0-alpha08` is released. Version 1.4.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c47131cd5b50c3091fc0874eb606aaac5b168fa..f5b23e167495c326c77bb21a1cdada0298ed5599/benchmark).

**API Changes**

- Moved `TraceProcessor.runSession()` extension APIs to be experimental, as they are likely to move to be concrete constructors eventually on Android. ([Ib0528](https://android-review.googlesource.com/#/q/Ib05284ba1b7250386a1993ae2e7a122b2b9c28d6), [b/393640753](https://issuetracker.google.com/issues/393640753))
- Most of the implementation of Startup Insights are now public/experimental, and move to the `TraceProcessor` artifact See `StartupInsights`. ([I0aa00](https://android-review.googlesource.com/#/q/I0aa00936ef8919aa2712958a7ea755f3d915ee99))
- Deprecate `BenchmarkRule.runWithTimingDisabled {}` in favor of `BenchmarkRule.runWithMeasurementDisabled {}`, which more clearly describes the behavior - all metrics are paused. Additionally, expose the `MicrobenchmarkScope` superclass since redeclaring the `runWithMeasurementDisabled` function to open access isn't possible, since it's inline. ([I9e23b](https://android-review.googlesource.com/#/q/I9e23b0dfcff18f162ca0d2517734f3038870b59c), [b/389149423](https://issuetracker.google.com/issues/389149423), [b/149979716](https://issuetracker.google.com/issues/149979716))
- Benchmark libraries have moved to Kotlin 2.0. ([I9d1e0](https://android-review.googlesource.com/#/q/I9d1e09ba06d9966236338b59cfdc86fc2971956f))
- Removed `androidx.benchmark.startupProfiles.enable` instrumentation argument. It is no longer useful, as it can be controlled by `includeInStartupProfile` arg in `BaselineProfileRule.collect()`. ([I39eb4](https://android-review.googlesource.com/#/q/I39eb4a83d5d64a9dae4dcdc6db0ac8fc6e5f4121))

**Bug Fixes**

- Reduced the amount of Microbenchmark internal functions called during profiling to make e.g. Method traces more clear ([Ifaed8](https://android-review.googlesource.com/#/q/Ifaed8548554016a97280546473e38ed020ae0760))
- Speculative fix for crashes: 'Failed to stop \[`ProcessPid(processName=perfetto, pid=...)`\]'. Now Benchmark will log a message instead of crashing when a background Perfetto process isn't able to be stopped before running the benchmark. ([I37d3e](https://android-review.googlesource.com/#/q/I37d3e254f7f3e49c53387dae89bb5bed7d2c9bf5), [b/323601788](https://issuetracker.google.com/issues/323601788))
- Fix `IllegalStateExceptions` with 'Expected `pm dump-profiles` stdout' label that were caused by overly strict output format check. ([I358dc](https://android-review.googlesource.com/#/q/I358dcbf377999586cea08254232f6b7850aec7bd))

### Version 1.4.0-alpha07

January 29, 2025

`androidx.benchmark:benchmark-*:1.4.0-alpha07` is released. Version 1.4.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c47131cd5b50c3091fc0874eb606aaac5b168fa/benchmark).

**New Features**

- `BaselineProfileRule` now introduces a `collectWithResults(...)` API which includes a list of paths to the computed profiles. ([I056f8](https://android-review.googlesource.com/#/q/I056f8d0e0c339398b6bd6cc4dde922aa5178a475))
- Added `androidx.benchmark.measureRepeatedOnMainThread.throwOnDeadline` instrumentation argument, which can be set to false to disable the throw on deadline behavior of `measureRepeatedOnMainThread` for local testing. Not otherwise recommended, as this increases the likelihood of ANRs during tests. ([Idbeec](https://android-review.googlesource.com/#/q/Idbeecc1394b11395946d6e2bdf4187940a1099a0), [b/353226476](https://issuetracker.google.com/issues/353226476))

**API Changes**

- Added `@JvmOverloads` to `MicrobenchmarkConfig` constructor. ([I13fd3](https://android-review.googlesource.com/#/q/I13fd37e4c79e3c1262592712edb465f518c2440e))
- Refactored `BenchmarkRule` to be built on top of coroutines, and support better `yield()` behavior. This refactor removed several experimental `BenchmarkState` APIs, but will be followed by replacements as needed. Additionally, added `runWithMeasurementDisabled` to clarify behavior (all measurement is paused). In the future, `runWithTimingDisabled` will be deprecated. ([I19837](https://android-review.googlesource.com/#/q/I19837fc604b9e308957fc01ed009c0e921b8fe28), [b/389149423](https://issuetracker.google.com/issues/389149423), [b/311242861](https://issuetracker.google.com/issues/311242861))
- Move `PerfettoTraceProcessor` to `TraceProcessor` in a new `androidx.benchmark:benchmark-traceprocessor` artifact, and make most of its API non-experimental. Any custom `TraceMetric` or anything reading from traces will need to update to the new `TraceProcessor` import. The new `TraceProcessor` API works exactly like the old one, but is a standalone interface library (somewhat analogous to the `androidx.sqlite` layer from Room) with an Android-specific implementation built into macrobenchmark. The new artifact can be used on JVM as well, but currently you'll need to start your own copy of the `TraceProcessor` binary and offer a port to connect to it on. ([I3a767](https://android-review.googlesource.com/#/q/I3a7675f25f4425745b6f255dcd1a0cec81a068ba), [I62563](https://android-review.googlesource.com/#/q/I6256342f25d3f00ef864cf14b75a7159c6a40573), [b/381134564](https://issuetracker.google.com/issues/381134564))

**Bug Fixes**

- Throw a clearer error message when `MacrobenchmarkScope.startActivityAndWait` fails to launch the target process (potentially due to a crash in the target process), instead of the more ambiguous 'Unable to confirm activity launch completion' message ([I3539b](https://android-review.googlesource.com/#/q/I3539b64f0ca064f6771bdbd8a92d374407e4a1d7))
- Fixed several syntax errors in Kotlin samples, and syntax highlighting in several Java / build.gradle samples. ([Ib3808](https://android-review.googlesource.com/#/q/Ib38080138d6eec79635262dd0713764c6468521a))
- Clarified `ArtMetric` and `CaptureInfo` parameter docs. ([I96e60](https://android-review.googlesource.com/#/q/I96e60d9c17bef4a4663b4318c52aa5a005f27de4))

### Version 1.4.0-alpha06

December 11, 2024

`androidx.benchmark:benchmark-*:1.4.0-alpha06` is released. Version 1.4.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6f09cf2ae979e48fdb19485f757a033e4a34bb82..46295bc0b75a16f452e8e0090e8de41073d4dbb6/benchmark).

**API Changes**

- Removed usage of `@Language("sql")` in `PerfettoTraceProcessor.Session.query()`, as Studio highlighting/parsing is broken. ([Idc2fa](https://android-review.googlesource.com/#/q/Idc2fa4a86e2fb4637c2a6de84f7d5320f3677a6a), [b/377733398](https://issuetracker.google.com/issues/377733398))

**Bug Fixes**

- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage: `-Xjspecify-annotations=strict` (this is the default starting with version 2.1.0 of the Kotlin compiler). ([I46810](https://android-review.googlesource.com/#/q/I468104b1daa61c3998c5558fed2b2804f0ef85e9), [b/326456246](https://issuetracker.google.com/issues/326456246))
- Corrected `ArtMetric` to report class load (not init), and improved docs to clarify runtime behavior. ([I9915c](https://android-review.googlesource.com/#/q/I9915cf126210f6d886cde0cdd05a731f7c2723a9))
- On Android Multiuser, execute commands as root only on rooted devices. ([I88b44](https://android-review.googlesource.com/#/q/I88b443366249e2d9c208b8895a4e89cb6839f997))

### Version 1.4.0-alpha05

November 13, 2024

`androidx.benchmark:benchmark-*:1.4.0-alpha05` is released. Version 1.4.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ccd90a76bd7c4acf4f4f01eca76350e383bc441e..6f09cf2ae979e48fdb19485f757a033e4a34bb82/benchmark).

**Bug Fixes**

- Fixed an issue on API 34+ where `CompilationMode.None()` would have inconsistent performance not representative of initial, worst case performance. This works around a platform change which allows ART's compilation state `verify` to partially compile apps (only affecting class loading) shortly after first launch. ([Ie48d0](https://android-review.googlesource.com/#/q/Ie48d043455681ea44a012c808a2d307b5becb93b))
- Fixed issue where (especially short) traces could be captured that wouldn't report measurement from built-in Macrobenchmark Metrics, due to the process name being truncated within the Perfetto trace. Now macrobenchmark works around this issue by looking for the truncated package name in all built-in queries, in addition to the expected package name. Note that custom `TraceMetric` implementations or other direct callers of `PerfettoSession.query` can implement this same behavior by changing `process.name LIKE "$packageName"` in a Perfetto query to instead be `(process.name LIKE "$packageName" OR process.name LIKE "$(packageName.takeLast(15))")`. ([I5bf01](https://android-review.googlesource.com/#/q/I5bf01b5a9378f3314a1d5a7e4d7968b444cefe89), [b/377565760](https://issuetracker.google.com/issues/377565760))

### Version 1.4.0-alpha04

October 30, 2024

`androidx.benchmark:benchmark-*:1.4.0-alpha04` is released. Version 1.4.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7..ccd90a76bd7c4acf4f4f01eca76350e383bc441e/benchmark).

**New Features**

- (Experimental) Enable Baseline Profile generation, and benchmarking on apps installed to a secondary user, for example any app on headless Android Auto devices. This support has been tested in some scenarios, but let us know with a bug if it doesn't work for you. ([I9fcbe](https://android-review.googlesource.com/#/q/I9fcbecf2a9c9075d161de69118c443d7a37102c0), [b/356684617](https://issuetracker.google.com/issues/356684617), [b/373641155](https://issuetracker.google.com/issues/373641155))

**Bug Fixes**

- `isProfileable` is now always overridden in benchmark builds, and `isDebuggable` is also now always overridden in both benchmark and `nonMinified` (baseline profile capture) builds. ([I487fa](https://android-review.googlesource.com/#/q/I487fa71083921682173f04fcbb477be5baf165f8), [b/369213505](https://issuetracker.google.com/issues/369213505))
- Fixes compilation detection on some physical devices prior to API 28 - affects json `context.compilationMode`, as well as behavior of `androidx.benchmark.requireAot=true` (which no longer incorrectly throws) ([Ic3e08](https://android-review.googlesource.com/#/q/Ic3e0899e6ea3558d9662788aecd7f8742fd2dee1), [b/374362482](https://issuetracker.google.com/issues/374362482))
- In `CpuEventCounter` metrics, throw if invalid measurements are observed (e.g. instructions/cpucycles==0) ([I8c503](https://android-review.googlesource.com/#/q/I8c5034be932bd09b6d3292015806d8721d292df2))

### Version 1.4.0-alpha03

October 16, 2024

`androidx.benchmark:benchmark-*:1.4.0-alpha03` is released. Version 1.4.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6..b8a68b0896897fa158508d73a31998a26161d9a7/benchmark).

**API Changes**

- **Macrobenchmark** : Adds `ArtMetric`, which can be used to inspect profile coverage or general Android RunTime performance. Captures number and total duration of JIT, class init (where available), and class verification. Additionally, changes `CaptureInfo` to include optional ART mainline version with default. ([I930f7](https://android-review.googlesource.com/#/q/I930f757630862010bcedad124248e995e1540681))
- Add `coefficientOfVariation` to Benchmark JSON output to show stability within a given benchmark run. ([Ib14ea](https://android-review.googlesource.com/#/q/Ib14ea1430ed691e130c3b5e50a4b411c46dd2f4e))

**Bug Fixes**

- Fixed `CollectBaselineProfileTask` when AVD device has spaces in it. ([Ia0225](https://android-review.googlesource.com/#/q/Ia0225358081e895d1be20582f97130fad2f06c84), [b/371642809](https://issuetracker.google.com/issues/371642809))
- Speculative fix for errors from `StartupMode.COLD` exceptions: `Package <packagename> must not be running prior to cold start!`. Now, `MacrobenchmarkScope.killProcess()` (including the one run before each iteration, used to implement `StartupMode.COLD` behavior) will wait to verify that the app's processes have all stopped running. ([I60aa6](https://android-review.googlesource.com/#/q/I60aa6669366286e7275c2debcda7221c78165659), [b/351582215](https://issuetracker.google.com/issues/351582215))
- Fixed issue where UNLOCKED_ error would show up on some rooted emulators. ([Ic5117](https://android-review.googlesource.com/#/q/Ic511753fd82a39f7a2abc87100730e4b1148a661))
- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage: `-Xjspecify-annotations=strict` (this is the default starting with version 2.1.0 of the Kotlin compiler). ([I7104f](https://android-review.googlesource.com/#/q/I7104f0ca68a72a7e996b79f1609cde685e6c61e6), [b/326456246](https://issuetracker.google.com/issues/326456246))

### Version 1.4.0-alpha02

October 2, 2024

`androidx.benchmark:benchmark-*:1.4.0-alpha02` is released. Version 1.4.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ae6231161ff1106af46ae79c4a49f16376287132..b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6/benchmark).

**API Changes**

- Moved Gradle tasks `lockClocks` and `unlockClocks` to be on benchmark projects, instead of available at the top level. This change was necessary as there is unfortunately no way to register these as top level actions without breaking project isolation. ([I02b8f](https://android-review.googlesource.com/#/q/I02b8fdfdf2f67127534f349a9e64aaa9a78b66e5), [b/363325823](https://issuetracker.google.com/issues/363325823))

**Bug Fixes**

- `BaselineProfileRule` now collects profiles for multi-process apps by signaling each running process at the end of the block to dump profiles. If a profile based compilation never successfully finds a process to broadcast to, the compilation will fail, as it's unexpected to have profile data within. Additionally, added an instrumentation argument to control dump wait duration: `androidx.benchmark.saveProfileWaitMillis` ([I0f519](https://android-review.googlesource.com/#/q/I0f51962266d3771ef72fad1a8c368316d8650694), [b/366231469](https://issuetracker.google.com/issues/366231469))
- [From Benchmark `1.3.2`](https://developer.android.com/jetpack/androidx/releases/benchmark#1.3.2): Fixed Firebase Test Lab (FTL) being unable to pull Baseline Profile or Macrobenchmark result files from the Baseline Profile Gradle Plugin. ([I2f678](https://android-review.googlesource.com/#/q/I2f6789d81a32d04df976437c2be426cbe04488ac), [b/285187547](https://issuetracker.google.com/issues/285187547))

To use FTL apply the plugin to the baseline profile module in the plugin block, with:

      plugins {
          ...
          id("com.google.firebase.testlab")
      }

and then configure firebase test lab with:

      firebaseTestLab {

          // Credentials for FTL service
          serviceAccountCredentials.set(file("credentials.json"))

          // Creates one or more managed devices to run the tests on.
          managedDevices {
              "ftlDeviceShiba34" {
                  device = "shiba"
                  apiLevel = 34
              }
          }

          // Ensures the baseline profile is pulled from the device.
          // Note that this will be automated as well later with aosp/3272935.
          testOptions {
              results {
                  directoriesToPull.addAll("/storage/emulated/0/Android/media/${android.namespace}")
              }
          }
      }

Also the created FTL device needs to be added to the baseline profile extension:

      baselineProfile {
          managedDevices += "ftlDeviceShiba34"
          useConnectedDevices = false
      }

### Version 1.4.0-alpha01

September 18, 2024

`androidx.benchmark:benchmark-*:1.4.0-alpha01` is released. Version 1.4.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ae6231161ff1106af46ae79c4a49f16376287132/benchmark).

**New Feature - App Startup Insights**

- Initial version of app startup insights can be enabled in Macrobenchmark. ([09fae38](https://android.googlesource.com/platform/frameworks/support/+/09fae383d2acafcbf326a5e5e9dbb1fba0ba163c))

To enable in a startup benchmark:

      @Test
      fun startup {
          macrobenchmarkRule.measureRepeated(
              ...
              packageName = "com.example.my.application.id"
              metrics = listOf(StartupTimingMetric()),
              iterations = 5,
              startupMode = StartupMode.COLD,
              compilationMode = CompilationMode.None(),
              experimentalConfig = ExperimentalConfig(startupInsightsConfig = StartupInsightsConfig(isEnabled = true))
              ) {
              scope.startActivityAndWait(...)
          }
      }

Then running your startup benchmark will analyze the trace to look for common problems, and print them after metrics to Studio test output in the benchmark tab, e.g.:

    StartupBenchmark_startup[startup=COLD,compilationMode=None]
    ├── Metrics
    │   ├──   timeToFullDisplayMs                min  1,147.2,   median  1,208.8,   max  1,307.4
    │   └──   timeToInitialDisplayMs             min  1,147.2,   median  1,208.8,   max  1,307.4
    ├── App Startup Insights
    │   ├── App in debuggable mode (expected: false)
    │   │   └── seen in iterations: 0(true) 1(true) 2(true) 3(true) 4(true) 5(true) 6(true) 7(true) 8(true) 9(true)
    │   ├── Potential CPU contention with another process (expected: < 100000000ns)
    │   │   └── seen in iterations: 4(105022546ns)
    │   └── Main Thread - Binder transactions blocked (expected: false)
    │       └── seen in iterations: 7(true)
    └── Traces
        └── Iteration 0 1 2 3 4 5 6 7 8 9

This feature is still a work-in-progress, with improvements to documentation and extensibility to follow, but feedback is welcome.

**New Features**

- Added gradle property `androidx.baselineprofile.suppressWarnings` to suppress all baseline profile warnings. ([314153a](https://android.googlesource.com/platform/frameworks/support/+/314153ac0c604e8b7bde1cf191c1dda920416717))
- Microbench metrics are now displayed in Perfetto traces as counters. ([3214854](https://android.googlesource.com/platform/frameworks/support/+/3214854e6ee4cebe4b6776a6f8d02df6addb6bd2))
- Add experimental scripts for disabling jit (requires root / runtime restart), and resetting device perf/test state. These are not currently published as gradle tasks. ([7c3732b](https://android.googlesource.com/platform/frameworks/support/+/7c3732b4f6ac3ac6a2aac93621b0b7fbbefd1202))
- Added benchmark argument to skip tests when running on emulator. When `automaticGenerationDuring` build is enabled, benchmarks will also trigger baseline profile generation. This will fail, if emulators are used. With the new argument `skipBenchmarksOnEmulator` we can instead skip the test. ([0c2ddcd](https://android.googlesource.com/platform/frameworks/support/+/0c2ddcd70f6090ccc660e49c03048e1de85c2073))
- Change perf event enable logic to run on API 23+ ([2550048](https://android.googlesource.com/platform/frameworks/support/+/2550048909d02279f8a0e759e7c21dabab35f93a))

**API Changes**

- Existing experimental `PerfettoConfig` argument to `MacrobenchmarkRule.measureRepeated()` moved to the new `ExperimentalConfig` object.

**Bug Fixes**

- Increase `lockClocks.sh` retry count ([99e9dac](https://android.googlesource.com/platform/frameworks/support/+/99e9dac2528133a2f7a9bbcf0fb55bac35c95483))
- Don't create `nonMinified` and benchmark build types if existing. Due to a bug, even if `nonMinified` and benchmark build types existed, they were going to be recreated. ([e75f0a5](https://android.googlesource.com/platform/frameworks/support/+/e75f0a518d11e27d4862ef903a9b29e64c0d6625))
- Ignore non-terminating slices from `TraceSectionMetric` results. ([a927d20](https://android.googlesource.com/platform/frameworks/support/+/a927d2035c0c4eed2b3a2484164f9f48a0393445))
- Improved emulator check to consider `sdk_` prefix. ([1587de8](https://android.googlesource.com/platform/frameworks/support/+/1587de845dc66a5dd7a2fc016f4653d6691a6bf2))
- Treat non-running packages as cleared in `FrameTimingGfxInfoMetric`. ([35cc79c](https://android.googlesource.com/platform/frameworks/support/+/35cc79ca5e14ac6f05772b1ec29de94d214b847e))
- Fix `androidx.benchmark.cpuEventCounter` producing corrupt values for non-Instruction events. ([06edd59](https://android.googlesource.com/platform/frameworks/support/+/06edd596b9ced3114159059ba176c7ec173fc51d))
- Fix `resumeTiming/runWithTimingDisabled` to respect metric priority order, and significantly reduce impact of lower priority metric pause/resume on higher priority metric results. For example, if using cpu perf counters via `cpuEventCounter.enable` instrumentation argument, timeNs is no longer significantly reduced when pause/resume occur. ([5de0968](https://android.googlesource.com/platform/frameworks/support/+/5de09686debf78730da51df37c78f91e77d3dbc5))

## Version 1.3

### Version 1.3.4

March 26, 2025

`androidx.benchmark:benchmark-*:1.3.4` is released. Version 1.3.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/250f8dcbcecb3ce22668b2fdb4500653e9292fc5..1efd7dc7fcf9f1c9f2e48376e12bfe1691292c10/benchmark).

**Bug Fixes**

- Fixed Gradle Project Isolation incompatibilities in the Benchmark Baseline Gradle Plugin. ([b/404523257](https://issuetracker.google.com/issues/404523257))

### Version 1.3.3

October 16, 2024

`androidx.benchmark:benchmark-*:1.3.3` is released. Version 1.3.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ee1918bf61abcf745cedcdbbb6ebbdf1808da586..250f8dcbcecb3ce22668b2fdb4500653e9292fc5/benchmark).

**Bug Fixes**

- Fixed `CollectBaselineProfileTask` when AVD device has spaces in it ([Ia0225](https://android-review.googlesource.com/#/q/Ia0225358081e895d1be20582f97130fad2f06c84), [b/371642809](https://issuetracker.google.com/issues/371642809))

### Version 1.3.2

October 2, 2024

`androidx.benchmark:benchmark-*:1.3.2` is released. Version 1.3.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8b90fce166a020c62a93085f5f104552517472c5..ee1918bf61abcf745cedcdbbb6ebbdf1808da586/benchmark).

**Bug Fixes**

- Fixed Firebase Test Lab (FTL) being unable to pull Baseline Profile or Macrobenchmark result files from the Baseline Profile Gradle Plugin. ([I2f678](https://android-review.googlesource.com/#/q/I2f6789d81a32d04df976437c2be426cbe04488ac), [b/285187547](https://issuetracker.google.com/issues/285187547))

To use FTL apply the plugin to the baseline profile module in the plugin block, with:

      plugins {
          ...
          id("com.google.firebase.testlab")
      }

and then configure firebase test lab with:

      firebaseTestLab {

          // Credentials for FTL service
          serviceAccountCredentials.set(file("credentials.json"))

          // Creates one or more managed devices to run the tests on.
          managedDevices {
              "ftlDeviceShiba34" {
                  device = "shiba"
                  apiLevel = 34
              }
          }

          // Ensures the baseline profile is pulled from the device.
          // Note that this will be automated as well later with aosp/3272935.
          testOptions {
              results {
                  directoriesToPull.addAll("/storage/emulated/0/Android/media/${android.namespace}")
              }
          }
      }

Also the created FTL device needs to be added to the baseline profile extension:

      baselineProfile {
          managedDevices += "ftlDeviceShiba34"
          useConnectedDevices = false
      }

### Version 1.3.1

September 18, 2024

`androidx.benchmark:benchmark-*:1.3.1` is released. Version 1.3.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/392c9f0664b76c0f1bc8ff14f591f1d7d65a4476..8b90fce166a020c62a93085f5f104552517472c5/benchmark).

**Bug Fixes**

- Added gradle property `androidx.baselineprofile.suppressWarnings` to suppress all baseline profile warnings ([I7c36e](https://android-review.googlesource.com/#/q/I7c36e3a0da43aa113394404215725b9c86b46cd5), [b/349646646](https://issuetracker.google.com/issues/349646646))
- Fixed Baseline Profile Gradle Plugin to use pre-existing `nonMinified...` and `benchmark...` if created by the app instead of creating wrappers. ([Ia8934](https://android-review.googlesource.com/#/q/Ia8934fdf3ff51d993f4fef8195821d72315026e2), [b/361370179](https://issuetracker.google.com/issues/361370179))
- Fixed `java.lang.AssertionError: ERRORS (not suppressed): EMULATOR` when `automaticGenerationDuringBuild` is enabled on emulators. New argument is used to instead skip the test. ([If3f51](https://android-review.googlesource.com/#/q/If3f51413074ac8b29bb42740038d285121430b50), [b/355515798](https://issuetracker.google.com/issues/355515798))
- Microbenchmark minification - keep subclasses of `org.junit.runner.notification.RunListener` in benchmark library proguard ([Ic8ed5](https://android-review.googlesource.com/#/q/Ic8ed5d229c53d4f7779429e003331c251a5f1b39), [b/354264743](https://issuetracker.google.com/issues/354264743))
- Fix `TraceSectionMetric` to Ignore non-terminating slices. Previously these were considered to have -1 duration, e.g. during summation or finding minimum duration. ([If74b7](https://android-review.googlesource.com/#/q/If74b7a13a054c5a39b2f397e2c54f715abf7e3d3))
- Fixed an issue in `FrameTimingGfxInfoMetric` where starting the metric would crash if the process wasn't already running. ([I6e412](https://android-review.googlesource.com/#/q/I6e4126f2b3be7fdea22811141a68299c41296abe))

### Version 1.3.0

August 21, 2024

`androidx.benchmark:benchmark-*:1.3.0` is released. Version 1.3.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/2f785440e93a6465ac53828357b5f71f0ad28329..392c9f0664b76c0f1bc8ff14f591f1d7d65a4476/benchmark).

**Microbenchmark changes since 1.2.0**

- Method tracing is on by default in microbenchmarks when running on most devices
  - Method tracing runs as a separate phase, after measurements - this enables accurate measurements and method traces to both be output from a single benchmark run
  - Method tracing on some Android OS and ART versions will affect later measurement phases - on these versions, method tracing is off by default and a warning is printed to Studio output
- Main thread benchmarks and ANRs
  - Added `measureRepeatedOnMainThread` for UI thread benchmarks (e.g. those that interact with Compose/View UIs) to avoid ANRs when running for many seconds.
  - Method traces are skipped if expected to overrun the ANR avoidance deadline. Set `androidx.benchmark.profiling.skipWhenDurationRisksAnr` to false to disable this behavior (not recommended for CI runs, as ANRs can cause problem in long CI runs).
- Minification
  - Embedded proguard rules to improve microbenchmarking with minification enabled
  - Minification/R8 in a library module requires AGP 8.3, and can be enabled via `android.buildTypes.release.androidTest.enableMinification` in your `build.gradle`
  - Experimental `BlackHole.consume()` API added to prevent dead code elimination ([If6812](https://android-review.googlesource.com/c/platform/frameworks/support/+/3084471), [b/286091643](https://issuetracker.google.com/issues/286091643))
- Metrics
  - Experimental cpu event counter feature (metrics from `perf_event_open`, which requires root on most versions of the platform), access via `InstrumentationArgument` `androidx.benchmark.cpuEventCounter.enable` (can be set to `true`), and `androidx.benchmark.cpuEventCounter.events` can be set e.g. to (`Instructions,CpuCycles`). This should be supported on some userdebug emulators, but support has not been tested across all available emulators

**MACRObenchmark changes since 1.2.0**

- Method tracing overhaul for macrobenchmarks.
  - Now method traces are scoped to the duration of the `measureBlock`, and can capture multiple sessions if the process starts multiple times.
  - Previously, method tracing would only work for `StartupMode.COLD` benchmarks, and capture nothing for `measureBlocks` that didn't restart the target process
  - Fixed method traces flush in macrobenchmark, so that method traces should be fully captured and valid, even on slower devices. ([I6349a](https://android-review.googlesource.com/#/q/I6349a48dca4116ac9b481882395ee630785f6181), [b/329904950](https://issuetracker.google.com/issues/329904950))
- Correctly dump ART profile during individual `warmUp` iterations when process is killed so `CompilationMode.Partial(warmup=N)` measurements are more accurate. ([I17923](https://android-review.googlesource.com/#/q/I17923a8bc7d37fa8472910fa33f840f182d1dbff))
- Drop Shader broadcast failure message
  - Added debugging suggestions to drop shader broadcast failure message
  - Add two instrumentation arguments for overriding shader dropping behavior to workaround crashes when benchmarking apps without `ProfileInstaller` 1.3:
    - `androidx.benchmark.dropShaders.enable=true/false` : can be used to skip all shader dropping (including that done in `StartupMode.Cold` launches), esp when benchmarking apps that don't yet use profileinstaller 1.3
    - `androidx.benchmark.dropShaders.throwOnFailure=true/false` : can be used to tolerate failures when trying to drop shaders, for example when benchmarking apps without profileinstaller 1.3 ([I4f573](https://android-review.googlesource.com/#/q/I4f57309332981ee79d082237ebaca887f39417b3))
- Added experimental `MacrobenchmarkRule#measureRepeated` variant which takes a custom `PerfettoConfig` for fully customized Perfetto trace recording. Note that incorrectly configured configs may cause built in Metric classes to fail. ([Idfd3d](https://android-review.googlesource.com/#/q/Idfd3d0c071005f04f8be9975c6379e6095416775), [b/309841164](https://issuetracker.google.com/issues/309841164), [b/304038384](https://issuetracker.google.com/issues/304038384))
- Cancel background dexopt jobs before running a Macrobenchmark to reduce interference. ([I989ed](https://android-review.googlesource.com/#/q/I989ed4f9e8384734f2fd16da7d6817f8dd1ee6cd))
- Macrobenchmark now waits for 1 second for the target application to flush an ART profile (previously it waited for 500 ms). ([I85a50](https://android-review.googlesource.com/#/q/I85a50e775f8b997c9a69c7a40d1e2b59561a10b1), [b/316082056](https://issuetracker.google.com/issues/316082056))
- [TraceSectionMetric](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/TraceSectionMetric) overhaul
  - **Note** : `TraceSectionMetric` changes below can affect outputs in CI usage, and may create discontinuities, or break parsing
  - Sum is now the default, as most usage of this metric is for repeated events, and first would discard data in these cases
  - Changed to be more customizable, with more available modes
  - Mode names are now embedded in metric output name (in Studio and JSON)
  - Now supports slices created using `Trace.{begin|end}AsyncSection`.
- Metrics
  - Power - Added `PowerMetric.deviceSupportsHighPrecisionTracking`, `PowerMetric.deviceBatteryHasMinimumCharge()` and `PowerMetric.deviceSupportsPowerEnergy()`
  - Renamed `Metric.getResult` to `getMeasurements` to match return type
  - Added log.w / exception labels to all startup detection failures. This does not change current behavior (so some errors throw, and others silently fail to detect the startup), just makes it more understandable. Generally the ones that `Log.w()` and fail to report startup metrics are those where non-frame events are missing, exceptions are thrown when startup is detected except for frame timing information (from UI/RT slices). ([Id240f](https://android-review.googlesource.com/#/q/Id240f7698dfb977457362a137f0070e73dc2495c), [b/329145809](https://issuetracker.google.com/issues/329145809))
  - Added `frameCount` measurement to `FrameTimingMetric` to aid in discovery of scenarios where measurements change because the number of frames produced changed (new animations added, invalidation issues fixed). ([I1e5aa](https://android-review.googlesource.com/#/q/I1e5aac6e28546cb5a9e1714ceac342c43e3a444c))
  - Clarified that `frameOverrunMs` is the preferred metric for tracking when available in docs, and why. ([I18749](https://android-review.googlesource.com/#/q/I1874977e4a9e8c0bebde86a7f6159d5730a26c47), [b/329478323](https://issuetracker.google.com/issues/329478323))
  - Fixes issue where unterminated frames at the beginning and end of the trace could be paired together, which would incorrectly report as a single extremely long frame. ([I39353](https://android-review.googlesource.com/#/q/I393531f8cf983b2700c419c00a9c7c47ec382e67), [b/322232828](https://issuetracker.google.com/issues/322232828))
  - Improve `FrameTimingMetric` error when frames aren't produced, and always output link to trace when failing metric parsing to assist in diagnosing problem. ([I956b9](https://android-review.googlesource.com/#/q/I956b90505fbd72a80dc00ad2214420f4d3957659))
  - Fixed crash in `FrameTimingMetric` failing to parse frame id, especially on certain OEM devices. ([Ia24bc](https://android-review.googlesource.com/#/q/Ia24bc3c90b317252f579cc2425547f034ef96ef8), [b/303823815](https://issuetracker.google.com/issues/303823815), [b/306235276](https://issuetracker.google.com/issues/306235276))
  - Relaxed strictness of checks in `FrameMetrics`, and added more detail to error messages. ([Iadede](https://android-review.googlesource.com/#/q/Iadededa9b5721f1e68534a0457c3dfc2f8c91b0f))

**Baseline Profile capture / Gradle plugin changes since 1.2.0**

- Increased max recommended version of AGP to 9.0.0-alpha01.
- Ensure `mergeArtProfile` and `mergeStartupProfile` tasks always wait for baseline profile generation. ([I623d6](https://android-review.googlesource.com/q/I623d65b8fedc7abb1d22fb2ca016582703f51176), [b/343086054](https://issuetracker.google.com/issues/343086054))
- Generating a baseline profile successfully will output a summary of what changed ([I824c8](https://android-review.googlesource.com/#/q/I824c84553c4c1c0dd5b585f0846093762b938460), [b/269484510](https://issuetracker.google.com/issues/269484510))
- Added DSL to disable warnings ([Ic4deb](https://android-review.googlesource.com/#/q/Ic4deb86fc3b91a31854053f19581e9798e43cbd6), [b/331237001](https://issuetracker.google.com/issues/331237001))
- Fix to ensure benchmarks use generated baseline profiles when `automaticGenerationDuringBuild` is off ([Ic144f](https://android-review.googlesource.com/#/q/Ic144f394c09ec666d4892a4168a2197dc5031039), [b/333024280](https://issuetracker.google.com/issues/333024280))
- Fix `BaselineProfile` gradle plugin property overrides to enable baseline profile generation and benchmarking when customizing a `nonMinified` or benchmark build type. ([Ib8f05](https://android-review.googlesource.com/#/q/Ib8f0555001ff719f4b82c35cf50c13b4a3fa308d), [b/324837887](https://issuetracker.google.com/issues/324837887))
- Fix for including library baseline profiles in AAR prior to AGP 8.3.0-alpha15. ([I1d2af](https://android-review.googlesource.com/#/q/I1d2af6193d596a43a5f6a05eb15b2b0951523ad4), [b/313992099](https://issuetracker.google.com/issues/313992099))
- Fixed baseline and startup profile output url at the end of generation task. ([I802e5](https://android-review.googlesource.com/#/q/I802e5e2b335a1efa0370a0ac3d5e5bc656827f0f), [b/313976958](https://issuetracker.google.com/issues/313976958))

**Other significant changes since 1.2.0**

- Trace capture
  - Reduced EXITCODE 2 error when starting perfetto from an error to logged warning
  - Enable AIDL tracing by default in benchmarks(requires API 28) ([Ia0af2](https://android-review.googlesource.com/#/q/Ia0af2a55ac2635db68427845860dc96d93994220), [b/341852305](https://issuetracker.google.com/issues/341852305))
  - Enable porter tag tracing by default in benchmarks. This captures, for example, wakelock tracepoints. ([Icfe44](https://android-review.googlesource.com/#/q/Icfe44e708991bb03eff2c8df527a6fe9f872fb88), [b/286551983](https://issuetracker.google.com/issues/286551983))
  - Increased trace capture start timeout to avoid crashes when starting tracing on slower devices ([I98841](https://android-review.googlesource.com/#/q/I988418daa69ec33343364f7ad7c5fca26a39a5fa), [b/329145808](https://issuetracker.google.com/issues/329145808))
  - Added public API `PerfettoTraceProcessor.Session.queryMetrics` APIs with JSON, textproto, and proto binary (undecoded) variants. These allow you to query metrics built into `TraceProcessor` ([I54d7f](https://android-review.googlesource.com/#/q/I54d7fb0cfd2d6e448bda78d9397cb96d77a2125b), [b/304038382](https://issuetracker.google.com/issues/304038382))
  - Enable blocking start on Perfetto trace record to reduce risk of missing data at beginning of trace. Only supported on API 33+. ([Ie6e41](https://android-review.googlesource.com/#/q/Ie6e417ad248b431ebf6096e2865265d51553be7f), [b/310760059](https://issuetracker.google.com/issues/310760059))
- JSON output
  - Added additional information in benchmark context in JSON output:
    - `context.artMainlineVersion` - integer version of Art mainline module (if present on device, `-1` otherwise)
    - `context.build.id` - Equals [android.os.Build.ID](http://android.os.Build.ID)
    - `context.build.version.codename` - Equals [android.os.Build.VERSION.CODENAME](http://android.os.Build.VERSION.CODENAME)
    - `context.build.version.abbreviatedCodename` - corresponds to first letter of pre-release codename (including on release builds) ([Ie5020](https://android-review.googlesource.com/c/platform/frameworks/support/+/3081738))
  - Added `profilerOutput` list to JSON output for easier tooling around profiling traces (e.g. Perfetto, Method traces) ([I05ddd](https://android-review.googlesource.com/#/q/I05ddd9af8864fdb79ce076e836699b80fca864e6), [b/332604449](https://issuetracker.google.com/issues/332604449))
  - Added a warning when Android Test Orchestrator is used in benchmark modules, as this will cause per-module output JSON files to be repeatedly overwritten. ([Ia1af6](https://android-review.googlesource.com/#/q/Ia1af6a178c9ef1c7e0dd80f735749eb97f416d7e), [b/286899049](https://issuetracker.google.com/issues/286899049))
  - Throw when filenames are longer than 200 chars to avoid unclear crashes when writing or post-processing files. ([I4a5ab](https://android-review.googlesource.com/#/q/I4a5abd3ce0107d4465fd88f9067592a8a06f8e7c))

### Version 1.3.0-rc01

August 7, 2024

`androidx.benchmark:benchmark-*:1.3.0-rc01` is released. Version 1.3.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/56579bc30499ce39f0d7a6713a065b00c6194206..2f785440e93a6465ac53828357b5f71f0ad28329/benchmark).

**Bug Fixes**

- Fix `androidx.benchmark.cpuEventCounter` producing corrupt values for non-Instruction events ([I7386a](https://android-review.googlesource.com/#/q/I7386abe3494b2b11a2447fa85a4109613857c28c), [b/286306579](https://issuetracker.google.com/issues/286306579))
- Fix `resumeTiming`/`runWithTimingDisabled` to respect metric priority order, and significantly reduce impact of lower priority metric pause/resume on higher priority metric results. For example, if using cpu perf counters via `cpuEventCounter.enable` instrumentation argument, timeNs is no longer significantly reduced when pause/resume occur. ([I39c2e](https://android-review.googlesource.com/#/q/I39c2eb911129927972740d074ee8f2adca7bda1a), [b/286306579](https://issuetracker.google.com/issues/286306579), [b/307445225](https://issuetracker.google.com/issues/307445225))
- Reduced chance of stack sampling causing `measureRepeatedOnMainThread` from hitting main thread hard timeout by moving stack sampling conversion off main thread. ([I487a8](https://android-review.googlesource.com/#/q/I487a8df198f66a1af0001d2f0faece5288eff178), [b/342237318](https://issuetracker.google.com/issues/342237318))
- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See [this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd) for more details. ([I9496c](https://android-review.googlesource.com/#/q/I9496cfaeb50a5c484fbee6521b74a0605fb013dc), [b/345472586](https://issuetracker.google.com/issues/345472586))
- Added agp version check to send package name as instr arg. Previous to AGP 8.4.0 the target app package name cannot be send to the instrumentation app via instrumentation arguments. ([0c72a3f](https://android.googlesource.com/platform/frameworks/support/+/0c72a3f2f9bd7c26741d94fa210a8ac227bf03cc))

### Version 1.3.0-beta02

July 10, 2024

`androidx.benchmark:benchmark-*:1.3.0-beta02` is released. Version 1.3.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e688db5c82e85000364f92965558ef1e2236c5a0..56579bc30499ce39f0d7a6713a065b00c6194206/benchmark).

**Bug Fixes**

- Gracefully handle EXITCODE `2` when starting Perfetto to log a warning, but proceed.

### Version 1.3.0-beta01

June 12, 2024

`androidx.benchmark:benchmark-*:1.3.0-beta01` is released. Version 1.3.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6a69101fd0edc8d02aa316df1f43e0552fd2d7c4..e688db5c82e85000364f92965558ef1e2236c5a0/benchmark).

**API Changes**

- Renamed `MethodTracing.affectsMeasurementOnThisDevice` to `AFFECTS_MEASUREMENT_ON_THIS_DEVICE` for consistency. ([I1bdfa](https://android-review.googlesource.com/#/q/I1bdfa9acbd481f837649a2444fee46185d49bd61))
- Added experimental `BlackHole.consume()` api to prevent dead code elimination in microbenchmarks. ([If6812](https://android-review.googlesource.com/#/q/If681208c4e5ad5d054117c2320b4fd56b86f4ff5), [b/286091643](https://issuetracker.google.com/issues/286091643))
- Microbenchmark will now correctly throw to prevent method tracing from interfering with measurements. This occurs on certain devices when method tracing is forced on (via instrumentation args or `MicrobenchmarkConfig`), and if a measurement is attempted after a method trace. Affected devices are running API 26-30 or certain ART mainline module versions affected by this interference, and can be detected at runtime via `ProfilerConfig.MethodTracing.affectsMeasurementOnThisDevice`. ([Iafb92](https://android-review.googlesource.com/#/q/Iafb92c47c76bf257c047634b61401d873ce85cc5), [b/303660864](https://issuetracker.google.com/issues/303660864))

**Bug Fixes**

- Bumped max agp version recommended to 9.0.0-alpha01. ([I5bbb0](https://android-review.googlesource.com/#/q/I5bbb0401cf54f7f5394e7462235947d61be20ee2))
- Added compilation mode to benchmark context ([If5612](https://android-review.googlesource.com/#/q/If5612552a718b459e95cd96dc721e92a88e3fa8a), [b/325512900](https://issuetracker.google.com/issues/325512900))
- Enable AIDL tracing by default (requires API 28) ([Ia0af2](https://android-review.googlesource.com/#/q/Ia0af2a55ac2635db68427845860dc96d93994220), [b/341852305](https://issuetracker.google.com/issues/341852305))
- Added additional information in benchmark context in JSON output:
  - `context.artMainlineVersion` - integer version of Art mainline module (if present on device, -1 otherwise)
  - `context.build.id` - Equals `android.os.Build.ID`
  - `context.build.version.codename` - Equals `android.os.Build.VERSION.CODENAME`
  - `context.build.version.abbreviatedCodename` - corresponds to first letter of pre-release codename (even on release builds) ([Ie5020](https://android-review.googlesource.com/#/q/Ie502065af175c2a8054bbe85716f15f4ff38b822))
- Fixes `StackSampling` to respect `androidx.benchmark.profiling.sampleDurationSeconds` ([Ib1d53](https://android-review.googlesource.com/#/q/Ib1d5318442eb4bb586d6d5c06ce57bb929e1d996))
- Change macro-\>common dependency to be `api()`, so it's easier to use e.g. `PerfettoTrace` and `PerfettoConfig`. ([Icdae3](https://android-review.googlesource.com/#/q/Icdae394628d71131e556c6a02840c6c894f82957), [b/341851833](https://issuetracker.google.com/issues/341851833))
- Ensure `mergeArtProfile` and `mergeStartupProfile` tasks always wait for baseline profile generation. ([I623d6](https://android-review.googlesource.com/q/I623d65b8fedc7abb1d22fb2ca016582703f51176), [b/343086054](https://issuetracker.google.com/issues/343086054))
- Consider variant enable state when deciding whether variant should be enabled. ([I5d19e](https://android-review.googlesource.com/q/I5d19e3040d28243857fab9b9a679057d6ad46c1b), [b/343249144](https://issuetracker.google.com/issues/343249144))
- Increased default start timeout for perfetto trace processor. ([I87e8c](https://android-review.googlesource.com/q/I87e8c9ec3472db0aafb908b590a9a91f6e9e5ed8), [b/329145808](https://issuetracker.google.com/issues/329145808))

### Version 1.3.0-alpha05

May 14, 2024

`androidx.benchmark:benchmark-*:1.3.0-alpha05` is released. Version 1.3.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1cca2c587b3e9207f9ee45e4c84b96b3512e748f..6a69101fd0edc8d02aa316df1f43e0552fd2d7c4/benchmark).

**Bug Fixes**

- Throw clearer exception when macrobench metric returns zero values for all iterations ([Iab58f](https://android-review.googlesource.com/#/q/Iab58f90540ac47c15d1e013ce6d7dcc491babb5c), [b/314931695](https://issuetracker.google.com/issues/314931695))
- Additional workaround rules added to microbench proguard rules, including support for listener rules and other observed warnings / errors. ([I14d8f](https://android-review.googlesource.com/#/q/I14d8fe36a73ce04076da29eb792679651e895601), [b/329126308](https://issuetracker.google.com/issues/329126308), [b/339085669](https://issuetracker.google.com/issues/339085669))
- Method tracing runs as a separate phase during a Macrobenchmark, and it no longer affects measurements. ([If9a50](https://android-review.googlesource.com/#/q/If9a504a7bce7228840339b34294ba3fdf98aceeb), [b/285912360](https://issuetracker.google.com/issues/285912360), [b/336588271](https://issuetracker.google.com/issues/336588271))
- Added extra debugging suggestions to drop shader broadcast failure message. ([I5efa6](https://android-review.googlesource.com/#/q/I5efa660caabba1e9367aeabfd48b320dca41eed1), [b/325502725](https://issuetracker.google.com/issues/325502725))

### Version 1.3.0-alpha04

May 1, 2024

`androidx.benchmark:benchmark-*:1.3.0-alpha04` is released. Version 1.3.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9ece0ba5451df94f20485ea5647d9221742585a1..1cca2c587b3e9207f9ee45e4c84b96b3512e748f/benchmark).

**API Changes**

- Added experimental `MacrobenchmarkRule#measureRepeated` variant which takes a custom `PerfettoConfig` for fully customized Perfetto trace recording. Note that incorrectly configured configs may cause built in Metric classes to fail. ([Idfd3d](https://android-review.googlesource.com/#/q/Idfd3d0c071005f04f8be9975c6379e6095416775), [b/309841164](https://issuetracker.google.com/issues/309841164), [b/304038384](https://issuetracker.google.com/issues/304038384))
- Rename `PowerMetric.deviceSupportsPowerEnergy` to `PowerMetric.deviceSupportsHighPrecisionTracking` for clarity ([I5b82f](https://android-review.googlesource.com/#/q/I5b82f10d03f4e612dda30bd144d4f99548357f80))
- Added `PowerMetric.deviceBatteryHasMinimumCharge()` and `PowerMetric.deviceSupportsPowerEnergy()` to enable changing or skipping benchmarks based on device power measurement capability. ([I6a591](https://android-review.googlesource.com/#/q/I6a591cd0c68e7a9e93069ee7f636fc1772f9a256), [b/322121218](https://issuetracker.google.com/issues/322121218))

**Bug Fixes**

- Added comparison with previous baseline profile ([I824c8](https://android-review.googlesource.com/#/q/I824c84553c4c1c0dd5b585f0846093762b938460), [b/269484510](https://issuetracker.google.com/issues/269484510))
- Added DSL to disable warnings ([Ic4deb](https://android-review.googlesource.com/#/q/Ic4deb86fc3b91a31854053f19581e9798e43cbd6), [b/331237001](https://issuetracker.google.com/issues/331237001))
- Changed exception to info log when benchmark variants are disabled ([I8a517](https://android-review.googlesource.com/#/q/I8a517fac2e12c761d49259bf30471e66a04b5383), [b/332772491](https://issuetracker.google.com/issues/332772491))
- Make it simpler to capture method traces for a Macrobenchmark is scoped to the duration of the actual `measureBlock()`. Previously, it started at target process launch and only supported cold starts ([Iee85a](https://android-review.googlesource.com/#/q/Iee85a37d5b03d92a3128c976b41bd145b2921161), [b/300651094](https://issuetracker.google.com/issues/300651094))
- Avoid crashing when perfetto trace processor is slow to start ([I98841](https://android-review.googlesource.com/#/q/I988418daa69ec33343364f7ad7c5fca26a39a5fa), [b/329145808](https://issuetracker.google.com/issues/329145808))

### Version 1.3.0-alpha03

April 17, 2024

`androidx.benchmark:benchmark-*:1.3.0-alpha03` is released. Version 1.3.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a57d7d17753695012b58c9ce7ad55a8d39157e62..9ece0ba5451df94f20485ea5647d9221742585a1/benchmark).

**New Features**

- Adds public API `PerfettoTraceProcessor.Session.queryMetrics` APIs with JSON, textproto, and proto binary (undecoded) variants. These allow you to query [metrics built into TraceProcessor](https://perfetto.dev/docs/quickstart/trace-analysis#trace-based-metrics) ([I54d7f](https://android-review.googlesource.com/#/q/I54d7fb0cfd2d6e448bda78d9397cb96d77a2125b), [b/304038382](https://issuetracker.google.com/issues/304038382))
- Added `profilerOutput` to JSON output for easier tooling around profiling traces (e.g. perfetto, method traces). ([I05ddd](https://android-review.googlesource.com/#/q/I05ddd9af8864fdb79ce076e836699b80fca864e6), [b/332604449](https://issuetracker.google.com/issues/332604449))
- Added power tag to benchmark Perfetto Config. This captures, for example, wakelock tracepoints. ([Icfe44](https://android-review.googlesource.com/#/q/Icfe44e708991bb03eff2c8df527a6fe9f872fb88), [b/286551983](https://issuetracker.google.com/issues/286551983))
- Added inst argument `androidx.benchmark.profiling.skipWhenDurationRisksAnr`, can be set to false to avoid skipping method traces when expected duration may cause an ANR - strongly recommended to avoid in CI runs.
- Added experimental inst argument `androidx.benchmark.profiling.perfCompare.enable`, set this to true to run comparison timing between measurement and profiling phases. Useful in e.g. evaluating overhead of method tracing. ([I61fb4](https://android-review.googlesource.com/#/q/I61fb4703f52e8451bf87abf7d50f6f3b1facdabf), [b/329146942](https://issuetracker.google.com/issues/329146942))

**API Changes**

- Changed `TraceSectionMetric.Mode` to sealed class to enable future expansion without breaking exhaustive when statements ([I71f7b](https://android-review.googlesource.com/#/q/I71f7b246b0db606cec972d9a55e83f0281fa55f4))
- Added `TraceSectionMetric.Mode.Average` and `.Count`, and reordered args so the more common argument (mode) was earlier in the arg list, reducing need for specifying parameter names. ([Ibf0b0](https://android-review.googlesource.com/#/q/Ibf0b0b5a791460b6d37a4ef43dc369d6c8414ab7), [b/315830077](https://issuetracker.google.com/issues/315830077), [b/322167531](https://issuetracker.google.com/issues/322167531))
- Renamed `Metric.getResult` to `getMeasurements` to match return type ([I42595](https://android-review.googlesource.com/#/q/I4259554a5266d4dbc8e7319b0b88c682733dc64a))

**Bug Fixes**

- Fix to ensure benchmarks use generated baseline profiles when `automaticGenerationDuringBuild` is off ([Ic144f](https://android-review.googlesource.com/#/q/Ic144f394c09ec666d4892a4168a2197dc5031039), [b/333024280](https://issuetracker.google.com/issues/333024280))
- Fix `BaselineProfile` gradle plugin property overrides to enable baseline profile generation and benchmarking when customizing a `nonMinified` or benchmark build type. ([Ib8f05](https://android-review.googlesource.com/#/q/Ib8f0555001ff719f4b82c35cf50c13b4a3fa308d), [b/324837887](https://issuetracker.google.com/issues/324837887))
- Fixed method traces flush in macrobenchmark, so that method traces should be fully captured and valid, even on slower devices. ([I6349a](https://android-review.googlesource.com/#/q/I6349a48dca4116ac9b481882395ee630785f6181), [b/329904950](https://issuetracker.google.com/issues/329904950))
- Enable blocking start on Perfetto trace record to reduce risk of missing data at beginning of trace. Only supported on API 33+. ([Ie6e41](https://android-review.googlesource.com/#/q/Ie6e417ad248b431ebf6096e2865265d51553be7f), [b/310760059](https://issuetracker.google.com/issues/310760059))
- Added a warning when Android Test Orchestrator is used in benchmark modules, as this will cause per-module output JSON files to be repeatedly overwritten. ([Ia1af6](https://android-review.googlesource.com/#/q/Ia1af6a178c9ef1c7e0dd80f735749eb97f416d7e), [b/286899049](https://issuetracker.google.com/issues/286899049))
- Force ',' (comma) thousands separators for consistency in Studio output, ignoring device locale ([I3e921](https://android-review.googlesource.com/#/q/I3e92172b3b507068eac6154bd1f8fa02d3236197), [b/313496656](https://issuetracker.google.com/issues/313496656))
- `TraceSectionMetric` now supports slices created using `Trace.{begin|end}AsyncSection`. ([I91b32](https://android-review.googlesource.com/#/q/I91b326e121fcca4b3ce8f65381eea87de796cdd1), [b/300434906](https://issuetracker.google.com/issues/300434906))
- Added log.w / exception labels to all startup detection failures. This does not change current behavior (so some errors throw, and others silently fail to detect the startup), just makes it more understandable. Generally the ones that `Log.w()` and fail to report startup metrics are those where non-frame events are missing, exceptions are thrown when startup is detected except for frame timing information (from UI/RT slices). ([Id240f](https://android-review.googlesource.com/#/q/Id240f7698dfb977457362a137f0070e73dc2495c), [b/329145809](https://issuetracker.google.com/issues/329145809))
- Cancel background dexopt jobs before running a Macrobenchmark to reduce interference. ([I989ed](https://android-review.googlesource.com/#/q/I989ed4f9e8384734f2fd16da7d6817f8dd1ee6cd))
- Added `frameCount` measurement to `FrameTimingMetric` to aid in discovery of scenarios where measurements change because the number of frames produced changed (new animations added, invalidation issues fixed). ([I1e5aa](https://android-review.googlesource.com/#/q/I1e5aac6e28546cb5a9e1714ceac342c43e3a444c))
- Clarified that `frameOverrunMs` is the preferred metric for tracking when available in docs, and why. ([I18749](https://android-review.googlesource.com/#/q/I1874977e4a9e8c0bebde86a7f6159d5730a26c47), [b/329478323](https://issuetracker.google.com/issues/329478323))

### Version 1.3.0-alpha02

March 20, 2024

`androidx.benchmark:benchmark-*:1.3.0-alpha02` is released. Version 1.3.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e1b82c49c59d8e976ce558aba5586f6c61bc9054..a57d7d17753695012b58c9ce7ad55a8d39157e62/benchmark).

**New Features**

- Experimental R8 support in microbench via embedded proguard rules. Note that this support is experimental, and requires AGP 8.3 for minification of library module tests. Use the following to enable R8 minification/optimization in your benchmark module's `build.gradle`, which should lead to a significant performance increase, depending on workload. ([I738a3](https://android-review.googlesource.com/#/q/I738a3294c5ded7b336ed0f49d0615eb9231cce51), [b/184378053](https://issuetracker.google.com/issues/184378053))

      android {
          buildTypes.release.androidTest.enableMinification = true
      }

**Bug Fixes**

- Fixes method tracing warning to be on separate line from microbench output. ([I0455c](https://android-review.googlesource.com/#/q/I0455c4edcdc592c56e60dd19bd32d9bd33f6af6a), [b/328308833](https://issuetracker.google.com/issues/328308833))

### Version 1.3.0-alpha01

February 21, 2024

`androidx.benchmark:benchmark-*:1.3.0-alpha01` is released. [Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9e027e27c0db4f6f105eca82dca664195b5f0f54..e1b82c49c59d8e976ce558aba5586f6c61bc9054/benchmark)

**API Changes**

- Renamed `MicrobenchmarkConfig` boolean parameters to avoid unnecessary word 'should' ([Ia8f00](https://android-review.googlesource.com/#/q/Ia8f009b76a7adfc081bf3e4a2e730393fd4d4af8), [b/303387299](https://issuetracker.google.com/issues/303387299))
- Added `BenchmarkRule.measureRepeatedOnMainThread` so main thread benchmarks (e.g. ones touching Views or Compose UIs) can avoid triggering ANRs, especially during large suites in CI. ([I5c86d](https://android-review.googlesource.com/#/q/I5c86dd05d6eca4984805d13a18d22b39a2382b02))
- Added `FrameTimingGfxInfoMetric`, an experimental alternate implementation of `FrameTimingMetric` with measurements coming directly from the platform, rather than extracted from the Perfetto trace. ([I457cb](https://android-review.googlesource.com/#/q/I457cbf351ee86141130d1667b6f352cd2ade453b), [b/322232828](https://issuetracker.google.com/issues/322232828))
- Add the ability to dump an ART profile during individual `warmUp` iterations. ([I17923](https://android-review.googlesource.com/#/q/I17923a8bc7d37fa8472910fa33f840f182d1dbff))
- Several changes to `TraceSectionMetric` API:
  - Add `Mode.Min`, `Mode.Max`
  - Add label argument to override section name as metric label
  - Added mode name to output to clarify metric meaning
  - Changed default to sum, as most usage of this metric is for repeated events Be aware of this changes in CI usage, as it may create discontinuities or break parsing. ([Ic1e82](https://android-review.googlesource.com/#/q/Ic1e821511d80afb2927b3cb1095336de85e82ba1), [b/301892382](https://issuetracker.google.com/issues/301892382), [b/301955938](https://issuetracker.google.com/issues/301955938))

**Bug Fixes**

- Improved error message in baseline profile gradle plugin when specified managed device does not exist ([Idea2b](https://android-review.googlesource.com/#/q/Idea2b6d830807f215a576192bbbf844659a97c58), [b/313803289](https://issuetracker.google.com/issues/313803289))
- Fix for including library baseline profiles in AAR prior to AGP 8.3.0-alpha15 ([I1d2af](https://android-review.googlesource.com/#/q/I1d2af6193d596a43a5f6a05eb15b2b0951523ad4), [b/313992099](https://issuetracker.google.com/issues/313992099))
- Fixed baseline and startup profile output url at the end of generation task ([I802e5](https://android-review.googlesource.com/#/q/I802e5e2b335a1efa0370a0ac3d5e5bc656827f0f), [b/313976958](https://issuetracker.google.com/issues/313976958))
- Adjusted data source timeouts to attempt to fix `java.lang.IllegalStateException: Failed to stop [ProcessPid(processName=perfetto, pid=...)]` ([I8dc7d](https://android-review.googlesource.com/#/q/I8dc7d5091ea1a8e68cb5effb21363f1c3196cf56), [b/323601788](https://issuetracker.google.com/issues/323601788))
- Add two instrumentation arguments for overriding shader dropping behavior to workaround crashes when benchmarking apps without `ProfileInstaller` 1.3:
  - `androidx.benchmark.dropShaders.enable=true/false` : can be used to skip all shader dropping (including that done in `StartupMode.Cold` launches), esp when benchmarking apps that don't yet use profileinstaller 1.3
  - `androidx.benchmark.dropShaders.throwOnFailure=true/false` : can be used to tolerate failures when trying to drop shaders, for example when benchmarking apps without profileinstaller 1.3 ([I4f573](https://android-review.googlesource.com/#/q/I4f57309332981ee79d082237ebaca887f39417b3))
- Skip method tracing on UI thread when expected to take longer than a few seconds, and cleanup method traces when throwing. ([I6e768](https://android-review.googlesource.com/#/q/I6e7689e1c0087aa557015aea5690e439786d5565))
- Throw when filenames are longer than 200 chars to avoid unclear crashes when writing or post-processing files. ([I4a5ab](https://android-review.googlesource.com/#/q/I4a5abd3ce0107d4465fd88f9067592a8a06f8e7c))
- Fixes issue where unterminated frames at the beginning and end of the trace could be paired together, which would incorrectly report as a single extremely long frame. ([I39353](https://android-review.googlesource.com/#/q/I393531f8cf983b2700c419c00a9c7c47ec382e67), [b/322232828](https://issuetracker.google.com/issues/322232828))
- Use `--skip verification` on API 30+ when reinstalling a package on API 30-33 to clear ART profiles on user builds. This helps bypass Play Protect warnings that cause failures on some class of devices. ([Ic9e36](https://android-review.googlesource.com/#/q/Ic9e366f45be17cc45da5f273901ff2bc620ff9eb))
- Use `am force-stop` to kill apps when not a system app like System UI or Launcher. ([I5e028](https://android-review.googlesource.com/#/q/I5e0280463ecbfe34b0805225dba0f77f2c740a27))
- Macrobenchmark now waits for `1 second` for the target application to flush an ART profile (previously it waited for `500 ms`). ([I85a50](https://android-review.googlesource.com/#/q/I85a50e775f8b997c9a69c7a40d1e2b59561a10b1), [b/316082056](https://issuetracker.google.com/issues/316082056))
- Improve `FrameTimingMetric` error when frames aren't produced, and always output link to trace when failing metric parsing to assist in diagnosing problem. ([I956b9](https://android-review.googlesource.com/#/q/I956b90505fbd72a80dc00ad2214420f4d3957659))
- Fixed crash in `FrameTimingMetric` failing to parse frame id, especially on certain OEM devices. ([Ia24bc](https://android-review.googlesource.com/#/q/Ia24bc3c90b317252f579cc2425547f034ef96ef8), [b/303823815](https://issuetracker.google.com/issues/303823815), [b/306235276](https://issuetracker.google.com/issues/306235276))
- Relaxed strictness of checks in `FrameMetrics`, and added more detail to error messages. ([Iadede](https://android-review.googlesource.com/#/q/Iadededa9b5721f1e68534a0457c3dfc2f8c91b0f))

## Version 1.2

### Version 1.2.4

April 17, 2024

`androidx.benchmark:benchmark-*:1.2.4` is released. Version 1.2.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9e027e27c0db4f6f105eca82dca664195b5f0f54..e7365ab824864067473dc58826e3ab710577345e/benchmark).

**Bug Fixes**

- Fixes baseline profile srcset not being set up in benchmark variants. Also fixes `automaticGenerationDuringBuild` in libraries causing a circular dependency. ([I28ab7](https://android-review.googlesource.com/#/q/I28ab748ce760dcf90086a34e6bf6571a3d54d3bb), [b/333024280](https://issuetracker.google.com/issues/333024280))
- Use `am force-stop` to kill apps when not a system app like System UI or Launcher. This fixes `StartupMode.COLD` benchmarks crashing from "Package $package must not be running prior to cold start!" due to process kill not fully succeeding. ([I5e028](https://android-review.googlesource.com/#/q/I5e0280463ecbfe34b0805225dba0f77f2c740a27))

### Version 1.2.3

January 24, 2024

`androidx.benchmark:benchmark-*:1.2.3` is released. [Version 1.2.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b6e0f5ffac318239f704fedbde6281bdd42d9fd9..9e027e27c0db4f6f105eca82dca664195b5f0f54/benchmark)

**Bug Fixes**

- Removed exception from Baseline Profile Gradle Plugin when AGP version is 8.3.0 or higher.
- Fix for including library baseline profiles in AAR prior to AGP 8.3.0-alpha15.

### Version 1.2.2

December 1, 2023

`androidx.benchmark:benchmark-*:1.2.2` is released. [Version 1.2.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/dd28c3e7d9e6ce9ec5ea046c8b09c28d3449656a..72f6955a7392567f82ddbd849864f8d27a358781/benchmark)

**Baseline Profiles**

- Execution logs will show the baseline profile output file path as a local file URI ([aosp/2843918](https://android-review.googlesource.com/2843918), [aosp/2853665](https://android-review.googlesource.com/2853665), [b/313976958](https://issuetracker.google.com/issues/313976958))

### Version 1.2.1

November 15, 2023

`androidx.benchmark:benchmark-*:1.2.1` is released. [Version 1.2.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4d17fe57ec366c9d3a8fc21a851974189b615a12..dd28c3e7d9e6ce9ec5ea046c8b09c28d3449656a/benchmark)

**New Features**

- Improved error message when user disables test variants ([b/307478189](https://issuetracker.google.com/issues/307478189))
- Added properties to support AS test run integration ([b/309805233](https://issuetracker.google.com/issues/309805233)), ([b/309116324](https://issuetracker.google.com/issues/309116324))

### Version 1.2.0

October 18, 2023

`androidx.benchmark:benchmark-*:1.2.0` is released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c65e8e30c0edf5bb898c705ceab72d04ffbc0de7..02ee67f42727c99060859cf146f7a61c8db1fe96/benchmark)

**Important changes since 1.1.0**

**Baseline Profiles**

- New [Baseline Profile Gradle Plugin](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile#android%20studio%20hedgehot) automates capturing and including baseline profiles in your test and build workflow.
- `BaselineProfileRule.collect` now stable, a streamlined and simplified version of the previous experimental `BaselineProfileRule.collectBaselineProfile` API
  - Just specify `packageName`, and drive your app
- For libraries generating baseline profiles, you can now filter the rules generated either in code (`BaselineProfileRule.collect` argument), or even more simply in the gradle plugin
- Fixes
  - Fixed baseline profile collection on Android U+ ([Id1392](https://android-review.googlesource.com/#/q/Id1392207ec545dc4b095c4b435a92bb2a1ff0c66), [b/277645214](https://issuetracker.google.com/issues/277645214))

**Macrobenchmark**

- Compilation
  - Macrobenchmark now correctly fully resets compilation state for each compile - this requires reinstalling the APK prior to Android 14, so benchmarking on Android 14+ is strongly recommended if you want to persist state (like user login) in what's being measured.
  - You can also work around this by controlling app compilation separately, and skipping compilation with [`CompilationMode.Ignore()`](https://developer.android.com/reference/androidx/benchmark/macro/CompilationMode.Ignore) or [instrumentation argument](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-instrumentation-args#compilation-enabled)
- Instrumentation Arguments

  - Support for [`androidx.benchmark.dryRunMode.enable`](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-instrumentation-args#dryrunmode-enable) instrumentation argument, (already available in microbenchmark) for quicker validation runs (e.g. when creating the benchmark, or in presubmit)
  - Support for `androidx.benchmark.profiling.mode=StackSampling` and `MethodTracing`.
  - Added [`androidx.benchmark.enabledRules`](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-instrumentation-args#enabled-rules) to allow runtime filtering baseline profile vs macrobenchmark rule tests
  - Added [`androidx.benchmark.perfettoSdkTracing.enable`](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-instrumentation-args#perfettoSdkTracing) argument to enable tracing with tracing-perfetto, e.g. Compose recomposition tracing. Note that when used with `StartupMode.COLD`, timing will be significantly affected as the tracing library is loaded and enabled during app startup.
- Requirements

  - Macrobenchmark now requires `ProfileInstaller` 1.3.0 or greater in the target app, to enable profile capture / reset, and shader cache clearing.
- New Experimental [Metric APIs](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics)

  - Added experimental [`TraceSectionMetric`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/TraceSectionMetric), which allows for extracting simple timing from [`trace("") {}`](https://developer.android.com/topic/performance/tracing/custom-events) blocks in your app, or [TraceMetric](https://developer.android.com/reference/androidx/benchmark/macro/TraceMetric) for leveraging the full query capability of Perfetto `TraceProcessor`.
  - Added experimental [`PowerMetric`](https://developer.android.com/reference/androidx/benchmark/macro/PowerMetric) to capture power usage information
  - Added experimental [`MemoryCountersMetric`](https://developer.android.com/reference/androidx/benchmark/macro/MemoryCountersMetric) to count page faults
  - Added experimental [`PerfettoTraceProcessor`](https://developer.android.com/reference/androidx/benchmark/perfetto/PerfettoTraceProcessor) API, which is used internally to extract metrics from System traces (aka Perfetto traces)
- Fixes

  - Fixed crashes when installing or extracting profiles from an app installed from multiple APKs (e.g. from app bundle).
  - Fixed `FrameTimingMetric` ignoring frames with inconsistent frame IDs (generally, frames during ripples on API 31+) ([I747d2](https://android-review.googlesource.com/#/q/I747d23e6f5f38eda2c51ee3d26929fa4130e297c), [b/279088460](https://issuetracker.google.com/issues/279088460))
  - Fixed parsing errors on traces \> 64MB ([Ief831](https://android-review.googlesource.com/#/q/Ief831b2c58ebfeac3ae5cb2bfcb8623b920ad356), [b/269949822](https://issuetracker.google.com/issues/269949822))
  - Clarified errors when device (especially emulator) OS image not correctly configured for tracing, or compilation
  - Skip battery level check for devices without battery (micro and macro)
  - Improved file output, with more clear errors for invalid output directories, and safer defaults
  - Improved stability of `StartupMode.COLD` by consistently dropping the shader cache (also exposed via `MacrobenchmarkScope.dropShaderCache`)
  - Fixed leanback fallback for `startActivityAndWait`.

**Microbenchmark**

- Features
  - Profiling was moved to a separate phase, after other metrics, so one test run can display both accurate timing *and* profiling results.
- Experimental APIs
  - Added experimental [`MicrobenchmarkConfig`](https://developer.android.com/reference/kotlin/androidx/benchmark/MicrobenchmarkConfig) API for defining custom metrics and configuring tracing and profiling. Can be used to capture method traces, or capture tracepoints (but be aware of tracing overhead).
  - Added experimental APIs for controlling [`BenchmarkState`](https://developer.android.com/reference/kotlin/androidx/benchmark/BenchmarkState) separately from `BenchmarkRule`, without JUnit
  - Added experimental [`PerfettoTrace`](https://developer.android.com/reference/androidx/benchmark/perfetto/PerfettoTrace) record to enable capturing Perfetto traces, with custom configuration, separate from benchmark APIs.
- Fixes
  - Workaround missing leading whitespaces in Android Studio benchmark output.
  - Fix issue where warnings could fail to print in Android Studio benchmark output.
  - Fixed `SampledProfiling` crash on Android 13 (API 33) and higher.
  - Massively improved performance of `dryRunMode` by skipping `IsolationActivity` and Perfetto tracing (Up to 10x faster dry run mode on older OS versions).

### Version 1.2.0-rc02

October 6, 2023

`androidx.benchmark:benchmark-*:1.2.0-rc02` is released. [Version 1.2.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/fc9d0ceb0cf1daabde110d9965d3dd87319b575c..c65e8e30c0edf5bb898c705ceab72d04ffbc0de7/benchmark)

**Bug Fixes**

- Fix Benchmark file output to no longer break `BaselineProfile` Plugin file copying. Files were generated and copied off device, but had been renamed such that the gradle plugin wouldn't see them. ([I8dbcc](https://android-review.googlesource.com/#/q/I8dbccc5a11b4c391169cff6dfbd2a0001fd41001), [b/303034735](https://issuetracker.google.com/issues/303034735), [b/296453339](https://issuetracker.google.com/issues/296453339))
- Clarified `tracing-perfetto` loading error messages when injecting from macrobenchmark module into target application.

### Version 1.2.0-rc01

September 20, 2023

`androidx.benchmark:benchmark-*:1.2.0-rc01` is released. [Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/119f68768b14c444b7ba65b4b44abd0ed7d21002..fc9d0ceb0cf1daabde110d9965d3dd87319b575c/benchmark)

**Bug Fixes**

- An exception (with remedy instructions) is now thrown when Perfetto SDK tracing fails to initialize in a Benchmark. ([I6c878](https://android-review.googlesource.com/#/q/I6c87872507c126bdde3bc476a39baf75cc58c9de), [b/286228781](https://issuetracker.google.com/issues/286228781))
- Fix OOM crash when converting ART method trace -\> perfetto format. ([I106bd](https://android-review.googlesource.com/#/q/I106bdf99084af10f26a4503b02ae74b9eef8add0), [b/296905344](https://issuetracker.google.com/issues/296905344))
- (Macrobenchmark) Clarified method tracing label when linked in Studio test output, and fixed method tracing filenames to be unique on device/host, so they won't be overwritten when more than one benchmark is run. ([I08e65](https://android-review.googlesource.com/#/q/I08e65d3fe8ab77614b5a3cbc241fb7901ba57135), [b/285912360](https://issuetracker.google.com/issues/285912360))
- Ensures that the device is awake when capturing a baseline profile. ([I503fc](https://android-review.googlesource.com/#/q/I503fc259ecb28a0fd0c4ee5cca74795391dcbbb0))

### Version 1.2.0-beta05

August 30, 2023

`androidx.benchmark:benchmark-*:1.2.0-beta05` is released. [Version 1.2.0-beta05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/22eceaa7039e3fc1207b151f73e842c8021075f7..119f68768b14c444b7ba65b4b44abd0ed7d21002/)

**New Features**

- The Baseline Profile Gradle Plugin now supports Android Gradle Plugin 8.3. ([aosp/2715214](https://android.googlesource.com/platform/frameworks/support/+/2eb1e46de9ab545a059814e2ef7083c441f79693))

### Version 1.2.0-beta04

August 23, 2023

`androidx.benchmark:benchmark-*:1.2.0-beta04` is released. [Version 1.2.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5d7dd999525725bd038a00ca4e89e0fef624a6da..22eceaa7039e3fc1207b151f73e842c8021075f7/benchmark)

**New Features**

- The Baseline Profiles Gradle plugin now supports Android Gradle Plugin 8.3. ([aosp/2715214](https://android.googlesource.com/platform/frameworks/support/+/2eb1e46de9ab545a059814e2ef7083c441f79693))

**Bug Fixes**

- Fix failures in writing / moving and pulling files (especially those from parameterized tests) by sanitizing output file names further, avoiding '=' and ':' in output file names. ([I759d8](https://android-review.googlesource.com/#/q/I759d8bd2eec57db3829038fb73dad80e8d9849e2))

### Version 1.2.0-beta03

August 9, 2023

`androidx.benchmark:benchmark-*:1.2.0-beta03` is released. [Version 1.2.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d0e769360e8a16c7f813af4eb2c79d700f6b52a3..5d7dd999525725bd038a00ca4e89e0fef624a6da/benchmark)

**API Changes**

- Added argument to filter `TraceSectionMetric` to only the target package, on by default ([Ia219b](https://android-review.googlesource.com/#/q/Ia219bc25cd07a4c1915a1d37e744b2450a088744), [b/292208786](https://issuetracker.google.com/issues/292208786))

**Bug Fixes**

- Renamed `fullTracing.enable` instrumentation argument to `perfettoSdkTracing.enable` for consistency with artifact name, and other references. `fullTracing.enable` will continue to work as a fallback. ([I7cc00](https://android-review.googlesource.com/#/q/I7cc007e681db791998a08659ad09c3c21ab50513))
- Benchmark library internal tracepoints (including microbenchmark loop/phase tracing) will now show up in Studio system trace viewer, and nest under the correct process in Perfetto. ([I6b2e7](https://android-review.googlesource.com/#/q/I6b2e7690d366b92407c1845095feccc29b059a05), [b/293510459](https://issuetracker.google.com/issues/293510459))
- Removed macrobenchmark NOT-PROFILEABLE error on API 31+, and skip profileable check on eng/userdebug rooted devices. ([I2abac](https://android-review.googlesource.com/#/q/I2abac3fea3fb6eec37c50c774d7fe034abe6bc18), [b/291722507](https://issuetracker.google.com/issues/291722507))
- When using Dex Layout Optimizations, startup profile rules are also now considered as baseline profile rules. ([aosp/2684246](https://android.googlesource.com/platform/frameworks/support/+/1aa59a271e2157e2882838da24858cd05ee296fd), [b/293889189](https://issuetracker.google.com/issues/293889189))

### Version 1.2.0-beta02

July 26, 2023

`androidx.benchmark:benchmark-*:1.2.0-beta02` is released. [Version 1.2.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c2c1745b1d05b772c7bbe82834a9197ba5b85114..d0e769360e8a16c7f813af4eb2c79d700f6b52a3/benchmark)

**API Changes**

- Added experimental APIs for microbench custom metrics and configuration (e.g. profiler, and tracing). ([I86101](https://android-review.googlesource.com/#/q/I86101b06f608d0c6ee4945fa25b3cc7c377a745c), [b/291820856](https://issuetracker.google.com/issues/291820856))

**Bug Fixes**

- Report error in macrobench when OS is misconfigured for tracing, as was recently fixed in API 26/28 ARM64 emulators. ([I0a328](https://android-review.googlesource.com/#/q/I0a328b08a0ef4b356d3d7b593dbb89e47d00815e), [b/282191686](https://issuetracker.google.com/issues/282191686))
- Added detail to compilation reset failure to suggest updating emulator, as some emulators have recently fixed this issue. ([I8c815](https://android-review.googlesource.com/#/q/I8c81570e0b2e03b9f6453e13f0706b10f59f0455), [b/282191686](https://issuetracker.google.com/issues/282191686))
- Make `androidx.test.uiautomator:uiautomator:2.2.0` an `api` instead of an `implementation` dependency. ([I1981e](https://android-review.googlesource.com/#/q/I1981ef1fcbd7aa5fe9a75568b6df826f77a0335a))

### Version 1.2.0-beta01

July 18, 2023

`androidx.benchmark:benchmark-*:1.2.0-beta01` is released. [Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3b5b931546a48163444a9eddc533489fcddd7494..c2c1745b1d05b772c7bbe82834a9197ba5b85114/benchmark)

**Bug Fixes**

- Fix warnings being sometimes suppressed in Benchmark output in Studio, and workaround leading whitespaces from Benchmark output not showing up in Studio ([Ia61d0](https://android-review.googlesource.com/#/q/Ia61d0fdc52ca0de2ece777ea6dd76bc77876fcf2), [b/227205461](https://issuetracker.google.com/issues/227205461), [b/286306579](https://issuetracker.google.com/issues/286306579), [b/285912360](https://issuetracker.google.com/issues/285912360))
- Fixed comment for `FrameTimingMetric`. The submetric is named `frameDurationCpuMs`. ([Ib097f](https://android-review.googlesource.com/#/q/Ib097f4f633ede0f2932aaaff7c9d5dbbb74daf88), [b/288830934](https://issuetracker.google.com/issues/288830934)).

### Version 1.2.0-alpha16

June 21, 2023

`androidx.benchmark:benchmark-*:1.2.0-alpha16` is released. [Version 1.2.0-alpha16 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8423c3f497cfbf2bf7b87006ca05f38626060135..3b5b931546a48163444a9eddc533489fcddd7494/benchmark)

**API Changes**

- `BaselineProfileRule.collectBaselineProfile()` API has been renamed to `BaselineProfileRule.collect()`. ([I4b665](https://android-review.googlesource.com/#/q/I4b66589863999d3b3b018f22997a7736d5edc1bf))

**Bug Fixes**

- Macrobenchmark support for `androidx.benchmark.profiling.mode = MethodTracing`. ([I7ad37](https://android-review.googlesource.com/#/q/I7ad37bee17646cfef1564c9f0c84d20923d63ed9), [b/285912360](https://issuetracker.google.com/issues/285912360))
- Microbenchmark profiling moved to a separate phase, so it occurs in sequence *after* measurement, instead of replacing it. `MethodTracing` trace sections are also now included in the captured Perfetto trace, if present. ([I9f657](https://android-review.googlesource.com/#/q/I9f6573ccd97ed3079be46a95962728a6c428fe85), [b/285014599](https://issuetracker.google.com/issues/285014599))
- Add count measurement to `TraceSectionMetric` with `Mode.Sum`. ([Ic121a](https://android-review.googlesource.com/#/q/Ic121ac1432a973413b5318ccf5df6a2e1556419a), [b/264398606](https://issuetracker.google.com/issues/264398606))

### Version 1.2.0-alpha15

June 7, 2023

`androidx.benchmark:benchmark-*:1.2.0-alpha15` is released. [Version 1.2.0-alpha15 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6f3ac2bd197d5e61ab2708125b57d6ae4003ad68..8423c3f497cfbf2bf7b87006ca05f38626060135/benchmark)

**New Features**

- Added experimental `MemoryUsageMetric` for tracking memory usage of a target application. ([I56453](https://android-review.googlesource.com/#/q/I564531163aae2fa317d68a0676cfaf3068d12ee5), [b/133147125](https://issuetracker.google.com/issues/133147125), [b/281749311](https://issuetracker.google.com/issues/281749311))
- Add support for fully custom Perfetto configs with `PerfettoTrace.record` ([If9d75](https://android-review.googlesource.com/#/q/If9d752af8dd395b903f7530f393b1bb0b3fb3441), [b/280460183](https://issuetracker.google.com/issues/280460183))
- Added property to skip baseline profile generation. Usage: `./gradlew assemble -Pandroidx.baselineprofile.skipgeneration`. ([I37fda](https://android-review.googlesource.com/#/q/I37fda3f4b5761d8229c83be7d7a2cda197e8dbc8), [b/283447020](https://issuetracker.google.com/issues/283447020))

**API Changes**

- The `collectBaselineProfile` API always generates stable baseline profiles. The `collectStableBaselineProfile` API has been removed and `collectBaselineProfile` should be used instead. ([I17262](https://android-review.googlesource.com/#/q/I1726295116bbecbcbc72561aee96538c1ea9a514), [b/281078707](https://issuetracker.google.com/issues/281078707))
- Changed `BaselineProfileRule`'s `filterPredicate` arg to non-null, with a equivalent default value so that the default filter behavior is more clear in docs. ([I3816e](https://android-review.googlesource.com/#/q/I3816e294acb3fd7b6a1e1ec646c6e717f15c2549))

**Bug Fixes**

- Disable `IsolationActivity` and Perfetto tracing in `dryRunMode` to significantly improve performance, as these were majority of runtime. ([Ie4f7d](https://android-review.googlesource.com/#/q/Ie4f7deac2b04002199ece5f72161b69af5a35425))
- Support for call stack sampling in Macrobenchmarks using instrumentation test arguments `androidx.benchmark.profiling.mode=StackSampling` and `androidx.benchmark.profiling.sampleFrequency`. ([I1d13b](https://android-review.googlesource.com/#/q/I1d13b9bae8d4511946ec9914e48e160f17a3bd3f), [b/282188489](https://issuetracker.google.com/issues/282188489))
- Fixes crash when dropping shaders on Android U (API 34), as well as on emulators. ([I031ca](https://android-review.googlesource.com/#/q/I031ca38e15b9412e84a33eee4eb709cbf3014066), [b/274314544](https://issuetracker.google.com/issues/274314544))

### Version 1.2.0-alpha14

May 3, 2023

`androidx.benchmark:benchmark-*:1.2.0-alpha14` is released. [Version 1.2.0-alpha14 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..6f3ac2bd197d5e61ab2708125b57d6ae4003ad68/benchmark)

**Bug Fixes**

- Fix `FrameTimingMetric` ignoring frames with inconsistent frame IDs. This would cause some animations on recent platform versions (API 31+) to ignore many frames while `RenderThread` was animating (e.g. during a ripple). ([I747d2](https://android-review.googlesource.com/#/q/I747d23e6f5f38eda2c51ee3d26929fa4130e297c), [b/279088460](https://issuetracker.google.com/issues/279088460))
- Fixed trace processor parsing for traces larger than 64Mb. ([Ief831](https://android-review.googlesource.com/#/q/Ief831b2c58ebfeac3ae5cb2bfcb8623b920ad356), [b/269949822](https://issuetracker.google.com/issues/269949822))
- Fixed baseline profile generation on Android U failing because of the different output of `pm dump-profiles` command. ([Id1392](https://android-review.googlesource.com/#/q/Id1392207ec545dc4b095c4b435a92bb2a1ff0c66), [b/277645214](https://issuetracker.google.com/issues/277645214))
- Fix GPU clock locking script to compare strings correctly ([I53e54](https://android-review.googlesource.com/#/q/I53e5416ca2b24933a3d6d43db678dad035132dd2), [b/213935715](https://issuetracker.google.com/issues/213935715))

### Version 1.2.0-alpha13

April 5, 2023

`androidx.benchmark:benchmark-*:1.2.0-alpha13` is released. [Version 1.2.0-alpha13 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..a200cb82769634cecdb118ec4f0bfdf0b086e597/benchmark)

**API Changes**

- Added profile type parameter when generating baseline profiles to support upcoming startup profile feature ([Ie20d7](https://android-review.googlesource.com/#/q/Ie20d730efea37940bf9df519c86cdb29a4074d34), [b/275093123](https://issuetracker.google.com/issues/275093123))
- Added new experimental `TraceMetric` API for defining fully custom metrics based on content of a Perfetto trace. ([I4ce31](https://android-review.googlesource.com/#/q/I4ce3147b5bd1a13ae6a500389abdae3df461cacd), [b/219851406](https://issuetracker.google.com/issues/219851406))
- Add an experimental metric to determine the number of page faults during a benchmark. ([I48db0](https://android-review.googlesource.com/#/q/I48db0fe0dcc3ee0119b078e15b32d56c2361a838))

### Version 1.2.0-alpha12

March 22, 2023

`androidx.benchmark:benchmark-*:1.2.0-alpha12` is released. [Version 1.2.0-alpha12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e5004231d20c419159b85e5d668a0b7fd5199811..5e7d256f82fbafb6d059ab7b18fddd87c7531553/benchmark)

**New Features**

- The new baseline profile gradle plugin is released in alpha version, making it easier to generate a baseline profile and simplifying the developer workflow.

**API Changes**

- Removed Perfetto tracing support on API 21 and 22, which includes both Microbenchmarks and the experimental `PerfettoTrace` APIs. Prior to this version, `UiAutomation` connections were unreliable on some devices. ([I78e8c](https://android-review.googlesource.com/#/q/I78e8c6a08bb37ba4d7bbe48a474f725cedfafc85))
- Added public experimental API for `PerfettoTraceProcessor` to enable parsing trace content. This is a step toward fully custom metrics based on Perfetto trace data. ([I2659e](https://android-review.googlesource.com/#/q/I2659e84e85281f62f77abb6806f9c00bc2442f56), [b/219851406](https://issuetracker.google.com/issues/219851406))

### Version 1.2.0-alpha11

March 8, 2023

`androidx.benchmark:benchmark-*:1.2.0-alpha11` is released. [Version 1.2.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/87533b4ff06971ed59028936cd9b6da988cd4522..e5004231d20c419159b85e5d668a0b7fd5199811/benchmark)

**Bug Fixes**

- Fixed crashes in `MacrobenchmarkRule` and `BaselineProfileRule` when reinstalling or extracting profiles from an app bundle with multiple APKs. ([I0d8c8](https://android-review.googlesource.com/#/q/I0d8c8a50daee8ef3951a5d0266b5767f65fad4e7), [b/270587281](https://issuetracker.google.com/issues/270587281))

### Version 1.2.0-alpha10

February 22, 2023

`androidx.benchmark:benchmark-*:1.2.0-alpha10` is released. [Version 1.2.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/adf1c279a86ab3886e1666c08e2c3efba783367b..87533b4ff06971ed59028936cd9b6da988cd4522/benchmark)

**New Features**

- On Android 14+, Macrobenchmark no longer reinstalls target applications to reset compilation state, thanks to a new platform feature. Previously it was necessary to have a rooted device, or to deal with all application state (e.g. user login) being removed before each benchmark runs. ([I9b08c](https://android-review.googlesource.com/#/q/I9b08cfecc36735d057b388e75d1c9b50b53ed083), [b/249143766](https://issuetracker.google.com/issues/249143766))

**Bug Fixes**

- Fix `DryRunMode` to no longer crash with empty profile, due to compilation skipping. Instead, it runs a single iteration and extracts the profile to ensure something is captured. ([I2f05d](https://android-review.googlesource.com/#/q/I2f05dcb4b21b7bc1e3fc6262ab6106d383f885dc), [b/266403227](https://issuetracker.google.com/issues/266403227))
- Fix `PowerMetric` crash when checking for powerstats presence on old API levels. ([5faaf9](https://android-review.googlesource.com/#/q/306948d9069d67c4df87f863042d33ebbf5faaf9), [b/268253898](https://issuetracker.google.com/issues/268253898))

### Version 1.2.0-alpha09

January 11, 2023

`androidx.benchmark:benchmark-*:1.2.0-alpha09` is released. [Version 1.2.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4a2f5e696614339c1ac21f706c1a17c0285780e7..adf1c279a86ab3886e1666c08e2c3efba783367b/benchmark)

**Bug Fixes**

- Enabled passing `None` to `androidx.benchmark.enabledRules` instrumentation arg to disable all benchmarks / baseline profile generation. ([I3d7fd](https://android-review.googlesource.com/#/q/I3d7fd97e7a1ac46cf890d77501ba640bec8acb47), [b/258671856](https://issuetracker.google.com/issues/258671856))
- Fix `PerfettoTrace` capture in app modules (i.e. non-self-instrumenting test APKs) ([I12cfc](https://android-review.googlesource.com/#/q/I12cfc219b4d3deadd222995cd6f11b470f54956f))
- Fixed baseline profile adb pull argument order in Studio output ([I958d1](https://android-review.googlesource.com/#/q/I958d17f5f017a6774c8f35dd73bc6b1d25bbde61), [b/261781624](https://issuetracker.google.com/issues/261781624))
- Arm emulator api 33 is now correctly recognized as such when trying to run a macrobenchmark and will correctly print the warning. ([69133b](https://android.googlesource.com/platform/frameworks/support/+/69133b2c7390cb0a2f242737223f61ed0497deb2),[b/262209591](https://issuetracker.google.com/issues/262209591))
- Skip battery level check on devices without battery in Macrobenchmark ([fe4114](https://android.googlesource.com/platform/frameworks/support/+/fe4114abf03ac5ec371503cd9cbac4502f5388f4), [b/232448937](https://issuetracker.google.com/issues/232448937))

### Version 1.2.0-alpha08

December 7, 2022

`androidx.benchmark:benchmark-*:1.2.0-alpha08` is released. [Version 1.2.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a1e318590b217ecfce1b2de17eed2f18b6a680bb..4a2f5e696614339c1ac21f706c1a17c0285780e7/benchmark)

**API Changes**

- Added experimental new APIs `PerfettoTrace.record {}` and `PerfettoTraceRule` to capture Perfetto traces (also known as System Traces) as part of a test, to inspect test behavior and performance. ([I3ba16](https://android-review.googlesource.com/#/q/I3ba165beded0d8aabde791e3ac1b786d415404ed))
- `BaselineProfileRule` now accepts a filter predicate instead of a list of package prefixes. This gives the test full control on filtering. ([I93240](https://android-review.googlesource.com/#/q/I93240ab87438738dc1936a8a28de050002b34223))
- Add an experimental API `BaselineProfileRule.collectStableBaselineProfile` which waits until a baseline profile is stable for N iterations. ([I923f3](https://android-review.googlesource.com/#/q/I923f37dc420501c606e9a809e0711791055acac3))
- Add the ability to specify an output file name prefix when generating baseline profiles using `BaselineProfileRule`. ([I7b59f](https://android-review.googlesource.com/#/q/I7b59f0017e8556dbeb40433e96a17089bf09b2fc), [b/260318655](https://issuetracker.google.com/issues/260318655))

**Bug Fixes**

- Improve safety of file output writing, which should prevent output files from silently not being written / appended, especially on API 21/22. ([If8c44](https://android-review.googlesource.com/#/q/If8c444abd9115f214a84e15fbf93d8362d54e58f), [b/227510293](https://issuetracker.google.com/issues/227510293))
- Fix `simpleperf` trace output to create and place the file correctly. This should also more generally fix issues where a file is unsuccessfully pulled by gradle. ([I12a1c](https://android-review.googlesource.com/#/q/I12a1cda85c3fb4925c6875b6a738e96494eb5f80), [b/259424099](https://issuetracker.google.com/issues/259424099))
- Improve profileinstaller error message printed when profileinstaller is too old. This now tells you to update profileinstaller version (1.2.1) for measuring baseline profiles on API 31 through 33, instead of saying it's not supported. ([Ia517f](https://android-review.googlesource.com/#/q/Ia517fe8ffdcf09d3b24354253309983a99a6091f), [b/253519888](https://issuetracker.google.com/issues/253519888))
- Fix several shell command failures onerror message Print needed API \<=23, including failed perfetto capture binary setup and trace capture failures ([Ib6b87](https://android-review.googlesource.com/#/q/Ib6b872bca51c04c69a454dc1d896d3d7200abcc0), [b/258863685](https://issuetracker.google.com/issues/258863685))
- Automatically sort generated profile rules to minimize the number of changes as they change over time (when checking-in profile rules into source control). ([Ie2509](https://android-review.googlesource.com/#/q/Ie2509e9680444645162e583ea6247d3c2f8063c4))
- Fixed crash on unrooted builds below Android 13 (API 33) with message `Expected no stderr from echo 3 > /proc/sys/vm/drop_caches` ([I6c245](https://android-review.googlesource.com/#/q/I6c2454926a9f73b665e7ec8f349ad21afe1f94b5), [b/259508183](https://issuetracker.google.com/issues/259508183))

**Known Issues**
- `MacrobenchmarkScope.dropShaderCache()` may crash due to a missing broadcast registry in profileinstaller manifest, which has not yet been released. ([I5c728](https://android-review.googlesource.com/#/q/I5c728449d99419a7599451414fe09f82c5970d3d), [b/258619948](https://issuetracker.google.com/issues/258619948)) To workaround the issue in `profileinstaller:1.3.0-alpha02`, add the following to your application's (not your benchmark's) AndroidManifest.xml:

      <!-- workaround bug in profileinstaller 1.3.0-alpha02, remove when updating to alpha03+ -->
      <receiver
        android:name="androidx.profileinstaller.ProfileInstallReceiver"
        android:permission="android.permission.DUMP"
        android:exported="true">
        <intent-filter>
            <action android:name="androidx.profileinstaller.action.BENCHMARK_OPERATION" />
        </intent-filter>
      </receiver>

### Version 1.2.0-alpha07

November 9, 2022

`androidx.benchmark:benchmark-*:1.2.0-alpha07` is released. [Version 1.2.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/548c8ac2570ae6cf15798fea1380491f7d93796b..a1e318590b217ecfce1b2de17eed2f18b6a680bb/benchmark)

**API Changes**

- Adds `PowerMetric` API for measuring energy and power in Macrobenchmarks. ([Ife601](https://android-review.googlesource.com/#/q/Ife60176ae827bef14c86b1604b146e7b1208c439), [b/220183779](https://issuetracker.google.com/issues/220183779))
- Fixed `MacrobenchmarkScope.dropShaderCache()` to actually drop the shader cache. This removes roughly 20ms of noise from `StartupMode.COLD` benchmarks, as shaders are now consistently cleared each iteration. Previously, `Partial` compilation using warmup iterations would report incorrectly fast numbers, as shader caching was more likely to happen during warmup. This fix requires either a rooted device, or using `profileinstaller:1.3.0-alpha02` in the target app. For `ProfileInstaller` library's API changes, please refer to [ProfileInstaller 1.30-alpha02](https://developer.android.com/jetpack/androidx/releases/profileinstaller#1.3.0-alpha02) page. ([Ia5171](https://android-review.googlesource.com/#/q/Ia5171b0f40dd8ce6f64f5ccf0a33281a4d8b121e), [b/231455742](https://issuetracker.google.com/issues/231455742))
- Added `TraceSectionMode("label", Mode.Sum)`, allowing measurement of total time spent on multiple trace sections with the same label. For instance, `TraceSectionMetric("inflate", Mode.Sum)` will report a metric `inflateMs` for the total time in a macrobenchmark spent on inflation. Also removed API 29 requirement, as `TraceSectionMetric` works together with `androidx.tracing.Trace` back to lower API levels, with the use of [`forceEnableAppTracing`](https://developer.android.com/reference/androidx/tracing/Trace#forceEnableAppTracing()) within the target app. ([Id7b68](https://android-review.googlesource.com/#/q/Id7b68e23f5ded4d20ab21771dbf9eb96d9dcfdb7), [b/231455742](https://issuetracker.google.com/issues/231455742))

**Bug Fixes**

- Improved safety of all internal shell commands by validating all output/errors. ([I5984d](https://android-review.googlesource.com/#/q/I5984d1f7f176e47445264998250add7c27c5418c), [b/255402908](https://issuetracker.google.com/issues/255402908), [b/253094958](https://issuetracker.google.com/issues/253094958))
- Specify device in baseline profile `adb pull` command, so the pull command can be simply copied if multiple devices are connected (up to one emulator) ([I6ac6c](https://android-review.googlesource.com/#/q/I6ac6c7d2bbd9888dd889b1b790ba21795464f4fa), [b/223359380](https://issuetracker.google.com/issues/223359380))
- Add error if macrobenchmark test apk isn't set up as self-instrumenting. This error prevents macrobenchmarking from within the target app's process. In process, macrobench wouldn't be able to compile/kill/cold start the app, or control its own permissions ([I4279b](https://android-review.googlesource.com/#/q/I4279be0297389eb2602651d0ac9bdaaf1cb65705))
- Fixed an issue in `measureRepeated()` where `StartupMode.COLD` wouldn't kill the target process after `setupBlock`. Now `setupBlock` interacting with the app will not leave the app process running, and an invalid cold start measurement. ([I8ebb7](https://android-review.googlesource.com/#/q/I8ebb7eecb507a247a17947e6886eb816f1f92040))

### Version 1.2.0-alpha06

October 24, 2022

`androidx.benchmark:benchmark-*:1.2.0-alpha06` is released. [Version 1.2.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4586cf6e518f0c59410ef2b291e34ff9fdcff4e1..548c8ac2570ae6cf15798fea1380491f7d93796b/benchmark)

**API Changes**

- `BaselineProfileRule` no longer requires root on Android 13 (API 33), and is no longer experimental. ([Ie0a7d](https://android-review.googlesource.com/#/q/Ie0a7d13cbe34476113bad955e47ed771d84e65a4), [b/250083467](https://issuetracker.google.com/issues/250083467), [b/253094958](https://issuetracker.google.com/issues/253094958))
  - This change also fixes how profiles from an app are flushed to disk on unrooted devices, but requires updating the target app's profileinstaller dependency.
  - To use `BaselineProfileRule` or `CompilationMode.Partial(warmupIterations)` on an unrooted device, you must also update your target app to use `androidx.profileinstaller.profileinstaller:1.3.0-alpha01`. This enables flushing the profile to disk correctly, so that it can be compiled/extracted.

**Bug Fixes**

- Fixes `SampledProfiling` crash on API 33+. ([I40743](https://android-review.googlesource.com/#/q/I40743831d240327bbf3d89d09f510d9db09e67c0), [b/236109374](https://issuetracker.google.com/issues/236109374))

### Version 1.2.0-alpha05

October 5, 2022

`androidx.benchmark:benchmark-*:1.2.0-alpha05` is released. [Version 1.2.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bdce26bd7556b92d2d4d2af3de881dd8e2c51459..4586cf6e518f0c59410ef2b291e34ff9fdcff4e1/benchmark)

**Bug Fixes**

- Fix frame breakdown in Studio system trace viewer for benchmark captured traces ([I3f3ae](https://android-review.googlesource.com/#/q/I3f3aeb22ec932674c0486fa4fe1e76da01954123), [b/239677443](https://issuetracker.google.com/issues/239677443))
- Correct `FrameTimingMetric` to list `FrameOverrun` as requiring API 31 instead of 29 ([I716dd](https://android-review.googlesource.com/#/q/I716dd1527f9f2101ef50e4439b380f8cea9173c9), [b/220702554](https://issuetracker.google.com/issues/220702554))
- Set iteration in `BaselineProfileRule`, and throw clearly if target package not installed (was already done for MacrobenchmarkRule). ([Ic09a3](https://android-review.googlesource.com/#/q/Ic09a3b654cdf60a3e73f5349b7cea1a4e337eae7), [b/227991471](https://issuetracker.google.com/issues/227991471))

### Version 1.2.0-alpha04

September 21, 2022

`androidx.benchmark:benchmark-*:1.2.0-alpha04` is released. [Version 1.2.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cce7b70f6a5ebf955cf748a73c18b63228b22c74..bdce26bd7556b92d2d4d2af3de881dd8e2c51459/benchmark)

**New Features**

- Add support for `dryRunMode.enable` instrumentation argument to macrobenchmark (already available in micro) for faster local development, and validating app automation (e.g. in presubmit). This overrides iterations to 1, skips compilation, suppresses all [configuration errors](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview#configuration-errors), and disables measurement .json file output. ([Ib51b4](https://android-review.googlesource.com/#/q/Ib51b446731deef7aec7ddd604f0f701e1b0d7feb), [b/175149857](https://issuetracker.google.com/issues/175149857))

  On Gradle command line:

      ./gradlew macrobenchmark:cC -P android.testInstrumentationRunnerArguments.androidx.benchmark.dryRunMode.enable=true

  In build.gradle:

      android {
          defaultConfig {
              testInstrumentationRunnerArgument 'androidx.benchmark.dryRunMode.enable', 'true'
          }
      }

**Bug Fixes**

- Fixed `StartupTimingMetric` to no longer require measured Activities to be launched through `MacrobenchmarkScope.startActivityAndWait()`. This means the metric can pick up launches from e.g. notifications, `Context.startActivity()`, in-app Activity based navigation, or shell commands. ([Ia2de6](https://android-review.googlesource.com/#/q/Ia2de6bc01cb697c016474ba364ef21a768b4e060), [b/245414235](https://issuetracker.google.com/issues/245414235))
- Fix bug where `startActivityAndWait` would timeout trying to wait for launch completion on emulators by reducing strictness of frame detection. ([Ibe2c6](https://android-review.googlesource.com/#/q/Ibe2c6c5519973f5c3311f4abb02e21c66a77bd2e), [b/244594339](https://issuetracker.google.com/issues/244594339), [b/228946895](https://issuetracker.google.com/issues/228946895))

### Version 1.2.0-alpha03

September 7, 2022

`androidx.benchmark:benchmark-*:1.2.0-alpha03` is released. [Version 1.2.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/dd1e45e8550560087f6447a34a9145048b5766f4..cce7b70f6a5ebf955cf748a73c18b63228b22c74/benchmark)

**New Features**

- Added experimental APIs for using `BenchmarkState` independently, separate from `BenchmarkRule` / `JUnit4`. ([Id478f](https://android-review.googlesource.com/#/q/Id478f193ede7bfe746439471da6b6ca46651a9dd), [b/228489614](https://issuetracker.google.com/issues/228489614))

**Bug Fixes**

- Added Leanback fallback for `startActivityAndWait`. ([01ed77](https://android-review.googlesource.com/#/q/01ed77e9aeafebf441ab9c4f1119f672796a72d2), [b/242899915](https://issuetracker.google.com/issues/242899915))

### Version 1.2.0-alpha02

August 24, 2022

`androidx.benchmark:benchmark-*:1.2.0-alpha02` is released. [Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a7f0710ad21f556f0dde9bf7bdab6d2135170fd4..dd1e45e8550560087f6447a34a9145048b5766f4/benchmark)

**API Changes**

- Default to `am force stop` for `MacrobenchmarkScope.killProcess()`, even when rooted, except during Baseline Profile generation. This can be overridden with an optional boolean argument. ([02cce9](https://android-review.googlesource.com/#/q/02cce9c2e6a1f33bed2606e35d55974b74929532), [b/241214097](https://issuetracker.google.com/issues/241214097))

**Bug Fixes**

- Support baseline profile generation for System apps. ([I900b8](https://android-review.googlesource.com/#/q/I900b8913cb154ee8acd0b9e001de2c290cc7962f), [b/241214097](https://issuetracker.google.com/issues/241214097))
- Support checking for ODPM power metrics on unrooted devices. ([a38c78](https://android-review.googlesource.com/#/q/a38c786b3acec5b7681af3fd2c2a17466069011f), [b/229623230](https://issuetracker.google.com/issues/229623230))

### Version 1.2.0-alpha01

July 27, 2022

`androidx.benchmark:benchmark-*:1.2.0-alpha01` is released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/69956fa74719518e58b93b55aab2f87546412ec4..a7f0710ad21f556f0dde9bf7bdab6d2135170fd4/benchmark)

**New Features**

- New tracing-perfetto-common component allowing tooling to enable Perfetto SDK tracing in an app that exposes it ([I2cc7f](https://android-review.googlesource.com/#/q/I2cc7fa6b77325f2bfb6337d47b8027e5699d7d6a))
- Added `androidx.benchmark.enabledRules` instrumentation argument to enable filtering macrobenchmark runs to just benchmarks, or just baseline profile generation. Pass in 'Macrobenchmark', or 'BaselineProfile' to just run one type of test, e.g. when just generating `BaselineProfiles` on an emulator. Comma-separated list also Supported. ([I756b7](https://android-review.googlesource.com/#/q/I756b7695adba25f31ca31a6408b14c8aeedfdf6a), [b/230371561](https://issuetracker.google.com/issues/230371561))

  E.g. in Your macrobenchmark's build.gradle:

      android {
          defaultConfig {
              testInstrumentationRunnerArgument 'androidx.benchmark.enabledRules', 'BaselineProfile'
          }
      }

  Or from the Gradle command line:

      ./gradlew macrobenchmark:cC -P android.testInstrumentationRunnerArguments.androidx.benchmark.enabledRules=BaselineProfile

**API Changes**

- Added new `PowerMetric` for measuring energy and power tasks in benchmarks. ([I9f39b](https://android-review.googlesource.com/#/q/I9f39b285c9758fc63737b9bc0f763004e00ab6b7), [b/220183779](https://issuetracker.google.com/issues/220183779))
- Added a new compilation mode `CompilationMode.Ignore` to skip profile reset and compilation. ([Ibbcf8](https://android-review.googlesource.com/#/q/Ibbcf8e8c627d227e0f290bddf464b67d9b6653bc), [b/230453509](https://issuetracker.google.com/issues/230453509))
- Added a new parameter to `BaselineProfileRule#collectBaselineProfile` to filter output file by package names ([If7338](https://android-review.googlesource.com/#/q/If7338bff7f7a1bde4daeff1af1f684985103012d), [b/220146561](https://issuetracker.google.com/issues/220146561))
- Enables developer to discharge device to measure power drain. ([I6a6cb](https://android-review.googlesource.com/#/q/I6a6cb257c89dfd585fbb3369fe5ef021ffa0dae6))
- Added the ability to clear shader cache in `MacrobenchmarkScope`. ([I32122](https://android-review.googlesource.com/#/q/I3212295da7acc1abba7a85b74d9a79dbc2dac15c))
- Enables developer to configure display of metric type and detail desired subsystem categories. ([I810c9](https://android-review.googlesource.com/#/q/I810c934554d25e107cf01bd90c5c922991b238b2))
- Previously an `UnsupportedOperationException` was thrown in the benchmark if run on an unsupported device. Now UOE only occurs if the metric is used on the unsupported device (ie: `PowerMetric.configure`). ([I5cf20](https://android-review.googlesource.com/#/q/I5cf2004861662d9a751847ed4457178d36b8980f), [b/227229375](https://issuetracker.google.com/issues/227229375))
- Added `TotalPowerMetric` and `TotalEnergyMetric` for measuring total power and energy in each system category in macrobenchmarks. ([I3b26b](https://android-review.googlesource.com/#/q/I3b26bad74b0607e06435d2443ac616a7975a4d84), [b/224557371](https://issuetracker.google.com/issues/224557371))

**Bug Fixes**

- Fixed an issue where compiled methods were not correctly being reset between each macrobenchmark on unrooted builds. This unfortunately requires reinstalling the apk each iteration, which will clear application data for each macrobenchmark. ([I31c74](https://android-review.googlesource.com/#/q/I31c740019640da0d0913066bb9ac59ab5c2a9627), [b/230665435](https://issuetracker.google.com/issues/230665435))
- Fix trace recording crash on API 21/22 ([If7fd6](https://android-review.googlesource.com/#/q/If7fd6d645112295b63411f27e61b7c4ed33a4525), [b/227509388](https://issuetracker.google.com/issues/227509388), [b/227510293](https://issuetracker.google.com/issues/227510293), [b/227512788](https://issuetracker.google.com/issues/227512788))
- Overhaul activity launch completion detection to fix 'Unable to read any metrics' exception in startup macrobenchmarks. ([Ia517c](https://android-review.googlesource.com/#/q/Ia517c59c07d9c24e4471e86fb603dca56a6f855f))

## Version 1.1.1

### Version 1.1.1

November 9, 2022

`androidx.benchmark:benchmark-*:1.1.1` is released. [Version 1.1.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/69956fa74719518e58b93b55aab2f87546412ec4..9be9b55a7576c208b79da083ca7e40f7fc8e4596/benchmark)

**Bug Fixes**

- Fixes `android.system.ErrnoException: open failed: EACCES` which would occur on some Android11 (API 30)+ devices. This is a cherry-pick of a fix from `1.2.0-alpha01`. ([aosp/2072249](https://android-review.googlesource.com/c/platform/frameworks/support/+/2072249))

## Version 1.1.0

### Version 1.1.0

June 15, 2022

`androidx.benchmark:benchmark-*:1.1.0` is released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0456df6ed2f0c42f907084cc9796b95f3ef525e4..69956fa74719518e58b93b55aab2f87546412ec4/benchmark)

- This version is identical to `androidx.benchmark:benchmark-*:1.1.0-rc03`.

**Important changes since 1.0.0**

- Support for Jetpack Macrobenchmarks, which allows you to measure whole-app interactions like [startup](https://developer.android.com/reference/androidx/benchmark/macro/StartupTimingMetric) and [scrolling](https://developer.android.com/reference/androidx/benchmark/macro/FrameTimingMetric), provides the [ability to capture traces](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics) \& [measure trace sections](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics#trace-section).

- Support for [Baseline Profiles](https://d.android.com/baselineprofiles)

  - [`CompilationMode.Partial`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/CompilationMode.Partial) to measure the effectiveness of Baseline Profiles.
  - [`@BaselineProfileRule`](https://developer.android.com/reference/androidx/benchmark/macro/junit4/BaselineProfileRule) to automatically generate Baseline profiles for a given critical user journey.
- Support for Allocation metrics \& [profiling](https://developer.android.com/benchmark#profiling) during Microbenchmark runs.

### Version 1.1.0-rc03

June 1, 2022

`androidx.benchmark:benchmark-*:1.1.0-rc03` is released. [Version 1.1.0-rc03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7b763db64a7c0867291eb3b155da3b7fe1f7af5a..0456df6ed2f0c42f907084cc9796b95f3ef525e4/benchmark)

**Bug Fixes**

- Avoid reinstalling the target package on every benchmark iteration. ( [aosp/​​2093027](https://android-review.googlesource.com/c/platform/frameworks/support/+/2093027), [b/231976084](https://issuetracker.google.com/issues/231976084))

- Remove the `300ms` delay from `pressHome()`. ([aosp/2086030](https://android-review.googlesource.com/c/platform/frameworks/support/+/2086030/), [b/231322975](https://issuetracker.google.com/issues/231322975))

- Improve Macrobenchmark iteration speed by optimizing Shell commands used under the hood. ([aosp/2086023](https://android-review.googlesource.com/c/platform/frameworks/support/+/2086023), [b/231323582](https://issuetracker.google.com/issues/231323582))

- Support for Managed Gradle Devices when generating Baseline Profiles with Macrobenchmarks. ([aosp/2062228](https://android-review.googlesource.com/c/platform/frameworks/support/+/2062228), [b/228926421](https://issuetracker.google.com/issues/228926421))

### Version 1.1.0-rc02

May 11, 2022

`androidx.benchmark:benchmark-*:1.1.0-rc02` is released. [Version 1.1.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c132bd2ce9a7b1cae3d8035d59d3dde892d6a121..7b763db64a7c0867291eb3b155da3b7fe1f7af5a/benchmark)

- Note that this release includes a behavior change, as apps are now fully reinstalled in between each benchmark to ensure accurate measurements.

**Bug Fixes/Behavior Changes**

- Fixed an issue where app compilation was not correctly reset between macrobenchmarks, and not reset at all on unrooted builds. This fixes many cases where running multiple tests would result in `CompilationMode` having little to no effect on measurements. To workaround this problem, the target app is now fully reinstalling each test method, which will clear application data between each macrobenchmark. ([I31c74](https://android-review.googlesource.com/#/q/I31c740019640da0d0913066bb9ac59ab5c2a9627), [b/230665435](https://issuetracker.google.com/issues/230665435))

- As this prevents apps from setting up state before tests, it is now possible to skip compilation / reinstallation to enable working around this. You can for example fully compile the target with a shell command `cmd package compile -f -m speed <package>`, and then bypass macrobenchmark's compilation step.

  E.g. in Your macrobenchmark's build.gradle:

      android {
          defaultConfig {
              testInstrumentationRunnerArgument 'androidx.benchmark.compilation.enabled, 'false'
          }
      }

  Or from the Gradle command line:

      ./gradlew macrobenchmark:cC -P android.testInstrumentationRunnerArguments.androidx.benchmark.compilation.enabled=false

- Made it possible to share a module between macrobenchmarks and baseline profile generating tests by adding `androidx.benchmark.enabledRules` instrumentation argument. Pass in 'Macrobenchmark', or 'BaselineProfile' to just run one type of test, e.g. when generating `BaselineProfiles` on an emulator. ([I756b7](https://android-review.googlesource.com/#/q/I756b7695adba25f31ca31a6408b14c8aeedfdf6a), [b/230371561](https://issuetracker.google.com/issues/230371561))

  E.g. in Your macrobenchmark's build.gradle:

      android {
          defaultConfig {
              testInstrumentationRunnerArgument 'androidx.benchmark.enabledRules', 'BaselineProfile'
          }
      }

  Or from the Gradle command line:

      ./gradlew macrobenchmark:cC -P android.testInstrumentationRunnerArguments.androidx.benchmark.enabledRules=BaselineProfile

### Version 1.1.0-rc01

April 20, 2022

`androidx.benchmark:benchmark-*:1.1.0-rc01` is released. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6055e4c5b3ffb001b032c8e82f53e9c052611ac9..c132bd2ce9a7b1cae3d8035d59d3dde892d6a121/benchmark)

**Bug Fixes**

- Baseline profile output links in Android Studio now use a unique file name. This way the output always reflects the latest results of using a `BaselineProfileRule`. ( [aosp/2057008](https://android-review.googlesource.com/c/platform/frameworks/support/+/2057008), [b/228203086](https://issuetracker.google.com/issues/228203086) )

### Version 1.1.0-beta06

April 6, 2022

`androidx.benchmark:benchmark-*:1.1.0-beta06` is released. [Version 1.1.0-beta06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e8cd367922a88feb90c1ec59ea14c65f339c0de..6055e4c5b3ffb001b032c8e82f53e9c052611ac9/benchmark)

**Bug Fixes**

- Fix trace recording crash on API 21/22 ([If7fd6](https://android-review.googlesource.com/#/q/If7fd6d645112295b63411f27e61b7c4ed33a4525), [b/227509388](https://issuetracker.google.com/issues/227509388))
- Overhaul activity launch completion detection to fix 'Unable to read any metrics' exception in startup macrobenchmarks. ([Ia517c](https://android-review.googlesource.com/#/q/Ia517c59c07d9c24e4471e86fb603dca56a6f855f))
- Fix startup metrics for Macrobenchmarks when `CompilationMode.None()` is used. Before this change, `CompilationMode.Partial()` would appear to be slower than `Compilation.None()`. ([611ac9](https://android-review.googlesource.com/c/platform/frameworks/support/+/2052357)).

### Version 1.1.0-beta05

March 23, 2022

`androidx.benchmark:benchmark-*:1.1.0-beta05` is released. [Version 1.1.0-beta05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/39a48a4e0a2478359e60946680f7f77a4680f6df..1e8cd367922a88feb90c1ec59ea14c65f339c0de/benchmark)

**Bug Fixes**

- Kill package after skipping profile installation when using [`CompilationMode.None`](https://developer.android.com/reference/androidx/benchmark/macro/CompilationMode.None). ([aosp/1991373](https://android-review.googlesource.com/c/platform/frameworks/support/+/1991373))
- Fixed an issue where Macrobenchmarks is unable to collect startup metrics when using`StartupMode.COLD`. ([aosp/2012227](https://android-review.googlesource.com/c/platform/frameworks/support/+/2012227) [b/218668335](https://issuetracker.google.com/issues/218668335))

### Version 1.1.0-beta04

February 23, 2022

`androidx.benchmark:benchmark-*:1.1.0-beta04` is released. [Version 1.1.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db2ecbef194afcddfaede22e1d884a8959a9277c..39a48a4e0a2478359e60946680f7f77a4680f6df/benchmark)

**Bug Fixes**

- Fix missing metrics on Android 10, and
  `NoSuchElementException` caused by process names not being captured
  correctly in traces. ([Ib4c17](https://android-review.googlesource.com/#/q/Ib4c173655d87ff8f5a8dd9959e6639fbb66e0ecd), [b/218668335](https://issuetracker.google.com/issues/218668335))

- Use `PowerManager` for thermal throttling detection on Q (API
  29) and higher. This significantly reduces frequency of false
  positives in thermal throttling detection (benchmark retry after 90
  second cooldown), and speeds up benchmarks significantly on user
  builds. It also provides throttle detection even when clocks are
  locked (if they're locked too high for the device's physical
  environment). ([I9c027](https://android-review.googlesource.com/#/q/I9c02781c91bb1f646f98d1c84f44fa16c6e5e7ba), [b/217497678](https://issuetracker.google.com/issues/217497678), [b/131755853](https://issuetracker.google.com/issues/131755853))

- Filter simpleperf sampled profiling to `measureRepeated` thread only to simplify inspection ([Ic3e12](https://android-review.googlesource.com/#/q/Ic3e12bb15660e78b63d23f070c2c5e676e744701), [b/217501939](https://issuetracker.google.com/issues/217501939))

- Support metrics from named UI subprocesses in multi-process apps ([Ice6c0](https://android-review.googlesource.com/#/q/Ice6c0360953f464641774b0a1056af7015ecf8de), [b/215988434](https://issuetracker.google.com/issues/215988434))

- Filter Baseline Profile rules to target Android 9 (SDK 28). [aosp/1980331](https://android-review.googlesource.com/c/platform/frameworks/support/+/1980331) [b/216508418](https://issuetracker.google.com/issues/216508418)

- Skip Profile Installation when using `Compilation.None()`. Additionally, report warnings when the app is using an older version of `androidx.profileinstaller` and Android Gradle Plugin. [aosp/1977029](https://android-review.googlesource.com/c/platform/frameworks/support/+/1977029)

### Version 1.1.0-beta03

February 9, 2022

`androidx.benchmark:benchmark-*:1.1.0-beta03` is released. [Version 1.1.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9dceceb54300ed028a7e8fc7a3454f270337ffde..db2ecbef194afcddfaede22e1d884a8959a9277c/benchmark)

**API Changes**

- Added `AudioUnderrunMetric` into macrobenchmark library under experimental flag to allow detection of audio underruns ([Ib5972](https://android-review.googlesource.com/#/q/Ib5972944077ec4609d3e862dadf4cfedacaf1b11))
- `BaselineProfileRule` no longer accepts a `setup` block as this functioned the same as the `profileBlock`. ([Ic7dfe](https://android-review.googlesource.com/#/q/Ic7dfe2424734ceb106e01763ba5a2c4d1b195fcc), [b/215536447](https://issuetracker.google.com/issues/215536447))

  For e.g.

      @Test
      fun collectBaselineProfile() {
          baselineRule.collectBaselineProfile(
              packageName = PACKAGE_NAME,
              setupBlock = {
                  startActivityAndWait()
              },
              profileBlock = {
                  // ...
              }
          )
      }

      @Test
      fun collectBaselineProfile() {
          baselineRule.collectBaselineProfile(
              packageName = PACKAGE_NAME,
              profileBlock = {
                  startActivityAndWait()
                  // ...
              }
          )
      }

**Bug Fixes**

- Fixed issue where microbench profiler traces would fail to be updated in subsequent runs when linked in Studio output ([I5ae4d](https://android-review.googlesource.com/#/q/I5ae4d8eae1f463f75fcc43ceb751c01d4e5f4d8d), [b/214917025](https://issuetracker.google.com/issues/214917025))
- Prevent compilation shell commands on API 23 ([Ice380](https://android-review.googlesource.com/#/q/Ice3802adb7cdacdf675336b7d5029169e423f87e))
- Renamed `FrameCpuTime` -\> `FrameDurationCpu`, `FrameUiTime` -\> `FrameDurationUi` to clarify these are durations, not timestamps, and to match prefixes. ([I0eba3](https://android-review.googlesource.com/#/q/I0eba35542431905ab926f5dc7db4ab6e292fde69), [b/216337830](https://issuetracker.google.com/issues/216337830))

### Version 1.1.0-beta02

January 26, 2022

`androidx.benchmark:benchmark-*:1.1.0-beta02` is released. [Version 1.1.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d9b4f36e1191ffaa8744492ca8a3c3bd155324fc..9dceceb54300ed028a7e8fc7a3454f270337ffde/benchmark)

**Bug Fixes**

- Microbenchmark Stack Sampling / Method Tracing Profile results are now linked in Studio output, similar to other profiling outputs, and do not suppress the allocation metric. ([Idcb65](https://android-review.googlesource.com/#/q/Idcb65521f8f477be80455c8bbdd846eadd5bc2ce), [b/214440748](https://issuetracker.google.com/issues/214440748), [b/214253245](https://issuetracker.google.com/issues/214253245))
- BaselineProfileRule now prints the `adb pull` command in logcat and Studio output for pulling generated BaselineProfile text file. ([f08811](https://android-review.googlesource.com/#/q/748189b7ae0d235803fd247c6de6d3b624f08811))

### Version 1.1.0-beta01

January 12, 2022

`androidx.benchmark:benchmark-*:1.1.0-beta01` is released. [Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3ed0ccb23b6bea0fb5f2b0244dc2f1c351dc96f3..d9b4f36e1191ffaa8744492ca8a3c3bd155324fc/benchmark)

**Bug Fixes**

- Fixes profiler argument enable being ignored. ([I37373](https://android-review.googlesource.com/#/q/I373734dfa19f8afb3d0a963c597f8351eb74af36), [b/210619998](https://issuetracker.google.com/issues/210619998))
- Removed deprecated `CompliationModes` ([I98186](https://android-review.googlesource.com/#/q/I9818634d94ec91593110680369abdabfc49b15b7), [b/213467659](https://issuetracker.google.com/issues/213467659))
- Switched baseline profile arg of `CompilationMode.Partial` to enum for clarity. ([Id67ea](https://android-review.googlesource.com/#/q/Id67eaffdfc7246f3a9c45e89f72a2128ce2d4d78))

### Version 1.1.0-alpha13

December 15, 2021

`androidx.benchmark:benchmark-*:1.1.0-alpha13` is released. [Version 1.1.0-alpha13 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cc1240d00b28657ee0c1a937f60430eaf1b03b09..301586664b5aad60548f21866cad502d524dbf9f/benchmark)

**API Changes**

- Add low-overhead System Tracing to microbench output on Android Q (API 29+). Note that this does not currently capture custom tracing (via `android.os.Trace` or `androidx.tracing` Jetpack APIs) to avoid affecting results. This tracing should be useful in diagnosing instability, especially from sources outside the benchmark. ([I298be](https://android-review.googlesource.com/#/q/I298be3c9f9f7ef9ba1d2c63d79c864e8c8b16e04), [b/205636583](https://issuetracker.google.com/issues/205636583), [b/145598917](https://issuetracker.google.com/issues/145598917))
- Clarify `CompilationModes` into three classes - Full, None, Partial. Previously they were inconsistently named after compilation arguments (which we now treat as implementation details) and features. This makes the tradeoffs, potential combinations, and behavior across platform versions more clear. ([I3d7bf](https://android-review.googlesource.com/#/q/I3d7bf0f3ce65ebe2cf464a4d88d3d1a98a014215), [b/207132597](https://issuetracker.google.com/issues/207132597))
- Setup and measure are now always in pairs, in order. You can now query the package name and iteration (though the iteration may be `null` in certain warmup scenarios). ([Id3b68](https://android-review.googlesource.com/#/q/Id3b68c2d02163c97614f9cf20beb1dc2b449cd59), [b/208357448](https://issuetracker.google.com/issues/208357448), [b/208369635](https://issuetracker.google.com/issues/208369635))

**Bug Fixes**

- Fixed `CompilationMode.Speed` incorrectly treated as `None` ([I01137](https://android-review.googlesource.com/#/q/I011378d9c24cba60f15802b38f918d3ce33cf607))

### Version 1.1.0-alpha12

November 17, 2021

`androidx.benchmark:benchmark-*:1.1.0-alpha12` is released. [Version 1.1.0-alpha12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f07d12061370a603549747200c79b60239706330..cc1240d00b28657ee0c1a937f60430eaf1b03b09/benchmark)

**New Features**

- Add experimental TraceSectionMetric for custom trace-based timing measurements. ([I99db1](https://android-review.googlesource.com/#/q/I99db1c735f639a626bdc023b477058bf24bb7602), [b/204572664](https://issuetracker.google.com/issues/204572664))

**Bug Fixes**

- Wake device each iteration, to ensure UI can be tested - requires lockscreen is disabled. ([Ibfa28](https://android-review.googlesource.com/#/q/Ibfa283d90c297d2a440ec9d4261887c75516d8cf), [b/180963442](https://issuetracker.google.com/issues/180963442))
- Fixes multiple crashes in StackSampling profiling mode on emulators and non-rooted devices ([Icdbda](https://android-review.googlesource.com/#/q/Icdbda7d0659aa07f1bdd47eb1b5234af7e714ce8), [b/202719335](https://issuetracker.google.com/issues/202719335))
- Removed 0.5 second sleep at the end of each iteration - if you see missing metrics with this change, please file a bug. ([Iff6aa](https://android-review.googlesource.com/#/q/Iff6aa112c49c005dfda274f8407c89e31f44d4ec))
- Reduce chances of dropped data, and lower memory overhead from tracing ([Id2544](https://android-review.googlesource.com/#/q/Id254422b83525f9d87a6bd359e2723601b510ab5), [b/199324831](https://issuetracker.google.com/issues/199324831), [b/204448861](https://issuetracker.google.com/issues/204448861))
- Reduce trace size by \~40% by switching to compact sched storage format. ([Id5fb6](https://android-review.googlesource.com/#/q/Id5fb6277cc37c303b62b0a8abb4adb19d40fcc5c), [b/199324831](https://issuetracker.google.com/issues/199324831))
- Updated implementations of startup metrics to always end at end of renderthread. This will be more contistent across platform versions, and more closely map to in-app measurements. ([Ic6b55](https://android-review.googlesource.com/#/q/Ic6b55121ce0f08a89665790e222587717478da1d))

### Version 1.1.0-alpha11

November 3, 2021

`androidx.benchmark:benchmark-*:1.1.0-alpha11` is released. [Version 1.1.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/31a8acd5d0aa030454712d3df1ec114631651ef3..f07d12061370a603549747200c79b60239706330/benchmark)

**API Changes**

- Macrobenchmark now has a `minSdkVersion` of `23`. ([If2655](https://android-review.googlesource.com/#/q/If265556949897999b3841e99bb59919fcdfa2c15))
- Adds a new experimental `BaselineProfileRule` which is capable of generating baseline profiles for app's critical user journey. Detailed documentation to follow. ([Ibbefa](https://android-review.googlesource.com/#/q/Ibbefa8ef27e60b6634f9c4a604db91ae715c69c5), [b/203692160](https://issuetracker.google.com/issues/203692160))
- Removes measureRepeated interface variant, which was added for java callers, as it caused ambiguity in completing/resolving the method. Java callers will again need to return Unit.Instance from measureRepeated. If this is an inconvenience, please file a bug, we can revisit this in a future version. ([Ifb23e](https://android-review.googlesource.com/#/q/Ifb23eaa6926a7375def8e5a3a63a4e951c19f0e0), [b/204331495](https://issuetracker.google.com/issues/204331495))

### Version 1.1.0-alpha10

October 27, 2021

`androidx.benchmark:benchmark-*:1.1.0-alpha10` is released. [Version 1.1.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db476cd663f3d4c2d60594fd492ec621639b2c72..31a8acd5d0aa030454712d3df1ec114631651ef3/benchmark)

**API Changes**

- Backport StartupTimingMetric to work back to API 23. This new implementation also better handles reportFullyDrawn() to wait until corresponding content has been rendered. ([If3ac9](https://android-review.googlesource.com/#/q/If3ac9a339bedbb61785c80ea78c0e7ae8f9018e9), [b/183129298](https://issuetracker.google.com/issues/183129298))
- Added JvmOverloads to multiple MacrobenchmarkScope methods for Java callers. ([I644fe](https://android-review.googlesource.com/#/q/I644fe5b1ba90200ae264e8dabd68ae27689befa8), [b/184546459](https://issuetracker.google.com/issues/184546459))
- Provide alternative MacrobenchmarkRule.measureRepeated function that uses a `Consumer<MacrobenchmarkScope>` for idiomatic usage in Java language. ([If74ab](https://android-review.googlesource.com/#/q/If74abe75c4b0defd0016acd3de20689cf604badd), [b/184546459](https://issuetracker.google.com/issues/184546459))

**Bug Fixes**

- Fix for traces not starting early enough, and missing metric data. This is expected to fix "Unable to read any metrics during benchmark" exceptions that were caused by the library itself. ([I6dfcb](https://android-review.googlesource.com/#/q/I6dfcbda59c6f5887433f3b1227613f8789ca6307), [b/193827052](https://issuetracker.google.com/issues/193827052), [b/200302931](https://issuetracker.google.com/issues/200302931))
- FrameNegativeSlack has been renamed to FrameOverrun to clarify its meaning - how much the frame went over its time budget. ([I6c2aa](https://android-review.googlesource.com/#/q/I6c2aa3a408b3cc455bcabcd1479933672f186636), [b/203008701](https://issuetracker.google.com/issues/203008701))

### Version 1.1.0-alpha09

October 13, 2021

`androidx.benchmark:benchmark-*:1.1.0-alpha09` is released. [Version 1.1.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9..db0888af4fa9a8eaeaf55cc1f120724bc67bdb20/benchmark)

**Bug Fixes**

- Support dropping Kernel page cache without root on API 31/S+, which will increase accuracy of [StartupMode.COLD](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/StartupMode#ENUM_VALUE:COLD) launches. ([Iecfdb](https://android-review.googlesource.com/#/q/Iecfdbd7b712ceaba109c7551c669845db1ff51b7), [b/200160030](https://issuetracker.google.com/issues/200160030))

### Version 1.1.0-alpha08

September 29, 2021

`androidx.benchmark:benchmark-*:1.1.0-alpha08` is released. [Version 1.1.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/47e81d1c497b8a57534a460c277855db1b0257ae..1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9/benchmark)

**API Changes**

- Enable scrolling macrobenchmarks to run back to API 23 ([If39c2](https://android-review.googlesource.com/#/q/If39c203832b9aed765aa05d7573eb9c88bf1dc70), [b/183129298](https://issuetracker.google.com/issues/183129298))
- Add new type of sampled metric to UI and JSON output, focused on percentiles of multiple samples per iteration. ([I56247](https://android-review.googlesource.com/#/q/I56247e421890537d27f1e3f284209aa590472377), [b/199940612](https://issuetracker.google.com/issues/199940612))
- Switch to floating point metrics throughout the benchmark libraries (truncated in the Studio UI). ([I69249](https://android-review.googlesource.com/#/q/I69249339c0a2ccedd015e45c6ab528cb114d7103), [b/197008210](https://issuetracker.google.com/issues/197008210))

### Version 1.1.0-alpha07

September 1, 2021

`androidx.benchmark:benchmark-*:1.1.0-alpha07` is released. [Version 1.1.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc..47e81d1c497b8a57534a460c277855db1b0257ae/benchmark)

**API Changes**

- Raised min API to 21 to reflect the intended lowest API level to be supported in the future. Current min API supported continues to be conveyed via RequiredApi(), and is currently 29 ([I440d6](https://android-review.googlesource.com/#/q/I440d67683d41150fc9dd84d4f0a7100f2c9f32bd), [b/183129298](https://issuetracker.google.com/issues/183129298))

**Bug Fixes**

- Fixes `ProfileInstaller` to make it easier for apps using baseline profiles to run MacroBenchmarks using `CompilationMode.BaselineProfile`. ([I42657](https://android-review.googlesource.com/#/q/I426579600594e238b5b46adc20a6d4b33da3bab5), [b/196074999](https://issuetracker.google.com/issues/196074999)) NOTE: requires also updating to `androidx.profileinstaller:profileinstaller:1.1.0-alpha04` or greater.
- `StartupMode.COLD` + `CompilationMode.None` benchmarks are now more stable. ([I770cd](https://android-review.googlesource.com/#/q/I770cd76def3add73a14bee1b6acb1deea8900e93), [b/196074999](https://issuetracker.google.com/issues/196074999))

### Version 1.1.0-alpha06

August 18, 2021

`androidx.benchmark:benchmark-*:1.1.0-alpha06` is released. [Version 1.1.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d725303accfa9be6d5c3d61c7603ed1b9a780cbd..1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc/benchmark)

**API Changes**

- Added `androidx.benchmark.iterations` instrumentation argument to allow manual overriding of iteration count when testing/profiling locally. ([6188be](https://android.googlesource.com/platform/frameworks/support/+/6188be16ae462fa0c42da6a7fa70d7d4b7cd42d3), [b/194137879](https://issuetracker.google.com/issues/194137879))

**Bug Fixes**

- Switched to Simpleperf as default sampling profiler on API 29+. ([Ic4b34](https://android-review.googlesource.com/#/q/Ic4b346221bb91dea1e7078e369f106f9e48be1e3), [b/158303822](https://issuetracker.google.com/issues/158303822))

**Known Issues**

- `CompilationMode.BaselineProfile` is a work in progress. Avoid using it to determine how good a profile is for now.

### Version 1.1.0-alpha05

August 4, 2021

`androidx.benchmark:benchmark-*:1.1.0-alpha05` is released. [Version 1.1.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ccf79f53033e665475116a4e78ff124df2a52c4b..d725303accfa9be6d5c3d61c7603ed1b9a780cbd/benchmark)

`1.1.0-alpha04` was cancelled before release due to a sporatic crash. [b/193827052](https://issuetracker.google.com/issues/193827052)

**API Changes**

- Switched [startActivityAndWait](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/MacrobenchmarkScope#startActivityAndWait(android.content.Intent)) to invoke launch via `am start`, which reduces the time of each measurement iteration by approximately 5 seconds, at the cost of no longer supporting intent parcelables. ([I5a6f5](https://android-review.googlesource.com/#/q/I5a6f55819fe095da1317b55405a6a5a9fe3cb758), [b/192009149](https://issuetracker.google.com/issues/192009149)

**Bug Fixes**

- Reduce aggressiveness of thermal throttle detection, and recompute baseline if throttles are detected frequently. ([I7327b](https://android-review.googlesource.com/#/q/I7327b4f1c15317fad28de1f06a148aad29c7cd4f))
- Fixes FrameTimingMetric to work on Android S beta ([Ib60cc](https://android-review.googlesource.com/#/q/Ib60ccf09fb2fa09f128374140c3657015626dd2c), [b/193260119](https://issuetracker.google.com/issues/193260119))
- Use an `EmptyActivity` to bring the target app out of a force-stopped state to better support `CompilationMode.BaselineProfile`. ([Id7cac](https://android-review.googlesource.com/#/q/Id7cac284a5a42f5aeaf92ba6522061f794afcc96), [b/192084204](https://issuetracker.google.com/issues/192084204))
- Changed trace file extension to `.perfetto-trace` to match platform standard. ([I4c236](https://android-review.googlesource.com/#/q/I4c236a26dfc5494415ee3f4d340329244a22c2b6), [b/174663039](https://issuetracker.google.com/issues/174663039))
- StartupTimingMetric now outputs the "fullyDrawnMs" metric to measure time until your application has completed rendering. To define this metric for your app, call Activity.reportFullyDrawn when your initial content is ready, such as when your initial list items are loaded from DB or network. (reportFullyDrawn method available without build version checks on ComponentActivity). Note that your test must run long enough to capture the metric (startActivityAndWait doesn't wait for reportFullyDrawn). ([If1141](https://android-review.googlesource.com/#/q/If1141474620b0f2d50f59801a1a8e1cac49ae51d), [b/179176560](https://issuetracker.google.com/issues/179176560))
- Reduce cost of appending Ui metadata to traces by 50+ ms ([Ic8390](https://android-review.googlesource.com/#/q/Ic839003ca1a321d56dca7686db29cb3c00c67fc5), [b/193923003](https://issuetracker.google.com/issues/193923003))
- Drastically increased polling frequency when stopping tracing, which can reduce e.g. startup benchmark runtime by 30+% ([Idfbc1](https://android-review.googlesource.com/#/q/Idfbc18c4c997d2d78292b14a44d405d11fe7b43e), [b/193723768](https://issuetracker.google.com/issues/193723768))

### Version 1.1.0-alpha03

June 16, 2021

`androidx.benchmark:benchmark-*:1.1.0-alpha03` is released. [Version 1.1.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/66681ad83c328d0dd821b943bb3d375f02c1db61..ccf79f53033e665475116a4e78ff124df2a52c4b/benchmark)

**New Features**

- Added a new `CompilationMode.BaselineProfile` to support profiles installed using the [Jetpack ProfileInstaller library](https://developer.android.com/jetpack/androidx/releases/profileinstaller). ([aosp/1720930](https://android-review.googlesource.com/c/platform/frameworks/support/+/1720930))

**Bug Fixes**

- The sample Gradle code for suppressing benchmark errors has been updated to use a non-deprecated API with a syntax that also supports .gradle.kts users.

  E.g.,

      testInstrumentationRunnerArguments["androidx.benchmark.suppressErrors"] = "EMULATOR,LOW-BATTERY"

### Version 1.1.0-alpha02

May 18, 2021

Benchmark version 1.1.0-alpha02 brings a big component to benchmarking - Macrobenchmark. In addition to *benchmark* allowing you to measure CPU loops, *macrobenchmark* allows you to measure whole-app interactions like startup and scrolling, and capture traces. For more information see the [library documentation](https://developer.android.com/benchmark).

`androidx.benchmark:benchmark-*:1.1.0-alpha02` is released. [Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/945594abd75f83bd14daf4fbcd8621796161281e..66681ad83c328d0dd821b943bb3d375f02c1db61/benchmark)

**New Features**

Macrobenchmark artifacts added (`androidx.benchmark:benchmark-macro-junit4` and `androidx.benchmark:benchmark-macro`)

- Capture startup, scrolling/animation performance metrics from your app, locally or in CI
- Capture and inspect traces from within Android Studio

**Bug Fixes**

- Workaround shell permissions issue with output directory on Android 12 (Note - may require updating Android Gradle Plugin to 7.0.0 canary and Android Studio to Arctic Fox (2020.3.1), to continue capturing output files on affected devices). ([Icb039](https://android-review.googlesource.com/#/q/Icb039cf7a41342b44cb2d79229898662ee76869e))
- Support configuration caching in BenchmarkPlugin ([6be1c1](https://android-review.googlesource.com/#/q/6be1c120b8c4cbf64c0ae7865780ebe39c1ba2be), [b/159804788](https://issuetracker.google.com/issues/159804788))
- Simplified file output - on by default, in a directory that doesn't require `requestLegacyExternalStorage=true` ([8b5a4d](https://android-review.googlesource.com/#/q/8b5a4df9f4344d8df875558c4b5cc5621ef3ffc8), [b/172376362](https://issuetracker.google.com/issues/172376362))
- Fixes library printing logcat warnings about not finding JIT thread on platform versions where it is not present. ([I9cc63](https://android-review.googlesource.com/#/q/I9cc637ed3d5ec50169f4bad795d47c4f2a03befa), [b/161847393](https://issuetracker.google.com/issues/161847393))
- Fix for reading device max frequency. ([I55c7a](https://android-review.googlesource.com/#/q/I55c7ade72e880d6b045ef6e24bc2a54b2d774acd))

### Version 1.1.0-alpha01

June 10, 2020

`androidx.benchmark:benchmark-common:1.1.0-alpha01`, `androidx.benchmark:benchmark-gradle-plugin:1.1.0-alpha01`, and `androidx.benchmark:benchmark-junit4:1.1.0-alpha01` are released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e4841066bef97212f3eeb84f894d36dc5a25f756..945594abd75f83bd14daf4fbcd8621796161281e/benchmark)

**New Features of 1.1**

- Allocation Metric - Benchmarks now run an additional phase after warmup and timing, capturing allocation counts. Allocations can cause performance problems on older versions of the platform (140ns in O became 8ns in M - measured on Nexus5X, with locked clocks). This metric is displayed in Android Studio console output, as well as in the
- [Profiling support](https://developer.android.com/benchmark#profiling) - You can now capture profiling data for a benchmark run, to inspect why your code may be running slowly. Benchmark supports capturing either method tracing, or method sampling from ART. These files can be inspected with the Profiler inside Android Studio using *File \> Open*.
- The Benchmark Gradle plugin now provides defaults for simpler setup:
  - `testBuildType` is set to release by default, to avoid using dependencies with code coverage built-in. The release buildType is also configured as the default buildType, which allows Android Studio to automatically select the correct build variant when opening a project for the first time. ([b/138808399](https://issuetracker.google.com/issues/138808399))
  - `signingConfig.debug` is used as the default signing config ([b/153583269](https://issuetracker.google.com/issues/153583269))

\*\* Bug Fixes \*\*

- Significantly reduced the warmup transition overhead, where the first measurement for each benchmark was artificially higher than others. This issue was more pronounced in very small benchmarks (1 microsecond or less). ([b/142058671](https://issuetracker.google.com/issues/142058671))
- Fixed `InstrumentationResultParser` error printed for each benchmark when running from command line. ([I64988](https://android-review.googlesource.com/#/q/I64988447a89d7e0314cedabf87812eaf6c413545), [b/154248456](https://issuetracker.google.com/issues/154248456))

**Known Issues**

- Command line, gradle invocations of Benchmark do not print out results directly. You can work around this by either running through Studio, or parsing the JSON output file for results.
- Benchmark reporting fails to pull the report from devices that have an app installed with an applicationId ending with either "android" or "download" (case insensitive). Users hitting this issue should upgrade the Android Gradle Plugin to 4.2-alpha01 or later.

## Version 1.0.0

### Benchmark Version 1.0.0

November 20, 2019

`androidx.benchmark:benchmark-common:1.0.0`, `androidx.benchmark:benchmark-gradle-plugin:1.0.0`, and `androidx.benchmark:benchmark-junit4:1.0.0` are released with no changes from 1.0.0-rc01. [Version 1.0.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/12751d3bc911509ac8f983745088c152fc999978..e4841066bef97212f3eeb84f894d36dc5a25f756/benchmark).

**Major features of 1.0.0**

The Benchmark library allows you to write performance benchmarks of app code and get results quickly.

It prevents build and runtime configuration issues and stabilizes device performance to ensure that measurements are accurate and consistent. Run the benchmarks [directly in Android Studio](https://developer.android.com/studio/profile/benchmark#run-benchmark), or [in Continuous Integration](https://developer.android.com/studio/profile/run-benchmarks-in-ci) to observe code performance over time, and to prevent regressions.

Major features include:

- [Clock stabilization](https://developer.android.com/studio/profile/benchmark#clock-stability)
- Automatic thread prioritization
- Support for UI performance testing, such as in the [RecyclerView Sample](https://github.com/android/performance-samples/tree/main/MicrobenchmarkSample)
- JIT-aware warmup and looping
- JSON benchmark output for post-processing

### Version 1.0.0-rc01

October 23, 2019

`androidx.benchmark:benchmark-common:1.0.0-rc01`, `androidx.benchmark:benchmark-gradle-plugin:1.0.0-rc01`, and `androidx.benchmark:benchmark-junit4:1.0.0-rc01` are released. [Version 1.0.0-rc01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/1c249aa2bda2320b9d136bfa1f5c9ca95e856efc..12751d3bc911509ac8f983745088c152fc999978/benchmark/).

**New features**

- Added systrace tracing to benchmarks

**Bug fixes**

- Fixed metric instability issue where JIT wouldn't finish before warm up due to deprioritization ([b/140773023](https://issuetracker.google.com/issues/140773023))
- Unified JSON output directory across Android Gradle Plugin 3.5 and 3.6

### Version 1.0.0-beta01

October 9, 2019

`androidx.benchmark:benchmark-common:1.0.0-beta01`, `androidx.benchmark:benchmark-gradle-plugin:1.0.0-beta01`, and `androidx.benchmark:benchmark-junit4:1.0.0-beta01` are released. [Version 1.0.0-beta01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/7ccc99ac1b0e06dbae4c0f30bbc06a6bae1889f6..1c249aa2bda2320b9d136bfa1f5c9ca95e856efc/benchmark).

**New features**

- Run garbage collection before each warmup to reduce memory pressure from one benchmark to leak to the next ([b/140895105](https://issuetracker.google.com/issues/140895105))

**Bug fixes**

- Added `androidx.annotation:android-experimental-lint` dependency, so that Java code will correctly produce lint errors when experimental API is not used, similar to what is provided by the Kotlin experimental annotation for Kotlin callers.
- Now correctly detects usage of `additionalTestOutputDir` instrumentation argument for output in Android Gradle Plugin 3.6, to know when AGP will handle data copy.
- Fix undetected clock frequency in JSON to correctly print `-1` ([b/141945670](https://issuetracker.google.com/issues/141945670)).

### Version 1.0.0-alpha06

September 18, 2019

`androidx.benchmark:benchmark-common:1.0.0-alpha06`, `androidx.benchmark:benchmark-gradle-plugin:1.0.0-alpha06`, and `androidx.benchmark:benchmark-junit4:1.0.0-alpha06` are released. [Version 1.0.0-alpha06 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/befedb9611cf6cd7fbf5f0d3e18f60c5facc1d31..7ccc99ac1b0e06dbae4c0f30bbc06a6bae1889f6/benchmark).

**New features**

- Added a check for incorrectly using the old package for the test runner, which now provides a more-helpful error message

**API changes**

- The experimental annotation `ExperimentalAnnotationReport` is now correctly public. Usage of the experimental [BenchmarkState#report](https://developer.android.com/reference/kotlin/androidx/benchmark/BenchmarkState#report) API now requires this annotation

### Version 1.0.0-alpha05

September 5, 2019

`androidx.benchmark:benchmark-common:1.0.0-alpha05`, `androidx.benchmark:benchmark-gradle-plugin:1.0.0-alpha05`, and `androidx.benchmark:benchmark-junit4:1.0.0-alpha05` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/a94f37182adc928f3f4bba0ffe8836866ecb2f21..befedb9611cf6cd7fbf5f0d3e18f60c5facc1d31/benchmark).

**API changes**

- `BenchmarkState.reportData` API is now marked experimental

**Bug fixes**

- Fix for the clock-locking script, which would fail on devices that were either missing the `cut` or `expr` shell utilities.
- Fixed an issue with `./gradlew lockClocks` task that would hang on devices that were rooted with an older version of the su utility, which did not support the `-c` flag.

### Version 1.0.0-alpha04

August 7, 2019

`androidx.benchmark:benchmark-common:1.0.0-alpha04`, `androidx.benchmark:benchmark-gradle-plugin:1.0.0-alpha04`, and `androidx.benchmark:benchmark-junit4:1.0.0-alpha04` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/e648705631f06c43be445aafdccd8f55121dce8d..a94f37182adc928f3f4bba0ffe8836866ecb2f21/benchmark).

New documentation has also been added for how to use the Benchmark library without Gradle, both for usage with different build systems (such as Bazel or Buck), and when running in CI. For more information, see [Build benchmarks without Gradle](https://developer.android.com/studio/profile/build-benchmarks-without-gradle) and [Run benchmarks in Continuous Integration](https://developer.android.com/studio/profile/run-benchmarks-in-ci).

**New features**

- Gradle plugin
  - Now automatically disables test coverage, and sets the `AndroidBenchmarkRunner` by default ([b/138374050](https://issuetracker.google.com/issues/138374050))
  - Added support for new AGP-based data copy, when running benchmarks and when using AGP 3.6+
- JSON format additions
  - Output total benchmark test run time ([b/133147694](https://issuetracker.google.com/issues/133147694))
  - `@Parameterized` benchmarks that use a name string (for example `@Parameters(name = "size={0},depth={1}")`) now output parameter names and values per benchmark in the JSON output ([b/132578772](https://issuetracker.google.com/issues/132578772))
- Dry Run mode ([b/138785848](https://issuetracker.google.com/issues/138785848))
  - Added a "dry run" mode for running each benchmark loop only once, to check for errors/crashes without capturing measurements. This can be useful e.g. for, for example, quickly running benchmarks in presubmit to check that they're not broken.

**API changes**

- Module structure has changed, splitting the library ([b/138451391](https://issuetracker.google.com/issues/138451391))
  - `benchmark:benchmark-junit4` contains classes with JUnit dependency: `AndroidBenchmarkRunner`, and `BenchmarkRule`, both of which have moved into the `androidx.benchmark.junit4` package
  - `benchmark:benchmark-common` contains the rest of the logic, including the BenchmarkState API
  - This split will allow the library to support benchmarking without JUnit4 APIs in the future
- Configuration warnings are now treated as errors, and will crash the test ([b/137653596](https://issuetracker.google.com/issues/137653596))
  - This is done to further encourage accurate measurements, especially in CI
  - These errors can be reduced back to warnings with an instrumentation argument. For example: `-e androidx.benchmark.suppressErrors "DEBUGGABLE,LOW_BATTERY"`

**Bug fixes**

- Errors when writing to external storage on Q devices provide more-descriptive messages, with suggestions of how to resolve the issue
- Screens are automatically turned on during benchmark runs, instead of failing when the screen is off

**External contributions**

- Thanks to Sergey Zakharov for contributing JSON output improvements and the fix for screen off issues!

### Version 1.0.0-alpha03

July 2, 2019

`androidx.benchmark:benchmark:1.0.0-alpha03` and `androidx.benchmark:benchmark-gradle-plugin:1.0.0-alpha03` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/a1664e857bbcb746318a95abefa845edd9c88bf8..e648705631f06c43be445aafdccd8f55121dce8d/benchmark).

**New features**

- Expose sleep duration due to thermal throttling per benchmark in the full JSON report

**Bug fixes**

- The Gradle plugin should no longer be required to be applied after Android plugins and the Android block
- Adds support for benchmark reports on Android 10 devices using scoped storage

### Version 1.0.0-alpha02

June 6, 2019

`androidx.benchmark:1.0.0-alpha02` and
`androidx.benchmark:benchmark-gradle-plugin:1.0.0-alpha02` are released. The
commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/a04120000a63645245f046b0aa7773cb2c6d9768..a1664e857bbcb746318a95abefa845edd9c88bf8/benchmark).

Note that we are treating the JSON schema as an API. We plan to follow the same
stability constraints as other APIs: stable (with very rare exceptions) once in
beta, and fixed in final release, with only additions in minor releases and
changes/removals in major releases.

**API changes**

- Overhauled JSON schema. Further changes to the JSON schema are likely to be
  limited to additions:

  - Reorganized the result object structure to support additional metric groups in the future ([b/132713021](https://issuetracker.google.com/issues/132713021))
  - Added test run context information, such as device and build info and whether clocks are locked, to the top-level object ([b/132711920](https://issuetracker.google.com/issues/132711920))
  - Time metric names now have 'ns' in their name ([b/132714527](https://issuetracker.google.com/issues/132714527))
  - Additional stats added per reported metric (maximum, median, minimum), and removed simplified 'nanos' summary stat ([b/132713851](https://issuetracker.google.com/issues/132713851))
- Removed XML output
  ([b/132714414](https://issuetracker.google.com/issues/132714414))

- Thermal throttle detection removed from `BenchmarkState.reportData` API
  ([b/132887006](https://issuetracker.google.com/issues/132887006))

**Bug fixes**

- Fixed `./gradlew lockClocks` not sticking on some recent OS devices ([b/133424037](https://issuetracker.google.com/issues/133424037))
- Throttling detection disabled for emulator ([b/132880807](https://issuetracker.google.com/issues/132880807))

### Version 1.0.0-alpha01

May 7, 2019

`androidx.benchmark:benchmark:1.0.0-alpha01` is released. The commits included
in this version are available
[here](https://android.googlesource.com/platform/frameworks/support/+log/a04120000a63645245f046b0aa7773cb2c6d9768/benchmark).