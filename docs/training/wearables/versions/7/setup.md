---
title: https://developer.android.com/training/wearables/versions/7/setup
url: https://developer.android.com/training/wearables/versions/7/setup
source: md.txt
---

This page explains how to set up the official emulator for testing, and how to
upgrade your app to target Wear OS 7.

## Set up an emulator

Use the Wear OS 7 emulator to test behavior changes, explore new features, and
test your app on different screen sizes and watch hardware profiles.

### Download and install the emulator

To set up a virtual device to run Wear OS 7, follow these steps:

1. Download the [latest release of Android Studio](https://developer.android.com/studio).
2. In Android Studio, click **Tools \> SDK Manager**.
3. In the **SDK Tools** tab, select the latest version of **Android Emulator** and click **OK** to install the latest version if it isn't already installed.
4. In Android Studio, open the Device Manager by selecting **Tools \> Device
   Manager** . Click **Create device**.
5. In the **Category** pane, select **Wear OS**.
6. Select a hardware profile (for example, **Wear OS Large Round** or **Wear
   OS Small Round** ) and click **Next**.
7. Select a Wear OS 7 system image to download:
   - In the **SDK Platforms** tab (or recommended tab), select the system image for **Wear OS 7.0** (**API Level 37**).
   - Ensure to specify the architecture (e.g., `ARM 64 v8a` or `Intel
     x86_64` depending on the developer's host machine).
   - If not installed, click **Download** next to the release name.
8. Once downloaded, select the image, click **Next** , and then **Finish**.

![Android Studio showing the Wear OS 7 system image selection](https://developer.android.com/static/training/wearables/versions/7/images/wear7-emulator-setup.png) Select the Wear OS 7.0 system image in Android Studio.

### Pre-installed experiences

The Wear OS 7 emulator includes a variety of pre-installed applications, watch
faces, and widgets to help you test your app's integration with the system.

#### Applications

- Contacts
- Find Hub
- Find my phone
- Flashlight
- Media Controls
- Messages
- Phone
- Play Store
- Settings

#### Watch faces

- Offhand
- Perfunctory
- Superficial

#### Widgets

- Favorites
- Contact

## Update your app to target Wear OS 7

After you [update your app](https://developer.android.com/training/wearables/versions/7/changes) to prepare it for Wear OS 7, you can further
improve your app's compatibility by targeting Wear OS 7 (API level 37), which is
based on Android 17, or higher.

If you update your target SDK version, handle the system behavior changes that
take effect for apps that [target Android 17 or higher](https://developer.android.com/about/versions/17/behavior-changes-17).

> [!NOTE]
> **Note:** If you publish your Wear OS app to Google Play, you must [target a
> sufficiently recent version of the platform](https://support.google.com/googleplay/android-developer/answer/11926878).

### Update your build file

To update your target SDK version, open your module-level `build.gradle` or
`build.gradle.kts` file, and update them with the following values for Wear OS 7
(Android 17):

### Groovy

    android {
        compileSdk 37
        ...
        defaultConfig {
            targetSdk 37
        }
    }

### Kotlin

    android {
        compileSdk = 37
        ...
        defaultConfig {
            targetSdk = 37
        }
    }