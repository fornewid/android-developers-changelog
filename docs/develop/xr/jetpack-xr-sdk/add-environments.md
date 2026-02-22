---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/add-environments
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/add-environments
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

In the Jetpack XR SDK, spatial environments are immersive surroundings that you
can add to your app to customize the background of the virtual scene. Spatial
environments are only visible when an app is in Full Space.

## Overview of spatial environments

A [`SpatialEnvironment`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialEnvironment) is used to manage an app's spatial environment
preferences. It is a composite of a standalone skybox image and glTF-specified
geometry. Only a single skybox image and a single glTF geometry file can be set
at a time.

A skybox represents the image a user sees around them in the virtual scene,
creating the illusion of a distant background environment, like a sky,
mountains, or cityscape. The user cannot interact with or get closer to the
skybox. The Jetpack XR SDK supports spherical skyboxes in the
[OpenEXR](https://openexr.com/) standard. In addition to providing an immersive
background for your app, an EXR skybox also provides image based lighting (IBL)
to 3D models loaded by your app. For more information, refer to the [guide for
working with 3D models](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models).

Spatial environments can also include 3D geometry content in the
[glTF](https://www.khronos.org/gltf/) standard. Environment geometry loaded this way will
automatically be aligned with the real-world floor. Environment geometry is a
great way to add realism to your environment through foreground and midground
elements that blend into the skybox with the parallax effect.

In the [design guidance for spatial environments](https://developer.android.com/design/ui/xr/guides/environments), you can learn about the
different types of assets you can use to create spatial environments and how to
create safe and enjoyable spatial environments.

You can set your app's spatial environment to one of these three configurations:

- A combination of a skybox image and glTF geometry.
- A passthrough surface, where the environment that is displayed is a live feed from the device's outward facing cameras. At full opacity, this passthrough surface completely occludes the skybox and geometry.
- A mixed configuration, where the passthrough surface is not at full opacity, nor is it at zero opacity. In this case, the passthrough surface becomes semi-transparent and alpha blends with the skybox and geometry behind it.

> [!NOTE]
> **Note:** When you set preferences for the `SpatialEnvironment`, the methods don't necessarily take effect immediately. Instead, these methods set a preference that will be applied when the device enters a state where the app environment can be changed. In the code snippets, you'll see listeners for handling these state changes.

### Spatial capabilities for spatial environments

- [`SpatialCapabilities`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialCapabilities): Represents the spatial capabilities of the
  current session. Certain spatial capabilities are relevant to spatial
  environments.

- [`SPATIAL_CAPABILITY_PASSTHROUGH_CONTROL`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialCapabilities#SPATIAL_CAPABILITY_PASSTHROUGH_CONTROL()): Indicates whether or not the
  activity can enable or disable passthrough at the current time.

- [`SPATIAL_CAPABILITY_APP_ENVIRONMENT`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialCapabilities#SPATIAL_CAPABILITY_APP_ENVIRONMENT()): Indicates whether or not the
  activity can set its own spatial environment at the current time.

## Import and load spatial environment resources

glTF and EXR resources for spatial environments are loaded asynchronously by
using the [`Session`](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-session) class.

### Create a glTF resource

A glTF resource can be created as a [`GltfModel`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/GltfModel), where the glTF is loaded
from a local file. A `GltfModel` can be used as part of a spatial app
environment.


```kotlin
val environmentGeometry = GltfModel.create(session, Paths.get("DayGeometry.glb"))
```

<br />

### Create an EXR image resource

An EXR image resource can be created as an [`ExrImage`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/ExrImage), where the EXR is
loaded from a local file. An `ExrImage` can be used with `cmgen` to create a ZIP
file of the IBL for your skyboxes. See [our guide on optimizing environment
assets](https://developer.android.com/develop/xr/jetpack-xr-sdk/optimize-environment-assets) for more details.


```kotlin
val lightingForSkybox = ExrImage.createFromZip(session, Paths.get("BlueSkyboxLighting.zip"))
```

<br />

## Set the `SpatialEnvironmentPreference` for your app

The [`preferredSpatialEnvironment`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialEnvironment#setSpatialEnvironmentPreference(androidx.xr.scenecore.SpatialEnvironment.SpatialEnvironmentPreference)) property controls the preferred spatial
environment for an app. When this property is used to set a preference, it does
not cause an immediate change unless [`isPreferredSpatialEnvironmentActive`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialEnvironment#isSpatialEnvironmentPreferenceActive())
is already `true`. Once the device enters a state where the XR background can be
changed and the [`SpatialCapabilities.SPATIAL_CAPABILITY_APP_ENVIRONMENT`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialCapabilities#SPATIAL_CAPABILITY_APP_ENVIRONMENT())
capability is available, the preferred spatial environment for the application
will be automatically displayed.

Setting the preference to `null` will disable the preferred spatial environment
for the app, meaning the default system environment will be displayed instead.

If the given [`SpatialEnvironmentPreference`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialEnvironment.SpatialEnvironmentPreference) is not null, but all of its
properties are null, then the spatial environment will consist of a black skybox
and no geometry.

To get notified of changes to the `SpatialEnvironment` state, use
[`addOnSpatialEnvironmentChangedListener`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialEnvironment#addOnSpatialEnvironmentChangedListener(java.util.function.Consumer)).

### Basic usage

This code snippet creates the environment geometry and skybox resources and then
sets the spatial environment preference. This preference will be remembered, and
it will be applied when the app has the capability to set its own environment.


```kotlin
val spatialEnvironmentPreference =
    SpatialEnvironment.SpatialEnvironmentPreference(lightingForSkybox, environmentGeometry)
session.scene.spatialEnvironment.preferredSpatialEnvironment = spatialEnvironmentPreference
if (session.scene.spatialEnvironment.isPreferredSpatialEnvironmentActive) {
    // The environment was successfully updated and is now visible, and any listeners
    // specified using addOnSpatialEnvironmentChangedListener will be notified.
} else {
    // The passthrough opacity preference was successfully set, but not
    // immediately visible. The passthrough opacity change will be applied
    // when the activity has the SPATIAL_CAPABILITY_APP_ENVIRONMENT capability.
    // Then, any listeners specified using addOnSpatialEnvironmentChangedListener
    // will be notified.
}
```

<br />

### Advanced usage

For more advanced use cases where you need finer control over the environment,
you can incorporate [`SpatialCapabilities`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialCapabilities) checks and implement an
[`addOnSpatialEnvironmentChangedListener`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialEnvironment#addOnSpatialEnvironmentChangedListener(java.util.function.Consumer)) to determine when you want to set
the spatial environment preference.

## Set the PassthroughOpacityPreference for the spatial environment for your app

One of the components of an app's immersive virtual background is a passthrough
surface. In this case the background that is displayed is a live feed from the
device's outward facing cameras.

[`setPassthroughOpacityPreference`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialEnvironment#setPassthroughOpacityPreference(kotlin.Float)) is used to set the preferred passthrough
opacity for an app. This method only sets a preference and does not cause an
immediate change unless the
[`SpatialCapabilities.SPATIAL_CAPABILITY_PASSTHROUGH_CONTROL`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialCapabilities#SPATIAL_CAPABILITY_PASSTHROUGH_CONTROL()) capability is
available. Once the device enters a state where the passthrough opacity can be
changed, and the `SpatialCapabilities.SPATIAL_CAPABILITY_PASSTHROUGH_CONTROL`
capability is available, the preferred passthrough opacity for the application
will be automatically applied.

The values for passthrough opacity preference range from `0.0f` (zero opacity,
where the passthrough surface is not visible) to `1.0f` (full opacity, where the
passthrough surface hides the spatial environment). The
`setPassthroughOpacityPreference` parameter is a nullable float. Setting the
value to null indicates that the app has no passthrough opacity preference, and
will return passthrough control to the system.

### Basic usage

This code snippet sets the passthrough opacity preference. This preference will
be remembered, and it will be applied when the app has the capability to set
passthrough opacity.


```kotlin
session.scene.spatialEnvironment.preferredPassthroughOpacity = 1.0f
if (session.scene.spatialEnvironment.currentPassthroughOpacity == 1.0f) {
    // The passthrough opacity request succeeded and should be visible now, and any listeners
    // specified using addOnPassthroughOpacityChangedListener will be notified.
} else {
    // The passthrough opacity preference was successfully set, but not
    // immediately visible. The passthrough opacity change will be applied
    // when the activity has the
    // SpatialCapabilities.SPATIAL_CAPABILITY_PASSTHROUGH_CONTROL capability.
    // Then, any listeners specified using addOnPassthroughOpacityChangedListener
    // will be notified.
}
```

<br />

### Advanced usage

For more advanced use cases where you need finer control over the passthrough
opacity, you can incorporate `SpatialCapabilities` checks and add a listener
using [`addOnPassthroughOpacityChangedListener`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialEnvironment#addOnPassthroughOpacityChangedListener(java.util.function.Consumer)) to determine when you want
to set the passthrough opacity preference.

## Asset optimization

When creating assets for setting your users' `SpatialEnvironment`, ensure that
your assets achieve high-quality resolution while maintaining a reasonable file
size. To learn more, see [our guidance on optimizing Environment assets](https://developer.android.com/develop/xr/jetpack-xr-sdk/optimize-environment-assets).

## Determine the current passthrough opacity


```kotlin
val currentPassthroughOpacity = session.scene.spatialEnvironment.currentPassthroughOpacityhttps://github.com/android/snippets/blob/e6bd0ecb017905ea2b0423d974e826421caa7d2b/xr/src/main/java/com/example/xr/scenecore/Environments.kt#L77-L77
```

<br />

## See also

- [Spatial environments design guidance](https://developer.android.com/design/ui/xr/guides/environments)