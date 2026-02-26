---
title: https://developer.android.com/develop/xr/unity/performance/urp-asset-settings
url: https://developer.android.com/develop/xr/unity/performance/urp-asset-settings
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Unity provides a variety of performance-related features and settings in its
Universal Render Pipeline (URP) Asset settings. Enable or disable these features
to reduce GPU and CPU performance costs and to improve visual quality.

## Change URP Asset settings

Follow these steps to access Unity's URP Asset settings, where you can configure
the performance features that are outlined in the subsequent sections:

1. From the Unity main menu, click **Edit \> Project Settings \> Graphics**.
2. Find your **Default Render Pipeline** asset, which is also your URP asset.
3. Search for this asset in your project.
4. Right-click the asset and select **Properties**.

### Disable HDR

Disable HDR to improve performance on mobile XR hardware, where HDR provides
minimal visual benefit compared to its performance cost.

#### Disable this feature

In the URP Asset properties that you [navigated to earlier](https://developer.android.com/develop/xr/unity/performance/urp-asset-settings#access-urp-asset-settings), disable **HDR**.

### Disable post processing

Post processing is expensive on mobile XR hardware and often provides minimal
visual benefit compared to its performance cost.

#### Disable this feature

1. In the URP Asset properties that you [navigated to earlier](https://developer.android.com/develop/xr/unity/performance/urp-asset-settings#access-urp-asset-settings), find the **Renderer List**.
2. In the **Renderer List** , right-click the **Universal Renderer** and select **Properties**.
3. In the **Post-Processing** section, deselect **Enabled**.

### Disable Depth Priming Mode

XR devices use two views, which increases the performance cost of performing the
depth pre-pass required for depth priming. Depth priming skips drawing
overlapping pixels to speed up rendering by using the depth texture to check for
overlaps.

But for untethered XR devices, there's no advantage to using depth priming as
you can achieve similar results by using hardware optimization features like
Low-Resolution-Z (LRZ) or Hidden Surface Removal (HSR).

#### Benefits

- Avoids increased performance impact from the depth pre-pass due to the two views on XR devices.
- Allows use of hardware optimizations like LRZ or HSR for similar results.
- Eliminates an unsupported and unnecessary step for untethered XR devices.

#### Disable this feature

1. In the URP Asset properties that you [navigated to earlier](https://developer.android.com/develop/xr/unity/performance/urp-asset-settings#access-urp-asset-settings), find the **Renderer List**.
2. Right-click the **(Universal Renderer Data)** file and select **Properties**.
3. Change the **Depth Priming Mode** to **Disabled**.

### Enable MSAA for anti-aliasing

Using Multi-sample Anti-aliasing (MSAA) is an efficient way to improve visual
quality on mobile and untethered XR platforms. Tile-based GPUs, which are common
in these devices, can store more samples in the same tile.

This makes MSAA a performance-efficient anti-aliasing solution. A 2X MSAA value
provides a good balance between visual quality and performance.

#### Enable this feature

In the URP Asset properties that you [navigated to earlier](https://developer.android.com/develop/xr/unity/performance/urp-asset-settings#access-urp-asset-settings), change **Anti
Aliasing (MSAA)** to **2x**.

## Use URP Debug mode settings and features

Other important URP Asset settings are available through Debug mode. Follow
these steps to access these settings:

1. From the Unity main menu, click **Edit \> Project Settings**.
2. Select **Graphics** section from the left panel.
3. Find your **Default Render Pipeline** asset (this is your URP asset).
4. Search for this asset in your project and select it.
5. Click the three dots in the top right and select **Debug**.

### Disable Depth and Opaque Textures

Disabling depth and opaque textures eliminates extra texture copying that wastes
GPU time. These textures cause additional copy operations and GMEM loads, which
reduces performance.

In your URP Asset Debug settings, disable the following options:

- **Require Depth Textures**
- **Require Opaque Texture**

### Enable SRP Batcher

The [SRP Batcher](https://unity.com/blog/engine-platform/srp-batcher-speed-up-your-rendering)
reduces CPU time for scenes with many materials using the same shader variant by
reducing render-state changes between draw calls.

In your URP Asset Debug settings, enable **Use SRP Batcher**.