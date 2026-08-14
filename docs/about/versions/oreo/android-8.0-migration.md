---
title: https://developer.android.com/about/versions/oreo/android-8.0-migration
url: https://developer.android.com/about/versions/oreo/android-8.0-migration
source: md.txt
---

Android 8.0 (API level 26) introduces behavior changes as well as new features and APIs that
you can take advantage of in your apps. This document gives you an overview of the steps to migrate
your apps to Android 8.0 across two key phases:

1. [Ensure compatibility with Android 8.0](https://developer.android.com/about/versions/oreo/android-8.0-migration#ct)

   Verify that your app is fully functional on the new version of the platform. At this stage,
   you do not use new APIs or change your app's `targetSdkVersion`, but minor changes
   might be necessary.
2. [Update your target version and use Android 8.0 features](https://developer.android.com/about/versions/oreo/android-8.0-migration#bfa)

   When you are ready to take advantage of the new features of
   the platform, update your `targetSdkVersion` to 26, verify the app continues
   to function as expected, and then begin using new APIs.

## Ensure compatibility with Android 8.0

The objective here is to make sure that your existing app works as-is on Android 8.0
(API level 26). Because some platform changes might affect the way your app behaves,
some adjustments might be necessary, but you do not need to use new APIs or
change your `targetSdkVersion`.
![Ensure compatibility with Android 8.0 step-by-step](https://developer.android.com/static/images/about/versions/oreo/o-compat-flow-mobile.svg)

### Prepare a device running Android 8.0

- If you have a compatible device (Pixel, Pixel XL, Pixel C, Nexus 5X, Nexus 6P, or Nexus Player), follow the [instructions
  to flash your device](https://developers.google.com/android/images#instructions).
- Or download the Android 8.0 system image for the Android Emulator. It's listed in the [SDK Manager](https://developer.android.com/studio/intro/update#sdk-manager) under **Android 8.0** as **Google APIs Intel x86 Atom System Image** .

  **Note:** The Android 8.0 system image is available for download from
  [Android Studio 3.0](https://developer.android.com/studio/preview) and higher.
  For more information, see the section below to [get the Android 8.0 SDK](https://developer.android.com/about/versions/oreo/android-8.0-migration#ptb).

### Perform compatibility testing

For the most part, testing compatibility with Android 8.0 (API level 26)
entails the same type of testing you perform when preparing to release your app. This is a good time to review the [Core App Quality Guidelines](https://developer.android.com/develop/quality-guidelines/core-app-quality) and [Best Practices for Testing](https://developer.android.com/training/testing).

However, there's another aspect to testing: Android 8.0 introduces changes to the Android
platform that can affect your app's behavior or break the app altogether, even if you do not change
your `targetSdkVersion`. For this reason, it is important that you review the key changes
in table 1, and test any fixes that you implement to accommodate the changes.

**Table 1.** Key changes that affect all apps
running on Android 8.0 devices.

| Change | Summary | Further reference |
|---|---|---|
| Less frequent background location updates | If your app receives location updates from a background service, it receives less frequent updates on Android 8.0 (API level 26) compared to older versions of Android. Specifically, a background service cannot receive location updates more than a few times per hour. However, while your app is in the foreground, the rate of location updates is unchanged. | [Background Location Limits](https://developer.android.com/about/versions/oreo/background-location-limits) |
| `net.hostname` no longer supported | Querying the `net.hostname` system property produces a null result. | None |
| New exception from `https://developer.android.com/reference/java/net/DatagramSocket#send(java.net.DatagramPacket)` | The `https://developer.android.com/reference/java/net/DatagramSocket#send(java.net.DatagramPacket)` method throws a `https://developer.android.com/reference/java/net/SocketException` if the previously executed `https://developer.android.com/reference/java/net/DatagramSocket#connect(java.net.InetAddress, int)` method failed. | [Behavior Changes: Network and HTTP(S) connectivity](https://developer.android.com/about/versions/oreo/android-8.0-changes#networking-all) |
| Proper `https://developer.android.com/reference/java/lang/NullPointerException` from `https://developer.android.com/reference/java/util/AbstractCollection` methods | `https://developer.android.com/reference/java/util/AbstractCollection#removeAll(java.util.Collection<?>)` and `https://developer.android.com/reference/java/util/AbstractCollection#retainAll(java.util.Collection<?>)` now always throw a `https://developer.android.com/reference/java/lang/NullPointerException`; previously, the `https://developer.android.com/reference/java/lang/NullPointerException` was not thrown when the collection was empty. This change makes the behavior consistent with the documentation. | [Behavior Changes: Collection handling](https://developer.android.com/about/versions/oreo/android-8.0-changes#ch-all) |
| Proper `https://developer.android.com/reference/java/lang/NullPointerException` from `https://developer.android.com/reference/android/icu/util/Currency#getDisplayName()` | Calling `https://developer.android.com/reference/android/icu/util/Currency#getDisplayName()` throws a `https://developer.android.com/reference/java/lang/NullPointerException`. | [Behavior Changes: Locales and internationalization](https://developer.android.com/about/versions/oreo/android-8.0-changes#lai) |


For a more extensive list of behavior changes in Android 8.0
(API level 26), also
see [Android 8.0 Behavior Changes](https://developer.android.com/about/versions/oreo/android-8.0-changes).

## Update your target version and use Android 8.0 features

This section explains how to enable full support for Android 8.0
(API level 26) by updating your `targetSdkVersion` to 26
and adding new features available in Android 8.0.

In addition to offering you new APIs, Android 8.0 introduces some behavior
changes when you update your `targetSdkVersion` to 26. Because some behavior changes
might require code changes to avoid breakage, you should first understand how your app might be
affected when you change the `targetSdkVersion` by reviewing all [behavior changes for apps targeting Android 8.0](https://developer.android.com/about/versions/oreo/android-8.0-changes#o-apps).

**Note:** The steps described above to
[ensure platform compatibility](https://developer.android.com/about/versions/oreo/android-8.0-migration#ec) are prerequisite
to targeting your app to Android 8.0, so be sure you complete those steps first.
![Update target version and use Android 8.0 features step-by-step](https://developer.android.com/static/images/about/versions/oreo/o-building-flow-mobile.svg)

### Get the Android 8.0 SDK

You can get the SDK packages to build your app with Android 8.0
(API level 26) using the latest version of
[Android Studio](https://developer.android.com/studio) (Android Studio 3.0+ is recommended).
Android Studio 3.0+ includes tools to help you with Android 8.0 features
such as [adaptive icons](https://developer.android.com/guide/practices/ui_guidelines/icon_design_adaptive) and
[downloadable fonts](https://developer.android.com/guide/topics/ui/look-and-feel/downloadable-fonts).
If you don't need those features yet, then you can use the stable version of Android Studio
2.3.3 to build your app with Android 8.0 and use the new APIs.

To get set up with either version of Android Studio, follow these steps:

1. Launch Android Studio and open the SDK Manager by clicking **Tools \> SDK Manager**.
2. In the **SDK Platforms** tab, check **Show Package Details** . Below **Android 8.0 Preview** check the following:
   - **Android SDK Platform 26**
   - **Google APIs Intel x86 Atom System Image** (only required for the emulator)
3. Switch to the **SDK Tools** tab and check all items that have updates available (click each checkbox that shows a dash ![](https://developer.android.com/static/studio/images/sdk-manager-icon-update_2-0_2x.png)). This should include the latest versions of the following items that are required:
   - **Android SDK Build-Tools 26.0.0**
   - **Android SDK Platform-Tools 26.0.0**
   - **Android Emulator 26.0.0**
4. Click **OK** to install all the selected SDK packages.

Now you're ready to start building with Android 8.0.

### Update your build configuration


Update `compileSdkVersion`,
`targetSdkVersion`, and the Support Library version to the latest
available revisions, for example:

```
android {
  compileSdkVersion 26

  defaultConfig {
    targetSdkVersion 26
  }
  ...
}

dependencies {
  compile 'com.android.support:appcompat-v7:26.0.0'
}

// REQUIRED: https://developer.android.com/studio/build/dependencies#google-maven is required for the latest
// support library that is compatible with Android 8.0
repositories {
    google()

    // If you're using a version of Gradle lower than 4.1, you must instead use:
    // maven {
    //     url 'https://maven.google.com'
    // }
}
```

### Remove broadcast receivers from your manifest file

Because Android 8.0 (API level 26) introduces new
[limitations
for broadcast receivers](https://developer.android.com/about/versions/oreo/background#broadcasts), you should remove any broadcast receivers that are
registered for *implicit* broadcast intents. Leaving them in place does not break your app
at build-time or runtime, but they have no effect when your app runs on Android 8.0.

Broadcasts that only your app can respond to---*Explicit* broadcast intents and
broadcasts sent to your app's package name specifically---continue to work the same on
Android 8.0.

There are exceptions to this new restriction. For a
list of implicit broadcasts that still work in apps targeting Android 8.0, see [Implicit Broadcast Exceptions](https://developer.android.com/guide/components/broadcast-exceptions).

### Test your Android 8.0 app


With the above preparations complete, you can build your app and then test
it further to make sure it works properly when targeting Android 8.0
(API level 26). This is another good time to review the
[Core App
Quality Guidelines](https://developer.android.com/develop/quality-guidelines/core-app-quality) and [Best
Practices for Testing](https://developer.android.com/training/testing).


When you build your app with the `targetSdkVersion` set to 26,
there are specific platform changes you should be aware of. Some of
these changes can significantly affect your app's behavior or even
break your app altogether, even if you do not implement new
features in Android 8.0.

Table 2 provides a list of these changes with links to more information.

**Table 2.** Key changes that affect apps
when `targetSdkVersion` is set to 26.

| Change | Summary | Further reference |
|---|---|---|
| Privacy | Android 8.0 (API level 26) does not support use of the net.dns1, net.dns2, net.dns3, or net.dns4 system properties. | [Behavior Changes: Privacy](https://developer.android.com/about/versions/oreo/android-8.0-changes#pr) |
| Writable and Executable Segments Enforced | For native libraries, Android 8.0 (API level 26) enforces the rule that data shouldn't be executable, and code shouldn't be writable. | [Behavior Changes: Native Libraries](https://developer.android.com/about/versions/oreo/android-8.0-changes#ndk) |
| ELF header and section validation | The dynamic linker checks more values in the ELF header and section headers, and fails if they are invalid. | [Behavior Changes: Native Libraries](https://developer.android.com/about/versions/oreo/android-8.0-changes#ndk) |
| Notifications | Apps targeting the Android 8.0 (API level 26) version of the SDK must implement one or more notification channels to post notifications to users. | [API Overview: Notifications](https://developer.android.com/about/versions/oreo/android-8.0#notifications) |
| The `https://developer.android.com/reference/java/util/List#sort(java.util.Comparator<? super E>)` method | Implementations of this method may no longer call `https://developer.android.com/reference/java/util/Collections#sort(java.util.List<T>)`, or your app will throw an exception due to stack overflow. | [Behavior Changes: Collection handling](https://developer.android.com/about/versions/oreo/android-8.0-changes#o-ch) |
| The `https://developer.android.com/reference/java/util/Collections#sort(java.util.List<T>)` method | In List implementations, `https://developer.android.com/reference/java/util/Collections#sort(java.util.List<T>)` now throws a `https://developer.android.com/reference/java/util/ConcurrentModificationException`. | [Behavior Changes: Collection handling](https://developer.android.com/about/versions/oreo/android-8.0-changes#o-ch) |


For a more extensive list of behavior changes in Android 8.0 (API level 26),
see [Android 8.0 Behavior Changes](https://developer.android.com/about/versions/oreo/android-8.0-changes).

To explore the new features and APIs available with Android 8.0 (API level 26), see
[Android 8.0 Features and APIs](https://developer.android.com/about/versions/oreo/android-8.0-changes).