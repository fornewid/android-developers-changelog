---
title: Sample, Codelab and Developer Stories  |  Android game development  |  Android Developers
url: https://developer.android.com/games/optimize/adpf/sample-codelab-story
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Games dev center](https://developer.android.com/games)
* [Guides](https://developer.android.com/games/guides)

Send feedback

# Sample, Codelab and Developer Stories Stay organized with collections Save and categorize content based on your preferences.




## Sample App

The [ADPF sample app](https://github.com/android/games-samples/tree/main/agdk/adpf)
demonstrates the basic use of the ADPF API.

![ADPF Demo Game Application](/static/games/optimize/adpf/images/adpf_demo_app.png)


**Figure 1.** ADPF Demo Game Application

The sample displays the device's thermal status using the ADPF
[`getThermalHeadroom`](/reference/android/os/PowerManager#getThermalHeadroom(int))
API and the [thermal status](/reference/android/os/PowerManager.OnThermalStatusChangedListener)
API. The app also dynamically changes the workload based on the Thermal headroom
and the [Performance Hint Manager API](/reference/android/os/PerformanceHintManager)
to control render thread performance.

## Codelab

The [Integrating Adaptability Features Into Your C++ Game](/adaptability-codelab)
codelab guides you to integrate ADPF features into your game with simple steps
that you can follow at your own pace. At the end of the codelab, you will have
integrated the following features and will better understand their
functionalities:

* [Thermal API](/games/optimize/adpf#thermal): listen to device thermal condition and react before the device falls into thermal throttling state.
* [Game Mode API](/games/optimize/adpf/gamemode/about-API-and-interventions): understand player's optimization preference (maximize performance or preserving battery) and adjust accordingly.
* [Game State API](/reference/android/app/GameState): let the system know the state of your game (loading, playing, UI, etc) and the system can adjust resources accordingly (boost I/O, or CPU, GPU, etc).
* [Performance Hint API](/reference/android/os/PerformanceHintManager): let the system know your threading model and workload so that the system can allocate resources accordingly.

![ADPF Codelab Infographic](/static/games/optimize/adpf/images/adpf_codelab.png)


**Figure 2.**ADPF Codelab Infographic

## Developer Stories

Check out how game developers increased their FPS stability and optimize their
power consumption using Adaptability APIs in these developer success stories!

* [Kakao Games increased FPS stability to 96% through Android Adaptability](/stories/games/kakaogames-adaptability)
* [Gameloft reduces device power consumption by 70%, resulting in 35% longer play time with the Game Mode API](/stories/games/gameloft-gamemode)
* [Android Game Development Kit (AGDK) update: Adaptability and performance features](https://www.youtube.com/watch?v=_-FwUrQAsVg)
* [GDC Vault - Google Developer Summit: Improving Game Performance with Android Dynamic Performance Framework](https://www.gdcvault.com/play/1029174/Google-Developer-Summit-Improving-Game)
* [MediaTek enhances dynamic performance of Android SoCs](/stories/games/mediatek-adpf)
* [NCSoft Lineage W improves sustained performance and prevents thermal throttling by using ADPF](/stories/games/lineagew-adpf)
* [ARM getting started with Android Dynamic Performance Framework (ADPF) in Unreal Engine](/stories/games/arm-adpf)
* [Netmarble Games: Optimizing Performance with ADPF](/stories/games/netmarble-got-adpf)






Send feedback