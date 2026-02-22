---
title: https://developer.android.com/training/wearables/get-started/debugging
url: https://developer.android.com/training/wearables/get-started/debugging
source: md.txt
---

# Debug a Wear OS app

Debugging on Wear OS uses the same standard tools and processes as[debugging on other Android-powered form factors](https://developer.android.com/studio/debug).

This page contains instructions and links to help you debug your Wear OS apps.

## Debug targets

You can debug your Wear OS app using either the[Android Emulator](https://developer.android.com/studio/run/emulator)or a physical device.

### Android emulator

The[Android Emulator](https://developer.android.com/studio/run/emulator)lets you test your app on various virtual watch configurations directly from Android Studio.

1. **Set up an emulator:** If you haven't already, follow the steps to[configure an emulator](https://developer.android.com/training/wearables/get-started/creating#configure-emulator).
2. **Select the emulator:**In the Android Studio toolbar, choose the Wear OS virtual device you want to run your app on from the target device drop-down menu.
3. **Run your app:** Click**Run** ![Run icon](https://developer.android.com/static/studio/images/buttons/toolbar-run.png). Android Studio installs the app on the emulator and starts it.

For more details on emulator features specific to Wear OS, see[The Wear OS Emulator](https://developer.android.com/training/wearables/get-started/emulator).

### Physical watch

Debugging on a physical watch helps evaluate the real-world user experience and test hardware-specific features like sensors. You can connect to a physical watch using Wi-Fi or, on supported watches, a USB connection.

To connect a physical watch:

1. **Prepare the watch:** [Enable ADB debugging](https://developer.android.com/training/wearables/get-started/creating#prepare-watch-for-testing)in the watch's developer options.
2. **Connect:** Follow the detailed instructions for USB or Wi-Fi connections, including using`adb pair`and`adb connect`, in[Run apps on a hardware device](https://developer.android.com/studio/run/device). The setup procedure is similar to other Android devices.

| **Note:** Debugging over Bluetooth is no longer supported as of Wear OS 3.

## Additional debugging and setup

While most debugging tools work the same as on other Android devices, some aspects are specific to Wear OS.

### Install a specific OS version

If your testing requires a specific version of Wear OS, you can flash a software image directly onto watches that support a USB data connection. For example, you can flash a[factory image](https://developers.google.com/android/images-watch)or a[full OTA image](https://developers.google.com/android/ota-watch)onto a Google Pixel Watch.

### Test watch--phone connections

If your app's functionality spans both a watch and a phone, and you are testing on an emulated watch, you can use[Android Studio's Wear OS pairing assistant](https://developer.android.com/training/wearables/get-started/connect-phone)to pair your test device with a physical or virtual phone.

### Capture screenshots and videos

Capturing screenshots and videos using the Android Studio interface works the same for Wear OS as it does for[other devices](https://developer.android.com/training/wearables/get-started/screenshots). However, if you use`adb`from the command line, the process can differ, as you may need to specify particular codecs. For more information, see[Capture Wear OS screenshots](https://developer.android.com/training/wearables/get-started/screenshots).