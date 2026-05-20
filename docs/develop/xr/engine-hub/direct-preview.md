---
title: https://developer.android.com/develop/xr/engine-hub/direct-preview
url: https://developer.android.com/develop/xr/engine-hub/direct-preview
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Direct Preview Preview is a feature in the [Android XR Engine
Hub](https://developer.android.com/develop/xr/engine-hub) that lets you test and iterate on complex interactions directly inside
your game engine's editor using live data from the Android XR Device. This
completely bypasses the usual, time-consuming build-and-deploy cycle within XR
development.

With Direct Preview, instead of exporting a full APK every time
you make a change, your host machine renders and debugs the content, streams the
visual viewport directly to your physical Android XR device, and streams
supported OpenXR extensions back to the host machine in real-time.

## Direct Preview OpenXR support

Direct Preview enables instant, low-latency testing inside your
engine's viewport for the following streamed extensions:

| Feature or capability | OpenXR extension string |
|---|---|
| Device Anchor Persistence | [`XR_ANDROID_device_anchor_persistence`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_device_anchor_persistence) |
| Raycast | [`XR_ANDROID_raycast`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_raycast) |
| Trackables (Planes/Depth) | [`XR_ANDROID_trackables`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_trackables) |
| Object Tracking | [`XR_ANDROID_trackables_object`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_trackables_object) |
| Scene Meshing | [`XR_ANDROID_scene_meshing`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_scene_meshing) |
| Face Tracking | [`XR_ANDROID_face_tracking`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_face_tracking) |
| Eye Tracking | [`XR_ANDROID_eye_tracking`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_eye_tracking) |
| Passthrough Camera State | [`XR_ANDROID_passthrough_camera_state`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_passthrough_camera_state) |
| Hand Interaction | [`XR_EXT_hand_interaction`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_hand_interaction) |

## Get started with Direct Preview in the Android Engine Hub

Follow the steps in the following sections to enable
Direct Preview, configure your physical Android XR device, and
enable and start low-latency Direct Preview in your game engine:

### Download and install the Android XR Engine Hub

First, [download and install](https://developer.android.com/develop/xr/engine-hub) the latest version of the Android XR Engine
Hub.

### Connect and configure your Android XR device

Next, connect and configure your Android XR device for
Direct Preview:

1. Close any open game engine editors that you have running.
2. Open the [Android XR Engine Hub](https://developer.android.com/develop/xr/engine-hub).

   ![The Device Manger screen in the Android XR Engine Hub](https://developer.android.com/static/images/develop/xr/engine-hub/device-manager.png)
3. Connect your Android XR device to your host machine using a high-quality
   USB-C cable.

   > [!NOTE]
   > **Note:** You must enable [developer options](https://developer.android.com/studio/debug/dev-options#enable) and [debugging](https://developer.android.com/studio/debug/dev-options#Enable-debugging) on the Android XR device so that your host machine can send ADB (Android Debug Bridge) commands.

4. From the device drop-down menu at the top of the interface, select your
   connected Android XR device.

   ![Select the device that you want to use with Direct Preview](https://developer.android.com/static/images/develop/xr/engine-hub/select-device.png)
5. Check that the stream client is initialized:

   1. Click **Install Stream Client** to deploy the necessary daemon to your headset.
   2. Click **Set** for **Active OpenXR Runtime** to redirect engine calls from the host machine to the device stream.

   ![Enable Direct Preview in the Android XR Engine Hub](https://developer.android.com/static/images/develop/xr/engine-hub/direct-preview.png)

### Configure and start Direct Preview in your game engine

Finally, configure and start Direct Preview in your game engine:

1. Complete the first-time setup and configuration steps for your game engine:

   - [Unity](https://developer.android.com/develop/xr/unity/direct-preview)
   - [Godot](https://developer.android.com/develop/xr/godot/direct-preview)
   - [Unreal Engine](https://developer.android.com/develop/xr/unreal/direct-preview)
2. Follow the steps in the "Start Direct Preview" section for
   your game engine each time you want to start Direct Preview:

   - [Unity](https://developer.android.com/develop/xr/unity/direct-preview#start)
   - [Godot](https://developer.android.com/develop/xr/godot/direct-preview#start)
   - [Unreal Engine](https://developer.android.com/develop/xr/unreal/direct-preview#start)

   > [!IMPORTANT]
   > **Important:** If you get a new Android XR device that you want to use with Direct Preview, follow the preceding steps in the Android XR Engine hub to [connect and configure that device](https://developer.android.com/develop/xr/engine-hub/direct-preview#connect-configure) for Direct Preview before you start Direct Preview through your game engine.