---
title: https://developer.android.com/training/wearables/versions/5/update-target-sdk
url: https://developer.android.com/training/wearables/versions/5/update-target-sdk
source: md.txt
---

# Update your app&#39;s target SDK version for Wear&nbsp;OS&nbsp;5

After you[update your app](https://developer.android.com/training/wearables/versions/5/changes)to prepare it for Wear OS 5, you can further improve your app's compatibility with this version of Wear OS by targeting Android 14 (API level 34).

If you update your target SDK version, handle the system behavior changes that take effect for apps that[target Android 14 or higher](https://developer.android.com/about/versions/14/behavior-changes-14).

## Update your build file

To update your target SDK version, open your module-level`build.gradle`or`build.gradle.kts`file, and update them with values for Android 14.

How you format the values in your build file depends on the version of the Android Gradle plugin (AGP) that you are using.

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

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Update your app's target SDK version for Wear OS 4](https://developer.android.com/training/wearables/versions/4/update-target-sdk)
- [Behavior changes: Apps targeting Android 12](https://developer.android.com/about/versions/12/behavior-changes-12)
- [Schedule alarms](https://developer.android.com/develop/background-work/services/alarms/schedule)