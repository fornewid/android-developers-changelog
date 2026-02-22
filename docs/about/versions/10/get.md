---
title: https://developer.android.com/about/versions/10/get
url: https://developer.android.com/about/versions/10/get
source: md.txt
---

# Get Android 10

To get started with Android 10, you'll need a hardware device or emulator running Android 10 for testing and development.

You can get Android 10 in any of these ways:

1. Get an OTA update or system image for a[Google Pixel device](https://developer.android.com/about/versions/10/get#on_pixel)
2. Get an OTA update or system image for a[partner device](https://developer.android.com/about/versions/10/get#on_partner)
3. Get a GSI system image for a[qualified Treble-compliant device](https://developer.android.com/about/versions/10/get#on_gsi)
4. Set up an[Android Emulator](https://developer.android.com/about/versions/10/get#on_emulator)to run Android 10

## Google Pixel device

If you have a qualified Google Pixel device, you can[check \& update your Android version](https://support.google.com/pixelphone/answer/7680439)to receive Android 10 over the air.

Alternatively, if you'd rather flash your device manually, you can get the Android 10 system image for your device on the[Pixel downloads page](https://developers.google.com/android/images). Read the general instructions for how to[flash a system image](https://developers.google.com/android/images#instructions)to your device. This approach can be useful when you need more control over testing, such as for automated testing or regression testing.

In most cases, you don't need to do a full reset of your data to move to Android 10, but it's recommended that you back up data before enrolling your device.

Android 10 is available for the following Google Pixel devices:

- Pixel and Pixel XL
- Pixel 2 and 2 XL
- Pixel 3 and 3 XL
- Pixel 3a and 3a XL

## Partner device

You can use any device from our ecosystem of partners for development and testing on Android 10. It's important to make sure the device you use is certified to provide official support for Android 10.

For device availability and official support for Android 10, please check with your device manufacturer or a carrier store in your region. For support on your device, visit the device manufacturer's support site.

## Qualified Treble-compliant device

For broader testing on a variety of Treble-compliant devices, you can download and flash a Generic System Image (GSI) to your device. Visit the[GSI page](https://developer.android.com/topic/generic-system-image)for details on how to flash a GSI image to your device.

## Android Emulator

If you don't have access to a hardware device that can run Android 10, we recommend setting up an Android Emulator for development and testing. Configuring the Android Emulator to run Android 10 is a great solution for exploring new features and APIs and testing with Android 10 behavior changes.

Setting up the emulator is fast and convenient and allows you to emulate various screen sites and device characteristics. You can even emulate a foldable device (in Android Studio 3.5 and later).

To set up an emulator with Android 10, install the latest system image and create a new virtual device as follows:

1. In Android Studio, click**Tools \> SDK Manager**
2. In the**SDK Platforms** tab, select**Show Package Details**at the bottom of the window.
3. Below**Android 10.0 (29)** , select a system image such as**Google Play Intel x86 Atom System Image**.
4. In the**SDK Tools** tab, select the latest version of**Android Emulator**.
5. Click**OK**to begin the install.
6. After install is finished, select**Tools \> AVD Manager** and follow the instructions to[create a new AVD](https://developer.android.com/studio/run/managing-avds#createavd). Be sure to select a device definition that does*not* include Play Store, and select**29**for the system image.
7. When you return to the AVD Manager's list of virtual devices, double-click your new virtual device to launch it.