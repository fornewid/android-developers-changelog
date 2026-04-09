---
title: Install and configure Android Studio for XR development  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/get-studio
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Install and configure Android Studio for XR development Stay organized with collections Save and categorize content based on your preferences.




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

The Jetpack XR SDK includes some features and changes that aren't compatible
with some lower versions of Android Studio. For the best development experience
while developing for Android XR, use the [latest Canary build](/studio/preview) of Android
Studio. Other versions might not include Android XR tools. Remember that you can
keep your existing version of Android Studio installed, as you can [install
multiple versions side-by-side](/studio/preview/install-preview).

[![](/static/images/spot-icons/android-studio.svg)

Get a Canary build

Download the latest Canary build of Android Studio.

arrow\_forward](https://developer.android.com/studio/preview)

## Install Android Studio

Complete the following steps to download and configure Android Studio for
Android XR:

1. Close any versions of Android Studio that you already have installed.
2. Download the latest Canary build of [Android Studio](/studio/preview), extract it into
   your preferred location, and launch the application.
3. Follow the installation instructions in the wizard.
4. In the **Welcome to Android Studio** dialog, click **More Actions**, and
   then select **SDK Manager**.

   ![Android studio welcome
   screen](/static/images/develop/xr/jetpack-xr-sdk/studio-welcome.png)
5. In the **Android SDK** settings, click the **SDK Tools** tab, and then
   select the following tools to install:

   * Android SDK Build-Tools
   * Android Emulator
   * Android SDK Platform-Tools
   * Layout Inspector for API 31 - 36

   ![Android studio SDK Tools
       tab](/static/images/develop/xr/jetpack-xr-sdk/studio-sdk-tools.png)

   **Note:** If you had a previous version of Android Studio installed, you might
   need to re-select each option, and then click **Apply** to download the
   latest updates to these tools.

## Create virtual devices to run on the Android XR Emulator

To see how your app's experiences look and behave on different types of XR
devices, you can run your app on virtual XR devices on the Android XR Emulator.
See the following pages for information on setting up the emulator for different
types of virtual XR devices:

* [XR headsets and XR glasses](/develop/xr/jetpack-xr-sdk/run/create-avds/xr-headsets-glasses)
* [AI glasses](/develop/xr/jetpack-xr-sdk/run/create-avds/ai-glasses)

## Enable usage statistics to help improve Android Studio for XR (optional)

Because this is a Canary build of Android Studio, many of the features are still
under development. Consider enabling usage statistics and sending feedback to
help us improve these tools.

To enable usage statistics:

1. Click **Settings > Appearance & Behavior > System Settings > Data Sharing**.
2. Select **Send usage statistics**.

   ![Android Studio data sharing
   settings](/static/images/develop/xr/jetpack-xr-sdk/studio-data-sharing-settings.png)

[Previous

arrow\_back

Overview](/develop/xr/jetpack-xr-sdk/get-started)

[Next

Create an Android XR project

arrow\_forward](/develop/xr/jetpack-xr-sdk/create-project)