---
title: Customize 3D models in your app  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/customize-3d-models
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Customize 3D models in your app Stay organized with collections Save and categorize content based on your preferences.



Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/xr-headsets-icon.svg)


XR Headsets

![](/static/images/develop/xr/xr-glasses-icon.svg)


Wired XR Glasses

[Learn about XR device types →](/develop/xr/devices)

After you've [added a 3D model to your app](/develop/xr/jetpack-xr-sdk/add-3d-models), you can enhance the visual
experience by defining custom material properties and applying textures to the
object. Jetpack XR's material system is based on the [glTF™ 2.0](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html)
specification, and 3D models are rendered using
[physically-based rendering (PBR)](https://en.wikipedia.org/wiki/Physically_based_rendering). These are open standards maintained by
the Khronos Group.

Material attributes can be adjusted during runtime to change an object's
appearance dynamically based on user input or the current state of the app.

For details about each supported property and the customizable parameters
in Android XR, see our [reference documentation](/reference/kotlin/androidx/xr/scenecore/KhronosPbrMaterial). To better understand these
properties, see the [Khronos glossary](https://www.khronos.org/gltf/pbr#pbr-glossary).

## Customize the material properties of your 3D model

A `Material` defines a set of visual properties for an object's surface and
determines how that surface interacts with light in the scene.

In Jetpack XR, the [`KhronosPbrMaterial`](/reference/kotlin/androidx/xr/scenecore/KhronosPbrMaterial) and [`KhronosUnlitMaterial`](/reference/kotlin/androidx/xr/scenecore/KhronosUnlitMaterial)
classes are used to create and manipulate these materials. As the name implies,
[`KhronosUnlitMaterials`](/reference/kotlin/androidx/xr/scenecore/KhronosUnlitMaterial) are unlit and not impacted by scene
lighting. [`KhronosPbrMaterial`](/reference/kotlin/androidx/xr/scenecore/KhronosPbrMaterial) lets you customize a wider range of
properties, such as sheen color, how metallic or rough an object is, and whether
it emits light.

![Example of changing the base colors on a 3d model](/static/images/develop/xr/jetpack-xr-sdk/customize-3d-models/change_color.gif)

To customize the material properties of your 3D model, first you'll create the
new material using [`KhronosPbrMaterial`](/reference/kotlin/androidx/xr/scenecore/KhronosPbrMaterial). You'll need to set the appropriate
[`AlphaMode`](/reference/kotlin/androidx/xr/scenecore/AlphaMode) for the visual appearance you are trying to achieve:

```
val pbrMaterial = KhronosPbrMaterial.create(
    session = xrSession,
    alphaMode = AlphaMode.OPAQUE
)

MaterialOverride.kt
```

Next, define the properties you want to modify. In this example, we use
[`setBaseColorFactor`](/reference/kotlin/androidx/xr/scenecore/KhronosPbrMaterial#setBaseColorFactor(androidx.xr.runtime.math.Vector4)) to change the base color. This method requires a
`Vector4`, where the `x`, `y`, `z`, and `w` components correspond to the RGBA
(Red, Green, Blue, and Alpha) values respectively:

```
pbrMaterial.setBaseColorFactor(
    Vector4(
        x = 0.5f,
        y = 0.0f,
        z = 0.5f,
        w = 0.0f
    )
)

MaterialOverride.kt
```

## Create custom textures for your 3D model

A [`Texture`](/reference/kotlin/androidx/xr/scenecore/Texture) is an image asset that you can apply to the surface of a 3D
model to provide color, detail, or other surface information. The Jetpack XR
Texture API lets you load image data, such as PNG files, from your app's
`/assets/` folder asynchronously.

When loading a texture, you can specify a [`TextureSampler`](/reference/kotlin/androidx/xr/scenecore/TextureSampler), which controls
how the texture is rendered. The sampler defines filtering properties (for when
the texture appears smaller or larger than its original size) and wrapping modes
(for handling coordinates outside the standard `[0, 1]` range).
A `Texture` object by itself is just data; it must be assigned to a `Material`
to have a visual effect on a 3D model.

![Example of changing the texture on a 3d model](/static/images/develop/xr/jetpack-xr-sdk/customize-3d-models/change_texture.gif)

To create a custom texture, first you'll need to save the image file to your
`/assets/` folder. As a best practice, you may want to create a `textures`
subdirectory in that folder as well.

After you've saved the file in the appropriate directory, create the texture
with the [`Texture`](/reference/kotlin/androidx/xr/scenecore/Texture) API. This is also where you would apply an optional
[`TextureSampler`](/reference/kotlin/androidx/xr/scenecore/TextureSampler) if needed:

```
val texture = Texture.create(
    session = xrSession,
    path = Path("textures/texture_file.png")
)

MaterialOverride.kt
```

Next, define the type of texture and set its corresponding parameters. In this
example, we apply an occlusion texture and set the strength:

```
pbrMaterial.setOcclusionTexture(
    texture = texture,
    strength = 1.0f
)

MaterialOverride.kt
```

## Apply materials and textures to your 3D objects

To apply the new material or texture, override the existing material for a
specific node on your glTF node. Do this by calling
[`setMaterialOverride`](/reference/kotlin/androidx/xr/scenecore/GltfModelNode#setMaterialOverride(androidx.xr.scenecore.Material,kotlin.String,kotlin.Int)) on the [`GltfModelNode`](/reference/kotlin/androidx/xr/scenecore/GltfModelNode):

```
gltfModelNode.setMaterialOverride(
    material = pbrMaterial
)

MaterialOverride.kt
```

To remove the newly-created materials, call [`clearMaterialOverride`](/reference/kotlin/androidx/xr/scenecore/GltfModelNode=clearMaterialOverride(kotlin.String,kotlin.Int)) on
the previously overridden node on your [`GltfModelNode`](/reference/kotlin/androidx/xr/scenecore/GltfModelNode). This returns
your 3D Model to its default state:

```
gltfModelNode.clearMaterialOverride()

MaterialOverride.kt
```

**Note:** These classes create materials asynchronously and need to be handled
appropriately to avoid memory leaks. For more information, see our guidance on
[Asynchronous background processing](/develop/background-work/background-tasks/asynchronous).


---

glTF and the glTF logo are trademarks of the
Khronos Group Inc.