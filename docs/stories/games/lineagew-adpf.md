---
title: https://developer.android.com/stories/games/lineagew-adpf
url: https://developer.android.com/stories/games/lineagew-adpf
source: md.txt
---

# NCSoft Lineage W improves sustained performance and prevents thermal throttling by using ADPF

![Screenshot from NCSoft Lineage W](https://developer.android.com/static/images/cards/distribute/stories/lineagew_game.png)

NCSoft Lineage W is a massively multiplayer online role-playing game (MMORPG) developed by NCSoft. This game inherits the legacy of the original Lineage W game and offers an environment where players from around the world can cooperate and compete through global servers. Set in a unique medieval fantasy world, Lineage W provides players with a deep gaming experience through various classes, skills, and combat systems.

NCSoft used the Android Dynamic Performance Framework to maximize graphical quality while preventing performance issues caused by thermal throttling.

## Android Dynamic Performance Framework

The[Android Dynamic Performance Framework (ADPF)](https://developer.android.com/games/optimize/adpf)provides information on resource usage and helps developers respond to changing performance, thermal, and user situations in real time. It includes both the Thermal and Performance Hint APIs. The[Thermal APIs](https://developer.android.com/games/optimize/adpf/thermal)offer information about a device's thermal state, while the[Performance Hint API](https://developer.android.com/games/optimize/adpf/performance-hint-api)provides performance hints that assist Android in selecting the optimal CPU operating point and core placement.

## Unreal Engine ADPF plugin

The[Unreal Engine ADPF plugin](https://github.com/android/adpf-unreal-plugin)provides the easiest way to use ADPF in games using the Unreal Engine.

The plugin checks the device's thermal status every second. When the device overheats, the plugin adjusts the graphic quality settings using the default Unreal Scalability settings. There are four levels and each level is mapped to various graphic qualities (resolution, view distance, post-processing, and so on).

If you already have in-game settings (such as low, mid, and high quality) that are configurable by the player, we recommend you to use these settings instead of the default Unreal Scalability levels.

The plugin uses two methods to check device thermals: one is by assessing the thermal headroom and the other is by checking the thermal status. The thermal headroom provides more detailed information, and it is enabled by default.

The plugin creates the two performance hint sessions for the game and render threads. It reports the target and actual duration to the framework every frame, and it helps achieve the target frames per second (FPS).

## How NCSoft optimized performance

Your browser doesn't support the video tag.**Figure 1.**In game video.

Lineage W used ADPF to prevent performance issues caused by thermal throttling. They endeavored to maximize the use of graphical quality settings that provide significant performance gains while minimizing the impact on actual gameplay. NCSoft verified the stability and operation of each stage when adjusting the quality through the headroom value. Various tests were required to provide users with a good gaming experience for each adjusted value of the graphics quality setting.

The game targets 30 FPS by default, but NCSoft changed the target FPS to 60 in order to test how ADPF can improve their FPS.

![Screenshot from NCSoft Lineage W](https://developer.android.com/static/images/cards/distribute/stories/lineagew_graph1.png "Figure 2: Performance result without Android Adaptability")

During 30 minutes of gameplay testing on a Pixel 6 running Android 13, the FPS dropped drastically from 60 FPS to 32 FPS and the thermal headroom value reached 1.0f (the threshold for severe thermal throttling) at the 4 min mark.

![Screenshot from NCSoft Lineage W](https://developer.android.com/static/images/cards/distribute/stories/lineagew_graph2.png "Figure 3: Performance result with Unreal Scalability")

When the game used the Unreal Engine ADPF plugin with the default Unreal Scalability, it was able to maintain 60 FPS for 15 mins. The average frame rate throughout these 30 minutes also increased to 57.5 FPS. However, the thermal headroom showed similar values as before, meaning that the device heated up in a similar way and suffered from thermal throttling.

![Screenshot from NCSoft Lineage W](https://developer.android.com/static/images/cards/distribute/stories/lineagew_graph3.png "Figure 4: Performance result with Lineage W graphic quality")

To address this, the Lineage W team decided that they needed to give ADPF more control over the fidelity parameters to avoid thermal throttling. After integrating Lineage W's in-game graphics quality settings with the Unreal Engine ADPF plugin, they achieved optimal results. This integration resulted in stable frame rates at 60 FPS while maintaining a thermal headroom value lower than 1.0, indicating efficient thermal management.

By using Lineage W's in-game quality settings with ADPF, NCSoft was able to deliver a more stable and enjoyable user experience.

![Screenshot from NCSoft Lineage W](https://developer.android.com/static/images/cards/distribute/stories/lineagew_option.jpg "Figure 5: In-game graphic option")

Because ADPF is not fully supported by all Android-powered device manufacturers, NCSoft implemented this as an in-game option "Adaptive Performance Optimization" for players to opt-in.

## Get started with ADPF and Unreal Engine plugin

Developers who are interested in using Android Adaptability or the ADPF Unreal Engine plugin should do the following:

- Learn more about[ADPF](https://developer.android.com/games/optimize/adpf)and the[Unreal Engine ADPF plugin](https://github.com/android/adpf-unreal-plugin).
- Customize your scalers to your game content instead of using the[Unreal Engine scalability](https://dev.epicgames.com/documentation/en-us/unreal-engine/scalability-reference-for-unreal-engine).
- Monitor the performance of the game to ensure that its meeting expectations. Experiment with different settings to find the best performance and minimal thermal increase.
- Change graphic quality settings separately to reduce sudden performance decreases.

Regardless of which engine you use, you can always choose to use the APIs directly. Learn more at[Android Adaptability](https://developer.android.com/games/optimize/adpf)and[Unreal Engine ADPF plugin](https://github.com/android/adpf-unreal-plugin).