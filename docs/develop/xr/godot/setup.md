---
title: https://developer.android.com/develop/xr/godot/setup
url: https://developer.android.com/develop/xr/godot/setup
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

This guide details the recommended engine versions, required SDKs, and Android
project settings when developing a Godot Engine app for Android XR.

## Prerequisites

Before you can configure a Godot Engine project for Android XR development, you
need to complete the following prerequisites:

1. Download **Godot 4.6.2** from the [official Godot website](https://godotengine.org/download).
2. Ensure you have an [XR headset](https://developer.android.com/develop/xr/devices#xr-headsets) or some [XR glasses](https://developer.android.com/develop/xr/devices#xr-glasses).
3. Install [Android Studio](https://developer.android.com/studio).

## Install Android build support

Godot requires specific Android build tools to compile and export packages for
spatial computing.

1. In Android Studio, use the SDK Manager to install the following packages and
   tools:

   - **Android SDK Platform**: Android 14.0 ("UpsideDownCake") (API Level 34)
   - **Android SDK Build-Tools**: Version 34.0.0 or higher
   - **NDK**: Any 28.x version
   - **CMake**: Version 3.10.2

   You might need to select **Show Package Details** in the SDK Manager to see
   all of the available versions of a tool.
2. In Godot, go to **Editor \> Editor Settings \> Export \> Android** and provide
   the path to your SDK.

## Create a Godot XR project

Set up a new project for spatial rendering:

1. Open Godot and create a new project.
2. For the **Renderer** , select **Mobile**.

   This is the highly-performant, Vulkan-first graphics API recommended for
   Android XR.

   ![Create New Project dialog in Godot Engine.](https://developer.android.com/static/images/develop/xr/godot/godot-new-project.png)
3. Select any other options that you want, and click **Create**.

4. Construct your internal XR scene (including `XROrigin3D` and `XRCamera3D`)
   using the [Official Godot XR Scene Setup Guide](https://docs.godotengine.org/en/stable/tutorials/xr/setting_up_xr.html).

   ![Construct your internal XR scene in your new Godot project](https://developer.android.com/static/images/develop/xr/godot/godot-xr-scene-setup.webp)

## Configure project settings

Next, you'll configure project settings to enable OpenXR and configure the
rendering pipeline for mobile performance:

1. Open Godot.
2. Configure the following project settings for OpenXR:
   - Go to **Project \> Project Settings \> XR \> OpenXR** , and select **Enabled**.
   - Go to **Project \> Project Settings \> XR \> Shaders** , and select **Enabled**.
3. Go to **Rendering \> Anti Aliasing \> Quality \> MSAA 3D** , and select
   **4x**.

   This setting provides the best clarity in Android XR.

## Set up your project to export to Android XR

Complete the following steps to set up your project to export to Android XR:

1. **Set up an Export Preset** : Go to **Project \> Export** and click **Add... \>
   Android**.

2. **Complete the Deployment Guide** : Follow the [Official Godot Android
   Deployment Guide](https://docs.godotengine.org/en/stable/tutorials/xr/deploying_to_android.html) for step-by-step instructions on
   permissions and one-click deployment.

3. **Check your project's SDK Versions**:

   - For the **Min SDK**: 34
   - For the **Target SDK**: 34
4. **Configure the XR Mode** : Set the **XR Mode** to **OpenXR** in the export
   settings.

## Install the Godot OpenXR Vendors Plugin

Your app must use the Vendors Plugin to access Android XR specific extensions.
Follow these steps to get a compatible version:

1. In Godot, select **AssetLib**.
2. Search for "Vendor".

   ![Find different versions of the Godot OpenXR Vendors plugin by searching the Godot Asset Library](https://developer.android.com/static/images/develop/xr/godot/godot-assetlib-search.png)
3. Find version 5.1 (or higher) of the [Godot OpenXR Vendors
   plugin](https://github.com/godotvr/godot_openxr_vendors) and download it.

4. After the download completes, select **Install**.

   ![Install the Godot OpenXR Vendors plugin](https://developer.android.com/static/images/develop/xr/godot/godot-configure-asset-install.png)

## See also

For more information about Android XR development with Godot, see the following
pages in the Godot Engine documentation:

- [Official Godot XR Documentation](https://docs.godotengine.org/en/stable/tutorials/xr/index.html)
- [Godot Android Export Documentation](https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_android.html)