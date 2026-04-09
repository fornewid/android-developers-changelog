---
title: Android Studio  |  Android Developers
url: https://developer.android.com/build/releases/agp-2-3-0-release-notes
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [Gradle build guides](https://developer.android.com/build/releases/past-releases)

Stay organized with collections

Save and categorize content based on your preferences.



# Android Gradle Plugin 2.3.0 (February 2017)

**2.3.3 (June 2017)**

This is a minor update that adds compatibility with
[Android Studio 2.3.3](/studio/releases#Revisions).

**2.3.2 (May 2017)**

This is a minor update that adds compatibility with
[Android Studio
2.3.2](/studio/releases#Revisions).

**2.3.1 (April 2017)**

This is a minor update to Android plugin 2.3.0 that fixes an issue
where some physical Android devices did not work properly with
[Instant Run](/studio/run#instant-run) (see
[Issue #235879](https://code.google.com/p/android/issues/detail?id=235879)).

Dependencies:

|  | Minimum version | Default version | Notes |
| --- | --- | --- | --- |
| Gradle | 3.3 | 3.3 | To learn more, see [updating Gradle](/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 25.0.0 | 25.0.0 | [Install](/studio/intro/update#sdk-manager) or [configure](/tools/releases/build-tools) SDK Build Tools. |

New:
:   * Uses Gradle 3.3, which includes performance improvements and
      new features. For more details, see the
      [Gradle release notes](https://docs.gradle.org/3.3/release-notes).
    * **Build cache**: stores certain outputs that the Android
      plugin generates when building your project (such as unpackaged
      AARs and pre-dexed remote dependencies). Your clean builds are
      much faster while using the cache because the build system can
      simply reuse those cached files during subsequent builds, instead
      of recreating them. Projects using Android plugin 2.3.0 and higher use
      the build cache by default. To learn more, read
      [Improve Build Speed with
      Build Cache](/studio/build/build-cache).
      + Includes a `cleanBuildCache` task that
        [clears
        the build cache](/studio/build/build-cache#clear_the_build_cache).
      + If you are using the experimental version of build cache
        (included in earlier versions of the plugin), you should
        [update your plugin](#updating-plugin) to the
        latest version.

Changes:
:   * Supports changes to Instant Run included in
      [Android Studio 2.3](/studio/releases).
    * Configuration times for very large projects should be
      significantly faster.
    * Fixed issues with auto-downloading for the
      [constraint layout
      library](/training/constraint-layout).
    * Plugin now uses
      [ProGuard version 5.3.2](https://www.guardsquare.com/en/proguard/manual/versions).
    * Includes many fixes for
      [reported bugs](https://code.google.com/p/android/issues/list?can=1&q=Component%3DTools++Subcomponent%3DTools-gradle%2CTools-build%2CTools-instantrun%2CTools-cpp-build+Target%3D2.3+status%3AFutureRelease%2CReleased+&sort=priority+-status&colspec=ID+Status+Priority+Owner+Summary+Stars+Reporter+Opened&cells=tiles). Please continue to
      [file bug reports](/studio/report-bugs) when you
      encounter issues.