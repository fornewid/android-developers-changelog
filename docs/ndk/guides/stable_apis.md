---
title: https://developer.android.com/ndk/guides/stable_apis
url: https://developer.android.com/ndk/guides/stable_apis
source: md.txt
---

# Native APIs

This page gives an overview of the libraries included in the NDK, with links to the relevant parts of the NDK API reference, and to guides where they exist.

## Use native APIs

There are two steps to using a library that the NDK provides:

1. Tell the build system to link against the library.

   - If you are using[ndk-build](https://developer.android.com/ndk/guides/ndk-build): Add the library to`LOCAL_LDLIBS`in your[Android.mk](https://developer.android.com/ndk/guides/android_mk). Note that you strip the leading`lib`and say`-l`instead. For example, to link against`libfoo`and`libbar`, you'd write:`makefile
     LOCAL_LDLIBS := -lfoo -lbar`

     For more about`LOCAL_LDLIBS`, see the[Android.mk docs](https://developer.android.com/ndk/guides/android_mk)documentation.
   - If you are using[CMake](https://developer.android.com/ndk/guides/cmake): Follow the instructions in Studio's[Add NDK APIs](https://developer.android.com/studio/projects/configure-cmake#add-ndk-api)documentation.

2. `#include`the appropriate headers from your code.

Note that APIs which are newer than your application's`minSdkVersion`won't be callable by default, and you must instead use them via[`dlopen()`](https://man7.org/linux/man-pages/man3/dlopen.3.html)and`dlsym()`. For an easier approach, see[Using newer APIs](https://developer.android.com/ndk/guides/using-newer-apis).

## Core C/C++

### C library

The standard C11 library headers such as`<stdlib.h>`and`<stdio.h>`are available as usual.

Note that on Android, unlike Linux, there are no separate`libpthread`or`librt`libraries. That functionality is included directly in`libc`, which does not need to be explicitly linked against.

There is a separate`libm`for math functions (following the usual Unix tradition), but like`libc`this is automatically linked by the build systems.

Dynamic linker functionality in`<dlfcn.h>`such as dlopen(3) and dlsym(3) is available, but you must explicitly link against`libdl`.

Library:`libc`/`libm`/`libdl`

### C++ library

C++17 support is available. For more information on C++ library support, see[C++ library support](https://developer.android.com/ndk/guides/cpp-support).

### Logging

`<android/log.h>`contains APIs for logging to logcat.
| **Note:** `<android/log.h>`only provides logging primitives. For examples of more usable APIs, see Android's[`log/log.h`](https://android.googlesource.com/platform/system/logging/+/refs/heads/master/liblog/include/log/log.h)and[`android-base/logging.h`](https://cs.android.com/android/platform/superproject/+/master:system/libbase/include/android-base/logging.h).

Available since API level 3.

Library:`liblog`

Reference:[Logging](https://developer.android.com/ndk/reference/group/logging)

### Trace

The native tracing API`<android/trace.h>`provides the native equivalent of the`android.os.Trace`class in the Java programming language. This API lets you trace named units of work in your code by writing trace events to the system trace buffer. You can then collect and analyze the trace events using the[Systrace tool](https://developer.android.com/topic/performance/tracing/command-line).

Available since API level 23.

Library:`libandroid`

Guide:[Native Tracing](https://developer.android.com/ndk/guides/tracing)

### zlib compression

You can use the[Zlib compression library](http://www.zlib.net/manual.html)by including`<zlib.h>`and linking against`libz`.

The NDK always includes the latest zlib header files at the time of release, and the`libz.a`included in the NDK for*static* linking is always that same version, but the`libz.so`for*dynamic* linking comes from the device, and be whatever version happened to be released on that device. In particular, this means that the headers you built against do not match the version of zlib on the device, so the usual warnings against making assumptions about implementation details are especially valid here. We are not aware of any issues with public API, but struct layout in particular has changed over time and will likely continue to do so. Note that new API in later zlib versions will obviously not be available on OS versions that predate the API. It is possible to avoid all these problems (at the cost of increased APK size) by always using the static`libz.a`instead of`libz.so`.

Available since API level 3 (but see note above).

Library:`libz`

## Graphics

### OpenGL ES 1.0 - 3.2

The standard OpenGL ES 1.x headers (`<GLES/gl.h>`and`<GLES/glext.h>`), 2.0 headers (`<GLES2/gl2.h>`and`<GLES2/gl2ext.h>`), 3.0 headers (`<GLES3/gl3.h>`and`<GLES3/gl3ext.h>`), 3.1 headers (`<GLES3/gl31.h>`and`<GLES3/gl3ext.h>`), and 3.2 headers (`<GLES3/gl32.h>`and`<GLES3/gl3ext.h>`) contain the declarations necessary for OpenGL ES.

To use OpenGL ES 1.x, link your native module to`libGLESv1_CM`.

To use OpenGL ES 2.0, link your native module to`libGLESv2`.

To use OpenGL ES 3.x, link your native module to`libGLESv3`.

All Android-based devices support OpenGL ES 1.0 and 2.0.

Only Android devices that have the necessary GPU fully support later versions of OpenGL ES, but the libraries are present on all devices that support the API level where they were introduced. It's safe to link against the libraries, but an app must query the OpenGL ES version string and extension string to determine whether the current device supports the features it needs. For information on how to perform this query, see the description of[`glGetString()`](http://www.khronos.org/opengles/sdk/1.1/docs/man/glGetString.xml)in the OpenGL specification.

Additionally, you must put a[`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element)tag in your manifest file to indicate the version of[OpenGL ES](https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl#manifest)that you require.

OpenGL ES 1.0 is available since API level 4.

OpenGL ES 2.0 is available since API level 5.

OpenGL ES 3.0 is available since API level 18.

OpenGL ES 3.1 is available since API level 21.

OpenGL ES 3.2 is available since API level 24.

### EGL

EGL provides a native platform interface via the`<EGL/egl.h>`and`<EGL/eglext.h>`headers for allocating and managing OpenGL ES contexts and surfaces.

EGL allows you to perform the following operations from native code:

- List supported EGL configurations.
- Allocate and release OpenGL ES surfaces.
- Create and destroy OpenGL ES contexts.
- Swap or flip surfaces.

API level 24 added support for the[`EGL_KHR_mutable_render_buffer`](https://www.khronos.org/registry/EGL/extensions/KHR/EGL_KHR_mutable_render_buffer.txt),[`ANDROID_create_native_client_buffer`](https://www.khronos.org/registry/EGL/extensions/ANDROID/EGL_ANDROID_create_native_client_buffer.txt), and[`ANDROID_front_buffer_auto_refresh`](https://www.khronos.org/registry/EGL/extensions/ANDROID/EGL_ANDROID_front_buffer_auto_refresh.txt)extensions.

Available since API level 9.

Library:`libEGL`

Guide:[EGL Native Platform Interface](http://www.khronos.org/egl)

### Vulkan

Vulkan is a low-overhead, cross-platform API for high-performance 3D graphics rendering. Vulkan is an[open standard](https://www.khronos.org/vulkan/)maintained by the Khronos Group. The standard`<vulkan/vulkan.h>`header file contains the declarations needed to perform Vulkan rendering calls from your code.

For code samples, see the LunarG[VulkanSamples](https://github.com/LunarG/VulkanSamples)and[android-vulkan-tutorials](https://github.com/googlesamples/android-vulkan-tutorials)projects on GitHub.

The Vulkan library is present on all devices supporting API level 24 or later, but apps must check at runtime that the necessary GPU hardware support is available. Devices without Vulkan support will return zero devices from[`vkEnumeratePhysicalDevices`](https://www.khronos.org/registry/vulkan/specs/1.1/html/vkspec.html#vkEnumeratePhysicalDevices).

Available since API level 24.

Library:`libvulkan`

Guide:[Vulkan graphics API guide](https://developer.android.com/ndk/guides/graphics)

### Bitmaps

The`libjnigraphics`library exposes API that allows access to the pixel buffers of Java`Bitmap`objects. The workflow is as follows:

1. Call`AndroidBitmap_getInfo()`to retrieve information, such as width and height, about a given bitmap handle.

2. Call`AndroidBitmap_lockPixels()`to lock the pixel buffer and retrieve a pointer to it. Doing so ensures that the pixels do not move until the app calls`AndroidBitmap_unlockPixels()`.

3. Modify the pixel buffer as appropriate for its pixel format, width, and other characteristics.

4. Call`AndroidBitmap_unlockPixels()`to unlock the buffer.

Available since API level 8.

Library:`libjnigraphics`

Reference:[Bitmap API reference](https://developer.android.com/ndk/reference/group/bitmap)

### Sync API

Available since API level 26.

Library:`libsync`

Reference:[Sync API reference](https://developer.android.com/ndk/reference/group/sync)

## Camera

The native camera APIs perform fine-grained photo capture and processing. Unlike the Java camera2 API, the native camera API does not support deprecated camera HAL 1.0 implementations (that is, the available camera list in the native camera API won't list camera devices that have the[LEGACY](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#INFO_SUPPORTED_HARDWARE_LEVEL_LEGACY)hardware level).

Available since API level 24.

Library:`libcamera2ndk`

Reference:[Camera API reference](https://developer.android.com/ndk/reference/group/camera)

## Media

### libmediandk

The Media APIs provide low-level native interfaces similar to`MediaExtractor`,`MediaCodec`and other related Java APIs.

Library:`libmediandk`

Reference:[Media API reference](https://developer.android.com/ndk/reference/group/media)

### OpenMAX AL

| **Note:** Use of OpenMAX AL is no longer recommended. New code should instead use the Android Media APIs.

Android native multimedia handling is based on Khronos Group OpenMAX AL 1.0.1 API.

The standard OpenMAX AL headers`<OMXAL/OpenMAXAL.h>`and`<OMXAL/OpenMAXAL_Platform.h>`contain the declarations necessary for performing multimedia output from the native side of Android.

The NDK distribution of OpenMAX AL also provides Android-specific extensions. For information about these extensions, see the comments in`<OMXAL/OpenMAXAL_Android.h>`.

Available since API level 14.

Library:`libOpenMAXAL`

## Android native application APIs

For more information, see the[Android NDK API reference](https://developer.android.com/ndk/reference)documentation.

APIs include:

- [Asset](https://developer.android.com/ndk/reference/group/asset)
- [Choreographer](https://developer.android.com/ndk/reference/group/choreographer)
- [Configuration](https://developer.android.com/ndk/reference/group/configuration)
- [Input](https://developer.android.com/ndk/reference/group/input)
- [Looper](https://developer.android.com/ndk/reference/group/looper)
- [Native Activity](https://developer.android.com/ndk/reference/group/native-activity)
- [Native Hardware Buffers](https://developer.android.com/ndk/reference/group/a-hardware-buffer)
- [Native Window](https://developer.android.com/ndk/reference/group/a-native-window)
- [Memory](https://developer.android.com/ndk/reference/group/memory)
- [Networking](https://developer.android.com/ndk/reference/group/networking)
- [Sensor](https://developer.android.com/ndk/reference/group/sensor)
- [Storage](https://developer.android.com/ndk/reference/group/storage)
- [SurfaceTexture](https://developer.android.com/ndk/reference/group/surface-texture)

Library:`libandroid`

Library:`libnativewindow`for more recent Native Window functionality

Full reference:[Android NDK API reference](https://developer.android.com/ndk/reference)

### Binder APIs

Binder APIs allow you to create communication channels between processes. This is the low level implementation of Android interprocess communication. When possible, prefer higher-level components. However, this library is available for advanced use cases.

Library:`libbinder_ndk`

Reference:[Binder](https://developer.android.com/ndk/reference/group/ndk-binder)

### Hardware Buffer APIs

There are two native APIs that let you create your own pipelines for cross-process buffer management.

The native hardware buffer API[`<android/hardware_buffer.h>`](https://developer.android.com/ndk/reference/hardware__buffer_8h)lets you directly allocate buffers to create your own pipelines for cross-process buffer management. You can allocate an`AHardwareBuffer`and use it to obtain an[`EGLClientBuffer`](https://www.khronos.org/registry/EGL/extensions/KHR/EGL_KHR_image_base.txt)resource type via the`eglGetNativeClientBufferANDROID`extension. You can pass that buffer to[`eglCreateImageKHR`](https://www.khronos.org/registry/EGL/extensions/KHR/EGL_KHR_image_base.txt)to create an[`EGLImage`](https://www.khronos.org/registry/EGL/extensions/KHR/EGL_KHR_image_base.txt)resource type, which may then be bound to a texture via[`glEGLImageTargetTexture2DOES`](https://www.khronos.org/registry/OpenGL/extensions/OES/OES_EGL_image.txt)on supported devices. This can be useful for creating textures that may be shared cross-process.

The native hardware buffer JNI API (`<android/hardware_buffer_jni.h>`) lets you obtain a[`HardwareBuffer`](https://developer.android.com/reference/android/hardware/HardwareBuffer)object, which is a[Parcelable](https://developer.android.com/reference/android/os/Parcelable)and thus may be transported between two different processes. This gives your app similar capabilities to[SurfaceFlinger](https://source.android.com/devices/graphics/arch-sf-hwc.html#surfaceflinger)such as creating your own queue of buffers between processes without accessing internal Android APIs.

## Audio

| **Note:** Developers should consider using the open source Oboe library which is available on[GitHub](https://github.com/google/oboe). Oboe is a C++ wrapper that provides an API that closely resembles AAudio. It calls AAudio when it is available, and falls back to OpenSL ES if AAudio is not available.

### AAudio

AAudio is the currently-supported native audio API. It replaced OpenSL ES, and provides better support for high-performance audio apps that require low-latency audio.

Available since API level 26.

Library:`libaaudio`

Guide:[AAudio API guide](https://developer.android.com/ndk/guides/audio/aaudio/aaudio)

Reference:[AAudio API reference](https://developer.android.com/ndk/reference/group/audio)

### OpenSL ES

OpenSL ES is another native audio API which is also supported, but see the note at the Guide below.

Available since API level 9. API level 14 added PCM support.

Library:`libOpenSLES`

Guide:[OpenSL ES for Android guide](https://developer.android.com/ndk/guides/audio/opensl/opensl-for-android)

## Neural Networks API

The Neural Networks API (NNAPI) provides apps with hardware acceleration for on-device machine learning operations. The API supports on-device model creation, compilation, and execution. Apps typically do not use NNAPI directly; instead, the API is meant to be called by machine learning libraries, frameworks, and tools that let developers train their models and deploy them on Android devices.

Available since API level 27.

Library:`libneuralnetworks`

Guide:[Neural Networks guide](https://developer.android.com/ndk/guides/neuralnetworks)

Reference:[Neural Networks API reference](https://developer.android.com/ndk/reference/group/neural-networks)