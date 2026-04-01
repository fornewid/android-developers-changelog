---
title: Check for spatial capabilities  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/check-spatial-capabilities
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Check for spatial capabilities Stay organized with collections Save and categorize content based on your preferences.



Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/xr-headsets-icon.svg)


XR Headsets

![](/static/images/develop/xr/xr-glasses-icon.svg)


Wired XR Glasses

[Learn about XR device types →](/develop/xr/devices)

Spatial capabilities can vary across devices and change as users interact with
your app or the system. They can even be changed by your app itself—for example,
moving into Home Space or Full Space. To avoid issues, your app needs to check
for spatial capabilities to determine which APIs are supported in the current
environment.

## Check for spatial capabilities using Jetpack Compose for XR

Jetpack Compose for XR creates a Composition Local for checking spatial
capabilities. Use this to check whether spatial UI, spatial audio, environments,
passthrough, or 3D content is enabled.

You can use [`LocalSpatialCapabilities.current`](/reference/kotlin/androidx/xr/compose/platform/package-summary#LocalSpatialCapabilities()) to check if the following
spatial capabilities are currently available:

* [`isSpatialUiEnabled`](/reference/kotlin/androidx/xr/compose/platform/SpatialCapabilities#isSpatialUiEnabled()): Indicates whether the application may create
  spatial UI elements (for example, `SpatialPanel`).
* [`isContent3dEnabled`](/reference/kotlin/androidx/xr/compose/platform/SpatialCapabilities#isContent3dEnabled()): Indicates whether the application may create 3D
  objects.
* [`isAppEnvironmentEnabled`](/reference/kotlin/androidx/xr/compose/platform/SpatialCapabilities#isAppEnvironmentEnabled()): Indicates whether the application may set
  the environment.
* [`isPassthroughControlEnabled`](/reference/kotlin/androidx/xr/compose/platform/SpatialCapabilities#isPassthroughControlEnabled()): Indicates whether the application may
  control the passthrough state.
* [`isSpatialAudioEnabled`](/reference/kotlin/androidx/xr/compose/platform/SpatialCapabilities#isSpatialAudioEnabled()): Indicates whether the application may use
  spatial audio.

The following example shows how to check if spatial UI is enabled:

```
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

SpatialCapabilities.kt
```

## Check for spatial capabilities using SceneCore

When using the SceneCore library, you'll have to create a [session](/develop/xr/jetpack-xr-sdk/add-session). Once
the session is created, use [`spatialCapabilities`](/reference/kotlin/androidx/xr/scenecore/Scene#spatialCapabilities()) from the session's
[`scene`](/reference/kotlin/androidx/xr/scenecore/Scene) to query which spatial capabilities are currently available.

* [`SPATIAL_3D_CONTENT`](/reference/kotlin/androidx/xr/scenecore/SpatialCapability#SPATIAL_3D_CONTENT()): The activity can create 3D
  contents.
* [`APP_ENVIRONMENT`](/reference/kotlin/androidx/xr/scenecore/SpatialCapability#APP_ENVIRONMENT()): The activity can set its own
  environment.
* [`EMBED_ACTIVITY`](/reference/kotlin/androidx/xr/scenecore/SpatialCapability#EMBED_ACTIVITY()): The activity can spatially
  embed another activity.
* [`PASSTHROUGH_CONTROL`](/reference/kotlin/androidx/xr/scenecore/SpatialCapability#PASSTHROUGH_CONTROL()): The activity can enable
  or disable passthrough.
* [`SPATIAL_AUDIO`](/reference/kotlin/androidx/xr/scenecore/SpatialCapability#SPATIAL_AUDIO()): The activity can use spatial
  audio.
* [`SPATIAL_UI`](/reference/kotlin/androidx/xr/scenecore/SpatialCapability#SPATIAL_UI()): The activity can spatialize itself (for
  example, adding a spatial panel).

You can also choose to subscribe to a callback,
[`addSpatialCapabilitiesChangedListener`](/reference/kotlin/androidx/xr/scenecore/Scene#addSpatialCapabilitiesChangedListener(java.util.function.Consumer)) that notifies you when spatial
capabilities have changed.

```
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

SpatialCapabilities.kt
```

## Use blend mode to check the device's display capabilities

On Android XR, XR headsets and wired XR glasses have varying hardware
capabilities, especially concerning their display type. You might need to adapt
the colors of your app's UI and rendered objects to maximize visibility, which
might be influenced by the display type and the preferred blend mode employed by the
device. The [`DisplayBlendMode`](/reference/kotlin/androidx/xr/runtime/XrDevice.DisplayBlendMode) API provides the device's blend mode
capability for rendering. Use this API to determine how virtual content is
added to the real world.

Here are some of the blend mode types to be aware of:

* [`ADDITIVE`](/reference/kotlin/androidx/xr/runtime/XrDevice.DisplayBlendMode#ADDITIVE()): Virtual content is added to the real world by adding the
  pixel values for each of Red, Green, and Blue components. Alpha is ignored, and
  black pixels appear transparent.
* [`ALPHA_BLEND`](/reference/kotlin/androidx/xr/runtime/XrDevice.DisplayBlendMode#ALPHA_BLEND()): Virtual content is added to the real world by alpha
  blending the pixel values based on the Alpha component.
* [`NO_DISPLAY`](/reference/kotlin/androidx/xr/runtime/XrDevice.DisplayBlendMode#NO_DISPLAY()): Blending is not supported on the device.

Use `XrDevice.getCurrentDevice(session).getPreferredDisplayBlendMode()` from the
[Jetpack XR Runtime library](/jetpack/androidx/releases/xr-runtime) to check what type of blend mode is being used
and make adjustments as needed.

## See also

* [Create a session](/develop/xr/jetpack-xr-sdk/check-spatial-capabilities)
* [Transition between HSM and FSM](/develop/xr/jetpack-xr-sdk/transition-home-space-to-full-space)
* [Add spatial environments to your app](/develop/xr/jetpack-xr-sdk/add-environments)
* [Add 3D models to your app](/develop/xr/jetpack-xr-sdk/add-3d-models)