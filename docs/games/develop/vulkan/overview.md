---
title: https://developer.android.com/games/develop/vulkan/overview
url: https://developer.android.com/games/develop/vulkan/overview
source: md.txt
---

# Use Vulkan for graphics

[Vulkan](https://www.vulkan.org/)is a modern cross-platform 3D graphics API designed to minimize abstraction between device graphics hardware and your game. Vulkan is the primary low-level graphics API on Android, replacing[OpenGL ES](https://www.khronos.org/opengles/). OpenGL ES is still supported on Android, but is no longer under active feature development. Vulkan offers the following advantages over OpenGL ES:

- A more efficient architecture with lower CPU overhead in the graphics driver
- New optimization strategies to improve CPU performance
- New graphics features not available in OpenGL ES such as bindless APIs and ray tracing

Vulkan is available on Android from[Android 7 (API level 24)](https://developer.android.com/about/versions/nougat). All 64-bit Android devices from Android 10 (API level 29) and higher support Vulkan 1.1.[Eighty-five percent](https://developer.android.com/about/dashboards)of active Android devices support Vulkan. The[Android Baseline profile](https://developer.android.com/ndk/guides/graphics/android-baseline-profile)defines a minimum feature set for Vulkan-capable devices.

Vulkan helps you create better looking and more performant games. Vulkan unlocks the full potential of modern graphics hardware. Vulkan is used by the[Android UI rendering framework](https://skia.org/docs/user/special/vulkan/)on compatible devices. Current versions of the Unity and Unreal game engines choose Vulkan as their default renderer on compatible Android devices. The[ANGLE](https://github.com/google/angle)project implements a conformant implementation of the OpenGL ES API on top of Vulkan.

## Get started

### C/C++

To learn how to use Vulkan in your C/C++ game engine on Android, see[Get started with Vulkan on Android](https://developer.android.com/games/develop/vulkan/native-engine-support#get_started_with_vulkan_on_android).

Furthermore, there is a generic Vulkan section for non-game developers in the Native Development Kit (NDK) documentation covering the following topics:

- [Shader compilers](https://developer.android.com/ndk/guides/graphics/shader-compilers)for improved performance
- [Validation layers](https://developer.android.com/ndk/guides/graphics/validation-layer)for Vulkan code debugging
- [Vulkan extensions](https://developer.android.com/ndk/guides/graphics/extensions)for custom functionality
- [Android Baseline profile](https://developer.android.com/ndk/guides/graphics/android-baseline-profile)for device requirements

### Game engines

- [Vulkan on Unity](https://developer.android.com/games/develop/vulkan/game-engine-support#unity)
- [Vulkan on Unreal](https://developer.android.com/games/develop/vulkan/game-engine-support#unreal)

## About ANGLE

Vulkan is the preferred Android interface to the GPU.[Android 15](https://developer.android.com/about/versions/15/summary)and up includes ANGLE as an optional layer for running OpenGL ES on top of Vulkan. Moving to ANGLE standardizes the Android OpenGL implementation for improved compatibility, and in some cases, improved performance.

Test your OpenGL ES app stability and performance with ANGLE using a wide variety of Android 15+ devices by enabling ANGLE for your package with the following two adb commands. Replace "package-name" with the package to test.

`adb shell settings put global angle_gl_driver_selection_pkgs package-name`

`adb shell settings put global angle_gl_driver_selection_values angle`

These settings persist across a device reboot. To disable ANGLE use the following commands:

`adb shell settings delete global angle_gl_driver_selection_pkgs`

`adb shell settings delete global angle_gl_driver_selection_values`
| **Important:** Use the adb commands to test the ANGLE driver for OpenGL ES games. For new projects, use Vulkan.

### Android ANGLE on Vulkan roadmap

![Android ANGLE on Vulkan roadmap](https://developer.android.com/static/games/develop/vulkan/angle/angle-roadmap-android-15.png)
| **Note:** As part of streamlining the Android GPU stack, we will ship ANGLE as the GL system driver on more new devices, with the expectation that ultimately OpenGL ES will be available only through ANGLE. We will however continue support for OpenGL ES on all devices.

### Report issue for ANGLE

If you encountered any issue with ANGLE, report it to us by submitting it in our[issue tracker](https://issuetracker.google.com/issues/new?component=1765977&template=2111394).
| **Note:** This issue tracker is not subject to any SLA.