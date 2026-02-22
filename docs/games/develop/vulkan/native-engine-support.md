---
title: https://developer.android.com/games/develop/vulkan/native-engine-support
url: https://developer.android.com/games/develop/vulkan/native-engine-support
source: md.txt
---

## Get started with Vulkan on Android

Vulkan is the primary low-level graphics API on Android. Vulkan provides optimal
performance for games that implement their own game engine and renderer.

To successfully implement Vulkan in your game engine you must:

- Identify which Android devices to use with Vulkan
- Understand the tradeoffs of supporting older Android devices
- Add Vulkan to your Android build target
- Choose a shader compiler to create SPIR-V for Vulkan
- Determine the available Vulkan API version at runtime
- Learn how to optimize your Vulkan rendering operations with Vulkan profiles, frame pacing, and pre-rotation
- Select graphics tools for debugging and performance analysis

<!-- -->

**Note:** For information on using Vulkan on Android with the Unity or Unreal game engines, see:
- [Vulkan on Unity](https://developer.android.com/games/develop/vulkan/game-engine-support#unity)
- [Vulkan on Unreal](https://developer.android.com/games/develop/vulkan/game-engine-support#unreal)

## Choose minimum device specifications for Vulkan

Vulkan is available on Android beginning with Android 7.0 (API level 24). Not
all Android devices running Android 7.0 or higher support Vulkan. You need to
determine which Vulkan-capable Android devices your game supports.

### Recommendations

Use the following specifications as minimum requirements for Vulkan support:

- Device is running Android 10.0 (API level 29) or higher
- Device supports Vulkan API version 1.1 or higher
- Device has hardware capabilities and features compatible with the 2022 [Android Baseline profile](https://developer.android.com/ndk/guides/graphics/android-baseline-profile)

| **Note:** Vulkan 1.1 support is a requirement for *new* 64-bit Android devices beginning with Android 10.0. The 2022 Android Baseline profile also sets a minimum Vulkan API version of 1.1. Most, but not all, Vulkan 1.1--capable devices are compatible with the 2022 Android Baseline profile. For compatibility statistics, visit the [Distribution dashboard](https://developer.android.com/about/dashboards#Vulkan).

### Older device support

If your game is designed to run on a wide range of devices with varying levels
of graphics capabilities, you may need to support devices older than those
recommended in [Choose minimum devices specifications for Vulkan](https://developer.android.com/games/develop/vulkan/native-engine-support#choose-minimum).
Before building support for older devices, evaluate whether Vulkan provides
benefits to your game. Games that have lots of draw calls and that use OpenGL ES
can see significant driver overhead due to the high cost of making draw calls
within OpenGL ES. These games can become CPU bound from spending large portions
of their frame time in the graphics driver. The games can also see significant
reductions in CPU and power use by switching from OpenGL ES to Vulkan. This is
especially applicable if your game has complex scenes that can't effectively use
instancing to reduce draw calls. When targeting older devices, include OpenGL ES
rendering support as a fallback, as some devices in your target device list may
have Vulkan implementations that can't run your game reliably.

You may not want to support older Vulkan-capable devices because they lack
performance and features or have stability issues.

#### Performance and Features

Older Vulkan-capable Android devices may not have the rendering performance or
hardware support for features needed to run your game. This is especially likely
if your game has high-fidelity graphics and Vulkan is the only API you are
targeting on Android. Many older devices are limited to version 1.0.3 of the
Vulkan API and are often missing widely used Vulkan extensions available on more
modern hardware.

#### Stability

Older Android devices could be using out-of-date Vulkan drivers. These driver
versions might include bugs that can affect the stability of your game. Working
around driver bugs can involve significant amounts of testing and engineering
time.

## Add Vulkan to your project

To add Vulkan to your project you need to:

- Include Vulkan API headers
- Compile shader code to SPIR-V
- Call the Vulkan API at runtime

### Include Vulkan API headers

Your game needs to include the Vulkan API header files to compile code that uses
Vulkan. You can find a copy of the Vulkan headers in the [Android NDK](https://developer.android.com/ndk) or
packaged in [Vulkan SDK releases](https://www.vulkan.org/tools#download-these-essential-development-tools). Any particular NDK version
only includes Vulkan headers available at the time of the NDK release. If you
use Vulkan headers from the NDK, use NDK version 25 or higher, which includes
header files that support Vulkan version 1.3. The Vulkan SDK has the most
current version of the headers.

### Compile shader code to SPIR-V

The Vulkan API expects shader programs to be provided in the SPIR-V binary
intermediate format. This convention is different from OpenGL ES, where you
could submit source code written in the
[OpenGL Shading Language](https://www.khronos.org/opengl/wiki/OpenGL_Shading_Language) (GLSL) as text
strings. Use a shader compiler to take code written in a shader
language such as GLSL or the [High-level Shader Language](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl) (HLSL)
and compile it into SPIR-V modules for use with Vulkan.

The [shaderc](https://github.com/google/shaderc) compiler can be used to compile shader programs
written in GLSL into SPIR-V. If your game uses HLSL, the
[DirectXShaderCompiler](https://github.com/microsoft/DirectXShaderCompiler) supports SPIR-V output. Typically, you
compile shader programs offline as part of the asset build process for
your game and include the SPIR-V modules as part of your runtime assets.

### Call the Vulkan API at runtime

To call the Vulkan API, your game needs to obtain function pointers to Vulkan
API calls. The most straightforward way to do this is to link against the
`libvulkan.so` shared library, which is included in the Android NDK. Linking
against the library has two shortcomings: additional function dispatch overhead
and limitations on which Vulkan API function pointers are automatically
resolved.

When you call a Vulkan API function, control passes through a [dispatch
table](https://github.com/KhronosGroup/Vulkan-Loader/blob/main/docs/LoaderInterfaceArchitecture.md#dispatch-tables-and-call-chains) managed by a construct called the Vulkan loader. Android
uses its own [Vulkan loader](https://cs.android.com/android/platform/superproject/main/+/main:frameworks/native/vulkan/libvulkan/) implementation and not the LunarG
loader. This loader system is part of the layer architecture of the Vulkan API.
Linking to the system library at build time results in an additional dispatch
level for a given API call. While the overhead is small, it can be noticeable
for games that perform high volumes of Vulkan calls.

The system library generally only resolves pointers to Vulkan functions that are
considered part of the core API. Vulkan has a large number of extensions, which
define additional Vulkan functions, many of which are not automatically resolved
by the system library. You need to manually resolve pointers to these Vulkan
functions before using them.

To mitigate these issues, dynamically resolve pointers to all Vulkan functions
you intend to use at runtime. One way to accomplish this is by using an
open source meta-loader library such as [volk](https://github.com/zeux/volk). The
[AGDKTunnel](https://github.com/android/games-samples/tree/main/agdk/agdktunnel) sample game integrates volk for this purpose. If
you are using a meta-loader library, don't link against the `libvulkan.so`
shared library in your build scripts.

## Determine the available Vulkan API version

Android supports the following Vulkan API versions:

- 1.0.3
- 1.1
- 1.3

The highest Vulkan API version number available on a given device is determined
by Android version and Vulkan driver support.

### Android version

Platform support for a Vulkan API version is dependent on a minimum Android
version (API level):

- 1.3 --- Android 13.0 (API level 33) and higher
- 1.1 --- Android 10.0 (API level 29) and higher
- 1.0.3 --- Android 7.0 (API level 24) and higher

### Vulkan driver support

Android platform support for a Vulkan API version does not guarantee the API
version is supported by the device's Vulkan driver. A device running Android 13
might only support version 1.1 of the Vulkan API.

When initializing Vulkan, don't request an API version greater than:

- The maximum Vulkan API version for the version of Android running on the device
- The Vulkan API version reported by [vkEnumerateInstanceVersion](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/vkEnumerateInstanceVersion.html)
- The Vulkan API version reported by the `apiVersion` property of the [VkPhysicalDeviceProperties](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VkPhysicalDeviceProperties.html) structure

An example of determining the highest supported Vulkan API version follows:  

    // Minimum Android API levels for Vulkan 1.3/1.1 version support
    static constexpr int kMinimum_vk13_api_level = 33;
    static constexpr int kMinimum_vk11_api_level = 29;

    uint32_t GetHighestSupportedVulkanVersion(VkPhysicalDevice physical_device) {
      uint32_t instance_api_version = 0;
      vkEnumerateInstanceVersion(&instance_api_version);

      VkPhysicalDeviceProperties device_properties;
      vkGetPhysicalDeviceProperties(physical_device, &device_properties);

      // Instance and device versions don't have to match, use the lowest version
      // number for API support if they don't.
      const uint32_t driver_api_version =
          (instance_api_version < device_properties.apiVersion) ?
          instance_api_version : device_properties.apiVersion;

      const int device_api_level = android_get_device_api_level();
      if (device_api_level >= kMinimum_vk13_api_level &&
          driver_api_version >= VK_API_VERSION_1_3) {
        return VK_API_VERSION_1_3;
      } else if (device_api_level >= kMinimum_vk11_api_level &&
                 driver_api_version >= VK_API_VERSION_1_1) {
        return VK_API_VERSION_1_1;
      }
      return VK_API_VERSION_1_0;
    }

## Determine Vulkan profile compatibility

Vulkan profiles are JSON files that define a set of required features,
extensions, capabilities, and minimum parameter limits that a Vulkan device must
support to be compatible with the profile. To determine if a device is
compatible with a specific Vulkan profile, such as the 2022 [Android Baseline
profile](https://developer.android.com/ndk/guides/graphics/android-baseline-profile), use the open source [Vulkan Profiles API library](https://github.com/KhronosGroup/Vulkan-Profiles/blob/main/OVERVIEW.md).
You can also parse the profile JSON file yourself and query device capabilities
using the relevant Vulkan APIs to determine profile compatibility.

### Vulkan Profiles

Android is using [Vulkan Profiles](https://vulkan.lunarg.com/doc/sdk/1.3.280.0/windows/profiles_definitions.html)
which defines which features and extensions are available for each of the
devices running Android.

Android Baseline Profile (ABP) is the first attempt at building Vulkan Profile.
[ABP2021](https://github.com/KhronosGroup/Vulkan-Profiles/blob/main/profiles/VP_ANDROID_baseline_2021.json) and [ABP2022](https://github.com/KhronosGroup/Vulkan-Profiles/blob/main/profiles/VP_ANDROID_baseline_2022.json)
are backward looking profiles aimed to cover \> 85% of active devices at that
time. There will be no new ABP going forward.

Vulkan Profiles for Android (VPA) is the new forward looking profile aimed to
reflect the needs of software developers and drive consistent features as soon
as hardware developers can deliver them.
[VPA15_minimums](https://github.com/KhronosGroup/Vulkan-Profiles/blob/main/profiles/VP_ANDROID_15_minimums.json)
is the first profile for Android 15 and there will be a new VPA every year to
cover each major Android release.

## Implement frame pacing

Proper frame pacing is an essential part of delivering a high-quality gameplay
experience. The Android Game Development Kit includes the [Frame Pacing
library](https://developer.android.com/games/sdk/frame-pacing) to help your game achieve optimal frame pacing. For more
implementation details, see
[Integrate Android Frame Pacing into your Vulkan renderer](https://developer.android.com/games/sdk/frame-pacing/vulkan).

## Don't rely on implicit synchronization and frame pacing

[vkAcquireNextImageKHR](https://registry.khronos.org/vulkan/specs/latest/man/html/vkAcquireNextImageKHR.html) and [vkQueuePresentKHR](https://registry.khronos.org/vulkan/specs/latest/man/html/vkQueuePresentKHR.html)
are used to manage the swapchain. Avoid relying on their potential blocking
behavior for general application or GPU synchronization.

The precise blocking behavior of these functions can differ substantially
across:

- Android devices
- GPU drivers
- Presentation engine states ([VkPresentModeKHR](https://registry.khronos.org/vulkan/specs/latest/man/html/VkPresentModeKHR.html))

The sole purpose of [vkAcquireNextImageKHR](https://registry.khronos.org/vulkan/specs/latest/man/html/vkAcquireNextImageKHR.html) is to acquire
an available presentable image and it may or may not block.
Similarly, [vkQueuePresentKHR](https://registry.khronos.org/vulkan/specs/latest/man/html/vkQueuePresentKHR.html) queues a request to display an
image and also may or may not block.

Neither function provides reliable guarantees for synchronizing unrelated
CPU tasks or GPU operations.

For robust synchronization, always employ explicit Vulkan primitives like
semaphores for GPU-GPU dependencies (e.g., render-to-present),
fences for GPU-CPU synchronization (e.g., knowing when rendering is finished on
the CPU), and pipeline barriers or events for finer-grained GPU execution and
memory dependencies. Using explicit synchronization ensures predictable behavior
and avoids subtle bugs caused by implementation-specific timing variations
inherent in Android's diverse hardware ecosystem.

## Implement pre-rotation

Android devices can display in multiple orientations. The device orientation can
be different from the orientation of the render surface. Unlike OpenGL ES on
Android, Vulkan does not handle discrepancies between the two. To understand how
the orientation process works and the optimal method of handling orientation
differences when using Vulkan, see [Handle device rotation with Vulkan
pre-rotation](https://developer.android.com/games/optimize/vulkan-prerotation).

## Troubleshoot and profile Vulkan rendering

Multiple tools are available to help you diagnose rendering issues and
performance problems with Vulkan rendering code.

For more information on Vulkan's debugging and profiling tools, checkout the
[Tools \& advanced features](https://developer.android.com/games/develop/vulkan/tools-and-advanced-features)
section.

### Vulkan validation layers

Vulkan validation layers are runtime libraries that can be enabled to inspect
your calls to the Vulkan API and provide warnings or errors about incorrect or
nonoptimal use. These validation layers are not active by default, as the
validation process adds runtime overhead and impacts the performance of your
game. For information on how to use validation layers with your game, see
[Debugging with validation layer](https://developer.android.com/games/develop/vulkan/tools-and-advanced-features#debugging-with-validation-layer).
| **Note:** Some GPU vendors offer validation layer libraries specific to their GPUs in addition to the standard Vulkan validation layers. Use the GPU-specific validation layers to receive targeted feedback about particular GPUs. These layers can be downloaded from the developer website of the GPU vendor.

### Frame capture tools

Use frame capture tools to record and replay the Vulkan API calls made during a
game frame. These tools let you:

- View information about and visualizations of active graphic resources
- See the sequence of API calls made by your game and see the API parameters
- Explore the state of the graphics pipeline at the time of a draw call
- Visualize the results of rendering up to a specific draw call in the frame

Use the open source [RenderDoc](https://developer.android.com/games/develop/vulkan/tools-and-advanced-features#renderdoc) tool to capture frames from
games running on Android. RenderDoc supports frame capture of both Vulkan and
OpenGL ES.

The [Android GPU Inspector (AGI)](https://developer.android.com/agi) can also be used to capture Vulkan frames.

### Performance analysis tools

Use performance analysis tools to investigate rendering issues in your game that
cause suboptimal frame rates. Individual GPU vendors provide tools designed to
profile your game and provide performance data specific to their GPU
architectures. The performance characteristics and bottlenecks of your game can
vary significantly when rendering on GPUs from different vendors or even on
different GPU generations from the same vendor.

You can also use the Android GPU Inspector to gather and analyze
performance data. Unlike the vendor tools, Android GPU Inspector is compatible
with multiple GPUs from different vendors. However, Android GPU Inspector does
not support older Android devices and may not be compatible with all new
devices.

## Improve Vulkan testing with CTS-D

Android-powered device manufacturers use Compatibility Test Suite (CTS) to help
ensure that their devices are compatible. [Developer-Powered CTS (CTS-D)](https://source.android.com/docs/compatibility/cts/develop-cts-d) are
tests submitted by Android application developers to make sure that future
Android devices satisfy their use cases and are able to run their applications
smoothly and without bugs.

If you manage to trigger a new bug with your Vulkan application that affects any
specific Android-powered device, you can submit a new test proposal, describing
your issue and ways to check for it. This ensures that the issue is fixed in
a future update for the device, and also ensures that the same bug won't happen
to any other devices.

Check out the [CTS submission process](https://source.android.com/docs/compatibility/cts/develop-cts-d#submission-process)
for step-by-step instructions on how to submit
the test proposal.