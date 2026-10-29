---
title: https://developer.android.com/develop/xr/unreal
url: https://developer.android.com/develop/xr/unreal
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

[Unreal Engine](https://www.unrealengine.com) support for XR development is built on the
[OpenXR](https://www.khronos.org/openxr/) standard, ensuring that [OpenXR features supported for
Android XR](https://developer.android.com/develop/xr/openxr) are natively supported in Unreal.

Follow this guide to learn about:

- Unreal Engine support for Android XR
  - Unreal Engine XR basics
  - Developing and publishing apps for Android XR
  - Unreal Engine plugins for Android XR
  - Getting support
- Input and interaction
- Supported extensions

## Unreal Engine support for Android XR

When you build Unreal apps for Android XR, you can take advantage of the spatial
computing capabilities of the latest versions of Unreal Engine 5. Unreal Engine
5 provides support for the core OpenXR specification, while the Android XR
Extensions for Unreal provide support for Android XR and other specific
extensions to help you get started quickly.

### Unreal Engine XR basics

If you are new to Unreal or XR development, you can refer to Unreal's [XR
development documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/developing-for-xr-experiences-in-unreal-engine) to understand basic concepts and
workflows. Here are a few key areas to explore:

- **XR Framework** : Learn how to construct an [VR Pawn](https://dev.epicgames.com/documentation/en-us/unreal-engine/vr-template-in-unreal-engine) by attaching a Camera Component (representing the headset) and [Hand
  Input](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OpenXRHandTracking) (representing the hands) to a shared scene root.
- **OpenXR Plugin** : The [core interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine) for Android XR device support.
- **XR Architecture** : How Unreal handles the [tech stack and XR subsystems](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-xr-development-in-unreal-engine).
- **Project Setup** : [Configuring your `.uproject`](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-unreal-engine-projects-for-android-development) for spatial rendering.
- **Graphics Guidance** : Utilizing [foveated rendering, multiview, and
  variable rate shading (VRS)](https://dev.epicgames.com/documentation/en-us/unreal-engine/xr-performance-features-in-unreal-engine).
- **Performance and Profiling** : Tools and techniques for [optimizing your XR
  application](https://dev.epicgames.com/documentation/en-us/unreal-engine/xr-performance-and-profiling-in-unreal-engine).
- **Best Practices** : Design and development guidelines for creating [comfortable and immersive XR experiences](https://dev.epicgames.com/documentation/en-us/unreal-engine/xr-best-practices-in-unreal-engine).

### Develop and publish apps for Android

Unreal Engine provides comprehensive documentation for [developing, building,
and publishing for Android](https://dev.epicgames.com/documentation/en-us/unreal-engine/sharing-and-releasing-projects-for-unreal-engine). This documentation covers managing
Android permissions within the Engine, configuring Android Build Settings
(through Project Settings \> Platforms \> Android), and using the Unreal
Automation Tool (UAT).

Additionally, see the documentation for [packaging and distributing apps for
Android XR](https://developer.android.com/develop/xr/package-and-distribute) for specific requirements that apply to spatial apps that are
distributed on the Google Play Store. Ensure your app also adheres to the
[quality guidelines for immersive experiences](https://developer.android.com/docs/quality-guidelines/android-xr) to provide a consistent and
comfortable user experience on Android XR.

### Unreal Engine plugins for Android XR

There are two core plugins that provide support for building Unreal apps for
Android XR. These plugins are managed through the Plugins menu (Edit \> Plugins).

#### Android XR OpenXR Plugin

The Android XR OpenXR Plugin is the primary engine interface that adds Android
XR support to Unreal. It implements the OpenXR extensions required for spatial
tracking, environmental understanding, and perception. To learn how to add and
configure this plugin, refer to the [Unreal Engine OpenXR
documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine).

#### Android XR Extensions for Unreal

The Android XR Extensions for Unreal (v1.1.0, supporting Unreal Engine 5.6.x and
5.8.x) supplement the base OpenXR support, including additional features to help
you build immersive experiences such as spatial entities, spatial and depth
raycasting, viewport feathering, light estimation cubemap, advanced hand mesh
data, and specific hardware optimizations. To learn how to import and configure
this package, follow the [Android XR Extensions quickstart](https://developer.android.com/develop/xr/unreal/xr-extensions-quickstart) or explore the
[Android XR Extensions for Unreal API reference](https://developer.android.com/develop/xr/unreal/reference).

### Get support

If you encounter issues, see the [support section for Unreal Engine](https://developer.android.com/develop/xr/support#unreal) on our
support page for help.

## Input and interaction

Creating interactive spatial experiences requires mapping physical movements to
digital actions. Unreal Engine uses the Enhanced Input system combined with
OpenXR to handle both motion controllers and hand tracking. By setting up Input
Actions and Input Mapping Contexts, you can create flexible interactions---like
grabbing, pointing, and UI navigation---that work seamlessly across different
Android XR input methods.

For a comprehensive guide on building these mechanics, refer to Unreal Engine's
documentation on [Making Interactive XR Experiences](https://dev.epicgames.com/documentation/en-us/unreal-engine/making-interactive-xr-experiences-in-unreal-engine).

Android XR supports the following specific interaction methods within Unreal
Engine:

### Interaction profiles

You can configure interaction profiles in your Project Settings under the OpenXR
section. This allows your app to maintain consistent input mapping across
different controllers and tracking methods.

### Hand interaction

Hand interaction is provided through the OpenXR Hand Tracking extension. You can
access hand joint data and poses through the XR Tracking components in
Blueprints or C++.

### Eye gaze interaction

Eye gaze data can be retrieved as a standard input pose, letting you drive UI
focus or social presence features. This requires the
`android.permission.EYE_TRACKING_FINE` permission.

### Face tracking

Access real-time facial expression data to animate avatars or drive social
interactions. This uses the [`XR_ANDROID_face_tracking`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_face_tracking)
extension.

## Supported extensions

The following OpenXR extensions are supported when developing for Android XR in
Unreal:

| Feature or capability | OpenXR extension string | Provided by |
|---|---|---|
| [Device Anchor Persistence](https://developer.android.com/develop/xr/unreal/reference/class/UAndroidXRAnchorPersistenceBlueprintFunctionLibrary) | [`XR_ANDROID_device_anchor_persistence`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_device_anchor_persistence) | Android XR Extensions for Unreal (v1.0.0) |
| [Raycast](https://developer.android.com/develop/xr/unreal/reference/class/UAndroidXRTrackablesCoreBlueprintFunctionLibrary) | [`XR_ANDROID_raycast`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_raycast) | Android XR Extensions for Unreal (v1.0.0) |
| [Trackables (Planes/Depth)](https://developer.android.com/develop/xr/unreal/reference/class/UAndroidXRTrackablesCoreBlueprintFunctionLibrary) | [`XR_ANDROID_trackables`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_trackables) | Android XR Extensions for Unreal (v1.0.0) |
| [Object Tracking](https://developer.android.com/develop/xr/unreal/reference/class/UAndroidXRTrackablesObjectBlueprintFunctionLibrary) | [`XR_ANDROID_trackables_object`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_trackables_object) | Android XR Extensions for Unreal (v1.0.0) |
| [Scene Meshing](https://developer.android.com/develop/xr/unreal/reference/class/UAndroidXRSceneMeshingBlueprintFunctionLibrary) | [`XR_ANDROID_scene_meshing`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_scene_meshing) | Android XR Extensions for Unreal (v1.0.0) |
| [Face Tracking](https://developer.android.com/develop/xr/unreal/reference/class/UAndroidXRFaceTrackingSubsystem) | [`XR_ANDROID_face_tracking`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_face_tracking) | Android XR Extensions for Unreal (v1.0.0) |
| [Eye Tracking](https://developer.android.com/develop/xr/unreal/reference/class/UAndroidXREyeTrackingSubsystem) | [`XR_ANDROID_eye_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking) | Android XR Extensions for Unreal (v1.0.0) |
| [Passthrough Camera State](https://developer.android.com/develop/xr/unreal/reference/class/UAndroidXRBlueprintFunctionLibrary#getpassthroughcamerastate) | [`XR_ANDROID_passthrough_camera_state`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_passthrough_camera_state) | Android XR Extensions for Unreal (v1.0.0) |
| [Passthrough Mesh Layer](https://developer.android.com/develop/xr/unreal/reference/class/UAndroidXRPassthroughMeshSubsystem) | [`XR_ANDROID_composition_layer_passthrough_mesh`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_composition_layer_passthrough_mesh) | Android XR Extensions for Unreal (v1.0.0) |
| [Depth Texture](https://developer.android.com/develop/xr/unreal/reference/class/UAndroidXRDepthTextureBlueprintFunctionLibrary) | [`XR_ANDROID_depth_texture`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture) | Android XR Extensions for Unreal (v1.0.0) |
| [Light Estimation](https://developer.android.com/develop/xr/unreal/reference/class/UAndroidXRLightEstimationBlueprintFunctionLibrary) | [`XR_ANDROID_light_estimation`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_light_estimation) | Android XR Extensions for Unreal (v1.0.0) |
| [Light Estimation Cubemap](https://developer.android.com/develop/xr/unreal/reference/class/UAndroidXRLightEstimationBlueprintFunctionLibrary) | [`XR_ANDROID_light_estimation_cubemap`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap) | Android XR Extensions for Unreal (v1.1.0) |
| [Performance Metrics](https://developer.android.com/develop/xr/unreal/reference/class/UAndroidXRPerformanceMetricsBlueprintFunctionLibrary) | [`XR_ANDROID_performance_metrics`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_performance_metrics) | Android XR Extensions for Unreal (v1.0.0) |
| [Recommended Resolution](https://developer.android.com/develop/xr/unreal/reference/class/UAndroidXRRecommendedResolutionBlueprintFunctionLibrary) | [`XR_ANDROID_recommended_resolution`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_resolution) | Android XR Extensions for Unreal (v1.0.0) |
| [Hand Interaction](https://developer.android.com/develop/xr/unreal/reference/class/UHandInteractionBlueprintFunctionLibrary) | [`XR_EXT_hand_interaction`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_hand_interaction) | Android XR Extensions for Unreal (v1.0.0) |
| Debug Utils | [`XR_EXT_debug_utils`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_debug_utils) | Unreal Native OpenXR |
| Performance Settings | [`XR_EXT_performance_settings`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_performance_settings) | Unreal Native OpenXR |
| Display Refresh Rate | [`XR_FB_display_refresh_rate`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_display_refresh_rate) | Unreal Native OpenXR |
| [Hand Tracking Mesh](https://developer.android.com/develop/xr/unreal/reference/class/UHandTrackingMeshBlueprintFunctionLibrary) | [`XR_FB_hand_tracking_mesh`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_hand_tracking_mesh) | Android XR Extensions for Unreal (v1.0.0) |
| Space Warp | [`XR_FB_space_warp`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_space_warp) | Unreal Native OpenXR |
| Equirect2 Composition Layer | [`XR_KHR_composition_layer_equirect2`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_composition_layer_equirect2) | Unreal Native OpenXR |
| Android Thread Settings | [`XR_KHR_android_thread_settings`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_android_thread_settings) | Unreal Native OpenXR |
| [Global Passthrough Dimming](https://developer.android.com/develop/xr/unreal/reference/class/UAndroidXRGlobalDimmingBlueprintFunctionLibrary) | [`XR_ANDROID_global_passthrough_dimming`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_global_passthrough_dimming) | Android XR Extensions for Unreal (v1.0.0) |
| [System Extension Properties](https://developer.android.com/develop/xr/unreal/reference/class/UAndroidXRSystemExtensionsBlueprintFunctionLibrary) | [`XR_ANDROID_enumerate_system_extension_properties`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_enumerate_system_extension_properties) | Android XR Extensions for Unreal (v1.0.0) |
| [Spatial Entities](https://developer.android.com/develop/xr/unreal/reference/class/UAndroidXRSpatialEntitiesSubsystem) | [`XR_EXT_spatial_entity`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity) | Android XR Extensions for Unreal (v1.0.0) |
| [Spatial Plane Tracking](https://developer.android.com/develop/xr/unreal/reference/class/UAndroidXRSpatialPlaneTrackingSubsystem) | [`XR_EXT_spatial_plane_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking) | Android XR Extensions for Unreal (v1.0.0) |
| [Spatial Marker Tracking](https://developer.android.com/develop/xr/unreal/reference/class/UAndroidXRSpatialMarkerTrackingSubsystem) | [`XR_EXT_spatial_marker_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking) | Android XR Extensions for Unreal (v1.0.0) |
| [Spatial Anchors \& Persistence](https://developer.android.com/develop/xr/unreal/reference/class/UAndroidXRSpatialAnchorsSubsystem) | [`XR_EXT_spatial_anchor`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor), [`XR_EXT_spatial_persistence`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence) | Android XR Extensions for Unreal (v1.0.0) |
| [Viewport Feathering](https://developer.android.com/develop/xr/unreal/reference/class/UAndroidXRViewportFeatheringBlueprintFunctionLibrary) | [`XR_ANDROID_viewport_feathering`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_viewport_feathering) | Android XR Extensions for Unreal (v1.1.0) |
| [Spatial Discovery](https://developer.android.com/develop/xr/unreal/reference/class/UAndroidXRSpatialDiscoveryRaycastSubsystem) \& [Depth Raycast](https://developer.android.com/develop/xr/unreal/reference/class/UAndroidXRSpatialDepthRaycastSubsystem) | [`XR_ANDROID_spatial_discovery_raycast`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast) | Android XR Extensions for Unreal (v1.1.0) |

Extensions are provided by one of these sources:

- **Android XR Extensions for Unreal** : These are Google-specific extensions (`ANDROID`) and spatial entity extensions (`EXT`) developed for the Android XR platform. To utilize these spatial capabilities, [install and enable the
  Android XR Extensions plugin](https://developer.android.com/develop/xr/unreal/xr-extensions-quickstart) in your `.uproject` and see the [Android XR Extensions for Unreal API reference](https://developer.android.com/develop/xr/unreal/reference) for Blueprint and C++ usage.
- **Unreal Native OpenXR** : These features leverage the Khronos (`KHR`), Extension (`EXT`), and Meta (`FB`) standard extensions that are already integrated and maintained directly within Unreal Engine's core OpenXR plugin.

> [!NOTE]
> **Note:** Both `XR_ANDROID_device_anchor_persistence` (`AndroidXRAnchorPersistence`) and `XR_EXT_spatial_anchor` / `XR_EXT_spatial_persistence` (`AndroidXRSpatialAnchors`) coexist as supported alternatives in v1.1.0+. For projects using the Spatial Entities architecture (`XR_EXT_spatial_entity`), use `XR_EXT_spatial_anchor` and `XR_EXT_spatial_persistence`.