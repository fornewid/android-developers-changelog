---
title: Android Studio  |  Android Developers
url: https://developer.android.com/build/releases/agp-1-1-2-release-notes
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [Gradle build guides](https://developer.android.com/build/releases/past-releases)

Stay organized with collections

Save and categorize content based on your preferences.



# Android plugin for Gradle, revision 1.1.2 (February 2015)

Dependencies:

|  | Minimum version | Default version | Notes |
| --- | --- | --- | --- |
| Gradle | 2.2.1 | 2.2.1 | To learn more, see [updating Gradle](/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 21.1.1 | 21.1.1 | [Install](/studio/intro/update#sdk-manager) or [configure](/tools/releases/build-tools) SDK Build Tools. |

General Notes:
:   * Normalized path when creating a mockable JAR for unit
      testing.
    * Fixed the `archivesBaseName` setting in the
      `build.gradle` file.
    * Fixed the unresolved placeholder failure in manifest merger
      when building a library test application.