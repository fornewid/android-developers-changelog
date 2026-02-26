---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/run/debug-layout/augmented
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/run/debug-layout/augmented
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) AI Glasses [](https://developer.android.com/develop/xr/devices#ai-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

While you're building augmented experiences with Jetpack Compose Glimmer
components for AI glasses, you can inspect and debug your layout with the Layout
Inspector in Android Studio.
[![](https://developer.android.com/static/images/picto-icons/plus.svg) See also If you're new to using the Layout Inspector, learn how to do other common tasks in the layout debugging guide.](https://developer.android.com/studio/debug/layout-inspector)

## Turn off the embedded Layout Inspector

If you're running your app on [virtual AI glasses devices](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/ai-glasses) with the Android
XR Emulator, you need to turn off the embedded Layout Inspector:

1. Open your project in Android Studio, and then navigate to **Android Studio \>
   Settings \> Tools \> Layout Inspector**.

2. Deselect **Enable embedded Layout Inspector**, and then restart Android
   Studio.

   ![Android Studio settings page for the Layout Inspector
   tool.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/disable-embedded-layout-inspector.png)

## Open the Layout Inspector

1. In Android Studio, [run your app](https://developer.android.com/studio/run).
2. When you see a screen you want to inspect, select **Tools \> Layout
   Inspector** from the menu bar.

   The Layout Inspector opens, along with the **Layout Display** and the
   **Component Tree** panel.
3. From the **Running devices** drop-down menu, switch from the AI glasses AVD
   to the phone AVD that's acting as the host device.

   ![Layout Inspector view with the "Running devices" drop-down menu
   highlighted.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/augmented-layout-inspector-select-avd.png)
4. In the **Layout Display**, scroll past the UI layout for the phone AVD to
   find the UI layout for the AI glasses. Click elements here to inspect their
   attributes.

   ![Layout Inspector view showing the AI glasses UI in the Layout
   Display.](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/run/augmented-layout-inspector-glasses-ui.png)

## Inspect layout attributes

As you interact with your app, inspect a view in the AI glasses UI by clicking
it in the **Layout Display** or in the **Component Tree** . All of the layout
attributes for that view appear in the **Attributes** panel.