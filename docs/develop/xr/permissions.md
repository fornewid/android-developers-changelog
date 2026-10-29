---
title: https://developer.android.com/develop/xr/permissions
url: https://developer.android.com/develop/xr/permissions
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Just like apps on mobile devices and other form factors, some capabilities
offered by XR apps require your app to [declare permissions](https://developer.android.com/training/permissions/declaring#add-to-manifest)
in your app's AndroidManifest file. In the case of dangerous permissions, your
app may need to [request runtime permissions](https://developer.android.com/training/permissions/requesting). Read [Permissions
on Android](https://developer.android.com/guide/topics/permissions/overview) and [permission best practices](https://developer.android.com/training/permissions/usage-notes) for more
in-depth information.

The following permissions can be used by XR apps. All of the permissions in this
section are considered dangerous permissions, so you must declare them in your
app manifest **and** request them at runtime.

### android.permission.EYE_TRACKING_COARSE

Representing the user's eye pose, status, and orientation, such as for use with
avatars. Use this permission when low-precision eye tracking data is needed.

### Jetpack XR SDK

N/A

### OpenXR Extensions

- [`XR_ANDROID_eye_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking)
- [`xrGetCoarseTrackingEyesInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking)

### Unity Features

- [Android XR: AR Face](https://docs.unity3d.com/Packages/com.unity.xr.androidxr-openxr@0.4/manual/features/faces.html)

### android.permission.EYE_TRACKING_FINE

Eye gaze for selection, input, interactions, and eye-tracked foveated rendering.

### Jetpack XR SDK

N/A

### OpenXR Extensions

- [`XR_EXT_eye_gaze_interaction`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_eye_gaze_interaction)
- [`xrGetFineTrackingEyesInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking)
- [`XR_META_foveation_eye_tracked`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_META_foveation_eye_tracked)
- [`XR_VARJO_foveated_rendering`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_VARJO_foveated_rendering)

### Unity Features

- [Eye Gaze Interaction](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.13/manual/features/eyegazeinteraction.html)

### android.permission.FACE_TRACKING

Tracking and rendering facial expressions.

### Jetpack XR SDK

N/A

### OpenXR Extensions

- [`XR_ANDROID_face_tracking`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_face_tracking)
- [`XR_ANDROID_face_tracking_data_source`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source)

### Unity Features

- [`XRFaceTrackingFeature`](https://developer.android.com/develop/xr/unity/reference/class/Google/XR/Extensions/XRFaceTrackingFeature)

### android.permission.RECORD_AUDIO

Recording audio input, such as for audio-driven face tracking data sources.

### Jetpack XR SDK

N/A

### OpenXR Extensions

- [`XR_ANDROID_face_tracking_data_source`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source)

### Unity Features

N/A

### android.permission.HAND_TRACKING

Tracking hand joint poses and angular and linear velocities; using a mesh
representation of the user's hands.

> [!NOTE]
> **Note:** This permission is not required for detecting basic gestures such as pinching, poking, aiming, and gripping.

### Jetpack XR SDK

- [Hand state and joint poses](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-hands)

### OpenXR Extensions

- [`XR_ANDROID_hand_mesh`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_hand_mesh)
- [`XR_EXT_hand_tracking`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_hand_tracking)
- [`XR_FB_hand_tracking_aim`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_hand_tracking_aim)
- [`XR_FB_hand_tracking_mesh`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_hand_tracking_mesh)

### Unity Features

- [`XR Hands`](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.5/manual/index.html)
- [`XRHandMeshFeature`](https://developer.android.com/develop/xr/unity/reference/class/Google/XR/Extensions/XRHandMeshFeature)

### android.permission.BODY_TRACKING

Tracking body joint poses and skeleton proportions.

### Jetpack XR SDK

N/A

### OpenXR Extensions

- [`XR_ANDROID_body_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_body_tracking)

### Unity Features

- [`XRBodyTrackingFeature`](https://developer.android.com/develop/xr/unity/reference/class/Google/XR/Extensions/XRBodyTrackingFeature)

### android.permission.SCENE_UNDERSTANDING_COARSE

Light estimation; projecting passthrough onto mesh surfaces; performing raycasts
against trackables in the environment; plane, image, marker, QR code, mesh, and
object tracking; persistent and shared anchors.

### Jetpack XR SDK

- [`PanelEntity`](https://developer.android.com/develop/xr/jetpack-xr-sdk/ui-compose#create-spatial)
- [Plane tracking](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-arcore#retrieve-state)
- [Hit testing](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-arcore#perform-hit-test)
- [Anchor persistence](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-arcore#persist-anchor)

### OpenXR Extensions

- [`XR_ANDROID_anchor_sharing_export`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_anchor_sharing_export)
- [`XR_ANDROID_composition_layer_passthrough_mesh`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_composition_layer_passthrough_mesh)
- [`XR_ANDROID_device_anchor_persistence`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_device_anchor_persistence)
- [`XR_ANDROID_light_estimation`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_light_estimation)
- [`XR_ANDROID_raycast`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_raycast)
- [`XR_ANDROID_spatial_anchor_space`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space)
- [`XR_ANDROID_spatial_component_subsumed_by`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_component_subsumed_by)
- [`XR_ANDROID_spatial_discovery_bounds`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds)
- [`XR_ANDROID_spatial_entity_bound_anchor`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_entity_bound_anchor)
- [`XR_ANDROID_spatial_object_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_object_tracking)
- [`XR_ANDROID_trackables`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_trackables)
- [`XR_ANDROID_trackables_image`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image)
- [`XR_ANDROID_trackables_marker`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker)
- [`XR_ANDROID_trackables_object`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_trackables_object)
- [`XR_ANDROID_trackables_qr_code`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code)
- [`XR_EXT_spatial_anchor`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor)
- [`XR_EXT_spatial_image_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking)
- [`XR_EXT_spatial_marker_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking)
- [`XR_EXT_spatial_mesh_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking)
- [`XR_EXT_spatial_object_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_object_tracking)
- [`XR_EXT_spatial_persistence`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence)
- [`XR_EXT_spatial_persistence_operations`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_spatial_persistence_operations)
- [`XR_EXT_spatial_plane_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking)

### Unity Features

- [`XRAnchorFeature`](https://developer.android.com/develop/xr/unity/reference/class/Google/XR/Extensions/XRAnchorFeature)
- [`XRLightEstimationFeature`](https://developer.android.com/develop/xr/unity/reference/class/Google/XR/Extensions/XRLightEstimationFeature)
- [`XRPassthroughFeature`](https://developer.android.com/develop/xr/unity/reference/class/Google/XR/Extensions/XRPassthroughFeature)
- [`XRTrackableFeature`](https://developer.android.com/develop/xr/unity/reference/class/Google/XR/Extensions/XRTrackableFeature)
- [`XRObjectTrackingFeature`](https://developer.android.com/develop/xr/unity/reference/class/Google/XR/Extensions/XRObjectTrackingFeature)

### android.permission.SCENE_UNDERSTANDING_FINE

Depth textures; scene meshing; cubemap light estimation; depth raycasting and
spatial annotations.

### Jetpack XR SDK

N/A

### OpenXR Extensions

- [`XR_ANDROID_depth_texture`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture)
- [`XR_ANDROID_light_estimation_cubemap`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap)
- [`XR_ANDROID_scene_meshing`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_scene_meshing)
- [`XR_ANDROID_spatial_annotation_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking)
- [`XR_ANDROID_spatial_discovery_raycast`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast)

### Unity Features

- [`XRDepthTextureFeature`](https://developer.android.com/develop/xr/unity/reference/class/Google/XR/Extensions/XRDepthTextureFeature)

### android.permission.ACCESS_FINE_LOCATION

Precise Earth-relative location and orientation for Geospatial tracking and
anchors.

### Jetpack XR SDK

N/A

### OpenXR Extensions

- [`XR_ANDROID_geospatial`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial)
- [`XR_ANDROID_geospatial_anchor`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor)

### Unity Features

N/A