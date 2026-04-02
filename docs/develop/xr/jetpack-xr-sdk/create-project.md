---
title: Create an Android XR project  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/create-project
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Create an Android XR project Stay organized with collections Save and categorize content based on your preferences.



Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/xr-headsets-icon.svg)


XR Headsets

![](/static/images/develop/xr/xr-glasses-icon.svg)


Wired XR Glasses

![](/static/images/develop/xr/ai-glasses-icon.svg)


AI Glasses

[Learn about XR device types →](/develop/xr/devices)

Your Android Studio project encompasses all the files and necessary
configurations for developing an Android XR app with the Jetpack XR SDK. This
includes source code, assets, test code, and build configurations.

If you're adding XR experiences to an existing app:

1. Open your existing Android Studio project in [the latest Canary build of
   Android Studio](/develop/xr/jetpack-xr-sdk/get-studio).
2. [Set up the Jetpack XR SDK](/develop/xr/jetpack-xr-sdk/set-up-sdk).
3. See the following topics for more information, depending on what types of
   experiences you're trying to build:
   * **Building immersive experiences**: If you're spatializing an existing
     app for [XR headsets](/develop/xr/devices#xr-headsets) and [XR glasses](/develop/xr/devices#xr-glasses), see [Bring your Android
     app into 3D with XR](/develop/xr/jetpack-xr-sdk/add-xr-to-existing) for more information.
   * **Building augmented experiences**: If you're extending your mobile app
     to [AI glasses](/develop/xr/devices#ai-glasses) see [Start building for AI glasses](/develop/xr/jetpack-xr-sdk/ai-glasses/build) to get
     started.

## Create a new project

If you want to start a new Android XR project in Android Studio, follow these
steps:

1. Open Android Studio.

   1. If you see the **Welcome to Android Studio** window, click **New
      Project**.
   2. If Android Studio reopened an existing project, select **File > New >
      New Project** from the menu bar.

   ![Android studio welcome screen](/static/images/develop/xr/jetpack-xr-sdk/setup/welcome-2.png)
2. From the list of **Templates**, select **XR**, and then choose the template
   that corresponds to the [type of XR device](/develop/xr/devices) you want to build for.

   ![Android studio new project screen](/static/images/develop/xr/jetpack-xr-sdk/setup/new-project.png)
3. Click **Next**.
4. Choose a name for your project, and then click **Finish**.

## Next steps

Explore the code provided in the template, and check out the documentation for
[building immersive experiences](/develop/xr/jetpack-xr-sdk/add-xr-to-existing) for XR headsets and XR glasses, and the
documentation for [building augmented experiences](/develop/xr/jetpack-xr-sdk/ai-glasses/build) for AI glasses.

[Previous

arrow\_back

Install and configure Android Studio](/develop/xr/jetpack-xr-sdk/get-studio)

[Next

Set up the Jetpack XR SDK

arrow\_forward](/develop/xr/jetpack-xr-sdk/set-up-sdk)