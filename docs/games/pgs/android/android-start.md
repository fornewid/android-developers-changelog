---
title: https://developer.android.com/games/pgs/android/android-start
url: https://developer.android.com/games/pgs/android/android-start
source: md.txt
---

| **Note:** This guide is for the Play Games Services v2 SDK. For information on the previous version of this SDK, see the [Play Games Services v1
| documentation](https://developer.android.com/games/pgs/v1/android).

This guide describes how to set up an Android Studio project to use the
Play Games Services SDK. You must complete these steps before you
set up Play Games Services [sign-in](https://developer.android.com/games/pgs/android/android-signin) and add
Play Games Services features to your game.

## Before you begin

To prepare your app, complete the steps in the following sections.

### App prerequisites

Make sure that your app's build file uses the following values:

- A `minSdkVersion` of `19` of higher
- A `compileSdkVersion` of `28` or higher

### Set up your game in Google Play Console

The Google Play Console is where you manage Google Play games services for your
game, and configure metadata for authorizing and authenticating your game. For
more information, see
[Set Up Google Play Games Services](https://developer.android.com/games/pgs/console/setup).

## Configure your app

In your project-level `build.gradle` file, include
[Google's Maven repository](https://maven.google.com/web/index.html)
and [Maven central repository](https://search.maven.org/artifact)
in both your `buildscript` and `allprojects` sections:

      buildscript {
        repositories {
          google()
          mavenCentral()
        }
      }

      allprojects {
        repositories {
          google()
          mavenCentral()
        }
      }

Add the [Google Play services](https://developers.google.com/android)
dependency for the Play Games SDK to your
[module's Gradle build file](https://developer.android.com/studio/build#module-level), which is commonly

`app/build.gradle`:

      dependencies {
        implementation "com.google.android.gms:play-services-games-v2:+"
      }

After completing these steps you must set up
[sign-in](https://developer.android.com/games/pgs/android/android-signin)
in order for the game to access Play Games Services features.