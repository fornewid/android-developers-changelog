---
title: https://developer.android.com/develop/xr/unity/xr-extensions-quickstart
url: https://developer.android.com/develop/xr/unity/xr-extensions-quickstart
source: md.txt
---

# Android XR Extensions for Unity quickstart

Each feature includes a sample for you to use and play with code and scene setups. This quickstart walks you through importing the Android XR Extensions for Unity package and then configuring the face tracking sample.

## Prerequisites

Before completing these steps, make sure you've completed the steps described in[Unity project setup](https://developer.android.com/develop/xr/unity/setup).

## Import packages

To load a Unity Package Manager package from a Git URL:

1. In**Window** , open the**Package Manager**.
2. Open the add menu in the**Package Manager**toolbar.
3. In the options for adding packages, click the**+**(plus) button.
4. In the drop-down list, click**Install package from git URL**.

   ![Example of the Install package from git URL button in the UI](https://developer.android.com/static/images/develop/xr/unity/xr-extensions-quickstart/add-menu.png)
5. Enter the following URL:

       https://github.com/android/android-xr-unity-package.git

6. Select**Install**.

## Configure the face tracking sample

All samples, including this one, include a README file containing instructions on how to configure and set up the project.

To import and configure the sample:

1. Go to**Package Manager** \>**In Project** \>**Android XR Extensions for Unity**.

   ![Example of the package manager settings](https://developer.android.com/static/images/develop/xr/unity/xr-extensions-quickstart/package-manager-settings.png)
2. Select the**Samples** tab. Find the**Face Tracking** sample and click**Import**.

   ![Example of the samples tab](https://developer.android.com/static/images/develop/xr/unity/xr-extensions-quickstart/import-face-tracking-sample.png)
3. Go to**Edit \> Project Settings \> XR Plug-in Management**.

4. In the**Android** tab, under**Plug-in Providers** , enable**OpenXR**.

   Then, enable the**Android XR (Extensions) feature group** .![Example of the project settings screen](https://developer.android.com/static/images/develop/xr/unity/xr-extensions-quickstart/plugin-providers-settings.png)
5. Go to**Edit \> Project Settings \> XR Plug-in Management \> OpenXR**.

6. Enable**Android XR: Face Tracking**.

   ![Enable Android XR: Face Tracking](https://developer.android.com/static/images/develop/xr/unity/xr-extensions-quickstart/openxr-feature-groups-enable-face-tracking.png)
7. Under**XR Plug-in Management \> Project Validation**, fix all OpenXR-related issues. This helps configure your Player Settings.

   ![Example of the project validation settings](https://developer.android.com/static/images/develop/xr/unity/xr-extensions-quickstart/project-validation-settings.png)
8. In your**Project** , open the**FaceTracking** scene, located in**Assets \> Samples \> Android XR Extensions for Unity \>*version*\> Face Tracking**.

   ![Open the Face Tracking scene](https://developer.android.com/static/images/develop/xr/unity/xr-extensions-quickstart/face-tracking-unity-scene.png)

*** ** * ** ***

OpenXR™ and the OpenXR logo are trademarks owned by The Khronos Group Inc. and are registered as a trademark in China, the European Union, Japan and the United Kingdom.