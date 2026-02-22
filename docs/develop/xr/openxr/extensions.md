---
title: https://developer.android.com/develop/xr/openxr/extensions
url: https://developer.android.com/develop/xr/openxr/extensions
source: md.txt
---

<br />


Applicable XR devices  
This guidance helps you build experiences for these types of XR devices.  
[Learn about XR device types →](https://developer.android.com/develop/xr/devices)  
![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets)  
![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses)  
[Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Android XR supports OpenXR through the [OpenXR 1.1 specification](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html)
and a long list of third party vendor extensions. Using these extensions offers
you that familiar experience when developing for XR. Some of these capabilities
require [Android runtime permissions](https://developer.android.com/develop/xr/get-started#permissions-xr). If you are looking to build directly
on the OpenXR APIs, you can find the required header files [in the
jetpack-xr-natives repository](https://github.com/google-ar/jetpack-xr-natives/tree/release/third_party/OpenXR_KHR/generated/include/openxr).

### Android XR Vendor Extensions

| **Preview:** All `XR_ANDROID` extensions have been submitted to the Khronos group for approval. Documentation for these extensions will be relocated to the official specification documentation over time.

| Extension Name | Description |
|---|---|
| [`XR_ANDROID_composition_layer_passthrough_mesh`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh) | Allows the app to project passthrough textures onto arbitrary geometry through an additional composition layer. This extension requires [`android.permission.SCENE_UNDERSTANDING_COARSE`](https://developer.android.com/develop/xr/get-started#permissions-xr). |
| [`XR_ANDROID_depth_texture`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture) | Exposes raw and smooth depth for occlusion, hit tests, and other specific tasks that make use of accurate scene geometry, such as counterfeit face detection. Provides a low resolution depth texture and confidence of a scene from the current camera/eye poses. This extension requires [`android.permission.SCENE_UNDERSTANDING_FINE`](https://developer.android.com/develop/xr/get-started#permissions-xr). |
| [`XR_ANDROID_device_anchor_persistence`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_device_anchor_persistence) | Allows the application to persist, retrieve, and unpersist anchors on the current device, across applications and device sessions. This extension requires [`android.permission.SCENE_UNDERSTANDING_COARSE`](https://developer.android.com/develop/xr/get-started#permissions-xr). |
| [`XR_ANDROID_eye_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking) | Allows the application to obtain the position and orientation of the user's eyes, which is designed to make eye pose and status representation for avatars more realistic. Don't use this extension for other eye tracking purposes. For interaction, [`XR_EXT_eye_gaze_interaction`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_eye_gaze_interaction) should be used instead. This extension requires [`android.permission.EYE_TRACKING_COARSE`](https://developer.android.com/develop/xr/get-started#permissions-xr) or [`android.permission.EYE_TRACKING_FINE`](https://developer.android.com/develop/xr/get-started#permissions-xr). |
| [`XR_ANDROID_face_tracking`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_face_tracking) | Allows the application to get weights of blend shapes and render facial expressions in XR experiences. This extension requires [`android.permission.FACE_TRACKING`](https://developer.android.com/develop/xr/get-started#permissions-xr). |
| [`XR_ANDROID_hand_mesh`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_hand_mesh) | Enables hand tracking inputs represented as a dynamic hand mesh. This extension is intended to provide vertex and index buffers for the mesh of a personalized representation of the user's hands. For tracking hand joints [`XR_EXT_hand_tracking`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_hand_tracking) such be used and for interactions [`XR_EXT_hand_interaction`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_hand_interaction) such be used. This extension requires [`android.permission.HAND_TRACKING`](https://developer.android.com/develop/xr/get-started#permissions-xr). |
| [`XR_ANDROID_light_estimation`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation) | Estimates the environmental lighting (including [spherical harmonics](https://en.wikipedia.org/wiki/Spherical_harmonics)) of a user's current environment. This extension allows the application to request data representing the lighting of the real-world environment around the headset. This information can be used when rendering virtual objects to light them under the same conditions as the scene they're placed in. This extension requires [`android.permission.SCENE_UNDERSTANDING_COARSE`](https://developer.android.com/develop/xr/get-started#permissions-xr). |
| [`XR_ANDROID_mouse_interaction`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_mouse_interaction) | This extension introduces a new interaction profile specifically designed for mouse devices to input through the OpenXR action system. Allows for commonly used action poses for user mouse profiles, including both mouse devices and trackpad devices. This is designed for interacting with objects through a mouse pointer in 3D space. For example, using a virtual laser pointer to aim at a virtual button on the wall is an interaction suited to the "aim" pose. |
| [`XR_ANDROID_passthrough_camera_state`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_passthrough_camera_state) | Provides enabled, initializing, or disabled states for the passthrough camera. |
| [`XR_ANDROID_performance_metrics`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_performance_metrics) | This extension provides APIs to enumerate and query various performance metrics counters of the current XR device, compositor and XR application. |
| [`XR_ANDROID_raycast`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_raycast) | This extension allows the application to perform raycasts against trackables in the environment. This extension requires [`android.permission.SCENE_UNDERSTANDING_COARSE`](https://developer.android.com/develop/xr/get-started#permissions-xr). |
| [`XR_ANDROID_scene_meshing`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_scene_meshing) | Allows the application to get a semantic 3D mesh of the real-world environment in real-time. This extension requires [`android.permission.SCENE_UNDERSTANDING_FINE`](https://developer.android.com/develop/xr/get-started#permissions-xr). |
| [`XR_ANDROID_trackables`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_trackables) | This extension allows the application to access trackables such as planes from the physical environment, and create anchors attached to a trackable. This extension requires [`android.permission.SCENE_UNDERSTANDING_COARSE`](https://developer.android.com/develop/xr/get-started#permissions-xr). |
| [`XR_ANDROID_trackables_object`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_trackables_object) | Provides support for tracking physical objects such as keyboard and mouse in a scene. This extension requires [`android.permission.SCENE_UNDERSTANDING_COARSE`](https://developer.android.com/develop/xr/get-started#permissions-xr). |
| [`XR_ANDROID_trackables_qr_code`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code) | Enables physical QR Code tracking and QR Code data decoding. This extension requires [`android.permission.SCENE_UNDERSTANDING`](https://developer.android.com/develop/xr/get-started#permissions-xr). |
| [`XR_ANDROID_unbounded_reference_space`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_unbounded_reference_space) | Provides an unbounded reference space that can be used to build better scene understanding over time. This reference space enables the viewer to move freely through a complex environment, often many meters from where they started, while always optimizing for coordinate system stability near the viewer. |

### Other Supported Extensions

The following additional extensions are also supported. Information is located
on external sites.
| **Note:** Extensions marked with an asterisk (\*) require [Android runtime
| permissions](https://developer.android.com/develop/xr/get-started#permissions-xr).

- [`XR_EXT_debug_utils`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_debug_utils)
- [`XR_EXT_dpad_binding`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_dpad_binding)
- [`XR_EXT_eye_gaze_interaction`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_eye_gaze_interaction) \*
- [`XR_EXT_hand_tracking`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_hand_tracking) \*
- [`XR_EXT_hand_interaction`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_hand_interaction)
- [`XR_EXT_palm_pose`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_palm_pose)
- [`XR_EXT_performance_settings`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_performance_settings)
- [`XR_EXT_uuid`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_uuid)
- [`XR_FB_composition_layer_depth_test`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_composition_layer_depth_test)
- [`XR_FB_display_refresh_rate`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_display_refresh_rate)
- [`XR_FB_foveation`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_foveation)
- [`XR_FB_foveation_configuration`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_foveation_configuration)
- [`XR_FB_foveation_vulkan`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_foveation_vulkan)
- [`XR_FB_hand_tracking_aim`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_hand_tracking_aim) \*
- [`XR_FB_space_warp`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_space_warp)
- [`XR_KHR_android_create_instance`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_android_create_instance)
- [`XR_KHR_android_surface_swapchain`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_android_surface_swapchain)
- [`XR_KHR_android_thread_settings`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_android_thread_settings)
- [`XR_KHR_binding_modification`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_binding_modification)
- [`XR_KHR_composition_layer_color_scale_bias`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_composition_layer_color_scale_bias)
- [`XR_KHR_composition_layer_cube`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_composition_layer_cube)
- [`XR_KHR_composition_layer_cylinder`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_composition_layer_cylinder)
- [`XR_KHR_composition_layer_depth`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_composition_layer_depth)
- [`XR_KHR_composition_layer_equirect2`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_composition_layer_equirect2)
- [`XR_KHR_convert_timespec_time`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_convert_timespec_time)
- [`XR_KHR_loader_init`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_loader_init)
- [`XR_KHR_loader_init_android`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_loader_init_android)
- [`XR_KHR_opengl_es_enable`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_opengl_es_enable)
- [`XR_KHR_swapchain_usage_input_attachment_bit`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_swapchain_usage_input_attachment_bit)
- [`XR_KHR_vulkan_enable2`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_vulkan_enable2)
- [`XR_META_vulkan_swapchain_create_info`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_META_vulkan_swapchain_create_info)
- [`XR_MND_headless`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_MND_headless)

*** ** * ** ***

OpenXR™ and the OpenXR logo are trademarks owned
by The Khronos Group Inc. and are registered as a trademark in China,
the European Union, Japan and the United Kingdom.