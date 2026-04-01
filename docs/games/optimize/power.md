---
title: https://developer.android.com/games/optimize/power
url: https://developer.android.com/games/optimize/power
source: md.txt
---

Android games are played primarily on battery-powered devices such as phones or
tablets. Optimize your game's power efficiency to help users play your game
longer and give them confidence to start a game session even when their device
isn't fully charged.

## Use an optimal display refresh rate

Display refresh rate is the speed at which the display panel of a device can
change to show new information. Traditionally, handheld devices used a refresh
rate of 60Hz, updating the display contents sixty times a second. Modern devices
often feature displays with higher refresh rates capable of updating at 90Hz or
120Hz. Higher refresh rates result in smoother user experiences for actions such
as scrolling, but increase the power consumption of the display panel.

Games commonly have a target frame rate of 30 or 60 frames per second. If the
display refresh rate is higher than the target frame rate of the game, there is
no benefit from the higher refresh rate, only increased power consumption. On
high-refresh-rate devices, adjust the display refresh rate to match your game
target frame rate as closely as possible.

### Integrate or enable the Swappy frame pacing library

The Android Game Development Kit (AGDK) includes a frame pacing library known as
Swappy. Swappy optimizes the device's display refresh rate to match your game
frame rate as closely as possible. If you are using a custom game engine, review
the [Frame Pacing Library](https://developer.android.com/games/sdk/frame-pacing) guide to learn how to integrate the library into
your engine.

Swappy is already integrated into the Unreal engine ([Frame Pacing for Mobile
Devices](https://dev.epicgames.com/documentation/en-us/unreal-engine/frame-pacing-for-mobile-devices-in-unreal-engine)) and the Unity engine
([PlayerSettings.Android.optimizedFramePacing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-optimizedFramePacing.html))
and optimizes the display refresh rate if enabled in your game project.

### Call the Android frame rate API

As an alternative to integrating the frame pacing library, use the [Android
frame rate API](https://developer.android.com/media/optimize/performance/frame-rate) to directly adjust the display refresh rate.

## Use the Vulkan API for graphics

Android supports two graphics APIs: the older OpenGL ES API and the newer Vulkan
API. Vulkan is now the primary graphics API on Android and is more efficient
than OpenGL ES. For more information on Vulkan's benefits and how to use it, see
[Use Vulkan for graphics](https://developer.android.com/games/develop/vulkan/overview).

## Respond to device thermal conditions

High utilization of the device's CPU and GPU generates heat. Power efficiency
drops as the device heats up. If a device gets too hot, it downclocks the
speed of the CPU and GPU to reduce power consumption and allow the device to
cool. This behavior, referred to as thermal throttling, affects the performance
of your game and its rate of battery drain. Use the [Android Thermal API](https://developer.android.com/games/optimize/adpf/thermal) to
monitor the thermal state of the device to adjust your game's workload to
prevent thermal throttling.

## Query the device Game Mode

Game Mode is a feature that lets the user specify a preference of whether to
trade off performance against battery life, battery life against performance, or
select a neutral default. If your game supports variable performance
configurations, use the [Game Mode API](https://developer.android.com/games/optimize/adpf/gamemode/gamemode-api) to check for this preference and
modify your game settings accordingly.

## Additional resources

[Android Studio power profiler](https://developer.android.com/studio/profile/power-profiler)

[Unity power efficiency demo sample (GitHub)](https://github.com/android/games-samples/tree/main/unity/power_efficiency_demo)