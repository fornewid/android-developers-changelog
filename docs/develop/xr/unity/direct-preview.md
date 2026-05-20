---
title: https://developer.android.com/develop/xr/unity/direct-preview
url: https://developer.android.com/develop/xr/unity/direct-preview
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Direct Preview lets you test and iterate on complex interactions
directly inside the Unity Editor Play Mode using live data from the Android XR
Device. With Direct Preview, the host machine renders and debugs
the content, streams the visual viewport directly to your physical Android XR
device, and streams supported OpenXR extensions back to the host in real time.

Follow this guide to set up Direct Preview for your project in
Unity.

## Prerequisites

Before beginning, ensure your development environment meets the following
requirements:

- **Unity version** : Unity 6 [version 6000.3.5f2](https://unity.com/releases/editor/whats-new/6000.0.58f2) or higher.
- **Project setup** : Complete all steps in the [Unity project setup](https://developer.android.com/develop/xr/unity/setup) guide.
- **Unity packages** : Complete all steps in the [Android XR Extensions for
  Unity quickstart](https://developer.android.com/develop/xr/unity/xr-extensions-quickstart) guide. When importing packages, use version 1.2.0 or higher of the Android XR Extensions for Unity. This is provided as a tar file in [each release](https://github.com/android/android-xr-unity-package/releases).

<!-- -->

- **Android XR Engine Hub** : Complete all the steps in the [get started](https://developer.android.com/develop/xr/engine-hub#get-started) section of the Android XR Engine Hub guide to install and configure your host machine for Direct Preview.
- **Hardware**:

  - Use a host machine running Windows 11.
  - Use a modern graphics card with **Vulkan Video Encoding** support.

  > [!IMPORTANT]
  > **Important:** Update your GPU drivers to their latest versions before to check for all of its Vulkan capabilities.

### Review known issues and limitations

Review the following known issues and limitations so you know what to expect as
you use Direct Preview in Unity:

- **Audio**: Audio doesn't stream to the headset. Instead, it plays through the speakers or headphones on your host machine.
- **Resolution** : Controls for altering resolution are limited. The system requests `{2364, 2880}` per eye.
- **UI/UX**: The client connection flow is functional but unpolished for this early release.
- **Extension Support**: While many extensions are supported (such as Hand Tracking, Eye Gaze, and Face Tracking), this is a limited set compared to native builds.

## Configure graphics settings

Set Vulkan as the default renderer on Windows that handles video stream
encoding:

1. Navigate to **Edit** \> **Project Settings** \> **Player**.
2. Click the **Other Settings** tab.
3. Deselect **Auto Graphics API for Windows**.
4. If **Direct3D11** or **Direct3D12** are listed, select each one and click **minus (-)**.
5. **Add Vulkan** : Click **plus (+)** and select **Vulkan**.

   ![Use Vulkan as the Graphics API for Windows](https://developer.android.com/static/images/develop/xr/unity/direct-preview-graphics-api-windows.png)
6. **Restart** the Unity Editor to apply these changes.

## Configure OpenXR plugin management settings

Configure your OpenXR plugins for streaming:

1. Navigate to **Edit** \> **Project Settings** \> **XR Plug-in Management**.
2. Click the **Windows / Standalone** tab (this tab has a computer icon).
3. In the **Plug-in Providers** section, select **OpenXR**.
4. In the **OpenXR Feature Group** section, select **Android XR (Extensions)**.
5. Select both **Android XR Support** and **Android XR: AR Sessions**.

   This enables all supported features and dependencies for streaming.

   ![Enable multiple OpenXR plugins to support Direct Preview streaming](https://developer.android.com/static/images/develop/xr/unity/direct-preview-openxr-plugin-management.png)
6. **Restart** the Unity Editor to apply these changes.

## Configure graphics and quality settings

Configure the following settings to ensure stream compatibility:

1. Navigate to **Edit** \> **Project Settings** \> **XR Plugin Management** \> **OpenXR**.
2. For each of the following settings, select the following options:

   - **Render Mode**: Multi-pass
   - **Depth Submission**: Depth 24 bit
   - **Foveated Rendering API**: Legacy

   ![Configure the graphics and quality settings to ensure stream
   compatibility](https://developer.android.com/static/images/develop/xr/unity/direct-preview-graphics-quality.png)

## Perform project validation

Perform project validation to fix any OpenXR errors in your project's
configuration:

1. Navigate to **Edit** \> **Project Settings** \> **XR Plug-in Management** \> **Project Validation**.
2. Click the **Standalone** tab.
3. Click **Fix All** for any errors with the `[OpenXR]` prefix.
4. Click **Fix All** for any errors with the `[Android XR Streaming]` prefix.

   ![Perform project validation to fix any OpenXR errors in your project's
   configuration:](https://developer.android.com/static/images/develop/xr/unity/direct-preview-project-validation.png)

## Start Direct Preview

Start Direct Preview to stream directly from Unity:

1. Connect your Android XR device to your host machine using a high-quality
   USB-C cable.

   > [!NOTE]
   > **Note:** You must enable [developer options](https://developer.android.com/studio/debug/dev-options#enable) and [debugging](https://developer.android.com/studio/debug/dev-options#Enable-debugging) on the Android XR device so that your host machine can send ADB (Android Debug Bridge) commands.

2. If you've never used this device with Direct Preview before,
   [connect and configure the device for Direct Preview](https://developer.android.com/develop/xr/engine-hub/direct-preview#connect-configure)
   in the Android XR Engine Hub before you start
   Direct Preview through your game engine.

3. In the Unity Editor, click **Play**.

   The device stream automatically starts.