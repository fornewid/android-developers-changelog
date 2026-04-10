---
title: https://developer.android.com/games/optimize/adpf/gamemode/gamemode-interventions
url: https://developer.android.com/games/optimize/adpf/gamemode/gamemode-interventions
source: md.txt
---

[Video](https://www.youtube.com/watch?v=9j25t_6TD48)

*Game Mode interventions* are
game-specific optimizations set by original equipment manufacturers (OEMs)
to improve the performance of games that are no longer being updated by
developers. For example:

- Using WindowManager backbuffer resize.
- Using ANGLE instead of native GLES drivers.

You can have your game support and manage the
[Game Mode API](https://developer.android.com/games/optimize/adpf/gamemode/gamemode-api), to have it override
Game Mode interventions provided by the OEM.

The Game Mode API and interventions are available on:

- Select [Android 12](https://developer.android.com/about/versions/12/get) devices
- Devices running [Android 13](https://developer.android.com/about/versions/13/get) or higher

Each game can:

- Implement the Game Mode API behavior,
- Propose Game Mode interventions settings to OEMs, or
- Explicitly opt out of Game Mode interventions.

> [!WARNING]
> **Warning:** OEMs might choose to implement Game Mode interventions without developer feedback.

## Background

This section describes what the Game Mode interventions do and how to optimize
your game for each mode.

### WindowManager backbuffer resizing

The [WindowManager](https://developer.android.com/reference/android/view/WindowManager) backbuffer resize
intervention can reduce a device's GPU load. It can also reduce
battery consumption when a game is paced at a target frame rate.

Enabling resize can result in a reduction of up to 30% of GPU and 10% of overall
system power usage. The results can vary based on the
device used, environmental conditions, and other factors, such as simultaneous
processing.

An unpaced game that is GPU bound is likely to experience higher frame rates
during reduced GPU loads.

We strongly recommend that all games are
[well paced](https://developer.android.com/games/sdk/frame-pacing), because uneven frame rates significantly
impact how users perceive performance.

### FPS throttling

Android FPS throttling is a Game Mode intervention that helps games run at a
more stable frame rate to reduce battery consumption. The intervention is
available in [Android 13](https://developer.android.com/about/versions/13/get) or later. For more
information, see the [FPS throttling overview](https://developer.android.com/games/optimize/adpf/gamemode/fps-throttling).

## Evaluate Game Mode interventions

This sections uses the [adb](https://developer.android.com/studio/command-line/adb) command.

## Set up the modes

You must opt out of Game Modes in the app's
[Game Mode config file](https://developer.android.com/games/optimize/adpf/gamemode/gamemode-api#opt-in_game_modes)
before testing the Game Mode interventions. Otherwise the platform will bypass
them and respect only in-game optimizations.

    <?xml version="1.0" encoding="UTF-8"?>
    <game-mode-config
        xmlns:android="http://schemas.android.com/apk/res/android"
        android:supportsBatteryGameMode="false"
        android:supportsPerformanceGameMode="false"
    />

### (Optional) Back up existing device config

For Pixel or other devices, there might be a pre-existing game intervention
config in your device config. You can query the config using the command:

    adb shell device_config get game_overlay <PACKAGE_NAME>

If the query returns `null`, ignore the pre-existing config. Otherwise, save it
and reset to it after the evaluation.

### Evaluate Interventions

To evaluate the WindowManager backbuffer resize intervention on its own, use the
following command to set different WindowManager buffer resize values across
game modes.

    adb shell device_config put game_overlay <PACKAGE_NAME>
    mode=2,downscaleFactor=0.9:mode=3,downscaleFactor=0.5

In the example above, `mode=2` is "Performance" and `mode=3`
is "Battery Saver". The `downscaleFactor` value is specified as a percent that
applies to the resize setting (for example, 0.7 is 70% and 0.8 is 80%). A 90%
(0.9) resize is almost negligible, whereas 50% (0.5) is significant.

**Warning:** Child processes may not be resized correctly in Android 12. In
particular, make sure toasts and pop-ups render correctly. We
recommend that you limit the resize setting to at least 70%.

After the new resize valies are set up, switch between game modes to see how
your game is affected by the WindowManager backbuffer resize intervention:

    adb shell cmd game mode [standard|performance|battery] <PACKAGE_NAME>

Make sure you restart the game after each game mode selection. The
downscaling intervention requires app restart.

## Opt-out from interventions

You can control whether an intervention is applied to your game
by opting out. Each intervention has its own opt-out setting.

1. The same config XML file that's used to control opt-in and opt-out of Game Modes is also used for intervention settings:

    <?xml version="1.0" encoding="UTF-8"?>
    <game-mode-config
        xmlns:android="http://schemas.android.com/apk/res/android"
        android:allowGameDownscaling="false"
        android:allowGameFpsOverride="false"
    />

1. Rebuild and resubmit your game to opt-out.

By default, interventions set by the original equipment manufacturers
(OEMs) will be used unless you explicitly opt your game out of using them.

## Resources

For more information about measuring and optimizing game performance:

- [System Profilers](https://developer.android.com/games/tools) - analyze CPU usage and graphics calls.

- [Android GPU Inspector](https://developer.android.com/agi) - profile graphics on
  Android.

- [Android Frame Pacing Library](https://developer.android.com/games/sdk/frame-pacing) - help OpenGL and
  Vulkan games achieve smooth rendering and correct frame pacing.

- [Android Performance Tuner](https://developer.android.com/games/sdk/performance-tuner) - measure and
  optimize frame rate and graphics across Android devices at scale.

- [Power Profiler](https://developer.android.com/studio/profile/power-profiler) - find where your app uses
  more energy than necessary.