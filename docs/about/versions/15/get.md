---
title: https://developer.android.com/about/versions/15/get
url: https://developer.android.com/about/versions/15/get
source: md.txt
---

![](https://developer.android.com/static/images/lockups/android-stacked.svg)

You can get Android 15 in any of the following ways:

- [Get Android 15 on a Google Pixel device](https://developer.android.com/about/versions/15/get#on_pixel)
- [Set up the Android Emulator](https://developer.android.com/about/versions/15/get#on_emulator)
- [Get a generic system image (GSI)](https://developer.android.com/about/versions/15/get#on_gsi)

## Get Android 15 on a Google Pixel device

If you have a [supported Pixel device](https://developer.android.com/about/versions/15/get#google-pixel-devices), you can [check and update your
Android version](https://support.google.com/pixelphone/answer/7680439) to receive Android 15 over the air.

In most cases, you don't need to do a full reset of your data to move to Android
15, but it's recommended that you back up data before installing Android 15 on
your device.

### Supported Google Pixel devices

Android 15 OTAs and downloads are available for the following Pixel devices:

- Pixel 6 and 6 Pro
- Pixel 7 and 7 Pro
- Pixel 7a
- Pixel Fold
- Pixel Tablet
- Pixel 8 and 8 Pro
- Pixel 8a
- Pixel 9, 9 Pro, 9 Pro XL, and 9 Pro Fold

### Flash or manually install a system image

Alternatively, if you'd rather flash your device, we recommend using the
[Android Flash Tool](https://flash.android.com/release/15.0.0).

If you need to flash your device manually for some other reason, you can get the
Android 15 system image for your device on the [Pixel downloads page](https://developers.google.com/android/images). Read
the general instructions for how to [flash a system image](https://developers.google.com/android/images#instructions) to your device.
This approach can be useful when you need more control over testing, such as for
automated testing or regression testing.

## Set up the Android Emulator

Configuring the Android Emulator to run Android 15 is a great solution for
exploring new features and APIs and testing Android 15 behavior changes. Setting
up the emulator is fast and convenient and lets you emulate various screen sizes
and device characteristics.

Depending on the type of testing you need to do, consider setting up a variety
of virtual devices from these device categories:

- [Phone](https://developer.android.com/about/versions/15/get#phone-avd)
- [Tablet or large-screen device](https://developer.android.com/about/versions/15/get#large-screen-avd)

### Set up a virtual device (phone)

To set up a virtual device to emulate a typical phone, follow these steps:

1. Install [Android Studio Koala Feature Drop \| 2024.1.2 or higher](https://developer.android.com/studio).
2. In Android Studio, click **Tools \> SDK Manager**.
3. In the **SDK Tools** tab, select the latest version of **Android Emulator** , and click **OK**. This action installs the latest version if it isn't already installed.
4. In Android Studio, click **Tools \> Device Manager** , then click **Add a new
   device ![](https://developer.android.com/static/studio/images/buttons/ic_plus_dark.png) \> Create
   Virtual Device** in the **Device Manager** panel.

   ![Create an Android Virtual Device in Android
   Studio](https://developer.android.com/static/about/versions/15/images/15-create-avd.png)
5. Select a device definition for a [supported Pixel device](https://developer.android.com/about/versions/15/get#on_pixel) in the
   **Phone** Category tab, then click **Next**.

6. Find the Android 15 system image, called **VanillaIceCream** , and click
   **Download** ![](https://developer.android.com/static/about/versions/15/images/15-studio-download.png)
   next to the **Release Name** to get it. After the download completes, select
   this system image and click **Next**.

7. Finalize other settings for your virtual device, then click **Finish**.

8. After returning to the list of virtual devices in the Device Manager, find
   your Android 15 virtual device and click **Start**
   ![](https://developer.android.com/static/about/versions/15/images/15-launch-avd-icon.png).

### Set up a virtual device (tablet or large-screen)

To set up a virtual device to emulate a tablet or other large-screen device,
follow these steps:

1. Install [Android Studio Koala Feature Drop \| 2024.1.2 or higher](https://developer.android.com/studio).
2. In Android Studio, click **Tools \> SDK Manager**.
3. In the **SDK Tools** tab, select the latest version of **Android Emulator** , and click **OK**. This action installs the latest version if it isn't already installed.
4. In Android Studio, click **Tools \> Device Manager** , then click **Add a new
   device ![](https://developer.android.com/static/studio/images/buttons/ic_plus_dark.png) \> Create
   Virtual Device** in the **Device Manager** panel.

   ![Create an Android Virtual Device in Android
   Studio](https://developer.android.com/static/about/versions/15/images/15-create-avd.png)
5. Select a device definition with a large screen, such as the **Pixel Tablet**
   in the **Tablet** Category tab or the **Pixel Fold** in the **Phone**
   Category tab, then click **Next**.

6. Find the Android 15 system image, called **VanillaIceCream** , and click
   **Download** ![](https://developer.android.com/static/about/versions/15/images/15-studio-download.png)
   next to the **Release Name** to get it. After the download completes, select
   this system image and click **Next**.

7. Finalize other settings for your virtual device, then click **Finish**.

8. After returning to the list of virtual devices in the Device Manager, find
   your Android 15 virtual device and click **Start**
   ![](https://developer.android.com/static/about/versions/15/images/15-launch-avd-icon.png).

Repeat these steps to create large screen device definitions that you can use to
test your app in a variety of large screen scenarios.

#### Resizable emulator

In addition to large screen virtual devices that you can configure for Android
15, you can try the resizable device configuration. When you're using a
resizable device definition with an Android 15 system image, the Android
Emulator lets you quickly toggle between the three reference devices: phone,
foldable, and tablet. When using the foldable reference device, you can also
toggle between folded and unfolded states.

This flexibility makes it easier to both validate your layout at design time and
test the behavior at runtime, using the same reference devices. To create a new
resizable emulator, use the Device Manager in Android Studio to create a new
virtual device and select the **Resizable** device definition in the **Phone**
category.
![](https://developer.android.com/static/about/versions/15/images/15-resizable-emulator.png) Use the resizable device definition for the Android Emulator to test Android 15 in a variety of large screen scenarios.

## Get a generic system image (GSI)

Android [Generic System Image (GSI)](https://developer.android.com/topic/generic-system-image) binaries are available to developers
for app testing and validation purposes on supported Treble-compliant devices.
You can use these images to address any compatibility issues as well as discover
and report OS and framework issues.

See the [GSI documentation](https://developer.android.com/topic/generic-system-image) for device requirements, flashing instructions,
and information on choosing the right image type for your device. Once you're
ready to download a GSI binary, see the [Downloads section](https://developer.android.com/topic/generic-system-image/releases#android-gsi-15) on the GSI
binaries page.


## More information

To learn about which changes might affect you, and to learn how to test these
changes in your app, read the following topics:

- [Behavior changes that affect all apps](https://developer.android.com/about/versions/15/behavior-changes-all)
- [Behavior changes that affect only apps that target Android 15](https://developer.android.com/about/versions/15/behavior-changes-15)

To learn more about new APIs and features available in Android 15, read [Android
15 features](https://developer.android.com/about/versions/15/features).