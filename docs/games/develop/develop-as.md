---
title: https://developer.android.com/games/develop/develop-as
url: https://developer.android.com/games/develop/develop-as
source: md.txt
---

# Develop your game in Android Studio

You can use Android Studio with C/C++ to bring your game to life on Android.

[Android Studio](https://developer.android.com/studio)is the official Integrated Development Environment (IDE) for Android app development. It includes extensive support for the C/C++ programming language and development using the[Android Native Development Kit (NDK)](https://developer.android.com/ndk), and is available on multiple operating systems.

If you have existing Microsoft Visual Studio projects and develop primarily on Windows in C or C++, you can use the[Android Game Development Extension](https://developer.android.com/games/agde)for Microsoft Visual Studio instead.

## Manage your project

Android Studio integrates CMake support for configuration and management of C/C++ code. CMake allows you to structure your C/C++ project in a modular fashion. Android Studio's Gradle build system and[Android Gradle plugin](https://developer.android.com/studio/releases/gradle-plugin)use CMake to set up the build process for native C/C++ code modules.

The Android Studio editor has robust editing and indexing capabilities for C/C++ code. Standard features of the editor include code completion, syntax reformatting, symbol lookups, and pre-compile error checking.

## Integrate dependencies

Android Studio's Gradle build system supports declaring local or remote binary dependencies for your project. A common use case is pulling in libraries such as[Android Jetpack](https://developer.android.com/jetpack)from a Maven remote dependency server. These dependencies allow precise control of what version of a dependency is being integrated into an app. Remote dependencies also help avoid committing extraneous files into your project's version control system.

## Debug in Android Studio

Android Studio provides a debugger that enables you to debug your game on either an emulator or a physical device. The Android Studio debugger supports C/C++, Java, and Kotlin, and uses[LLDB](https://lldb.llvm.org/)to debug C/C++. Program breakpoints and variable inspection are available for all languages. You can set hardware watchpoints when debugging C/C++ code using LLDB. The Android Studio debugger supports defining custom data type renderers for enhanced display of project data structures.

## Profile in Android Studio

Android Studio includes profiling tools that help measure the runtime performance of your game. Profiling categories include CPU usage, memory usage, network activity and energy use. Effective use of profiling tools can reduce performance hiccups or out of memory crashes in your game that negatively impact your players. Reducing energy consumption of your game can avoid performance problems due to thermal throttling.

Android Studio features application package analysis tools that let you inspect what is taking up space in your build. These tools, when used in concert with features such as Play Asset Delivery, help optimize the size of your game and ensure your users don't download more data than is necessary.

## More Information

For more information on Android Studio, including system requirements, download links, and the user guide, visit the[Android Studio](https://developer.android.com/studio)page.