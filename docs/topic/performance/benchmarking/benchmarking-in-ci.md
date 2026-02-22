---
title: https://developer.android.com/topic/performance/benchmarking/benchmarking-in-ci
url: https://developer.android.com/topic/performance/benchmarking/benchmarking-in-ci
source: md.txt
---

You can run benchmarks in Continuous Integration (CI) to track performance over time and recognize performance regressions---or improvements---before your app even releases. This page provides basic information about benchmarking in CI.

Before getting started with benchmarking in CI, consider how capturing and evaluating results differs from regular tests.

### Fuzzy results

Although benchmarks are instrumented tests, results aren't just a pass or fail. Benchmarks provide timing measurements for the given device they run on. Graphing results over time lets you monitor change and observe noise in the measurement system.

### Use real devices

Run benchmarks on physical Android devices. While they can run on emulators, it's strongly discouraged because it doesn't represent a realistic user experience and instead provides numbers tied to the host OS and hardware capabilities. Consider using real devices or a service that lets you run tests on real devices, such as[Firebase Test Lab](https://firebase.google.com/products/test-lab).
| **Note:** Check the sample setup of Firebase Test Lab and Github Actions in our[samples](https://github.com/android/performance-samples/tree/main/MacrobenchmarkSample/ftl).

## Run the benchmarks

Running the benchmarks as part of your CI pipeline may be different than running it locally from Android Studio. Locally, you typically run the Android integration tests with one Gradle`connectedCheck`task. This task automatically builds your APK and test APK and runs the tests on the device(s) connected to the CI server. When running in CI, this flow usually needs to be split into separate phases.

### Build

For the Microbenchmark library, run the Gradle task`assemble[VariantName]AndroidTest`, which creates your test APK that contains both your application code as well as your tested code.

Alternatively, Macrobenchmark library requires you to build your target APK and test APK separately. Therefore run`:app:assemble[VariantName]`and`:macrobenchmark:assemble[VariantName]`Gradle tasks.

### Install and run

These steps are typically done without needing to run Gradle tasks. Note, they may be abstracted depending on whether you use a service that lets you run tests on real devices.

For installation, use the`adb install`command and specify the test APK or the target APK.

Run the`adb shell am`instrument command to run all the benchmarks:  

    adb shell am instrument -w com.example.benchmark/androidx.benchmark.junit4.AndroidBenchmarkRunner

When using the Macrobenchmark library, use regular`androidx.test.runner.AndroidJUnitRunner`as instrumentation runner.
| **Note:** Before version 1.1.0, the JSON output must be manually enabled by adding the instrumentation argument`-e "androidx.benchmark.output.enable" "true"`.

You can pass the same instrumentation arguments as in the Gradle configuration using`-e`argument. For all the instrumentation arguments options, see[Microbenchmark Instrumentation Arguments](https://developer.android.com/topic/performance/benchmarking/microbenchmark-instrumentation-args)or[Add instrumentation arguments](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-instrumentation-args)for Macrobenchmark.

For example, you can set the`dryRunMode`argument to run microbenchmarks as part of your pull request verification process. With this flag enabled, microbenchmarks run only in single loop, verifying they are running correctly but not taking too long to execute.  

    adb shell am instrument -w -e "androidx.benchmark.dryRunMode.enable" "true" com.example.benchmark/androidx.benchmark.junit4.AndroidBenchmarkRunner

For more information on how to run instrumentation tests from the command line, see[Run tests with ADB](https://developer.android.com/studio/test/command-line#run-tests-with-adb).

### Lock clocks

The Microbenchmark Gradle plugin provides the command`./gradlew lockClocks`to lock the CPU clocks of a rooted device. This is useful for ensuring stability when you have access to rooted devices, such as "userdebug" builds. You can replicate this with the`lockClocks.sh`shell script, available in the[library's source](https://android.googlesource.com/platform/frameworks/support/+/refs/heads/androidx-main/benchmark/gradle-plugin/src/main/resources/scripts/lockClocks.sh).
| **Note:** The lock clocking is only necessary for microbenchmarks.

You can either run the script directly from a Linux or Mac host, or you can push to the device with a few adb commands:  

```
adb push path/lockClocks.sh /data/local/tmp/lockClocks.sh
adb shell /data/local/tmp/lockClocks.sh
adb shell rm /data/local/tmp/lockClocks.sh
```

If you run the shell script directly on a host, it dispatches these commands to a connected device.

For more information on why it is helpful to lock the CPU clocks, see how to[obtain consistent benchmarks](https://developer.android.com/topic/performance/benchmarking/microbenchmark-overview#benchmark-consistency).

## Collect the results

The benchmarking libraries output measurements in[JSON](https://developer.android.com/topic/performance/benchmarking/benchmarking-in-ci#benchmark-data-example), along with profiling traces to a directory on the Android-powered device after each benchmark run.[Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)library outputs multiple perfetto trace files: one per measured iteration of each`MacrobenchmarkRule.measureRepeated`loop.[Microbenchmark](https://developer.android.com/topic/performance/benchmarking/microbenchmark-overview), however, creates just one trace file for all the iterations of each`BenchmarkRule.measureRepeated`.[Profiling](https://developer.android.com/topic/performance/benchmarking/microbenchmark-profile)trace files are also output to this same directory.

### Save and locate the files

If you run the benchmarks with Gradle, these files are automatically copied to your host computer's outputs directory under`build/outputs/connected_android_test_additional_output/debugAndroidTest/connected/`.

If running directly with the`adb`command, you need to pull the files manually. By default, the reports are saved on-device in the media directory of the tested app's external storage. For convenience, the library prints the path of the file into Logcat. Note, that the output folder may be different depending on which Android version the benchmarks are running on.  

    Benchmark: writing results to /storage/emulated/0/Android/media/com.example.macrobenchmark/com.example.macrobenchmark-benchmarkData.json

You can also configure the location where benchmark reports are saved on the device using the instrumentation argument[`additionalTestOutputDir`](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-instrumentation-args#additional-test-output). This folder must be writable by your app.  

    adb shell am instrument -w -e additionalTestOutputDir /sdcard/Download/ com.example.benchmark/androidx.benchmark.junit4.AndroidBenchmarkRunner

On Android 10 (API level 29) and higher, your app's tests run in a storage sandbox by default which prevents your app from accessing files outside of the app-specific directory. To be able to save into a global directory, such as`/sdcard/Download`, pass the following instrumentation argument:  

    -e no-isolated-storage true

You also must explicitly allow legacy storage options in your benchmark's manifest:  

    <application android:requestLegacyExternalStorage="true" ... >

For more information, see[Temporarily opt-out of scoped storage](https://developer.android.com/training/data-storage/use-cases#opt-out-scoped-storage).

### Retrieve the files

In order to retrieve the generated files from the device, use the`adb pull`command, which pulls the specified file into the current directory on your host:  

    adb pull /storage/emulated/0/Android/media/com.example.macrobenchmark/com.example.macrobenchmark-benchmarkData.json

To retrieve all of the`benchmarkData`from a specified folder, check the following snippet:  

    # The following command pulls all files ending in -benchmarkData.json from the directory
    # hierarchy starting at the root /storage/emulated/0/Android.
    adb shell find /sdcard/Download -name "*-benchmarkData.json" | tr -d '\r' | xargs -n1 adb pull

The trace files (`.trace`or`.perfetto-trace`) are saved in the same folder as the`benchmarkData.json`, thus you can collect them in the same way.

### Benchmark data example

The benchmark libraries generate JSON files containing information about the device it was running the benchmarks on and the actual benchmarks it ran. The following snippet represents the generated JSON file:  

    {
        "context": {
            "build": {
                "brand": "google",
                "device": "blueline",
                "fingerprint": "google/blueline/blueline:12/SP1A.210812.015/7679548:user/release-keys",
                "model": "Pixel 3",
                "version": {
                    "sdk": 31
                }
            },
            "cpuCoreCount": 8,
            "cpuLocked": false,
            "cpuMaxFreqHz": 2803200000,
            "memTotalBytes": 3753299968,
            "sustainedPerformanceModeEnabled": false
        },
        "benchmarks": [
            {
                "name": "startup",
                "params": {},
                "className": "com.example.macrobenchmark.startup.SampleStartupBenchmark",
                "totalRunTimeNs": 4975598256,
                "metrics": {
                    "timeToInitialDisplayMs": {
                        "minimum": 347.881076,
                        "maximum": 347.881076,
                        "median": 347.881076,
                        "runs": [
                            347.881076
                        ]
                    }
                },
                "sampledMetrics": {},
                "warmupIterations": 0,
                "repeatIterations": 3,
                "thermalThrottleSleepSeconds": 0
            }
        ]
    }  
    https://github.com/android/performance-samples/blob/09d89822210bc2653163bdd2766b07badedbb94d/MacrobenchmarkSample/com.example.macrobenchmark-benchmarkData.json

## Additional resources

- For guidance in how to detect performance regressions, see[Fighting Regressions with Benchmarks in CI](https://medium.com/androiddevelopers/fighting-regressions-with-benchmarks-in-ci-6ea9a14b5c71).
- To see how to setup Github Actions with Firebase Test Lab, see[Setting up Jetpack Macrobenchmarks for CI](https://github.com/android/performance-samples/tree/main/MacrobenchmarkSample/ftl)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Best practices for SQLite performance](https://developer.android.com/topic/performance/sqlite-performance-best-practices)
- [Create and measure Baseline Profiles without Macrobenchmark](https://developer.android.com/topic/performance/baselineprofiles/manually-create-measure)
- [Stuck partial wake locks](https://developer.android.com/topic/performance/vitals/wakelock)