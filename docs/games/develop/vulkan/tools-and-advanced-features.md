---
title: https://developer.android.com/games/develop/vulkan/tools-and-advanced-features
url: https://developer.android.com/games/develop/vulkan/tools-and-advanced-features
source: md.txt
---

# Tools and advanced features

## Debuggers

### Debugging with validation layer

Vulkan is designed for high performance and low driver overhead. To achieve
this, it includes only very limited error checking and debugging capabilities
by default. If you do something wrong, the driver will often crash instead of
returning an error code, or even worse, it will appear to work on your graphics
card but completely fail on others.

To enable extensive checks during your development, Vulkan provides validation
layers, which are pieces of code that can be inserted between the API and the
graphics driver to do things like running extra checks on function parameters
and tracking memory management problems. You can enable validation layers during
development and completely disable them when releasing your application with
zero overhead.

Validation layers can be written by anyone, but Khronos provides a single
standard set called `VK_LAYER_KHRONOS_validation`. Check out
[Vulkan validation layers on Android](https://developer.android.com/ndk/guides/graphics/validation-layer)
from the Android NDK page to enable the validation layer in your application.

### RenderDoc

RenderDoc is another powerful open source tool that lets you capture a frame for
inspection and analysis. It is a very powerful tool that has been used by
graphics programmers to debug their rendered scenes. It supports Vulkan on
Android well although your application has to be set as
[debuggable](https://developer.android.com/guide/topics/manifest/application-element#debug)
for it to work.

For information on how to set up and use it on your Android application, check
out [How do I use RenderDoc on Android](https://renderdoc.org/docs/how/how_android_capture.html).

## Capture / Replay Libraries

### GFXReconstruct

GFXReconstruct is an open source project that provides tools to capture and
replay graphics API calls executed by an application. The recorded trace can
later be replayed to reconstruct the graphics-specific behavior of the captured
application. One of the main advantages of GFXReconstruct is that it lets you
use it on your released application (when you have turned off
[android:debuggable](https://developer.android.com/guide/topics/manifest/application-element#debug)).

For more information, visit the project
[repository](https://github.com/LunarG/gfxreconstruct).
Setting up and usage information for Vulkan on Android is available in
[GFXReconstruct API Capture and Replay for Android](https://github.com/LunarG/gfxreconstruct/blob/dev/USAGE_android.md).

Note that the trace files are not portable, meaning that you cannot capture the
file on one device and replay it on another device (with different OS version,
chipsets, or even driver version).

## Profilers

### Android GPU Inspector (AGI)

Android GPU Inspector (AGI) is a graphics profiler built for Android that
includes a [System Profile](https://developer.android.com/agi/sys-trace/system-profiler) and a
[Frame Profiler](https://developer.android.com/agi/frame-trace/frame-profiler). It provides high-level
profiling information that allows you to understand your game's performance
profile and identify bottlenecks.

To download AGI and learn how to use it, check out the
[Android GPU Inspector](https://gpuinspector.dev/) website.

### Android Studio Profiler

Android Studio Profiler is a useful tool for profiling your app performance.
However, it is not specifically geared towards graphics profiling. It consists
of CPU Profiler, Memory Profiler, Network Profiler, Energy Profiler, Power
Profiler and Event Monitor.

For more information on how to set up and use Android Studio Profiler, check out
[Profile your app performance](https://developer.android.com/studio/profile) section.

## OEM Profilers

The tools in this section are OEM specific and may not work on devices running
on other chips.

### ARM Performance Studio for Mobile

[Arm Performance Studio for Mobile](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio%20for%20Mobile)
is the new name for Arm Mobile Studio. It is a suite of tools that includes
[Graphics Analyzer](https://developer.arm.com/tools-and-software/graphics-and-gaming/arm-mobile-studio/components/graphics-analyzer)
and [Frame Advisor](https://developer.arm.com/Tools%20and%20Software/Frame%20Advisor)
to help you identify and fix performance problems on ARM GPUs.

For more information, check out [Arm Performance Studio for Mobile](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio%20for%20Mobile)
website.

### ARM PerfDoc for Mali GPUs

[PerfDoc](https://github.com/ARM-software/perfdoc) is a Vulkan layer developed
to validate applications against ARM's Mali GPU best practices. It has since
been merged into VK_LAYER_KHRONOS_validation and is essentially part of the
standard Vulkan validation layers.

For information on how to use it, check out [Debugging with validation layer](https://developer.android.com/games/develop/vulkan/tools-and-advanced-features#debugging-with-validation-layer)
section.

### Qualcomm Snapdragon Profiler

Qualcomm Snapdragon Profiler is a profiling software developed by Qualcomm for
application developers to analyze CPU, GPU, DSP, memory, power, thermal and
network performance to identify bottlenecks on their chipsets.

For more information, check out
[Snapdragon Profiler on Qualcomm Developer Network](https://developer.qualcomm.com/software/snapdragon-profiler).

### Samsung GPUWatch

Samsung's [GPUWatch](https://developer.samsung.com/galaxy-gamedev/gpuwatch.html)
is a tool for observing GPU activity on Samsung devices. Unlike the other tools,
you can use this tool directly from your mobile device, so it is very handy to
check your application performance immediately even when you do not have access
to another host computer.

For more information on how to enable it, check out the [User Guide](https://developer.samsung.com/galaxy-gamedev/gpuwatch-userguide/gpuwatch_v2.html).

### PVRTune

Imagination Technologies'
[PVRTune](https://developer.imaginationtech.com/solutions/pvrtune/) enables
developers to profile applications on PowerVR hardware in real-time with a wide
array of counters and metrics. It also allows the session to be saved for
further low-level analysis and to detect performance bottlenecks.

For more information on how to use PVRTune, check out the [Manual](https://docs.imgtec.com/tools-manuals/pvrtune-manual/html/pvrtune-manual/topics/introduction.html).

## Migration Tools

### Converting shaders from GLSL to SPIR-V

The Vulkan API expects shader programs to be provided in the SPIR-V binary
intermediate format. This convention is different from OpenGL ES, where you
could submit source code written in the [OpenGL Shading Language (GLSL)](https://www.khronos.org/opengl/wiki/OpenGL_Shading_Language)
as text strings.

NDK r12 and later includes a runtime library for compiling GLSL shaders into
SPIR-V which can be used by Vulkan. The [shaderc](https://github.com/google/shaderc)
compiler can be used to compile shader programs written in GLSL into SPIR-V.
If your game uses HLSL, the [DirectXShaderCompiler](https://github.com/microsoft/DirectXShaderCompiler)
supports SPIR-V output.

Typically, you will need to compile shader programs offline as part of the asset
build process for your game and include the SPIR-V modules as part of your
runtime assets.

For more information on the shader compilation process for your Vulkan
application, check out [Vulkan shader compilers on Android](https://developer.android.com/ndk/guides/graphics/shader-compilers)
in the Android NDK section.

## Advanced Features

### Integrate Android Frame Pacing into your Vulkan renderer

Android Frame Pacing library (also known as Swappy) helps Vulkan games achieve
smooth rendering and correct pacing to keep the game rendering loop in sync with
the OS's display subsystem and the underlying display hardware.

Correct pacing eliminates visual artifacts known as tearing, optimize power
consumption through synchronization between display refreshes and frame
presentation, and also eliminate janks by stabilizing frame rate. To learn more
about the importance of frame pacing, check out the
[Frame Pacing Library](https://developer.android.com/games/sdk/frame-pacing) section of the AGDK.

For more information on how to integrate frame pacing into your game, check out
[Integrate Android Frame Pacing into your Vulkan renderer](https://developer.android.com/games/sdk/frame-pacing/vulkan).

### Handle device orientation with Vulkan pre-rotation

Surface rotation handling outside of the application may not be free. Even on
some higher end devices with dedicated Display Processing Unit (DPU), there will
still likely be a measurable performance penalty to pay and the impact will
depend whether your application is CPU bound or GPU bound.

Vulkan provides developers with the power to specify much more information to
devices about the rendering state compared to OpenGL. One such information is
**device orientation** and its relationship to **render surface orientation**.
This capability lets you implement pre-rotation to get the most out of Vulkan on
Android.

For more information on how to efficiently handle device rotation on your
Vulkan application, check out [Handle device orientation with Vulkan pre-rotation](https://developer.android.com/games/optimize/vulkan-prerotation)
and the accompanying
[demo application](https://github.com/google/vulkan-pre-rotation-demo).

### Optimize with reduced precision

The numerical format of graphics data and shader calculations can have a
significant impact on the performance of your game. The majority of calculations
and data in modern 3D graphics are using floating point numbers. Vulkan on
Android uses floating point numbers that are 32 or 16 bits in size. A 32-bit
floating point number is commonly referred to as single precision or full
precision. Although 64-bit floating point type is defined in Vulkan, it is not
commonly supported and its use is not recommended.

Check out
[Optimize with reduced precision](https://developer.android.com/games/optimize/vulkan-reduced-precision)
for information on how to optimize your Vulkan application for best performance
on your arithmetics.