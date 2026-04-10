---
title: https://developer.android.com/stories/games/diablo-raytracing
url: https://developer.android.com/stories/games/diablo-raytracing
source: md.txt
---

# Diablo Immortal boosts image quality with hardware ray tracing

![](https://developer.android.com/static/images/cards/distribute/stories/diablo_raytracing_hero_image.jpg)

[Diablo Immortal](https://play.google.com/store/apps/details?id=com.blizzard.diablo.immortal)is a free-to-play multiplayer action role-playing game (ARPG) jointly developed by[Blizzard Entertainment](https://www.blizzard.com/en-gb/)and[NetEase](https://www.neteasegames.com/m/). Diablo Immortal, a new chapter in the Diablo series, launched in 2022. The game fills the story gap between[Diablo 2](https://diablo2.blizzard.com/en-gb/)and[Diablo 3](https://diablo3.blizzard.com/en-gb/)and unfolds a new adventure around the fragments of the*World Stone* , where players explore the continent of[Sanctuary](https://diablo.fandom.com/wiki/Sanctuary)to fight against demons and corrupted forces.

With the innovation of mobile GPU architecture and breakthroughs in hardware acceleration capabilities,[ray tracing](https://en.wikipedia.org/wiki/Ray_tracing_(graphics))technology is gradually migrating from desktop to mobile devices, becoming one of the core drivers of high-fidelity graphics rendering. Calculation of physically realistic dynamic[reflections](https://en.wikipedia.org/wiki/Reflection_(computer_graphics))is computationally demanding, but a dedicated hardware unit makes this possible on power-constrained mobile platforms. By tracing the propagation path of light through the scene in real time, the technology accurately simulates the reflective behavior of complex surfaces such as mirrors, metals, and liquids. Ray tracing overcomes the spatial limitations and approximation errors of traditional rasterization schemes and supports the global consistent expression of dynamic light sources, off-screen objects, and multilevel reflections.

The Diablo Immortal team decided to use hardware-based ray tracing to accurately represent reflection of objects outside of the screen, avoiding problems such as missing objects and edge breaks caused by more traditional solutions that rely on information displayed inside the current screen. Ray tracing provides more realistic specular reflection effects, especially in dynamic scenes. Other solutions are limited by the camera's perspective and rendering pipeline, often resulting in visual defects.

## Hardware ray tracing on mobile

[Hardware ray tracing](https://developer.arm.com/documentation/101897/0304/Ray-tracing)technology mainly includes two implementation paradigms:[ray tracing pipeline](https://developer.arm.com/documentation/101897/0304/Ray-tracing/Ray-tracing-pipeline)and[ray query](https://developer.arm.com/documentation/101897/0304/Ray-tracing/Ray-query).

Ray tracing pipeline builds a complete pipeline through dedicated shader stages (ray generation / intersection / closest-hit shader). Although it can achieve precise ray interaction control, ray tracing pipeline requires independent pipeline configuration, which increases development complexity.

Ray query, on the other hand, allows ray queries to be initiated directly from traditional[computation](https://www.khronos.org/opengl/wiki/Compute_Shader)or[fragment](https://www.khronos.org/opengl/wiki/Fragment_Shader)shaders, making it a core technology for mobile ray tracing. By eliminating the need for separate pipelines, ray query not only significantly simplifies the development process, but also has three major advantages:

1. Provides compatibility with heterogeneous computing environments and noncomplete ray tracing hardware
2. Supports on-demand invocation of ray tracing at any shading stage
3. By reducing resource usage, meets the bandwidth and power constraints of mobile platforms and provides a feasible basis for advanced effects such as[dynamic global illumination](https://en.wikipedia.org/wiki/Global_illumination)and real-time reflection in mobile games

Diablo Immortal uses[Vulkan](https://www.vulkan.org/)to take advantage of the GPU's hardware ray tracing capabilities. The game computes the path of light rays through the scene in real time and accounts for complex material properties to achieve breakthrough real-time reflection effects on Android devices.
![](https://developer.android.com/static/images/cards/distribute/stories/diablo_raytracing_reflection_on.jpg)**Figure 1.**Scene with ray-traced reflection on.![](https://developer.android.com/static/images/cards/distribute/stories/diablo_raytracing_reflection_off.jpg)**Figure 2.**Scene with ray-traced reflection off.

## Acceleration structure

The[acceleration structure](https://docs.vulkan.org/spec/latest/chapters/accelstructures.html)is the core of hardware ray tracing. Acceleration structure greatly improves the efficiency of ray intersection testing through hierarchical data organization.

The system typically has two levels: the top-level acceleration structure (TLAS) and bottom-level acceleration structure (BLAS):

- TLAS plays the role of[scene manager](https://en.wikipedia.org/wiki/Scene_graph)--- By recording the spatial transformation matrix (including position, rotation, and scale) of all BLAS instances, TLAS realizes the global organization of dynamic scenes. For example, TLAS allows developers to distribute hundreds of instances of the same tree model in different positions and poses in the scene; and so, developers only need to update the transformation matrix of the moving object each frame instead of reconstructing the geometry.
- BLAS as the base unit --- Responsible for efficiently encoding the geometric details of a single 3D object, BLAS establishes a spatial index structure through the[bounding volume hierarchy (BVH) algorithm](https://en.wikipedia.org/wiki/Bounding_volume_hierarchy)so that irrelevant areas can be quickly skipped during ray detection.

This hierarchical design allows the ray tracing pipeline to form an efficient detection chain of*ray ==\> TLAS (coarse sieve object instance) ==\> BLAS (exact intersection)*.

Separating dynamic and static models is key to minimizing the cost of acceleration structure construction:

- Static model --- The BLAS only needs to be built once in the initialization stage and can be directly reused in subsequent scene loading. To avoid the loading lag of large-scale scenes, the asynchronous preconstruction technology of framing can be used to spread the BLAS construction task to multiple frames.
- Dynamic model
  - Skeletal animation-driven --- The skinned vertex data needs to be computed in parallel by compute shader every frame to generate a new vertex buffer and then trigger the incremental update of the corresponding BLAS, which avoids complete reconstruction to improve performance.
  - Rigid body transformation --- If only translation/rotation/zoom transforms are involved, there is no need to modify BLAS, just update its world transform matrix in TLAS and then trigger the TLAS quick update process.

Periodic reconstruction is essential for maintaining acceleration structure efficiency in ray tracing dynamic scenes. When dynamic objects undergo significant changes in geometric topology, such as deformation or large-scale vertex displacement, the original spatial division may fail, reducing collision detection performance during ray traversal. As a result, a full reconstruction, rather than an incremental update, of the highly dynamic BLAS/TLAS must be triggered every N frames.

Finally, to optimize the performance of ray-tracing rendering, adopt a dynamic TLAS construction strategy based on the character's viewable region: only the models within the character's active radius threshold are included in the TLAS to reduce the core overhead of ray intersection calculation.

## Ray-traced reflections

Ray-traced reflections have several advantages over traditional techniques such as[screen-space reflections (SSR)](https://lettier.github.io/3d-game-shaders-for-beginners/screen-space-reflection.html)and planar reflections (simple surfaces that project a scene in one dimension). Ray-traced reflection physically simulates the path of light, accurately captures dynamic objects inside and outside the scene, supports natural reflections from curved and nonplanar surfaces, and enables multiple light bounce effects such as mirrors. By contrast, SSR is limited to the information visible on the screen, and flat planar reflections are prone to visual errors or distortion in complex scenes.
![](https://developer.android.com/static/images/cards/distribute/stories/diablo_raytracing_wings_reflection.jpg)**Figure 3.**The reflection of the wings in the pool.![](https://developer.android.com/static/images/cards/distribute/stories/diablo_raytracing_monster_reflection.jpg)**Figure 4.**The reflection of the monster.

Ray-traced reflection is similar to traditional SSR in principle: ray-traced reflection emits rays in the direction of line-of-sight reflection on a pixel-by-pixel basis and calculates the intersection of the rays with the scene objects. The intersection point returned by the ray query API contains geometric information (including instance ID, geometry index, and primitive index) and rasterization parameters (barycentric coordinates) at the triangle level, but does not contain pixel color data. The typical solution uses[bindless resource binding technology](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/ray_tracing/rt05_bindless/)to precompile all texture and material parameters of the scene into a global index array. Using the geometric identifiers returned by ray query, the physical properties of the corresponding material (such as normal map and roughness) can be looked up and then combined with barycentric coordinate interpolation to calculate the surface shading information, and the real color value of the intersection can be reconstructed through rasterization.

However, during the process of implementation, the Diablo Immortal team discovered two significant technical problems:

1. The lighting model was forced to be unified, which conflicted with the diverse shading systems accumulated in the history of the project and would result in a mismatch between the specular material and the original material.
2. The variety of vertex formats leads to the degradation of instruction branching efficiency in the rasterization stage, which is a major issue under the tight performance budget of the mobile device.

The Diablo Immortal team innovatively introduced the visibility buffer to separate geometry processing from shading calculations:

- Ray tracing phase --- Pixel-level ray hit information is captured in real time through ray query. The 3D spatial identifier (`InstanceID`with`PrimitiveIndex`) of the intersection point is encoded into a compact visibility ID and written into the screen space buffer.
- Coloring stage --- Similar to the operations done by vertex and pixel shaders, the geometric identifiers in the visibility buffer are dynamically parsed, the vertex properties (such as UVs and normals) and physically-based material maps of the original model are fetched, and the shading calculations associated with the material type are finally performed.

This solution allows art assets to be connected to the ray-traced reflection system without having to modify vertex formats or shaders.

## Specific rendering steps

### Ray query pass

Corresponds to the ray tracing stage and generates a visibility buffer for screen space reflections:

- Color0
  - Format：R32G32UInt
  - R = TriangleID，G = Barycentrics

![](https://developer.android.com/static/images/cards/distribute/stories/diablo_raytracing_visibility_buffer.png)**Figure 5.**Visibility buffer.

- Depth:
  - Format：Depth32F
  - D = EncodeAsFloat(InstanceIdx, GeometryIdx)
  - The material identifier of the intersection is encoded in 32-bit floating point and written to the depth buffer for the next stage of the material's depth-coding-match detection technique

![](https://developer.android.com/static/images/cards/distribute/stories/diablo_raytracing_encoded_depth.png)**Figure 6.**Encoded depth.

Compared with compute shader, ray query in pixel shader has the following advantages:

- Pipeline integration --- Pipeline is embedded directly into existing forward/deferred rendering pipelines, maintaining render pipeline state continuity.
- Mobile bandwidth optimization --- For the mobile tile-based architecture, on-chip lossless compression can be triggered when ray hit data is written to`RenderTarget`, reducing memory bandwidth consumption compared with traditional compute shader output to buffer.
- Ray quantity control --- Nonreflective areas can be marked and rejected by means of a precalculation phase in combination with a stencil test.

### Resolve pass

In the coloring stage (see[Ray-traced reflections](https://developer.android.com/stories/games/diablo-raytracing#ray-traced-reflections)), the Diablo Immortal team achieved fast identification matching by using the depth test hardware unit and performing coloring of materials in successive batches.

For each material, a full-screen draw pass is issued. The vertex shader dynamically reconstructs the current material's encoded identifier. Using the Depth Equal Test, the identifier is compared against encoded values in the depth buffer, and only pixels whose encoded values exactly match are retained, that is, those pixels that belong to the current material Instance. The retained pixels execute the corresponding material shader.

Next, high-precision material reproduction is implemented in the pixel shader:

- Geometry data decoding --- Extracts the triangle identifier (`MeshID`+`PrimitiveID`) and barycentric coordinates from the visibility buffer and dynamically loads the vertex attributes (position, UV, normal, etc.) of the corresponding triangle from the vertex buffer. Since each model is shaded as an independent material, advanced features such as binding are not necessary.
- Surface parameter reconstruction --- Calculates the UV coordinates at the intersection using barycentric coordinate interpolation. Software rasterization is performed to sample the map based on the interpolated UVs.
- Shading calculation reuse --- Directly reuses existing shader code to maintain the same material logic as the main rendering pipeline.

![](https://developer.android.com/static/images/cards/distribute/stories/diablo_raytracing_resolved_reflection.png)**Figure 7.**Resolved reflection.

Finally, the models that actually participate in the reflection calculation only account for a very small portion of the scene. The reflection model identification data returned by the GPU can be asynchronously read to eliminate the models/materials that do not participate in the reflection, effectively reducing the number of draw calls (a draw call occurs when materials and a mesh are submitted to the GPU for drawing) in the shading stage.

## Physically-based specular reflection

To achieve high-fidelity reflections, reflective surfaces are classified as one of three types according to roughness:

1. No reflection --- Reflection calculations for these surfaces can be skipped to save resources. If the surface is very rough, the reflection becomes blurry and faint, so the contribution is not obvious.
2. Mirror reflection --- Like a smooth mirror, the reflected image is clear and not blurred. Shoot the line directly in the direction of reflection from the line of sight.
3. Glossy reflection --- The reflection with a certain roughness of the surface is simulated based on[GGX importance sampling](https://schuttejoe.github.io/post/ggximportancesamplingpart1/), which can take into account both computational efficiency and physical accuracy. The reflection deviates to the main direction of specular reflection when emitting the line, which improves the sampling efficiency of the highlight area.

To achieve usable image quality with limited power consumption, the Diablo Immortal team adopted a[1SPP+Denoiser](https://github.com/gtong-nv/BMFR-DXR-Denoiser)solution. That is, the Diablo Immortal team took one sample per pixel, and then a temporal/spatial noise reduction algorithm is used to smooth out the large amount of noise introduced by low sampling rate.

The Diablo Immortal team chose the Reflection Denoiser in AMD FidelityFX Denoiser, a high-performance denoiser optimized for ray-traced reflections and screen-space reflections. The core advantage of the Reflection Denoiser is the denoiser's spatiotemporal hybrid noise reduction algorithm: by fusing the current frame and historical frame data (based on motion compensation), combined with spatial filtering techniques (such as variance-guided edge retention filtering), the Reflection Denoiser efficiently eliminates noise and outputs smooth reflection effects at very low sampling.

To adapt to the characteristics of self-developed render pipelines and meet the stringent performance constraints of mobile, the Diablo Immortal team has implemented targeted streamlining and architecture adaptation when integrating AMD FidelityFX Reflection Denoiser.

## High fidelity ray tracing with Vulkan

Diablo Immortal runs on a wide range of Vulkan-enabled Android devices where the Diablo Immortal team took advantage of innovative GPU hardware ray-tracing capabilities. Vulkan reduced development overhead and friction, facilitating the delivery of high-quality Diablo Immortal content and gameplay to Android users.

## Get started with Ray tracing on Vulkan

As demonstrated by Diablo Immortal, achieving ray tracing effects on Android involves leveraging the[Vulkan API](https://developer.android.com/ndk/guides/graphics/getting-started)on capable hardware. Developers interested in using Vulkan directly can refer to[Learn about Ray Tracing with Vulkan on Android](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/ray_tracing/)by[ARM](https://www.arm.com/)or the[Raytracing](https://docs.qualcomm.com/bundle/publicresource/topics/80-78185-2/best_practices.html#raytracing)section of the Adreno GPU on Mobile: Best Practices by Qualcomm. For details on the API, refer to the official Khronos[Ray Tracing In Vulkan](https://www.khronos.org/blog/ray-tracing-in-vulkan)specifications.

For engine-based development,[Unreal Engine](https://www.unrealengine.com/en-US)in collaboration with ARM provides[experimental support for Lumen with hardware ray tracing on mobile](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/how-to-enable-hwrt-on-lumen-for-android-devices/). While[Unity's](https://unity.com/)support for hardware ray tracing on Android is still evolving, keep an eye on the Unity updates.