---
title: https://developer.android.com/training/wearables/versions/6/setup
url: https://developer.android.com/training/wearables/versions/6/setup
source: md.txt
---

# Prepare for Wear OS 6

This page explains how to set up the official emulator for testing, and how to upgrade your app to target Wear OS 6.

## Set up an emulator

<br />

The Wear OS 6 emulator lets you do the following:

- Test behavior changes in Wear OS 6.
- Explore the new features that are available in Wear OS 6.
- View the watch faces that you create using[Watch Face Studio](https://developer.samsung.com/watch-face-studio/user-guide/index.html).

Using the emulator, you can test different screen sizes and watch faces.
**Note:** The Wear OS 6 emulator isn't available in China. Learn more about how to[create Wear OS apps for China](https://support.google.com/wearos/answer/6321140)and support the China market.  
![Apps include find my device, flashlight, media controls, phone, Play Store, and settings](https://developer.android.com/static/training/wearables/versions/6/images/emulator-apps-screen.png)The grid view of the set of apps available in the emulator.

<br />

### Download and install the emulator

To set up a virtual device to run Wear OS 6, follow these steps.
| **Note:** Unlike in previous versions of Wear OS, the emulator that runs Wear OS 6**uses a signed build**. This means that you can't get root access to the emulator image.

1. Download the[latest preview release of Android Studio](https://developer.android.com/studio/preview).

   | **Note:** You need Android Studio Narwhal or later to get the emulator for Wear OS 6.
2. In Android Studio, click**Tools \> SDK Manager**.

3. In the**SDK Tools tab** , select the latest version of**Android Emulator** and click**OK**to install the latest version if it isn't already installed.

4. In Android Studio, open the Device Manager by selecting**Tools \> Device Manager** . Click**Create device**.

5. In the**Category** pane, select**Wear OS** and choose a hardware profile. Click**Next**.

6. Select a Wear OS 6 system image to download, which is the image with**API Level** 36.0 and the**Target**Android 16.0 ("Baklava") (Wear OS 6.0).

   If you don't already have a system image installed that matches your device definition, click**Download** next to the**Release Name**to get it.
7. Click**Next** and then click**Finish**.

### Test your app on the emulator

After creating the virtual device, run and test your application on a emulator that runs Wear OS 6:

1. Go to the Android Studio toolbar and select the virtual device you just created.
2. Click**Run** ![](https://developer.android.com/static/studio/images/buttons/toolbar-run.png).

### Apps available on the emulator

The following user-space apps are pre-installed onto the official emulator:

- Find My Phone
- Flashlight
- Media Controls
- Phone
- Play Store
- Settings

In addition, the following system apps are available in the emulator:

- Android Accessibility Suite
- Bluetooth
- Credential Manager
- Download Manager
- Emergency information
- Google Play services
- Health Services for Wear OS
- Speech Recognition and Synthesis from Google
- Wear Services
- Wireless Emergency Alerts

## Update your app to target Wear OS 6

After you[update your app](https://developer.android.com/training/wearables/versions/6/changes)to prepare it for Wear OS 6, you can further improve your app's compatibility with this version of Wear OS by targeting Wear OS 6 (API level 36), which is based on Android 16, or higher.

If you update your target SDK version, handle the system behavior changes that take effect for apps that[target Android 16 or higher](https://developer.android.com/about/versions/16/behavior-changes-16).
| **Note:** If you publish your Wear OS app to Google Play, you must[target a sufficiently recent version of the platform](https://support.google.com/googleplay/android-developer/answer/11926878). To give yourself time to test your app, it's best to complete this upgrade soon.

### Update your build file

To update your target SDK version, open your module-level`build.gradle`or`build.gradle.kts`file, and update them with the following values for Wear OS 6 (Android 16):  

### Groovy

    android {
        compileSdk 36
        ...
        defaultConfig {
            targetSdk 36
        }
    }

### Kotlin

    android {
        compileSdk = 36
        ...
        defaultConfig {
            targetSdk = 36
        }
    }