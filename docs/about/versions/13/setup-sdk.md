---
title: https://developer.android.com/about/versions/13/setup-sdk
url: https://developer.android.com/about/versions/13/setup-sdk
source: md.txt
---

# Set up the Android 13 SDK

To develop with Android 13 APIs and test your app with the Android 13 behavior changes, you need to set up the Android 13 SDK. Follow the instructions on this page to set up the Android 13 SDK in Android Studio and build and run your app on Android 13.

## Get Android Studio

The Android 13 SDK includes changes that are not compatible with some lower versions of Android Studio. For the best development experience with the Android 13 SDK, use Android Studio Chipmunk \| 2021.2.1 or higher.

[Get Android Studio](https://developer.android.com/studio)

## Install the SDK

Within Android Studio, you can install the Android 13 SDK as follows:

1. Click**Tools \> SDK Manager** , then click**Show Package Details**.
2. In the**SDK Platforms** tab, expand the**Android 13.0 ("Tiramisu")** section and select the**Android SDK Platform 33**package.
3. In the**SDK Tools** tab, expand the**Android SDK Build-Tools 34** section and select the latest`33.x.x`version.
4. Click**Apply \> OK**to download and install the selected packages.

## Update your app's build configuration

To access Android 13 APIs and test your app's compatibility with Android 13, open your module-level`build.gradle`or`build.gradle.kts`file, and update them with values for Android 13. How you format the values depends on the version of the Android Gradle plugin (AGP) that you are using.
| **Note:** If you aren't quite ready to fully support Android 13, you can still perform app compatibility testing by using a debuggable app, an Android 13 device, and the[compatibility framework](https://developer.android.com/about/versions/13/reference/compat-framework-changes), without changing your app to compile with or target the SDK.

### AGP 7.0.0 or higher

If you are using AGP 7.0.0 or higher, update your app's`build.gradle`or`build.gradle.kts`file with the following values for Android 13:  

### Groovy

```groovy
android {
    compileSdk 33

    defaultConfig {
        targetSdk 33
    }
}
```

### Kotlin

```kotlin
android {
    compileSdk = 33

    defaultConfig {
        targetSdk = 33
    }
}
```

### AGP 4.2.0 or lower

If you are using AGP 4.2.0 or lower, update your app's`build.gradle`or`build.gradle.kts`file with the following values for Android 13:  

### Groovy

```groovy
android {
    compileSdkVersion "33"

    defaultConfig {
        targetSdkVersion "33"
    }
}
```

### Kotlin

```kotlin
android {
    compileSdkVersion = "33"

    defaultConfig {
        targetSdkVersion = "33"
    }
}
```

## Next steps

To learn about which changes might affect you, and to learn how to test these changes in your app, read the following topics:

- [Behavior changes that affect all apps](https://developer.android.com/about/versions/13/behavior-changes-all)
- [Behavior changes that affect only apps that target Android 13](https://developer.android.com/about/versions/13/behavior-changes-13)

To learn more about new APIs and features available in Android 13, read[Android 13 features](https://developer.android.com/about/versions/13/features).