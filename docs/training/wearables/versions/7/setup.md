---
title: https://developer.android.com/training/wearables/versions/7/setup
url: https://developer.android.com/training/wearables/versions/7/setup
source: md.txt
---

This page explains how to set up the official emulator for testing, and how to
upgrade your app to target Wear OS 7.

## Set up an emulator

Following the same process as for mobile devices, use the Wear OS 7 emulator to
test behavior changes and explore new features in Wear OS 7.

To set up the Wear OS 7 emulator, follow the instructions to
[Create a Wear OS virtual device](https://developer.android.com/training/wearables/get-started/creating), taking note of the following
requirements:

- Use [Android Studio Canary](https://developer.android.com/studio/preview). Accessing Canary versions of the Wear OS 7 emulator requires an Android Studio release from the Canary channel.
- Select the **Wear OS 7.0 - Preview** system image when creating the virtual device.

![Android Studio showing the Wear OS 7 system image selection](https://developer.android.com/static/training/wearables/versions/7/images/emulator-setup.png) Select the Wear OS 7.0 --- Preview system image in Android Studio.

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