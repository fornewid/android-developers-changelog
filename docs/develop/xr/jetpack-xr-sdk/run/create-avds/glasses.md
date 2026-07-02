---
title: Create virtual devices for audio glasses and display glasses  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/glasses
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 4](https://android-developers.googleblog.com/2026/05/android-xr-sdk-developer-preview-4-updates.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Create virtual devices for audio glasses and display glasses Stay organized with collections Save and categorize content based on your preferences.





Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/ai-glasses-icon.svg)


Audio &  
Display Glasses

[Learn about XR device types →](/develop/xr/devices)

The Android XR Emulator is a specialized version of the Android Emulator that is
designed for XR app development. It lets you test and debug your XR apps within
the familiar environment of Android Studio.

Before you can run your app in the Android XR Emulator, you need to set it up.
Create Android Virtual Devices (AVDs) for audio glasses and display glasses to
use with the Android XR Emulator as you test and debug your app. The emulator
for audio glasses and display glasses acts as a separate, virtual device that
you can pair with an emulator instance running a phone AVD.

Follow the steps in the following sections to set up everything you need for
these virtual devices.

[![](/static/images/picto-icons/plus.svg)

See also

If this your first time using an emulator with Android Studio, review the Android Emulator documentation.

arrow\_forward](https://developer.android.com/studio/run/emulator)

## Check system requirements

Before you start creating Android Virtual Devices (AVDs) for audio glasses and
display glasses, review the following system requirements.

**Note:** The Android XR Emulator is designed for developing Android apps in Android
Studio and doesn't support Unity or OpenXR apps.

* **Android Studio**: Install the [latest Canary build](/studio/preview) and [configure
  Studio for XR development](/develop/xr/jetpack-xr-sdk/get-studio).
* **System**: A computer with at least [the same specs as what's required for
  the Android Emulator](/studio/run/emulator#requirements), except ChromeOS isn't supported. Plan for extra
  disk space because audio glasses and display glasses AVDs also require a
  phone AVD to act as the host device for your app.

## Create an Android Virtual Device for audio glasses or display glasses

Follow these steps to create an AVD for audio glasses or display glasses that
you can use as you test and debug your app:

1. Open the latest Canary build of Android Studio, and then click **Tools >
   Device Manager > Add a new device
   ![](/static/studio/images/buttons/ic_plus.png) > Create Virtual Device**.

   ![The Device Manager panel in Android Studio.](/static/images/develop/xr/jetpack-xr-sdk/run/xr-avds-audio-display-glasses.png)
2. In the **Add Device** window, in the **Form Factor** section, select **XR**.
3. From the list, select either **Audio Glasses** or **Display Glasses**, and
   then click **Next**.
4. In the **Configure Virtual Device** tab in the **Select system image**
   section, select the most-recent system image that is compatible with your
   system from the list of system images.

   ![Android Studio ](/static/images/develop/xr/jetpack-xr-sdk/run/audio-glasses-avd-system-image.png)
5. Click **Finish**, and also click **Yes** if prompted to download the system
   image that you selected.

## Create a phone AVD to act as the host device

Audio glasses and display glasses AVDs also require a phone AVD to act as the
host device for your app.

**Note:** Each audio glasses or display glasses AVD needs a separate, phone AVD to
act as a host device. A single phone AVD can't be paired to multiple audio or
display glasses AVDs.

First, create a phone AVD to act as the host device for the glasses:

1. In Android Studio, return to the Device Manager and click **Add a new device
   ![](/static/studio/images/buttons/ic_plus.png) > Create Virtual Device**.
2. In the **Add Device** window, in the **Form Factor** section, select
   **Phone**.
3. Select any phone device (this example uses a Pixel 9 Pro), and then click
   **Next**.
4. From the **API** drop-down menu, select **API CANARY Preview**.

   ![The AVD API level configuration for the phone host device.](/static/images/develop/xr/jetpack-xr-sdk/run/host-device-avd-api.png)
5. In the **Select system image** section, select the most-recent system image
   that is compatible with your system from the list of system images:

   * Pre-Release 16 KB Page Size Google Play ARM 64 v8a System Image (macOS)
   * Pre-Release 16 KB Page Size Google Play Intel x86\_64 Atom System Image
     (Windows and Linux)

   ![The AVD system image configuration for the phone host device.](/static/images/develop/xr/jetpack-xr-sdk/run/host-device-avd-system-image.png)
6. Click **Finish**, and also click **Yes** if prompted to download the system
   image that you selected.

## Pair the devices

Finally, pair the devices:

1. In the Device Manager, find the audio glasses or display glasses AVD and
   select **Pair Glasses** from the overflow menu.

   ![The Pair Glasses option in the Device Manager launches the Pairing Assistant.](/static/images/develop/xr/jetpack-xr-sdk/run/audio-display-glasses-avd-pair.png)

   **Note:** If you encounter issues while pairing the devices using the Pairing
   Assistant, you can also try to [pair manually](/develop/xr/jetpack-xr-sdk/run/emulator/glasses-troubleshoot#pairing-assistant).
2. Select the phone AVD from the list of compatible devices.

   ![The list of compatible host devices that can be paired.](/static/images/develop/xr/jetpack-xr-sdk/run/pairing-assistant-select-device.png)

   The Pairing Assistant launches both AVDs in the emulator and initiates
   pairing.
3. On the phone AVD, accept the permission requests to associate the devices.

   ![The Pairing Assistant uses the phone AVD to present association requests.](/static/images/develop/xr/jetpack-xr-sdk/run/pairing-assistant-accept-requests.png)

   The Pairing Assistant completes pairing.

   ![The Pairing Assistant completes pairing after the association requests are accepted.](/static/images/develop/xr/jetpack-xr-sdk/run/pairing-assistant-complete.png)

**Note:** After you've completed pairing the first time, the emulators automatically
reconnect the devices to each other whenever you launch them. If the emulators
fail to reconnect the devices, see the [troubleshooting steps](/develop/xr/jetpack-xr-sdk/run/emulator/glasses-troubleshoot#emulators-dont-reconnect).

## Next steps

After you've created your AVDs for audio glasses and display glasses, you can
[run your app on the AVDs using the emulator](/develop/xr/jetpack-xr-sdk/run/emulator/glasses).

---

OpenXR™ and the OpenXR logo are trademarks owned
by The Khronos Group Inc. and are registered as a trademark in China,
the European Union, Japan and the United Kingdom.

[Next

Run your app on the emulator

arrow\_forward](/develop/xr/jetpack-xr-sdk/run/emulator/glasses)