---
title: https://developer.android.com/develop/devices/chromeos/learn/development-environment
url: https://developer.android.com/develop/devices/chromeos/learn/development-environment
source: md.txt
---

Running Android apps on a Chromebook gives users access to the vast Android
ecosystem and gives Android developers the opportunity to reach ChromeOS users.

ChromeOS provides Android developers with the tools to deploy and test their
apps on Chromebooks. To improve users' experiences, verify your apps on
different form factors.

Whether you are deploying your Android app directly from ChromeOS (using Android
Studio on your Chromebook) or from another device, you can use [Android Debug
Bridge](https://developer.android.com/studio/command-line/adb) to deploy your app and debug different interactions with
Chromebooks.

## Enable ADB debugging

| **Note:** This feature is available on Chromebooks launched after 2020.

Previously, using ADB on a Chromebook was only possible in developer mode. Since
Chrome 81, developers can keep their devices out of developer mode and still
deploy apps they develop directly in ChromeOS. Here's how:

1. Go to **Settings** and [turn on Linux](https://developers.google.com/chromeos/app-development/develop), if you haven't
   already.

   ![Turning on Linux in ChromeOS settings.](https://developer.android.com/static/images/topic/arc/turnon_linux.gif) **Figure 1.** Turning on Linux in ChromeOS settings.
2. Once Linux is available, open the Linux settings.

3. Open the **Develop Android apps** option.

4. Toggle **Enable ADB debugging**. The Chromebook restarts.

   ![Enabling ADB debugging in Linux settings.](https://developer.android.com/static/images/topic/arc/debug_settings.gif) **Figure 2.** Enabling ADB debugging in Linux settings. **Note:** If the ADB toggle is not available after you enable Linux, or if it can't be toggled, you might have to factory-reset your device.
5. After the Chromebook restarts, a message lets you know that there might be
   applications that were not downloaded from the app store on the device.

   ![Notice about non-Play Store apps after enabling ADB.](https://developer.android.com/static/images/develop/chromeos/login_notice.jpg) **Figure 3.** Notice about non-Play Store apps after enabling ADB.
6. ADB is now available to deploy apps to your Chromebook, run debugging
   commands, and interact directly with the device.

To verify that your Android app works well on a variety of Chromebook devices
and available form factors, Google recommends that you test your app on the
following devices:

- An ARM-based Chromebook
- An x86-based Chromebook
- A device with a touchscreen and one without one
- A convertible device that changes between a laptop and a tablet
- A device with a stylus

## Deploy from ChromeOS

After enabling ADB debugging, you can load an Android app directly onto your
ChromeOS device using [Android Studio](https://developers.google.com/chromeos/app-development/develop/deploying-apps#deploy-with-android-studio). If you have an Android
Package Kit (APK), you can load it using the terminal.

### Deploy with Android Studio

After you have set up [Android Studio](https://developer.android.com/studio/install#chrome-os) and ADB, you can push your
apps to the Chromebook's Android container directly from Android Studio. The
Chromebook appears as an option in the device menu:
![Chromebook listed in Android Studio's device menu.](https://developer.android.com/static/images/develop/chromeos/as_devices.png) **Figure 4.** Chromebook listed in Android Studio's device menu.

When you push your app to a Chromebook, the ADB authorization
dialog appears. After you give authorization, your application launches in a new window.
![Authorizing ADB and running an app from Android Studio.](https://developer.android.com/static/images/develop/chromeos/run_app.gif) **Figure 5.** Authorizing ADB and running an app from Android Studio.

You can now deploy the app to the Chromebook and test and
debug it.

### Deploy with terminal

Follow these steps to deploy your app to a Chromebook using the terminal:

1. Install ADB if necessary, using the following command:

       sudo apt install adb

2. Connect to the device using the following command:

       adb connect arc

3. An authorization dialog for USB debugging appears. Grant the authorization:

   ![USB debugging authorization dialog.](https://developer.android.com/static/images/develop/chromeos/usb_dialog.png) **Figure 6.** USB debugging authorization dialog.
4. Install your app from the terminal using the following command:

       adb install [path to your APK]

![Connecting to a Chromebook and installing an APK via the terminal.](https://developer.android.com/static/images/develop/chromeos/adb_connect.gif) **Figure 7.** Connecting to a Chromebook and installing an APK via the terminal.

## Deploy from another device

If you can't use the preceding method and need to push your app from another
device, you can connect the device to ADB using a [USB](https://developers.google.com/chromeos/app-development/develop/deploying-apps#connect-to-adb-over-usb) connection
or a [network address](https://developers.google.com/chromeos/app-development/develop/deploying-apps#connect-to-adb-over-a-network).

### Connect to ADB over a network

Follow these steps to connect to ADB over a network:

1. Make sure you have [enabled ADB debugging](https://developer.android.com/develop/devices/chromeos/learn/development-environment#enable-adb-debugging).

2. Get the IP address of your Chromebook using the following steps:

   - Click the clock in the bottom-right area of the screen.
   - Click the gear icon.
   - Click the network type you are connected to, such as Wi-Fi or mobile data, then the name of the network.
   - Take note of the IP address.

| **Tip:** Another quick way to find your Chromebook's IP address is to click the clock in the bottom right, then click the Wi-Fi icon, and finally click the Network info button.

Connect to your Chromebook:

1. Return to your development machine and use ADB to connect to your Chromebook
   using its IP address:

       adb connect <ip_address>

2. On your Chromebook, click **Allow** when prompted to allow the
   debugger. Your ADB session is established.

#### Troubleshoot ADB debugging over a network

| **Note:** If your network prohibits these kinds of connections, you can set up your own router or hotspot or you can try Ethernet using a port or dongle.

Sometimes the ADB device shows that it's offline when everything is connected
properly. In this case, complete the following steps to troubleshoot the issue:

1. Deactivate **ADB debugging** in *Developer options*.
2. In a terminal window, run `adb kill-server`.
3. Re-activate the **ADB debugging** option.
4. In a terminal window, attempt to run `adb connect`.
5. Click **Allow** when prompted to allow debugging. Your ADB session establishes.