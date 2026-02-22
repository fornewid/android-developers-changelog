---
title: https://developer.android.com/ndk/guides/graphics/extensions
url: https://developer.android.com/ndk/guides/graphics/extensions
source: md.txt
---

# Vulkan extensions on Android

Android devices may fully or partially support[Vulkan extensions](https://www.khronos.org/registry/vulkan/specs/1.0-extensions/html/vkspec.html#extended-functionality-extensions)that provide additional functionality.

To determine if a Vulkan extension is available on a particular target device, use the Vulkan extension enumeration functions (`vkEnumerateInstanceExtensionProperties()`and`vkEnumerateDeviceExtensionProperties()`) as described in the[Vulkan specification](https://www.khronos.org/registry/vulkan/specs/1.0-extensions/html/vkspec.html#extended-functionality-extensions). To see an example, you can refer to this[code sample](https://github.com/LunarG/VulkanSamples/blob/master/API-Samples/instance_extension_properties/instance_extension_properties.cpp)in the Vulkan samples repo.

The following table summarizes the list of Vulkan extensions that Android supports, the minimum OS version for the extension support, and the extension type.

|         OS Version         |                                                                  Vulkan Extension                                                                  | Extension Type |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| Android 8.0 (API level 26) | [VK_KHR_incremental_present](https://www.khronos.org/registry/vulkan/specs/1.0-extensions/html/vkspec.html#VK_KHR_incremental_present)             | Device         |
| Android 8.0 (API level 26) | [VK_KHR_shared_presentable_image](https://www.khronos.org/registry/vulkan/specs/1.0-extensions/html/vkspec.html#VK_KHR_shared_presentable_image)   | Device         |
| Android 8.0 (API level 26) | [VK_KHR_get_surface_capabilities2](https://www.khronos.org/registry/vulkan/specs/1.0-extensions/html/vkspec.html#VK_KHR_get_surface_capabilities2) | Instance       |
| Android 8.0 (API level 26) | [VK_EXT_hdr_metadata](https://www.khronos.org/registry/vulkan/specs/1.0-extensions/html/vkspec.html#VK_EXT_hdr_metadata)                           | Device         |
| Android 8.0 (API level 26) | [VK_EXT_swapchain_colorspace](https://www.khronos.org/registry/vulkan/specs/1.0-extensions/html/vkspec.html#VK_EXT_swapchain_colorspace)           | Instance       |
| Android 8.0 (API level 26) | [VK_GOOGLE_display_timing](https://www.khronos.org/registry/vulkan/specs/1.0-extensions/html/vkspec.html#VK_GOOGLE_display_timing)                 | Device         |
| Android 7.0 (API level 24) | [VK_KHR_android_surface](https://www.khronos.org/registry/vulkan/specs/1.0-extensions/html/vkspec.html#VK_KHR_android_surface)                     | Instance       |
| Android 7.0 (API level 24) | [VK_KHR_surface](https://www.khronos.org/registry/vulkan/specs/1.0-extensions/html/vkspec.html#VK_KHR_surface)                                     | Instance       |