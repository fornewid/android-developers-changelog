---
title: https://developer.android.com/build/releases/agp-3-0-0-release-notes
url: https://developer.android.com/build/releases/agp-3-0-0-release-notes
source: md.txt
---

<br />

# Android Gradle Plugin 3.0.0 (October 2017)

Android Gradle plugin 3.0.0 includes a variety of changes that aim to
address performance issues of large projects.

For example, on a
[sample skeleton
project](https://github.com/jmslau/perf-android-large.git) with \~130 modules and a large number of external dependencies
(but no code or resources), you can experience performance improvements
similar to the following:

| Android plugin version + Gradle version | Android plugin 2.2.0 + Gradle 2.14.1 | Android plugin 2.3.0 + Gradle 3.3 | Android plugin 3.0.0 + Gradle 4.1 |
| Configuration (e.g. running `./gradlew --help`) | \~2 mins | \~9 s | \~2.5 s |
| 1-line Java change (implementation change) | \~2 mins 15 s | \~29 s | \~6.4 s |
|---|---|---|---|

Some of these changes break existing builds. So, you should consider the  

effort of migrating your project before using the new plugin.

If you don't experience the performance improvements described above,
please [file a bug](https://issuetracker.google.com/issues/new?component=192708&template=840533)
and include a trace of your build using the
[Gradle Profiler](https://github.com/gradle/gradle-profiler).

This version of the Android plugin requires the following:

|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 4.1 | 4.1 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 26.0.2 | 26.0.2 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. With this update, you no longer need to specify a version for the build tools---the plugin uses the minimum required version by default. So, you can now remove the android.buildToolsVersion property. |


**3.0.1 (November 2017)**

This is a minor update to support Android Studio 3.0.1, and includes general
bug fixes and performance improvements.

## Optimizations

- Better parallelism for multi-module projects through a fine grained task graph.
- When making changes to dependency, Gradle performs faster builds by not re-compiling modules that do not have access to that dependency's API. You should restrict which dependencies leak their APIs to other modules by [using
  Gradle's new dependency configurations](https://developer.android.com/studio/build/dependencies#dependency_configurations): `implementation`, `api`, `compileOnly`, and `runtimeOnly`.
- Faster incremental build speed due to per-class dexing. Each class is now compiled into separate DEX files, and only the classes that are modified are re-dexed. You should also expect improved build speeds for apps that set `minSdkVersion` to 20 or lower, and use [legacy multi-dex](https://developer.android.com/studio/build/multidex#mdex-pre-l).
- Improved build speeds by optimizing certain tasks to use chached outputs. To benefit from this optimization, you need to first [enable the Gradle build cache](https://docs.gradle.org/current/userguide/build_cache.html#sec:build_cache_enable).
- Improved incremental resource processing using AAPT2, which is now enabled by default. If you are experiencing issues while using AAPT2, please [report a bug](https://developer.android.com/studio/report-bugs). You can also disable AAPT2 by setting `android.enableAapt2=false` in your `gradle.properties` file and restarting the Gradle daemon by running `./gradlew --stop` from the command line.

<br />

<br />

## New features

- [Variant-aware dependency
  management](https://developer.android.com/studio/build/build-variants#variant_aware). When building a certain variant of a module, the plugin now automatically matches variants of local library module dependencies to the variant of the module you are building.
- Includes a new Feature module plugin to support [Android Instant Apps](https://developer.android.com/topic/instant-apps) and the Android Instant Apps SDK (which you can download [using the SDK manager](https://developer.android.com/studio/intro/update#sdk-manager)). To learn more about creating Feature modules with the new plugin, read [Structure of an
  instant app with multiple features](https://developer.android.com/topic/instant-apps/getting-started/structure#structure_of_an_instant_app_with_multiple_features).
- Built-in support for using certain Java 8 language features and Java 8 libraries. **Jack is now deprecated and no longer required** , and you should first disable Jack to use the improved Java 8 support built into the default toolchain. For more information, read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support).
- Added support for running tests with
  [Android
  Test Orchestrator](https://developer.android.com/training/testing/junit-runner#using-android-test-orchestrator), which allows you to run each of your app's tests within
  its own invocation of Instrumentation. Because each test runs in its own
  Instrumentation instance, any shared state between tests doesn't accumulate
  on your device's CPU or memory. And, even if one test crashes, it takes down
  only its own instance of Instrumentation, so your other tests still run.

  - Added `testOptions.execution` to determine whether to use on-device test orchestration. If you want to [use
    Android Test Orchestrator](https://developer.android.com/training/testing/junit-runner#using-android-test-orchestrator), you need to specify `ANDROID_TEST_ORCHESTRATOR`, as shown below. By default, this property is set to `HOST`, which disables on-device orchestration and is the standard method of running tests.

  ### Groovy

  ```groovy
          android {
            testOptions {
              execution 'ANDROID_TEST_ORCHESTRATOR'
            }
          }
          
  ```

  ### Kotlin

  ```kotlin
          android {
            testOptions {
              execution = "ANDROID_TEST_ORCHESTRATOR"
            }
          }
          
  ```
- New `androidTestUtil` dependency configuration allows you to
  install another test helper APK before running your instrumentation tests,
  such as Android Test Orchestrator:

  ### Groovy

  ```groovy
          dependencies {
            androidTestUtil 'com.android.support.test:orchestrator:1.0.0'
            ...
          }
          
  ```

  ### Kotlin

  ```kotlin
          dependencies {
            androidTestUtil("com.android.support.test:orchestrator:1.0.0")
            ...
          }
          
  ```
- Added `testOptions.unitTests.includeAndroidResources` to
  support unit tests that require Android resources, such as
  [Roboelectric](http://robolectric.org/). When you set this
  property to `true`, the plugin performs resource, asset, and
  manifest merging before running your unit tests. Your tests can then
  inspect `com/android/tools/test_config.properties` on the
  classpath for the following keys:

  - `android_merged_assets`: the absolute path to the
    merged assets directory.

    **Note:** For library modules, the merged assets
    do not contain the assets of dependencies (see
    [issue
    #65550419](https://issuetracker.google.com/65550419)).
  - `android_merged_manifest`: the absolute path to the
    merged manifest file.

  - `android_merged_resources`: the absolute path to the
    merged resources directory, which contains all the resources from
    the module and all its dependencies.

  - `android_custom_package`: the package name of the
    final R class. If you dynamically modify the application ID, this
    package name may not match the `package` attribute in the
    app's manifest.

- Support for [fonts
  as resources](https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml) (which is a new feature introduced in [Android 8.0 (API level 26)](https://developer.android.com/about/versions/oreo)).
- Support for language-specific APKs with [Android
  Instant Apps SDK 1.1](https://developer.android.com/topic/instant-apps/release-notes#android_instant_apps_development_sdk_v110) and higher.
- You can now change the output directory for your external native build
  project, as shown below:

  ### Groovy

  ```groovy
          android {
              ...
              externalNativeBuild {
                  // For ndk-build, instead use the ndkBuild block.
                  cmake {
                      ...
                      // Specifies a relative path for outputs from external native
                      // builds. You can specify any path that's not a subdirectory
                      // of your project's temporary build/ directory.
                      buildStagingDirectory "./outputs/cmake"
                  }
              }
          }
          
  ```

  ### Kotlin

  ```kotlin
          android {
              ...
              externalNativeBuild {
                  // For ndk-build, instead use the ndkBuild block.
                  cmake {
                      ...
                      // Specifies a relative path for outputs from external native
                      // builds. You can specify any path that's not a subdirectory
                      // of your project's temporary build/ directory.
                      buildStagingDirectory = "./outputs/cmake"
                  }
              }
          }
          
  ```
- You can now [use CMake 3.7 or
  higher](https://developer.android.com/studio/projects/install-ndk#vanilla_cmake) when building native projects from Android Studio.
- New `lintChecks` dependency configuration allows you to
  build a JAR that defines custom lint rules, and package it into your AAR
  and APK projects.

  Your custom lint rules must belong to a separate project that outputs
  a single JAR and includes only
  [`compileOnly`](https://docs.gradle.org/current/userguide/java_plugin.html#sec:java_plugin_and_dependency_management)
  dependencies. Other app and library modules can then depend on your lint
  project using the `lintChecks` configuration:

  ### Groovy

  ```groovy
          dependencies {
              // This tells the Gradle plugin to build ':lint-checks' into a lint.jar file
              // and package it with your module. If the module is an Android library,
              // other projects that depend on it automatically use the lint checks.
              // If the module is an app, lint includes these rules when analyzing the app.
              lintChecks project(':lint-checks')
          }
          
  ```

  ### Kotlin

  ```kotlin
          dependencies {
              // This tells the Gradle plugin to build ':lint-checks' into a lint.jar file
              // and package it with your module. If the module is an Android library,
              // other projects that depend on it automatically use the lint checks.
              // If the module is an app, lint includes these rules when analyzing the app.
              lintChecks(project(":lint-checks"))
          }
          
  ```

<br />

<br />

## Behavior changes

- Android plugin 3.0.0 removes certain APIs, and your build will break if you use them. For example, you can no longer use the Variants API to access `outputFile()` objects or use `processManifest.manifestOutputFile()` to get the manifest file for each variant. To learn more, read [API changes](https://developer.android.com/studio/known-issues#variant_api).
- You no longer need to specify a version for the build tools (so, you can now remove the `android.buildToolsVersion` property). By default, the plugin automatically uses the minimum required build tools version for the version of Android plugin you're using.
- You now enable/disable PNG crunching in the `buildTypes` block, as shown below. PNG crunching is enabled by default for all builds except debug builds because it increases build times for projects that include many PNG files. So, to improve build times for other build types, you should either disable PNG crunching or [convert
  your images to WebP](https://developer.android.com/studio/write/convert-webp#convert_images_to_webp).

  ### Groovy

  ```groovy
        android {
          buildTypes {
            release {
              // Disables PNG crunching for the release build type.
              crunchPngs false
            }
          }
        }
        
  ```

  ### Kotlin

  ```kotlin
        android {
          buildTypes {
            release {
              // Disables PNG crunching for the release build type.
              isCrunchPngs = false
            }
          }
        }
        
  ```
- The Android plugin now automatically builds executable targets that you configure in your external CMake projects.
- You must now [add annotation
  processors](https://developer.android.com/studio/build/dependencies#annotation_processor) to the processor classpath using the `annotationProcessor` dependency configuration.
- Using the deprecated `ndkCompile` is now more restricted. You should instead migrate to using either CMake or ndk-build to compile native code that you want to package into your APK. To learn more, read [Migrate from
  ndkcompile](https://developer.android.com/studio/projects/add-native-code#ndkCompile).

<br />