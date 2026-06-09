---
title: https://developer.android.com/tv/adt-1
url: https://developer.android.com/tv/adt-1
source: md.txt
---

# ADT-1 Developer Kit

The ADT-1 Developer Kit is a streaming media player and game controller designed for running and testing apps built for Android TV.

The ADT-1 kit*is not required* for building and testing apps for Android TV. The Android SDK includes all the software needed to build TV apps and an emulator for running and testing them. For more information, see the[Get Started](https://developer.android.com/training/tv/start)guide for TV apps. You can also test TV apps on any available Android TV device.

**Note: The ADT-1 kit is no longer available**.

## ADT-1 Frequently Asked Questions

The following information is provided to help set up and use the ADT-1 device.

### Device Setup

**How do I turn my device on?**

Plug the included power cable into the back of ADT-1. The device does not have an on/off switch.

**How do I completely turn my device off?**

Unplug the included power cable from the back of ADT-1. The device does not have an on/off switch. However, ADT-1 will begin sleeping (daydream) based on user settings in**Settings \> Device \> Display \> Daydream**.

**How do I connect to the network?**

ADT-1 has both wireless and Ethernet for connecting to your network. To change your wireless network, go to**Settings \> Device \> Wi-Fi**. To use an Ethernet network connection, simply plug an Ethernet cable (that is connected to your network) into the port on the back of ADT-1.

**How do I use the developer cable?**

The developer cable has three connectors: a small, male power connector that plugs into the power port on the back of ADT-1, a standard male USB-A connector that connects your PC, and a small, female power connector that the included power supply plugs into.

**Note:** Make sure you have enabled USB debugging in**Settings \> Preferences \> Developer options \> Debugging \> USB debugging**, so that you can use the Android Debug Bridge (adb) to connect with the ADT-1 device.

**Can I connect without a developer cable?**

Yes. The ADT-1 device is enabled for Android Debug Bridge (adb) connections over TCP/IP. To connect to the ADT-1 device using this method:

1. Make sure that your development computer and the ADT-1 device are on the same network.
2. Determine the IP address of the ADT-1 device by navigating to**Settings \> Device \> Wi-Fi \> your-network-name \> Status info**.
3. Connect to the ADT-1 device using the following adb command:  

   ```
   $ adb connect <ip-address-for-adt-1>:4321
   ```

**Note:** Make sure you have enabled USB debugging in**Settings \> Preferences \> Developer options \> Debugging \> USB debugging**, so that you can use the Android Debug Bridge (adb) to connect with the ADT-1 device.

### User Input

**How do I put the gamepad that came with my ADT-1 into pairing mode?**

Press and hold the Back and Home buttons together for about three seconds, until all four blue LEDs flash together. When the LEDs are flashing, the gamepad is in pairing mode.

**How do I use the gamepad with the on-screen keyboard?**

Use the D-pad or left joystick to move the cursor, and press A to select. Press X to delete a character, and press Y to insert a space. Also, you can press the right joystick to toggle caps lock, and press the left joystick to show additional symbols.

**Can I control ADT-1 with my phone or tablet?**

Yes. In order to control the ADT-1 with Android phones or tablets, you can download a remote control app from the Google Play Store. For more information, see[Android TV Remote Control App](https://developer.android.com/tv/adt-1#emote).

**Can I connect a USB keyboard or mouse to ADT-1?**

Yes, you can connect a USB keyboard or mouse to the USB port on the back of ADT-1.

**Note:**The ADT-1 device is not compatible with all manufacturers and models of these devices. If a particular keyboard or mouse does not work, try a different model.

**How do I connect a Bluetooth device without an input device already attached?**

You can put ADT-1 into Bluetooth pairing mode using a hardware button. Press the small, round button on the back of ADT-1 to make it search for Bluetooth devices in pairing mode. If multiple accessories are found, press the small, round button to select the device you want to pair. Pairing will happen automatically after a few seconds.

**How do I connect additional Bluetooth accessories?**

<br />

To pair Bluetooth devices to ADT-1 from the user interface, go to**Settings \> Remote \& Accessories \> Add accessory**

### Google Cast

**Can I cast to an ADT-1 device?**

<br />

Yes. The ADT-1 includes Google Cast receiver functionality, similar to Chromecast. Since the ADT-1 is a developer device running a development software release, the Google Cast receiver is open only to a limited number of apps.

**Which Cast apps are supported on ADT-1?**

<br />

As a developer device, the ADT-1 supports casting from only the following apps/websites:

- YouTube
- Netflix
- Google Play Movies and TV (Android and iOS only)
- Google Play Music
- Mirror your Android device screen to ADT-1

Coming soon:

- Google Play Movies and TV (Chrome)

**Note:**When casting from a Chrome browser, you must use Chrome V.36 or higher. Chrome V.36 is available in beta-channel and is planned to be released soon.

**How do I cast to ADT-1?**

<br />

You cast to an ADT-1 device the same way you do with a Chromecast device. Open the supported Cast apps or webpages, press the**Cast** button and you should see the ADT-1 as a Cast target. For more information about on how to cast, see[Learn How to Cast](http://www.google.com/intl/en/chrome/devices/chromecast/learn.html).

**Will my Google Cast sender apps work on ADT-1 just like Chromecast?**

<br />

Yes. Your Cast app works on ADT-1 and Android TV products without additional work.

<br />

**Note:**Your iOS sender app requires the Google Cast iOS API version 2.2.1 or later to work with the ADT-1 device.

**How do I register my ADT-1 in order to run my apps?**

1. Go to**Settings \> Device \> Google Cast**and turn on developer support, allowing the ADT-1 device to send its serial number to Google.
2. Register your ADT-1 device in the Google Cast Developer Console, using the 12 character serial number engraved on the back of the ADT-1.

For more Google Cast developer information, see the[Cast developer site](https://developers.google.com/cast/). Please use the Google Cast SDK[issue tracker](https://code.google.com/p/google-cast-sdk/issues/list)for filing issues related to Cast. Make sure you mention the ADT-1 device when filing an issue.

**How do I debug my Cast app on ADT-1?**

Connect your development platform using the power/USB cable, and using a Chrome browser, navigate to`chrome://inspect/#devices`to debug the webview.

### Troubleshooting

**Why doesn't the on-screen keyboard come up?**

Enable the keyboard in the device Settings. Go to**Settings \> Preferences \> Keyboard \> Current keyboard** and choose**Leanback keyboard**.

**How do I perform a hardware reboot?**

Locked it up, huh? No worries. We've done that a few times ourselves. Unplug and replug the included power cable from the back of ADT-1 to reboot it.

**How do I perform a factory reset?**

**Warning:**This procedure removes all data from the device, including system data, downloaded apps, app data, and account settings.

From the home screen, go to**Settings \> Device \> Storage \& Reset** , and select**Factory data reset**.

**How do I perform a hardware reset?**

**Warning:**This procedure performs a factory data reset, removing all data from the device, including system data, downloaded apps, app data, and account settings.

Unplug the power cable from the back of ADT-1. Press and hold the small, round button on the back of ADT-1 as you re-insert the power cable, and continue to hold the small round button. The LED will begin flashing red for a few seconds, then change to multi-color cycle. When the LED starts the multi-color cycle, release the small, round button, and ADT-1 boots up. If you release the button while the LED is flashing red, the device will be in Fastboot mode.

## Android TV Remote Control App

![Android TV Remote Screenshots](https://developer.android.com/static/tv/images/android-tv-remote.png)

A remote control app is available for Android phones and tablets that allows you to interact with the ADT-1 device. This app allows you to switch between D-pad input mode or touchpad mode to navigate content and play games on a Android TV device. You can also tap the mic button to start a voice search, or use the keyboard to input text using this app.

You download the remote control app from the Google Play Store using[this link](https://play.google.com/store/apps/details?id=com.google.android.tv.remote).

**Note:**your Android phone or tablet must be connected to the same local network as ADT-1.

## Regulatory Disclosures and Safety Information

The ADT-1 device comes with important regulatory disclosures and safety information. Please read this information before using the device:

- [Regulatory Disclosures](https://developer.android.com/tv/adt-1/regulatory)
- [Important Safety Information](https://developer.android.com/tv/adt-1/safety)