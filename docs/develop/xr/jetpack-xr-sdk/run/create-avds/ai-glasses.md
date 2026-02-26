---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/ai-glasses
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/ai-glasses
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) AI Glasses [](https://developer.android.com/develop/xr/devices#ai-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

The Android XR Emulator is a specialized version of the Android Emulator that is
designed for XR app development. It lets you test and debug your XR apps within
the familiar environment of Android Studio.

Before you can run your app in the Android XR Emulator, you need to set it up.
Create Android Virtual Devices (AVDs) for AI glasses to use with the Android XR
Emulator as you test and debug your app. The emulator for AI glasses acts as a
standalone, virtual device that you can pair with an emulator instance running a
phone AVD.

Follow the steps in the following sections to set up everything you need for
these virtual devices.
[![](https://developer.android.com/static/images/picto-icons/plus.svg) See also If this your first time using an emulator with Android Studio, review the Android Emulator documentation.](https://developer.android.com/studio/run/emulator)

## Check system requirements

Before you start creating Android Virtual Devices (AVDs) for AI glasses, review
the following system requirements.

> [!NOTE]
> **Note:** The Android XR Emulator is designed for developing Android apps in Android Studio and doesn't support Unity or OpenXR apps.

- **Android Studio** : Install the [latest Canary build](https://developer.android.com/studio/preview) and [configure
  Studio for XR development](https://developer.android.com/develop/xr/jetpack-xr-sdk/get-studio).
- **System** : A computer with at least [the same specs as what's required for
  the Android Emulator](https://developer.android.com/studio/run/emulator#requirements), except ChromeOS isn't supported. Plan for extra disk space because AI glasses AVDs also require a phone AVD to act as the host device for your app.

## Create an Android Virtual Device for AI glasses

Follow these steps to create an AVD for AI glasses to use as you test and debug
your app:

1. Open the latest Canary build of Android Studio, and then click **Tools \>
   Device Manager \> Add a new device
   ![](https://developer.android.com/static/studio/images/buttons/ic_plus.png) \> Create Virtual Device**.

   ![The Device Manager panel in Android
   Studio.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/xr-avds.png)
2. In the **Add Device** window, in the **Form Factor** section, select **XR**.

3. From the list, select **AI Glasses** , and then click **Next**.

4. In the **Configure Virtual Device** tab in the **Select system image**
   section, select the most-recent AI Glasses system image that is compatible
   with your system from the list of system images.

   ![Android Studio "Configure virtual device"
   window.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/ai-glasses-avd-system-image.png)
5. Click **Finish** and click **Yes** if prompted to download the system image
   that you selected.

## Create a phone AVD to act as the host device

AI glasses AVDs also require a phone AVD to act as the host device for your app.
First, create a phone AVD to act as the host device for the AI glasses:

1. In Android Studio, return to the Device Manager and click **Add a new device
   ![](https://developer.android.com/static/studio/images/buttons/ic_plus.png) \> Create Virtual Device**.
2. In the **Add Device** window, in the **Form Factor** section, select **Phone**.
3. Select any phone device (this example uses a Pixel 9 Pro), and then click **Next**.
4. From the **API** drop-down menu, select **API CANARY Preview**.

   ![The AVD API level configuration for the phone host
   device.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/host-device-avd-api.png)
5. In the **Select system image** section, select the most-recent system image
   that is compatible with your system from the list of system images:

   - Google Play ARM 64 v8a System Image (macOS)
   - Google Play Intel x86_64 Atom System Image (Windows and Linux)

   ![The AVD system image configuration for the phone host
   device.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/host-device-avd-system-image.png)
6. Click **Finish**.

## Pair the devices

Finally, pair the devices:

> [!NOTE]
> **Note:** If you're having issues pairing the devices using the Pairing Assistant, you can also try to [pair
> manually](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/emulator/ai-glasses-troubleshoot#pairing-assistant).

1. In the Device Manager, find the AI glasses AVD and select **Pair Glasses**
   from the overflow menu.

   ![The Pair Glasses option in the Device Manager launches the Pairing
   Assistant.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/ai-glasses-avd-pair-glasses.png)
2. Select the phone AVD from the list of compatible devices.

   ![The list of compatible host devices that can be
   paired.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/pairing-assistant-select-device.png)

   The Pairing Assistant launches both AVDs in the emulator and initiates
   pairing.

   ![The Pairing Assistant uses the phone AVD to present association
   requests.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/pairing-assistant-accept-requests.png)
3. On the phone AVD, accept both requests to associate the devices.

   The Pairing Assistant completes pairing.

   ![The Pairing Assistant completes pairing after the association requests are
   accepted.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/pairing-assistant-complete.png)

> [!NOTE]
> **Note:** After you've completed pairing the first time, the emulators automatically reconnect the devices to each other whenever you launch them. If the emulators fail to reconnect the devices, see the [troubleshooting steps](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/emulator/ai-glasses-troubleshoot#emulators-dont-reconnect).

## Next steps

Now that you've created your AVDs for AI glasses, [run your app on the AVDs
using the emulator](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/emulator/ai-glasses).

*** ** * ** ***

OpenXR™ and the OpenXR logo are trademarks owned
by The Khronos Group Inc. and are registered as a trademark in China,
the European Union, Japan and the United Kingdom.