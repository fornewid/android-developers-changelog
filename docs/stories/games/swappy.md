---
title: https://developer.android.com/stories/games/swappy
url: https://developer.android.com/stories/games/swappy
source: md.txt
---

# Mir 2 improves rendering performance by using the Frame Pacing library

![](https://developer.android.com/static/images/cards/distribute/stories/mir-2-preview.jpg)Mir 2: Return of the King

[Mir 2: Return of the King](https://play.google.com/store/apps/details?id=com.krsc.shark)is a high-quality Legend IP mobile game authorized by Actoz Soft and developed by[HK ZHILI YAOAN LIMITED](https://www.zhiliyaoan.com/)using the Unity game engine.

This game not only perfectly recreates the feelings of*Mir 2*, a representative of Korean fantasy MMORPG, but also offers many of the most popular game contents, such as equipment collection, large-scale sand attack, and other core gameplay.

The game used the Android[Frame Pacing library](https://developer.android.com/games/sdk/frame-pacing)(Swappy) to improve the stability of its frame rate, achieve smooth rendering, and significantly boost their Android Vitals (Slow Session metric).

## **Slow Sessions launched on Android vitals**

[Slow Sessions](https://developer.android.com/topic/performance/vitals/slow-session)is an Android vitals metric in Google Play console. A slow session has more than 25% slow frames. A frame is slow if it is:

1. At 20fps, it is not presented within 50ms after the previous frame.

2. At 30fps, it is not presented within 34ms after the previous frame.

In due course, Play will start steering users away from games that cannot achieve 20 FPS on their phones.

There are many reasons a frame might present or render longer on the screen than the developer's target frame time. The game could be CPU or GPU bound, overheating (causing thermal throttling), or there's a**mismatch in the game's framerate and the device's display refresh rate**.

## **What is the Frame Pacing library**

The Android[Frame Pacing library](https://developer.android.com/games/sdk/frame-pacing), also known as Swappy, is part of the AGDK libraries. Swappy helps OpenGL and Vulkan games achieve smooth rendering and correct frame pacing on Android.

The library handles multiple refresh rates if they are supported by the device, which gives a game more flexibility in presenting a frame. For example, for a device that supports a 60 Hz refresh rate as well as 90 Hz, a game that cannot produce 60 frames per second can drop to 45 FPS instead of 30 FPS to remain smooth. The library detects the expected game frame rate and auto-adjusts frame presentation times accordingly.

The Frame Pacing library also improves battery life because it avoids unnecessary display updates. For example, if a game is rendering at 60 FPS but the display is updating at 120 Hz, the screen is updated twice for every frame. The Frame Pacing library avoids this by setting the refresh rate to the value supported by the device that's closest to the target frame rate.

## How Mir 2 improved Rendering performance with the Frame Pacing library

Mir 2 ([미르2: 왕의 귀환](https://play.google.com/store/apps/details?id=com.krsc.shark)) was facing an issue with unstable rendering performance where they experienced 40% slow sessions at a framerate threshold of 20 FPS, much higher than Google Play's 20% threshold.
![](https://developer.android.com/static/images/cards/distribute/stories/swappy-figure-1.png)**Figure 1.**Slow session metric before integrating the Frame Pacing library.

Mir 2 ([미르2: 왕의 귀환](https://play.google.com/store/apps/details?id=com.krsc.shark)) is a high fidelity graphic game, some devices are facing challenges to maintain a stable FPS. Their[frame rate distribution](https://support.google.com/googleplay/android-developer/answer/9844486#zippy=%2Cslow-session-rate-fps-or-fps-games-only)shows lots of sessions are running at FPS lower than 20fps.
![](https://developer.android.com/static/images/cards/distribute/stories/swappy-figure-2.png)**Figure 2.** The game's FPS distribution before integrating the Frame Pacing library.  
Each bucket represents the percentage of sessions where 75% of their frames were faster than the bucket label.

When the display workload takes longer than the application workload, additional frames are added to a queue. This leads, once again, to stuttering and may also lead to an extra frame of latency due to buffer-stuffing.
![](https://developer.android.com/static/images/cards/distribute/stories/swappy-figure-3.png)**Figure 3.**Long frame B gives incorrect pacing for 2 frames---A and B.

The Frame Pacing library solves this by using sync fences ([`EGL_KHR_fence_sync`](https://www.khronos.org/registry/EGL/extensions/KHR/EGL_KHR_fence_sync.txt)and[`VkFence`](https://www.khronos.org/registry/vulkan/specs/1.1-extensions/man/html/VkFence.html)) to inject waits into the application that allow the display pipeline to catch up, rather than allowing back pressure to build up. Frame A still presents an extra frame, but frame B now presents correctly.
![](https://developer.android.com/static/images/cards/distribute/stories/swappy-figure-4.png)**Figure 4.**Frames C and D wait to present.

Mir 2 easily integrated the Frame Pacing library by leveraging Unity's built in[Optimized Frame Pacing](https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html)feature. The action resulted in significant improvement for their rendering performance, specifically dropping the Slow Session metric from**40%** to**10%**.
![](https://developer.android.com/static/images/cards/distribute/stories/swappy-figure-5.png)**Figure 5.**Slow Session improvement after integrating the Frame Pacing library.

The number of slow sessions have been reduced significantly for Mir2 after they integrated the library.
![](https://developer.android.com/static/images/cards/distribute/stories/swappy-figure-6.png)**Figure 6.** The game's FPS distribution after integrating frame pacing.  
Each bucket represents the percentage of sessions where 75% of their frames were faster than the bucket label.

## Get Started with the Frame Pacing library

### How to use the Frame Pacing library in native game engines

See the following guides to integrate the Android Frame Pacing library into your game:

- [Integrate Android Frame Pacing into your Vulkan renderer](https://developer.android.com/games/sdk/frame-pacing/vulkan)
- [Integrate Android Frame Pacing into your OpenGL renderer](https://developer.android.com/games/sdk/frame-pacing/opengl)

### How to use the Frame Pacing library in the Unity game engine

Unity has integrated the Android Frame Pacing library into their engine. To enable this feature in Unity, check the[Optimized Frame Pacing](https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html)checkbox under*Project Settings \> Player \> Settings for Android \> Resolution and Presentation*:
![](https://developer.android.com/static/images/cards/distribute/stories/swappy-figure-7.png)**Figure 7.**Enable Frame Pacing in Unity Engine.

Alternatively, programmatically enable the[Optimized Frame Pacing option](https://docs.unity3d.com/ScriptReference/PlayerSettings.Android-optimizedFramePacing.html)in your logic code to allow Unity to evenly distribute frames for less variance in frame rate, creating smoother gameplay.

### **How to use the Frame Pacing library in Unreal game engine**

Unreal 4.25 and later integrates the Android[Frame Pacing library](https://developer.android.com/games/sdk/frame-pacing), which is part of the[Android Game Development Kit](https://developer.android.com/games/agdk). The[Mobile Frame Pacing](https://docs.unrealengine.com/SharingAndReleasing/Mobile/Rendering/MobileFramePacing/)article explains how to enable the Android Frame Pacing library and how to control frame pacing from C++ code.