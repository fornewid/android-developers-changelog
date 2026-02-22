---
title: https://developer.android.com/develop/xr/unity/setup
url: https://developer.android.com/develop/xr/unity/setup
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

This guide details the recommended editor versions, graphics settings, URP settings, and Android project settings when developing a Unity application for Android XR.

## Prerequisites

To develop with Unity you will need to[Download and install Unity Hub](https://unity.com/download).

Install[version 6000.0.58f2](https://unity.com/releases/editor/whats-new/6000.0.58f2)or higher of the Unity Editor and Android Build Support, which includes:

- OpenJDK
- Android SDK
- Android NDK Tools

## Select a rendering engine

We recommend using the Vulkan Graphics API to render Android XR apps. To select Vulkan as your Graphics API, follow these steps:

1. In Unity, go to**Edit** \>**Project Settings** \>**Player**.
2. Select the**Android** tab and navigate to**Other Settings \> Rendering**.
3. If**Auto Graphics API** is enabled, disable this setting to reveal the**Graphics APIs**section.
4. In the**Graphics APIs** section, select the**Add (+)** button and select**Vulkan**from the dropdown.

   ![Example showing how to change the graphics api settings in the UI](https://developer.android.com/static/images/develop/xr/unity/setup/graphics-api-settings.png)
5. Re-order the Graphics APIs using the handles (=) so that Vulkan is listed first.

6. Optionally, select any other Graphics APIs and click the**Remove**(-) button to remove them.

## Universal Render Pipeline

Android XR is compatible with the Universal Render Pipeline (URP). If you plan to use passthrough, you should update the default URP settings for best passthrough performance on Android XR.
| **Note:** For existing projects with assets made for Built-in Render Pipeline, you should use the[Render Pipeline Converter](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@17.0/manual/features/rp-converter.html)to convert those assets to be compatible with URP.

The following table has a list of Unity's recommended URP settings, which are explained in greater detail in the following sections.

|     Setting     |            Location             | Recommended value |
|-----------------|---------------------------------|-------------------|
| HDR             | Universal Render Pipeline Asset | Disabled          |
| Post-processing | Universal Renderer Data         | Disabled          |

| **Note:** Vulkan is required if you're using URP. We recommend using Vulkan as your graphics API for Android XR, as newer graphics features are supported only with that API.

### Universal Render Pipeline Asset settings

Follow these steps to optimize your Universal Render Pipeline Asset for Android XR:

1. Locate your project's**Universal Render Pipeline Asset** . One way to do this is to type`t:UniversalRenderPipelineAsset`into the**Project**window's search bar.

   | **Note:** If your project does not contain a Universal Render Pipeline Asset, refer to[Installing the Universal Render Pipeline into an existing Project](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@17.0/manual/InstallURPIntoAProject.html)from the URP docs.
2. Under the**Quality** header, disable**HDR**.

   ![Universal Render Pipeline Asset shown with recommended settings](https://developer.android.com/static/images/develop/xr/unity/setup/quality-settings.png)

### Universal Renderer Data settings

Follow these steps to optimize your Universal Renderer Data for Android XR:

1. Locate your project's**Universal Renderer Data Asset** . One way to do this is to type`t:UniversalRendererData`into the**Project**window's search bar.

2. In the**Inspector** , under the**Post-processing** header, uncheck**Enabled**.

   ![Universal Renderer Data shown with recommended settings](https://developer.android.com/static/images/develop/xr/unity/setup/post-processing-settings.png)

## Minimal Android API level

Set your project to a minimal API level of 24, which is required by the OpenXR Loader. Otherwise, your builds may fail.

Complete these steps to set the minimal Android API level.

1. Go to**Edit** \>**Project Settings** \>**Player**.
2. Select the Android tab and open**Other Settings**.
3. In the**Identification** section, for**Minimal API level**, select 24 or higher.

## Application entry point

Configure the following settings for application entry point:

1. Go to**Edit** \>**Project Settings** \>**Player**.
2. Select the**Android** tab and open**Other Settings**.
3. In the**Configuration** section, make sure**Application Entry Point** has**GameActivity** checked and**Activity**unchecked.

## Pop-up windows

Most Android XR apps require resizable windows, as they are required to render pop-ups such as system permission requests.

Follow these steps to ensure pop-up windows are rendered properly.

1. Go to**Edit** \>**Project Settings** \>**Player**.
2. Select the**Android** tab and open**Resolution and Presentation**
3. In the**Resolution** section, enable**Resizeable Activity**.

## See also

- [Unity Android XR: OpenXR](https://docs.unity3d.com/Packages/com.unity.xr.androidxr-openxr@latest)
- [Import Android XR Extensions for Unity](https://developer.android.com/develop/xr/unity/xr-extensions-quickstart)

*** ** * ** ***

OpenXR™ and the OpenXR logo are trademarks owned by The Khronos Group Inc. and are registered as a trademark in China, the European Union, Japan and the United Kingdom.