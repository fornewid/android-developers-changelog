---
title: https://developer.android.com/about/canary
url: https://developer.android.com/about/canary
source: md.txt
---

# Android Canary

![Android brand logo](https://developer.android.com/static/images/shared/android-logo-verticallockup_primary.png)The Canary channel lets you explore and test the most up-to-date Android builds with pre-release Android APIs and potential upcoming behavior changes. You should expect issues and breaking changes; these cutting-edge builds won't be the best choice to use as a primary or only device. As a result, you may get an early look at how your app could be impacted by changes, and be able to experiment with new capabilities to get your app ready for the future of Android.

You can get the Android Canary in the following ways:

- [Install on a Google Pixel device](https://developer.android.com/about/canary#on_pixel)
- [Configure the Android Emulator](https://developer.android.com/about/canary#on_emulator)

## Install on a Google Pixel device

To get the Android Canary on a Google Pixel device, use the[Android Flash Tool](https://flash.android.com/).

After you've flashed a Canary build to a supported Pixel device, your device is automatically enrolled in the Android Canary for Pixel channel, and will be offered continuous over-the-air (OTA) updates to the latest Canary builds.

### Exit the Canary channel on a Google Pixel device

In order to return to a beta or release channel, you'll have to wipe your device and flash a build from the appropriate channel using the Android Flash Tool or other means.

## Configure the Android Emulator

Configuring the Android Emulator to run Android Canary is a great solution for exploring new features and APIs and testing possible future behavior changes. Setting up the emulator is fast and convenient and lets you emulate various screen sizes and device characteristics.

### Set up a virtual device

To set up a virtual device to emulate a typical phone, follow these steps:

1. Install the latest[preview release](https://developer.android.com/studio/preview)of Android Studio.
2. In Android Studio, click**Tools \> SDK Manager**.
3. In the**SDK Tools** tab, select the latest version of**Android Emulator** , and click**OK**. This action installs the latest version if it isn't already installed.
4. In Android Studio, click**Tools \> Device Manager** , then click**Add a new device![plus](https://developer.android.com/static/studio/images/buttons/ic_plus_dark.png)\> Create Virtual Device** in the**Device Manager**panel.
5. Select a device definition, then click**Next**.
6. Find the Android Canary system image and click**Download** next to the**Release Name** to get it. After the download completes, select this system image and click**Next**.
7. Finalize other settings for your virtual device, then click**Finish**.
8. After returning to the list of virtual devices in the Device Manager, find your Android Canary virtual device and click**Start**.

Repeat these steps to create emulators with device definitions that you can use to test your app across a variety of form factors. Consider using a resizable emulator by selecting the**Resizable** device definition in the**Phone**category.