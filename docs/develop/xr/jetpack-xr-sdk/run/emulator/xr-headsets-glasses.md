---
title: Run your app's immersive experiences on the emulator  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/run/emulator/xr-headsets-glasses
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 4](https://android-developers.googleblog.com/2026/05/android-xr-sdk-developer-preview-4-updates.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

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
capacity beyond your physical test devices. You can use the emulator controls to
help you test how your app behaves in common scenarios with XR headsets and XR
glasses. See the following sections for details about running your [virtual
Android XR devices](/develop/xr/jetpack-xr-sdk/run/create-avds/xr-headsets-glasses) in the emulator and the emulator controls you can use.

**Important:** Check that you're
[using the latest Canary build of Android Studio](/studio/preview) and that you've [configured
Studio for XR development](/develop/xr/jetpack-xr-sdk/get-studio) with the latest versions of all the required
tools.

[![](/static/images/picto-icons/plus.svg)

See also

If this your first time using an emulator with Android Studio, review the Android Emulator documentation.

arrow\_forward](https://developer.android.com/studio/run/emulator)

## Run your app on the emulator

1. To start the emulator, click **Run** for the AVD in the Device Manager.

   ![Android Studio device manager screen](/static/images/develop/xr/jetpack-xr-sdk/run/xr-device-avd-run.png)

   The emulator opens in the side panel.

   ![Android Studio emulator screen](/static/images/develop/xr/jetpack-xr-sdk/run/xr-headset-emulator-loaded.png)
2. To launch your app in the emulator, click **Run** in the Android Studio main
   toolbar.

   ![Android Studio run app configurtion](/static/images/develop/xr/jetpack-xr-sdk/run/xr-device-avd-run-app.png)

**Caution:** In rare cases for Windows users, using the Android XR Emulator with
either an XR headset or XR glasses AVD might result in system freezes or crashes
on some Windows configurations. Save all your data before running the emulator.
As a workaround, [enable WHPX](/studio/run/emulator-acceleration#vm-windows-whpx). See [release notes](/studio/preview/features) for more known issues.

## Use emulator controls for XR headsets and XR glasses

When the Android XR Emulator loads, look for the menu like the one shown in
figure 1. Use the controls in this menu to interact with the emulator.

![](/static/images/develop/xr/jetpack-xr-sdk/run/emulator-menu.png)


**Figure 1.** Use the controls in the emulator menu to interact with the emulator.

### Interact with apps

The emulator supports multiple interaction modes. To interact with the system
or an Android app, select one of the following modes from the emulator controls:

![Modes for the Android XR Emulator interaction option](/static/images/develop/xr/jetpack-xr-sdk/run/xr-glasses-app-interaction-modes.png)


**Figure 2.** Select a mode to interact with app in the emulator.

* **Hand tracking**: hands automatically direct their raycasts toward your
  mouse pointer position. Drag to perform pinch interactions to select,
  hold, or manipulate a panel or 3D object.

  **Note:** The emulator currently supports single-handed (right hand only) pinch
  interactions. Left-hand controls and alternative gestures, such as grabbing
  and poking, aren't currently supported.
* **Eye tracking**: the emulator simulates the user's eye-gaze focus using
  your mouse pointer's position in 3D space. Moving your mouse shifts the
  gaze focus across UI elements. Click your mouse to select the focused UI
  element.
* **Connected mouse and keyboard**: move your mouse cursor over the emulator
  window to interact directly with elements within the virtual space.

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


**Figure 3.** Toggle passthrough to see a simulated passthrough environment.

When enabled, passthrough mode displays a simulated indoor environment. Use this
mode to test apps in mixed reality.

![](/static/images/develop/xr/jetpack-xr-sdk/run/xr-headset-emulator-passthrough.png)


**Figure 4.** A simulated passthrough environment shows spatial UI elements anchored within a room.

### Adjust the environment dimming levels on XR glasses

[XR Glasses](/design/ui/xr/guides/get-started#xr-glasses-wired) utilize additive displays on semi-transparent lenses and can
also include dimming technology. By darkening the physical background, these
lenses ensure that digital content remains crisp and legible, even in bright
physical environments.

Use the emulator's environment dimming controls to accurately preview immersive
content on XR glasses. To adjust the dimming levels, click the **Environment
Visibility** icon and use the environment dimming slider to pick a level between
fully transparent and maximum opacity.

![](/static/images/develop/xr/jetpack-xr-sdk/run/xr-glasses-environment-dimming.webp)


**Figure 5.** By adjusting the dimming levels, you can accurately preview how your digital content blends with or stands out against the physical world.

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