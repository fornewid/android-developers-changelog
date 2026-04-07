---
title: https://developer.android.com/tv/adt-2
url: https://developer.android.com/tv/adt-2
source: md.txt
---

# ADT-2 Developer Kit

The ADT-2 Developer Kit is a streaming media player device for running and
testing apps that are built for Android TV.

The information on this page explains how to set up and use the ADT-2 device.
However, the ADT-2 *is not required* for building and testing apps for Android
TV. The Android SDK includes all the software that you need to [build TV
apps](https://developer.android.com/training/tv/start/index.html) and [an
emulator](https://developer.android.com/training/tv/start/start.html#run-on-a-virtual-device)
that you can use to run your TV apps and test them. You can
also test TV apps on [any available Android TV device](https://developer.android.com/training/tv/start/start.html#run-on-a-real-device).

## Frequently asked questions

The following information explains how you can set up and use the ADT-2 device.

### Device setup

**How do I turn my device on?**

To turn your ADT-2 on:

1. Plug the power connector of the included Y-cable into the power port on the back of the device.
2. Plug the power supply into the power port of the Y-cable.
3. Plug the power supply into a power outlet.

   The device does not have an on and off switch.

| **Note:** If you only plug the ADT-2 into a USB port on a TV, the device might not receive enough power.

**What will happen when the ADT-2 boots for the first time?**

During the very first boot, the ADT-2 boot process takes longer than usual. This
behavior is expected and happens only once. While you perform the initial setup
for your account, the device also downloads the latest updates. The ADT-2 can
take a while to download these updates depending on your internet bandwidth.
After the download has completed, the device will reboot.

**When should I update my remote?**

You should update your remote whenever possible to ensure that you have the best
experience possible with the ADT-2. A notification displays on the main screen
whenever a update for your remote is available.

**How do I completely turn my device off?**

To turn off your ADT-2, unplug the power connector of the included Y-cable from
the power port on the back of the device. The device does not have an on and off
switch. You can also configure your ADT-2 to go to sleep (daydream) in
**Settings \> Device \> Display \> Daydream**.

**How do I connect the ADT-2 to my wireless network?**

The ADT-2 has a built-in Wi-Fi adapter for connecting to your network. You can
change the network that the device is connected to in **Settings \> Device \> Wi-
Fi**.

**How do I use the Y-cable?**

The included Y-cable has three connectors:

- A small, male power connector that plugs into the power port on the back of the ADT-2
- A standard, male USB-A connector that connects to your computer
- A small, female power port that the included power supply plugs into

| **Note:** If you only plug the ADT-2 into a USB port on a TV, the device might not receive enough power. Use the included Y-cable and power supply to plug the device into a power outlet to ensure that the device receives enough power.

**Can I connect to the ADT-2 without the Y-cable?**

Yes. The ADT-2 device is enabled for Android Debug Bridge (adb) connections over
TCP/IP, so you can also [connect to the ADT-2 device over Wi-
Fi](https://developer.android.com/studio/command-line/adb#wireless).

Once the device and computer are on the same network, run the following command
to connect to the device:  

    $ adb connect <ip-address-for-adt-2>

You can find the IP address for your devices in
**Settings \> Device Preferences \> About \> Status**.
| **Note:** Make sure you have enabled USB debugging in **Settings \> Preferences \>
| Developer options \> Debugging \> USB debugging**, so that you can use the Android Debug Bridge (adb) to connect with the ADT-2.

## Known issues

### Voice search is sometimes slow after initial setup

After you complete your initial account setup, voice search can be slow while
the ADT-2 updates Play Store apps in the background. Depending on your internet
bandwidth, this process usually completes within 30 minutes.

### Cannot pair remote when other devices are present

If you unpair your remote in the ADT-2 device settings, you can't pair your
remote again if you have other Bluetooth devices in discovery mode that are in
range of the ADT-2 dongle.