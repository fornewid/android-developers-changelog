---
title: https://developer.android.com/about/versions/14/setup-sdk
url: https://developer.android.com/about/versions/14/setup-sdk
source: md.txt
---

# Set up the Android 14 SDK

To develop with Android 14 APIs and test your app with the Android 14 behavior changes, you need to set up the Android 14 SDK. Follow the instructions on this page to set up the Android 14 SDK in Android Studio and build and run your app on Android 14.

## Get Android Studio

The Android 14 SDK includes changes that are not compatible with some lower versions of Android Studio. For the best development experience with the Android 14 SDK, use Android Studio Flamingo \| 2022.2.1 or higher.

<br />

[Get Android Studio](https://developer.android.com/studio)

## Install the SDK

Within Android Studio, you can install the Android 14 SDK as follows:

1. Click**Tools \> SDK Manager** , then click**Show Package Details**.
2. In the**SDK Platforms** tab, expand the**Android 14.0 ("UpsideDownCake")** section and select the**Android SDK Platform 34**package.
3. In the**SDK Tools** tab, expand the**Android SDK Build-Tools 34** section and select the latest`34.x.x`version.
4. Click**Apply \> OK**to download and install the selected packages.

## Update your app's build configuration

To access Android 14 APIs and test your app's compatibility with Android 14, open your module-level`build.gradle`or`build.gradle.kts`file, and update them with values for Android 14. How you format the values depends on the version of the Android Gradle plugin (AGP) that you are using.
| **Note:** If you aren't quite ready to fully support Android 14, you can still perform app compatibility testing by using a debuggable app, an Android 14 device, and the[compatibility framework](https://developer.android.com/about/versions/14/reference/compat-framework-changes), without changing your app to compile with or target the SDK.

### AGP 7.0.0 or higher

If you are using AGP 7.0.0 or higher, update your app's`build.gradle`or`build.gradle.kts`file with the following values for Android 14:  

### Groovy

```groovy
android {
    compileSdk 34
    ...
    defaultConfig {
        targetSdk 34
    }
}
```

### Kotlin

```kotlin
android {
    compileSdk = 34
    ...
    defaultConfig {
        targetSdk = 34
    }
}
```

### AGP 4.2.0 or lower

If you are using AGP 4.2.0 or lower, update your app's`build.gradle`or`build.gradle.kts`file with the following values for Android 14:  

### Groovy

```groovy
android {
    compileSdkVersion "34"
    ...
    defaultConfig {
        targetSdkVersion "34"
    }
}
```

### Kotlin

```kotlin
android {
    compileSdkVersion = "34"
    ...
    defaultConfig {
        targetSdkVersion = "34"
    }
}
```

## Next steps

To learn about the changes that might affect your app, and to learn how to test these changes in your app, read the following topics:

- [Behavior changes that affect all apps](https://developer.android.com/about/versions/14/behavior-changes-all)
- [Behavior changes that affect only apps that target Android 14](https://developer.android.com/about/versions/14/behavior-changes-14)

To learn more about new APIs and features available in Android 14, read[Android 14 features](https://developer.android.com/about/versions/14/features).