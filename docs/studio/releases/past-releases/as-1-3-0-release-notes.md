---
title: Android Studio  |  Android Developers
url: https://developer.android.com/studio/releases/past-releases/as-1-3-0-release-notes
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [IDE guides](https://developer.android.com/studio/releases/past-releases)

Stay organized with collections

Save and categorize content based on your preferences.



# Android Studio v1.3.0 (July 2015)

Fixes and enhancements:

* Added options to enable
  [developer services](/tools/studio/studio-features#dev-services),
  such as [Google AdMob](https://developers.google.com/admob/) and
  [Analytics](/distribute/analyze/start), in your app from within
  Android Studio.
* Added additional [annotations](/tools/debugging/annotations),
  such as `@RequiresPermission`, `@CheckResults`, and
  `@MainThread`.
* Added the capability to generate Java heap dumps and analyze thread allocations from the
  [Memory Monitor](/tools/studio#mem-cpu). You can also
  convert Android-specific HPROF binary format files to standard HPROF format from within
  Android Studio.
* Integrated the [SDK Manager](/tools/help/sdk-manager)
  into Android Studio to simplify package and tools access and provide update notifications.

  **Note:** The standalone SDK Manager is still available from
  the command line, but is recommended for use only with standalone SDK
  installations.
* Added the `finger` command in the emulator console to simulate
  [fingerprint](/tools/studio/studio-features#finger-print)
  authentication.
* Added a `<public>` resource declaration to designate library
  resources as
  [public and private](/tools/studio/studio-features#private-res)
  resources.

  **Note:** Requires
  [Android plugin for Gradle](/tools/building/plugin-for-gradle)
  version 1.3 or higher.
* Added [data binding](/tools/data-binding/guide) support to
  create declarative layouts that bind your application logic to layout elements.
* Added support for a separate
  [test APK module](/tools/studio/studio-features#test-module)
  to build test APKs in Android Studio.
* Updated the [AVD Manager](/tools/devices/managing-avds) with HAXM
  optimizations and improved notifications.
* Added 64-bit ARM and MIPS emulator support for
  [QEMU](http://wiki.qemu.org/Main_Page) 2.1.
* Simplified the resolution of Lint warnings
  by adding quick fixes, such as the automatic generation of
  [Parcelable](/reference/android/os/Parcelable)
  implementation.
* Added live template
  support for quick insertion of code snippets.