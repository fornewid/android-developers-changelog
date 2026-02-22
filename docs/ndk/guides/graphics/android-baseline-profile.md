---
title: https://developer.android.com/ndk/guides/graphics/android-baseline-profile
url: https://developer.android.com/ndk/guides/graphics/android-baseline-profile
source: md.txt
---

| **Note:** The Android Baseline Profiles (ABP) are being renamed to Android Vulkan Profiles (AVP). This change better reflects their purpose: to provide developers with a reliable set of Vulkan features based on the current state of the Android-powered device ecosystem for a given year. As a result, the following naming changes are taking place: Android Baseline Profile 2021 is now Android Vulkan Profile 2021. Android Baseline Profile 2022 is now Android Vulkan Profile 2022.

Google has released the Android Vulkan Profile 2025, an updated profile designed to give developers access to the latest compatible features.

When we released the initial Android Baseline Profile 2021 (now Android Vulkan Profile 2021), we wanted to remove the challenges developers consistently encountered when determining what Vulkan functionality they could rely upon across the diverse set of Android-powered devices.

The Android Vulkan Profile 2021 addressed this pain point with a Vulkan profile that specified a set of Vulkan extensions, features, formats, and limits that were found on the vast majority of active Android devices in 2021. This profile was created with available data and discussions with Khronos partners to have a high level of compatibility with both existing and future devices and represents the complete set of Vulkan functionality that meets these constraints. We continued this process with the release of the Android Vulkan Profile 2022.

Just as with our initial 2021 and 2022 profiles, the Android Vulkan Profile 2025 includes a collection of Vulkan extensions, features, formats, and limits that are found on the vast majority of active Android devices. As the Android ecosystem has evolved, we have been able to add more extensions and features in the AVP 2025 as compared to previous versions. We believe that many developers will be able to benefit from the additional functionality found in this new profile.

We encourage you to read the full[Android Vulkan Profile 2025](https://github.com/KhronosGroup/Vulkan-Profiles/blob/main/profiles/Android/VP_ANDROID_vulkan_profile_2025.json)on GitHub.

## Key highlights of AVP 2025

Building on the previous profiles, Android Vulkan Profile 2025 now includes:

- Additional memory features with`VK_KHR_external_memory_fd`and`VK_KHR_vulkan_memory_model`
- Finer-grained control of floating point operations with`VK_KHR_shader_float_controls`
- Support for resetting GPU queries from the host with`VK_EXT_host_query_reset`
- Standard support for more pixel formats, including packed`A2B10G10R10`,`B10G11R11_UFLOAT`,`B4G4R4A4`, and many more

## Key highlights of AVP 2022 and 2021

Android Vulkan Profile 2021 included functionality such as:

- Compressed textures through ASTC and ETC
- Variable colorspaces through`VK_EXT_swapchain_colorspace`
- Sample shading and multisample interpolation through`sampleRateShading`

Extending this functionality, the Android Vulkan Profile 2022 also adds a collection of features, such as:

- Full support for Vulkan 1.1
- 16 bit integers in shaders through`shaderInt16`
- Vulkan and[Android Hardware Buffer](https://developer.android.com/reference/android/hardware/HardwareBuffer)interoperability through`VK_ANDROID_external_memory_android_hardware_buffer`
- Querying Vulkan driver properties with`VK_KHR_driver_properties`
- Greater control over renderpass creation with`VK_KHR_create_renderpass2`

Developers have three distinct profiles to use when developing their games, allowing them to select the profile that best fits the specific requirements of their project.

| Profile  | Vulkan device support\* |
|----------|-------------------------|
| AVP 2025 | 80.1%                   |
| AVP 2022 | 86.5%                   |
| AVP 2021 | 95.5%                   |

\*Based on active Vulkan supporting device data from October 2025.

We publish updated support percentages for the Android Vulkan Profiles in the[Android Distribution Dashboard](https://developer.android.com/about/dashboards).