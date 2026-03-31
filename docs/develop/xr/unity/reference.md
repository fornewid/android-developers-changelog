---
title: Android XR Extensions for Unity  |  Android XR for Unity  |  Android Developers
url: https://developer.android.com/develop/xr/unity/reference
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Unity](https://developer.android.com/develop/xr/unity)
* [Guides](https://developer.android.com/develop/xr/get-started)

Stay organized with collections

Save and categorize content based on your preferences.



# Android XR Extensions for Unity

Reference documentation for the Android XR Extensions for Unity

| Pages | |
| --- | --- |
| [`ARTrackedImageExtensions`](/develop/xr/unity/reference/class/Google/XR/Extensions/ARTrackedImageExtensions) | Extensions to AR Foundation's `ARTrackedImage` class. |
| [`ARTrackedObjectExtensions`](/develop/xr/unity/reference/class/Google/XR/Extensions/ARTrackedObjectExtensions) | Extensions to AR Foundation's `ARTrackedObject` class. |
| [`AndroidXRHumanBodySubsystem`](/develop/xr/unity/reference/class/Google/XR/Extensions/AndroidXRHumanBodySubsystem) | The Android XR implementation of the `XRHumanBodySubsystem` so it can work seamlessly with `ARHumanBodyManager`. |
| [`AndroidXRImageTrackingSubsystem`](/develop/xr/unity/reference/class/Google/XR/Extensions/AndroidXRImageTrackingSubsystem) | The Android XR implementation of the XRImageTrackingSubsystem so it can work seamlessly with ARTrackedImageManager. |
| [`AndroidXRMouseInteractionProfile`](/develop/xr/unity/reference/class/Google/XR/Extensions/AndroidXRMouseInteractionProfile) | This OpenXRInteractionFeature enables the use of Android XR Mouse interaction profile in OpenXR. |
| [`AndroidXRMouse`](/develop/xr/unity/reference/class/Google/XR/Extensions/AndroidXRMouseInteractionProfile/AndroidXRMouse) | An Input device based on Android XR Mouse interaction profile. |
| [`AndroidXRMouseUsages`](/develop/xr/unity/reference/class/Google/XR/Extensions/AndroidXRMouseInteractionProfile/AndroidXRMouseUsages) | Tags that can be used with InputDevice.TryGetFeatureValue to get mouse related input features. |
| [`AndroidXRObjectTrackingSubsystem`](/develop/xr/unity/reference/class/Google/XR/Extensions/AndroidXRObjectTrackingSubsystem) | The Android XR implementation of the `XRObjectTrackingSubsystem` so it can work seamlessly with `ARTrackedObjectManager`. |
| [`AndroidXRPermissionExtensions`](/develop/xr/unity/reference/class/Google/XR/Extensions/AndroidXRPermissionExtensions) | Helper class for `AndroidXRPermission`. |
| [`AndroidXRPermissionUtil`](/develop/xr/unity/reference/class/Google/XR/Extensions/AndroidXRPermissionUtil) | Utility component to help manage runtime permission requests. |
| [`AndroidXRRuntimeImageLibrary`](/develop/xr/unity/reference/class/Google/XR/Extensions/AndroidXRRuntimeImageLibrary) | Constructs a RuntimeReferenceImageLibrary which stores reference images for Marker Tracking and QR Code trackng at Android XR devices. |
| [`AndroidXRSessionSubsystem`](/develop/xr/unity/reference/class/Google/XR/Extensions/AndroidXRSessionSubsystem) | The Android XR implementation of the `XRSessionSubsystem` so it can work seamlessly with `ARSession`. |
| [`XRAvatarSkeletonJointIDUtility`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRAvatarSkeletonJointIDUtility) | Utility class for [XRAvatarSkeletonJointID](/develop/xr/unity/reference/namespace/Google/XR/Extensions#xravatarskeletonjointid). |
| [`XRBodyTrackingFeature`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRBodyTrackingFeature) | This `OpenXRInteractionFeature` configures Android XR extensions `XR_ANDROIDX_body_tracking` at runtime and provides `XRHumanBodySubsystem` implementation that works on Android XR platform. |
| [`XREnvironmentBlendModeFeature`](/develop/xr/unity/reference/class/Google/XR/Extensions/XREnvironmentBlendModeFeature) | This `OpenXRInteractionFeature` configures  `XrEnvironmentBlendMode` `at OpenXR runtime.` |
| [`XRFaceState`](/develop/xr/unity/reference/struct/Google/XR/Extensions/XRFaceState) | This struct contains the blendshape parameter weights, current status of the face tracker and face joint poses. |
| [`XRFaceTrackingFeature`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRFaceTrackingFeature) | This `OpenXRInteractionFeature` configures new extension |
| [`XRFaceTrackingManager`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRFaceTrackingManager) | This class provides the current eye information. |
| [`XRFoveationFeature`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRFoveationFeature) | This `OpenXRInteractionFeature` configures the  `XR_FB_foveation` `extension at OpenXR runtime.` |
| [`XRHandMeshFeature`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRHandMeshFeature) | This feature provides access to the `XR_ANDROID_hand_mesh` extension. |
| [`XRHumanBodyProportions`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRHumanBodyProportions) | Defines the human body proportions to be used for computing the rest pose skeleton. |
| [`XRMarkerDatabase`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRMarkerDatabase) | A marker database is a collection of [XRMarkerDatabaseEntry](/develop/xr/unity/reference/struct/Google/XR/Extensions/XRMarkerDatabaseEntry#structGoogle_1_1XR_1_1Extensions_1_1XRMarkerDatabaseEntry) which stores marker information used to configure marker tracking at runtime when [XRMarkerTrackingFeature](/develop/xr/unity/reference/class/Google/XR/Extensions/XRMarkerTrackingFeature#classGoogle_1_1XR_1_1Extensions_1_1XRMarkerTrackingFeature) is enabled. |
| [`XRMarkerDatabaseEntry`](/develop/xr/unity/reference/struct/Google/XR/Extensions/XRMarkerDatabaseEntry) | Represents an entry in an [XRMarkerDatabase](/develop/xr/unity/reference/class/Google/XR/Extensions/XRMarkerDatabase#classGoogle_1_1XR_1_1Extensions_1_1XRMarkerDatabase) with the specialized information that can be converted into a marker XRReferenceImage, then used at ARTrackedImageManager.referenceLibrary for runtime configuration. |
| [`XRMarkerTrackingFeature`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRMarkerTrackingFeature) | This OpenXRInteractionFeature configures Android XR extensions `XR_ANDROID_trackables` and `XR_ANDROID_trackables_marker` at runtime and provides XRImageTrackingSubsystem implementation that works on Android XR platform. |
| [`XRMeshSubsystemExtension`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRMeshSubsystemExtension) | Extensions to AR Foundation's `XRMeshSubsystem` class. |
| [`XRObjectTrackingFeature`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRObjectTrackingFeature) | This `OpenXRInteractionFeature` configures Android XR extensions `XR_ANDROID_trackables` and `XR_ANDROID_trackables_object` at runtime and provides XRObjectTrackingSubsystem implementation that works on Android XR platform. |
| [`XRPassthroughFeature`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRPassthroughFeature) | This `OpenXRInteractionFeature` configures the `XR_ANDROID_composition_layer_passthrough_mesh` and `XR_ANDROID_passthrough_camera_state` extensions at OpenXR runtime and provides passthrough geometry capabilities in the OpenXR platform. |
| [`XRPassthroughLayerData`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRPassthroughLayerData) | Example of defining a layer data script for a passthrough layer. |
| [`XRQrCodeTrackingFeature`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRQrCodeTrackingFeature) | This OpenXRInteractionFeature configures Android XR extensions `XR_ANDROID_trackables` and `XR_ANDROID_trackables_qr_code` at runtime and provides XRImageTrackingSubsystem implementation that works on Android XR platform. |
| [`XRSceneMeshingFeature`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRSceneMeshingFeature) | This feature provides access to the `XR_ANDROID_scene_meshing` extension. |
| [`XRSessionFeature`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRSessionFeature) | This `OpenXRInteractionFeature` provides Android XR session management for all extended Android XR features, and common session configurations. |
| [`XRSystemStateFeature`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRSystemStateFeature) | This [XRSystemStateFeature](/develop/xr/unity/reference/class/Google/XR/Extensions/XRSystemStateFeature#classGoogle_1_1XR_1_1Extensions_1_1XRSystemStateFeature) provides a function to query the system state information at runtime. |
| [`XRUnboundedRefSpaceFeature`](/develop/xr/unity/reference/class/Google/XR/Extensions/XRUnboundedRefSpaceFeature) | This `XRUnboundedRefSpaceFeature` makes the `UNBOUNDED` reference space available in this app and can be used by setting the `XRInputSubsystem` tracking origin mode. |
| [`XrSystemState`](/develop/xr/unity/reference/struct/Google/XR/Extensions/XrSystemState) | Contains system state information. |