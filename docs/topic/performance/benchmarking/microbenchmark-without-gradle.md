---
title: https://developer.android.com/topic/performance/benchmarking/microbenchmark-without-gradle
url: https://developer.android.com/topic/performance/benchmarking/microbenchmark-without-gradle
source: md.txt
---

# Build Microbenchmarks without Gradle

This page describes configuring a non-Gradle build system when using the Microbenchmark library.

Although the Microbenchmark library ships a Gradle plugin to integrate directly with the Android Gradle plugin, you can also use it in other build systems, such as[Bazel](https://bazel.build)or[Buck](https://buck.build).

## Instrumentation

Use[`AndroidBenchmarkRunner`](https://developer.android.com/reference/kotlin/androidx/benchmark/junit4/AndroidBenchmarkRunner)or a subclass as your instrumentation runner by specifying it in the instrumentation block of the test manifest:  

```xml
<manifest
    package="com.example.library.test" ...>

    <instrumentation android:name="androidx.benchmark.junit4.AndroidBenchmarkRunner" />
    ...
</manifest>
```

To get accurate measurements, benchmarks must not be[debuggable](https://developer.android.com/guide/topics/manifest/application-element#debug). If you don't set the debuggable flag correctly, the library throws an error, rather than reporting invalid results. You might need to toggle this setting during local runs for use with Android Studio profilers, which require`debuggable=true`.

You can build Microbenchmarks to run in two ways: within a self-instrumenting APK, or with one test APK instrumenting another APK.

### Self-instrumenting APKs

With a self-instrumenting APK---as output by Gradle for an[`androidTest`](https://developer.android.com/reference/tools/gradle-api/8.3/null/com/android/build/api/variant/AndroidTest)directory from`com.android.library`---you must disable debuggable in the single APK's Android manifest:  

```xml
<manifest
    package="com.example.library.test" ...>

    <instrumentation
        android:name="androidx.benchmark.junit4.AndroidBenchmarkRunner"
        android:targetPackage="com.example.library.test"/>

    <application android:debuggable="false"/>
</manifest>
```

### App APK instrumented by test APK

If your build outputs two APKs---an app APK and test APK, as output by Gradle for the`androidTest`directory from the`com.android.app`package---you must set the app APK to`debuggable=false`. The test APK's debuggable flag is ignored by the Android OS.  

```xml
<!-- Test manifest. -->
<manifest
    package="com.example.android.app.test" ...>

    <instrumentation
        android:name="androidx.benchmark.junit4.AndroidBenchmarkRunner"
        android:targetPackage="com.example.android.app"/>
    <!-- This debuggable is ignored by the OS. -->
</manifest>

<!-- App being tested. -->
<manifest
    package="com.example.android.app" ...>

    <application android:debuggable="false"/>
</manifest>
```

Android Studio and Gradle don't support microbenchmarking an app module APK. This is due to the complexity of supporting an additional testing directory that depends on a non-debuggable, optimized, or minified variant of the APK, but without minification breaking calls from benchmarks into app code.

## Compilation

We recommend compiling your microbenchmark APK before running tests, using the following command:  

    adb shell cmd package compile -f -m speed com.example.benchmark

## Minification and optimization

We recommend using minification and optimization for your benchmarks to get performance that is close to release. For example code, see the[Benchmark sample project](https://github.com/android/performance-samples/blob/main/MicrobenchmarkSample/microbenchmark/build.gradle.kts).

## Code coverage

We recommend running benchmarks with coverage disabled and without any library or DEX mangling by tools such as JaCoCo.

For this reason, we recommend you isolate benchmarks as a source set from other instrumentation tests and build them separately with release dependencies. This avoids having to build tests more than once, both with and without coverage.

Debug variants of libraries that your benchmark depends on, especially those built locally, might be built with coverage enabled.

## Run your tests

You can run your tests from the command line and specify the classes to run with, as shown in the following example:  

    adb shell am instrument -w com.example.benchmark/androidx.benchmark.junit4.AndroidBenchmarkRunner

To configure the Microbenchmark library at runtime without Gradle, see[Microbenchmark instrumentation arguments](https://developer.android.com/studio/profile/microbenchmark-instrumentation-args).

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Write a Microbenchmark](https://developer.android.com/topic/performance/benchmarking/microbenchmark-write)
- [Create Baseline Profiles {:#creating-profile-rules}](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile)