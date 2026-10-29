---
title: https://developer.android.com/build/releases/agp-3-2-0-release-notes
url: https://developer.android.com/build/releases/agp-3-2-0-release-notes
source: md.txt
---

<br />

# Android Gradle Plugin 3.2.0 (September 2018)

This version of the Android plugin requires the following:

|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 4.6 | 4.6 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 28.0.3 | 28.0.3 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |

**3.2.1 (October 2018)**

With this update, you no longer need to specify a version for the SDK Build
Tools. The Android Gradle plugin now uses version 28.0.3 by default.

<br />

<br />

## New features

- **Support for building Android App Bundles:** The app bundle is a new upload
  format that includes all your app's compiled code and resources while
  deferring APK generation and signing to the Google Play Store. You no longer
  have to build, sign, and manage multiple APKs, and users get smaller downloads
  that are optimized for their device. To learn more, read
  [About Android App Bundles](https://developer.android.com/guide/app-bundle).

- **Support for improved incremental build speeds when using annotation processors:**
  The [`AnnotationProcessorOptions`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.AnnotationProcessorOptions.html)
  DSL now extends [`CommandLineArgumentProvider`](https://docs.gradle.org/current/javadoc/org/gradle/process/CommandLineArgumentProvider.html),
  which enables either you or the annotation processor author to annotate
  arguments for the processor using
  [incremental build property type annotations](https://docs.gradle.org/current/userguide/more_about_tasks.html#sec:up_to_date_checks).
  Using these annotations improves the correctness and performance of
  incremental and cached clean builds. To learn more, read
  [Pass arguments to annotation processors](https://developer.android.com/studio/build/dependencies#processor-arguments).

- **Migration tool for AndroidX:** When using Android Gradle plugin 3.2.0 with
  Android 3.2 and higher, you can migrate your project's local and Maven
  dependencies to use the new AndroidX libraries by selecting **Refactor \>
  Migrate to AndroidX** from the menu bar. Using this migration tool also sets
  the following flags to `true` in your `gradle.properties` file:

  - **`android.useAndroidX`:** When set to `true`, the Android plugin uses the
    appropriate AndroidX library instead of a Support Library. When this flag
    is not specified, the plugin sets it to `false` by default.

  - **`android.enableJetifier`:** When set to `true`, the Android plugin
    automatically migrates existing third-party libraries to use AndroidX by
    rewriting their binaries. When this flag is not specified, the plugin sets
    it to `false` by default. You can set this flag to `true` only while
    `android.useAndroidX` is also set to `true`, otherwise you get a build error.

    To learn more, read the [AndroidX overview](https://developer.android.com/topic/libraries/support-library/androidx-overview).
- **New code shrinker, R8:** R8 is a new tool for code shrinking and obfuscation
  that replaces ProGuard. You can start using the preview version of R8 by
  including the following in your project's `gradle.properties` file:

  ```groovy
          android.enableR8 = true
          
  ```

  ```kotlin
          android.enableR8 = true
          
  ```

<br />

<br />

## Behavior changes

- Desugaring with D8 is now enabled by default.

- AAPT2 is now on Google's Maven repo. To use AAPT2, make sure that you
  have the `google()` dependency in your `build.gradle`
  file, as shown below:

  ```groovy
            buildscript {
                  repositories {
                      google() // here
                      jcenter()
                  }
                  dependencies {
                      classpath 'com.android.tools.build:gradle:3.2.0'
                  }
              }
              allprojects {
                  repositories {
                      google() // and here
                      jcenter()
              }
            
  ```

  ```kotlin
            buildscript {
                  repositories {
                      google() // here
                      jcenter()
                  }
                  dependencies {
                      classpath 'com.android.tools.build:gradle:3.2.0'
                  }
              }
              allprojects {
                  repositories {
                      google() // and here
                      jcenter()
              }
            
  ```
- Native multidex is now enabled by default. Previous versions of Android
  Studio enabled native multidex when deploying the debug version of an app to a
  device running Android API level 21 or higher. Now, whether you're deploying
  to a device or building an APK for release, the Android Gradle plugin
  enables native multidex for all modules that set
  `minSdkVersion=21` or higher.

- The plugin now enforces a minimum version of the protobuf plugin (0.8.6),
  Kotlin plugin (1.2.50), and Crashlytics plugin (1.25.4).

- The feature module plugin,`com.android.feature`, now
  enforces the use of only letters, digits, and underscores when specifying
  a module name. For example, if your feature module name includes dashes,
  you get a build error. This behavior matches that of the dynamic feature
  plugin.

<br />

<br />

## Bug fixes

- JavaCompile is now cacheable in projects with data binding. ([Issue #69243050](https://issuetracker.google.com/69243050))
- Better compile avoidance for library modules with data binding. ([Issue #77539932](https://issuetracker.google.com/77539932))
- You can now re-enable [configure-on-demand](https://docs.gradle.org/current/userguide/multi_project_builds.html#sec:configuration_on_demand) if you've disable it in earlier versions due to some unpredictable build errors. ([Issue #77910727](https://issuetracker.google.com/77910727))

<br />