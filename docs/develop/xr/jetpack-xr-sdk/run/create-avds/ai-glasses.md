---
title: Create virtual AI glasses devices  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/ai-glasses
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Create virtual AI glasses devices Stay organized with collections Save and categorize content based on your preferences.




Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/ai-glasses-icon.svg)


AI Glasses

[Learn about XR device types →](/develop/xr/devices)

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

[![](/static/images/picto-icons/plus.svg)

See also

If this your first time using an emulator with Android Studio, review the Android Emulator documentation.

arrow\_forward](https://developer.android.com/studio/run/emulator)

## Check system requirements

Before you start creating Android Virtual Devices (AVDs) for AI glasses, review
the following system requirements.

**Note:** The Android XR Emulator is designed for developing Android apps in Android
Studio and doesn't support Unity or OpenXR apps.

* **Android Studio**: Install the [latest Canary build](/studio/preview) and [configure
  Studio for XR development](/develop/xr/jetpack-xr-sdk/get-studio).
* **System**: A computer with at least [the same specs as what's required for
  the Android Emulator](/studio/run/emulator#requirements), except ChromeOS isn't supported. Plan for extra
  disk space because AI glasses AVDs also require a phone AVD to act as the
  host device for your app.

## Create an Android Virtual Device for AI glasses

Follow these steps to create an AVD for AI glasses to use as you test and debug
your app:

1. Open the latest Canary build of Android Studio, and then click **Tools >
   Device Manager > Add a new device
   ![](/static/studio/images/buttons/ic_plus.png) > Create Virtual Device**.

   ![The Device Manager panel in Android
   Studio.](/static/images/develop/xr/jetpack-xr-sdk/run/xr-avds.png)
2. In the **Add Device** window, in the **Form Factor** section, select **XR**.
3. From the list, select **AI Glasses**, and then click **Next**.
4. In the **Configure Virtual Device** tab in the **Select system image**
   section, select the most-recent AI Glasses system image that is compatible
   with your system from the list of system images.

   ![Android Studio "Configure virtual device"
   window.](/static/images/develop/xr/jetpack-xr-sdk/run/ai-glasses-avd-system-image.png)
5. Click **Finish** and click **Yes** if prompted to download the system image
   that you selected.

## Create a phone AVD to act as the host device

AI glasses AVDs also require a phone AVD to act as the host device for your app.
First, create a phone AVD to act as the host device for the AI glasses:

1. In Android Studio, return to the Device Manager and click **Add a new device
   ![](/static/studio/images/buttons/ic_plus.png) > Create Virtual Device**.
2. In the **Add Device** window, in the **Form Factor** section, select
   **Phone**.
3. Select any phone device (this example uses a Pixel 9 Pro), and then click
   **Next**.
4. From the **API** drop-down menu, select **API CANARY Preview**.

   ![The AVD API level configuration for the phone host
   device.](/static/images/develop/xr/jetpack-xr-sdk/run/host-device-avd-api.png)
5. In the **Select system image** section, select the most-recent system image
   that is compatible with your system from the list of system images:

   * Google Play ARM 64 v8a System Image (macOS)
   * Google Play Intel x86\_64 Atom System Image (Windows and Linux)

   ![The AVD system image configuration for the phone host
   device.](/static/images/develop/xr/jetpack-xr-sdk/run/host-device-avd-system-image.png)
6. Click **Finish**.

## Pair the devices

Finally, pair the devices:

**Note:** If you're having issues pairing the devices using the Pairing Assistant,
you can also try to [pair
manually](/develop/xr/jetpack-xr-sdk/run/emulator/ai-glasses-troubleshoot#pairing-assistant).

1. In the Device Manager, find the AI glasses AVD and select **Pair Glasses**
   from the overflow menu.

   ![The Pair Glasses option in the Device Manager launches the Pairing
   Assistant.](/static/images/develop/xr/jetpack-xr-sdk/run/ai-glasses-avd-pair-glasses.png)
2. Select the phone AVD from the list of compatible devices.

   ![The list of compatible host devices that can be
   paired.](/static/images/develop/xr/jetpack-xr-sdk/run/pairing-assistant-select-device.png)

   The Pairing Assistant launches both AVDs in the emulator and initiates
   pairing.

   ![The Pairing Assistant uses the phone AVD to present association
   requests.](/static/images/develop/xr/jetpack-xr-sdk/run/pairing-assistant-accept-requests.png)
3. On the phone AVD, accept both requests to associate the devices.

   The Pairing Assistant completes pairing.

   ![The Pairing Assistant completes pairing after the association requests are
   accepted.](/static/images/develop/xr/jetpack-xr-sdk/run/pairing-assistant-complete.png)

**Note:** After you've completed pairing the first time, the emulators automatically
reconnect the devices to each other whenever you launch them. If the emulators
fail to reconnect the devices, see the [troubleshooting steps](/develop/xr/jetpack-xr-sdk/run/emulator/ai-glasses-troubleshoot#emulators-dont-reconnect).

## Next steps

Now that you've created your AVDs for AI glasses, [run your app on the AVDs
using the emulator](/develop/xr/jetpack-xr-sdk/run/emulator/ai-glasses).

---

OpenXR™ and the OpenXR logo are trademarks owned
by The Khronos Group Inc. and are registered as a trademark in China,
the European Union, Japan and the United Kingdom.

[Next

Run your app on the emulator

arrow\_forward](/develop/xr/jetpack-xr-sdk/run/emulator/ai-glasses)