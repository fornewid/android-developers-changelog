---
title: https://developer.android.com/about/versions/pie/android-9.0-migration
url: https://developer.android.com/about/versions/pie/android-9.0-migration
source: md.txt
---

Android 9 (API level 28) introduces new features and APIs that
you can take advantage of in your apps, as well as new behavior changes.
This document gives you an overview of the steps to migrate
your apps to Android 9 across two key phases:

1. [Ensure basic compatibility with Android 9](https://developer.android.com/about/versions/pie/android-9.0-migration#ct)

   Verify that your existing app is fully functional on the new version of the platform.
   At this stage, you do not use new APIs or change your app's `targetSdkVersion`,
   but minor changes might be necessary.
2. [Target the new platform, compile with the Android 9 SDK, and
   build with Android 9 features](https://developer.android.com/about/versions/pie/android-9.0-migration#bfa)

   When you are ready to take advantage of the new features of
   the platform, update your `targetSdkVersion` to `28`, verify the app continues
   to function as expected, and then begin using new APIs.

## Prepare a device running Android 9

If you have a compatible device, obtain the
Android 9 system image for your device from the manufacturer; click here for
[factory images for
Pixel devices](https://developers.google.com/android/images). General instructions for
flashing a system image are [here](https://developers.google.com/android/images#instructions).

You can also download the Android 9 system image for the Android Emulator. It's listed in the
[SDK Manager](https://developer.android.com/studio/intro/update#sdk-manager) under
**Android API 28** as **Google APIs Intel x86 Atom System Image**.

**Note:** The Android 9 emulator system image is available for download in
[Android Studio 3.1](https://developer.android.com/studio/preview) and higher;
[Android Studio 3.2](https://developer.android.com/studio/preview) provides maximum compatibility.
For more information, see [Get the Android 9 SDK](https://developer.android.com/about/versions/pie/android-9.0-migration#ptb).

## Ensure compatibility with Android 9

The objective here is to make sure that your existing app works as-is on
Android 9. Because some platform changes might affect the way your app behaves,
some adjustments might be necessary, but you do not need to use new APIs or
change your `targetSdkVersion`.
![Ensure compatibility with Android 9 step-by-step](https://developer.android.com/static/images/about/versions/pie/o-compat-flow.svg)

### Perform compatibility testing

For the most part, testing compatibility with Android 9
entails the same type of testing you perform when preparing to release your app. This is a good time to review the [Core App Quality Guidelines](https://developer.android.com/develop/quality-guidelines/core-app-quality) and [Best Practices for Testing](https://developer.android.com/training/testing).

However, there's another aspect to testing: Android 9 introduces changes to the Android
platform that can affect your app's behavior or break the app altogether, even if you do not change
your `targetSdkVersion`. For this reason, it is important that you review the key changes
in table 1, and test any fixes that you implement to accommodate the changes.

**Table 1.** Key changes that affect all apps
running on Android 9 devices.

| Change | Summary |
|---|---|
| Restrictions on non-SDK interfaces | Access to specific non-SDK interfaces is now blocked, whether the access is direct, via JNI, or via reflection. Attempts to access restricted interfaces generates errors such as `NoSuchFieldException` and `NoSuchMethodException`. See [Restrictions on non-SDK interfaces](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces) for details. |
| Removal of Crypto provider | Starting in Android 9, Crypto JCA provider has been removed. Calls to `SecureRandom.getInstance("SHA1PRNG", "Crypto")` will throw `NoSuchProviderException`. |
| Stricter UTF-8 decoder | In Android 9, the UTF-8 decoder for Java language is stricter and follows the Unicode standard. |
| Access to camera, microphone, and sensors blocked for idle apps | While apps are idle, they can no longer access camera, microphone, or SensorManager sensors. |


For a more extensive list of behavior changes for all apps running on Android 9,
see [the Behavior Changes](https://developer.android.com/about/versions/pie/android-9.0-changes-all) document.

## Update your target version and use Android P features

This section explains how to enable full support for Android 9
by updating your `targetSdkVersion` to 28
and adding new features available in Android 9.

In addition to offering you new APIs, Android 9 introduces some behavior
changes when you update your `targetSdkVersion` to 28. Because some behavior changes
might require code changes to avoid breakage, you should first understand how your app might be
affected when you change the `targetSdkVersion` by reviewing all [behavior changes for apps targeting Android 9](https://developer.android.com/about/versions/pie/android-9.0-changes-28).

**Note:** The steps described above to
[ensure platform compatibility](https://developer.android.com/about/versions/pie/android-9.0-migration#tfc) are prerequisite
to targeting your app to Android 9, so be sure to complete those steps first.
![Update target version and use Android 9 features step-by-step](https://developer.android.com/static/images/about/versions/pie/o-building-flow.svg)

### Get the Android 9 SDK

You can get the SDK packages to build your app with Android 9
using [Android Studio 3.1](https://developer.android.com/studio/preview) or higher.
If you don't need the new features in Android 9 yet, and only want to compile against that
version of the platform, you can use [Android Studio 3.1](https://developer.android.com/studio/preview).
[Android Studio 3.2](https://developer.android.com/studio/preview) provides complete support for
Android 9 features.

### Test your Android 9 app


With the above preparations complete, you can build your app and then test
it further to make sure it works properly when targeting Android 9
(API level 28). This is another good time to review the
[Core App
Quality Guidelines](https://developer.android.com/develop/quality-guidelines/core-app-quality) and [Best
Practices for Testing](https://developer.android.com/training/testing).


When you build your app with the `targetSdkVersion` set to P,
there are specific platform changes you should be aware of. Some of
these changes can significantly affect your app's behavior or even
break your app altogether, even if you do not implement new
features in Android 9.

Table 2 provides a list of these changes with links to more information.

**Table 2.** Key changes that affect apps
when `targetSdkVersion` is set to 28.

| Change | Summary |
|---|---|
| Foreground service permission | Apps wanting to use foreground services must now request the FOREGROUND_SERVICE permission first. This is a normal permission, so the system automatically grants it to the requesting app. Starting a foreground service without the permission throws a SecurityException. |
| Deprecation of Bouncy Castle ciphers | Android 9 deprecates several ciphers from the Bouncy Castle provider in favor of those provided by the Conscrypt provider. Calls to `getInstance()` that request the Bouncy Castle provider generate `NoSuchAlgorithmException` errors. To resolve the errors, do not specify a provider in getInstance() (that is, request the default implementation). |
| Removal of direct access to `Build.serial` | Apps needing the Build.serial identifier must now request the `READ_PHONE_STATE` permission and then use the new `Build.getSerial()` method added in Android 9. |
| Disallowed sharing of WebView data directory | Apps can no longer share a single WebView data directory across processes. If your app has more than one process using WebView, CookieManager, or any other API in the android.webkit package, your app will crash when the second process calls a WebView method. |
| Access to app's data directory blocked by SELinux | The system enforces per-app SELinux sandboxes with per-app SELinux restrictions on each app's private data directory. Directly accessing another app's data directory by path is now disallowed. Apps may continue to share data using IPC mechanisms, including by passing FDs. |


For a more extensive list of behavior changes for apps targeting Android 9,
see [Behavior Changes](https://developer.android.com/about/versions/pie/android-9.0-changes-28) document.

To explore the new features and APIs available Android 9, see
[Android 9 Features and APIs](https://developer.android.com/about/versions/pie/android-9.0).