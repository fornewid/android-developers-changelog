---
title: https://developer.android.com/develop/ui/views/graphics/webgpu
url: https://developer.android.com/develop/ui/views/graphics/webgpu
source: md.txt
---

The Android Jetpack
[WebGPU library](https://developer.android.com/reference/kotlin/androidx/webgpu/package-summary)
provides idiomatic Kotlin bindings for the
[WebGPU standard](https://www.w3.org/TR/webgpu/), enabling
high-performance, modern 3D graphics and compute capabilities within your
Android applications.

WebGPU is the successor to WebGL and the spiritual descendant of OpenGL,
built from the ground up to reflect how modern GPUs work and expose GPU
capabilities in a cross-platform, safe, and
ergonomic way.

## Why WebGPU?

- **Streamlined Usability** : While Vulkan is the primary low-level graphics API on Android. WebGPU offers a modern, higher-level API that is **more approachable and significantly less verbose to use compared to Vulkan**.
- **Batching and Serialization** WebGPU records multiple commands into **Command Buffers**, part of its design to minimize protocol chattiness. This also minimizes the need to call external methods when using Kotlin bindings.
- **Universal Support**: WebGPU shader code (WGSL) can be directly shared across WebGPU implementations across platforms, including the web.
- **Optimized Compute**: Seamless, copy-free buffer sharing between compute and graphics tasks enhances performance and simplifies development compared to legacy APIs.

## Who this library is for

This library is designed for building high-performance applications that require
direct access to the GPU:

- Image and video processing filters
- Data visualizations
- Machine Learning inference
- Games and simulations

**Non-Goals**: This is a graphics API, not a game engine. You are responsible
for managing your own render loop, camera matrices, and scene graph.

## Core WebGPU concepts

Understanding the foundational WebGPU objects and how they interact is essential
to WebGPU development.

|---|---|
| **Concept** | **Description** |
| **Instance** | The entry point to WebGPU, granting access to Adapters and Surfaces |
| **Adapter** | Represents a specific GPU on the device |
| **Device** | Your logical connection to the GPU where resources are created |
| **Queue** | The mechanism used to submit commands to the GPU |
| **Shader Module** | Your GPU code, written in the WebGPU Shading Language [(WGSL)](https://www.w3.org/TR/WGSL/) |
| **Pipelines** | Objects describing the entire GPU state (shaders, blending) for a task |
| **Bind Groups** | Ties data buffers (ex: textures) to shaders |
| **Command Encoder** | An object used to build a sequence of GPU commands into a command buffer |