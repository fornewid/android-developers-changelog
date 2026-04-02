---
title: Game engine support  |  Android game development  |  Android Developers
url: https://developer.android.com/games/develop/vulkan/game-engine-support
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Games dev center](https://developer.android.com/games)
* [Guides](https://developer.android.com/games/guides)

Send feedback

# Game engine support Stay organized with collections Save and categorize content based on your preferences.



Popular multi-platform game engines have supported Vulkan for some time.
However, due to varying levels of device support, these game engines have
implemented ways to allowlist good devices and denylist known bad devices.

You can start from these engines' default list and let the engine automatically
use Vulkan on supported devices and fall back to OpenGL ES for non-supported
devices.

## Unity

To enable automatic device selection on Unity, follow the steps to configure
[Auto Graphics API](/games/engines/unity/start-in-unity#auto_graphics_api).

Use the [VkQuality Unity engine plugin](/games/engines/unity/unity-vkquality) to
provide launch-time recommendations of the graphics API for your game to use on
a specific device.

## Unreal Engine

To enable automatic device selection on Unreal Engine, follow the steps to
[Support Vulkan](/games/engines/unreal/unreal-on-android#vulkan). When you
select both **Support Vulkan** and **Support OpenGL ES 3.2**, Unreal uses Vulkan
by default. If the device doesn't support Vulkan, Unreal falls back to
OpenGL ES 3.2.

If you are using specific Vulkan features that are known to behave badly on
certain devices, you can customize your `BaseDeviceProfile.ini` file to exclude those
devices. Check out [Customizing Device Profiles and Scalability for Android](https://dev.epicgames.com/documentation/en-us/unreal-engine/customizing-device-profiles-and-scalability-in-unreal-engine-projects-for-android#androiddeviceprofiles)
to learn how to customize it. Remember to keep your `BaseDeviceProfile.ini` file
updated. As new device drivers may fix previously known bad devices, you do not
want to miss out on optimizations that you will get for free from the updated
device drivers.




Send feedback