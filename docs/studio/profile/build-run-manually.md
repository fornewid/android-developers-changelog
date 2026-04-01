---
title: Build and run a profileable app manually  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/profile/build-run-manually
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [IDE guides](https://developer.android.com/studio/intro)

# Build and run a profileable app manually Stay organized with collections Save and categorize content based on your preferences.




To build a [profileable](/studio/profile#requirements) application manually, you
need to first build a release application and then update its manifest file,
which turns the release application into a profileable application. After you
configure the profileable application, launch the profiler and select a
profileable process to analyze.

## Build a release app

To build a release application for profiling purposes, do the following:

1. Sign your application with the debug key by adding the following lines to your application's
   `build.gradle` file. If you already have a working release build variant, you can
   skip to the next step.

   ```
           buildTypes {
             release {
               signingConfig signingConfigs.debug
             }
           }
   ```
2. In Android Studio, select **Build** > **Select Build Variant...** and choose the
   release variant.

## Change release to profileable

To convert your [release app](#build-release-app) to a profileable app, do the
following:

1. Open the
   `AndroidManifest.xml` file and adding the following within
   `<application>`. For more details, see
   [Build your app for release](/studio/publish/preparing#publishing-build).

   `<profileable android:shell="true"/>`
2. Depending on the SDK version, you might see an error related to manifest
   validation; if you can't resolve them and deem it safe to treat the errors
   as warnings, you can do so by adding the following lines to your
   `build.gradle` file.

   ```
         aaptOptions {
           additionalParameters =["--warn-manifest-validation"]
         }
   ```