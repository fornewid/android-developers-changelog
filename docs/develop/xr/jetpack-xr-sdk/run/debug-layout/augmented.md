---
title: Debug your app layout for augmented experiences with Layout Inspector  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/run/debug-layout/augmented
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Debug your app layout for augmented experiences with Layout Inspector Stay organized with collections Save and categorize content based on your preferences.



Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/ai-glasses-icon.svg)


AI Glasses

[Learn about XR device types →](/develop/xr/devices)

While you're building augmented experiences with Jetpack Compose Glimmer
components for AI glasses, you can inspect and debug your layout with the Layout
Inspector in Android Studio.

[![](/static/images/picto-icons/plus.svg)

See also

If you're new to using the Layout Inspector, learn how to do other common tasks in the layout debugging guide.

arrow\_forward](https://developer.android.com/studio/debug/layout-inspector)

## Turn off the embedded Layout Inspector

If you're running your app on [virtual AI glasses devices](/develop/xr/jetpack-xr-sdk/run/create-avds/ai-glasses) with the Android
XR Emulator, you need to turn off the embedded Layout Inspector:

1. Open your project in Android Studio, and then navigate to **Android Studio >
   Settings > Tools > Layout Inspector**.
2. Deselect **Enable embedded Layout Inspector**, and then restart Android
   Studio.

   ![Android Studio settings page for the Layout Inspector
   tool.](/static/images/develop/xr/jetpack-xr-sdk/run/disable-embedded-layout-inspector.png)

## Open the Layout Inspector

1. In Android Studio, [run your app](/studio/run).
2. When you see a screen you want to inspect, select **Tools > Layout
   Inspector** from the menu bar.

   The Layout Inspector opens, along with the **Layout Display** and the
   **Component Tree** panel.
3. From the **Running devices** drop-down menu, switch from the AI glasses AVD
   to the phone AVD that's acting as the host device.

   ![Layout Inspector view with the "Running devices" drop-down menu
   highlighted.](/static/images/develop/xr/jetpack-xr-sdk/run/augmented-layout-inspector-select-avd.png)
4. In the **Layout Display**, scroll past the UI layout for the phone AVD to
   find the UI layout for the AI glasses. Click elements here to inspect their
   attributes.

   ![Layout Inspector view showing the AI glasses UI in the Layout
   Display.](/static/images/develop/xr/jetpack-xr-sdk/run/augmented-layout-inspector-glasses-ui.png)

## Inspect layout attributes

As you interact with your app, inspect a view in the AI glasses UI by clicking
it in the **Layout Display** or in the **Component Tree**. All of the layout
attributes for that view appear in the **Attributes** panel.