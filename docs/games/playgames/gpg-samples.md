---
title: Samples and plug-ins  |  Android game development  |  Android Developers
url: https://developer.android.com/games/playgames/gpg-samples
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Games dev center](https://developer.android.com/games)
* [Guides](https://developer.android.com/games/guides)

Send feedback

# Samples and plug-ins Stay organized with collections Save and categorize content based on your preferences.



The samples and plug-ins for Google Play Games on PC demonstrate the SDK integrations
for certification and configuration of games in the PC environment.

## AGDKTunnel

[AGDKTunnel](https://github.com/android/games-samples/tree/main/agdk/agdktunnel)
is derived from the NDK sample Endless Tunnel. AGDKTunnel demonstrates the
following Google Play Games on PC SDK integrations:

* Google Play Games Services for Play identity and cloud save
* Input SDK for Google Play Games on PC

### Enable build for Google Play Games on PC

Build variants are used to differentiate between the default (mobile) platform
and the PC platform. To build AGDKTunnel to run in Google Play Games on PC,
follow these steps:

1. Go to **Build > Select Build Variant** and select the **playGamesPC** build variant.
2. (Optional) Enable **Google Play Games Services** to turn on cloud save on mobile and PC.
3. (Optional) Enable **Play Asset Delivery API** to deliver DXT1 compressed texture assets.

### Enable Google Play Games Services

Google Play Games Services (PGS) is used for sign-in and cloud save.
To enable these features, do the following:

1. Rename the AGDKTunnel package to a name of your choosing.
2. Create an application on the Google Play Console and follow the steps
   to set up Google Play Games Services using your package name.
3. Replace the `game_services_project_id` string value in
   `app/src/main/res/values/strings.xml` with the ID of your project in the
   Google Play Console.

## Trivial Kart

A sample game demonstrating use of Google Play technologies on
Android with the Unity engine.
For Google Play Games on PC, the game demonstrates:

* [Google Play Games Services](/games/pgs/overview) for sign-in, achievements, leaderboards, friends, and cloud save
* [Play Integrity](/google/play/integrity/overview) for receiving integrity signals about device integrity and Play license status
* The Input SDK for Google Play Games on PC

See the [trivialkart-unity](https://github.com/android/games-samples/tree/main/trivialkart/trivialkart-unity) sample for configuration information.

## Google Play Games Unity plug-ins

### Platform utils

The [platform\_utils\_package](https://github.com/android/games-samples/tree/main/googleplaygamesforpc/unity_projects/platform_utils_package)
is a tool for automating routines
for Google Play Games on PC with Unity. The package includes the following features:

* GPG platform define script: Adds a UNITY\_ANDROID\_x86\_64 define to the list of custom defines within Player settings
* Asset importer script: Sets every imported texture to a chosen texture compression (DXTC by default)
* Window options: Sets window options available under **Tools > GPG Settings**

### Input capture

The [input-capture\_package](https://github.com/android/games-samples/tree/main/googleplaygamesforpc/unity_projects/input_capture_package)
demonstrates mouse input capture features:

* [Mouse input capture](/games/playgames/input-mouse#capture_mouse_input) with Spacebar toggle
* Mouse button state events
* Mouse scroll events
* Screen geometry detection




Send feedback