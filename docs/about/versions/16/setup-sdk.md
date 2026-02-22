---
title: https://developer.android.com/about/versions/16/setup-sdk
url: https://developer.android.com/about/versions/16/setup-sdk
source: md.txt
---

To develop with Android 16 APIs and test your app with the Android 16 behavior
changes, you need to set up the Android 16 SDK. Follow the instructions on this
page to set up the Android 16 SDK in Android Studio and build and run your app
on Android 16.

## Get Android Studio

The Android 16 SDK includes changes that are not compatible with some lower
versions of Android Studio. For the best development experience with the Android
16 SDK, use Android Studio Meerkat \| 2024.3.1 or higher.

<br />

[Get Android Studio](https://developer.android.com/studio)

## Update your app's build configuration

| **Warning:** If your project does not use Android Gradle plugin 8.9.0-rc01 or higher, first run the [Android Gradle plugin Upgrade Assistant](https://developer.android.com/r/tools/upgrade-assistant/agp-upgrade-assistant) to upgrade to at least AGP 8.9.0-rc01.

To access Android 16 APIs, open your app's `build.gradle` or `build.gradle.kts`
file and update the `compileSdk` for Android 16 as follows:  

### Groovy

```groovy
android {
    compileSdk = 36
}
```

### Kotlin

```kotlin
android {
    compileSdk = 36
}
```

Android Studio can provide contextual information about the
behavior changes through the
[Android SDK Upgrade Assistant](https://developer.android.com/r/studio-ui/ide/android-sdk-upgrade-assistant).
Once you're ready to opt in to the new runtime behaviours for Android 16,
update your app's `targetSdk` as follows:  

### Groovy

```groovy
android {
    defaultConfig {
        targetSdk = 36
    }
}
```

### Kotlin

```kotlin
android {
    defaultConfig {
        targetSdk = 36
    }
}
```

### Manually install the SDK

Within Android Studio, you can install the Android 16 SDK as follows:

1. Click **Tools \> SDK Manager**.
2. In the **SDK Platforms tab** , expand the **Android Baklava Preview** section and select the **Android SDK Platform Baklava** package.
3. In the **SDK Tools** tab, expand the **Android SDK Build-Tools 36** section and select the latest `36.x.x` version.
4. Click **OK** to install the SDK.

## Next steps

To learn about the changes that might affect your app, and to learn how to test
these changes in your app, read the following topics:

- [Behavior changes that affect all apps](https://developer.android.com/about/versions/16/behavior-changes-all)
- [Behavior changes that affect only apps that target Android 16](https://developer.android.com/about/versions/16/behavior-changes-16)

To learn more about new APIs and features available in Android 16, read [Android
16 features](https://developer.android.com/about/versions/16/features).