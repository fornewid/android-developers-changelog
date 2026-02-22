---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/run/emulator/xr-headsets-glasses
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/run/emulator/xr-headsets-glasses
source: md.txt
---

<br />

<br />

Applicable XR devices  
This guidance helps you build experiences for these types of XR devices.  
[Learn about XR device types →](https://developer.android.com/develop/xr/devices)  
![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg)XR Headsets[](https://developer.android.com/develop/xr/devices#xr-headsets)  
![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg)Wired XR Glasses[](https://developer.android.com/develop/xr/devices#xr-glasses)  
[Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

As you test your app, use the Android XR Emulator to extend your testing capacity beyond your physical test devices. You can use the emulator controls to help you test how your app behaves in common scenarios with AI glasses. See the following sections for details about running your[virtual Android XR devices](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/xr-headsets-glasses)in the emulator and the emulator controls you can use.
**Important:** Check that you're using the latest Canary build of Android Studio. Other versions might not include Android XR tools. For more information, see[Install and configure Android Studio for XR development](https://developer.android.com/develop/xr/jetpack-xr-sdk/get-studio).  
[![](https://developer.android.com/static/images/picto-icons/plus.svg)
See also
If this your first time using an emulator with Android Studio, review the Android Emulator documentation.
arrow_forward](https://developer.android.com/studio/run/emulator)

## Run your app on the emulator

1. To start the emulator, click**Run**for the AVD in the Device Manager.

   ![Android Studio device manager screen](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/xr-device-avd-run.png)

   The emulator opens in the side panel.

   ![Android Studio emulator screen](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/xr-headset-emulator-loaded.png)
2. To launch your app in the emulator, click**Run**in the Android Studio main toolbar.

   ![Android Studio run app configurtion](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/xr-device-avd-run-app.png)

| **Caution:** In rare cases for Windows users, using the Android XR Emulator with either a XR headset or XR glasses AVD might result in system freezes or crashes on some Windows configurations. Save all your data before running the emulator. As a workaround,[enable WHPX](https://developer.android.com/studio/run/emulator-acceleration#vm-windows-whpx). See[release notes](https://developer.android.com/studio/preview/features)for more known issues.

## Use emulator controls for XR headsets and XR glasses

When the Android XR Emulator loads, look for the menu like the one shown in figure 1. Use the controls in this menu to interact with the emulator.
![](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/emulator-menu.png)**Figure 1.**Use the controls in the emulator menu to interact with the emulator.

### Enable the mouse and keyboard

The emulator supports interaction through a mouse and keyboard. When you want to interact with the system or an Android app in the emulator, select the interaction controls option:
![Icon for the Android XR Emulator interaction option](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/emulator-interaction-icon.png)

After selecting this, you can start interacting with elements within the virtual space by moving the mouse over the emulator window.

<br />

### Look and move around in the virtual environment

The Android XR Emulator renders apps and their content in a virtual 3D environment. Use the following controls to change the direction of your view:

|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| ![Android Studio rotate icon](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/studio-tools/rotate.png) | **Rotate**: Drag the mouse to pivot your view in that direction.                                                             |
| ![Android Studio pan icon](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/studio-tools/pan.png)       | **Pan** : Drag the mouse to move up, down, and side to side. This lets you view the emulator contents from different angles. |
| ![Android Studio dolly icon](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/studio-tools/dolly.png)   | **Dolly**: Drag the mouse to move closer or farther from the objects in view.                                                |
| ![Android Studio reset icon](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/studio-tools/reset.png)   | **Reset**: Click this button to return the emulator to the default view.                                                     |

You can also use the following keyboard shortcuts to move around in the virtual environment. To use these while using mouse and keyboard input, hold the`Option`key (macOS) or`Alt`key (Windows).

- `W`: (or up arrow key): Move forward in your current view.
- `A`: (or left arrow key): Side-step left.
- `S`: (or down arrow key): Move backward.
- `D`: (or right arrow key): Side-step right.
- `Q`: Move vertically downward.
- `E`: Move vertically upward.

### Enable passthrough mode

The menu at the top of the emulator includes the Toggle Passthrough option to enable or disable a simulated passthrough environment.
![](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/emulator-toggle-passthrough.png)**Figure 2.**Toggle passthrough to see a simulated passthrough environment.

When enabled, passthrough mode displays a simulated indoor environment. Use this mode to test apps in mixed reality.
![](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/xr-headset-emulator-passthrough.png)**Figure 3.**A simulated passthrough environment shows spatial UI elements anchored within a room.

### Other emulator controls

You can also use the following emulator controls:

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| ![Android Studio power icon](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/studio-tools/power.png)                                                                                                                                                      | **Power**: Simulates powering the device on or off.                                        |
| ![Android Studio volume up icon](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/studio-tools/volume-up.png)![Android Studio volume down icon](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/studio-tools/volume-down.png)        | **Volume**: Simulates volume control.                                                      |
| ![Android Studio screenshot icon](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/studio-tools/screen_shot.png)![Android Studio screen record icon](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/studio-tools/screen_record.png) | **Screenshot**: Takes a screenshot or screen recording of the current state of the device. |
| :back:![Android Studio home icon](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/studio-tools/home.png)![Android Studio overview icon](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/studio-tools/overview.png)                  | **Android 3 button controls**: Simulates the Back, Home, and Overview buttons.             |