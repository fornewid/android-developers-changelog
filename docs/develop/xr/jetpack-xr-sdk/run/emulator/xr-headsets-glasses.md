---
title: Run your app's immersive experiences on the emulator  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/run/emulator/xr-headsets-glasses
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Run your app's immersive experiences on the emulator Stay organized with collections Save and categorize content based on your preferences.



Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/xr-headsets-icon.svg)


XR Headsets

![](/static/images/develop/xr/xr-glasses-icon.svg)


Wired XR Glasses

[Learn about XR device types →](/develop/xr/devices)

As you test your app, use the Android XR Emulator to extend your testing
capacity beyond your physical test devices.
You can use the emulator controls to help you test how your app behaves in
common scenarios with AI glasses. See the following sections for details about
running your [virtual Android XR devices](/develop/xr/jetpack-xr-sdk/run/create-avds/xr-headsets-glasses) in the emulator and the emulator
controls you can use.

**Important:** Check that you're using the latest Canary build of Android Studio.
Other versions might not include Android XR tools. For more information, see
[Install and configure Android Studio for XR development](/develop/xr/jetpack-xr-sdk/get-studio).

[![](/static/images/picto-icons/plus.svg)

See also

If this your first time using an emulator with Android Studio, review the Android Emulator documentation.

arrow\_forward](https://developer.android.com/studio/run/emulator)

## Run your app on the emulator

1. To start the emulator, click **Run** for the AVD in the Device Manager.

   ![Android Studio device manager screen](/static/images/develop/xr/jetpack-xr-sdk/run/xr-device-avd-run.png)

   The emulator opens in the side panel.

   ![Android Studio emulator screen](/static/images/develop/xr/jetpack-xr-sdk/run/xr-headset-emulator-loaded.png)
2. To launch your app in the emulator, click **Run** in the Android
   Studio main toolbar.

   ![Android Studio run app configurtion](/static/images/develop/xr/jetpack-xr-sdk/run/xr-device-avd-run-app.png)

**Caution:** In rare cases for Windows users, using the Android XR Emulator with
either a XR headset or XR glasses AVD might result in system freezes or crashes
on some Windows configurations. Save all your data before running the emulator.
As a workaround, [enable WHPX](/studio/run/emulator-acceleration#vm-windows-whpx). See [release notes](/studio/preview/features) for more known issues.

## Use emulator controls for XR headsets and XR glasses

When the Android XR Emulator loads, look for the menu like the one shown in
figure 1. Use the controls in this menu to interact with the emulator.

![](/static/images/develop/xr/jetpack-xr-sdk/run/emulator-menu.png)


**Figure 1.** Use the controls in the emulator menu to interact with the emulator.

### Enable the mouse and keyboard

The emulator supports interaction through a mouse and keyboard. When you want to
interact with the system or an Android app in the emulator, select
the interaction controls option:

![Icon for the Android XR Emulator interaction option](/static/images/develop/xr/jetpack-xr-sdk/run/emulator-interaction-icon.png)

After selecting this, you can start interacting with elements within the virtual
space by moving the mouse over the emulator window.

### Look and move around in the virtual environment

The Android XR Emulator renders apps and their content in a virtual 3D
environment. Use the following controls to change the direction of your view:

|  |  |
| --- | --- |
| Android Studio rotate icon | **Rotate**: Drag the mouse to pivot your view in that direction. |
| Android Studio pan icon | **Pan**: Drag the mouse to move up, down, and side to side. This lets you view the emulator contents from different angles. |
| Android Studio dolly icon | **Dolly**: Drag the mouse to move closer or farther from the objects in view. |
| Android Studio reset icon | **Reset**: Click this button to return the emulator to the default view. |

You can also use the following keyboard shortcuts to move around in the virtual
environment. To use these while using mouse and keyboard input, hold the
`Option` key (macOS) or `Alt` key (Windows).

* `W`: (or up arrow key): Move forward in your current view.
* `A`: (or left arrow key): Side-step left.
* `S`: (or down arrow key): Move backward.
* `D`: (or right arrow key): Side-step right.
* `Q`: Move vertically downward.
* `E`: Move vertically upward.

### Enable passthrough mode

The menu at the top of the emulator includes the Toggle Passthrough option to
enable or disable a simulated passthrough environment.

![](/static/images/develop/xr/jetpack-xr-sdk/run/emulator-toggle-passthrough.png)


**Figure 2.** Toggle passthrough to see a simulated passthrough environment.

When enabled, passthrough mode displays a simulated indoor environment. Use
this mode to test apps in mixed reality.

![](/static/images/develop/xr/jetpack-xr-sdk/run/xr-headset-emulator-passthrough.png)


**Figure 3.** A simulated passthrough environment shows spatial UI elements anchored within a room.

### Other emulator controls

You can also use the following emulator controls:

|  |  |
| --- | --- |
| Android Studio power icon | **Power**: Simulates powering the device on or off. |
| Android Studio volume up icon Android Studio volume down icon | **Volume**: Simulates volume control. |
| Android Studio screenshot icon Android Studio screen record icon | **Screenshot**: Takes a screenshot or screen recording of the current state of the device. |
| Android Studio back icon Android Studio home icon Android Studio overview icon | **Android 3 button controls**: Simulates the Back, Home, and Overview buttons. |

[Previous

arrow\_back

Create virtual devices](/develop/xr/jetpack-xr-sdk/run/create-avds/xr-headsets-glasses)