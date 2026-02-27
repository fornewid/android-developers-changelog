---
title: https://developer.android.com/about/versions/16/qpr2/setup-sdk
url: https://developer.android.com/about/versions/16/qpr2/setup-sdk
source: md.txt
---

To develop with Android 16 QPR2 APIs and test your app with the Android 16 QPR2
behavior changes, you need to set up the Android 16 QPR2 SDK. Follow the
instructions on this page to set up the Android 16 QPR2 SDK in Android Studio
and build and run your app on Android 16 QPR2.

## Get Android Studio

The Android 16 QPR2 SDK includes changes that are not compatible with some lower
versions of Android Studio. For the best
development experience with the Android 16 QPR2 SDK, use the [latest preview
version](https://developer.android.com/studio/preview) of Android Studio. Remember that you can keep your existing version
of Android Studio installed, as you can [install multiple versions
side-by-side](https://developer.android.com/studio/preview/install-preview).

<br />

[Get Android Studio](https://developer.android.com/studio/preview)

## Update your app's build configuration

> [!WARNING]
> **Warning:** If your project does not use Android Gradle plugin 8.13.0 or higher, first run the [Android Gradle plugin Upgrade Assistant](https://developer.android.com/r/tools/upgrade-assistant/agp-upgrade-assistant) to upgrade to at least AGP 8.13.0.

To access Android 16 QPR2 APIs, open your app's `build.gradle` or
`build.gradle.kts` file and update the `compileSdk` for Android 16 QPR2 as
follows:

### Groovy

```groovy
android {
    compileSdk {
        version = release(36) {
            it.minorApiLevel = 1
        }
    }
}
```

### Kotlin

```kotlin
android {
    compileSdk {
        version = release(36) {
            minorApiLevel = 1
        }
    }
}
```

### Manually install the SDK

Within Android Studio, you can install the Android 16 QPR2 SDK as follows:

1. Click **Tools \> SDK Manager**.
2. In the **SDK Platforms tab** , expand the **Android 16.0 ("Baklava")** section and select the **Android SDK Platform 36.1** package.
3. In the **SDK Tools** tab, expand the **Android SDK Build-Tools 36** section and select the latest `36.x.x` version. These labels might have a suffix such as **rc1** or **rc2**.
4. Click **OK** to install the SDK.