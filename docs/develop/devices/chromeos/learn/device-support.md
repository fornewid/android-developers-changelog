---
title: https://developer.android.com/develop/devices/chromeos/learn/device-support
url: https://developer.android.com/develop/devices/chromeos/learn/device-support
source: md.txt
---

You can use the Google Play Store to install Android apps on several Google
Chromebooks. This document describes the Chromebooks, Chromeboxes, and
Chromebases on which you can install Android apps.

## Overview


Most Android phones have ARM chipsets. However, many ChromeOS devices use x86 chips.
The difference is not important for basic apps written in Kotlin or Java. However, for apps written in C/C++ code, including those created with game
engines, the chipset in the device can be an important concern.


Ideally, all apps and games with C/C++ code ship with all four major Android
[ABIs (Application Binary Interfaces)](https://developer.android.com/ndk/guides/abis):
armeabi-v7a (arm32), arm64-v8a (arm64), x86 (x86_32), and x86_64. This provides the best performance
and lowest battery consumption for each device. For example, a cmake-based `build.gradle`
file might contain:  

### Groovy

```groovy
externalNativeBuild {
    cmake {
        abiFilters 'armeabi-v7a', 'arm64-v8a', 'x86', 'x86_64'
    }
}
```

### Kotlin

```kotlin
externalNativeBuild {
    cmake {
        abiFilters("armeabi-v7a", "arm64-v8a", "x86", "x86_64")
    }
}
```

## Android Package Kit (APK) size


Each ABI in a monolithic APK increases its size. This can affect your users' disk usage, the app download size, and whether the app is affected
by the Play Store size limits. The best way to avoid this is to use
[Android App Bundles](https://developer.android.com/guide/app-bundle).


App Bundles
let you bundle all four ABIs from within Android Studio without increasing the
download size for your users. They also help you take advantage of [Dynamic Delivery](https://developer.android.com/guide/app-bundle/dynamic-delivery),
letting users download large game content only when requested. If App Bundles are not a possibility
for you, you can use the older [multi-APK](https://developer.android.com/google/play/publishing/multiple-apks) for
similar behaviour.

## 32-bit and 64-bit builds


All Android apps must provide a 64-bit build version. A 32-bit build is optional for both ARM and
x86 devices. See the [Android 64-bit⁠](https://developer.android.com/distribute/best-practices/develop/64-bit) for more information.


While only providing 64-bit builds reduces the number of build targets needed and your
testing surface, it also limits the kinds of devices that can run your game.
For
example, due to other hardware limitations, many older Chromebooks can only run 32-bit Android
apps, despite having 64-bit CPUs. To ensure your app can run on these devices, include
both 32 and 64-bit support.

## ARM translation


x86 Chromebooks try to translate ARM code whenever possible, but
translation slows performance and increases battery usage. For the best user
experience, provide x86 builds. If you can't, then include both arm32 and arm64 ABIs in
your builds, because some x86 Chromebooks might not translate arm64 code. example, due to other hardware limitations, many older Chromebooks can only run 32-bit Android
apps, despite having 64-bit CPUs. To help your app run on these devices, include
both 32 and 64-bit support.


Although arm32 translation is available on all Android-capable Chromebooks, not all Chromebooks
can translate arm64 code. This means that if your game only has arm64 build targets,
it isn't available for a large number of ChromeOS devices. If you are unable to ship
x86 binaries, include both arm32 and arm64 ABIs in your builds.

| Included ABIs | Support for ChromeOS |
|---|---|
| arm64 | Poor |
| arm32 and arm64 | OK (with translation) |
| arm32, arm64, x86_32, and x86_64 | Best |