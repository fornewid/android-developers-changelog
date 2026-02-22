---
title: https://developer.android.com/training/wearables/get-started/connect-phone
url: https://developer.android.com/training/wearables/get-started/connect-phone
source: md.txt
---

# Connect a watch to a phone

Wear OS apps should work independently of a phone. However, if your Wear OS app depends on a mobile app, see the following information about connecting either an emulated watch or a physical watch to a phone.

## Pair devices with a watch emulator

You can pair devices to your watch Android Virtual Device (AVD), or emulator, manually or with the Wear OS emulator pairing assistant.

### Use the Wear OS emulator pairing assistant

| **Note:** Your phone must run Android 11 (API level 30) or higher and have the Google Play Store installed to use the Wear OS emulator pairing assistant. To upgrade system images for your emulated devices, use the[SDK Manager](https://developer.android.com/studio/intro/update#sdk-manager).

The Wear OS emulator pairing assistant simplifies managing and connecting Wear emulators. You can pair multiple Wear devices with a single virtual or physical phone. Android Studio saves and re-pairs previously paired devices when you launch them.

To pair two devices, follow these steps:

1. If you haven't already,[create a Wear emulator](https://developer.android.com/training/wearables/get-started/creating#emulator).

2. In the**Device Manager** , click the overflow menu icon next to a device you want to pair and select**Pair Wearable**.

   ![Tap the overflow menu icon next to a device you want to pair and select Pair Wearable](https://developer.android.com/static/training/wearables/images/pair-wearable.png)**Figure 1**: Overflow menu of a device that can be paired with a Wear emulator.
3. This action launches the Wear OS emulator pairing assistant. If you selected**Pair Wearable** on the entry for a phone, you see a list of available Wear devices. If you started with a Wear device, you see a list of available phones. Select the device you want to pair and tap**Next**.

4. It might take a few minutes for Android Studio to launch and prepare the devices. If your phone doesn't have the Wear OS companion app installed, follow the prompts to sign in to the Play Store, install it, and set it up.

5. To pair your devices in the Wear OS app on your phone, tap the overflow menu and select**Pair with emulator**.

After your devices are successfully paired, the**Device Manager** shows small icons next to the paired devices. You can also tap the overflow drop-down menu and select**View Details**to see a list of paired devices.
![The Device Manager shows small icons next to the paired devices](https://developer.android.com/static/training/wearables/images/paired-devices.png)**Figure 2** : The**Paired Devices**tool window shows devices paired with the selected device.

### Pair a phone with the watch AVD

To add a Google Account to the watch AVD for development, pair a phone with the watch AVD and sync a Google Account. Then, follow these steps:

1. Follow the steps to[set up a phone](https://developer.android.com/training/wearables/get-started/connect-phone#setting-up-a-phone).

2. On the phone, enable**Developer Options** and**USB Debugging**.

3. Connect the phone to your computer through USB.

4. Forward the AVD's communication port to the connected phone each time the phone is connected with the following command:`adb -d forward tcp:5601
   tcp:5601`

5. In the Wear OS companion app on the phone, begin the standard pairing process. For example, on the**Welcome** screen, tap the**Set It Up** button. Alternatively, if an existing watch already is paired, tap**Add a New Watch**.

6. In the Wear OS companion app on the phone, tap the overflow menu, and then tap**Pair with Emulator**.

7. Tap the**Settings**icon.

8. Under**Device Settings** , tap**Emulator**.

9. Tap**Accounts**and select a Google Account. Follow the steps in the wizard to sync the account with the emulator. If necessary, type the screen-lock device password and Google Account password to start the account sync.

### Connect a phone to multiple Wear OS devices

To connect a second Wear device to a virtual or physical phone, follow the same steps you would for an initial pairing: locate the phone or Wear device you want to pair in the**Device Manager** , click the overflow menu icon, and click**Pair Wearable**.

## Set up a phone

This section describes how to set up a mobile phone with a Wear OS companion app.

### Use the Android version of the companion app

On an Android phone, go to the[Wear OS by Google Smartwatch](https://play.google.com/store/apps/details?id=com.google.android.wearable.app)app listing. Tap**Update** to download and install the app. After installation, confirm that**Auto-update** is selected for the app. See the "How to update individual Android apps automatically" section of[Update downloaded apps](https://support.google.com/googleplay/answer/113412). Tap**Open**to start the app.

#### Pair an Android phone to a watch

After you install the companion app on a phone, unpair any outdated watch pairings, if necessary. Then pair the phone to a newly imaged watch. To do this, complete the following steps:

1. On the phone, select your watch device name from the list of devices. A pairing code displays on the phone and on the watch. Check that the codes match.

2. Tap**Pair**to continue the pairing process. When the watch connects to the phone, a confirmation message displays. After confirming, a list of accounts will appear on the phone.

3. Choose a Google Account to add and sync to your watch.

4. Confirm the screen lock and enter the password to start copying the account from the phone to the watch.

5. Follow the instructions in the wizard to finish the pairing process.