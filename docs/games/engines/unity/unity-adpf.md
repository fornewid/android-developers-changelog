---
title: https://developer.android.com/games/engines/unity/unity-adpf
url: https://developer.android.com/games/engines/unity/unity-adpf
source: md.txt
---

# Unity Adaptive Performance and Android provider

[Unity Adaptive Performance](https://docs.unity3d.com/Packages/com.unity.adaptiveperformance@5.0/manual/installing-and-configuring.html)is a tool for game developers who want to optimize their games on mobile devices, particularly for the diverse Android ecosystem. Adaptive Performance enables your game to adapt to device performance and thermal characteristics in real time, ensuring a smooth and efficient gaming experience. The[Android provider](https://docs.unity3d.com/Packages/com.unity.adaptiveperformance.google.android@1.2/manual/index.html)implements Adaptive Performance on Android devices.

## How to use Unity Adaptive Performance

1. **Install the Adaptive Performance package:** Go to the Unity Package Manager and install the`Adaptive Performance`package.

2. **Install the Android provider:**In the Package Manager, find the section for Adaptive Performance and install the Android provider.

3. **Access Adaptive Performance settings:** In the Unity Editor, go to**Edit \> Project Settings**and find the Adaptive Performance section.

4. **Set Performance parameters:** Adjust settings like**Target Frame Rate** ,**Quality Settings**, and other performance thresholds as needed.

Unity Adaptive Performance needs a provider to get all the required information from the device. The Android provider is supported on Adaptive Performance 5.0 onwards, and it supports Unity 2021.3 onwards. The Unity 2021 and 2022 version package manager downloads Adaptive Performance 4.0, so a[manual update to version 5.0](https://docs.unity3d.com/Manual/upm-manifestPrj.html)is required.
![Adaptive Performance and Android Provider.](https://developer.android.com/static/images/games/engines/unity/unity-adpf-android-provider.png)**Figure 1.**Adaptive Performance and Android provider setup.

The Android provider 1.0 version is only enabled on Pixel devices. You should therefore it is use the newer 1.2 version.

## ADPF Performance hint API

Android provider implements ADPF performance hints by default. Every frame, the provider reports actual duration from the sum of the cpu and gpu duration and the target duration from the render frame rate.

The target duration from the render frame rate every frame. (See[Performance Hint API](https://developer.android.com/games/optimize/adpf/performance-hint-api).)

## Graphic scalers

Unity Adaptive Performance provides graphic scalers for**Framerate** ,**Resolution** ,**LOD**, and other profile properties. The scalers have min and max scales; each scale is changed by the device thermal warning level and thermal trend.
![Adaptive Performance graphic scalers.](https://developer.android.com/static/images/games/engines/unity/unity-adpf-scaler.png)**Figure 2.**Adaptive Performance graphic scalers.

## Best practices

The plugin attempts to prevent thermal throttling and provides a sustained target FPS with its basic implementation. To achieve immediate results, use ADPF with the default Unity Adaptive Performance scalers.

However, as each game is different, fine tune Unity Adaptive Performance scalers for each parameter, such as resolution, LOD, shadows, view distance, and others to allow ADPF to fully deliver dynamic performance for your game.

Here are the three key steps to getting the best results with ADPF Unity Adaptive Performance:

- **Establish a baseline:** Before using ADPF, thoroughly profile your game's performance. This data will serve as a valuable benchmark for comparison after you implement the plugin.![ADPF Unity Adaptive Performance best practices.](https://developer.android.com/static/images/games/engines/unity/unity-adpf-best-practices-1.png)**Figure 3.**Establish a baseline.
- **Harness Unity Adaptive Performance scalers:** Experiment with Unity Adaptive Performance scalers to gain performance benefits without much effort.![ADPF Unity Adaptive Performance best practices.](https://developer.android.com/static/images/games/engines/unity/unity-adpf-best-practices-2.png)**Figure 4.**Harness Unity Adaptive Performance scalers.
- **Prioritize in-game graphic settings:** Optimize your in-game graphic quality levels. These settings are tailored specifically to your game's content, ensuring smoother frame rates and better thermal management.![ADPF Unity Adaptive Performance best practices.](https://developer.android.com/static/images/games/engines/unity/unity-adpf-best-practices-3.png)**Figure 5.**Prioritize in-game graphic settings.

## Additional resources

See how[Kakao Games Ares used Unity Adaptive Performance](https://developer.android.com/stories/games/kakaogames-adaptability)to increase FPS stability to 96%.