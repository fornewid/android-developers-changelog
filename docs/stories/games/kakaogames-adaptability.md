---
title: https://developer.android.com/stories/games/kakaogames-adaptability
url: https://developer.android.com/stories/games/kakaogames-adaptability
source: md.txt
---

# Kakao Games increased FPS stability to 96% through Android Adaptability

![Screenshot from Kakao Games Ares](https://developer.android.com/static/images/cards/distribute/stories/kakaogames_title.jpg "Figure 1: Screenshot from NEW STATE Mobile")

## Background

[Ares: Rise of Guardians](https://play.google.com/store/apps/details?id=com.kakaogames.ares&hl=en_US)is a mobile-to-PC sci-fi MMORPG developed by Second Dive, a game studio based in Korea known for its expertise in developing action RPG series. The game is published by[Kakao Games](https://play.google.com/store/apps/dev?id=6236189329207394247&hl=en_US).

Set in a vast universe with a detailed, futuristic background, Ares is full of exciting gameplay and beautifully rendered characters involving combatants wearing battle suits. However, because of these richly detailed graphics, some users' devices struggled to handle the gameplay.

## What they did

For some users, their device would overheat after just a few minutes of gameplay and enter a thermally throttled state. In this state, the CPU frequency and GPU frequency are reduced, affecting the game's performance and causing the frames per second (FPS) to drop. However, as soon as the decreased FPS improved the thermal situation, the FPS increased again, and the cycle repeated. The FPS fluctuation caused the game to feel stuttery.

To solve this problem, Kakao Games used[Android Adaptability](https://developer.android.com/games/optimize/adpf)and[Unity Adaptive Performance](https://docs.unity3d.com/Packages/com.unity.adaptiveperformance@5.0/manual/index.html)to improve the performance and thermal management of their game.

Android Adaptability is a set of tools and libraries that enable a game to analyze and respond to changing performance, thermal, and user situations in real time. Android Adaptability includes the Android Dynamic Performance Framework (ADPF) thermal APIs, which provide information about the thermal state of a device, and the[`PerformanceHintManager`](https://developer.android.com/reference/android/os/PerformanceHintManager)API, which helps Android choose the optimal CPU operating point and core placement. Both APIs work with the Unity Adaptive Performance package to help you optimize your games.

Android Adaptability and Unity Adaptive Performance work together to adjust the graphics settings of your app or game to match the capabilities of the user's device. The result: improved performance, reduced thermal throttling, lower power consumption, and longer battery life.
Your browser doesn't support the video tag.

## What they achieved

After integrating adaptive performance, Ares is better able to manage its thermal situation, resulting in less throttling. Users are able to enjoy a higher frame rate, and FPS stability has increased from 75% to 96%.

In the charts below, the blue line indicates the thermal warning level. The bottom line (0.7) indicates no warning, the midline (0.8) is throttling imminent, and the upper line (0.9) is throttling.

As the first chart shows, before Ares implemented Android Adaptability, throttling happened after about 16 minutes of gameplay. The second chart shows the result of Android Adaptability integration: throttling doesn't occur until around 22 minutes.

![Screenshot from Kakao Games Ares](https://developer.android.com/static/images/cards/distribute/stories/kakaogames_before.png "Figure 2: Performance result without Android Adaptability")

![Screenshot from Kakao Games Ares](https://developer.android.com/static/images/cards/distribute/stories/kakaogames_after.png "Figure 3: Performance result with Android Adaptability")

Kakao Games also wanted to reduce device heating, which they knew wasn't possible with a continuously high graphic quality setting. The best practice is to gradually lower the graphical fidelity as device temperature increases to maintain a constant framerate and thermal equilibrium. So Kakao Games created a six-step change sequence with Android Adaptability that enabled stable FPS and lower device temperatures.

Automatic changes in fidelity are reflected in the in-game graphic quality settings (resolution, texture, shadow, effect, etc.) in the settings menu. Because some users want the highest graphic quality even if their device can't sustain performance at that level, Kakao Games gave users the option to manually disable Unity Adaptive Performance.

## Get started with Android Adaptability

Android Adaptability and Unity Adaptive Performance are now available to all Android game developers using the Unity Android provider on most Android devices after Android 11 (API level 30), thermal, and Android 12 (API level 31), performance hint API. You can use the[Android provider](https://docs.unity3d.com/Packages/com.unity.adaptiveperformance.google.android@1.0/manual/index.html)from the Adaptive Performance 5.0.0 version. The thermal APIs are integrated with Adaptive Performance to help you retrieve device thermal information, and the performance hint API is called every`Update()`automatically without any additional work.

## Additional resources

Learn how[Android Adaptability](https://developer.android.com/games/optimize/adpf)and[Unity Adaptive Performance](https://docs.unity3d.com/Packages/com.unity.adaptiveperformance@5.0/manual/index.html)can help you stabilize your game's FPS and reduce thermal throttling.