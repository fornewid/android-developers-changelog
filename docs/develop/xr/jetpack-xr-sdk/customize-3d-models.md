---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/customize-3d-models
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/customize-3d-models
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Before customizing a 3D model, you first need to [add it into your app](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models).
After you've added a 3D model to your app, you can enhance the visual and
interactive experience by customizing how the 3D model looks and moves.

For example, you can play and control embedded glTF animations, access and move
nodes that make up your model, or even load custom textures and define material
properties to override internal meshes. These capabilities let you dynamically
alter an object's appearance and behavior at runtime.

## 3D objects in Android XR

The Jetpack XR SDK supports the [glTF
2.0](https://www.khronos.org/glTF/) open standard by Khronos Group for 3D models and renders
these objects with [physically based rendering (PBR)](https://www.khronos.org/gltf/pbr) techniques
specified in the glTF 2.0 standard (along with supported [extensions](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models#gltf-extensions)). A
glTF (Graphics Library Transmission Format) is a standard file format for
transmitting and loading 3D scenes and models. A glTF model is composed of a
hierarchical structure of internal components.

Here are the key components to understand:

- **Nodes**: These define the structure and hierarchy of the model. Each node can have its own position, rotation, and scale.
- **Meshes**: The structural, 3D geometry that forms the shape of a 3D object.
- **Materials** : These [define the visual appearance of the
  meshes](https://www.khronos.org/gltf/pbr), such as their color, roughness, or how they react to lighting.
- **Textures**: An image asset, such as a PNG file, that you can apply to the surface of a 3D model to create custom patterns, color, detail, or other visual effects.
- **Animations** : These are predefined sequences or animation *tracks* that contain changes to individual nodes and meshes to create the appearance of movement over time.

In Jetpack Compose for XR, you render these files using [`SpatialGltfModel`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SpatialGltfModel.composable)
and track its loading and animation status using a [`SpatialGltfModelState`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SpatialGltfModelState).
For more information, see [Add 3D models to your app](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models).

## Animate 3D models

3D models can have embedded animations. Internally, animations use
[samplers](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-animation) to define the timing and values of a movement, and
[channels](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-animation) to connect those movements to individual nodes and
meshes. Skeletal animations and material animations created with the
[`KHR_animation_pointer`](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Khronos/KHR_animation_pointer/README.md) [glTF extension](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Khronos/KHR_animation_pointer/README.md) are
supported in the Jetpack XR SDK.

Using Compose for XR, to play an animation, specify the name of the specific
track from the list of [`animations`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SpatialGltfModelState#animations()). Use [`animation.start()`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SpatialGltfModelAnimation) to begin
playing. Optionally, you can specify the speed, the seek time, and whether or
not the animation should loop using [`SpatialGltfModelAnimation`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SpatialGltfModelAnimation):


```kotlin
val animation = modelState.getAnimations().find { it.name == "Walk" }

animation?.animationState?.let { state ->
    LaunchedEffect(state) {
        Log.i("SpatialGltfModelAnimationSample", "Animation State: $state")
    }
}

DisposableEffect(animation) {
    animation?.loop()
    onDispose {
        animation?.stop()
    }
}
```

<br />

## Manipulate Nodes: Poses and Rotation

To manipulate specific parts of a model and change its properties like rotation
or pose, you'll need to query the internal `nodes` of the glTF model using
`SpatialGltfModelState`.


```kotlin
// Retrieve the list of nodes (individual components/meshes) defined within the glTF model.
val entityNodes = modelState.nodes

// Find a specific node by name to apply modifications, such as material overrides.
val node = entityNodes.find { it.name == "node_name" }
```

<br />

After you find the correct node, you can set its `localPose` to change its 3D
position and rotation relative to its immediate parent [`GltfModelNode`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/GltfModelNode) or
use [`modelPose`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/GltfModelNode#modelPose()) to set the position relative to the
[`GltfModelEntity`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/GltfModelEntity) root. Similarly, you can use localScale/modelScale to
change the scale of the model relative to its parent or root.


```kotlin
LaunchedEffect(node, degrees) {
    val rotation = Quaternion.fromEulerAngles(degrees, 0f, degrees)
    node?.let {
        it.localPose = Pose(it.localPose.translation, rotation)
    }
}
```

<br />

## Customize the material properties of your 3D model

You can adjust material attributes during runtime to change an object's
appearance dynamically based on user input or the current state of the app.

In Jetpack XR, the [`KhronosPbrMaterial`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/KhronosPbrMaterial) and [`KhronosUnlitMaterial`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/KhronosUnlitMaterial)
classes are used to create and manipulate these materials. As the name implies,
[`KhronosUnlitMaterials`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/KhronosUnlitMaterial) are unlit and not impacted by scene lighting.
[`KhronosPbrMaterial`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/KhronosPbrMaterial) lets you customize a wider range of properties, such
as sheen color, how metallic or rough an object is, and whether it emits light.

For more information about each supported property and the customizable
parameters in Android XR, see our [reference documentation](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/KhronosPbrMaterial). To better
understand these properties, see the [Khronos glossary](https://www.khronos.org/gltf/pbr#pbr-glossary).
![](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/customize-3d-models/change_color.gif) **Figure 1.** Example of changing the base colors on a 3d model.

To customize the material properties of your 3D model, first you'll create the
new material using [`KhronosPbrMaterial`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/KhronosPbrMaterial). You'll need to set the
appropriate [`AlphaMode`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/AlphaMode) for the visual appearance you are trying to
achieve:

Next, define the properties you want to modify. This example uses
[`setBaseColorFactor`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/KhronosPbrMaterial#setBaseColorFactor(androidx.xr.runtime.math.Vector4)) to change the base color of the mesh to purple. This
method requires a `Vector4`, where the `x, y, z`, and `w` components correspond
to the RGBA (Red, Green, Blue, and Alpha) values respectively:


```kotlin
// Maintain a reference to the custom material to avoid re-creating it on every recomposition.
var pbrMaterial by remember { mutableStateOf<KhronosPbrMaterial?>(null) }

// Create and apply the custom material once the session is ready and the target node is available.
LaunchedEffect(node) {
    val material = KhronosPbrMaterial.create(
        session = xrSession,
        alphaMode = AlphaMode.OPAQUE
    ).also {
        pbrMaterial = it
        // Apply a base color factor (RGBA) to change the color of the model.
        it.setBaseColorFactor(
            Vector4(
                x = 0.5f,
                y = 0.0f,
                z = 0.5f,
                w = 1.0f
            )
        )
    }
```

<br />

## Load custom textures for your 3D model

A [`Texture`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/Texture) is an image asset that you can apply to the surface of a 3D
model to provide color, detail, or other surface information. The Jetpack XR
Texture API lets you load image data, such as PNG files, from your app's
`/assets/` folder asynchronously.

When loading a texture, you can specify a [`TextureSampler`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/TextureSampler), which controls
how the texture is rendered. The sampler defines filtering properties (for when
the texture appears smaller or larger than its original size) and wrapping modes
(for handling coordinates outside the standard `[0, 1]` range). A `Texture` must
be assigned to a [`KhronosPbrMaterial`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/KhronosPbrMaterial) to have a visual effect on a 3D
model.
![](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/customize-3d-models/change_texture.gif) **Figure 2.** Example of changing the texture on a 3d model.

To load a custom texture, first you'll need to save the image file to your
`/assets/` folder. As a best practice, you might want to create a `textures`
subdirectory in that folder as well.

After you've saved the file in the appropriate directory, create the texture
with the [`Texture`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/Texture) API. This is also where you would apply an optional
`TextureSampler` if needed.

This example applies an [occlusion texture](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/KhronosPbrMaterial#setOcclusionTexture(androidx.xr.scenecore.Texture,kotlin.Float,androidx.xr.scenecore.TextureSampler)) and sets the occlusion strength:


```kotlin
LaunchedEffect(node) {
    val material = KhronosPbrMaterial.create(
        session = xrSession,
        alphaMode = AlphaMode.OPAQUE
    ).also {
        pbrMaterial = it

        // Load a texture
        val texture = Texture.create(
            session = xrSession,
            path = Path("textures/texture_name.png")
        )

        // Set the texture and configure occlusion to define how the material surface handles ambient lighting.
        it.setOcclusionTexture(
            texture = texture,
            strength = 1.0f
        )
    }
    node?.setMaterialOverride(
        material = material
    )
}
```

<br />

## Apply materials and textures to your 3D objects

To apply the new material or texture, override the existing material for a
specific node on your glTF [node](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SpatialGltfModelState#nodes()). Do this by calling
[`setMaterialOverride`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/GltfModelNode#setMaterialOverride(androidx.xr.scenecore.Material,kotlin.Int)):


```kotlin
node?.setMaterialOverride(
    material = material
)
```

<br />

To remove the newly-created materials, call [`clearMaterialOverride`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/GltfModelNode#clearMaterialOverride(kotlin.Int)) on the
previously overridden [node](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/SpatialGltfModelState#nodes()). This returns your 3D Model to its default
state:


```kotlin
if (removeMaterial) {
    node?.clearMaterialOverride()
}
```

<br />

> [!NOTE]
> **Note:** These calls must be made to a node that has a mesh. If you call `setMaterialOverride` on a node without a mesh, an exception is thrown.

*** ** * ** ***

glTF and the glTF logo are trademarks of the
Khronos Group Inc.