---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/check-spatial-capabilities
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/check-spatial-capabilities
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Spatial capabilities can vary across devices and change as users interact with
your app or the system. They can even be changed by your app itself---for example,
moving into Home Space or Full Space. To avoid issues, your app needs to check
for spatial capabilities to determine which APIs are supported in the current
environment.

## Check for spatial capabilities using Jetpack Compose for XR

Jetpack Compose for XR creates a Composition Local for checking spatial
capabilities. Use this to check whether spatial UI, spatial audio, environments,
passthrough, or 3D content is enabled.

You can use [`LocalSpatialCapabilities.current`](https://developer.android.com/reference/kotlin/androidx/xr/compose/platform/package-summary#LocalSpatialCapabilities()) to check if the following
spatial capabilities are currently available:

- [`isSpatialUiEnabled`](https://developer.android.com/reference/kotlin/androidx/xr/compose/platform/SpatialCapabilities#isSpatialUiEnabled()): Indicates whether the application may create spatial UI elements (for example, `SpatialPanel`).
- [`isContent3dEnabled`](https://developer.android.com/reference/kotlin/androidx/xr/compose/platform/SpatialCapabilities#isContent3dEnabled()): Indicates whether the application may create 3D objects.
- [`isAppEnvironmentEnabled`](https://developer.android.com/reference/kotlin/androidx/xr/compose/platform/SpatialCapabilities#isAppEnvironmentEnabled()): Indicates whether the application may set the environment.
- [`isPassthroughControlEnabled`](https://developer.android.com/reference/kotlin/androidx/xr/compose/platform/SpatialCapabilities#isPassthroughControlEnabled()): Indicates whether the application may control the passthrough state.
- [`isSpatialAudioEnabled`](https://developer.android.com/reference/kotlin/androidx/xr/compose/platform/SpatialCapabilities#isSpatialAudioEnabled()): Indicates whether the application may use spatial audio.

The following example shows how to check if spatial UI is enabled:


```kotlin
if (LocalSpatialCapabilities.current.isSpatialUiEnabled) {
    Subspace {
        SpatialPanel(
            modifier = SubspaceModifier
                .width(1488.dp)
                .fillMaxHeight()
        ) {
            AppContent()
        }
    }
} else {
    AppContent()
}
```

<br />

## Check for spatial capabilities using SceneCore

When using the SceneCore library, you'll have to create a [session](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-session). Once
the session is created, use [`spatialCapabilities`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/Scene#spatialCapabilities()) from the session's
[`scene`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/Scene) to query which spatial capabilities are currently available.

- [`SPATIAL_3D_CONTENT`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialCapability#SPATIAL_3D_CONTENT()): The activity can create 3D contents.
- [`APP_ENVIRONMENT`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialCapability#APP_ENVIRONMENT()): The activity can set its own environment.
- [`EMBED_ACTIVITY`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialCapability#EMBED_ACTIVITY()): The activity can spatially embed another activity.
- [`PASSTHROUGH_CONTROL`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialCapability#PASSTHROUGH_CONTROL()): The activity can enable or disable passthrough.
- [`SPATIAL_AUDIO`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialCapability#SPATIAL_AUDIO()): The activity can use spatial audio.
- [`SPATIAL_UI`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialCapability#SPATIAL_UI()): The activity can spatialize itself (for example, adding a spatial panel).

You can also choose to subscribe to a callback,
[`addSpatialCapabilitiesChangedListener`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/Scene#addSpatialCapabilitiesChangedListener(java.util.function.Consumer)) that notifies you when spatial
capabilities have changed.


```kotlin
// Example 1: check if enabling passthrough mode is allowed
if (xrSession.scene.spatialCapabilities.contains(
        SpatialCapability.PASSTHROUGH_CONTROL
    )
) {
    xrSession.scene.spatialEnvironment.preferredPassthroughOpacity = 1f
}
// Example 2: multiple capability flags can be checked simultaneously:
if (xrSession.scene.spatialCapabilities.contains(SpatialCapability.PASSTHROUGH_CONTROL) &&
    xrSession.scene.spatialCapabilities.contains(SpatialCapability.SPATIAL_3D_CONTENT)
) {
    // ...
}
```

<br />

## Use blend mode to check the device's display capabilities

On Android XR, XR headsets and wired XR glasses have varying hardware
capabilities, especially concerning their display type. You might need to adapt
the colors of your app's UI and rendered objects to maximize visibility, which
might be influenced by the display type and the preferred blend mode employed by the
device. The [`DisplayBlendMode`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/XrDevice.DisplayBlendMode) API provides the device's blend mode
capability for rendering. Use this API to determine how virtual content is
added to the real world.

Here are some of the blend mode types to be aware of:

- [`ADDITIVE`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/XrDevice.DisplayBlendMode#ADDITIVE()): Virtual content is added to the real world by adding the pixel values for each of Red, Green, and Blue components. Alpha is ignored, and black pixels appear transparent.
- [`ALPHA_BLEND`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/XrDevice.DisplayBlendMode#ALPHA_BLEND()): Virtual content is added to the real world by alpha blending the pixel values based on the Alpha component.
- [`NO_DISPLAY`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/XrDevice.DisplayBlendMode#NO_DISPLAY()): Blending is not supported on the device.

Use `XrDevice.getCurrentDevice(session).getPreferredDisplayBlendMode()` from the
[Jetpack XR Runtime library](https://developer.android.com/jetpack/androidx/releases/xr-runtime) to check what type of blend mode is being used
and make adjustments as needed.

## See also

- [Create a session](https://developer.android.com/develop/xr/jetpack-xr-sdk/check-spatial-capabilities)
- [Transition between HSM and FSM](https://developer.android.com/develop/xr/jetpack-xr-sdk/transition-home-space-to-full-space)
- [Add spatial environments to your app](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-environments)
- [Add 3D models to your app](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models)