---
title: https://developer.android.com/ndk/guides/graphics/getting-started
url: https://developer.android.com/ndk/guides/graphics/getting-started
source: md.txt
---

# Get started with Vulkan

| **Note:** Although this page includes[NativeActivity](https://developer.android.com/reference/android/app/NativeActivity)description,[GameActivity inside AGDK jetpack library](https://developer.android.com/games/agdk/integrate-game-activity)is an updated and well maintained implementation of`NativeActivity`, with more functionality and fast release cycles. It is highly recommended to use`GameActivity`for your new projects.

This document outlines how to get started with the Vulkan graphics library by downloading, compiling, and running Khronos© sample app.

## Prerequisites

Before beginning, make sure you have the right hardware and platform version prepared. You should use a device or an[emulator](https://developer.android.com/studio/run/emulator)that supports Vulkan, running Android 7.0 (Nougat), API level 24 or higher.

You can confirm your Android version by going to the**Settings** menu, and selecting**About phone** \>**Android Version**. Once you've confirmed that you have the right hardware and platform version set up, you can download the necessary software.

## Download

Before getting started, you must download several tools and other software. Note that on a Windows host, it is recommended that you avoid a deep file path hierarchy for tools and source code; this is to work around file path limits on some Windows OS versions.

1. If you don't already have Android Studio,[download it](https://developer.android.com/studio). This includes the most recent Android SDK.
2. [Install the NDK and CMake](https://developer.android.com/studio/projects/install-ndk)from within Android Studio or[download and install](https://developer.android.com/ndk/downloads)them separately.
3. Build and Run the[Hello JNI sample](https://github.com/android/ndk-samples/tree/main/hello-jni)to ensure Android Studio is working properly.
4. Install python3 and other components listed in[build.md](https://github.com/KhronosGroup/Vulkan-Samples/blob/main/docs/build.adoc#android)for your host platform.

## Import

In this section, you download[the Khronos© Vulkan© sample repository](https://github.com/KhronosGroup/Vulkan-Samples/), generate an Android gradle project, then open it with the Android Studio IDE.

1. Set the following environment variables:  

   ```
   export ANDROID_HOME=/path/to/sdk-directory
   export ANDROID_NDK_HOME=$ANDROID_HOME/ndk/{your-ndk-version-dir}
   ```
2. Add CMake to the $PATH, which is used to generate Android build scripts:  

   ```
   export PATH=$PATH:$ANDROID_HOME/cmake/{your-cmake-version}/bin
   ```
3. Open a terminal and download the source code to your development directory:  

   ```
   cd dev-directory
   git clone --recursive https://github.com/KhronosGroup/Vulkan-Samples.git
   ```
4. Follow these instructions (from[Build.md](https://github.com/KhronosGroup/Vulkan-Samples/blob/master/docs/build.md#android)) to generate the Android sample project:  

   ```
   cd Vulkan-Samples
   ./scripts/generate.py android
   ```
5. Open Android Studio. Choose**File \> Open** and select`Vulkan-Samples/build/android_gradle/build.gradle`. You should see something similar to the following after Android Studio loads the project:  
   ![Importing sample project to Studio.](https://developer.android.com/ndk/guides/images/vk-guide-init-project.png)

   <br />

   **Figure 1.**The sample project inside Android Studio.

   <br />

## Compile

All samples in this repo are organized into one Android project. To compile the project, do one of the following:

- To just compile the sources, use menu,**Build** \>**Make Project** , or type the**Ctrl-F9**shortcut key.
- To generate the sample APK, select menu**Build** \>**Build Bundle(s)/APK(s)** \>**Build APK(s)**.

You should see the build successful message inside Android Studio's**Build**window. In case there are errors showing up, fix them and re-compile.  
![Compiling sample project with Studio.](https://developer.android.com/ndk/guides/images/vk-guide-compile-project.png)

<br />

**Figure 2.**A successful sample build.

<br />

<br />

## Execute

Before running the sample project, make sure Android Studio recognizes your connected Vulkan device or Android Emulator. You should see something like the following:  
![Connecting test device to Studio.](https://developer.android.com/ndk/guides/images/vk-guide-test-device.png)

<br />

**Figure 3.**Connect the test device to Android Studio.

<br />

<br />

To run the project, do the following:

1. Use menu**Run \> Run vulkan_sample** , or click on the run button![](https://developer.android.com/ndk/guides/images/vk-guide-run-button.png)on the toolbar, and wait for the sample to get installed and started on your connected device.
2. On your connected Android device, authorize the needed access requests.
   - enable**Allow access to manage all files** , then tap the arrow**Back button**to return the sample main start screen.
   - allow the disk access:  
     ![allowing disk access.](https://developer.android.com/ndk/guides/images/vk-guide-allow-access.png)

     <br />

     **Figure 4.**Enable disk access.

     <br />

3. You should see the sample main menu screen, similar to the following:  
   ![sample main menu.](https://developer.android.com/ndk/guides/images/vk-guide-sample-menu.png)

   <br />

   **Figure 5.**Sample main menu.

   <br />

4. Browse through the sample list, and select a few to run. If you are new to Vulkan development, you can start with "API" samples. For example, tapping "Hello Triangle" should display a rendered triangle similar to the following:  
   ![Triangle](https://developer.android.com/ndk/guides/images/vk-guide-triangle.png)

   <br />

   **Figure 6.**Hello Triange sample.

   <br />

Your development system is now set up to run samples on your test device.

Vulkan Samples are developed for multiple operating systems, including those for desktop and mobile. Some samples under**Performance** ,**Extensions** , and**Tooling**may be unstable and crash on your device. This might be due to various reasons, such as:

- The specific Vulkan features weren't designed for Android.
- Your Android OS version is unsupported.
- The GPU capability of your hardware platform.

## Explore

The Java section of the Vulkan sample derives from the[NativeActivity](https://developer.android.com/reference/android/app/NativeActivity)class. It passes typical application lifecycle events, such as app creation, start, stop, and destroy to the C/C++ code. In the C/C++ section of the sample, there is a sample framework that implements the run-time sub sample switching functionality. At a very high level, Android system events/messages go through the following path to reach the sample app's Vulkan code:

- `NativeSampleActivity`Java section
- `NativeSampleActivity`C/C++ section
- `android_native_glue`code
- `android_main`
- Sample framework
- Individual sub sample's code

`android_main`is the bridge between`NativeSampleActivity`and the app code, which can be the starting point for you to follow the sample code. If you just want to focus on the Vulkan specific sources, you can explore the code under`Vulkan_Samples\samples`, which contains the following:

- The "api" category samples.
- The "performance" category samples.
- The "extensions" category samples.
- The "tooling" samples.

The`Vulkan_Samples\shaders`are the home for all shaders.

You can start browsing the "API" category samples to get familiar with basic Vulkan usage and the sample framework. Then you can progress to the "Performance" and "Extenstions" category samples. For shader code, you can use the**Project**view in Android Studio.  
![Triangle shader.](https://developer.android.com/ndk/guides/images/vk-guide-shaders.png)

<br />

**Figure 7.**Explore shader with Studio.

<br />

<br />

## Additional resources

The Vulkan API has been through a few versions, so it is maturing. The Vulkan standard committee and the Vulkan community have created a rich set of Vulkan material that demonstrates the API's usage and best practices. The following list contains some resources for Vulkan application development:

- **Vulkan Specification.** The Khronos Group maintains the Vulkan specification. See the[Vulkan homepage](https://www.khronos.org/vulkan)for the full specification, training,[guides](https://github.com/KhronosGroup/Vulkan-Guide)and[tutorials](https://www.vulkan.org/learn#key-resources).

- **Validation Layers.** Validation Layers are essential for application development. See the[Vulkan validation layers on Android](https://developer.android.com/ndk/guides/graphics/validation-layer)documentation for details.

- **Shaderc.** Shaderc code in the NDK is the downstream of the[Shaderc repo](https://github.com/google/shaderc). For the usage documentation and instructions to get the latest version, see[Shader compilers](https://developer.android.com/ndk/guides/graphics/shader-compilers).