---
title: https://developer.android.com/guide/platform
url: https://developer.android.com/guide/platform
source: md.txt
---

# Platform architecture

Android is an open source, Linux-based software stack created for a wide array of devices and form factors. Figure 1 shows the major components of the Android platform.
![The Android software stack](https://developer.android.com/static/guide/platform/images/android-stack_2x.png)

**Figure 1.**The Android software stack.

## Linux kernel

The foundation of the Android platform is the Linux kernel. For example,[the Android Runtime (ART)](https://developer.android.com/guide/platform#art)relies on the Linux kernel for underlying functionalities such as threading and low-level memory management.

Using a Linux kernel lets Android take advantage of[key security features](https://source.android.com/security/overview/kernel-security.html)and lets device manufacturers develop hardware drivers for a well-known kernel.

## Hardware abstraction layer (HAL)

The[hardware abstraction layer (HAL)](https://source.android.com/devices/architecture/hal)provides standard interfaces that expose device hardware capabilities to the higher-level[Java API framework](https://developer.android.com/guide/platform#api-framework). The HAL consists of multiple library modules, each of which implements an interface for a specific type of hardware component, such as the[camera](https://source.android.com/devices/camera/index.html)or[Bluetooth](https://source.android.com/devices/bluetooth.html)module. When a framework API makes a call to access device hardware, the Android system loads the library module for that hardware component.

## Android runtime

For devices running Android version 5.0 (API level 21) or higher, each app runs in its own process and with its own instance of the[Android Runtime (ART)](https://source.android.com/devices/tech/dalvik/index.html). ART is written to run multiple virtual machines on low-memory devices by executing Dalvik Executable format (DEX) files, a bytecode format designed specifically for Android that's optimized for a minimal memory footprint. Build tools, such as[`d8`](https://developer.android.com/studio/command-line/d8), compile Java sources into DEX bytecode, which can run on the Android platform.

Some of the major features of ART include the following:

- Ahead-of-time (AOT) and just-in-time (JIT) compilation
- Optimized garbage collection (GC)
- On Android 9 (API level 28) and higher,[conversion](https://developer.android.com/about/versions/pie/android-9.0#art-aot-dex)of an app package's DEX files to more compact machine code
- Better debugging support, including a dedicated sampling profiler, detailed diagnostic exceptions and crash reporting, and the ability to set watchpoints to monitor specific fields

Prior to Android version 5.0 (API level 21), Dalvik was the Android runtime. If your app runs well on ART, then it can work on Dalvik as well, but[the reverse might not be true](https://developer.android.com/guide/practices/verifying-apps-art).

Android also includes a set of core runtime libraries that provide most of the functionality of the Java programming language, including some[Java 8 language features](https://developer.android.com/guide/platform/j8-jack), that the Java API framework uses.

## Native C/C++ libraries

Many core Android system components and services, such as ART and HAL, are built from native code that requires native libraries written in C and C++. The Android platform provides Java framework APIs to expose the functionality of some of these native libraries to apps. For example, you can access[OpenGL ES](https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl)through the Android framework's[Java OpenGL API](https://developer.android.com/reference/android/opengl/package-summary)to add support for drawing and manipulating 2D and 3D graphics in your app.

If you are developing an app that requires C or C++ code, you can use the[Android NDK](https://developer.android.com/ndk)to access some of these[native platform libraries](https://developer.android.com/ndk/guides/stable_apis)directly from your native code.

## Java API framework

The entire feature-set of the Android OS is available to you through APIs written in the Java language. These APIs form the building blocks you need to create Android apps by simplifying the reuse of core, modular system components and services, which include the following:

- A rich and extensible[view system](https://developer.android.com/guide/topics/ui/overview)you can use to build an app's UI, including lists, grids, text boxes, buttons, and even an embeddable web browser
- A[resource manager](https://developer.android.com/guide/topics/resources/overview), providing access to non-code resources such as localized strings, graphics, and layout files
- A[notification manager](https://developer.android.com/guide/topics/ui/notifiers/notifications)that enables all apps to display custom alerts in the status bar
- An[activity manager](https://developer.android.com/guide/components/activities/intro-activities)that manages the lifecycle of apps and provides a common[navigation back stack](https://developer.android.com/guide/components/tasks-and-back-stack)
- [Content providers](https://developer.android.com/guide/topics/providers/content-providers)that enable apps to access data from other apps, such as the Contacts app, or to share their own data

Developers have full access to the same[framework APIs](https://developer.android.com/reference/packages)that Android system apps use.

## System apps

Android comes with a set of core apps for email, SMS messaging, calendars, internet browsing, contacts, and more. Apps included with the platform have no special status among the apps the user chooses to install. So, a third-party app can become the user's default web browser, SMS messenger, or even the default keyboard. Some exceptions apply, such as the system's Settings app.

The system apps function both as apps for users and to provide key capabilities that developers can access from their own app. For example, if you want your app to deliver SMS messages, you don't need to build that functionality yourself. You can instead invoke whichever SMS app is already installed to deliver a message to the recipient you specify.