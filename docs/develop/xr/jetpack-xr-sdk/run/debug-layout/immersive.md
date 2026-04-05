---
title: Debug your app layout for immersive experiences with Layout Inspector  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/run/debug-layout/immersive
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Debug your app layout for immersive experiences with Layout Inspector Stay organized with collections Save and categorize content based on your preferences.




Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/xr-headsets-icon.svg)


XR Headsets

![](/static/images/develop/xr/xr-glasses-icon.svg)


Wired XR Glasses

[Learn about XR device types →](/develop/xr/devices)

While you're building immersive experiences for XR headsets and XR glasses with
spatial panels and orbiters, you can inspect and debug your layout with the
Layout Inspector in Android Studio.

[![](/static/images/picto-icons/plus.svg)

See also

If you're new to using the Layout Inspector, learn how to do other common tasks in the layout debugging guide.

arrow\_forward](https://developer.android.com/studio/debug/layout-inspector)

## Open the Layout Inspector

1. In Android Studio, [run your app](/studio/run).
2. After app deployment has completed, select **Tools > Layout Inspector** from
   the menu bar.

   The Layout Inspector opens, with the **Layout Display** on the left and the
   **Component Tree** panel on the right.

   Spatial UI elements such as orbiters and panels appear as separate objects
   beneath the main content.

   ![Android Studio window with the Layout Inspector
   open.](/static/images/develop/xr/jetpack-xr-sdk/studio-tools/components1.png)

## Inspect layout attributes

As you interact with your app, inspect a view by clicking it in the **Layout
Display** or in the **Component Tree**. All of the layout attributes for that
view appear in the **Attributes** panel. For example in the following image, the
attributes are shown for the `AndroidComposeView` spatial panel that is labeled
"More articles":

![Android Studio window with the Layout Inspector open and the Attributes panel visible.](/static/images/develop/xr/jetpack-xr-sdk/studio-tools/attributes.png)


**Figure 1.** See a view's layout attributes by clicking it.