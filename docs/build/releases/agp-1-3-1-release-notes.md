---
title: Android Studio  |  Android Developers
url: https://developer.android.com/build/releases/agp-1-3-1-release-notes
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [Gradle build guides](https://developer.android.com/build/releases/past-releases)

Stay organized with collections

Save and categorize content based on your preferences.



# Android plugin for Gradle, revision 1.3.1 (August 2015)

**Dependencies:**

|  | Minimum version | Default version | Notes |
| --- | --- | --- | --- |
| Gradle | 2.2.1 | 2.2.1 | To learn more, see [updating Gradle](/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 21.1.1 | 21.1.1 | [Install](/studio/intro/update#sdk-manager) or [configure](/tools/releases/build-tools) SDK Build Tools. |

**General Notes:**

* Fixed the [ZipAlign](/tools/help/zipalign) task to properly
  consume the output of the previous task when using a customized filename.
* Fixed [Renderscript](/guide/topics/renderscript/compute)
  packaging with the [NDK](/tools/sdk/ndk).
* Maintained support for the `createDebugCoverageReport` build task.
* Fixed support for customized use of the `archiveBaseName`
  property in the `build.gradle` build file.
* Fixed the `Invalid ResourceType`
  [lint](/tools/help/lint) warning caused by parameter method
  annotation lookup when running
  [lint](/tools/help/lint) outside of Android Studio.