---
title: https://developer.android.com/develop/xr/unreal/setup
url: https://developer.android.com/develop/xr/unreal/setup
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

This guide details the recommended engine versions, required SDKs, and Android
project settings when developing an Unreal Engine app for Android XR.

## Prerequisites

Before you can set up Unreal Engine for Android XR development, you need to
install the following applications and tools:

1. Download and install the [Epic Games Launcher](https://epicgames.com/).

   1. From the Epic Games Launcher, install version **5.6.1** (or higher) of Unreal Engine.
2. Set up your system to build C++ code (for example, using Visual Studio 2022
   for Windows, or Xcode for macOS). For more information, see Epic's [C++
   development environment setup](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-your-development-environment-for-cplusplus-in-unreal-engine).

3. Install the [.NET 8.0 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/8.0).

4. Install [Android Studio](https://developer.android.com/studio) (Quail 2 \| 2026.1.2 Patch 1 or higher).

## Install Android build support

Because Android XR relies on specific SDK versions, you must install the correct
Android build tools alongside Unreal Engine.

1. Open the Epic Games Launcher.
2. Click the drop-down arrow next to your installed Engine version (Launch
   button) and click **Options**.

   1. Scroll further to the installation options, select **Android** , and click **Apply**.
   2. If prompted, allow the engine to register any file extensions that it requires.
3. Install [Java JDK 17](https://www.oracle.com/java/technologies/javase/jdk17-0-13-later-archive-downloads.html).

4. In Android Studio, use the SDK Manager to install the following
   specific versions required by the Android XR samples:

   - **SDK Platforms**: 34, 35, and 36
   - **NDK**: 29.0.x
   - **Command-line Tools** (all items)
5. Follow Epic's [Advanced setup and troubleshooting guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/advanced-setup-and-troubleshooting-guide-for-using-android-sdk) to
   configure the following system environment variables:

   - `ANDROID_HOME`
   - `JAVA_HOME`
   - `NDK_ROOT`

## Create an Unreal XR project

Next, create a new project and configure it with the necessary XR plugins and
inputs:

1. Launch Unreal Engine 5.6.1.
2. Under **New Project Categories** , select the **Virtual Reality** template.
3. In the **Project Defaults** menu, set the **Target Platform** to **Mobile**.
4. Set the **Quality Preset** to **Scalable** to promote optimal performance on mobile XR hardware.
5. Choose a project name, and then click **Create**.

## Configure Android settings

After your project is open, complete these steps to set the required Android API
levels and graphics settings for Android XR:

1. Go to **Edit \> Project Settings**.
2. Navigate to **Platforms \> Android**.
3. If the **Accept SDK License** button is highlighted red, click it.
4. In the **APKPackaging** section:
   - Set **Minimum SDK Version** to `34`.
   - Set **Target SDK Version** to `34` (or higher).
5. Scroll further to the **Build** section and select **Support Vulkan**.

   Vulkan is the recommended, highly-performant graphics API for Android XR.

## Configure rendering settings

To achieve the high frame rates and visual clarity required for Android XR, you
must also configure Unreal Engine to use the optimized mobile rendering path:

1. Go to **Edit \> Project Settings** and navigate to **Engine \> Rendering**.
2. Under the **Forward Renderer** section, select **Forward Shading**.

   The forward renderer is significantly faster for mobile VR than the default
   deferred renderer. Note that enabling this requires an editor restart and
   shader compilation.
3. Under the **Default Settings** section, set the **Anti-Aliasing Method** to
   **MSAA**.

4. Under the **Mobile** section, set **Mobile MSAA** to **4x**.

   MSAA provides the sharpest results for VR without the blurring effects
   caused by Temporal AA (TAA).
5. Under the **VR** section:

   1. Clear **Mobile HDR**.

      Disabling High Dynamic Range on mobile drastically reduces the
      post-processing overhead.
   2. Select **Mobile Multi-View**.

      This allows the engine to render both eyes in a single pass,
      significantly improving CPU performance.

## See also

For detailed instructions on deploying a template project to an Android-powered
device, refer to [Setting up Unreal Engine projects for Android
development](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-unreal-engine-projects-for-android-development).