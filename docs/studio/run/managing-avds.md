---
title: https://developer.android.com/studio/run/managing-avds
url: https://developer.android.com/studio/run/managing-avds
source: md.txt
---

An Android Virtual Device (AVD) is a configuration that defines the
characteristics of an Android phone, tablet, Wear OS, Android TV, or
Automotive OS device that you want to simulate in the
[Android Emulator](https://developer.android.com/studio/run/emulator).
The Device Manager is a tool you can launch from Android Studio that
helps you create and manage AVDs.

To open the new **Device Manager**, do one of the following:

- From the Android Studio Welcome screen, select **More Actions \> Virtual
  Device Manager**.

![Opening the Device Manager from the Welcome screen](https://developer.android.com/static/studio/images/run/device-manager-welcome-screen.png)

- After opening a project, select **View \> Tool Windows \> Device Manager** from the main menu bar, then click the **+** , and then click **Create
  Virtual Device**.

![New Device Manager window](https://developer.android.com/static/studio/images/run/tools-new-device-manager.png)

After creating your devices, you will be able to see a list of all the devices
on the device manager panel.

![Device Manager list](https://developer.android.com/static/studio/images/run/device-manager.png)

If you want to use virtual devices to run your automated instrumented
tests in a scalable and self-managed way, consider using [Gradle Managed
Devices](https://developer.android.com/studio/test/gradle-managed-devices).

## About AVDs

An AVD contains a hardware profile, system image, storage area, skin,
and other properties.

We recommend that you create an AVD for each system image that your app
could potentially support based on the
[`<uses-sdk>`](https://developer.android.com/guide/topics/manifest/uses-sdk-element) setting in your manifest.

### Hardware profile

<br />

The hardware profile defines the characteristics of a device as
shipped from the factory. The Device Manager comes pre-loaded with certain
hardware profiles, such as Pixel devices, and you can define or customize the
hardware profiles as needed.

<br />

![The Select Hardware dialog](https://developer.android.com/static/studio/images/run/select-hardware-window.png)

<br />

A device definition labeled with the Google Play logo in the
**Play Store** column includes both the Google Play Store app and
access to Google Play services, including a **Google Play** tab in the
**Extended controls** dialog that provides a convenient button for updating
Google Play services on the device.

<br />

<br />

Devices with this logo *and* a device type of "Phone" are also
[CTS](https://source.android.com/compatibility/cts/) compliant
and might use system images that include the Play Store app.

<br />

### System images

<br />

A system image labeled with **Google APIs** includes access to
[Google Play
services](https://developers.google.com/android/guides/overview).

<br />

![The System Image
dialog](https://developer.android.com/static/studio/images/run/system-image-device-configuration.png)

<br />

The **Recommended** tab lists recommended system images. The
other tabs include a more complete list. The right pane describes the
selected system image.

If you see a download icon next to a system image, that image isn't
currently installed on your development machine. Click the icon to download
the system image. You must be connected to the internet to download system
images.

<br />

<br />

The API level of the target device is important, because your app
doesn't run on a system image with an API level that's lower than the one
required by your app, as specified in the
[`minSdk`](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/BaseFlavor#minSdk()) attribute in the app manifest file. For more
information about the relationship between system API level and
`minSdk`, see [Version your app](https://developer.android.com/studio/publish/versioning).

<br />

<br />

If your app declares a
[`<uses-library>`](https://developer.android.com/guide/topics/manifest/uses-library-element) element in the manifest file, the app
requires a system image that includes that external library.
To run your app on an emulator, create an AVD that includes the required
library. To do so, you might need to use an add-on component for the AVD
platform; for example, the Google APIs add-on contains the Google Maps
library.

<br />

<br />

To ensure app security and a consistent experience with physical devices,
system images with the Google Play Store included are signed with a release
key, which means that you can't get elevated privileges (root) with these
images.

<br />

If you require elevated privileges (root) to aid with app troubleshooting, you
can use the Android Open Source Project (AOSP) system images that don't include
Google apps or services. Then you can use the `adb root` and `adb unroot`
commands to switch between normal and elevated privileges:

<br />

```
  % adb shell
  emu64a:/ $
  emu64a:/ $ exit
  % adb root
  restarting adbd as root
  % adb shell
  emu64a:/ #
  emu64a:/ # exit
  % adb unroot
  restarting adbd as non root
  % adb shell
  emu64a:/ $
  emu64a:/ $ exit
  %
  
```

<br />

| **Note:** When running with normal privilege level, the shell prompt ends with a `$` character, but when running with elevated (root) privileges, the shell prompt ends with a `#` character.

### Storage area

<br />

The AVD has a dedicated storage area on your development machine. It stores
the device user data, such as installed apps and settings, as well as
an emulated SD card. If needed, you can use the Device Manager to wipe user
data so the device has the same data as if it were new.

<br />

### Skin

<br />

An emulator skin specifies the appearance of a device. The Device Manager
provides some predefined skins. You can also define your own or use skins
provided by third parties.

<br />

### AVD and app features

<br />

Make sure your AVD definition includes the device features your app depends
on. See the sections about [hardware profile properties](https://developer.android.com/studio/run/managing-avds#hpproperties)
and [AVD properties](https://developer.android.com/studio/run/managing-avds#avdproperties) for lists of features you can
define in your AVDs.

<br />

## Create an AVD

<br />

To create a new AVD:

<br />

1. Open the Device Manager.
2. Click **Create Device** .

   The **Select Hardware** window appears.
   ![](https://developer.android.com/static/studio/images/run/select-hardware-window.png)

   Notice that only some hardware profiles include **Play
   Store** . These profiles are fully [CTS](https://source.android.com/compatibility/cts/) compliant and might
   use system images that include the Play Store app.
3. Select a hardware profile, then click **Next** .

   If you don't see the hardware profile you want, you can
   [create](https://developer.android.com/studio/run/managing-avds#createhp)
   or [import](https://developer.android.com/studio/run/managing-avds#importexporthp) a hardware profile, as described in
   other sections on this page.

   The **System Image** window appears.
   ![](https://developer.android.com/static/studio/images/run/system-image-device-configuration.png)
4. Select the system image for a particular API level, and then click **Next**.
5. The **Verify Configuration** window appears.
![](https://developer.android.com/static/studio/images/run/verify-configuration.png)
6. Change the [AVD properties](https://developer.android.com/studio/run/managing-avds#avdproperties) as needed, and then click **Finish** .

   Click **Show Advanced Settings** to show more
   settings, such as the skin.
7. The new AVD appears in the **Virtual** tab of the Device Manager and the target device menu.

To create an AVD starting with a copy:

1. From the **Virtual** tab of the Device Manager, click **Menu** ![](https://developer.android.com/static/images/tools/studio-advmgr-actions-overflow-icon.png) and select **Duplicate** .

   The [**Verify Configuration**](https://developer.android.com/studio/run/managing-avds#verifyconfigpage)
   window appears.
2. Click **Previous** if you need to make changes on the [System Image](https://developer.android.com/studio/run/managing-avds#systemimagepage) or [Select Hardware](https://developer.android.com/studio/run/managing-avds#selecthardwarepage) windows.
3. Make any changes you need, and then click **Finish** .

   The AVD appears in the **Virtual** tab of the Device Manager.

## Create a hardware profile

The Device Manager provides predefined hardware profiles for common devices
so you can easily add them to your AVD definitions. If
you need to define a different device, you can create a new hardware profile.

You can define a new hardware profile from the beginning
or copy a hardware profile as a starting point. The preloaded
hardware profiles aren't editable.

To create a new hardware profile from the beginning:

1. In the [Select Hardware](https://developer.android.com/studio/run/managing-avds#selecthardwarepage) window, click **New Hardware Profile**.
2. In the **Configure Hardware Profile** window, change the
   [hardware profile properties](https://developer.android.com/studio/run/managing-avds#hpproperties) as
   needed.

   ![The Configure hardware profile dialog](https://developer.android.com/static/studio/images/run/new-configure-hardware-profile.png)
3. Click **Finish** .

   Your new hardware profile appears in the **Select Hardware** window.
   You can [create an AVD](https://developer.android.com/studio/run/managing-avds#createavd)
   that uses the hardware profile
   by clicking **Next** or click **Cancel** to return
   to the **Virtual** tab or target device menu.

To create a hardware profile using a copy as a starting point:

<br />

1. In the **Select Hardware** window, select a hardware profile and click **Clone Device** or right-click a hardware profile and select **Clone** .

   <br />

2. In the **Configure Hardware Profile** window, change the [hardware profile properties](https://developer.android.com/studio/run/managing-avds#hpproperties) as needed.
3. Click **Finish**.
4. Your new hardware profile appears in the **Select Hardware** window. You can [create an AVD](https://developer.android.com/studio/run/managing-avds#createavd) that uses the hardware profile by clicking **Next** or click **Cancel** to return to the **Virtual** tab or target device menu.

<br />

## Edit existing AVDs

<br />

You can perform the following operations on an AVD from the Device Manager's
**Virtual** tab:

- To edit an AVD, click **Edit this AVD** ![](https://developer.android.com/static/studio/images/buttons/avd-edit.png) and make your changes.
- To delete an AVD, click **Menu** ![](https://developer.android.com/static/images/tools/studio-advmgr-actions-overflow-icon.png) and select **Delete**.
- To show the associated AVD INI and IMG files on disk, click **Menu** ![](https://developer.android.com/static/images/tools/studio-advmgr-actions-overflow-icon.png) and select **Show on Disk**.
- To view AVD configuration details that you can include in bug reports to the Android Studio team, click **Menu** ![](https://developer.android.com/static/images/tools/studio-advmgr-actions-overflow-icon.png) and select **View Details**.

<br />

## Edit existing hardware profiles

<br />

You can't edit or delete the preloaded hardware profiles, but
you can perform the following operations on other hardware profiles
from the **Select Hardware** window:

- To edit a hardware profile, select it and click **Edit Device** . You can also right-click a hardware profile and select **Edit**. Next, make your changes.
- To delete a hardware profile, right-click it and select **Delete**.

<br />

## Run and stop an emulator and clear data

<br />

From the **Virtual** tab, you can
perform the following operations on an emulator:

- To run an emulator that uses an AVD, click **Launch** ![](https://developer.android.com/static/images/tools/as-avd-start.png).
- To stop a running emulator, click **Menu** ![](https://developer.android.com/static/images/tools/studio-advmgr-actions-overflow-icon.png) and select **Stop**.
- To clear the data for an emulator, click **Menu** ![](https://developer.android.com/static/images/tools/studio-advmgr-actions-overflow-icon.png) and select **Wipe Data**.

<br />

## Import and export hardware profiles

From the **Select Hardware** window,
you can import and export hardware profiles as follows:

<br />

- To import a hardware profile, click **Import Hardware Profiles** and select the XML file on your computer containing the definition.
- To export a hardware profile, right-click it and select **Export**. Specify the location where you want to store the XML file containing the definition.

<br />

## AVD properties

The AVD configuration specifies the interaction between the development
computer and the emulator as well as properties you want to override in the
hardware profile. You can specify the following properties for AVD
configurations in the **Verify Configuration** window.
The properties labeled **(Advanced)** are only displayed if you
click **Show Advanced Settings**.

AVD configuration properties override hardware profile properties, and
emulator properties that you set while the emulator is running override them
both.

**Table 1.** AVD configuration properties

| AVD property | Description |
|---|---|
| AVD Name | Enter a name for the AVD. The name can contain uppercase or lowercase letters, numbers, periods, underscores, parentheses, dashes, and spaces. The name of the file storing the AVD configuration is derived from the AVD name. |
| AVD ID (Advanced) | View the AVD ID. The AVD ID is derived from the AVD name. You can use the ID to refer to the AVD from the command line. |
| Hardware Profile | Click **Change** to select a different hardware profile from the **Select Hardware** window. |
| System Image | Click **Change** to select a different system image from the **System Image** window. An active internet connection is required to download a new image. |
| Startup orientation | Select an option for the initial emulator orientation: - **Portrait:** oriented taller than wide - **Landscape:** oriented wider than tall An option is enabled only if it's supported in the hardware profile. When running the AVD in the emulator, you can change the orientation if both portrait and landscape are supported in the hardware profile. |
| Camera (Advanced) | Select an option for any enabled cameras. The Emulated and VirtualScene settings produce a software-generated image, while the Webcam setting uses your development computer's webcam to take a picture Camera options are available only if a camera is supported in the hardware profile. They are not available for Wear OS, Android TV, or Google TV. |
| Network: Speed (Advanced) | Select a network protocol to determine the speed of data transfer: - **GSM:** Global System for Mobile Communications - **HSCSD:** High-Speed Circuit-Switched Data - **GPRS:** Generic Packet Radio Service - **EDGE:** Enhanced Data rates for GSM Evolution - **UMTS:** Universal Mobile Telecommunications System - **HSDPA:** High-Speed Downlink Packet Access - **LTE:** Long-Term Evolution - **Full (default):** Transfer data as quickly as your computer allows. |
| Network: Latency (Advanced) | Select a network protocol to set how much time it takes for the protocol to transfer a data packet from one point to another point. |
| Emulated Performance: Graphics | Select how graphics are rendered in the emulator: - **Hardware:** use your computer graphics card for faster rendering. - **Software:** emulate the graphics in software, which is useful if you're having a problem with rendering in your graphics card. - **Automatic:** let the emulator decide the best option based on your graphics card. |
| Emulated Performance: Boot option (Advanced) | - Select how the AVD boots: - **Cold boot:** the device powers up each time from the device-off state. - **Quick boot:** the device loads the device state from a saved snapshot. |
| Emulated Performance: Multi-Core CPU (Advanced) | Select the number of processor cores on your computer that you want to use for the emulator. Using more processor cores speeds up the emulator. |
| Memory and Storage: RAM (Advanced) | Override the amount of RAM on the device set by the hardware manufacturer. Increasing the size uses more resources on your computer but supports faster emulator operation. Enter a RAM size and select the units, one of B (byte), KB (kilobyte), MB (megabyte), GB (gigabyte), or TB (terabyte). |
| Memory and Storage: VM Heap (Advanced) | Override the VM heap size set by the hardware manufacturer. Enter a heap size and select the units, one of B (byte), KB (kilobyte), MB (megabyte), GB (gigabyte), or TB (terabyte). |
| Memory and Storage: Internal Storage (Advanced) | Override the amount of non-removable memory space available on the device set by the hardware manufacturer. Enter a size and select the units, one of B (byte), KB (kilobyte), MB (megabyte), GB (gigabyte), or TB (terabyte). |
| Memory and Storage: SD Card (Advanced) | Specify the amount of removable memory space available to store data on the device. To use a virtual SD card managed by Android Studio, select **Studio-managed**, enter a size, and select the units, one of B (byte), KB (kilobyte), MB (megabyte), GB (gigabyte), or TB (terabyte). A minimum of 100 MB is recommended to use the camera. To manage the space in a file, select **External file** and click **...** to specify the file and location. For more information, see [mksdcard](https://developer.android.com/tools/help/mksdcard) and [AVD data directory](https://developer.android.com/studio/run/emulator-commandline#data-filedir). |
| Device Frame: Enable Device Frame | Select to enable a frame around the emulator window that mimics the look of a real device. |
| Custom Skin Definition (Advanced) | Select a skin that controls what the device looks like when displayed in the emulator. Specifying a screen size that's too big for the skin can mean that the screen is cut off, so you can't see the whole screen. See the [Create an emulator skin](https://developer.android.com/tools/devices/managing-avds#skins) section for more information. |
| Keyboard: Enable Keyboard Input (Advanced) | Select this option to use your hardware keyboard to interact with the emulator. This option is disabled for Wear OS and Android TV. |

## Hardware profile properties

You can specify the following properties for hardware profiles in the
**Configure Hardware Profile** window. AVD configuration properties
override hardware profile properties, and emulator properties that you set
while the emulator is running override them both.

The predefined hardware profiles included with the Device Manager aren't
editable. However, you can copy the profiles and edit the copies.

Some properties are disabled for some device types. For example, the "Round"
property is only available on Wear OS devices.

**Table 2.** Hardware profile
configuration properties

| Hardware profile property | Description |
|---|---|
| Device Name | Enter a name for the hardware profile. The name can contain uppercase or lowercase letters, numbers, periods, underscores, parentheses, and spaces. The name of the file storing the hardware profile is derived from the hardware profile name. |
| Device Type | Select one of the following: - Phone/Tablet - Wear OS - Android TV - Google TV - ChromeOS Device - Android Automotive |
| Screen: Screen Size | Specify the physical size of the screen in inches, measured on the diagonal. If the size is larger than your computer screen, it's reduced in size at launch. |
| Screen: Screen Resolution | Enter a width and height in pixels to specify the total number of pixels on the simulated screen. |
| Screen: Round | Select this option if the device has a round screen, such as some Wear OS devices. |
| Memory: RAM | Enter the RAM size of the device and select the units, one of B (byte), KB (kilobyte), MB (megabyte), GB (gigabyte), or TB (terabyte). |
| Input: Has Hardware Buttons (Back/Home/Menu) | Select this option if your device has hardware navigation buttons. Deselect it if these buttons are implemented in software only. If you select this option, the buttons don't appear on the screen. In either case, you can use the emulator side panel to simulate pressing the buttons. |
| Input: Has Hardware Keyboard | Select this option if your device has a hardware keyboard. Deselect it if it doesn't. If you select this option, a keyboard doesn't appear on the screen. In either case, you can use your computer keyboard to send keystrokes to the emulator. |
| Input: Navigation Style | Select one of the following: - **None:** no hardware controls. Navigation is through software. - **D-pad:** directional pad support. - **Trackball** - **Wheel** These options are for hardware controls on the device itself. However, the events sent to the device by an external controller are the same. |
| Supported device states | Select one or both options: - **Portrait:** oriented taller than wide - **Landscape:** oriented wider than tall You must select at least one option. If you select both options, you can switch between orientations in the emulator. |
| Cameras | To enable the camera, select one or both options: - **Back-Facing Camera:** the lens facing away from the user - **Front-Facing Camera:** the lens facing the user If the camera is enabled, you can use your development machine's webcam or a photo provided by the emulator to simulate taking a photo, based on the options you select in the AVD configuration. |
| Sensors: Accelerometer | Select this option if the device has hardware that helps it determine its orientation. |
| Sensors: Gyroscope | Select this option if the device has hardware that detects rotation or twist. In combination with an accelerometer, a gyroscope can provide smoother orientation detection and support a six-axis orientation system. |
| Sensors: GPS | Select this option if the device has hardware that supports the Global Positioning System (GPS) satellite-based navigation system. |
| Sensors: Proximity Sensor | Select this option if the device has hardware that detects when the device is close to the user's face during a phone call to disable input from the screen. |
| Default Skin | Select a skin that controls what the device looks like when displayed in the emulator. Specifying a screen size that's too big for the resolution can mean that the screen is cut off, so you can't see the whole screen. See the section that follows about [creating an emulator skin](https://developer.android.com/tools/devices/managing-avds#skins) for more information. |

## Create an emulator skin

An Android emulator skin is a collection of files that define the visual
and control elements of
an emulator display. If the skin definitions available in the AVD settings
don't meet your requirements,
you can create your own custom skin definition and then apply it to your AVD.

Each emulator skin contains:

<br />

- A `hardware.ini` file
- Layout files for supported orientations and physical configurations
- Image files for display elements, such as background, keys, and buttons

To create and use a custom skin:

1. Create a directory where you can save your skin configuration files.
2. Define the visual appearance of the skin in a text file named `layout`. This file defines many characteristics of the skin, such as the size and image assets for specific buttons. For example:

   <br />

   ```
   parts {
       device {
           display {
               width   320
               height  480
               x       0
               y       0
           }
       }

       portrait {
           background {
               image background_port.png
           }

           buttons {
               power {
                   image  button_vertical.png
                   x 1229
                   y 616
               }
           }
       }
       ...
   }
   ```

   <br />

3. Add bitmap files of the device images to the same directory.
4. Specify additional hardware-specific device configurations in an INI file for the device settings, such as `hw.keyboard` and `hw.lcd.density`.
5. Archive the files in the skin folder and select the archive file as a custom skin.

<br />

For more detailed information about creating emulator skins, see the
[Android Emulator Skin File Specification](https://android.googlesource.com/platform/external/qemu/+/emu-master-dev/android/docs/ANDROID-SKIN-FILES.TXT) in the tools source code.