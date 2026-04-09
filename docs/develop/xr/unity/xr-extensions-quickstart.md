---
title: Android XR Extensions for Unity quickstart  |  Android XR for Unity  |  Android Developers
url: https://developer.android.com/develop/xr/unity/xr-extensions-quickstart
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Unity](https://developer.android.com/develop/xr/unity)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Android XR Extensions for Unity quickstart Stay organized with collections Save and categorize content based on your preferences.




Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/xr-headsets-icon.svg)


XR Headsets

![](/static/images/develop/xr/xr-glasses-icon.svg)


Wired XR Glasses

[Learn about XR device types →](/develop/xr/devices)

Each feature includes a sample for you to use and play with code and scene
setups. This quickstart walks you through importing the Android XR Extensions
for Unity package and then configuring the face tracking sample.

## Prerequisites

Before completing these steps, make sure you've completed the steps described in
[Unity project setup](/develop/xr/unity/setup).

## Import packages

To load a Unity Package Manager package from a Git URL:

1. In **Window**, open the **Package Manager**.
2. Open the add menu in the **Package Manager** toolbar.
3. In the options for adding packages, click the **+** (plus) button.
4. In the drop-down list, click **Install package from git URL**.

   ![Example of the Install package from git URL button in the UI](/static/images/develop/xr/unity/xr-extensions-quickstart/add-menu.png)
5. Enter the following URL:

   ```
   https://github.com/android/android-xr-unity-package.git
   ```
6. Select **Install**.

## Configure the face tracking sample

All samples, including this one, include a README file containing
instructions on how to configure and set up the project.

To import and configure the sample:

1. Go to **Package Manager** > **In Project** > **Android XR Extensions for Unity**.

   ![Example of the package manager settings](/static/images/develop/xr/unity/xr-extensions-quickstart/package-manager-settings.png)
2. Select the **Samples** tab. Find the **Face Tracking** sample and click **Import**.

   ![Example of the samples tab](/static/images/develop/xr/unity/xr-extensions-quickstart/import-face-tracking-sample.png)
3. Go to **Edit > Project Settings > XR Plug-in Management**.
4. In the **Android** tab, under **Plug-in Providers**, enable **OpenXR**.

   Then, enable the **Android XR (Extensions) feature group**.
   ![Example of the project settings screen](/static/images/develop/xr/unity/xr-extensions-quickstart/plugin-providers-settings.png)
5. Go to **Edit > Project Settings > XR Plug-in Management > OpenXR**.
6. Enable **Android XR: Face Tracking**.

   ![Enable Android XR: Face Tracking](/static/images/develop/xr/unity/xr-extensions-quickstart/openxr-feature-groups-enable-face-tracking.png)
7. Under **XR Plug-in Management > Project Validation**, fix all OpenXR-related
   issues. This helps configure your Player Settings.

   ![Example of the project validation settings](/static/images/develop/xr/unity/xr-extensions-quickstart/project-validation-settings.png)
8. In your **Project**, open the **FaceTracking** scene, located in **Assets > Samples > Android XR Extensions for Unity > *version* > Face Tracking**.

   ![Open the Face Tracking scene](/static/images/develop/xr/unity/xr-extensions-quickstart/face-tracking-unity-scene.png)

---

OpenXR™ and the OpenXR logo are trademarks owned
by The Khronos Group Inc. and are registered as a trademark in China,
the European Union, Japan and the United Kingdom.