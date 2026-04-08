---
title: Android Studio  |  Android Developers
url: https://developer.android.com/build/releases/agp-1-1-1-release-notes
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [Gradle build guides](https://developer.android.com/build/releases/past-releases)

Stay organized with collections

Save and categorize content based on your preferences.



# Android plugin for Gradle, revision 1.1.1 (February 2015)

Dependencies:

|  | Minimum version | Default version | Notes |
| --- | --- | --- | --- |
| Gradle | 2.2.1 | 2.2.1 | To learn more, see [updating Gradle](/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 21.1.1 | 21.1.1 | [Install](/studio/intro/update#sdk-manager) or [configure](/tools/releases/build-tools) SDK Build Tools. |

General Notes:
:   * Modified build variants so only variants that package a
      [Wear](/training/wearables/apps) app trigger
      Wear-specific build tasks.
    * Changed dependency related issues to fail at build time rather
      than at debug time. This behavior lets you run diagnostic
      tasks (such as 'dependencies') to help resolve the conflict.
    * Fixed the `android.getBootClasspath()` method to
      return a value.