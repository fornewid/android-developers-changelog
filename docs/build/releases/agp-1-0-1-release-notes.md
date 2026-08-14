---
title: https://developer.android.com/build/releases/agp-1-0-1-release-notes
url: https://developer.android.com/build/releases/agp-1-0-1-release-notes
source: md.txt
---

# Android plugin for Gradle, revision 1.0.1 (January 2015)

Dependencies:
General Notes:
:
    - Fixed issue with Gradle build failure when accessing the `extractReleaseAnnotations` module. ([Issue 81638](http://b.android.com/81638)).
    - Fixed issue with `Disable` passing the `--no-optimize` setting to the Dalvik Executable (dex) bytecode. ([Issue
      82662](http://b.android.com/82662)).
    - Fixed manifest merger issues when importing libraries with a `targetSdkVersion` less than 16.
    - Fixed density ordering issue when using Android Studio with JDK 8.