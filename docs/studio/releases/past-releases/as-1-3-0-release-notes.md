---
title: https://developer.android.com/studio/releases/past-releases/as-1-3-0-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-1-3-0-release-notes
source: md.txt
---

<br />

# Android Studio v1.3.0 (July 2015)

Fixes and enhancements:

- Added options to enable [developer services](https://developer.android.com/tools/studio/studio-features#dev-services), such as [Google AdMob](https://developers.google.com/admob/) and [Analytics](https://developer.android.com/distribute/analyze/start), in your app from within Android Studio.
- Added additional [annotations](https://developer.android.com/tools/debugging/annotations), such as `@RequiresPermission`, `@CheckResults`, and `@MainThread`.
- Added the capability to generate Java heap dumps and analyze thread allocations from the [Memory Monitor](https://developer.android.com/tools/studio#mem-cpu). You can also convert Android-specific HPROF binary format files to standard HPROF format from within Android Studio.
- Integrated the [SDK Manager](https://developer.android.com/tools/help/sdk-manager) into Android Studio to simplify package and tools access and provide update notifications.

  **Note:** The standalone SDK Manager is still available from
  the command line, but is recommended for use only with standalone SDK
  installations.
- Added the `finger` command in the emulator console to simulate [fingerprint](https://developer.android.com/tools/studio/studio-features#finger-print) authentication.
- Added a `<public>` resource declaration to designate library resources as [public and private](https://developer.android.com/tools/studio/studio-features#private-res) resources.

  **Note:** Requires
  [Android plugin for Gradle](https://developer.android.com/tools/building/plugin-for-gradle)
  version 1.3 or higher.
- Added [data binding](https://developer.android.com/tools/data-binding/guide) support to create declarative layouts that bind your application logic to layout elements.
- Added support for a separate [test APK module](https://developer.android.com/tools/studio/studio-features#test-module) to build test APKs in Android Studio.
- Updated the [AVD Manager](https://developer.android.com/tools/devices/managing-avds) with HAXM optimizations and improved notifications.
- Added 64-bit ARM and MIPS emulator support for [QEMU](http://wiki.qemu.org/Main_Page) 2.1.
- Simplified the resolution of Lint warnings by adding quick fixes, such as the automatic generation of [Parcelable](https://developer.android.com/reference/android/os/Parcelable) implementation.
- Added live template support for quick insertion of code snippets.

<br />