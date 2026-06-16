---
title: https://developer.android.com/games/develop/vulkan/game-engine-support
url: https://developer.android.com/games/develop/vulkan/game-engine-support
source: md.txt
---

Popular multi-platform game engines have supported Vulkan for some time.
However, due to varying levels of device support, these game engines have
implemented ways to allowlist good devices and denylist known bad devices.

You can start from these engines' default list and let the engine automatically
use Vulkan on supported devices and fall back to OpenGL ES for non-supported
devices.

## How to use Vulkan

Configure your game engine to enable Vulkan on supported Android devices and
manage fallback behavior.

### Unity

To enable automatic device selection on Unity, follow the steps to configure
[Auto Graphics API](https://developer.android.com/games/engines/unity/start-in-unity#auto_graphics_api).

Use the [VkQuality Unity engine plugin](https://developer.android.com/games/engines/unity/unity-vkquality) to provide launch-time
recommendations of the graphics API for your game to use on a specific device.

### Unreal Engine

To enable automatic device selection on Unreal Engine, follow the steps to
[Support Vulkan](https://developer.android.com/games/engines/unreal/unreal-on-android#vulkan). When you select both **Support Vulkan**
and **Support OpenGL ES 3.2**, Unreal uses Vulkan by default. If the device
doesn't support Vulkan, Unreal falls back to OpenGL ES
3.2.

If you are using specific Vulkan features that are known to behave badly on
certain devices, you can customize your `BaseDeviceProfile.ini` file to exclude
those devices. Refer to [Customizing Device Profiles and Scalability for
Android](https://dev.epicgames.com/documentation/en-us/unreal-engine/customizing-device-profiles-and-scalability-in-unreal-engine-projects-for-android#androiddeviceprofiles) for more information. Remember to keep
your `BaseDeviceProfile.ini` file updated. As new device drivers may fix
previously known bad devices, you don't want to miss out on optimizations that
you will get from the updated device drivers.

## How to check dEQP Level

The [drawElements Quality Program (dEQP)](https://source.android.com/docs/core/graphics/implement-vulkan#vulk) is a conformance test suite
that verifies a device's Vulkan capabilities and driver stability. Checking the
device's dEQP level (`vk_deqp_level`) ensures its Vulkan driver meets minimum
stability standards, helping you avoid driver issues and rendering artifacts
before enabling Vulkan.

### Unity

Check the Android device's `vk_deqp_level` using the [VkQuality Unity engine
plugin](https://developer.android.com/games/engines/unity/unity-vkquality) to safely enable Vulkan.

### Unreal

Check the Android device's `vk_deqp_level` in Unreal Engine using the
[DEQP_UPL.xml](https://github.com/android/games-samples/commit/b802ef22d72a81b8aa1d0ad98932d76a42da87dd) file.

To use the file, download `DEQP_UPL.xml` and register it in your project's
`Build.cs` file:

    if (Target.Platform == UnrealTargetPlatform.Android)
    {
        AdditionalPropertiesForReceipt.Add("AndroidPlugin", Path.Combine(ModuleDirectory, "DEQP_UPL.xml"));
    }

When you build and run your game, Logcat displays the dEQP check result:

    UE_RHI_Selector: ==================================================
    UE_RHI_Selector: Device Model   : Pixel 10 Pro XL
    UE_RHI_Selector: OS Version     : Android 16
    UE_RHI_Selector: API Level      : 36
    UE_RHI_Selector: Device dEQP    : 0x7e90301 (2025-03-01)
    UE_RHI_Selector: Target dEQP    : 0x7e80301 (2024-03-01)
    UE_RHI_Selector: Modern Vulkan? : true
    UE_RHI_Selector: ==================================================