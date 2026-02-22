---
title: https://developer.android.com/about/versions/12/12L/setup-sdk
url: https://developer.android.com/about/versions/12/12L/setup-sdk
source: md.txt
---

# Set up the 12L SDK

To develop with the 12L APIs and test your app, you need to set up the 12L SDK. Follow the instructions on this page to set up the Android 12 SDK in Android Studio and build and run your app on 12L.

## Get Android Studio

The 12L SDK includes changes that are not compatible with some lower versions of Android Studio. For the best development experience with the 12L SDK, use Android Studio Chipmunk \| 2021.2.1 or higher.

[Get Android Studio](https://developer.android.com/studio)

## Install the SDK

Within Android Studio, you can install the 12L SDK as follows:

1. Click**Tools \> SDK Manager** , then click**Show Package Details**.
2. In the**SDK Platforms** tab, expand the**Android 12L ("Sv2")** section and select the**Android SDK Platform 32**package.
3. In the**SDK Tools** tab, expand the**Android SDK Build-Tools 34** section and select the latest`32.x.x`version.
4. Click**Apply \> OK**to download and install the selected packages.

## Update your app's build configuration

To access 12L APIs and test your app's compatibility with 12L, open your module-level`build.gradle`or`build.gradle.kts`file, and update the`compileSdkVersion`and`targetSdkVersion`with values for 12L:  

### Groovy

```groovy
android {
    compileSdkVersion "32"

    defaultConfig {
        targetSdkVersion "32"
    }
}
```

### Kotlin

```kotlin
android {
    compileSdkVersion("32")

    defaultConfig {
        targetSdkVersion("32")
    }
}
```

To learn more about the features and changes in 12L, see[12L features and changes](https://developer.android.com/about/versions/12/12L/summary).