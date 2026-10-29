---
title: https://developer.android.com/develop/xr/openxr/get-started
url: https://developer.android.com/develop/xr/openxr/get-started
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Before you start building with supported OpenXR extensions or with a supported
engine, review the manifest configuration and permission requirements in the
following sections to make sure your app is configured for XR development.

## Configure your app's manifest file

As with other Android app projects, your Android XR app must have an
`AndroidManifest.xml` file with specific manifest settings. The manifest file
describes essential information about your app to the Android build tools, the
Android operating system, and Google Play. See the [app manifest overview
guide](https://developer.android.com/guide/topics/manifest/manifest-intro) for more information.

> [!NOTE]
> **Note:** While apps built with [Unity](https://developer.android.com/develop/xr/unity), [Unreal Engine](https://developer.android.com/develop/xr/unreal), or [Godot](https://developer.android.com/develop/xr/godot) for Android XR build on top of OpenXR, you don't need to add most of these manifest elements or attributes manually if you use the official Android XR plugins for those engines. The engine plugins and export presets configure the manifest for your app based on your project and build settings.

For [XR differentiated apps](https://developer.android.com/docs/quality-guidelines/android-xr#android-xr-differentiated), your manifest file
must contain the following elements and attributes:

### PROPERTY_XR_ACTIVITY_START_MODE property

The `android:name="android.window.PROPERTY_XR_ACTIVITY_START_MODE"` property
lets the system know that an activity should be launched in a specific mode when
the activity is started.

This property has the following values:

- `XR_ACTIVITY_START_MODE_FULL_SPACE_UNMANAGED` (OpenXR only)

#### XR_ACTIVITY_START_MODE_FULL_SPACE_UNMANAGED

Apps built with OpenXR launch in Full Space and must use
`XR_ACTIVITY_START_MODE_FULL_SPACE_UNMANAGED` start mode. Unmanaged Full Space
signals to Android XR the app uses OpenXR.

> [!NOTE]
> **Note:** If you use one of the [Android XR packages for Unity](https://developer.android.com/develop/xr/unity), your app will also launch in Full Space. However, you don't need to add this to your manifest manually. The Unity packages create the manifest for your app based on your project and build settings.


    <manifest ... >

       <application ... >
           <property
               android:name="android.window.PROPERTY_XR_ACTIVITY_START_MODE"
               android:value="XR_ACTIVITY_START_MODE_FULL_SPACE_UNMANAGED" />
           <activity
               android:name="com.example.myapp.MainActivity" ... >

               <intent-filter>
                   <action android:name="android.intent.action.MAIN" />

                   <category android:name="android.intent.category.LAUNCHER" />
                   <category android:name="org.khronos.openxr.intent.category.IMMERSIVE_HMD" />
               </intent-filter>
           </activity>
       </application>
    </manifest>

### PROPERTY_XR_BOUNDARY_TYPE_RECOMMENDED property

The `android:name="android.window.PROPERTY_XR_BOUNDARY_TYPE_RECOMMENDED"`
property indicates that the application should be launched with a specific type
of boundary. Your app needs to specify
[`XR_BOUNDARY_TYPE_LARGE`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/manifest/package-summary#XR_BOUNDARY_TYPE_LARGE()) if it's designed to let
users move around their physical space. Specifying
[`XR_BOUNDARY_TYPE_NO_RECOMMENDATION`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/manifest/package-summary#XR_BOUNDARY_TYPE_NO_RECOMMENDATION()) provides no
recommendations for the type of safety boundary, so the system uses the type
that is already in use.

    <manifest ... >

       <application ... >
           <property
               android:name="android.window.PROPERTY_XR_BOUNDARY_TYPE_RECOMMENDED"
               android:value="XR_BOUNDARY_TYPE_LARGE" />
       </application>
    </manifest>

### Spatial container properties

If your app uses the [`XR_EXT_spatial_container`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_container)
extension (introduced in Spatial API Level 4) to present content in bounded 3D
volumes or 2D panels in addition to full immersive views, you can declare the
following manifest properties at the `<activity>` or `<application>` level to
provide launch hints to the runtime:

- `org.khronos.openxr.PROPERTY_ACTIVITY_HINT_XR_SPATIAL_CONTAINER_USED_BOUNDS_MODES`:
  Specifies the bounds modes used by the activity, separated by `|`.

  Valid values are:
  - `"2d_panel"`
  - `"bounded"`
  - `"immersive"`
- `org.khronos.openxr.PROPERTY_ACTIVITY_HINT_XR_SPATIAL_CONTAINER_INITIAL_BOUNDS_MODE`:
  Specifies the initial bounds mode of the activity when launched.

  Valid values are:
  - `XR_SPATIAL_CONTAINER_INITIAL_BOUNDS_MODE_BOUNDED`
  - `XR_SPATIAL_CONTAINER_INITIAL_BOUNDS_MODE_IMMERSIVE`
  - `XR_SPATIAL_CONTAINER_INITIAL_BOUNDS_MODE_UNDEFINED`

> [!NOTE]
> **Note:** These properties replace the `<category android:name="org.khronos.openxr.intent.category.IMMERSIVE_HMD" />` intent filter category when using `XR_EXT_spatial_container`.

    <manifest ... >

       <application ... >
           <activity
               android:name="com.example.myapp.MainActivity" ... >
               <property
                   android:name="org.khronos.openxr.PROPERTY_ACTIVITY_HINT_XR_SPATIAL_CONTAINER_USED_BOUNDS_MODES"
                   android:value="bounded|immersive" />
               <property
                   android:name="org.khronos.openxr.PROPERTY_ACTIVITY_HINT_XR_SPATIAL_CONTAINER_INITIAL_BOUNDS_MODE"
                   android:value="XR_SPATIAL_CONTAINER_INITIAL_BOUNDS_MODE_BOUNDED" />
           </activity>
       </application>
    </manifest>

### \<uses-native-library\> OpenXR

OpenXR applications must declare the use of the native OpenXR library to
successfully load its runtime. Without this
[declaration](https://developer.android.com/guide/topics/manifest/uses-native-library-element), the runtime fails to load.

    <manifest ... >

        <application ... >

        <uses-native-library android:name="libopenxr.google.so" android:required="false" />

           <activity
               android:name="com.example.myapp.MainActivity" ... >

               <intent-filter>
                   <action android:name="android.intent.action.MAIN" />

                   <category android:name="android.intent.category.LAUNCHER" />
               </intent-filter>
            </activity>
        </application>
    </manifest>

### PackageManager features for XR apps

When you
[distribute apps through the Google Play Store](https://developer.android.com/develop/xr/package-and-distribute),
you can specify required hardware or software features in the app manifest. The
[`uses-feature`](https://developer.android.com/guide/topics/manifest/uses-feature-element) element allows the Play Store to
appropriately filter apps shown to users.

The following features are specific to XR-differentiated apps.

#### android.software.xr.api.openxr

Apps that target the Android XR platform and are built with OpenXR or Unity must
include this feature in the app manifest with the `android:required` attribute
set to `true`.

Apps that use the
[Android XR Extensions Package for Unity](https://developer.android.com/develop/xr/unity#android-xr-extensions-unity) version
1.0.0 or higher or the
[Unity OpenXR: Android XR Package](https://developer.android.com/develop/xr/unity#unity-openxr) version
0.5.0-exp.1 or higher don't have to add this element manually to the app
manifest. These two packages will inject this element into the app manifest for
you.

Devices may specify a version for this feature, which indicates the highest
version of OpenXR supported by the device. The higher 16 bits represent the
major number, and the lower 16 bits represent the minor number. For example, to
specify OpenXR version 1.1, the value would be set to `"0x00010001"`.

Apps can use the feature version to indicate a minimum version of OpenXR that
the app requires. For example, if your app requires OpenXR version 1.1 support,
declare the following feature:

    <uses-feature android:name="android.software.xr.api.openxr"
        android:version="0x00010001"
        android:required="true" />

#### android.software.xr.api.spatial

OpenXR apps that require extensions introduced in a specific Android XR
[Spatial API version](https://developer.android.com/reference/kotlin/androidx/xr/runtime/SpatialApiVersions) can declare the
`android.software.xr.api.spatial` feature with `android:version` set to the
minimum required Spatial API level (such as `"1"`, `"2"`, `"3"`, or `"4"`). See
[Build with supported OpenXR extensions](https://developer.android.com/develop/xr/openxr/extensions) to check the
Spatial API version required for each extension.

    <!-- Indicates that the app requires Android XR Spatial API Level 4 or higher. -->
    <uses-feature android:name="android.software.xr.api.spatial"
        android:version="4"
        android:required="true" />

#### android.hardware.xr.input.controller

This feature indicates that the app requires input from a high precision, 6DoF
(degrees of freedom) motion controller to function correctly. If your app
supports controllers and can't function without them, set the value to `true`.
If your app supports controllers but can operate without them, set it to
`false`.

> [!NOTE]
> **Note:** 6DoF motion controllers are a pair of hardware controllers, one for each hand. Each controller is tracked independently in space through six degrees of freedom - both linear and rotational movements. These controllers typically have several hardware buttons, including a trigger as well as haptic feedback.

    <!-- Sets android:required to true, indicating that your app can't function on devices without controllers. -->
    <uses-feature android:name="android.hardware.xr.input.controller" android:required="true" />

#### android.hardware.xr.input.hand_tracking

This flag indicates that the app requires high fidelity hand tracking to
function correctly, including position, orientation, and velocity of joints in
the user's hand. If your app supports hand tracking and can't function without
it, set the value to `true`. If your app supports hand tracking, but can operate
without it, set it to `false`.

> [!NOTE]
> **Note:** This flag is not required for detecting basic gestures such as pinching, poking, aiming, and gripping.

    <!-- Sets android:required to true, indicating that your app can't function on devices without hand tracking. -->
    <uses-feature android:name="android.hardware.xr.input.hand_tracking" android:required="true" />

#### android.hardware.xr.input.eye_tracking

This flag indicates that the app requires high-fidelity eye tracking for input
to function correctly. If your app supports eye tracking for input and can't
function without it, set the value to `true`. If your app supports eye tracking
for input, but can operate without it, set it to `false`.

    <!-- Sets android:required to true, indicating that your app can't function on devices without eye tracking. -->
    <uses-feature android:name="android.hardware.xr.input.eye_tracking" android:required="true" />

#### android.hardware.xr.input.face_tracking

This flag indicates that the app requires face tracking hardware to function
correctly. If your app supports face tracking and can't function without it, set
the value to `true`. If your app supports face tracking, but can operate without
it, set it to `false`.

    <!-- Sets android:required to true, indicating that your app can't function on devices without face tracking. -->
    <uses-feature android:name="android.hardware.xr.input.face_tracking" android:required="true" />

#### android.hardware.location.gps

This flag indicates that the app uses precise GPS location on the device, such
as when using geospatial OpenXR extensions
([`XR_ANDROID_geospatial`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial) and
[`XR_ANDROID_geospatial_anchor`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor)). Set
`android:required` to `true` if your app can't function without GPS hardware, or
`false` if it can operate without it.

    <uses-feature android:name="android.hardware.location.gps" android:required="false" />

> [!NOTE]
> **Note:** Hand tracking, eye tracking, face tracking, body tracking, scene understanding, and location are privacy-sensitive capabilities and require apps to request runtime permissions. See [Understand permissions for
> XR](https://developer.android.com/develop/xr/permissions) for more information on declaring and requesting permissions.

## Understand permissions for OpenXR

Many OpenXR extensions access privacy-sensitive sensor data and capabilities. To
use these extensions, your app must both [declare the required
`<uses-permission>` elements](https://developer.android.com/training/permissions/declaring#add-to-manifest) in its
`AndroidManifest.xml` file and [request dangerous permissions at
runtime](https://developer.android.com/training/permissions/requesting) before calling the corresponding OpenXR
functions.

    <manifest ... >
        <!-- Example dangerous permissions required by specific OpenXR extensions -->
        <uses-permission android:name="android.permission.SCENE_UNDERSTANDING_COARSE" />
        <uses-permission android:name="android.permission.HAND_TRACKING" />
        ...
    </manifest>

The following table summarizes the dangerous Android permissions required by
supported OpenXR extensions on Android XR. For full details on XR permissions
across all SDKs, see [Understand permissions for XR](https://developer.android.com/develop/xr/permissions).

| Permission | Capabilities | OpenXR extensions |
|---|---|---|
| [`android.permission.EYE_TRACKING_COARSE`](https://developer.android.com/reference/android/Manifest.permission#EYE_TRACKING_COARSE) | Low-precision eye pose, status, and orientation (such as for avatars). | - [`XR_ANDROID_eye_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking) (`xrGetCoarseTrackingEyesInfoANDROID`) |
| [`android.permission.EYE_TRACKING_FINE`](https://developer.android.com/reference/android/Manifest.permission#EYE_TRACKING_FINE) | High-precision eye gaze for selection, input, interactions, and eye-tracked foveated rendering. | - [`XR_ANDROID_eye_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_eye_tracking) (`xrGetFineTrackingEyesInfoANDROID`) - [`XR_EXT_eye_gaze_interaction`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_eye_gaze_interaction) - [`XR_META_foveation_eye_tracked`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_META_foveation_eye_tracked) - [`XR_VARJO_foveated_rendering`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_VARJO_foveated_rendering) |
| [`android.permission.FACE_TRACKING`](https://developer.android.com/reference/android/Manifest.permission#FACE_TRACKING) | Tracking facial blend shapes and rendering facial expressions. | - [`XR_ANDROID_face_tracking`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_face_tracking) - [`XR_ANDROID_face_tracking_data_source`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source) |
| [`android.permission.RECORD_AUDIO`](https://developer.android.com/reference/android/Manifest.permission#RECORD_AUDIO) | Audio input for audio-driven face tracking data sources. | - [`XR_ANDROID_face_tracking_data_source`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_face_tracking_data_source) |
| [`android.permission.HAND_TRACKING`](https://developer.android.com/reference/android/Manifest.permission#HAND_TRACKING) | Tracking hand joint poses, velocities, aim state, and hand mesh representation. | - [`XR_ANDROID_hand_mesh`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_hand_mesh) - [`XR_EXT_hand_tracking`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_hand_tracking) - [`XR_FB_hand_tracking_aim`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_hand_tracking_aim) - [`XR_FB_hand_tracking_mesh`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_FB_hand_tracking_mesh) |
| [`android.permission.BODY_TRACKING`](https://developer.android.com/reference/android/Manifest.permission#BODY_TRACKING) | Tracking body joint poses and skeleton proportions. | - [`XR_ANDROID_body_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_body_tracking) |
| [`android.permission.SCENE_UNDERSTANDING_COARSE`](https://developer.android.com/reference/android/Manifest.permission#SCENE_UNDERSTANDING_COARSE) | Plane tracking, object tracking, image/marker/QR code tracking, anchors, persistence, raycasting against trackables, light estimation, and passthrough meshes. | - [`XR_ANDROID_anchor_sharing_export`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_anchor_sharing_export) - [`XR_ANDROID_composition_layer_passthrough_mesh`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_composition_layer_passthrough_mesh) - [`XR_ANDROID_device_anchor_persistence`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_device_anchor_persistence) - [`XR_ANDROID_light_estimation`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_light_estimation) - [`XR_ANDROID_raycast`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_raycast) - [`XR_ANDROID_spatial_anchor_space`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_anchor_space) - [`XR_ANDROID_spatial_component_subsumed_by`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_component_subsumed_by) - [`XR_ANDROID_spatial_discovery_bounds`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_bounds) - [`XR_ANDROID_spatial_entity_bound_anchor`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_entity_bound_anchor) - [`XR_ANDROID_spatial_object_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_object_tracking) - [`XR_ANDROID_trackables`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_trackables) - [`XR_ANDROID_trackables_image`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_image) - [`XR_ANDROID_trackables_marker`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_marker) - [`XR_ANDROID_trackables_object`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_ANDROID_trackables_object) - [`XR_ANDROID_trackables_qr_code`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_qr_code) - [`XR_EXT_spatial_anchor`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_anchor) - [`XR_EXT_spatial_image_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_image_tracking) - [`XR_EXT_spatial_marker_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_marker_tracking) - [`XR_EXT_spatial_mesh_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_mesh_tracking) - [`XR_EXT_spatial_object_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_object_tracking) - [`XR_EXT_spatial_persistence`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_persistence) - [`XR_EXT_spatial_persistence_operations`](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_spatial_persistence_operations) - [`XR_EXT_spatial_plane_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_EXT_spatial_plane_tracking) |
| [`android.permission.SCENE_UNDERSTANDING_FINE`](https://developer.android.com/reference/android/Manifest.permission#SCENE_UNDERSTANDING_FINE) | Depth textures, scene meshing, cubemap light estimation, depth raycasting, and spatial annotations. | - [`XR_ANDROID_depth_texture`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture) - [`XR_ANDROID_light_estimation_cubemap`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation_cubemap) - [`XR_ANDROID_scene_meshing`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_scene_meshing) - [`XR_ANDROID_spatial_annotation_tracking`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_annotation_tracking) - [`XR_ANDROID_spatial_discovery_raycast`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_spatial_discovery_raycast) |
| [`android.permission.ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION) | Precise Earth-relative location and orientation for Geospatial tracking and anchors. | - [`XR_ANDROID_geospatial`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial) - [`XR_ANDROID_geospatial_anchor`](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_geospatial_anchor) |

## Next steps

Now that you've finished configuring your app's manifest and reviewing important
information, explore ways that you can build with OpenXR:

- [Build with supported OpenXR extensions](https://developer.android.com/develop/xr/openxr/extensions)
- [Build with supported engines](https://developer.android.com/develop/xr/openxr#supported-engines)