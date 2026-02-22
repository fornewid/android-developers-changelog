---
title: https://developer.android.com/about/versions/13/get
url: https://developer.android.com/about/versions/13/get
source: md.txt
---

# Get Android 13

![](https://developer.android.com/static/images/lockups/android-stacked.svg)

You can get Android 13 in any of the following ways:

- [Get Android 13 on a Google Pixel device](https://developer.android.com/about/versions/13/get#on_pixel)
- [Set up the Android Emulator](https://developer.android.com/about/versions/13/get#on_emulator)
- [Get a generic system image (GSI)](https://developer.android.com/about/versions/13/get#on_gsi)
- [Get Android 13 Beta for Android TV](https://developer.android.com/about/versions/13/get#on_androidtv)

## Get Android 13 on a Google Pixel device

If you have a supported Google Pixel device, you can[check and update your Android version](https://support.google.com/pixelphone/answer/7680439)to receive Android 13 over the air.

In most cases, you don't need to do a full reset of your data to move to Android 13, but it's recommended that you back up data before installing Android 13 on your device.

Android 13 OTAs and downloads are available for the following Pixel devices:

- Pixel 4 and 4 XL
- Pixel 4a and 4a (5G)
- Pixel 5 and 5a
- Pixel 6 and 6 Pro
- Pixel 7 and 7 Pro
- Pixel Fold
- Pixel Tablet

### Flash or manually install a system image

Alternatively, if you'd rather flash your device, we recommend using the[Android Flash Tool](https://flash.android.com/release/13.0.0).

If you need to flash your device manually for some other reason, you can get the Android 13 system image for your device on the[Pixel downloads page](https://developers.google.com/android/images). Read the general instructions for how to[flash a system image](https://developers.google.com/android/images#instructions)to your device. This approach can be useful when you need more control over testing, such as for automated testing or regression testing.

## Set up the Android Emulator

Configuring the Android Emulator to run Android 13 is a great solution for exploring new features and APIs and testing Android 13 behavior changes. Setting up the emulator is fast and convenient and allows you to emulate various screen sizes and device characteristics.

Depending on the type of testing you need to do, consider setting up a variety of virtual devices from these device categories:

- [Phone](https://developer.android.com/about/versions/13/get#phone-avd)
- [Tablet or large-screen device](https://developer.android.com/about/versions/13/get#large-screen-avd)
- [TV](https://developer.android.com/training/tv/start/start#run-on-a-virtual-device)

### Set up a virtual device (phone)

To set up a virtual device to emulate a typical phone, follow these steps:

1. Install[Android Studio Chipmunk \| 2021.2.1 or higher](https://developer.android.com/studio).
2. In Android Studio, click**Tools \> SDK Manager**.
3. In the**SDK Tools** tab, select the latest version of**Android Emulator** , and click**OK**. This action installs the latest version if it isn't already installed.
4. In Android Studio, click**Tools \> AVD Manager**, and follow the instructions to create a new Android Virtual Device (AVD).

   Be sure to select a device definition for a[supported Pixel device](https://developer.android.com/about/versions/13/get#on_pixel)and a 64-bit Android 13 emulator system image. If you don't already have an Android 13 system image installed that matches your device definition, click**Download** next to the**Release Name**to get it.
5. Return to the list of virtual devices in the AVD Manager, and then double-click your Android 13 virtual device to launch it.

### Set up a virtual device (tablet or large-screen)

To set up a virtual device to emulate a tablet or other large-screen device, follow these steps:

1. Install[Android Studio Chipmunk \| 2021.2.1 or higher](https://developer.android.com/studio).

2. In Android Studio, click**Tools \> SDK Manager**.

3. In the**SDK Tools** tab, select the latest version of**Android Emulator** , and click**OK**. This action installs the latest version if it isn't already installed.

4. In Android Studio, click**Tools \> Device Manager** , then click**Create device** in the**Device Manager**panel.

   ![](https://developer.android.com/static/images/about/versions/13/13-create-avd.png)
5. Select a device definition with a large screen, such as the**Pixel C** in the**Tablet** category or the**7.6" Fold-in with outer display** in the**Phone** category, then click**Next**.

6. Find the Android 13 system image, called**Android API 33** , and click**Download** to get it. After the download completes, select this system image and click**Next**.

7. Finalize other settings for your virtual device, then click**Finish**.

8. After returning to the list of virtual devices in the Device Manager, find your Android 13 virtual device and click**Launch** ![](https://developer.android.com/static/images/about/versions/13/13-launch-avd-icon.png)to start it.

Repeat these steps to create large screen device definitions that you can use to test your app in a variety of large screen scenarios.

#### Resizable emulator

In addition to large screen virtual devices that you can configure for Android 13, you can try the resizable device configuration that's included in Android Studio Chipmunk \| 2021.2.1 or higher. When you're using a resizable device definition with a Android 13 system image, the Android Emulator lets you quickly toggle between the four reference devices: phone, foldable, tablet, and desktop. When using the foldable reference device, you can also toggle between folded and unfolded states.

This flexibility makes it easier to both validate your layout at design time and test the behavior at runtime, using the same reference devices. To create a new resizable emulator, use the Device Manager in Android Studio to create a new virtual device and select the**Resizable** device definition in the**Phone**category.
![](https://developer.android.com/static/images/about/versions/13/13-resizable-emulator.png)Use the new resizable device definition for the Android Emulator to test Android 13 in a variety of large screen scenarios.

## Get a generic system image (GSI)

Android[Generic System Image (GSI)](https://developer.android.com/topic/generic-system-image)binaries are available to developers for app testing and validation purposes on supported Treble-compliant devices. You can use these images to address any compatibility issues as well as discover and report OS and framework issues.

See the[GSI documentation](https://developer.android.com/topic/generic-system-image)for device requirements, flashing instructions, and information on choosing the right image type for your device. Once you're ready to download a GSI binary, see the[Downloads section](https://developer.android.com/topic/generic-system-image/releases#android-gsi-13)on the GSI binaries page.

## Get Android 13 Beta for Android TV

The Android 13 Beta for Android TV is provided through system images for the[ADT-3 Developer Kit](https://store.askey.com/adt-3.html)and the[Android Emulator for TV](https://developer.android.com/training/tv/start/start#run-on-a-virtual-device).

See[Android 13 Beta for TV](https://developer.android.com/tv/release/13/preview)to get started.

## More information

To learn about which changes might affect you, and to learn how to test these changes in your app, read the following topics:

- [Behavior changes that affect all apps](https://developer.android.com/about/versions/13/behavior-changes-all)
- [Behavior changes that affect only apps that target Android 13](https://developer.android.com/about/versions/13/behavior-changes-13)

To learn more about new APIs and features available in Android 13, read[Android 13 features](https://developer.android.com/about/versions/13/features).