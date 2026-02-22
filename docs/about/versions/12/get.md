---
title: https://developer.android.com/about/versions/12/get
url: https://developer.android.com/about/versions/12/get
source: md.txt
---

# Get Android 12

![](https://developer.android.com/static/images/lockups/android-stacked.svg)

You can get Android 12 in any of these ways:

- [Get Android 12 on a Google Pixel device](https://developer.android.com/about/versions/12/get#on_pixel)
- [Set up an Android emulator](https://developer.android.com/about/versions/12/get#on_emulator)
- [Get a generic system image (GSI)](https://developer.android.com/about/versions/12/get#on_gsi)
- [Get Android 12 for Android TV](https://developer.android.com/about/versions/12/get#on_androidtv)

## Get Android 12 on a Google Pixel device

If you have a supported Google Pixel device, you can[check and update your Android version](https://support.google.com/pixelphone/answer/7680439)to receive Android 12 over the air.

In most cases, you don't need to do a full reset of your data to move to Android 12, but it's recommended that you back up data before installing Android 12 on your device.

Android 12 OTAs and downloads are available for the following Google Pixel devices:

- Pixel 3 and 3 XL
- Pixel 3a and 3a XL
- Pixel 4 and 4 XL
- Pixel 4a and 4a (5G)
- Pixel 5 and Pixel 5a
- Pixel 6 and 6 Pro

### Flash or manually install a system image

Alternatively, if you'd rather flash your device, we recommend using the[Android Flash Tool](https://flash.android.com/release/12.0.0).

If you need to flash your device manually for some other reason, you can get the Android 12 system image for your device on the[Pixel downloads page](https://developers.google.com/android/images). Read the general instructions for how to[flash a system image](https://developers.google.com/android/images#instructions)to your device. This approach can be useful when you need more control over testing, such as for automated testing or regression testing.

## Set up an Android emulator

Configuring an Android emulator to run Android 12 is a great solution for exploring new features and APIs and testing Android 12 behavior changes. Setting up an emulator is fast and convenient and lets you emulate various screen sizes and device characteristics.

You can set up an emulator from inside Android Studio by doing the following:

1. Install[Android Studio Arctic Fox \| 2020.3.1 or higher](https://developer.android.com/studio).

2. In Android Studio, click**Tools \> SDK Manager**.

3. In the**SDK Tools** tab, select the latest version of**Android Emulator** , and click**OK**. This action installs the latest version if it isn't already installed.

4. In Android Studio, click**Tools \> AVD Manager**, and follow the instructions to create a new Android Virtual Device (AVD).

   Be sure to select a device definition for a[supported Pixel device](https://developer.android.com/about/versions/12/get#on_pixel)and a 64-bit Android 13 emulator system image. Note that 32-bit Android emulator system images are not supported in Android 12. If you don't already have an Android 12 system image installed that matches your device definition, click**Download** next to the**Release Name**to get it.
5. Return to the list of virtual devices in the AVD Manager, and then double-click your Android 12 virtual device to launch it.

## Get a generic system image (GSI)

Android[Generic System Image (GSI)](https://developer.android.com/topic/generic-system-image)binaries are available to developers for app testing and validation purposes on supported Treble-compliant devices. You can use these images to address any compatibility issues with Android 12 as well as discover and report OS and framework issues.

See the[GSI documentation](https://developer.android.com/topic/generic-system-image)for device requirements, flashing instructions, and information on choosing the right image type for your device. Once you're ready to download a GSI binary, see the[Android 12 GSI section](https://developer.android.com/topic/generic-system-image/releases#android-gsi-12)on the GSI releases page.

## Get Android 12 for Android TV

Android 12 for Android TV is provided through system images for the[ADT-3 Developer Kit](https://store.askey.com/adt-3.html).

See[Android 12 for TV](https://developer.android.com/tv/release/12)to get started.

## More information

To learn about which changes might affect you, and to learn how to test these changes in your app, read the following topics:

- [Behavior changes that affect all apps](https://developer.android.com/about/versions/12/behavior-changes-all)
- [Behavior changes that only affect apps that target Android 12](https://developer.android.com/about/versions/12/behavior-changes-12)

To learn more about new APIs and features available in Android 12, read[Android 12 features](https://developer.android.com/about/versions/12/features).