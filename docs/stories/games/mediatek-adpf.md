---
title: https://developer.android.com/stories/games/mediatek-adpf
url: https://developer.android.com/stories/games/mediatek-adpf
source: md.txt
---

# MediaTek enhances dynamic performance of Android SoCs

Improving performance and thermal management is essential for developing successful games on Android. Traditionally, developers had to manage these issues by decreasing game fidelity or by further optimizing the renderer. These changes tend to be game specific and can often be inflexible.

Several participants in the Android ecosystem offer adaptive performance APIs to developers. To simplify the integration of adaptive performance features and reduce fragmentation in the ecosystem, Google and MediaTek are collaborating to integrate our offerings: Android Dynamic Performance Framework (ADPF) and MediaTek Adaptive Gaming Technology (MAGT).

[ADPF](https://developer.android.com/games/optimize/adpf)offers developers the ability to adjust game workload based on real-time thermal situations and provide hints to the OS to optimize performance for the current workload. You can use these signals to adjust fidelity and performance settings such as the resolution, frame rate, and even resource loading strategy. This lets you better balance performance, thermals, and fidelity, giving Android gamers the best possible experience. The Android ecosystem has been putting this technology to great use. Kakao Games's Ares was able to[increase FPS stability to 96%](https://developer.android.com/stories/games/kakaogames-adaptability)by adjusting the workload at runtime in response to the thermal API.

MediaTek is a leading provider of SoCs on Android. The company produces a number of chips, such as the new Dimensity 9300. MediaTek also offers the MAGT SDK, which has been available since 2021. The SDK provides advanced features for performance tuning on MediaTek SoCs, such as fine-grained information about real-time performance, and hints for increasing workloads. In addition to offering MAGT to developers, MediaTek has begun offering enhanced ADPF capabilities.
![](https://developer.android.com/static/images/cards/distribute/stories/mediatek_google.jpg)**Figure 1.**MediaTek and Google collaboration.

## Prevent thermal throttling with ADPF and optimize performance

MediaTek allows the ADPF framework to access the current and target device temperatures to prevent severe throttling. By utilizing the ADPF[`getThermalHeadroom()`](https://developer.android.com/reference/kotlin/android/os/PowerManager#getthermalheadroom)function, applications can obtain an estimate of the available thermal headroom before the device reaches severe throttling. Using this estimate, applications can dynamically adjust workloads to prevent the device from triggering throttling, thereby enhancing the overall user experience.

The application (using Unity's[Boat Attack demo](https://github.com/Unity-Technologies/BoatAttack)as an example) also uses the Performance Hint Session API to optimize its performance. It provides the target frame time and current frame time for each frame through the[`updateTargetWorkDuration()`](https://developer.android.com/reference/kotlin/android/os/PerformanceHintManager.Session#updatetargetworkduration)and[`reportActualWorkDuration()`](https://developer.android.com/reference/kotlin/android/os/PerformanceHintManager.Session#reportactualworkduration)functions respectively. The MediaTek platform calculates the workload between two[`reportActualWorkDuration()`](https://developer.android.com/reference/kotlin/android/os/PerformanceHintManager.Session#reportactualworkduration)calls and allocates adequate CPU capacity to ensure the workload can be completed within the target duration.

As a result, the MediaTek platform consistently delivers optimal frames per second (FPS) with balanced power consumption, guaranteeing a smooth user experience.

## Enable better frame rates, reduced power consumption, and longer gaming sessions

Overall, the Unity Boat Attack demo improved frame rates by 8.5fps, reduced power consumption by 12%, and enabled longer game sessions by 25 minutes or more. The FPS standard deviation dropped by 25%. Such a dramatic improvement lets you increase the fidelity of your games and run play sessions for a longer period of time in a thermally sustainable way.
![](https://developer.android.com/static/images/cards/distribute/stories/mediatek_table.png)**Figure 2.**Performance results.![](https://developer.android.com/static/images/cards/distribute/stories/mediatek_fps.png)**Figure 3.**FPS chart.

Even without adjusting the fidelity settings, just by enabling performance hint session, the workload was able to to decrease its average Render thread time by almost 10%.

## What's next for adaptive performance on MediaTek SoCs

ADPF will be upgraded over the coming years with new features and to add new device-agnostic features from MAGT. For developers looking to get even more out of their MediaTek devices, the MAGT SDK contains advanced capabilities that uniquely target MediaTek chipset architectures and will soon also offer core ADPF features.
![](https://developer.android.com/static/images/cards/distribute/stories/mediatek_logo.png)![](https://developer.android.com/static/images/cards/distribute/stories/android_logo.png)**Figure 4.**MediaTek aligned with Android.

## Get started with Android adaptability

Android Dynamic Performance Framework is now available to all Android game developers for[Unity, Unreal, Cocos Creator game engines](https://developer.android.com/games/optimize/adpf/game-engine-support)and through our native C++ libraries.

- For Unity developers, you can get started with the[Adaptive Performance provider v5.0.0](https://docs.unity3d.com/Packages/com.unity.adaptiveperformance.google.android@1.2/manual/index.html). Note that Thermal API is supported by most Android devices from Android 11 (API level 30), and Performance Hint API from Android 12 (API level 31).
- For Unreal developers, you can get started with the[Android Dynamic Performance Unreal Engine plugin](https://github.com/android/adpf-unreal-plugin)for most Android devices targeting Android 12 (API level 31) or higher.
- For Cocos Creator, you can get started with Thermal API from v3.8.2 and Performance Hint API from[v3.8.3](https://github.com/cocos/cocos-engine/tree/v3.8.3).

For these game engines, the thermal APIs are integrated with Adaptive Performance to help you retrieve device thermal information, and the performance hint API is called automatically every`Update()`or`Monitor()`without any additional work. And lastly, for custom engines, you can reference our[native ADPF C++ sample](https://github.com/android/games-samples/tree/main/agdk/adpf).

## Additional resources

Learn how[Android Dynamic Performance Framework](https://developer.android.com/games/optimize/adpf)can help you stabilize your game's FPS and reduce thermal throttling.

Learn about[MediaTek Adaptive Gaming Technology](https://www.mediatek.com/technology/gaming-technologies)for advanced performance tuning on MediaTek SoCs.