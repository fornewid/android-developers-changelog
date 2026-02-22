---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

When working with 3D models, the Jetpack XR SDK supports the [glTF
2.0](https://www.khronos.org/glTF/) open standard. When Android XR renders apps built with the
Jetpack XR SDK, 3D models will be rendered with [physically based
rendering(PBR)](https://en.wikipedia.org/wiki/Physically_based_rendering) techniques specified in the glTF 2.0 standard
(along with supported [extensions](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models#gltf-extensions)). Most digital content creation (dcc)
tools, such as [Autodesk Maya](https://www.autodesk.com/products/maya/overview), [Maxon ZBrush](https://www.maxon.net/en/zbrush),
[Blender](https://www.blender.org/) and [Spline](https://spline.design/) can export 3D models into
the glTF format (`.gltf` or `.glb` files).

If a [`SpatialEnvironment`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialEnvironment) skybox has been specified by the user or by your
app, 3D models will be lit with lighting information provided by the environment
skybox. Reflective materials and specular highlights will also reflect the
environment skybox. If passthrough has been enabled, then the lighting,
reflections and specular highlights will be based on a simple, bright room with
a single directional light.

For a quick overview of the supported materials, refer to the [glTF PBR
Properties](https://www.khronos.org/gltf/pbr/) on the Khronos site.

There are two primary ways for apps built with the Jetpack XR SDK to load 3D
models.

- Load it into the `ActivitySpace` as described in [Place a 3D model into the
  `ActivitySpace`](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models#place-3d)
- Use the built-in [Scene Viewer](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models#load-3d) through an intent

## Place a 3D model into the ActivitySpace

Once you have your glTF file, the next step is to add it to the assets directory
in Android Studio. We recommend creating a `models` directory to better organize
your asset types.

![Example of adding assets to the /models directory](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/add-3d-models/models-directory.png)

To load the glTF model, call [`GltfModel.create()`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/GltfModel#create(androidx.xr.runtime.Session,java.nio.file.Path)).


```kotlin
val gltfModel = GltfModel.create(session, Paths.get("models", "saturn_rings.glb"))
```

<br />

At this point, the model is loaded into memory, but it's not being rendered yet.
If you have many 3D models to load or your model is large, it's a good idea to
load them asynchronously ahead of time. This way, users don't have to wait for
your models to be loaded into memory.

> [!TIP]
> **Tip:** If your app is going over [Google Play's maximum size
> limits](https://support.google.com/googleplay/android-developer/answer/9859372#size_limits) due to 3D assets and high resolution textures, you should consider using [Play Asset Delivery](https://developer.android.com/guide/playcore/asset-delivery) to optimize the delivery of your assets. For more information, see how to [package and distribute apps for
> Android XR](https://developer.android.com/develop/xr/package-and-distribute).

We need to add the glTF into the [`ActivitySpace`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/ActivitySpace). Call
[`GltfModelEntity.create`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/GltfModelEntity#create) to create an entity and place it into the
`ActivitySpace`. As best practice, you should [check that the app is in a state
which allows for spatial capabilities](https://developer.android.com/develop/xr/jetpack-xr-sdk/check-spatial-capabilities).


```kotlin
if (session.scene.spatialCapabilities.contains(SpatialCapability.SPATIAL_3D_CONTENT)) {
    val gltfEntity = GltfModelEntity.create(session, gltfModel)
}
```

<br />

You should now see the loaded 3D model when you run your app.

![Example of the loaded 3d model](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/add-3d-models/3d-model.jpg)

> [!IMPORTANT]
> **Important:** Some 3D content, such as 3D models, will only be visible when the app is in Full Space.

## Place a 3D model into a Compose SceneCoreEntity

While you will still need to load the glTF into memory using
[`GltfModel.create()`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/GltfModel#create(androidx.xr.runtime.Session,java.nio.file.Path)), you can place 3D models into a
[`SceneCoreEntity`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/package-summary#SceneCoreEntity(kotlin.Function0,androidx.xr.compose.subspace.layout.SubspaceModifier,kotlin.Function1,androidx.xr.compose.subspace.SceneCoreEntitySizeAdapter,kotlin.Function0)) if you are creating your UI with Jetpack Compose for XR.
Refer to [Use a SceneCoreEntity to place a 3D object in your layout](https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui#use-scenecoreentity).

## Animate 3D models

As part of the glTF specification, 3D models can have animations embedded.
Skeletal (rigged), rigid, morph target (blend shapes) animations are all
supported in the Jetpack XR SDK. Material animations created with the
[`KHR_animation_pointer` glTF extension](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Khronos/KHR_animation_pointer/README.md) are also supported.

To play an animation, call [`startAnimation()`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/GltfModelEntity#startAnimation(kotlin.Boolean,kotlin.String)) and specify the name of the
animation. You can optionally specify whether or not the animation should loop
indefinitely.


```kotlin
gltfEntity.startAnimation(loop = true, animationName = "Walk")
```

<br />

Calling `startAnimation` a second time, the current animation will stop and the
new animation will start.

You can query the current state of the animation through
[`getAnimationState()`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/GltfModelEntity#getAnimationState()).

If the animation name specified when calling `startAnimation()` doesn't exist,
the call silently fails, any running animations stop, and `getAnimationState()`
returns `STOPPED`.

## Load a 3D model using Scene Viewer

If you're looking for the simplest way to load a 3D model with basic interaction
capabilities, you may opt to [use Scene Viewer as you would on
mobile](https://developers.google.com/ar/develop/scene-viewer). A key difference between the Scene Viewer on Android XR
and on mobile is that Scene Viewer only supports the file URI parameter pointing
to the glTF file and all other parameters are ignored.

Scene Viewer is a separate app that is invoked using an intent and runs in Full
Space Mode. As a result, when you invoke it, your app will no longer be visible
and Scene Viewer will have focus. Any [environments](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-environments) you may have changed
will be reset to the user's system preferences.

Here's an example of using an [`Intent`](https://developer.android.com/reference/android/content/Intent) to view a glTF file in Scene Viewer
on Android XR:


```kotlin
val url =
    "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Models/master/2.0/Avocado/glTF/Avocado.gltf"
val sceneViewerIntent = Intent(Intent.ACTION_VIEW)
val intentUri =
    Uri.parse("https://arvr.google.com/scene-viewer/1.2")
        .buildUpon()
        .appendQueryParameter("file", url)
        .build()
sceneViewerIntent.setData(intentUri)
try {
    startActivity(sceneViewerIntent)
} catch (e: ActivityNotFoundException) {
    // There is no activity that could handle the intent.
}
```

<br />

For more information on the interactivity options for Scene Viewer, refer to our
[3D model design documentation](https://developer.android.com/design/ui/xr/guides/3d-content).

## glTF extensions

Jetpack XR SDK supports several gfTF extensions that expand the capabilities of
3D models. These capabilities are available through both the
[`GltfModelEntity`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/GltfModelEntity) and Scene Viewer.

- [`KHR_animation_pointer`](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Khronos/KHR_animation_pointer/README.md)
- [`KHR_draco_mesh_compression`](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Khronos/KHR_draco_mesh_compression/README.md)
- [`KHR_lights_punctual`](https://github.com/KhronosGroup/glTF/tree/main/extensions/2.0/Khronos/KHR_lights_punctual)
- [`KHR_materials_clearcoat`](https://github.com/KhronosGroup/glTF/tree/main/extensions/2.0/Khronos/KHR_materials_clearcoat)
- [`KHR_materials_sheen`](https://github.com/KhronosGroup/glTF/tree/main/extensions/2.0/Khronos/KHR_materials_sheen)
- [`KHR_materials_unlit`](https://github.com/KhronosGroup/glTF/tree/main/extensions/2.0/Khronos/KHR_materials_unlit)
- [`KHR_materials_variants`](https://github.com/KhronosGroup/glTF/tree/main/extensions/2.0/Khronos/KHR_materials_variants)
- [`KHR_mesh_quantization`](https://github.com/KhronosGroup/glTF/tree/main/extensions/2.0/Khronos/KHR_mesh_quantization)
- [`KHR_texture_basisu`](https://github.com/KhronosGroup/glTF/tree/main/extensions/2.0/Khronos/KHR_texture_basisu)
- [`KHR_texture_transform`](https://github.com/KhronosGroup/glTF/tree/main/extensions/2.0/Khronos/KHR_texture_transform)
- [`EXT_texture_webp`](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Vendor/EXT_texture_webp/README.md)