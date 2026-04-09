---
title: https://developer.android.com/guide/topics/renderscript/migrate/migrate-gles
url: https://developer.android.com/guide/topics/renderscript/migrate/migrate-gles
source: md.txt
---

# Migrate scripts to OpenGL ES 3.1

For workloads where GPU compute is ideal, migrating RenderScript scripts to OpenGL ES (GLES) allows applications written in Kotlin, Java, or using the NDK to take advantage of GPU hardware. A high-level overview follows to help you use OpenGL ES 3.1 compute shaders to replace RenderScript scripts.
| **Note:** Since Vulkan compute - accessible only from the NDK - maximizes control over GPU hardware, it may unlock more performance for your application.

## GLES Initialization

Instead of creating a RenderScript context object, perform the following steps to create a GLES offscreen context using EGL:

1. Get the default display

2. Initialize EGL using the default display, specifying the GLES version.

3. Choose an EGL config with a surface type of[`EGL_PBUFFER_BIT`](https://developer.android.com/reference/android/opengl/EGL14#EGL_PBUFFER_BIT "EGL_PBUFFER_BIT").

4. Use the display and config to create an EGL context.

5. Create the offscreen surface with[`eglCreatePBufferSurface`](https://developer.android.com/reference/android/opengl/EGL14#eglCreatePbufferSurface(android.opengl.EGLDisplay,%20android.opengl.EGLConfig,%20int%5B%5D,%20int) "eglCreatePbufferSurface"). If the context is going to only be used for compute, this can be a trivially small (1x1) surface.

6. Create the render thread and call[`eglMakeCurrent`](https://developer.android.com/reference/android/opengl/EGL14#eglMakeCurrent(android.opengl.EGLDisplay,%20android.opengl.EGLSurface,%20android.opengl.EGLSurface,%20android.opengl.EGLContext) "eglMakeCurrent")in the render thread with the display, surface, and EGL context to bind the GL context to the thread.

The sample app demonstrates how to initialize the GLES context in[`GLSLImageProcessor.kt`](https://developer.android.com/guide/topics/renderscript/migrate/GLES%20Sample). To learn more, see[EGLSurfaces and OpenGL ES](https://source.android.com/docs/core/graphics/arch-egl-opengl).
| **Note:** An alternate method of doing image processing in GLES is to render to an offscreen surface, rather than using GL compute. This example demonstrates using GL for compute, because maps more closely to using RenderScript.

### GLES debug output

Getting useful errors from OpenGL uses an extension to enable debug logging that sets a debug output callback. The method to do this from the SDK,`glDebugMessageCallbackKHR`, has never been implemented, and throws an[exception](https://cs.android.com/android/platform/superproject/main/+/main:frameworks/native/opengl/tools/glgen/stubs/gles11/glDebugMessageCallback.cpp;l=3?q=glDebugMessage&sq&ss=android/platform/superproject/main "Callback Exception"). The[sample app](https://github.com/android/renderscript-samples/blob/main/RenderScriptMigrationSample/app/src/main/java/com/android/example/rsmigration/GLSLImageProcessor.kt "GLES Sample")includes a wrapper for the callback from NDK code.

## GLES Allocations

A RenderScript Allocation can be migrated to an[Immutable storage texture](https://www.khronos.org/opengl/wiki/Texture_Storage#Immutable_storage "Immutable Storage")or a[Shader Storage Buffer Object](https://www.khronos.org/opengl/wiki/Shader_Storage_Buffer_Object "Shader Storage Buffer Object"). For read-only images, you can use a[Sampler Object](https://www.khronos.org/opengl/wiki/Sampler_Object "Sampler Object"), which allows for filtering.

GLES resources are allocated within GLES. To avoid memory copying overhead when interacting with other Android components, there is an extension for[KHR Images](https://registry.khronos.org/EGL/extensions/KHR/EGL_KHR_image_base.txt "KHR Image")that allows the sharing of 2D arrays of image data. This extension has been required for Android devices beginning with Android 8.0. The[graphics-core](https://developer.android.com/jetpack/androidx/releases/graphics)[Android Jetpack](https://developer.android.com/jetpack)library includes support for creating these images within managed code and mapping them to an allocated[`HardwareBuffer`](https://developer.android.com/reference/android/hardware/HardwareBuffer "HardwareBuffer"):  

    val outputBuffers = Array(numberOfOutputImages) {
      HardwareBuffer.create(
        width, height, HardwareBuffer.RGBA_8888, 1,
        HardwareBuffer.USAGE_GPU_SAMPLED_IMAGE
      )
    }
    val outputEGLImages = Array(numberOfOutputImages) { i ->
        androidx.opengl.EGLExt.eglCreateImageFromHardwareBuffer(
            display,
            outputBuffers[i]
        )!!
    }

Unfortunately, this doesn't create the immutable storage texture required for a compute shader to write directly to the buffer. The sample uses[`glCopyTexSubImage2D`](https://developer.android.com/reference/android/opengl/GLES20#glCopyTexSubImage2D(int,%20int,%20int,%20int,%20int,%20int,%20int,%20int) "glCopyTexSubImage2D")to copy the storage texture used by the compute shader into the`KHR Image`. If the OpenGL driver supports the[EGL Image Storage](https://registry.khronos.org/OpenGL/extensions/EXT/EXT_EGL_image_storage.txt "EGL Image Storage")extension, then that extension can be used to create a shared immutable storage texture to avoid the copy.

## Conversion to GLSL compute shaders

Your RenderScript scripts are converted into GLSL compute shaders.

### Write a GLSL compute shader

In OpenGL ES,compute shaders are written in the[OpenGL Shading Language](https://www.khronos.org/opengl/wiki/OpenGL_Shading_Language)(GLSL).
| **Note:** Unlike a RenderScript script, a GLSL compute shader can't have any invokable functions, and must have only one kernel.

### Adaptation of script globals

Based on the characteristics of the script globals, you can either use uniforms or uniform buffer objects for globals that are not modified within the shader:

- [Uniform buffer](https://www.khronos.org/registry/vulkan/specs/1.1-extensions/html/chap14.html#descriptorsets-uniformbuffer): Recommended for frequently-changed script globals of sizes larger than the push constant limit.

For globals that are changed within the shader, you can use use an[Immutable storage texture](https://www.khronos.org/opengl/wiki/Texture_Storage#Immutable_storage "Immutable Storage")or a[Shader Storage Buffer Object](https://www.khronos.org/opengl/wiki/Shader_Storage_Buffer_Object "Shader Storage Buffer Object").

## Execute Computations

Compute shaders aren't part of the graphics pipeline; they are general purpose and designed to compute highly-parallelizable jobs. This lets you have more control over how they execute, but it also means that you have to understand a bit more about how your job is parallelized.

### Create and initialize the compute program

Creating and initializing the compute program has lots in common with working with any other GLES shader.

1. Create the program and the compute shader associated with it.

2. Attach the shader source, compile the shader (and check the results of the compilation).

3. Attach the shader, link the program, and use the program.

4. Create, initialize, and bind any uniforms.

### Start a computation

Compute shaders operate within an abstract 1D, 2D, or 3D space on a series of workgroups, which are defined within the shader source code, and represent the minimum invocation size as well as the geometry of the shader. The following shader works on a 2D image and defines the work groups in two dimensions:  

    private const val WORKGROUP_SIZE_X = 8
    private const val WORKGROUP_SIZE_Y = 8
    private const val ROTATION_MATRIX_SHADER =
        """#version 310 es
        layout (local_size_x = $WORKGROUP_SIZE_X, local_size_y = $WORKGROUP_SIZE_Y, local_size_z = 1) in;

Workgroups can share memory, defined by`GL_MAX_COMPUTE_SHARED_MEMORY_SIZE`, which is at least 32 KB and can make use of`memoryBarrierShared()`to provide coherent memory access.

#### Define workgroup size

Even if your problem space works well with workgroup sizes of 1, setting an appropriate workgroup size is important for parallelizing the compute shader. If the size is too small, the GPU driver may not parallelize your computation enough, for example. Ideally, these sizes should be tuned per-GPU, although reasonable defaults work well enough on current devices, such as the workgroup size of 8x8 in the shader snippet.

There is a`GL_MAX_COMPUTE_WORK_GROUP_COUNT`, but it is substantial; it must be at least 65535 in all three axes according to the specification.

### Dispatch the shader

The final step in executing computations is to dispatch the shader using one of the dispatch functions such as[`glDispatchCompute`](https://developer.android.com/reference/android/opengl/GLES31#glDispatchCompute(int,%20int,%20int) "glDispatchCompute"). The dispatch function is responsible for setting the number of workgroups for each axis:  

    GLES31.glDispatchCompute(
      roundUp(inputImage.width, WORKGROUP_SIZE_X),
      roundUp(inputImage.height, WORKGROUP_SIZE_Y),
      1 // Z workgroup size. 1 == only one z level, which indicates a 2D kernel
    )

To return the value, first wait for the compute operation to finish using a memorybarrier:  

    GLES31.glMemoryBarrier(GLES31.GL_SHADER_IMAGE_ACCESS_BARRIER_BIT)

To chain multiple kernels together, (for example, to migrate code using`ScriptGroup`), create and dispatch multiple programs and synchronize their access to the output with memory barriers.

The[sample app](https://github.com/android/renderscript-samples/blob/main/RenderScriptMigrationSample/app/src/main/java/com/android/example/rsmigration/GLSLImageProcessor.kt "GLES Sample")demonstrates two compute tasks:

- HUE rotation: A compute task with a single compute shader. See`GLSLImageProcessor::rotateHue`for the code sample.
- Blur: A more complex compute task that sequentially executes two compute shaders. See`GLSLImageProcessor::blur`for the code sample.

To learn more about memory barriers, refer to[Ensuring visibility](https://www.khronos.org/opengl/wiki/Memory_Model#Ensuring_visibility)as well as[Shared variables](https://www.khronos.org/opengl/wiki/Compute_Shader#Shared_variables).