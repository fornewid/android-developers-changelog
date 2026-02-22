---
title: https://developer.android.com/games/optimize/vulkan-reduced-precision
url: https://developer.android.com/games/optimize/vulkan-reduced-precision
source: md.txt
---

The numerical format of graphics data and shader calculations can have a
significant impact on the performance of your game.

Optimal formats do the following:

- Increase efficiency of GPU cache use
- Reduce memory bandwidth consumption, saving power and increasing performance
- Maximize computational throughput in shader programs
- Minimize CPU RAM usage of your game

| **Note:** Guidance on this page is for Vulkan 1.1 or higher.

## Floating point formats

The majority of calculations and data in modern 3D graphics use floating point
numbers. Vulkan on Android uses floating point numbers that are 32 or
16 bits in size. A 32-bit floating point number is commonly referred to as
single precision or full precision; a 16-bit floating point number, half
precision.

Vulkan defines a 64-bit floating point type, but the type is not commonly
supported by Vulkan devices on Android, and its use is not recommended. A 64-bit
floating point number is commonly referred to as double precision.

## Integer formats

Signed and unsigned integer numbers are also used for data and calculations. The
standard integer size is 32 bits. Support for other bit sizes is device
dependent. Vulkan devices running Android commonly support 16-bit and 8-bit
integers. Vulkan defines a 64-bit integer type, but the type is not commonly
supported by Vulkan devices on Android, and its use is not recommended.

## Suboptimal half-precision behavior

Modern GPU architectures combine two 16-bit values together in a 32-bit pair and
implement instructions that operate on the pair. For optimal performance, avoid
using scalar 16-bit float variables; vectorize data into two- or four-element
vectors. The shader compiler may be able to use scalar values in vector
operations. However, if you rely on the compiler to optimize scalars, inspect
the compiler output to verify vectorization.

Converting to and from 32-bit and 16-bit\&#ndash;precision floating point has a
computational cost. Reduce overhead by minimizing precision conversions in your
code.

Benchmark performance differences between 16-bit and 32-bit versions of your
algorithms. Half precision does not always result in a performance improvement,
especially for complicated calculations. Algorithms that make heavy use of fused
multiply-add (FMA) instructions on vectorized data are good candidates for
improved performance at half precision.

## Numerical format support

All Vulkan devices on Android support single-precision, 32-bit floating point
numbers and 32-bit integer numbers in data and shader calculations. Support for
other formats is not guaranteed to be available and if available, not guaranteed
for all use cases.

Vulkan has two categories of support for optional numeric formats: arithmetic
and storage. Before using a specific format, ensure a device supports it in both
categories.

### Arithmetic support

A Vulkan device must declare arithmetic support for a numeric format for it to
be usable in shader programs. Vulkan devices on Android commonly support the
following formats for arithmetic:

- 32-bit integer (mandatory)
- 32-bit floating point (mandatory)
- 8-bit integer (optional)
- 16-bit integer (optional)
- 16-bit half-precision floating point (optional)

To determine if a Vulkan device supports 16-bit integers for arithmetic,
retrieve the device's features by calling the
[vkGetPhysicalDeviceFeatures2()](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/vkGetPhysicalDeviceFeatures2.html) function and checking whether
the `shaderInt16` field in the [VkPhysicalDeviceFeatures2](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VkPhysicalDeviceFeatures2.html)
result structure is true.
| **Note:** Support for `shaderInt16` and for version 1.1 of the Vulkan API is required by the 2022 [Android Baseline profile](https://developer.android.com/ndk/guides/graphics/android-baseline-profile) for Vulkan.

To determine whether a Vulkan device supports 16-bit floats or 8-bit integers,
perform the following steps:

1. Check whether the device supports the [VK_KHR_shader_float16_int8](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VK_KHR_shader_float16_int8.html) Vulkan extension. The extension is required for 16-bit float and 8-bit integer support.
2. If `VK_KHR_shader_float16_int8` is supported, append a [VkPhysicalDeviceShaderFloat16Int8Features](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VkPhysicalDeviceShaderFloat16Int8Features.html) structure pointer to a `VkPhysicalDeviceFeatures2.pNext` chain.
3. Check the `shaderFloat16` and `shaderInt8` fields of the `VkPhysicalDeviceShaderFloat16Int8Features` result structure after calling `vkGetPhysicalDeviceFeatures2()`. If the field value is `true`, the format is supported for shader program arithmetic.

| **Note:** To use 16-bit floats or 8-bit integers in your shaders, you *must* include `VK_KHR_shader_float16_int8` in a list of required extensions when you call the [vkCreateDevice()](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/vkCreateDevice.html) function.

While not a requirement in Vulkan 1.1 or the 2022
[Android Baseline profile](https://developer.android.com/ndk/guides/graphics/android-baseline-profile), support for the `VK_KHR_shader_float16_int8`
extension is very common on Android devices.

### Storage support

A Vulkan device must declare support for an optional numeric format for
specific storage types. The [VK_KHR_16bit_storage](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VK_KHR_16bit_storage.html) extension
declares support for 16-bit integer and 16-bit floating-point formats. Four
storage types are defined by the extension. A device can support 16-bit numbers
for none, some, or all storage types.

The storage types are:

- Storage buffer objects
- Uniform buffer objects
- Push constant blocks
- Shader input and output interfaces

| **Note:** Although `VK_KHR_16bit_storage` is included in core Vulkan 1.1, actual 16-bit format support for storage is optional. Check whether a device supports 16-bit formats for a given storage type before use.

Most, but not all, Vulkan 1.1 devices on Android support 16-bit formats in
storage buffer objects. Don't assume support based on the GPU model. Devices
with older drivers for a given GPU might not support storage buffer objects,
while devices with newer drivers do.

Support for 16-bit formats in uniform buffers, push constant blocks, and shader
input/output interfaces is generally dependent on the GPU manufacturer. On
Android, a GPU typically either supports all three of these types or none of
them.

An example function that tests for Vulkan arithmetic and storage format support:  

    struct ReducedPrecisionSupportInfo {
      // Arithmetic support
      bool has_8_bit_int_ = false;
      bool has_16_bit_int_ = false;
      bool has_16_bit_float_ = false;
      // Storage support
      bool has_16_bit_SSBO_ = false;
      bool has_16_bit_UBO_ = false;
      bool has_16_bit_push_ = false;
      bool has_16_bit_input_output_ = false;
      // Use 16-bit floats if we have arithmetic
      // support and at least SSBO storage support.
      bool use_16bit_floats_ = false;
    };

    void CheckFormatSupport(VkPhysicalDevice physical_device,
        ReducedPrecisionSupportInfo &info) {

      // Retrieve the device extension list so we
      // can check for our desired extensions.
      uint32_t device_extension_count;
      vkEnumerateDeviceExtensionProperties(physical_device, nullptr,
          &device_extension_count, nullptr);
      std::vector<VkExtensionProperties> device_extensions(device_extension_count);
      vkEnumerateDeviceExtensionProperties(physical_device, nullptr,
          &device_extension_count, device_extensions.data());

      bool has_16_8_extension = HasDeviceExtension("VK_KHR_shader_float16_int8",
          device_extensions);

      // Initialize the device features structure and
      // chain the storage features structure and 8/16-bit
      // support structure if applicable.
      VkPhysicalDeviceFeatures2 device_features;
      memset(&device_features, 0, sizeof(device_features));
      device_features.sType = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FEATURES_2;

      VkPhysicalDeviceShaderFloat16Int8Features f16_int8_features;
      memset(&f16_int8_features, 0, sizeof(f16_int8_features));
      f16_int8_features.sType =
          VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FLOAT16_INT8_FEATURES_KHR;

      VkPhysicalDevice16BitStorageFeatures storage_features;
      memset(&storage_features, 0, sizeof(storage_features));
      storage_features.sType =
          VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_16BIT_STORAGE_FEATURES;
      device_features.pNext = &storage_features;

      if (has_16_8_extension) {
        storage_features.pNext = &f16_int8_features;
      }

      vkGetPhysicalDeviceFeatures2(physical_device, &device_features);

      // Parse the storage features and determine
      // what kinds of 16-bit storage access are available.
      if (storage_features.storageBuffer16BitAccess ||
          storage_features.uniformAndStorageBuffer16BitAccess) {
        info.has_16_bit_SSBO_ = true;
      }
      info.has_16_bit_UBO_ = storage_features.uniformAndStorageBuffer16BitAccess;
      info.has_16_bit_push_ = storage_features.storagePushConstant16;
      info.has_16_bit_input_output_ = storage_features.storageInputOutput16;

      info.has_16_bit_int_ = device_features.features.shaderInt16;
      if (has_16_8_extension) {
        info.has_16_bit_float_ = f16_int8_features.shaderFloat16;
        info.has_8_bit_int_ = f16_int8_features.shaderInt8;
      }

      // Get arithmetic and at least some form of storage
      // support before enabling 16-bit float usage.
      if (info.has_16_bit_float_ && info.has_16_bit_SSBO_) {
        info.use_16bit_floats_ = true;
      }
    }

## Precision level for data

A half-precision floating point number can represent a smaller range of values
at a lower precision than a single-precision floating point number.
Half-precision is often a simple and perceptually lossless choice over
single-precision. However, half-precision may not be practical in all use cases.
For some types of data, the reduced range and precision can result in graphic
artifacts or incorrect rendering.

Data types that are good candidates for representation in half-precision
floating point include:

- Position data in local space coordinates
- Texture UVs for smaller textures with limited UV wrapping that can be constrained to a -1.0 to 1.0 coordinate range
- Normal, tangent, and bitangent data
- Vertex color data
- Data with low precision requirements centered on 0.0

Data types that are *not* recommended for representation in half-precision float
include:

- Position data in global world coordinates
- Texture UVs for high-precision use cases like UI element coordinates in an atlas sheet

## Precision in shader code

The [OpenGL Shading Language (GLSL)](https://www.khronos.org/opengl/wiki/OpenGL_Shading_Language) and
[High-level Shader Language](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl) (HLSL) shader
programming languages support specification of relaxed
precision or explicit precision for numeric types. Relaxed precision is treated
as a recommendation for the shader compiler. Explicit precision is a
requirement of the specified precision. Vulkan devices on Android generally use
16-bit formats when suggested by relaxed precision. Other Vulkan devices,
especially on desktop computers using graphics hardware lacking support
for 16-bit formats, may ignore relaxed precision and still use 32-bit formats.

#### Storage extensions in GLSL

The appropriate GLSL extensions must be defined to enable support for 16-bit or
8-bit numeric formats in storage and uniform buffer structures. The relevant
extension declarations are:  

    // Enable 16-bit formats in storage and uniform buffers.
    #extension GL_EXT_shader_16bit_storage : require
    // Enable 8-bit formats in storage and uniform buffers.
    #extension GL_EXT_shader_8bit_storage : require

These extensions are specific to GLSL and don't have an equivalent in HLSL.

### Relaxed precision in GLSL

Use the `highp` qualifier before a floating point type to suggest a
single-precision float and the `mediump` qualifier for a half-precision float.
GLSL compilers for Vulkan interpret the legacy `lowp` qualifier as `mediump`.
Some examples of relaxed precision:  

    mediump vec4 my_vector; // Suggest 16-bit half precision
    highp mat4 my_matrix;   // Suggest 32-bit single precision

### Explicit precision in GLSL

Include the `GL_EXT_shader_explicit_arithmetic_types_float16` extension in your
GLSL code to enable use of 16-bit floating point types:  

    #extension GL_EXT_shader_explicit_arithmetic_types_float16 : require

Declare 16-bit floating point scalar, vector, and matrix types in GLSL using the
following keywords:  

    float16_t   f16vec2     f16vec3    f16vec4
    f16mat2     f16mat3     f16mat4
    f16mat2x2   f16mat2x3   f16mat2x4
    f16mat3x2   f16mat3x3   f16mat3x4
    f16mat4x2   f16mat4x3   f16mat4x4

Declare 16-bit integer scalar and vector types in GLSL using the following
keywords:  

    int16_t     i16vec2     i16vec3    i16vec4
    uint16_t    u16vec2     u16vec3    u16vec4

### Relaxed precision in HLSL

HLSL uses the term *minimal precision* instead of relaxed precision. A minimal
precision type keyword specifies the minimum precision, but the compiler may
substitute a higher precision if higher precision is a better choice for the
target hardware. A minimal precision 16-bit float is specified by the
`min16float` keyword. Minimal precision signed and unsigned 16-bit integers are
specified by the `min16int` and `min16uint` keywords respectively. Additional
examples of minimal precision declarations include the following:  

    // Four element vector and four-by-four matrix types
    min16float4 my_vector4;
    min16float4x4 my_matrix4x4;

### Explicit precision in HLSL

Half-precision floating-point is specified by the `half` or `float16_t`
keywords. Signed and unsigned 16-bit integers are specified by the `int16_t`
and `uint16_t` keywords respectively. Additional examples of explicit precision
declarations include the following:  

    // Four element vector and four-by-four matrix types
    half4 my_vector4;
    half4x4 my_matrix4x4;

| **Note:** When using the open source [DirectXShaderCompiler](https://github.com/microsoft/DirectXShaderCompiler) to compile HLSL code for Vulkan using 16-bit types, the  
| `-enable-16bit-types` command line option *must* be used to enable support for 16-bit numeric formats.