---
title: https://developer.android.com/stories/games/godot-vulkan
url: https://developer.android.com/stories/games/godot-vulkan
source: md.txt
---

# Godot Engine Vulkan optimization for Android

![The Godot Engine mascot image](https://developer.android.com/static/images/cards/distribute/stories/godot_logo.png)

## Overview

[Godot Engine](https://godotengine.org/)is a popular multiplatform open-source game engine with robust support for Android. Godot can be used to create games of virtually any genre and is capable of both 2D and 3D graphics. Godot version 4 introduced a new rendering system with advanced features for high-fidelity graphics. The Godot 4 renderer is designed for modern graphics APIs such as Vulkan.

The Godot Foundation engaged the graphics optimization experts at[The Forge Interactive](https://theforge.dev/)and collaborated with Google to analyze and further improve the Godot 4 Vulkan renderer and merge those optimizations back into the project repository. The optimizations help developers improve custom Vulkan renderers on Android.

## Optimization methodology and results

The optimization process used two different 3D scenes in Godot as benchmarking targets. The rendering time of the scenes was measured on multiple devices during each iteration of optimization. To qualify for inclusion, changes to the renderer needed to show performance improvements on at least some tested devices and couldn't introduce performance regressions on any device.

Multiple popular Android GPU architectures were used in testing. While many optimizations brought general improvements, some optimizations had greater impact on specific GPU architectures. The sum total of all optimization work resulted in a general 10%-20% reduction in GPU frame times.

## General Vulkan optimization

The Forge performed general architectural refactoring on the Godot Vulkan rendering backend to improve performance and help the backend scale with increased content rendering demands. The optimizations are not specific to mobile hardware, but benefit all Godot Vulkan platforms.

### Dynamic UBO offset support

When binding a descriptor set that contains a dynamic uniform buffer object (UBO), Vulkan allows dynamic offsets into the UBO to be specified in the bind parameters. This feature can be used to pack data for multiple rendering operations into a single UBO, rebinding the descriptor set with a different dynamic offset to select the proper data for the shader. The Godot Vulkan renderer was updated to be able to use dynamic offsets instead of always initializing the offset to zero. This improvement enables future efficiency optimizations.

### Linear descriptor set pools

Formerly, the default behavior in the Godot Vulkan renderer was to create all descriptor set pools using the[`VK_DESCRIPTOR_POOL_CREATE_FREE_DESCRIPTOR_SET_BIT`](https://registry.khronos.org/vulkan/specs/latest/html/vkspec.html#descriptorsets-allocation)flag, meaning that descriptor set allocations could be freed back to the pool and reallocations could be made from the pool. This mode imposed additional overhead compared to descriptor set pools which only allow linear allocation followed by a total reset of the pool.

Where possible, descriptor set pools are now created as linear pools without setting`VK_DESCRIPTOR_POOL_CREATE_FREE_DESCRIPTOR_SET_BIT`. Linear pools are then reset as a whole when needed. This work also includes additional optimization to batch descriptor set binding when feasible, reducing the number of discrete calls to[`vkCmdBindDescriptorSets()`](https://registry.khronos.org/VulkanSC/specs/1.0-extensions/man/html/vkCmdBindDescriptorSets.html).

### Immutable sampler support

Sampler objects that contain sampling configuration data are traditionally bound as part of the descriptor set data. This method allows sampler objects to be dynamically swapped out in the descriptor set data. Vulkan also supports immutable samplers, which encode the sampler data directly into the descriptor set layout. This sampler configuration is bound when creating the descriptor set and pipeline state and cannot be changed post creation.

Immutable samplers trade off flexibility for no longer having to manage and bind discrete sampler objects. The Godot Vulkan renderer was updated to support use of immutable samplers; sampler usage was changed to use immutable samplers where practical.

## Mobile-focused optimization

Additional optimizations were implemented to specifically improve rendering performance on mobile graphics hardware. The optimizations are not generally relevant to desktop class graphics hardware due to different architectural designs.

The optimizations include:

- Replace use of large push constants
- Lazy buffer allocation
- Persistent buffer support
- ASTC decode mode change
- Screen pre-rotation

### Replace use of large push constants

Push constants are a feature that allows injecting constant values for the active shader program into the command buffer. Push constants are convenient because they don't require buffer creation and population and are not tied to descriptors. However, push constants have a limited maximum size and can negatively affect performance on mobile hardware.

During testing on Android devices, performance was improved by replacing push constant usage of more than 16 bytes with uniform buffers. Shaders that used 16 bytes or fewer of constant data were more performant with push constants. In addition to performance considerations, some graphics hardware has 64-byte alignment minimums for uniform buffers, which reduces memory efficiency due to unused padding when compared to using push constants.

### Lazy buffer allocation

Most mobile graphics hardware uses a tile-based deferred rendering (TBDR) architecture. GPUs that use TBDR break up the larger screen region into a grid of smaller tiles and render on a per-tile basis. Each tile is backed by a small amount of high-speed RAM that's used for storage by the GPU when the GPU renders a tile. With TBDR, render targets that are never sampled by another target outside of their render pass can effectively remain entirely in the tile RAM and don't require a buffer for a main memory backing store.

The[`VK_MEMORY_PROPERTY_LAZILY_ALLOCATED_BIT`](https://registry.khronos.org/vulkan/specs/1.3-extensions/html/vkspec.html#memory-device-lazy_allocation)was added during creation of appropriate render targets, such as the main color and depth targets, to avoid allocating buffer memory that would never be used. Lazy allocation memory savings in sample scenes was measured to be as high as approximately 50 megabytes of RAM.

### Persistent buffer support

Mobile hardware uses a Unified Memory Architecture (UMA) instead of hardware differentiation between main RAM and graphics RAM. When main RAM and graphics RAM are separate, data must be transferred from main RAM to graphics RAM to be used by the GPU. Godot already implements this transfer process in its Vulkan renderer through the use of staging buffers. On UMA hardware,a staging buffer is unnecessary for many types of data; memory can be used by both the CPU and GPU. The Forge implemented support for persistent shared buffers on supported hardware to eliminate staging when possible.
![Images of a godot scene displaying profiling information with and without persistent buffers enabled.](https://developer.android.com/static/images/cards/distribute/stories/godot_profile.jpg)**Figure 1.**Profiling differences between persistent buffers enabled and disabled in a sample scene.

### ASTC decode mode change

Adaptive scalable texture compression (ASTC) is the preferred modern texture compression format on mobile hardware. During decompression, the GPU by default may decode texels into an intermediate value that is a larger precision than required for visual fidelity, resulting in a loss of texturing efficiency. If supported by the target hardware, the[`VK_EXT_astc_decode_mode`](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VK_EXT_astc_decode_mode.html)extension is used to specify 8-bit unnormalized values per component when decoding instead of 16-bit floating point values.

### Screen pre-rotation

For optimal performance when using Vulkan on Android, games must reconcile the device orientation of the screen with their render surface orientation. This process is referred to as[pre-rotation](https://developer.android.com/games/optimize/vulkan-prerotation). Failure to perform pre-rotation can result in reduced performance due to the Android OS needing to add a compositor pass to manually rotate images. Support for pre-rotation on Android was added to the Godot renderer.

## Debugging improvements

In addition to making performance optimizations, The Forge improved the experience of debugging graphics issues in the Godot renderer with the following additions:

- Device fault extension
- Breadcrumbs
- Debug markers

### Device fault extension

When the GPU encounters an issue during rendering operations, the Vulkan driver can return a`VK_ERROR_DEVICE_LOST`result from a Vulkan API call. By default, no additional context information is provided as to why the driver returned`VK_ERROR_DEVICE_LOST`. The[`VK_EXT_device_fault`](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VK_EXT_device_fault.html)extension provides a mechanism for the driver to provide additional information about the nature of the fault. Godot added support for enabling the device fault extension (if available) and for reporting information returned by the driver.

### Breadcrumbs

A GPU crash or execution stall can be challenging to debug. To help identify what graphical content might have been rendered at the time of a fault,*breadcrumb*support was added to the Godot renderer. Breadcrumbs are user-defined values that can be attached to content in draw lists in the render graph. Breadcrumb data is written before a new render pass is started. If a crash or execution stall occurs, the current breadcrumb value can be used to determine what data may have caused the issue.

### Debug markers

Debug markers, when supported by the driver, are used for naming resources. This allows user-readable strings to be associated with operations like render passes and resources like buffers and texture when using a graphics tool such as RenderDoc. Debug marker annotation support was added to the Godot Vulkan renderer.

## Additional Links

[Godot Engine blog - Update on the Collaboration with Google and The Forge](https://godotengine.org/article/update-on-google-forge-2024/)

[Godot Engine Vulkan collaboration pull request](https://github.com/godotengine/godot/pull/90284)