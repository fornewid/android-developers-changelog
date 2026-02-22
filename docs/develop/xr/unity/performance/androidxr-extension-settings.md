---
title: https://developer.android.com/develop/xr/unity/performance/androidxr-extension-settings
url: https://developer.android.com/develop/xr/unity/performance/androidxr-extension-settings
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

Unity provides some performance-related features that are specific to Android XR and require the Android XR Extensions package. Enable these features to improve frame rates and reduce GPU load through spacewarp and Vulkan subsampling, and to reduce tracked rendering latency using late latching.

## Prerequisites

Before following this guidance, make sure you've verified and completed the following prerequisites:

- Complete all the steps for[setting up your project in Unity](https://developer.android.com/develop/xr/unity/setup).
- [Import the Android XR Extensions for Unity package](https://developer.android.com/develop/xr/unity/xr-extensions-quickstart#import_packages).

## Enable spacewarp

[URP Application Spacewarp](https://docs.unity3d.com/6000.2/Documentation/Manual/xr-graphics-spacewarp.html)is an OpenXR optimization that helps maintain high frame rates by synthesizing every other frame. The technique uses motion vectors and depth data from previous frames to predict where pixels should move, reducing computational power and energy use.

### Benefits

- Reduces GPU rendering workload by synthesizing alternate frames.
- Significantly reduces computational power and energy consumption.
- Uses reprojection to reduce latency between user movements and display updates.

### Enable this feature

1. From the Unity main menu, click**Edit \> Project Settings**.
2. Expand the**XR Plug-in Management**section.
3. Select the tab that corresponds to your current XR device.
4. Go to the**OpenXR Feature Groups**section.
5. In the**All Features** section, enable**Application SpaceWarp**.

   ![Unity settings for spacewarp](https://developer.android.com/static/images/develop/xr/unity/performance/spacewarp-settings.png)

| **Note:** Spacewarp requires your shaders to support motion vectors. For information on enabled motion vectors in your shaders, see[Unity's guidelines](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.15/manual/features/spacewarp/spacewarp-shaders.html).

## Enable vulkan subsampling

Vulkan Subsampling allows images be created and sampled at variable densities using Fragment Density Maps. This Vulkan feature enables different areas of the screen to be rendered and transferred to memory at different resolutions, which is particularly useful for foveated rendering, where peripheral areas can use a lower resolution.

### Benefits

- Provides varying improvement when combined with foveated rendering, depending on form factor.
- Reduces aliasing in peripheral areas through bilinear filtering.
- Enables efficient variable-rate rendering across different screen regions.

### Enable this feature

1. From the Unity main menu, click**Edit \> Project Settings**.
2. Expand the**XR Plug-in Management** section, and then click**OpenXR**.
3. Click the cog icon next to**Android XR (Extensions): Session Management**.
4. Enable**Subsampling (Vulkan)**.

   ![Unity settings for Vulkan subsampling](https://developer.android.com/static/images/develop/xr/unity/performance/vulkan-subsampling.png)

## Enable late latching

[Late latching](https://docs.unity3d.com/Packages/com.unity.xr.oculus@4.4/api/Unity.XR.Oculus.OculusSettings.html#Unity_XR_Oculus_OculusSettings_LateLatching)is a technique that minimizes the delay between the user's physical movement and the resulting visual change on the display. It allows the head pose to be updated late in the frame generation pipeline, which improves both the comfort and perceived frame rate of your XR apps. It achieves this by reducing input latency by close to a whole frame time.

### Benefits

- Significantly reduces Motion-to-Photon (MTP) latency.
- Improves user comfort and reduces motion sickness.
- Enhances stability and precision.

### Enable this feature

To enable late latching, turn on the feature at runtime for your app:  

    private XRDisplaySubsystem xrDisplay;

    private XRDisplaySubsystem.LateLatchNode lateLatchNode = XRDisplaySubsystem.LateLatchNode.Head;

    void Start()
    {
        List<XRDisplaySubsystem> xrDisplaySubsystems = new();

        SubsystemManager.GetSubsystems(xrDisplaySubsystems);

        if (xrDisplaySubsystems.Count >= 1)
        {
            xrDisplay = xrDisplaySubsystems[0];
        }
    }

    void Update()
    {
        if (xrDisplay != null)
        {
            transform.position += new Vector3(Mathf.Epsilon, 0, 0);

            Quaternion rot = transform.rotation;

            rot.x += Mathf.Epsilon;

            transform.rotation = rot;

            xrDisplay.MarkTransformLateLatched(transform, lateLatchNode);
        }
    }