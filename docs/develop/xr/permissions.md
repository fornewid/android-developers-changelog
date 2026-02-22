---
title: https://developer.android.com/develop/xr/permissions
url: https://developer.android.com/develop/xr/permissions
source: md.txt
---

<br />

<br />

Applicable XR devices  
This guidance helps you build experiences for these types of XR devices.  
[Learn about XR device types →](https://developer.android.com/develop/xr/devices)  
![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg)XR Headsets[](https://developer.android.com/develop/xr/devices#xr-headsets)  
![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg)Wired XR Glasses[](https://developer.android.com/develop/xr/devices#xr-glasses)  
![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg)AI Glasses[](https://developer.android.com/develop/xr/devices#ai-glasses)  
[Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Just like apps on mobile devices and other form factors, some capabilities offered by XR apps require your app to[declare permissions](https://developer.android.com/training/permissions/declaring#add-to-manifest)in your app's AndroidManifest file. In the case of dangerous permissions, your app may need to[request runtime permissions](https://developer.android.com/training/permissions/requesting). Read[Permissions on Android](https://developer.android.com/guide/topics/permissions/overview)and[permission best practices](https://developer.android.com/training/permissions/usage-notes)for more in-depth information.

The following permissions can be used by XR apps. All of the permissions in this section are considered dangerous permissions, so you must declare them in your app manifest**and**request them at runtime.

### android.permission.EYE_TRACKING_COARSE

Representing the user's eye pose, status, and orientation, such as for use with avatars. Use this permission when low-precision eye tracking data is needed.  

### Jetpack XR SDK

N/A

### OpenXR Extensions

- [`XR_ANDROID_eye_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking)
- [`xrGetCoarseTrackingEyesInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking)

### Unity Features

- [Android XR: AR Face](https://docs.unity3d.com/Packages/com.unity.xr.androidxr-openxr@0.4/manual/features/faces.html)

### android.permission.EYE_TRACKING_FINE

Eye gaze for selection, input, and interactions.  

### Jetpack XR SDK

N/A

### OpenXR Extensions

- [`XR_EXT_eye_gaze_interaction`](https://registry.khronos.org/OpenXR/specs/1.0/html/xrspec.html#XR_EXT_eye_gaze_interaction)
- [`xrGetFineTrackingEyesInfoANDROID`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking)

### Unity Features

- [Eye Gaze Interaction](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.13/manual/features/eyegazeinteraction.html)

### android.permission.FACE_TRACKING

Tracking and rendering facial expressions.  

### Jetpack XR SDK

N/A

### OpenXR Extensions

- [`XR_ANDROID_face_tracking`](https://developer.android.com/develop/xr/unity/reference/class/Google/XR/Extensions/XRFaceTrackingFeature)

### Unity Features

- [`XRFaceTrackingFeature`](https://developer.android.com/develop/xr/unity/reference/class/Google/XR/Extensions/XRFaceTrackingFeature)

### android.permission.HAND_TRACKING

Tracking hand joint poses and angular and linear velocities; Using a mesh representation of the user's hands.
**Note:** This permission is not required for detecting basic gestures such as pinching, poking, aiming, and gripping.  

### Jetpack XR SDK

- [Hand state and joint poses](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-hands)

### OpenXR Extensions

- [`XR_ANDROID_hand_mesh`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_hand_mesh)

- [`XR_EXT_hand_tracking`](https://registry.khronos.org/OpenXR/specs/1.0/html/xrspec.html#XR_EXT_hand_tracking)

### Unity Features

- [`XR Hands`](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.5/manual/index.html)

- [`XRHandMeshFeature`](https://developer.android.com/develop/xr/unity/reference/class/Google/XR/Extensions/XRHandMeshFeature)

### android.permission.SCENE_UNDERSTANDING_COARSE

Light estimation; projecting passthrough onto mesh surfaces; performing raycasts against trackables in the environment; plane tracking; object tracking; persistent anchors.  

### Jetpack XR SDK

- [`PanelEntity`](https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui#create-spatial)
- [Plane tracking](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-arcore#retrieve-state)
- [Hit testing](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-arcore#perform-hit-test)
- [Anchor persistence](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-arcore#persist-anchor)

### OpenXR Extensions

- [`XR_ANDROID_anchor_persistence`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_device_anchor_persistence)
- [`XR_ANDROID_light_estimation`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation)
- [`XR_ANDROID_composition_layer_passthrough_mesh`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh)
- [`XR_ANDROID_raycast`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_raycast)
- [`XR_ANDROID_trackables`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables)
- [`XR_ANDROID_trackables_object`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_object)

### Unity Features

- [`XRAnchorFeature`](https://developer.android.com/develop/xr/unity/reference/class/Google/XR/Extensions/XRAnchorFeature)
- [`XRLightEstimationFeature`](https://developer.android.com/develop/xr/unity/reference/class/Google/XR/Extensions/XRLightEstimationFeature)
- [`XRPassthroughFeature`](https://developer.android.com/develop/xr/unity/reference/class/Google/XR/Extensions/XRPassthroughFeature)
- [`XRTrackableFeature`](https://developer.android.com/develop/xr/unity/reference/class/Google/XR/Extensions/XRTrackableFeature)
- [`XRObjectTrackingFeature`](https://developer.android.com/develop/xr/unity/reference/class/Google/XR/Extensions/XRObjectTrackingFeature)

### android.permission.SCENE_UNDERSTANDING_FINE

Depth texture.  

### Jetpack XR SDK

N/A

### OpenXR Extensions

- [`XR_ANDROID_depth_texture`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture)

### Unity Features

- [`XRDepthTextureFeature`](https://developer.android.com/develop/xr/unity/reference/class/Google/XR/Extensions/XRDepthTextureFeature)