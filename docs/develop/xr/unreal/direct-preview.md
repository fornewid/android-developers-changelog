---
title: https://developer.android.com/develop/xr/unreal/direct-preview
url: https://developer.android.com/develop/xr/unreal/direct-preview
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Direct Preview lets you test and iterate on complex interactions
directly inside the Unreal Editor using live data from the Android XR Device.
With Direct Preview, the host machine renders and debugs the content, streams
the visual viewport directly to your physical Android XR device, and streams
supported OpenXR extensions back to the host in real time.

Follow this guide to set up Direct Preview for your project in
Unreal Engine.

## Prerequisites

Before beginning, ensure your development environment meets the following
requirements:

- **Unreal Engine version** : [Unreal Engine 5.6.1](https://www.unrealengine.com/download) or higher.
- **Project setup** : Complete all steps in the [Unreal Engine project setup](https://developer.android.com/develop/xr/unreal/setup) guide.

<!-- -->

- **Android XR Engine Hub** : Complete all the steps in the [get started](https://developer.android.com/develop/xr/engine-hub#get-started) section of the Android XR Engine Hub guide to install and configure your host machine for Direct Preview.
- **Hardware**:

  - Use a host machine running Windows 11.
  - Use a modern graphics card with **Vulkan Video Encoding** support.

  > [!IMPORTANT]
  > **Important:** Update your GPU drivers to their latest versions before to check for all of its Vulkan capabilities.

## Set up Android XR plugins

Set up Unreal Engine with the required Android XR plugins:

1. Follow the steps in the [Android XR Extensions for Unreal Engine
   quickstart](https://developer.android.com/develop/xr/unreal/xr-extensions-quickstart) guide.

   Later, if you create a new project or open a project that you haven't used
   with Direct Preview, follow those same steps again.
2. For each project, make sure the project has a symlink to the vendor plugins
   folder.

## Configure project settings

Configure your project settings for Direct Preview streaming:

1. Navigate to **Project Settings \> Platforms \> Windows**.
2. For **RHI** to **Vulkan**.
3. Navigate to **Edit \> Plugins**.
4. Enable the **AndroidXRStreaming** plugin.
5. Navigate to **Edit** \> **Project Settings** \> **Description**.
6. Enable **Start In VR**.

## Enable the streaming runtime

Now that the project has the **AndroidXRStreaming** plugin enabled, check if the
Android XR Streaming runtime is present:

1. Go to **Project Settings \> Plugins \> AndroidXRStreaming**.
2. Click **Enable AndroidXR Streaming**.

   ![Enable the Android XR Streaming runtime](https://developer.android.com/static/images/develop/xr/unreal/direct-preview-enable-streaming-runtime.png)

   > [!NOTE]
   > **Note:** This works by setting a session-based environment variable for the Unreal Engine process, so there is no need to change any registry entries even if multiple runtimes are present on the machine.

3. Restart Unreal Engine to apply these changes.

## Configure the streaming client

Configure the streaming client with different options for your project:

1. Go to **Project Settings \> Plugins**.
2. In **AndroidXRStreamingClient** section, review each of the following
   options and enable or disable them to match what you need for your project:

   - **Auto Start Client On Preview** : When enabled, launches the preview client app on any valid, selected device when clicking **Start VR
     Preview** from the editor.
   - **Auto Stop Client On Preview**: When enabled, terminates the preview client when the VR preview from the editor is stopped.
   - **Auto Select Compatible Device**: When enabled, automatically selects the first compatible device that is connected to the machine when searching for devices.
   - **Show Error Dialogs**: When enabled, displays additional error dialogs (for example, an error dialog displays if you try to start a VR preview without selecting a client device). Disable this option to hide these dialogs.
   - **Refresh** : When enabled, the **Refresh** button searches for connected devices and lists compatible ones (determined by the presence of the Direct Preview client app in the [Android XR Engine
     Hub](https://developer.android.com/develop/xr/engine-hub)).

## Start Direct Preview

Start Direct Preview to stream directly from Unreal Engine:

1. Connect your Android XR device to your host machine using a high-quality
   USB-C cable.

   > [!NOTE]
   > **Note:** You must enable [developer options](https://developer.android.com/studio/debug/dev-options#enable) and [debugging](https://developer.android.com/studio/debug/dev-options#Enable-debugging) on the Android XR device so that your host machine can send ADB (Android Debug Bridge) commands.

2. If you've never used this device with Direct Preview before,
   [connect and configure the device for Direct Preview](https://developer.android.com/develop/xr/engine-hub/direct-preview#connect-configure)
   in the Android XR Engine Hub before you start
   Direct Preview through your game engine.

3. In the Unreal Editor, click **Play level in VR** . Don't use the usual **Play
   in Editor** option when starting Direct Preview.