---
title: https://developer.android.com/games/develop/vulkan/frame-pacing-extensions
url: https://developer.android.com/games/develop/vulkan/frame-pacing-extensions
source: md.txt
---

Frame pacing is critical for delivering a smooth gaming experience. Frame pacing ensures
that frames are displayed at regular intervals, minimizing stutter and input
latency. While the
[Android Frame Pacing library (Swappy)](https://developer.android.com/games/sdk/frame-pacing) is the
recommended high-level solution for most games, low-level control is
available through Vulkan extensions.

Use the following Vulkan frame pacing extensions to
achieve precise control over frame presentation:

- [`VK_GOOGLE_display_timing`](https://developer.android.com/games/develop/vulkan/frame-pacing-extensions#vk_google_display_timing): Allows scheduling frames to be presented at specific times and querying past presentation times to adjust the rendering loop
- [`VK_EXT_present_timing`](https://developer.android.com/games/develop/vulkan/frame-pacing-extensions#vk_ext_present_timing): A newer, standardized extension that provides comprehensive timing feedback for presentation requests, introduced in Android 17 (API level 37) and higher

The `VK_GOOGLE_display_timing` extension is older and supported on a wider range
of Android devices. However, `VK_EXT_present_timing` is preferred when targeting
newer devices because it offers more features and more detailed timing
information.

## VK_GOOGLE_display_timing

The `VK_GOOGLE_display_timing` extension provides a way for applications to:

1. Query the duration of a display's refresh cycle
2. Specify a chosen presentation time for each frame
3. Query actual presentation times of past frames to implement a feedback loop

This extension is useful for games that implement their own frame pacing
algorithm instead of using Swappy.

### Enable the extension

To use `VK_GOOGLE_display_timing`, enable it when creating the Vulkan
device. Before enabling the extension, verify that it's supported by the physical device:

    // Check for extension support
    uint32_t extensionCount;
    vkEnumerateDeviceExtensionProperties(physicalDevice, nullptr, &extensionCount, nullptr);
    std::vector<VkExtensionProperties> availableExtensions(extensionCount);
    vkEnumerateDeviceExtensionProperties(physicalDevice, nullptr, &extensionCount, availableExtensions.data());

    bool supported = false;
    for (const auto& ext : availableExtensions) {
        if (strcmp(ext.extensionName, VK_GOOGLE_DISPLAY_TIMING_EXTENSION_NAME) == 0) {
            supported = true;
            break;
        }
    }

    if (supported) {
        // Add to your enabled extensions list when calling vkCreateDevice
        enabledDeviceExtensions.push_back(VK_GOOGLE_DISPLAY_TIMING_EXTENSION_NAME);
    }

### Query display refresh duration

You can query the refresh duration of the display associated with a swapchain
using [vkGetRefreshCycleDurationGOOGLE](https://docs.vulkan.org/refpages/latest/refpages/source/vkGetRefreshCycleDurationGOOGLE.html):

    VkRefreshCycleDurationGOOGLE refreshCycle;
    vkGetRefreshCycleDurationGOOGLE(device, swapchain, &refreshCycle);
    // refreshCycle.refreshDuration is the duration in nanoseconds

### Schedule frame presentation

To specify when a frame should be displayed, attach a
[VkPresentTimesInfoGOOGLE](https://docs.vulkan.org/refpages/latest/refpages/source/VkPresentTimesInfoGOOGLE.html) structure to the `pNext` chain of [VkPresentInfoKHR](https://docs.vulkan.org/refpages/latest/refpages/source/VkPresentInfoKHR.html)
when calling [vkQueuePresentKHR](https://docs.vulkan.org/refpages/latest/refpages/source/vkQueuePresentKHR.html):

    VkPresentTimeGOOGLE presentTime = {};
    presentTime.presentID = frameIndex; // Unique ID for this frame
    presentTime.desiredPresentTime = targetTimeNs; // Target time in nanoseconds (CLOCK_MONOTONIC)

    VkPresentTimesInfoGOOGLE presentTimesInfo = {};
    presentTimesInfo.sType = VK_STRUCTURE_TYPE_PRESENT_TIMES_INFO_GOOGLE;
    presentTimesInfo.swapchainCount = 1;
    presentTimesInfo.pTimes = &presentTime;

    VkPresentInfoKHR presentInfo = {};
    presentInfo.sType = VK_STRUCTURE_TYPE_PRESENT_INFO_KHR;
    presentInfo.pNext = &presentTimesInfo;
    // ... populate other presentInfo fields ...

    vkQueuePresentKHR(queue, &presentInfo);

The `desiredPresentTime` should be a timestamp from the system's monotonic
clock (`CLOCK_MONOTONIC`). Calculate this target time based on the display's
refresh rate and the actual presentation times of past frames. On Android, a
`desiredPresentTime` of 0 or any timestamp more than 1 second in the future is
ignored.

`VK_GOOGLE_display_timing` assumes all timestamps originate from the same clock.
On Android, all timestamps relevant to both `VK_GOOGLE_display_timing` and
`VK_EXT_present_timing` use `CLOCK_MONOTONIC`. (While `VK_EXT_present_timing`
supports multiple time domains, using different clocks is not necessary on
Android).

### Query past presentation times

To adjust your frame pacing loop, use [vkGetPastPresentationTimingGOOGLE](https://docs.vulkan.org/refpages/latest/refpages/source/vkGetPastPresentationTimingGOOGLE.html) to
query when past frames were actually displayed:

    uint32_t timingCount = 0;
    // Query the number of available timings
    vkGetPastPresentationTimingGOOGLE(device, swapchain, &timingCount, nullptr);

    if (timingCount > 0) {
        std::vector<VkPastPresentationTimingGOOGLE> presentationTimings(timingCount);
        vkGetPastPresentationTimingGOOGLE(device, swapchain, &timingCount, presentationTimings.data());

        for (const auto& timing : presentationTimings) {
            // Use timing information to adjust your pacing algorithm
            // timing.presentID identifies the frame
            // timing.actualPresentTime is when the frame was displayed (nanoseconds)
            // timing.earliestPresentTime is the earliest the frame could have been displayed
            // timing.presentMargin is the slack time between GPU completion and presentation
        }
    }

By comparing `actualPresentTime` with your `desiredPresentTime`, you can
determine whether frames are arriving too early or too late and adjust your rendering
loop accordingly.

### Code example

For a complete working example of how to integrate `VK_GOOGLE_display_timing`
into a Vulkan renderer, see the **cube demo** in the Android Game SDK
repository:

[Vulkan Cube Demo with Display Timing](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+/main/third_party/cube)

This demo demonstrates how to enable the extension, calculate target
presentation times, and process feedback from past presentation timings to
maintain a stable frame rate.

*** ** * ** ***

## VK_EXT_present_timing

Introduced in Vulkan and supported in Android 17 and higher, the
`VK_EXT_present_timing` extension is a standardized, more robust way to obtain
detailed feedback about frame presentation. It replaces and expands upon the
concepts in `VK_GOOGLE_display_timing`.

Key advantages of `VK_EXT_present_timing` include:

- **Standardized API**: Part of the official Khronos Vulkan extension set
- **Detailed Stage Queries**: Allows querying timestamps at specific stages of the presentation pipeline (for example, when the frame was dequeued, when the first pixel was sent to the display, and when the first pixel became visible)
- **Time Domain Support** : Supports different time domains (for example, system time, GPU time) and allows calibrating between them. A time domain represents a specific clock source or time base used to measure timestamps. On Android, all relevant timestamps use `CLOCK_MONOTONIC`, so utilizing multiple time domains is not necessary.
- **Integration with `VK_KHR_present_id2`** : Uses the standardized [VkPresentId2KHR](https://docs.vulkan.org/refpages/latest/refpages/source/VkPresentId2KHR.html) to identify presentation requests

### Enable the extension

To use `VK_EXT_present_timing`, you must enable it and its prerequisite,
`VK_KHR_present_id2`, during device creation. You should also check for
physical device features support:

    VkPhysicalDevicePresentId2FeaturesKHR presentId2Features = {};
    presentId2Features.sType = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PRESENT_ID_2_FEATURES_KHR;

    VkPhysicalDevicePresentTimingFeaturesEXT presentTimingFeatures = {};
    presentTimingFeatures.sType = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PRESENT_TIMING_FEATURES_EXT;
    presentTimingFeatures.pNext = &presentId2Features;

    VkPhysicalDeviceFeatures2 features2 = {};
    features2.sType = VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FEATURES_2;
    features2.pNext = &presentTimingFeatures;

    vkGetPhysicalDeviceFeatures2(physicalDevice, &features2);

    if (presentTimingFeatures.presentTiming && presentId2Features.presentId2) {
        // Enable VK_EXT_present_timing and VK_KHR_present_id2
        enabledDeviceExtensions.push_back(VK_EXT_PRESENT_TIMING_EXTENSION_NAME);
        enabledDeviceExtensions.push_back(VK_KHR_PRESENT_ID_2_EXTENSION_NAME);
    }

If either of these feature checks fail (`presentTiming` or `presentId2` is false), the device or driver does not support `VK_EXT_present_timing` or its prerequisite. In this case, your application cannot use `VK_EXT_present_timing` and should fall back to [`VK_GOOGLE_display_timing`](https://developer.android.com/games/develop/vulkan/frame-pacing-extensions#vk_google_display_timing) (if supported) or rely on default frame pacing mechanisms, such as Swappy.

### Enable present timing on the swapchain

When creating the swapchain, explicitly enable present timing by
setting the `VK_SWAPCHAIN_CREATE_PRESENT_TIMING_BIT_EXT` flag:

    VkSwapchainCreateInfoKHR swapchainCreateInfo = {};
    swapchainCreateInfo.sType = VK_STRUCTURE_TYPE_SWAPCHAIN_CREATE_INFO_KHR;
    swapchainCreateInfo.flags = VK_SWAPCHAIN_CREATE_PRESENT_TIMING_BIT_EXT;
    // ... populate other fields ...

    vkCreateSwapchainKHR(device, &swapchainCreateInfo, nullptr, &swapchain);

### Associate present IDs

When presenting, associate a unique ID with each frame using
`VkPresentId2KHR` (part of the `VK_KHR_present_id2` extension):

    uint64_t presentId = frameIndex; // Unique, monotonically increasing ID

    VkPresentId2KHR presentIdInfo = {};
    presentIdInfo.sType = VK_STRUCTURE_TYPE_PRESENT_ID_2_KHR;
    presentIdInfo.swapchainCount = 1;
    presentIdInfo.pPresentIds = &presentId;

    VkPresentInfoKHR presentInfo = {};
    presentInfo.sType = VK_STRUCTURE_TYPE_PRESENT_INFO_KHR;
    presentInfo.pNext = &presentIdInfo;
    // ... populate other presentInfo fields ...

    vkQueuePresentKHR(queue, &presentInfo);

### Query swapchain timing properties

Query swapchain timing properties, such as refresh duration, using
[vkGetSwapchainTimingPropertiesEXT](https://docs.vulkan.org/refpages/latest/refpages/source/vkGetSwapchainTimingPropertiesEXT.html):

    VkSwapchainTimingPropertiesEXT timingProperties = {};
    timingProperties.sType = VK_STRUCTURE_TYPE_SWAPCHAIN_TIMING_PROPERTIES_EXT;

    uint64_t propertiesCounter = 0;
    vkGetSwapchainTimingPropertiesEXT(device, swapchain, &timingProperties, &propertiesCounter);
    // timingProperties.refreshDuration is the duration in nanoseconds

### Query supported time domains

\]
As noted earlier, a time domain represents a specific clock source or time base.
While `VK_EXT_present_timing` supports multiple time domains and allows
calibrating between them, using different clocks is not necessary on Android
because all relevant timestamps use `CLOCK_MONOTONIC`. Query the supported
time domains for your swapchain:

    VkSwapchainTimeDomainPropertiesEXT timeDomainProps = {};
    timeDomainProps.sType = VK_STRUCTURE_TYPE_SWAPCHAIN_TIME_DOMAIN_PROPERTIES_EXT;

    // Query the count first
    vkGetSwapchainTimeDomainPropertiesEXT(device, swapchain, &timeDomainProps, nullptr);

    std::vector<VkTimeDomainKHR> timeDomains(timeDomainProps.timeDomainCount);
    std::vector<uint64_t> timeDomainIds(timeDomainProps.timeDomainCount);
    timeDomainProps.pTimeDomains = timeDomains.data();
    timeDomainProps.pTimeDomainIds = timeDomainIds.data();

    // Populate the data
    vkGetSwapchainTimeDomainPropertiesEXT(device, swapchain, &timeDomainProps, nullptr);

### Request target presentation time

To request that a frame be presented at a specific time, chain a
[VkPresentTimingInfoEXT](https://docs.vulkan.org/refpages/latest/refpages/source/VkPresentTimingInfoEXT.html) structure to your `VkPresentInfoKHR`.

    VkPresentTimingInfoEXT timingInfo = {};
    timingInfo.sType = VK_STRUCTURE_TYPE_PRESENT_TIMING_INFO_EXT;
    timingInfo.flags = VK_PRESENT_TIMING_INFO_PRESENT_AT_RELATIVE_TIME_BIT_EXT; // Or absolute if supported
    timingInfo.targetTime = targetTime; // Time value
    timingInfo.timeDomainId = timeDomainIds[0]; // Use a supported time domain ID
    timingInfo.presentStageQueries = VK_PRESENT_STAGE_IMAGE_FIRST_PIXEL_VISIBLE_BIT_EXT;

    VkPresentTimingsInfoEXT presentTimingsInfo = {};
    presentTimingsInfo.sType = VK_STRUCTURE_TYPE_PRESENT_TIMINGS_INFO_EXT;
    presentTimingsInfo.swapchainCount = 1;
    presentTimingsInfo.pTimingInfos = &timingInfo;

    // Chain to VkPresentId2KHR
    presentIdInfo.pNext = &presentTimingsInfo;

As noted earlier, on Android, a `targetTime` of 0 or any target timestamp more
than 1 second in the future is ignored.

### Query past presentation timings

To query detailed timing information for past presentations, first
configure the timing queue size using [vkSetSwapchainPresentTimingQueueSizeEXT](https://docs.vulkan.org/refpages/latest/refpages/source/vkSetSwapchainPresentTimingQueueSizeEXT.html),
and then retrieve the timings using [vkGetPastPresentationTimingEXT](https://docs.vulkan.org/refpages/latest/refpages/source/vkGetPastPresentationTimingEXT.html):

    // Set the size of the timing queue (do this during initialization)
    vkSetSwapchainPresentTimingQueueSizeEXT(device, swapchain, 10); // Keep last 10 frames

    // ... later in your frame loop ...

    VkPastPresentationTimingInfoEXT pastTimingInfo = {};
    pastTimingInfo.sType = VK_STRUCTURE_TYPE_PAST_PRESENTATION_TIMING_INFO_EXT;
    pastTimingInfo.swapchain = swapchain;

    VkPastPresentationTimingPropertiesEXT pastProperties = {};
    pastProperties.sType = VK_STRUCTURE_TYPE_PAST_PRESENTATION_TIMING_PROPERTIES_EXT;

    // First query to get the count of available timings
    vkGetPastPresentationTimingEXT(device, &pastTimingInfo, &pastProperties);

    if (pastProperties.presentationTimingCount > 0) {
        std::vector<VkPastPresentationTimingEXT> timings(pastProperties.presentationTimingCount);
        pastProperties.pPresentationTimings = timings.data();

        // Populate the timings
        vkGetPastPresentationTimingEXT(device, &pastTimingInfo, &pastProperties);

        for (const auto& timing : timings) {
            // timing.presentId identifies the frame (matches the presentId you set)
            // timing.targetTime is the requested target time
            // If you requested stage queries, you can inspect timing.pPresentStages
        }
    }

### Code example

For a complete integration example and conformance tests for
`VK_EXT_present_timing`, refer to the **deqp (Draw Elements Quality Program)**
tests in the Vulkan CTS (Compatibility Test Suite) repository:

[Vulkan CTS Present Timing Tests](https://github.com/KhronosGroup/VK-GL-CTS/blob/main/external/vulkancts/modules/vulkan/wsi/vktWsiPresentTimingTests.cpp)

These tests demonstrate how to configure swapchains for present timing, set
target times, and verify the accuracy of reported presentation timestamps
across different time domains.