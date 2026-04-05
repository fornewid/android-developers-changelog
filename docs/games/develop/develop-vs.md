---
title: https://developer.android.com/games/develop/develop-vs
url: https://developer.android.com/games/develop/develop-vs
source: md.txt
---

# Develop your game in Microsoft Visual Studio

[Android Game Development Extension](https://developer.android.com/games/agde)(AGDE) for Visual Studio allows you to target Android as a platform for your Visual Studio projects. AGDE supports a full range of development activities: project management, building, debugging, and profiling.

AGDE is best suited to you if you're developing primarily on Windows and use Microsoft Visual Studio to write C or C++ code. If you're writing C or C++ code using different tools, use Android Studio to develop for Android.

AGDE is part of the Android Game Development Kit. The Android Game Development Kit includes libraries and tools that support making great games on Android. The libraries in the Android Game Development Kit are compatible with AGDE projects. Tools like the Android Graphics Inspector can help you tune your game for optimal performance.

## Target Android in Visual Studio

AGDE adds Android as a platform target to Visual Studio. This enables existing multi-platform Visual Studio game projects to quickly integrate Android as a new platform. Visual Studio IntelliSense features are compatible with AGDE. All current Android CPU architectures are supported: both ARM and Intel in 32-bit and 64-bit.

## Build in Visual Studio

AGDE integrates with MSBuild for compiling and linking C++ code for Android. The Android NDK is used to supply the compiler and build toolchain. For developers that have specific dependencies, AGDE is compatible with multiple versions of the NDK. Project build settings are configured using the standard Visual Studio property system. AGDE is compatible with Incredibuild, enabling developers to use existing distributed build infrastructure to speed up build times when compiling for Android.

## Debug in Visual Studio

AGDE supports deploying to, running on, and debugging with both an emulator and a physical device. The debugger can also be attached to an already-running process. AGDE interfaces with LLDB for debugging support. With AGDE, debug sessions run inside Visual Studio, using its standard interface for breakpoints, tracing and variable inspection. Additional features include Memory and Register views, and disassembly of native code. LLDB shell functionality is available through the Visual Studio Command Window. Unreal Engine developers using 4.26.1 and later can use AGDE to debug on Android.

## Profile from Visual Studio

AGDE integrates with a standalone version of the Android Studio Profiler. This profiler can be launched from Visual Studio and attached to a running game session. The Android Studio Profiler displays real time usage statistics for CPU, memory, network, and energy.

## Requirements

AGDE requires an Intel or AMD PC running Microsoft Windows with the following software installed:

- .NET Core SDK 2.2
- Android Studio 3.5 or later
- Visual Studio 2017 (15.4.0 or later) or Visual Studio 2019 (16.0.0 or later)

## More information

(Links to download) (Links to AGDE guide)