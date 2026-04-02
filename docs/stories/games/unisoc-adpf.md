---
title: https://developer.android.com/stories/games/unisoc-adpf
url: https://developer.android.com/stories/games/unisoc-adpf
source: md.txt
---

# UNISOC Leverages ADPF for Enhanced Android Gaming Performance

Optimizing performance and thermal management is a critical challenge for game developers on Android. To create the best possible player experiences, developers need tools to balance high frame rates with sustainable power consumption. The Android Dynamic Performance Framework (ADPF) provides a crucial set of APIs that allow games to interact directly with the power and thermal systems of a device, enabling this fine-tuned optimization.

UNISOC is embracing these tools to deliver superior gaming on its SoCs. Starting with Android 14, UNISOC products fully support core ADPF APIs, including Performance Hint, Thermal, and Game Mode/State. To further enhance performance on its SoCs, UNISOC utilizes these ADPF APIs within its own UNISOC Miracle Gaming engine to monitor system workloads and dynamically adjust performance, ensuring a smoother and more stable gaming experience.
![Figure 1: UNISOC Miracle Gaming](https://developer.android.com/static/images/cards/distribute/stories/unisoc-adpf.jpg)Figure 1: UNISOC Miracle Gaming

## Optimizing Performance and Thermals with ADPF

UNISOC's implementation of ADPF gives developers powerful tools to manage game performance in real-time.

- **Performance Hint:** The`PerformanceHintManager`allows applications to pass information to the system, enabling the SoC to allocate the right amount of resources at the right time. By providing hints about workloads and reporting the actual duration of frames, games can help the system dynamically accelerate drawing and layer composition, leading to more consistent performance.

- **Thermal API:** To prevent disruptive thermal throttling, developers can use the`getThermalHeadroom()`API. This function provides a prediction of the device's thermal state, allowing an application to proactively adjust its workload before overheating occurs. This foresight is key to stabilizing the game's frame rate during intense, long-lasting sessions.

- **Game Mode and Game State APIs:** These APIs improve communication between the game and the system.`GameMode`allows users to signal their intent (e.g., choosing a "performance" setting in the game), while`GameState`lets the game inform the OS of its current status (e.g., loading, playing, etc.). Under the hood, the system can then leverage interventions like Game Resolution Scaling and Game FPS Overrides to optimize performance based on this context.

## Delivering Improved Frame Rates and Power Efficiency

The integration of ADPF on UNISOC SoCs delivers tangible improvements in frame rates, power consumption, and the overall gaming experience. In tests with the popular title LineageW from NCSOFT, the benefits were clear across various graphics settings.

At medium graphics quality, the game achieved a significant**28.1% frame rate boost** while simultaneously**decreasing power consumption by 3.7%**, achieving the dual benefits of a smoother experience and improved efficiency.

The results at other settings were also impressive:

- At high graphics settings, the frame rate soared by an impressive**50.1%**with only a minor 3.1% increase in power draw, showcasing ADPF's ability to unlock significant performance headroom.

- At low graphics settings, players saw an**11.5% increase in frame rate** with a corresponding**9.9% increase in power consumption**, demonstrating performance gains even on less demanding configurations.

![Figure 2: Low Graphics Frame Rate](https://developer.android.com/static/images/cards/distribute/stories/low-graphics-framerate.png)Figure 2: Low Graphics Frame Rate![Figure 3: Mid Graphics Frame Rate](https://developer.android.com/static/images/cards/distribute/stories/med-graphics-framerate.png)Figure 3: Mid Graphics Frame Rate![Figure 4: High Graphics Frame Rate](https://developer.android.com/static/images/cards/distribute/stories/high-graphics-framerate.png)Figure 4: High Graphics Frame Rate![Figure 5: Power Consumption](https://developer.android.com/static/images/cards/distribute/stories/power-consumption.png)Figure 5: Power Consumption

Furthermore, UNISOC demonstrates an "Adaptive Optimization" feature. When a user enables this option, the application can automatically adjust graphical elements like texture, foliage, and effect quality in response to system feedback, ensuring the delivery of a more stable frame rate.

## What's next for adaptive performance on UNISOC SoCs

UNISOC is committed to deepening its integration with ADPF. As the framework evolves, the UNISOC Miracle Gaming engine will continue to incorporate the latest core ADPF features, ensuring that developers and gamers benefit from the most up-to-date performance and thermal management technologies on UNISOC-powered devices.

## Get started with Android adaptability

The Android Dynamic Performance Framework is now available to all Android game developers for[Unity, Unreal, Cocos Creator game engines](https://developer.android.com/games/optimize/adpf/game-engine-support)and through native C++ libraries.

- For**Unity** developers, you can get started with the[Adaptive Performance provider v5.0.0.](https://docs.unity3d.com/Packages/com.unity.adaptiveperformance.google.android@1.2/manual/index.html)Note that the Thermal API is supported by most Android devices from Android 11 (API level 30), and the Performance Hint API from Android 12 (API level 31).

- For**Unreal** developers, you can get started with the[Android Dynamic Performance Unreal Engine plugin](https://github.com/android/adpf-unreal-plugin)for most Android devices targeting Android 12 (API level 31) or higher.

- For**Cocos Creator** , you can get started with the Thermal API from v3.8.2 and the Performance Hint API from[v3.8.3.](https://github.com/cocos/cocos-engine/tree/v3.8.3)

- For custom engines, you can reference the[native ADPF C++ sample](https://github.com/android/games-samples/tree/main/agdk/adpf).