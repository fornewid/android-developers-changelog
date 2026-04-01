---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/run/emulator/ai-glasses-troubleshoot
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/run/emulator/ai-glasses-troubleshoot
source: md.txt
---

Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) AI Glasses [](https://developer.android.com/develop/xr/devices#ai-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

You might encounter issues while [creating virtual AI glasses devices](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/ai-glasses) or
[running your app's augmented experiences on the emulator](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/emulator/ai-glasses). If you do
encounter issues, see the sections on this page for help resolving common
issues.

Some errors have multiple possible causes. This document lists some common
errors and their fixes, but you might encounter the same error message for a
different reason.

> [!NOTE]
> **Note:** If you don't see an issue listed here, you can also check the [release
> notes](https://developer.android.com/studio/releases/emulator) and [known issues](https://developer.android.com/studio/run/emulator-troubleshooting) for the standard Android Emulator to see if your issue is listed there. If you encounter a new issue, please see the [support
> page](https://developer.android.com/develop/xr/support#android-xr-emulator) to see how to report the issue to us.

## Can't pair emulators using Pairing Assistant

While [pairing the emulators using the Pairing Assistant](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/ai-glasses#pair-avds), the process fails.

### Cause

The Pairing Assistant can't find both emulators or is having another issue
while pairing.

### Fix

Follow these steps to manually pair the emulators on the phone AVD:

1. In the Android Studio **Device Manager** , find the [AI glasses AVD
   that you created](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/emulator/xr-headsets-glasses-troubleshoot) and click **Start**.

   ![Click](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/ai-glasses-avd-start.png)
2. Check that the AI Glasses AVD has fully launched. You'll see a "Pair phone
   to ..." message.

   ![The AI Glasses AVD has fully
   launched.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/ai-glasses-avd-ready-to-pair.png)
3. In the Android Studio **Device Manager** , find the [phone AVD
   that you created](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/emulator/ai-glasses) to act as a host device for the AI glasses emulator,
   and click **Start** .

   ![Click](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/phone-avd-start.png)
4. Check that the phone emulator has fully launched by waiting until you see
   the Home screen.

5. On the phone emulator, launch the Glasses app

   ![The app icon for the Glasses
   app.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/glasses-companion-app.png)
6. Select **Set up Glasses**.

   ![The app screen that shows the virtual devices are ready to
   pair.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/manual-pairing-set-up-glasses.png)
7. When prompted, select **Grant permissions** and accept the permissions
   request required by the Glasses Core app.


   <br />


   ![Grant the permissions required in the app.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/manual-pairing-missing-permissions.png)

   <br />

   ![Accept the permissions request from the app.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/manual-pairing-permissions-request.png)

   <br />

8. Select **Begin Pairing** on each app screen when prompted.


   <br />


   ![Select Begin Pairing on the first app screen.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/manual-pairing-begin-pairing.png)

   <br />

   ![Select Begin Pairing on the second app screen.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/manual-pairing-put-on-glasses.png)

   <br />

9. Select the AI glasses AVD from the list of devices.

   The emulators now attempt to pair the devices.

   ![Select the AI glasses AVD from the list that
   displays.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/manual-pairing-select-avd.png)
10. During pairing, accept the association requests for both the Glasses and Glasses Core apps.


    <br />


    ![The association request for the Glasses app.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/manual-pairing-companion-association.png)

    <br />

    ![The association request for the Glasses Core app.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/manual-pairing-core-association.png)

    <br />

11. Select **Next** to finish the pairing process.

> [!NOTE]
> **Note:** After you've completed pairing the first time, the emulators automatically reconnect the devices to each other whenever you launch them. If the emulators fail to reconnect the devices, follow the troubleshooting steps for when the [emulators don't reconnect the devices on relaunch](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/emulator/ai-glasses-troubleshoot#emulators-dont-reconnect).

## Emulator for AI glasses not pairing

While [pairing the emulators](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/ai-glasses#pair-avds), you encounter a message that says
"Disconnected" or "Couldn't pair glasses" and the emulators won't pair.


![](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/emulator-avd-disconnected.png) The "Disconnected" message indicates an issue with pairing.

<br />

![](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/companion-app-pairing-issue.webp) You might see this message in the Glasses app if there are issues while pairing.

<br />

<br />

### Cause

The glasses emulator isn't in pairing mode.

### Fix

1. Stop the AI glasses emulator.
2. In the Android Studio **Device Manager** , find the AI glasses AVD
   and click **Wipe Data** in the overflow menu.

   ![Click "Wipe Data" to start the AI glasses emulator while wiping user
   data.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/ai-glasses-avd-wipe-data.webp)

## Paired emulators don't reconnect devices on relaunch

After [initial pairing](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/ai-glasses#pair-avds), the emulators don't reconnect the devices to each
other when launched.

### Cause

A connectivity issue is stopping the devices from reconnecting.

### Fix

First, try the following method:

1. Stop the phone emulator and the AI glasses emulator.
2. In the Android Studio **Device Manager** , find the phone AVD
   and click **Cold Boot** in the overflow menu.

   ![Click "Cold Boot" to start the phone emulator with a cold
   boot.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/phone-avd-cold-boot.webp)
3. Wait for the phone emulator to fully boot, and then relaunch the AI glasses
   emulator.

If this method doesn't work, follow these steps:

1. Stop the AI glasses emulator.
2. In the Android Studio **Device Manager** , find the AI glasses AVD
   and click **Wipe Data** in the overflow menu.

   ![Click "Wipe Data" to start the AI glasses emulator while wiping user
   data.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/ai-glasses-avd-wipe-data.webp)
3. On the phone emulator, launch the system **Settings** app.

4. Select **Connected devices**.

5. Find the AI glasses device and select
   **Device details**.

6. Select **Forget \> Forget device**.

7. [Pair the devices](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/ai-glasses#pair-avds) again.

## AI glasses won't associate with phone

During [pairing](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/ai-glasses#pair-avds), the AI glasses won't associate with the phone.

### Cause

A connectivity issue is stopping the Glasses Core app from
detecting the AI glasses.

### Fix

First, try forgetting the Bluetooth device and re-pairing:

1. On the phone emulator, launch the system **Settings** app.
2. Select **Connected devices**.
3. Find the AI glasses device and select **Device details**.
4. Select **Forget \> Forget device**.
5. [Pair the devices](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/ai-glasses#pair-avds) again.

If this method doesn't work, follow these steps:

1. Stop the AI glasses emulator.
2. In the Android Studio **Device Manager** , find the AI glasses AVD
   and click **Wipe Data** in the overflow menu.

   ![Click "Wipe Data" to start the AI glasses emulator while wiping user
   data.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/ai-glasses-avd-wipe-data.webp)

## Projected activity won't launch on emulator

Your [projected activity](https://developer.android.com/develop/xr/jetpack-xr-sdk/ai-glasses/first-activity) won't launch on the AI glasses emulator.

### Cause

An issue is preventing the activity from being projected to the display.

### Fix

Follow the same troubleshooting steps as when the [emulators don't reconnect the
devices on relaunch](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/emulator/ai-glasses-troubleshoot#emulators-dont-reconnect).

## Can't use Gemini Live on the AI glasses emulator

While trying to use Gemini Live on the AI glasses emulator, you see the
following messages:


![A message that says the user isn't allowlisted for Gemini.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/ai-glasses-emulator-gemini-live-allowlist.png)

<br />

![A message that says something went wrong.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/ai-glasses-emulator-gemini-live-issue.png)

<br />

### Cause

The Google app needs to be updated to the latest version (minimum required
version is 16.46.63) on the phone emulator.

### Fix

1. In the Android Studio **Device Manager** , find the [phone AVD
   that you created](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/emulator/ai-glasses) to act as a host device for the AI glasses emulator,
   and click **Start** .

   ![Click](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/phone-avd-start.png)
2. Open the Google Play Store app.

3. Search for "Google" and select the Google app.

   ![Update the Google app from the Google Play Store app.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/ai-glasses-phone-avd-update-google-app.png)
4. Select **Update**.

## Can't install the public AI glasses emulators

You can't install the AI glasses emulators on the latest Android Studio Canary.

### Cause

You installed the AI glasses emulators before it was available as part of Android Studio Canary in the [Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html).

### Fix

Uninstall your previous AI glasses emulators and install the public version.

1. Open Android Studio.
2. Open the **SDK Manager**.
3. Check the **Show Package Details** checkbox. ![Check the **Show Package Details** checkbox](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/ai-glasses-uninstall-sdk-manager.png)
4. Clear **Android XR GlassesCore Phone** system image under any of the **Android 16.0** foldouts and click **Apply** to uninstall. ![Uninstall GlassesCore Phone system image](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/ai-glasses-uninstall-system-images.png)
5. Clear **Android XR Glasses SDK System Image** under any of the **Android 16.0** foldouts and click **Apply** to uninstall. ![Uninstall Glasses SDK system image](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/ai-glasses-uninstall-glasses-image.png)
6. Open the **Virtual Device Manager** and delete all **XR Glasses** and **XR GlassesCore Phone** devices. ![Delete VDM devices](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/ai-glasses-uninstall-device-manager.png)

After uninstalling the previous EAP AI glasses emulator, see our [documentation](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/ai-glasses)
to install the public AI glasses emulators in Android Studio Canary.

## See also

- [Create virtual AI glasses devices](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/ai-glasses)
- [Run your app's augmented experiences on the emulator](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/emulator/ai-glasses)