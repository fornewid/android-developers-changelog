---
title: https://developer.android.com/about/versions/12/setup-sdk
url: https://developer.android.com/about/versions/12/setup-sdk
source: md.txt
---

# Set up the Android 12 SDK

To develop with Android 12 APIs and test your app with the Android 12 behavior changes, you need to set up the Android 12 SDK. Follow the instructions on this page to set up the Android 12 SDK in Android Studio and build and run your app on Android 12.

## Get Android Studio

The Android 12 SDK includes changes that are not compatible with some lower versions of Android Studio. For the best development experience with the Android 12 SDK, use Android Studio Arctic Fox \| 2020.3.1 or higher.

[Get Android Studio](https://developer.android.com/studio)

## Install the SDK

Within Android Studio, you can install the Android 12 SDK as follows:

1. Click**Tools \> SDK Manager** , then click**Show Package Details**.
2. In the**SDK Platforms** tab, expand the**Android 12.0 ("S")** section and select the**Android SDK Platform 31**package.
3. In the**SDK Tools** tab, expand the**Android SDK Build-Tools 34** section and select the latest`31.x.x`version.
4. Click**Apply \> OK**to download and install the selected packages.

## Update your app's build configuration

To access Android 12 APIs and test your app's compatibility with Android 12, open your module-level`build.gradle`or`build.gradle.kts`file, and update the`compileSdkVersion`and`targetSdkVersion`with values for Android 12:  

### Groovy

```groovy
android {
    compileSdkVersion 31

    defaultConfig {
        targetSdkVersion 31
    }
}
```

### Kotlin

```kotlin
android {
    compileSdkVersion(31)

    defaultConfig {
        targetSdkVersion(31)
    }
}
```
| **Note:** If you aren't quite ready to fully support Android 12, you can still perform app compatibility testing by using a debuggable app, an Android 12 device, and the[compatibility framework](https://developer.android.com/about/versions/12/reference/compat-framework-changes), without changing either your app's`compileSdkVersion`or`targetSdkVersion`.

To learn about which changes might affect you, and to learn how to test these changes in your app, read the following topics:

- [Behavior changes that affect all apps](https://developer.android.com/about/versions/12/behavior-changes-all)
- [Behavior changes that affect only apps that target Android 12](https://developer.android.com/about/versions/12/behavior-changes-12)

To learn more about new APIs and features available in Android 12, read[Android 12 features](https://developer.android.com/about/versions/12/features).