---
title: https://developer.android.com/ndk/guides/sdk-versions
url: https://developer.android.com/ndk/guides/sdk-versions
source: md.txt
---

# Android SDK version properties

Android applications can set a number of SDK version properties in their`build.gradle`file. The[Android`build.gradle`](https://developer.android.com/studio/build#module-level)documentation explains what those properties mean for the application in general. This document explains how those properties affect NDK builds.

## compileSdkVersion

This property has no effect on NDK builds. API availability for the NDK is instead governed by`minSdkVersion`. This is because C++ symbols are eagerly resolved at library load time rather than lazily resolved when first called (as they are in Java). Using any symbols that are not available in the`minSdkVersion`will cause the library to fail to load on OS versions that do not have the newer API, regardless of whether or not those APIs will be called.

For a new app, choose the newest version available. For an existing app, update this to the latest version when convenient.

## targetSdkVersion

Similar to Java, the`targetSdkVersion`of your app can change the runtime behavior of native code. Behavior changes in the system are, when feasible, only applied to apps with a`targetSdkVersion`greater than or equal to the OS version that introduced the change.

For a new app, choose the newest version available. For an existing app, update this to the latest version when convenient (after updating`compileSdkVersion`).

While application developers generally know their app's`targetSdkVersion`, this API is useful for library developers that cannot know which`targetSdkVersion`their users will choose.

At runtime, you can get the`targetSdkVersion`used by an application by calling`android_get_application_target_sdk_version()`. This API is available in API level 24 and later. This function has the following signature:  

    /**
     * Returns the `targetSdkVersion` of the caller, or `__ANDROID_API_FUTURE__` if
     * there is no known target SDK version (for code not running in the context of
     * an app).
     *
     * The returned values correspond to the named constants in `<android/api-level.h>`,
     * and is equivalent to the AndroidManifest.xml `targetSdkVersion`.
     *
     * See also android_get_device_api_level().
     *
     * Available since API level 24.
     */
    int android_get_application_target_sdk_version() __INTRODUCED_IN(24);

Other behavior changes might depend on the device API level. You can get the API level of the device your application is running on by calling`android_get_device_api_level()`. This function has the following signature:  

    /**
     * Returns the API level of the device we're actually running on, or -1 on failure.
     * The returned values correspond to the named constants in `<android/api-level.h>`,
     * and is equivalent to the Java `Build.VERSION.SDK_INT` API.
     *
     * See also android_get_application_target_sdk_version().
     */
    int android_get_device_api_level();

Getting device API levels allows NDK code to be dynamically aware of behavior changes in the platform. Since minor API levels aren't tied to behavior changes, and we have no current plans to add new NDK functionality in minor API levels, there is no way to get the full device API level directly from an NDK call.

You can make use of either`dlopen()`/`dlsym()`or weak API references to call newer APIs than what your`minSdkVersion`specifies.

## maxSdkVersion

This property has no effect on NDK builds.

## minSdkVersion

The`minSdkVersion`set in your`build.gradle`file determines which APIs are available at build time (see[compileSdkVersion](https://developer.android.com/ndk/guides/sdk-versions#compilesdkversion)to understand why this differs from Java builds), and determines the minimum version of the OS that your code will be compatible with.

The`minSdkVersion`is used by the NDK to determine what features may be used when compiling your code. For example, this property determines which[FORTIFY](https://android-developers.googleblog.com/2017/04/fortify-in-android.html)features are used in libc, and may also enable performance or size improvements (such as[GNU hashes](https://android.googlesource.com/platform/bionic/+/master/android-changes-for-ndk-developers.md#gnu-hashes-availible-in-api-level-23)or[RELR](https://android.googlesource.com/platform/bionic/+/master/android-changes-for-ndk-developers.md#relative-relocations-relr)) for your binaries that are not compatible with older versions of Android. Even if you do not use any new APIs, this property still governs the minimum supported OS version of your code.
| **Warning:** Your app*might* work on older devices even if your native libraries are built with a newer`minSdkVersion`.**Do not rely on this behavior.**It is not guaranteed to work, and may not on other NDK versions, OS versions, or individual devices.

For a new app, see the user distribution data in Android Studio's New Project Wizard or on[apilevels.com](https://apilevels.com). Choose your balance between potential market share and maintenance costs. The lower your`minSdkVersion`, the more time you'll spend working around old bugs and adding fallback behaviors for features that weren't implemented yet.

For an existing app, raise your`minSdkVersion`whenever old API levels are no longer worth the maintenance costs, or lower it if your users demand it and it's worth the new maintenance costs. The Play console has metrics specific to your app's user distribution.
| **Note:** The NDK has its own`minSdkVersion`defined in`<NDK>/meta/platforms.json`. This is the lowest API level supported by the NDK. Do not set your app's`minSdkVersion`lower than this. Play may allow your app to be installed on older devices, but your NDK code may not work.

The`minSdkVersion`of your application is made available to the preprocessor via the`__ANDROID_MIN_SDK_VERSION__`macro (the legacy`__ANDROID_API__`is identical, but prefer the former because its meaning is clearer). This macro is defined automatically by Clang, so no header needs to be included to use it. For NDK builds, this macro is always defined.