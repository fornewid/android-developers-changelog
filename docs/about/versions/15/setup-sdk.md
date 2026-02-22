---
title: https://developer.android.com/about/versions/15/setup-sdk
url: https://developer.android.com/about/versions/15/setup-sdk
source: md.txt
---

# Set up the Android 15 SDK

To develop with Android 15 APIs and test your app with the Android 15 behavior changes, you need to set up the Android 15 SDK. Follow the instructions on this page to set up the Android 15 SDK in Android Studio and build and run your app on Android 15.

## Get Android Studio

The Android 15 SDK includes changes that are not compatible with some lower versions of Android Studio. For the best development experience with the Android 15 SDK, use Android Studio Koala Feature Drop \| 2024.1.2 or higher.

<br />

[Get Android Studio](https://developer.android.com/studio)

## Try out Android 15

If you aren't quite ready to fully support Android 15, you can still perform app compatibility testing by using a debuggable app, an Android 15 device (including[virtual devices](https://developer.android.com/studio/run/managing-avds)), and the[compatibility framework](https://developer.android.com/about/versions/15/reference/compat-framework-changes), without changing your app to compile with or target the SDK.

## Update your app's build configuration

| **Warning:** If your project does not use Android Gradle plugin 8.6.1 or higher, first run the[Android Gradle plugin Upgrade Assistant](https://developer.android.com/r/tools/upgrade-assistant/agp-upgrade-assistant)to upgrade to at least AGP 8.6.1.

To access Android 15 APIs, open your app's`build.gradle`or`build.gradle.kts`file and update the`compileSdk`for Android 15 as follows:  

### Groovy

```groovy
android {
    compileSdk = 35
}
```

### Kotlin

```kotlin
android {
    compileSdk = 35
}
```

Android Studio can provide contextual information about the behavior changes through the[Android SDK Upgrade Assistant](https://developer.android.com/r/studio-ui/ide/android-sdk-upgrade-assistant). Once you're ready to opt in to the new runtime behaviours for Android 15, update your app's`targetSdk`as follows:  

### Groovy

```groovy
android {
    defaultConfig {
        targetSdk = 35
    }
}
```

### Kotlin

```kotlin
android {
    defaultConfig {
        targetSdk = 35
    }
}
```

## Manually install the SDK

Within Android Studio, you can install the Android 15 SDK as follows:

1. Click**Tools \> SDK Manager** , then click**Show Package Details**.
2. In the**SDK Platforms tab** , expand the**Android API 35** section and select the**Android SDK Platform 35**package.
3. In the**SDK Tools** tab, expand the**Android SDK Build-Tools 35** section and select the latest`35.x.x`version.
4. Click**OK**to install the SDK.

## Next steps

To learn about the changes that might affect your app, and to learn how to test these changes in your app, read the following topics:

- [Behavior changes that affect all apps](https://developer.android.com/about/versions/15/behavior-changes-all)
- [Behavior changes that affect only apps that target Android 15](https://developer.android.com/about/versions/15/behavior-changes-15)

To learn more about new APIs and features available in Android 15, read[Android 15 features](https://developer.android.com/about/versions/15/features).