---
title: https://developer.android.com/develop/xr/godot
url: https://developer.android.com/develop/xr/godot
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Godot's support for XR development is built on the [OpenXR](https://www.khronos.org/openxr/)
standard, ensuring that [OpenXR features supported for Android XR](https://developer.android.com/develop/xr/openxr) are
natively supported in Godot's XR system.

Follow this guide to learn about:

- Godot Engine support for Android XR
  - Godot XR basics
  - Developing and publishing apps for Android XR
  - Godot OpenXR Vendors Plugin
  - Getting support
- Input and interaction
- Supported extensions

## Godot engine support for Android XR

When you build Godot apps for Android XR, you leverage the high-performance,
open-source spatial computing capabilities of Godot 4. While Godot provides
native support for the core OpenXR specification, the **Android XR Vendor
Extensions** in the [Godot OpenXR Vendors Plugin](https://godotvr.github.io/godot_openxr_vendors/) provide the
specific implementations required to support Android XR hardware.

[Set up your project](https://developer.android.com/develop/xr/godot/setup) to get the latest versions of Godot and other tools and
configure your development environment for Android XR.

### Godot XR basics

If you are new to Godot or XR development, refer to the [official Godot XR
documentation](https://docs.godotengine.org/en/stable/tutorials/xr/setting_up_xr.html) to understand the core architecture. Here are a
few key areas to explore:

- **XR Node Structure** : Learn how to construct an XR scene using the `XROrigin3D` node, containing an `XRCamera3D` (representing the headset) and `XRController3D` nodes (representing hands or controllers).
- **OpenXR Integration** : Godot uses an [internal OpenXR
  interface](https://docs.godotengine.org/en/stable/tutorials/xr/setting_up_xr.html) to communicate with Android XR.
- **Godot XR Tools** : A highly recommended [library of
  components](https://docs.godotengine.org/en/stable/tutorials/xr/index.html#godot-xr-tools) for common XR functions like movement, grabbing, and UI interaction.
- **Project Setup** : Configuring your .`godot` project for Android export and spatial rendering.

### Develop and publish apps for Android

Godot provides a streamlined workflow for [exporting to Android](https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_android.html):

- Manage Android permissions in the Export dialog.
- Configure the **Android Export Preset** (Minimum SDK 34).
- Use the **One-Click Deploy** feature to test directly on Android XR devices.

Additionally, see the documentation for [packaging and distributing apps for
Android XR](https://developer.android.com/develop/xr/package-and-distribute) for specific requirements that apply to immersive apps that are
distributed on the Google Play Store. Ensure your app also adheres to the
[quality guidelines for immersive experiences](https://developer.android.com/docs/quality-guidelines/android-xr) to provide a consistent and
comfortable user experience on Android XR.

### Godot OpenXR Vendors Plugin

To access Android XR specific features, you must use the [Godot OpenXR Vendors
plugin](https://godotvr.github.io/godot_openxr_vendors/).

#### Android XR Vendor Extension

The Android XR Vendor Extension is the primary interface that adds Android XR
support to Godot. It implements the OpenXR extensions required for environmental
understanding, perception, and hardware-specific features.

### Get support

If you encounter issues, see the [support section for Godot](https://developer.android.com/develop/xr/support#godot) on our support
page for help.

## Input and interaction

Godot uses a flexible [**Action Map**](https://docs.godotengine.org/en/latest/tutorials/xr/xr_action_map.html) system within OpenXR to
handle various input methods. By defining actions (like select or grab) and
binding them to the Android XR interaction profiles, you can create immersive
experiences that work with both 6DoF motion controllers and hand tracking.

Android XR supports the following specific interaction methods within Godot:

- **Interaction Profiles**: Configure standard profiles in the OpenXR Action Map to ensure consistent input across different hardware.
- **Hand Tracking** : Provided through the [`XR_EXT_hand_tracking`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_hand_tracking) extension. Access hand joint data through `XRController3D` or specialized hand nodes provided by Godot XR Tools.
- **Eye Gaze** : Retrieve eye gaze data as a standard input pose for UI focus or social presence features using the [`XR_EXT_eye_gaze_interaction`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_eye_gaze_interaction) or [`XR_ANDROID_eye_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking) extensions.
- **Face Tracking** : Access real-time facial expression data using the [`XR_ANDROID_face_tracking`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_face_tracking) extension to drive avatar animations.
- **Mouse Interaction** : Support mouse and trackpad input profiles in XR using the [`XR_ANDROID_mouse_interaction`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_mouse_interaction) extension.

## Supported extensions

The following OpenXR extensions are supported when developing for Android XR in
Godot:

| Feature or capability | OpenXR extension string | Provided by |
|---|---|---|
| [Device Anchor Persistence](https://godotvr.github.io/godot_openxr_vendors/manual/androidxr/trackables.html) | [`XR_ANDROID_device_anchor_persistence`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_device_anchor_persistence) | Vendors Plugin |
| [Raycast](https://godotvr.github.io/godot_openxr_vendors/manual/androidxr/trackables.html) | [`XR_ANDROID_raycast`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_raycast) | Vendors Plugin |
| [Trackables (Planes/Depth)](https://godotvr.github.io/godot_openxr_vendors/manual/androidxr/trackables.html) | [`XR_ANDROID_trackables`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_trackables) | Vendors Plugin |
| [Object Tracking](https://godotvr.github.io/godot_openxr_vendors/manual/androidxr/trackables.html) | [`XR_ANDROID_trackables_object`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_trackables_object) | Vendors Plugin |
| [Scene Meshing](https://godotvr.github.io/godot_openxr_vendors/manual/androidxr/scene_meshing.html) | [`XR_ANDROID_scene_meshing`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_scene_meshing) | Vendors Plugin |
| [Face Tracking](https://godotvr.github.io/godot_openxr_vendors/manual/body_tracking.html#face-tracking-setup) | [`XR_ANDROID_face_tracking`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_face_tracking) | Vendors Plugin |
| [Eye Tracking](https://godotvr.github.io/godot_openxr_vendors/manual/body_tracking.html#eye-tracking) | [`XR_ANDROID_eye_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking) | Vendors Plugin |
| Mouse Interaction | [`XR_ANDROID_mouse_interaction`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_mouse_interaction) | Vendors Plugin |
| [Passthrough Camera State](https://godotvr.github.io/godot_openxr_vendors/manual/androidxr/passthrough_camera_state.html) | [`XR_ANDROID_passthrough_camera_state`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_passthrough_camera_state) | Vendors Plugin |
| [Depth Texture](https://godotvr.github.io/godot_openxr_vendors/manual/androidxr/environment_depth.html) | [`XR_ANDROID_depth_texture`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture) | Vendors Plugin |
| [Light Estimation](https://godotvr.github.io/godot_openxr_vendors/manual/androidxr/light_estimation.html) | [`XR_ANDROID_light_estimation`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_light_estimation) | Vendors Plugin |
| [Performance Metrics](https://godotvr.github.io/godot_openxr_vendors/manual/performance_metrics.html) | [`XR_ANDROID_performance_metrics`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_performance_metrics) | Vendors Plugin |
| [Recommended Resolution](https://godotvr.github.io/godot_openxr_vendors/manual/androidxr/dynamic_resolution.html) | [`XR_ANDROID_recommended_resolution`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_recommended_resolution) | Vendors Plugin |
| Unbounded Reference Space | [`XR_ANDROID_unbounded_reference_space`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_unbounded_reference_space) | Vendors Plugin |
| [Hand Interaction](https://docs.godotengine.org/en/stable/tutorials/xr/openxr_hand_tracking.html#the-hand-interaction-profile) | [`XR_EXT_hand_interaction`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_hand_interaction) | Godot Native OpenXR |
| [Hand Tracking](https://docs.godotengine.org/en/stable/tutorials/xr/openxr_hand_tracking.html#the-hand-interaction-profile) | [`XR_EXT_hand_tracking`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_hand_tracking) | Godot Native OpenXR |
| [Hand Tracking Data Source](https://docs.godotengine.org/en/stable/tutorials/xr/openxr_hand_tracking.html) | [`XR_EXT_hand_tracking_data_source`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_hand_tracking_data_source) | Godot Native OpenXR |
| [Hand Tracking Mesh](https://godotvr.github.io/godot_openxr_vendors/manual/meta/hand_tracking.html#hand-mesh) | [`XR_FB_hand_tracking_mesh`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_hand_tracking_mesh) | Vendors Plugin |
| [Hand Tracking Aim](https://godotvr.github.io/godot_openxr_vendors/manual/meta/hand_tracking.html#hand-tracking-aim) | [`XR_FB_hand_tracking_aim`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_hand_tracking_aim) | Vendors Plugin |
| [Eye Gaze Interaction](https://docs.godotengine.org/en/stable/tutorials/xr/openxr_settings.html) | [`XR_EXT_eye_gaze_interaction`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_eye_gaze_interaction) | Godot Native OpenXR |
| [Palm Pose](https://docs.godotengine.org/en/stable/tutorials/xr/openxr_hand_tracking.html) | [`XR_EXT_palm_pose`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_palm_pose) | Godot Native OpenXR |
| [DPad Binding](https://docs.godotengine.org/en/stable/tutorials/xr/xr_action_map.html) | [`XR_EXT_dpad_binding`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_dpad_binding) | Godot Native OpenXR |
| [Binding Modification](https://docs.godotengine.org/en/stable/tutorials/xr/xr_action_map.html) | [`XR_KHR_binding_modification`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_binding_modification) | Godot Native OpenXR |
| [Spatial Entity](https://docs.godotengine.org/en/stable/tutorials/xr/openxr_spatial_entities.html) | [`XR_EXT_spatial_entity`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_entity) | Godot Native OpenXR |
| [Spatial Anchor](https://docs.godotengine.org/en/stable/tutorials/xr/openxr_spatial_entities.html) | [`XR_EXT_spatial_anchor`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor) | Godot Native OpenXR |
| [Spatial Plane Tracking](https://docs.godotengine.org/en/stable/tutorials/xr/openxr_spatial_entities.html) | [`XR_EXT_spatial_plane_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking) | Godot Native OpenXR |
| [Spatial Marker Tracking](https://docs.godotengine.org/en/stable/tutorials/xr/openxr_spatial_entities.html) | [`XR_EXT_spatial_marker_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking) | Godot Native OpenXR |
| [Spatial Persistence](https://docs.godotengine.org/en/stable/tutorials/xr/openxr_spatial_entities.html) | [`XR_EXT_spatial_persistence`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence) | Godot Native OpenXR |
| [Spatial Persistence Operations](https://docs.godotengine.org/en/stable/tutorials/xr/openxr_spatial_entities.html) | [`XR_EXT_spatial_persistence_operations`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_spatial_persistence_operations) | Godot Native OpenXR |
| [Future](https://docs.godotengine.org/en/stable/tutorials/xr/openxr_spatial_entities.html) | [`XR_EXT_future`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_future) | Godot Native OpenXR |
| User Presence | [`XR_EXT_user_presence`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_user_presence) | Godot Native OpenXR |
| [Foveated Rendering](https://docs.godotengine.org/en/latest/tutorials/xr/openxr_settings.html#foveation-level) | [`XR_FB_foveation`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_foveation) | Godot Native OpenXR |
| [Foveation Configuration](https://docs.godotengine.org/en/latest/tutorials/xr/openxr_settings.html#foveation-level) | [`XR_FB_foveation_configuration`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_foveation_configuration) | Godot Native OpenXR |
| [Foveation (Vulkan)](https://docs.godotengine.org/en/latest/tutorials/xr/openxr_settings.html#foveation-level) | [`XR_FB_foveation_vulkan`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_foveation_vulkan) | Godot Native OpenXR |
| [Eye-Tracked Foveated Rendering](https://docs.godotengine.org/en/latest/tutorials/xr/openxr_settings.html#foveation-level) | [`XR_META_foveation_eye_tracked`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_META_foveation_eye_tracked) | Godot Native OpenXR |
| [Swapchain Update State](https://docs.godotengine.org/en/latest/tutorials/xr/openxr_settings.html#foveation-level) | [`XR_FB_swapchain_update_state`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_swapchain_update_state) | Godot Native OpenXR |
| Frame Synthesis | [`XR_EXT_frame_synthesis`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_frame_synthesis) | Godot Native OpenXR |
| [Space Warp](https://godotvr.github.io/godot_openxr_vendors/manual/meta/application_space_warp.html) | [`XR_FB_space_warp`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_space_warp) | Vendors Plugin |
| [Display Refresh Rate](https://docs.godotengine.org/en/latest/tutorials/xr/a_better_xr_start_script.html#on-session-begun) | [`XR_FB_display_refresh_rate`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_display_refresh_rate) | Godot Native OpenXR |
| [Color Space](https://godotvr.github.io/godot_openxr_vendors/manual/meta/color_space.html) | [`XR_FB_color_space`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_color_space) | Vendors Plugin |
| [Composition Layer Settings](https://godotvr.github.io/godot_openxr_vendors/manual/meta/composition_layers.html) | [`XR_FB_composition_layer_settings`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_composition_layer_settings) | Vendors Plugin |
| [Composition Layer Depth Test](https://godotvr.github.io/godot_openxr_vendors/manual/meta/composition_layers.html) | [`XR_FB_composition_layer_depth_test`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_composition_layer_depth_test) | Vendors Plugin |
| [Composition Layer Image Layout](https://godotvr.github.io/godot_openxr_vendors/manual/meta/composition_layers.html) | [`XR_FB_composition_layer_image_layout`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_composition_layer_image_layout) | Vendors Plugin |
| [Composition Layer Cylinder](https://docs.godotengine.org/en/stable/tutorials/xr/openxr_composition_layers.html) | [`XR_KHR_composition_layer_cylinder`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_composition_layer_cylinder) | Godot Native OpenXR |
| [Composition Layer Equirect2](https://docs.godotengine.org/en/stable/tutorials/xr/openxr_composition_layers.html) | [`XR_KHR_composition_layer_equirect2`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_composition_layer_equirect2) | Godot Native OpenXR |
| [Composition Layer Depth](https://docs.godotengine.org/en/stable/tutorials/xr/openxr_composition_layers.html) | [`XR_KHR_composition_layer_depth`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_composition_layer_depth) | Godot Native OpenXR |
| [Composition Layer Color Scale Bias](https://docs.godotengine.org/en/stable/tutorials/xr/openxr_composition_layers.html) | [`XR_KHR_composition_layer_color_scale_bias`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_composition_layer_color_scale_bias) | Godot Native OpenXR |
| [Local Floor Reference Space](https://docs.godotengine.org/en/stable/tutorials/xr/setting_up_xr.html) | [`XR_EXT_local_floor`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_local_floor) | Godot Native OpenXR |
| Visibility Mask | [`XR_KHR_visibility_mask`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_visibility_mask) | Godot Native OpenXR |
| [Spatial Containers](https://developer.android.com/develop/xr/godot/spatial-containers) | [`XR_EXT_spatial_container`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_spatial_container), [`XR_EXT_spatial_container_self_rendering`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_spatial_container_self_rendering) | Godot Native OpenXR \& Vendors Plugin |

Extensions are provided by one of these sources:

- **Godot Native OpenXR**: Core XR functionality is maintained directly within the Godot Engine.
- **Vendors Plugin** : Android XR and vendor-specific spatial capabilities are provided through the [Vendors Plugin repository](https://github.com/godotvr/godot_openxr_vendors). You must use the [latest compatible version](https://developer.android.com/develop/xr/godot/setup#install-godot-vendors-plugin).