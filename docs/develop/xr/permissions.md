---
title: Understand permissions for XR  |  Android XR  |  Android Developers
url: https://developer.android.com/develop/xr/permissions
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Understand permissions for XR Stay organized with collections Save and categorize content based on your preferences.




Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/xr-headsets-icon.svg)


XR Headsets

![](/static/images/develop/xr/xr-glasses-icon.svg)


Wired XR Glasses

![](/static/images/develop/xr/ai-glasses-icon.svg)


AI Glasses

[Learn about XR device types →](/develop/xr/devices)

Just like apps on mobile devices and other form factors, some capabilities
offered by XR apps require your app to [declare permissions](/training/permissions/declaring#add-to-manifest)
in your app's AndroidManifest file. In the case of dangerous permissions, your
app may need to [request runtime permissions](/training/permissions/requesting). Read [Permissions
on Android](/guide/topics/permissions/overview) and [permission best practices](/training/permissions/usage-notes) for more
in-depth information.

The following permissions can be used by XR apps. All of the permissions in this
section are considered dangerous permissions, so you must declare them in your
app manifest **and** request them at runtime.

### android.permission.EYE\_TRACKING\_COARSE

Representing the user's eye pose, status, and orientation, such as for use with
avatars. Use this permission when low-precision eye tracking data is needed.

### Jetpack XR SDK

N/A

### OpenXR Extensions

* [`XR_ANDROID_eye_tracking`](/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking)
* [`xrGetCoarseTrackingEyesInfoANDROID`](/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking)

### Unity Features

* [Android XR: AR Face](https://docs.unity3d.com/Packages/com.unity.xr.androidxr-openxr@0.4/manual/features/faces.html)

### android.permission.EYE\_TRACKING\_FINE

Eye gaze for selection, input, and interactions.

### Jetpack XR SDK

N/A

### OpenXR Extensions

* [`XR_EXT_eye_gaze_interaction`](https://registry.khronos.org/OpenXR/specs/1.0/html/xrspec.html#XR_EXT_eye_gaze_interaction)
* [`xrGetFineTrackingEyesInfoANDROID`](/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking)

### Unity Features

* [Eye Gaze Interaction](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.13/manual/features/eyegazeinteraction.html)

### android.permission.FACE\_TRACKING

Tracking and rendering facial expressions.

### Jetpack XR SDK

N/A

### OpenXR Extensions

* [`XR_ANDROID_face_tracking`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRFaceTrackingFeature)

### Unity Features

* [`XRFaceTrackingFeature`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRFaceTrackingFeature)

### android.permission.HAND\_TRACKING

Tracking hand joint poses and angular and linear velocities; Using a mesh
representation of the user's hands.

**Note:** This permission is not required for detecting basic gestures such as
pinching, poking, aiming, and gripping.

### Jetpack XR SDK

* [Hand state and joint poses](/develop/xr/jetpack-xr-sdk/work-with-hands)

### OpenXR Extensions

* [`XR_ANDROID_hand_mesh`](/develop/xr/openxr/extensions/XR_ANDROID_hand_mesh)
* [`XR_EXT_hand_tracking`](https://registry.khronos.org/OpenXR/specs/1.0/html/xrspec.html#XR_EXT_hand_tracking)

### Unity Features

* [`XR Hands`](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.5/manual/index.html)
* [`XRHandMeshFeature`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRHandMeshFeature)

### android.permission.SCENE\_UNDERSTANDING\_COARSE

Light estimation; projecting passthrough onto mesh surfaces; performing raycasts
against trackables in the environment; plane tracking; object tracking;
persistent anchors.

### Jetpack XR SDK

* [`PanelEntity`](/develop/xr/jetpack-xr-sdk/ui-compose#create-spatial)
* [Plane tracking](/develop/xr/jetpack-xr-sdk/work-with-arcore#retrieve-state)
* [Hit testing](/develop/xr/jetpack-xr-sdk/work-with-arcore#perform-hit-test)
* [Anchor persistence](/develop/xr/jetpack-xr-sdk/work-with-arcore#persist-anchor)

### OpenXR Extensions

* [`XR_ANDROID_anchor_persistence`](/develop/xr/openxr/extensions/XR_ANDROID_device_anchor_persistence)
* [`XR_ANDROID_light_estimation`](/develop/xr/openxr/extensions/XR_ANDROID_light_estimation)
* [`XR_ANDROID_composition_layer_passthrough_mesh`](/develop/xr/openxr/extensions/XR_ANDROID_composition_layer_passthrough_mesh)
* [`XR_ANDROID_raycast`](/develop/xr/openxr/extensions/XR_ANDROID_raycast)
* [`XR_ANDROID_trackables`](/develop/xr/openxr/extensions/XR_ANDROID_trackables)
* [`XR_ANDROID_trackables_object`](/develop/xr/openxr/extensions/XR_ANDROID_trackables_object)

### Unity Features

* [`XRAnchorFeature`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRAnchorFeature)
* [`XRLightEstimationFeature`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRLightEstimationFeature)
* [`XRPassthroughFeature`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRPassthroughFeature)
* [`XRTrackableFeature`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRTrackableFeature)
* [`XRObjectTrackingFeature`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRObjectTrackingFeature)

### android.permission.SCENE\_UNDERSTANDING\_FINE

Depth texture.

### Jetpack XR SDK

N/A

### OpenXR Extensions

* [`XR_ANDROID_depth_texture`](/develop/xr/openxr/extensions/XR_ANDROID_depth_texture)

### Unity Features

* [`XRDepthTextureFeature`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRDepthTextureFeature)