---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/get-studio
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/get-studio
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) AI Glasses [](https://developer.android.com/develop/xr/devices#ai-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

The Jetpack XR SDK includes some features and changes that aren't compatible
with some lower versions of Android Studio. For the best development experience
while developing for Android XR, use the [latest Canary build](https://developer.android.com/studio/preview) of Android
Studio. Other versions might not include Android XR tools. Remember that you can
keep your existing version of Android Studio installed, as you can [install
multiple versions side-by-side](https://developer.android.com/studio/preview/install-preview).
[![](https://developer.android.com/static/images/spot-icons/android-studio.svg) Get a Canary build Download the latest Canary build of Android Studio.](https://developer.android.com/studio/preview)

## Install Android Studio

Complete the following steps to download and configure Android Studio for
Android XR:

1. Close any versions of Android Studio that you already have installed.

2. Download the latest Canary build of [Android Studio](https://developer.android.com/studio/preview), extract it into
   your preferred location, and launch the application.

3. Follow the installation instructions in the wizard.

4. In the **Welcome to Android Studio** dialog, click **More Actions** , and
   then select **SDK Manager**.

   ![Android studio welcome
   screen](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/studio-welcome.png)
5. In the **Android SDK** settings, click the **SDK Tools** tab, and then
   select the following tools to install:

   - Android SDK Build-Tools
   - Android Emulator
   - Android SDK Platform-Tools
   - Layout Inspector for API 31 - 36

   ![Android studio SDK Tools
   tab](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/studio-sdk-tools.png)

   > [!NOTE]
   > **Note:** If you had a previous version of Android Studio installed, you might need to re-select each option, and then click **Apply** to download the latest updates to these tools.

## Create virtual devices to run on the Android XR Emulator

To see how your app's experiences look and behave on different types of XR
devices, you can run your app on virtual XR devices on the Android XR Emulator.
See the following pages for information on setting up the emulator for different
types of virtual XR devices:

- [XR headsets and XR glasses](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/xr-headsets-glasses)
- [AI glasses](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/ai-glasses)

## Enable usage statistics to help improve Android Studio for XR (optional)

Because this is a Canary build of Android Studio, many of the features are still
under development. Consider enabling usage statistics and sending feedback to
help us improve these tools.

To enable usage statistics:

1. Click **Settings \> Appearance \& Behavior \> System Settings \> Data Sharing**.
2. Select **Send usage statistics**.

   ![Android Studio data sharing
   settings](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/studio-data-sharing-settings.png)