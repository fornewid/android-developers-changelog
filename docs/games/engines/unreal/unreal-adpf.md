---
title: https://developer.android.com/games/engines/unreal/unreal-adpf
url: https://developer.android.com/games/engines/unreal/unreal-adpf
source: md.txt
---

# ADPF Unreal Engine plugin

The[Android Dynamic Performance Framework)](https://developer.android.com/games/optimize/adpf)(ADPF) plugin for[Unreal Engine](https://www.unrealengine.com/en-US)provides stable performance and prevents thermal throttling.

You can[download the plugin](https://github.com/android/adpf-unreal-plugin)from GitHub.

## How to use the ADPF Unreal Engine plugin

1. Download the plugin

2. Copy the plugin into the project plugin folder

3. Enable the ADPF Unreal Engine plugin in the Unreal editor

4. Relaunch Unreal editor

5. Build and[cook](https://dev.epicgames.com/documentation/en-us/unreal-engine/cooking-content-in-unreal-engine?application_version=5.0)the game

![Enable ADPF Unreal Engine plugin.](https://developer.android.com/static/images/games/engines/unreal/unreal-adpf.png)**Figure 1.**Enable ADPF Unreal Engine plugin.

## Plugin console configuration

The plugin has the following[Unreal Engine console variables](https://dev.epicgames.com/documentation/en-us/unreal-engine/console-varaibles-cplusplus-in-unreal-engine)which enable you to change plugin options at runtime:

|                CVar                 | Valid Values | Default Value |                                                                                                              Description                                                                                                               |
|-------------------------------------|--------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| r.AndroidPerformanceEnabled         | 0, 1         | 1             | Enable/disable the Android Performance plugin. The plugin uses the Android adaptability API to adjust the game settings based on the thermal status of the device and will adjust the CPU as needed. 0: off (disabled) 1: on (enabled) |
| r.AndroidPerformanceHintEnabled     | 0, 1         | 1             | Enable/disable the performance hint manager. Enable this setting for optimal thread boosting on supported Android devices. 0: off (disabled) 1: on (enabled)                                                                           |
| r.AndroidPerformanceChangeQualities | 0, 1, 2      | 1             | Choose how the thermal status adjusts the game's fidelity level. 0: The system does not adjust any settings 1: Settings are adjusted according to the thermal headroom 2: Settings are adjusted according to the thermal listener      |

## How the ADPF Unreal Engine plugin works

The plugin calls the`Monitor()`function every frame and checks the elapsed time since the previous thermal check. If at least one second has passed, the plugin reads the current temperature and determines whether a change in graphic quality is necessary (for example, if the game is thermally throttled or near the thermal throttling threshold) and adjusts the settings accordingly.

The plugin also reports target and actual frame duration to the[performance hint session API](https://developer.android.com/games/optimize/adpf/performance-hint-api)and boosts CPU frequency or adjusts CPU scheduling if needed.
![ADPF Unreal Engine plugin flowchart.](https://developer.android.com/static/images/games/engines/unreal/ureal-adpf-flowchart.png)**Figure 2.**ADPF Unreal Engine plugin flowchart.

## How to change graphic quality based on thermal state

The plugin adjusts graphic quality using[Unreal Engine Scalability](https://dev.epicgames.com/documentation/en-us/unreal-engine/scalability-reference-for-unreal-engine)based on the feedback from the thermal APIs. Unreal Engine Scalability has four levels from 3 (highest quality) to 0 (lowest quality). Each level is mapped to resolution scale, view distance, anti-aliasing, post-processing, and other features.
![Unreal Engine Scalability.](https://developer.android.com/static/images/games/engines/unreal/unreal-adpf-scalability.png)**Figure 3.**Unreal Engine Scalability.

ADPF has two ways to determine the thermal state of the device:[thermal headroom](https://developer.android.com/reference/android/os/PowerManager#getThermalHeadroom(int))and[thermal status](https://developer.android.com/reference/android/os/PowerManager#getCurrentThermalStatus()). Thermal headroom provides a more precise value; and so, the plugin uses thermal headroom by default and disables the thermal status API.

The Unreal Engine Scalability changes based on following thermal values:

**Thermal headroom**

- **\< 0.75:**Quality level 3
- **0.75 to 0.85:**Quality level 2
- **0.85 to 0.95:**Quality level 1
- **\> 0.95:**Quality level 0

| **Note:** For reference, a value of 1.0 represents the onset of performance-impacting thermal throttling.

**Thermal status**

- **None:**Quality level 3
- **Light:**Quality level 2
- **Moderate:**Quality level 1
- **Severe and Critical:**Quality level 0

For more information, see[Thermal API](https://developer.android.com/games/optimize/adpf/thermal).

## Performance hint APIs

The plugin has two types of performance hint sessions --- one for the game thread, the other for render threads (Render and RHI threads). These two types of performance hints are used to report actual and target duration of every frame. The system adjusts CPU frequency and makes better scheduling choices when the actual duration is different from the target duration.

For details, see[Performance Hint API](https://developer.android.com/games/optimize/adpf/performance-hint-api).

## Best practices

The plugin prevents thermal throttling and provides a sustained target FPS with its basic implementation. To achieve immediate results, apply ADPF with the default Unreal Engine scalability levels.

However, as each game is different, fine tune[scalability levels](https://dev.epicgames.com/documentation/en-us/unreal-engine/scalability-reference-for-unreal-engine)for each parameter, such as resolution scale, view distance, anti-aliasing, post-processing, shadows, textures, and effects to allow ADPF to fully deliver dynamic performance for your game.

Here are the three key steps to getting the best results with the ADPF Unreal plugin:

- **Establish a baseline:** Before using ADPF, thoroughly profile your game's performance. This data will serve as a valuable benchmark for comparison after you implement the plugin.![ADPF Unreal Engine best pracices.](https://developer.android.com/static/images/games/engines/unreal/unreal-adpf-best-practices-1.png)**Figure 4.**Establish a baseline.
- **Harness Unreal Scalability:** Experiment with Unreal Scalability, even if it offers only modest performance gains. This will help give performance benefits without much effort.![ADPF Unreal Engine best pracices.](https://developer.android.com/static/images/games/engines/unreal/unreal-adpf-best-practices-2.png)**Figure 5.**Harness Unreal Scalability.
- **Prioritize in-game graphic settings:** Optimize your in-game graphic quality levels. These settings are tailored specifically to your game's content, ensuring smoother frame rates and better thermal management.![ADPF Unreal Engine best pracices.](https://developer.android.com/static/images/games/engines/unreal/unreal-adpf-best-practices-3.png)**Figure 6.**Prioritize in-game graphic settings.