---
title: https://developer.android.com/stories/games/com2us-vulkan
url: https://developer.android.com/stories/games/com2us-vulkan
source: md.txt
---

# Com2uS uses Vulkan for better graphics

![Game title logo screenshot from Com2uS Chronicles.](https://developer.android.com/static/images/cards/distribute/stories/com2us_logo.png)

*Summoners War: Chronicles* [US(WW)](https://play.google.com/store/apps/details?id=com.com2us.chronicles.android.google.us.normal)and[KR](https://play.google.com/store/apps/details?id=com.com2us.chronicles.android.google.kr.normal)by Com2uS exclusively utilizes Vulkan for rendering on Android, with up to 30% performance improvements.

[Vulkan](https://developer.android.com/games/develop/use-vulkan)is a modern, cross-platform 3D graphics API designed to minimize abstraction between device graphics hardware and your game. Vulkan has lower CPU overhead compared with OpenGL ES, and Vulkan offers a wider range of features.
![](https://developer.android.com/static/images/cards/distribute/stories/com2us_game.png)**Figure 1.**In game screenshot.Your browser doesn't support the video tag.**Figure 2.**In game video.

## Rendering features

Com2uS developed advanced rendering features for*Summoners War: Chronicles*including:

- Custom deferred rendering system with pre-render light culling and up to sixteen active lights in the[view frustum](https://en.wikipedia.org/wiki/Viewing_frustum)simultaneously
- Indirect rendering instancing method (called`Clay`) to draw many meshes, materials, and textures at once
- Extensive use of compute shaders for pre-rendering tasks
- Ability to dynamically adjust active shadow rendering and post-processing effects based on camera movement, graphic options, and runtime performance

## Mobile hardware accommodations

*Summoners War: Chronicles* uses the same renderer for Android devices, personal computers, and dedicated gaming consoles. To achieve optimal performance on mobile hardware, Com2uS tuned rendering settings including draw depth and density. To accommodate certain devices running on Android 11 (API level 30) and lower, Com2uS created alternate versions of some shaders and used reduced instance counts.*Summoners War: Chronicles* also uses[adaptive performance](https://developer.android.com/games/optimize/adpf)features on Android to dynamically adjust graphic options in response to device thermal conditions.

## Vulkan-only rationale

Com2uS used Vulkan exclusively for*Summoners War: Chronicles*for several reasons:

- Minimum device requirements excluded older, less powerful devices lacking[Vulkan support](https://developer.android.com/about/dashboards#Vulkan)
- Customization of the[Unity engine](https://developer.android.com/games/engines/unity/start-in-unity)Built-in Render Pipeline (BiRP) required features only available in the game's Vulkan backend
- Implementation of rendering features utilizing compute shader output and shader storage buffer objects (SSBOs) can be done on Vulkan but not OpenGL ES

## Compute workloads

*Summoners War: Chronicles*performs significant compute shader work to produce data for rendering. Compute shaders are used for:

- Object culling
- Collision inspection
- Animation tasks
- Indirect rendering data generation

The resulting compute data is written to Unity engine RWBuffer objects. To achieve optimal performance*Summoners War: Chronicles*runs all its compute jobs with a single dispatch, which requires the use of multiple RWBuffers simultaneously. This approach was only possible using Vulkan, as the Unity BiRP OpenGL ES backend only supports the use of one single RWBuffer a time.

The data sets generated for rendering are often larger than device size limits for uniform buffer objects (UBOs).*Summoners War: Chronicles*instead uses Shader storage buffer objects (SSBOs), which have larger capacity limits. However, binding SSBOs to vertex stage operations requires read-only SSBO support. OpenGL ES only supports read-write SSBOs while Vulkan can mark SSBOs as read-only.

## Indirect instanced rendering with Clay

For*Summoners War: Chronicles* , Com2uS developed a method to batch multiple materials, meshes, and textures into a single draw call. Com2uS refers to this system as*Clay*. Clay improves game performance by 30% as a result of significantly reducing draw calls.

Clay begins during the culling and collision phase by building a list of compatible visible renderable objects. Clay then generates rendering information for each identified object into SSBOs. This process is performed with compute shaders, which enable the use of indirect instanced rendering using the Unity renderer[DrawMeshInstancedIndirect](https://docs.unity3d.com/ScriptReference/Graphics.DrawMeshInstancedIndirect.html)function. With indirect rendering, the instance information and instance count parameters are generated directly on the GPU. When drawing objects, instead of binding a traditional object mesh, Clay binds a cone mesh as pictured:
![](https://developer.android.com/static/images/cards/distribute/stories/com2us_cone.png)**Figure 3.**A cone mesh.

Clay then transforms the cone mesh in the vertex shader using a bound SSBO of vertex transformation data generated by the compute shaders. Binding SSBOs to the vertex stage requires the use of Vulkan. Clay can use multiple transformed cones to render a single object. The object's complexity determines the number of cones.
![](https://developer.android.com/static/images/cards/distribute/stories/com2us_cone_usage.png)**Figure 4.**How cone mesh is transformed to tree.

Material data for objects is batched in another buffer generated by the compute shaders. The buffer is bound to the fragment shader. Textures for the objects being drawn are configured in a texture array. The array indices for an object\`s textures are included in the object's material data. Under ideal circumstances, Clay can render with a maximum of seven draw calls:

- Static objects
- Animated objects
- Shadows (four iterations)
- Reflections

## Unity plus Vulkan

*Summoners War: Chronicles*demonstrates that the powerful combination of the Unity game engine and Vulkan graphics API enables developers to bring advanced console quality graphics to Android devices.