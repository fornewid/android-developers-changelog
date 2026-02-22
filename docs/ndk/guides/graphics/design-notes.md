---
title: https://developer.android.com/ndk/guides/graphics/design-notes
url: https://developer.android.com/ndk/guides/graphics/design-notes
source: md.txt
---

# Vulkan design guidelines

Vulkan is unlike earlier graphics APIs in that drivers do not perform certain optimizations, such as pipeline reuse, for apps. Instead, apps using Vulkan must implement such optimizations themselves. If they do not, they may exhibit worse performance than apps running OpenGL ES.

When apps implement these optimizations themselves, they have the potential to do so more successfully than the driver can, because they have access to more specific information for a given use case. As a result, skillfully optimizing an app that uses Vulkan can yield better performance than if the app were using OpenGL ES.

This page introduces several optimizations that your Android app can implement to gain performance boosts from Vulkan.

## Hardware acceleration

Most devices[support Vulkan 1.1 via hardware acceleration](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VULKAN_HARDWARE_VERSION)while a small subset support it via software emulation. Apps can detect a software-based Vulkan device using`vkGetPhysicalDeviceProperties`and checking the`deviceType`field of the returned structure.[SwiftShader](https://github.com/google/swiftshader)and other CPU-based implementations have the value`VK_PHYSICAL_DEVICE_TYPE_CPU`. Apps can check specifically for SwiftShader by checking the`vendorID`and`deviceID`fields of this same structure for SwiftShader-specific values.

Performance-critical apps should avoid using software-emulated Vulkan implementations and fall back to OpenGL ES instead.

## Apply display rotation during rendering

When the upward-facing direction of an app doesn't match the orientation of the device's display, the compositor rotates the app's swapchain images so that it does match. It performs this rotation as it displays the images, which results in more power consumption---sometimes significantly more---than if it were not rotating them.

By contrast, rotating swapchain images while generating them results in little, if any, additional power consumption. The`VkSurfaceCapabilitiesKHR::currentTransform`field indicates the rotation that the compositor applies to the window. After an app applies that rotation during rendering, the app uses the`VkSwapchainCreateInfoKHR::preTransform`field to report that the rotation is complete.

## Minimize render passes per frame

On most mobile GPU architectures, beginning and ending a render pass is an expensive operation. Your app can improve performance by organizing rendering operations into as few render passes as possible.

Different attachment-load and attachment-store ops offer different levels of performance. For example, if you do not need to preserve the contents of an attachment, you can use the much faster`VK_ATTACHMENT_LOAD_OP_CLEAR`or`VK_ATTACHMENT_LOAD_OP_DONT_CARE`instead of`VK_ATTACHMENT_LOAD_OP_LOAD`. Similarly, if you don't need to write the attachment's final values to memory for later use, you can use`VK_ATTACHMENT_STORE_OP_DONT_CARE`to attain much better performance than`VK_ATTACHMENT_STORE_OP_STORE`.

Also, in most render passes, your app doesn't need to load or store the depth/stencil attachment. In such cases, you can avoid having to allocate physical memory for the attachment by using the`VK_IMAGE_USAGE_TRANSIENT_ATTACHMENT_BIT`flag when creating the attachment image. This bit provides the same benefits as does`glFramebufferDiscard`in OpenGL ES.

## Choose appropriate memory types

When allocating device memory, apps must choose a memory type. Memory type determines how an app can use the memory, and also describes caching and coherence properties of the memory. Different devices have different memory types available; different memory types exhibit different performance characteristics.

An app can use a simple algorithm to pick the best memory type for a given use. This algorithm picks the first memory type in the`VkPhysicalDeviceMemoryProperties::memoryTypes`array that meets two criteria: The memory type must be allowed for the buffer or image, and must have the minimum properties that the app requires.

Mobile systems generally don't have separate physical memory heaps for the CPU and GPU. On such systems,`VK_MEMORY_PROPERTY_DEVICE_LOCAL_BIT`is not as significant as it is on systems that have discrete GPUs with their own, dedicated memory. An app should not assume this property is required.

## Group descriptor sets by frequency

If you have resource bindings that change at different frequencies, use multiple descriptor sets per pipeline rather than rebinding all resources for each draw. For example, you can have one set of descriptors for per-scene bindings, another set for per-material bindings, and a third set for per-mesh-instance bindings.

Use immediate constants for the highest-frequency changes, such as changes executed with each draw call.