---
title: https://developer.android.com/develop/xr/unreal/xr-extensions-quickstart
url: https://developer.android.com/develop/xr/unreal/xr-extensions-quickstart
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

This quickstart guides you through importing the Android XR Extension Plugin for
Unreal Engine and then configuring your project settings.

## Prerequisites

Before completing these steps, make sure you've completed the steps described in
[Unreal Engine project setup](https://developer.android.com/develop/xr/unreal/setup).

## Add the Android XR Extension for Unreal Plugin

The Android XR functionality for Unreal Engine is delivered as a vendor plugin
that provides OpenXR extension support.

1. Create a `Plugins` folder in your Unreal project's root directory if it doesn't already exist.
2. Clone the [android-xr-unreal-vendor-plugin](https://github.com/android-xr/android-xr-unreal-vendor-plugin) repository into
   the `Plugins` folder:

       git clone https://github.com/android-xr/android-xr-unreal-vendor-plugin

3. Restart the Unreal Editor.

4. If you're prompted to rebuild missing modules, click **Yes**.

## Configure project settings

After the plugin is added, you must enable it within the editor:

1. Go to **Edit \> Plugins**.
2. Search for the **Android XR** or **OpenXR** extensions, and then enable them.
3. In **Project Settings** , navigate to the **Android** platform section.
4. Make sure that **Minimum SDK Version** and **Target SDK Version** are set to at least **34**.

## Next steps

After installing and enabling the Android XR Extensions plugins, explore the
following resources to start building and testing your app:

- Explore the [Android XR Extensions for Unreal API reference](https://developer.android.com/develop/xr/unreal/reference) for the Blueprint function libraries, subsystems, and components available for each extension.
- Review the [supported OpenXR extensions](https://developer.android.com/develop/xr/unreal#supported-extensions) to see which Unreal classes and OpenXR extensions are available for each capability.
- Set up [Direct Preview for Unreal Engine](https://developer.android.com/develop/xr/unreal/direct-preview) to stream and test your project live from the Unreal Editor on an Android XR device.