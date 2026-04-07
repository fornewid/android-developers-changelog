---
title: https://developer.android.com/guide/topics/renderscript/migrate/migrate-vulkan
url: https://developer.android.com/guide/topics/renderscript/migrate/migrate-vulkan
source: md.txt
---

# Migrate scripts to Vulkan

For workloads where GPU compute is ideal, migrating RenderScript scripts to Vulkan compute gives your app more direct control over GPU hardware, potentially unlocking additional performance compared to other APIs.
| **Note:** Vulkan is only accessible from within the NDK. If you want to use Kotlin or Java to write your GPU compute code, SDK bindings for OpenGL ES 3.1 compute are available.

A high-level overview follows to help you use Vulkan compute shaders to replace RenderScript scripts.

## Vulkan Initialization

Instead of creating a RenderScript context object in Kotlin or Java, perform the following steps to create a Vulkan context using the NDK.

1. Create a Vulkan instance.

2. Choose a Vulkan physical device that supports a compute queue.

3. Create a Vulkan logical device, and get the compute queue.

Optionally, you can set up the Vulkan validation layers on Android to speed up your Vulkan application development.

The sample app demonstrates how to initialize the Vulkan context in[`VulkanContext.h`](https://github.com/android/renderscript-samples/blob/main/RenderScriptMigrationSample/app/src/main/cpp/VulkanContext.h). To learn more, see the[Initialization](https://www.khronos.org/registry/vulkan/specs/1.1-extensions/html/chap4.html#initialization)and[Devices and Queues](https://www.khronos.org/registry/vulkan/specs/1.1-extensions/html/chap5.html#devsandqueues)sections of the Vulkan specification.

## Vulkan Allocations

A RenderScript Allocation can be migrated to a[Vulkan storage image](https://www.khronos.org/registry/vulkan/specs/1.1-extensions/html/chap14.html#descriptorsets-storageimage)or a[Vulkan storage buffer](https://www.khronos.org/registry/vulkan/specs/1.1-extensions/html/chap14.html#descriptorsets-storagebuffer). For better performance with read-only images, use a sampled image with fetch operations, either as a[combined image sampler](https://www.khronos.org/registry/vulkan/specs/1.1-extensions/html/chap14.html#descriptorsets-combinedimagesampler), or with distinct[sampler](https://www.khronos.org/registry/vulkan/specs/1.1-extensions/html/chap14.html#descriptorsets-sampler)and[sampled image](https://www.khronos.org/registry/vulkan/specs/1.1-extensions/html/chap14.html#descriptorsets-sampledimage)bindings.

The Vulkan resources are allocated within Vulkan. To avoid memory copying overhead when interacting with other Android components, consider using the[`VK_ANDROID_external_memory_android_hardware_buffer`extension](https://www.khronos.org/registry/vulkan/specs/1.1-extensions/man/html/VK_ANDROID_external_memory_android_hardware_buffer.html)to import an Android[`AHardwareBuffer`](https://developer.android.com/ndk/reference/group/a-%0Ahardware-buffer#ahardwarebuffer)into Vulkan. This extension is available on all Android devices supporting Vulkan 1.1. For more information, see[`FEATURE_VULKAN_HARDWARE_VERSION`](https://developer.android.com/reference/%0Aandroid/content/pm/PackageManager#FEATURE_VULKAN_HARDWARE_VERSION).

The sample app demonstrates how to create Vulkan resources in[`VulkanResources.h`](https://github.com/android/renderscript-samples/blob/main/RenderScriptMigrationSample/app/src/main/cpp/VulkanResources.h). To learn more, see the[resource creation](https://www.khronos.org/registry/vulkan/specs/1.1-extensions/html/chap12.html#resources)and[resource descriptors](https://www.khronos.org/registry/vulkan/specs/1.1-extensions/html/chap14.html#descriptorsets)sections of the Vulkan specification.

## Conversion to Vulkan compute shaders

Your RenderScript scripts must be converted to Vulkan compute shaders. You may also need to adapt your code depending on the use of RenderScript globals.

### Write a Vulkan compute shader

A Vulkan compute shader is commonly written in[OpenGL Shading Language](https://www.khronos.org/opengl/wiki/OpenGL_Shading_Language)(GLSL) and then compiled to the[Standard Portable Intermediate Representation-V](https://www.khronos.org/opengl/wiki/SPIR-V)(SPIR-V) format.

For detailed information and instructions for integrating shaders into your app, see[Vulkan shader compilers on Android](https://developer.android.com/ndk/guides/graphics/shader-compilers).
| **Note:** Unlike a RenderScript script, a GLSL shader script can't have any invokable functions, and must have only one kernel.

### Adaptation of script globals

Based on the characteristics of the script globals, we recommend using specialization constants, push constants, or uniform buffer objects for globals that are not modified within the shader:

- [Specialization constants](https://www.khronos.org/registry/vulkan/specs/1.1-extensions/html/chap10.html#pipelines-specialization-constants): Recommended for script globals that are mostly consistent across kernel invocations. Changing the value of specialization constants will need to recreate the compute pipeline.
- [Push constants](https://www.khronos.org/registry/vulkan/specs/1.1-extensions/html/chap14.html#descriptorsets-push-constants): Recommended for frequently-changed script globals of sizes smaller than[`maxPushConstantsSize`](https://www.khronos.org/registry/vulkan/specs/1.1-extensions/man/html/VkPhysicalDeviceLimits.html)(guaranteed minimum: 128 bytes).
- [Uniform buffer](https://www.khronos.org/registry/vulkan/specs/1.1-extensions/html/chap14.html#descriptorsets-uniformbuffer): Recommended for frequently-changed script globals of sizes larger than the push constant limit.

For globals that are changed within the shader, you can use either the[Vulkan storage image](https://www.khronos.org/registry/vulkan/specs/1.1-extensions/html/chap14.html#descriptorsets-storageimage)or the[Vulkan storage buffer](https://www.khronos.org/registry/vulkan/specs/1.1-extensions/html/chap14.html#descriptorsets-storagebuffer).

## Computations

You need to create a Vulkan compute pipeline in order to have the GPU execute your compute shader.

### Create a Vulkan compute pipeline

The[`ComputePipeline.h`](https://github.com/android/renderscript-samples/blob/main/RenderScriptMigrationSample/app/src/main/cpp/ComputePipeline.h)file in the sample app demonstrates how to create the Vulkan compute pipeline.

To use a compiled SPIR-V shader in Vulkan, construct a Vulkan compute pipeline as follows:

1. Create a shader module with the compiled SPIR-V shader.
2. Create a descriptor set layout specifying the resource bindings (see[Allocations](https://developer.android.com/guide/topics/renderscript/migrate/migrate-vulkan#allocations)for more details).
3. Create a descriptor set from the descriptor set layout.
4. Create a pipeline layout from the descriptor set layout.
5. Create a compute pipeline with the shader module and pipeline layout.

For more information, see the[Compute Pipelines](https://www.khronos.org/registry/vulkan/specs/1.1-extensions/html/chap10.html#pipelines-compute)section in the Vulkan specification.

### Start a computation

To start the computation with a compute pipeline:

1. Update the descriptor set with the Vulkan resources.
2. Create a Vulkan command buffer, and record the following commands:
   1. Bind the pipeline and the descriptor set.
   2. Dispatch compute workgroups.
3. Submit the command buffer to the compute queue.
4. Wait on the queue, or optionally return a sync fence.

To chain multiple kernels together (for example, to migrate codes using`ScriptGroup`), record them in a single command buffer and synchronize with memory barriers.

The[sample app](https://github.com/android/renderscript-samples/tree/main/RenderScriptMigrationSample/)demonstrates two compute tasks:

- HUE rotation: A simple compute task with a single compute shader. See`ImageProcessor::rotateHue`for the code sample.
- Blur: A more complex compute task that sequentially executes two compute shaders. See`ImageProcessor::blur`for the code sample.

To learn more about command buffers or memory barriers, refer to the sections in the Vulkan specification called[Command Buffers](https://www.khronos.org/registry/vulkan/specs/1.1-extensions/html/chap6.html#commandbuffers)and[Memory Barriers](https://www.khronos.org/registry/vulkan/specs/1.1-extensions/html/chap7.html#synchronization-memory-barriers).