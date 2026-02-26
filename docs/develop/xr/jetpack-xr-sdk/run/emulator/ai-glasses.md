---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/run/emulator/ai-glasses
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/run/emulator/ai-glasses
source: md.txt
---

Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) AI Glasses [](https://developer.android.com/develop/xr/devices#ai-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

As you test your app, use the Android XR Emulator to extend your testing
capacity beyond your physical test devices. You can use the emulator controls to
help you test how your app behaves in common scenarios with AI glasses. See the
following sections for details about running your
[virtual Android XR devices](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/ai-glasses) in the emulator and the emulator controls you
can use.

> [!IMPORTANT]
> **Important:** Check that you're using the latest Canary build of Android Studio. Other versions might not include Android XR tools. For more information, see [Install and configure Android Studio for XR development](https://developer.android.com/develop/xr/jetpack-xr-sdk/get-studio).

[![](https://developer.android.com/static/images/picto-icons/plus.svg) See also If this your first time using an emulator with Android Studio, review the Android Emulator documentation.](https://developer.android.com/studio/run/emulator)

## Run your app on the emulator

To run your app on the emulator, follow these steps:

1. In the Android Studio **Device Manger** , find the [phone AVD
   that you created](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/ai-glasses#phone-avd-host-device) to act as a host device for the AI glasses emulator,
   and click **Start** .

   ![Click](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/phone-avd-start.png)
2. In the Android Studio **Device Manger** , find the [AI glasses AVD
   that you created](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/ai-glasses#create-avd) and click **Start**.

   ![Click](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/ai-glasses-avd-start.png)
3. To launch your app in the emulator, select **the phone AVD** from the
   target device drop-down menu in the Android Studio main toolbar,
   and then click **Run**.

   ![Android Studio run app configuration](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/phone-avd-run-app.png)

## Use emulator controls for AI glasses

Use the emulator controls to help you test how your app behaves in common
scenarios with AI glasses. See the following sections for details on each of the
controls you can use.

### Provide touchpad input

Because AI Glasses don't have a touchscreen, interactions use a touchpad on the
physical device. For the Android XR Emulator, you can find the touchpad just
below the display area.

Use your computer's mouse within the touchpad area to simulate touch, and enable
**Two Finger** mode to perform two-finger gestures.

The right side of the emulator touchpad area represents the area on a real
device that is towards the front of the glasses (where the lenses are), while
the left side represents the area on a real device that is towards the back of
the glasses (where the glasses rest on your ears). Knowing this orientation is
important when simulating gestures such as swiping forward or backward.
![](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/emulator-ai-glasses-touchpad.png) **Figure 1.** The touchpad area on the Android XR Emulator is just below the display area.

### Provide voice input

To toggle the microphone, select **Microphone** from the emulator controls. This
connects and sends input to the emulator using the default microphone input
device from your computer. This has the same effect as using the **Virtual
microphone uses host audio input** option in the [emulator extended
controls](https://developer.android.com/studio/run/emulator-extended-controls#microphone).

While the microphone is on, speak to use hotwords and issue commands.
![](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/emulator-ai-glasses-microphone.png) **Figure 2.** Enable the microphone to use your computer's microphone to provide voice input.

### Simulate displayless AI glasses

While you test your app for AI glasses, you'll need to simulate a pair of
displayless AI glasses so that your app can [support different types of AI
glasses](https://developer.android.com/develop/xr/jetpack-xr-sdk/ai-glasses/support-different-types).

To help you test for these use cases, the Glasses app lets you
enable *Audio-only mode*:

1. In the phone emulator, open the Glasses app.

   ![The app icon for the Glasses
   app.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/glasses-companion-app.png)
2. Tap **Device Settings** , and then toggle **Audio-only mode**.

   ![Toggle Audio-only mode through the Glasses
   .](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/companion-app-audio-only-mode.png)
3. Stop the phone emulator and the AI glasses emulator.

4. In the Android Studio **Device Manger** , find the phone AVD
   and click **Cold Boot** in the overflow menu.

   ![Click "Cold Boot" to start the phone emulator with a cold
   boot.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/phone-avd-cold-boot.webp)

   > [!IMPORTANT]
   > **Important:** You must close and relaunch the phone emulator **with a cold
   > boot** each time you toggle Audio-only mode on or off.

5. Follow the other steps to [relaunch the AI glasses emulator and run your
   app](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/emulator/ai-glasses#run-app-emulator).

### Disable the display snooze timeout

Display timeout behavior is an important consideration when developing your
app's experiences for AI glasses. For this reason, we recommend leaving the
default behavior while performing your usual app testing. However, for cases
where the display timeout interferes with your testing, you can disable the
default behavior using the following ADB command:

    adb shell dumpsys activity service com.google.android.glasses.core/com.google.android.projection.core.app.service.AndroidProjectionCoreService preferences_set pref_automatic_snooze_timeout false

To restore the default display timeout behavior, run the following ADB command:

    adb shell dumpsys activity service com.google.android.glasses.core/com.google.android.projection.core.app.service.AndroidProjectionCoreService preferences_set pref_automatic_snooze_timeout true

### Use Gemini Live

Follow these steps to trigger Gemini Live in the AI glasses emulator:

1. Before you try and use Gemini Live, update the Google app to the latest
   version (minimum required version is 16.46.63) on the phone emulator:

   1. On the phone emulator, open the Google Play Store app.
   2. Search for "Google" and select the Google app.

      ![Update the Google app from the Google Play Store
      app.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/ai-glasses-phone-avd-update-google-app.png)
   3. Select **Update**.

2. Trigger Gemini Live from the AI glasses emulator, by touching \& holding the
   touchpad for about 2 seconds.

   The first time, this will trigger a set of permission requests on your phone
   emulator. Grant all the required permissions, and then touch \& hold the
   touchpad on the glasses emulator for about 2 seconds again.

   ![Accept all the required permissions to use Gemini Live on the AI glasses
   emulator.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/ai-glasses-gemini-live-permission-request.png)

   When Gemini live is active and listening, you'll see this on the AI glasses
   emulator:

   ![A visual indicator shows on the display when Gemini Live is
   active.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/ai-glasses-gemini-live-active.png)
3. Check that the host microphone input is active on the AI glasses emulator by
   looking at the phone emulator. You should see a notification like the
   following one:

   ![A notification on the phone emulator indicates that the host microphone
   input is
   active.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/ai-glasses-check-host-microphone.png)

> [!NOTE]
> **Note:** If you encounter issues while using Gemini Live, see the [troubleshooting
> steps](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/emulator/ai-glasses-troubleshoot#issues-gemini-live).

### Capture photos or videos

Camera capture features in the Android XR Emulator aren't available yet.