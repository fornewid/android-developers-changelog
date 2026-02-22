---
title: https://developer.android.com/about/versions/11/get
url: https://developer.android.com/about/versions/11/get
source: md.txt
---

You can get Android 11 in any of these ways:

1. Get an OTA update or system image for a [Google Pixel device](https://developer.android.com/about/versions/11/get#on_pixel)
2. Set up an [Android Emulator](https://developer.android.com/about/versions/11/get#on_emulator) to run Android 11
3. Get a GSI system image for a [qualified Treble-compliant device](https://developer.android.com/about/versions/11/get#on_gsi)

For instructions on how to set up Android Studio for testing and development,
see [Set up the SDK](https://developer.android.com/about/versions/11/setup-sdk).

## Get Android 11 on your Pixel device

If you have a qualified Google Pixel device, you can
[check and update your Android version](https://support.google.com/pixelphone/answer/7680439)
to receive Android 11 over the air.

Alternatively, if you'd rather flash your device manually, you can get the
Android 11 system image for your device on the
[Pixel downloads page](https://developers.google.com/android/images).
Read the general instructions for how to [flash a system
image](https://developers.google.com/android/images#instructions) to your
device. This approach can be useful when you need more control
over testing, such as for automated testing or regression testing.

In most cases, you don't need to do a full reset of your data to move to
Android 11, but it's recommended that you back up data before enrolling
your device.

Android 11 OTAs and downloads are available for the following Google Pixel
devices:

- Pixel 2 and 2 XL
- Pixel 3 and 3 XL
- Pixel 3a and 3a XL
- Pixel 4 and 4 XL

## Set up Android Emulator to run Android 11

Configuring the Android Emulator to run Android 11 is a great solution for
exploring new features and APIs and testing with Android 11 behavior changes.
Setting up the emulator is fast and convenient and allows you to emulate various
screen sizes and device characteristics.

You can set up an emulator with Android 11 from inside Android
Studio:

1. [Install the latest Preview build](https://developer.android.com/about/versions/11/setup-sdk#get-studio) of Android Studio.
2. In Android Studio, click **Tools \> SDK Manager**.
3. In the **SDK Tools** tab, select the latest version of **Android Emulator** , and click **OK**. This installs the latest version if it's not already installed.
4. In Android Studio, click **Tools \> AVD Manager** and follow the instructions
   to [create a new AVD](https://developer.android.com/studio/run/managing-avds#createavd).

   Be sure to select a Pixel 2, 3, 3a, 4, or 4a device definition and an Android
   11 (API level 30) system image. If you don't already have an Android 11 system
   image installed that matches your device definition, click **Download** next
   to the **Release Name** to get it.
5. When you return to the list of virtual devices in the AVD Manager,
   double-click your new virtual device to launch it.

## Testing on Android GSI

Android [Generic System Image (GSI)](https://developer.android.com/topic/generic-system-image) binaries
are available to developers for app testing and validation purposes on supported
Treble-compliant devices. You can use these images to address any compatibility
issues with Android 11 as well as discover and report OS and
framework issues before Android 11 is officially released.

See the [GSI documentation](https://developer.android.com/topic/generic-system-image) for device
requirements, flashing instructions, and information on choosing the right image
type for your device. Once you're ready to download a GSI binary, see the
[Android 11 GSI section](https://developer.android.com/topic/generic-system-image/releases#android-gsi-11) on
the GSI releases page.