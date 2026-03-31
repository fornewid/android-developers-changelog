---
title: Android Studio  |  Android Developers
url: https://developer.android.com/build/releases/agp-3-5-0-release-notes
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [Gradle build guides](https://developer.android.com/build/releases/past-releases)

Stay organized with collections

Save and categorize content based on your preferences.




# Android Gradle Plugin 3.5.0 (August 2019)

Android Gradle plugin 3.5.0, along with
[Android Studio 3.5](/studio/releases#3-5-0), is a major release
and a result of Project Marble, which is a focus on improving three main
areas of the Android developer tools: system health, feature polish, and
fixing bugs. Notably,
[improving project
build speed](https://medium.com/androiddevelopers/improving-build-speed-in-android-studio-3e1425274837) was a main focus for this update.

For information about these and other Project Marble updates, read the
[Android
Developers blog post](https://android-developers.googleblog.com/2019/05/android-studio-35-beta.html) or the sections below.

This version of the Android plugin requires the following:

|  | Minimum version | Default version | Notes |
| --- | --- | --- | --- |
| Gradle | 5.4.1 | 5.4.1 | To learn more, see [updating Gradle](/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 28.0.3 | 28.0.3 | [Install](/studio/intro/update#sdk-manager) or [configure](/tools/releases/build-tools) SDK Build Tools. |

**3.5.4 (July 2020)**

This minor update supports compatibility with new default settings and
features for
[package visibility
in Android 11](/about/versions/11/privacy/package-visibility).

See the [4.0.1 release notes](#4.0.1) for details.

**3.5.3 (December 2019)**

This minor update supports Android Studio 3.5.3 and includes various bug
fixes and performance improvements.

**3.5.2 (November 2019)**

This minor update supports Android Studio 3.5.2 and includes various bug
fixes and performance improvements.
To see a list of noteable bug fixes, read the related post on the
[Release Updates blog](https://androidstudio.googleblog.com/2019/11/android-studio-352-available.html).

**3.5.1 (October 2019)**

This minor update supports Android Studio 3.5.1 and includes various bug
fixes and performance improvements.
To see a list of noteable bug fixes, read the related post on the
[Release Updates blog](https://androidstudio.googleblog.com/2019/10/android-studio-351-available.html).

## Incremental annotation processing

The [Data Binding](/reference/android/databinding/package-summary)
annotation processor supports
[incremental annotation processing](https://docs.gradle.org/current/userguide/java_plugin.html#sec:incremental_annotation_processing)
if you set `android.databinding.incremental=true` in your
`gradle.properties` file. This optimization results in improved
incremental build performance. For a full list of optimized annotation
processors, refer to the table of [incremental annotation
processors](https://docs.gradle.org/current/userguide/java_plugin.html#state_of_support_in_popular_annotation_processors).

Additionally, KAPT 1.3.30 and higher also support incremental annotation
processors, which you can enable by including `kapt.incremental.apt=true` in
your `gradle.properties` file.

## Cacheable unit tests

When you enable unit tests to use Android resources, assets, and
manifests by setting
[`includeAndroidResources`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.TestOptions.UnitTestOptions.html#com.android.build.gradle.internal.dsl.TestOptions.UnitTestOptions:includeAndroidResources)
to `true`, the Android Gradle plugin generates a test config file
containing absolute paths, which breaks cache relocatability. You can instruct
the plugin to instead generate the test config using relative paths, which
allows the `AndroidUnitTest` task to be fully cacheable, by
including the following in your `gradle.properties` file:

```
      android.testConfig.useRelativePath = true
```

## Known issues

* When using Kotlin Gradle plugin 1.3.31 or earlier, you might see the
  following warning when building or syncing your project:

  ```
            WARNING: API 'variant.getPackageLibrary()' is obsolete and has been replaced
                    with 'variant.getPackageLibraryProvider()'.
  ```

  To resolve
  [this issue](https://youtrack.jetbrains.com/issue/KT-30784),
  upgrade the plugin to version 1.3.40 or higher.