---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/create-project
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/create-project
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) AI Glasses [](https://developer.android.com/develop/xr/devices#ai-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Your Android Studio project encompasses all the files and necessary
configurations for developing an Android XR app with the Jetpack XR SDK. This
includes source code, assets, test code, and build configurations.

If you're adding XR experiences to an existing app:

1. Open your existing Android Studio project in [the latest Canary build of
   Android Studio](https://developer.android.com/develop/xr/jetpack-xr-sdk/get-studio).
2. [Set up the Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk/set-up-sdk).
3. See the following topics for more information, depending on what types of experiences you're trying to build:
   - **Building immersive experiences** : If you're spatializing an existing app for [XR headsets](https://developer.android.com/develop/xr/devices#xr-headsets) and [XR glasses](https://developer.android.com/develop/xr/devices#xr-glasses), see [Bring your Android
     app into 3D with XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-xr-to-existing) for more information.
   - **Building augmented experiences** : If you're extending your mobile app to [AI glasses](https://developer.android.com/develop/xr/devices#ai-glasses) see [Start building for AI glasses](https://developer.android.com/develop/xr/jetpack-xr-sdk/ai-glasses/build) to get started.

## Create a new project

If you want to start a new Android XR project in Android Studio, follow these
steps:

1. Open Android Studio.

   1. If you see the **Welcome to Android Studio** window, click **New
      Project**.
   2. If Android Studio reopened an existing project, select **File \> New \>
      New Project** from the menu bar.

   ![Android studio welcome screen](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/setup/welcome-2.png)
2. From the list of **Templates** , select **XR** , and then choose the template
   that corresponds to the [type of XR device](https://developer.android.com/develop/xr/devices) you want to build for.

   ![Android studio new project screen](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/setup/new-project.png)
3. Click **Next**.

4. Choose a name for your project, and then click **Finish**.

## Next steps

Explore the code provided in the template, and check out the documentation for
[building immersive experiences](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-xr-to-existing) for XR headsets and XR glasses, and the
documentation for [building augmented experiences](https://developer.android.com/develop/xr/jetpack-xr-sdk/ai-glasses/build) for AI glasses.