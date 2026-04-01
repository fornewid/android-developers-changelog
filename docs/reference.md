---
title: https://developer.android.com/reference
url: https://developer.android.com/reference
source: md.txt
---

# Android API reference

Start building your Android app with the Android Platform APIs. They are available in[Kotlin](https://developer.android.com/reference/kotlin/packages)and[Java](https://developer.android.com/reference/packages).

**Note:**Many Kotlin reference topics are derived from Java-based source code. This means that some Kotlin reference topics might contain Java code snippets.

These additional libraries make it easy to add additional functionality and features to your app.

## Jetpack

AndroidX
:   Refactored versions of the Android APIs that are not bundled with the operating system.  
    [**Reference**](https://developer.android.com/reference/kotlin/androidx/packages)[**User Guide**](https://developer.android.com/jetpack/getting-started)

Jetpack Compose
:   Jetpack Compose is a modern toolkit for building native Android UI. Jetpack Compose simplifies and accelerates UI development on Android with less code, powerful tools, and intuitive Kotlin APIs.  
    [**Reference**](https://developer.android.com/reference/kotlin/androidx/compose)[**User Guide**](https://developer.android.com/jetpack/compose/tutorial)

AndroidX Constraint Layout
:   Includes`ConstraintLayout`and related APIs for building constraint-based layouts.  
    [**Reference**](https://developer.android.com/reference/androidx/constraintlayout/packages)[**User Guide**](https://developer.android.com/training/constraint-layout)
:   For`ConstraintLayout`in Compose.  
    [**Reference**](https://developer.android.com/reference/kotlin/androidx/constraintlayout/compose/package-summary)

Material Components
:   Material Components for Android*(MDC-Android)* help developers execute Material Design to build beautiful and functional Android apps.  
    [**Reference**](https://developer.android.com/reference/com/google/android/material/packages)[**User Guide**](https://developer.android.com/guide/topics/ui/look-and-feel)

Android NDK
:   The Android NDK is a toolset that lets you implement parts of your app in native code, using languages such as C and C++.  
    [**Reference**](https://developer.android.com/ndk/reference)[**User Guide**](https://developer.android.com/ndk)

Android Game Development Kit libraries
:   The Android Game Development Kit C/C++ game libraries make it easier to build, debug, optimize, and maintain your games.  
    [**Overview**](https://developer.android.com/games/agdk/libraries-overview)

Android Gradle Plugin
:   The Android Gradle Plugin (AGP) is the supported build system for Android applications and includes support for compiling many different types of sources and linking them together into an application that you can run on a physical Android device or an emulator.  
    [**Reference**](https://developer.android.com/reference/tools/gradle-api)[**User Guide**](https://developer.android.com/studio/build)
Cross device SDKThe Cross device SDK simplifies the development of rich and engaging multi-device experiences. Its core functionality includes device discovery and authorization, secure connections and data transfers, and multi-device sessions.  
[**Reference**](https://developer.android.com/reference/kotlin/crossdevice/packages)[**User Guide**](https://developer.android.com/guide/topics/connectivity/cross-device-sdk/overview)

## Google Play

Play In-app Billing Library
:   Provides APIs to help you implement Google Play's in-app billing and subscription features.  
    [**Reference**](https://developer.android.com/reference/com/android/billingclient/packages)[**User Guide**](https://developer.android.com/google/play/billing)

Play Core Library
:   Provides APIs to help you request, monitor, and manage on demand downloads for Play Feature Delivery, Play Asset Delivery, and offers additional APIs such as in-app updates and in-app reviews. This library is available in[Java](https://developer.android.com/reference/com/google/android/play/core/packages),[Native code](https://developer.android.com/reference/native/play/core),[Unity](https://developer.android.com/reference/unity)and[Unreal Engine](https://developer.android.com/reference/unreal-engine/play/core).

Play Install Referrer library
:   Provides APIs to securely retrieve referral content from Google Play.  
    [**Reference**](https://developer.android.com/reference/com/android/installreferrer/packages)

Google Play Games Services Unity Plugin API (v2)
:   Provides the Google Play Games Services Unity Plugin API for developers. It is meant for developers who use the Unity Plugin (v2) implementation for their game.  
    [**Reference**](https://developer.android.com/games/services/unity/v2/api)

Google Play Games Services Web REST API
:   Provides APIs for developers to enhance games with social leaderboards, achievements, game state, sign-in with Google, and more.  
    [**Reference**](https://developer.android.com/games/services/web/api/rest)

Google Play Games Services C++ API (v1)
:   Provides the Google Play Games Services C++ API for use with Google Play Game services. It is meant for developers who have an existing C++ implementation of their game.  
    [**Reference**](https://developer.android.com/games/services/cpp/api)

Google Play Games Services Management API
:   Provides the Google Play Games Services Management API to issue REST calls to programmatically control the metadata underlying the Google Play Games Services features. This API simplifies your testing of Google Play games services features and gives you flexibility when managing your games to address cheating and fix player accounts.  
    [**Reference**](https://developer.android.com/games/services/management/api)

Google Play Games Services Publishing API
:   Provides APIs that allows you to automate frequent tasks having to do with games production and distribution.  
    [**Reference**](https://developer.android.com/games/services/publishing/api)

## Google Assistant

Built-in Intents
:   Let users launch and control your Android app with their voice, using Google Assistant and[App Actions](https://developer.android.com/reference/app-actions/built-in-intents).

## Deprecated Libraries

These libraries are superseded by the[AndroidX](https://developer.android.com/reference/androidx/packages)libraries and are no longer maintened. They are still shipped in the SDK to support legacy apps. For more information see the[androidx migration guide](https://developer.android.com/jetpack/androidx/migrate).

Android Support Library
:   Provided a variety of Android feature and utility APIs that are compatible with a wide range of platform versions. The[original library](https://developer.android.com/reference/android/support/packages)is superseded by the[AndroidX](https://developer.android.com/reference/androidx/packages)libraries.

Android Test Support Library
:   Includes APIs for testing your Android app, including Espresso, JUnit Runner, JUnit4 rules, and UI Automator. The[original library](https://developer.android.com/reference/android/support/test/packages)is superseded by the[AndroidX Test](https://developer.android.com/reference/androidx/test/platform/app/package-summary)library.

Architecture Components
:   Includes APIs for a variety of core app components, such as APIs that manage your UI component lifecycle, data persistence, view model, and more. The[original library](https://developer.android.com/reference/android/arch/packages)is superseded by the[AndroidX](https://developer.android.com/reference/androidx/packages)libraries.

Constraint Layout Library
:   Legacy Support Library`ConstraintLayout`and related APIs for building constraint-based layouts. The[original library](https://developer.android.com/reference/android/support/constraint/packages)is superseded by the[AndroidX constraintlayout](https://developer.android.com/reference/androidx/constraintlayout/packages)library.

Android Things Library
:   Provided APIs to build connected devices running the Android Things platform. The[original library](https://developer.android.com/reference/com/google/android/things/packages)is no longer maintained.
Android Wearable LibraryProvides APIs to build apps for wearable devices running Wear OS by Google. The[original library](https://developer.android.com/reference/android/support/wearable/packages)is superseded by the[AndroidX Wear](https://developer.android.com/jetpack/androidx/releases/wear)libraries.