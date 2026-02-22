---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/customize-3d-models
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/customize-3d-models
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

After you've [added a 3D model to your app](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models), you can enhance the visual
experience by defining custom material properties and applying textures to the
object. Jetpack XR's material system is based on the [glTF™ 2.0](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html)
specification, and 3D models are rendered using
[physically-based rendering (PBR)](https://en.wikipedia.org/wiki/Physically_based_rendering). These are open standards maintained by
the Khronos Group.

Material attributes can be adjusted during runtime to change an object's
appearance dynamically based on user input or the current state of the app.

For details about each supported property and the customizable parameters
in Android XR, see our [reference documentation](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/KhronosPbrMaterial). To better understand these
properties, see the [Khronos glossary](https://www.khronos.org/gltf/pbr#pbr-glossary).

## Customize the material properties of your 3D model

A `Material` defines a set of visual properties for an object's surface and
determines how that surface interacts with light in the scene.

In Jetpack XR, the [`KhronosPbrMaterial`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/KhronosPbrMaterial) and [`KhronosUnlitMaterial`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/KhronosUnlitMaterial)
classes are used to create and manipulate these materials. As the name implies,
[`KhronosUnlitMaterials`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/KhronosUnlitMaterial) are unlit and not impacted by scene
lighting. [`KhronosPbrMaterial`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/KhronosPbrMaterial) lets you customize a wider range of
properties, such as sheen color, how metallic or rough an object is, and whether
it emits light.

![Example of changing the base colors on a 3d model](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/customize-3d-models/change_color.gif)

To customize the material properties of your 3D model, first you'll create the
new material using [`KhronosPbrMaterial`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/KhronosPbrMaterial). You'll need to set the appropriate
[`AlphaMode`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/AlphaMode) for the visual appearance you are trying to achieve:


```kotlin
val pbrMaterial = KhronosPbrMaterial.create(
    session = xrSession,
    alphaMode = AlphaMode.OPAQUE
)
```

<br />

Next, define the properties you want to modify. In this example, we use
[`setBaseColorFactor`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/KhronosPbrMaterial#setBaseColorFactor(androidx.xr.runtime.math.Vector4)) to change the base color. This method requires a
`Vector4`, where the `x`, `y`, `z`, and `w` components correspond to the RGBA
(Red, Green, Blue, and Alpha) values respectively:


```kotlin
pbrMaterial.setBaseColorFactor(
    Vector4(
        x = 0.5f,
        y = 0.0f,
        z = 0.5f,
        w = 0.0f
    )
)
```

<br />

## Create custom textures for your 3D model

A [`Texture`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/Texture) is an image asset that you can apply to the surface of a 3D
model to provide color, detail, or other surface information. The Jetpack XR
Texture API lets you load image data, such as PNG files, from your app's
`/assets/` folder asynchronously.

When loading a texture, you can specify a [`TextureSampler`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/TextureSampler), which controls
how the texture is rendered. The sampler defines filtering properties (for when
the texture appears smaller or larger than its original size) and wrapping modes
(for handling coordinates outside the standard `[0, 1]` range).
A `Texture` object by itself is just data; it must be assigned to a `Material`
to have a visual effect on a 3D model.

![Example of changing the texture on a 3d model](https://developer.android.com/static/images/develop/xr/jetpack-xr-sdk/customize-3d-models/change_texture.gif)

To create a custom texture, first you'll need to save the image file to your
`/assets/` folder. As a best practice, you may want to create a `textures`
subdirectory in that folder as well.

After you've saved the file in the appropriate directory, create the texture
with the [`Texture`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/Texture) API. This is also where you would apply an optional
[`TextureSampler`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/TextureSampler) if needed:


```kotlin
val texture = Texture.create(
    session = xrSession,
    path = Path("textures/texture_file.png")
)
```

<br />

Next, define the type of texture and set its corresponding parameters. In this
example, we apply an occlusion texture and set the strength:


```kotlin
pbrMaterial.setOcclusionTexture(
    texture = texture,
    strength = 1.0f
)
```

<br />

## Apply materials and textures to your 3D objects

To apply the new material or texture, override the existing material for a
specific node on your glTF entity. Do this by calling
[`setMaterialOverride`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/GltfModelEntity#setMaterialOverride(androidx.xr.scenecore.Material,kotlin.String,kotlin.Int)) on the [`GltfModelEntity`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/GltfModelEntity):


```kotlin
gltfModelEntity.setMaterialOverride(
    material = pbrMaterial,
    nodeName = "Node Name"
)
```

<br />

To remove the newly-created materials, call [`clearMaterialOverride`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/GltfModelEntity=clearMaterialOverride(kotlin.String,kotlin.Int)) on
the previously overridden node on your [`GltfModelEntity`](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/GltfModelEntity). This returns
your 3D Model to its default state:


```kotlin
gltfModelEntity.clearMaterialOverride(
    nodeName = "Node Name"
)
```

<br />

> [!NOTE]
> **Note:** These classes create materials asynchronously and need to be handled appropriately to avoid memory leaks. For mor information, see our guidance on [Asynchronous background processing](https://developer.android.com/develop/background-work/background-tasks/asynchronous).

*** ** * ** ***

glTF and the glTF logo are trademarks of the
Khronos Group Inc.