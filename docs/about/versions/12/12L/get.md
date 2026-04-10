---
title: https://developer.android.com/about/versions/12/12L/get
url: https://developer.android.com/about/versions/12/12L/get
source: md.txt
---

![](https://developer.android.com/static/images/about/versions/12/12L-foldable-emulator.png)

You can get the 12L feature drop in any of the following ways:

- [Download the 12L emulator image through Android Studio](https://developer.android.com/about/versions/12/12L/get#set-up-avd)
- [Get 12L on a partner device](https://developer.android.com/about/versions/12/12L/get#on_partner)
- [Get 12L on a Google Pixel device](https://developer.android.com/about/versions/12/12L/get#on_pixel)
- [Get a generic system image (GSI)](https://developer.android.com/about/versions/12/12L/get#on_gsi)

Complete instructions are below. Setup is fast and you can try your apps on a
variety of screen sizes.

For ideas on what to test, see [Get your apps
ready](https://developer.android.com/about/versions/12/12L/summary#get-apps-ready).

## Set up a 12L virtual device

To set up a 12L virtual device, follow these steps:

1. Install [Android Studio Chipmunk \| 2021.2.1 or higher](https://developer.android.com/studio).

2. In Android Studio, click **Tools \> SDK Manager**.

3. In the **SDK Tools** tab, select the latest version of **Android Emulator** ,
   and click **OK**. This action installs the latest version if it isn't
   already installed.

4. In Android Studio, click **Tools \> Device Manager** , then click **Create
   device** in the **Device Manager** panel.

   ![](https://developer.android.com/static/images/about/versions/12/12L-create-avd.png)
5. Select a device definition with a large screen, such as the **Pixel C** in
   the **Tablet** category or the **7.6" Fold-in with outer display** in the
   **Phone** category, then click **Next**.

6. Find the 12L system image, called **Android API 32** , and click **Download**
   to get it. After the download completes, select this system image and click
   **Next**.

   ![](https://developer.android.com/static/images/about/versions/12/12L-system-image.png)
7. Finalize other settings for your virtual device, then click **Finish**.

   ![](https://developer.android.com/static/images/about/versions/12/12L-device-configuration.png)
8. After returning to the list of virtual devices in the Device Manager, find
   your 12L virtual device and click **Launch**
   ![](https://developer.android.com/static/images/about/versions/12/12L-launch-avd-icon.png) to
   start it.

   ![](https://developer.android.com/static/images/about/versions/12/12L-launch-avd-full.png)

Repeat these steps to create a variety of large screen device definitions that
you can use to test your app in a variety of large screen scenarios.

### Resizable emulator

In addition to large screen virtual devices that you can configure for 12L, you
can try the resizable device configuration that's included in Android Studio
Chipmunk \| 2021.2.1 or higher. When you're using a resizable device definition
with a 12L system image, the Android Emulator lets you quickly toggle between
the four reference devices: phone, foldable, tablet, and desktop. When using the
foldable reference device, you can also toggle between folded and unfolded
states.

This flexibility makes it easier to both validate your layout at design time and
test the behavior at runtime, using the same reference devices. To create a new
resizable emulator, use the Device Manager in Android Studio to create a new
virtual device and select the **Resizable** device definition.
![](https://developer.android.com/static/images/about/versions/12/12L-resizable-emulator.gif) Use the new resizable device definition for the Android Emulator to test 12L with variety of large screen scenarios.

## Get 12L on a partner device

We've partnered with Lenovo to make 12L available for you to try on the Lenovo
P12 Pro.

You can learn how to install 12L on the Lenovo P12 Pro by visiting [Lenovo's
12L preview site](https://dev.lenovo.com/home/puahAndroid12).

Lenovo provides 12L updates on its own timeline and provides its own channel for
reporting issues found on their devices. We highly recommend using Lenovo's
feedback channels to report bugs and feedback that are specific to their
devices.


[Go to Lenovo's preview site](https://dev.lenovo.com/home/puahAndroid12)

## Get 12L on a Google Pixel device

If you have a supported Google Pixel device, you can [check and update your
Android version](https://support.google.com/pixelphone/answer/7680439) to
receive 12L over the air.

In most cases, you don't need to do a full reset of your data to move to 12L,
but it's recommended that you back up data before installing 12L on your device.

12L OTAs and downloads are available for the following Google Pixel
devices:

- Pixel 3a and 3a XL
- Pixel 4 and 4 XL
- Pixel 4a and 4a (5G)
- Pixel 5 and Pixel 5a
- Pixel 6 and 6 Pro

> [!NOTE]
> **Note:** Future Android 12 platform updates might not be available for some of these devices if the device's support window has passed.

### Flash or manually install a system image

Alternatively, if you'd rather flash your device, we recommend using the
[Android Flash Tool](https://flash.android.com/release/12.1.0).


[Flash 12L to a supported device](https://flash.android.com/release/12.1.0)

If you need to flash your device manually for some other reason, you can get the
12L system image for your device on the [Pixel downloads
page](https://developers.google.com/android/images). Read the general
instructions for how to [flash a system
image](https://developers.google.com/android/images#instructions) to your
device. This approach can be useful when you need more control over testing,
such as for automated testing or regression testing.

## Get a generic system image (GSI)

Android [Generic System Image (GSI)](https://developer.android.com/topic/generic-system-image) binaries
are available to developers for app testing and validation purposes on supported
Treble-compliant devices. You can use these images to address any compatibility
issues with 12L as well as discover and report OS and framework issues
before 12L is officially released.

See the [GSI documentation](https://developer.android.com/topic/generic-system-image) for device
requirements, flashing instructions, and information on choosing the right image
type for your device. Once you're ready to download a GSI binary, see the
[Android 12 GSI section](https://developer.android.com/topic/generic-system-image/releases#android-gsi-12) on
the GSI releases page.

## Next steps

After you have a device configured for 12L, here are some things to do next:

- [Learn more about what's in 12L](https://developer.android.com/about/versions/12/12L/summary)
- [Learn what to look for and test in your app](https://developer.android.com/about/versions/12/12L/summary#what-to-test)
- [Optimize your app for large screens](https://developer.android.com/large-screens)
- [Set up the 12L SDK](https://developer.android.com/about/versions/12/12L/setup-sdk)