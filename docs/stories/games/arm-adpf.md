---
title: https://developer.android.com/stories/games/arm-adpf
url: https://developer.android.com/stories/games/arm-adpf
source: md.txt
---

# Getting started with Android Dynamic Performance Framework (ADPF) in Unreal Engine

Android Dynamic Performance Framework (ADPF) is a powerful tool from Google for developers who want to optimize the performance of their applications. Through its thermal APIs, ADPF provides real-time information about the thermal state of the device, which is then used to adjust graphics settings in the application.

For research purposes, Arm developed a demo using Unreal Engine and ADPF to investigate how ADPF is used to optimize game performance.

ADPF monitors the thermal status, with the graphics qualities being adjusted in the game engine accordingly.

Keeping developers in mind, the objective is to allow users to play the game for longer without affecting the gameplay experience and the device consuming too much power.

## Before you begin

Before looking at the demo in more detail, it is important to highlight the[official Google documentation on ADPF](https://developer.android.com/games/optimize/adpf). This documentation is an invaluable resource which provides in-depth insights and guidance on how to use ADPF.

However, for those who prefer customizable learning, the ADPF sample repository contains practical examples of implementing ADPF in Android applications.

## Graphics settings adjustment

In the context of Unreal Engine, we can adjust graphics settings dynamically to maintain performance.

We used the Thermal State monitor and Thermal Headroom API in ADPF to monitor thermal throttling. You can then adjust quality settings, such as shadow quality, reflection quality and texture quality, as the device starts to throttle.

The following Graphics Quality settings in Unreal Engine are used to modify various settings:

- ViewDistanceQuality
- ShadowQuality
- GlobalIlluminationQuality
- ReflectionQuality
- AntiAliasingQuality
- TextureQuality
- VisualEffectQuality
- PostProcessingQuality
- FoliageQuality
- ShadingQuality
- OverallScalabilityLevel

## Real-world testing

![](https://developer.android.com/static/images/cards/distribute/stories/arm-gif1.gif)![](https://developer.android.com/static/images/cards/distribute/stories/arm-gif2.gif)

Arm creates our own demo games, which are used to research mobile graphics and game technologies. This year, we have tested ADPF on one of them, the SteelArms demo.

SteelArms has different levels of graphics intensities and a substantial CPU workload. It is built to be like modern mobile games, so we can model the game behavior on today's mobile phones. It also allows us to test how different technologies might work in a game on Arm-based mobile devices.

### Results

![](https://developer.android.com/static/images/cards/distribute/stories/arm-figure1-1.jpg)![](https://developer.android.com/static/images/cards/distribute/stories/arm-figure1-2.jpg)**Figure 1:**SteelArms full screen comparison with and without ADPF.

The previous images show a difference between the best (Cinematic) quality and lowest (Low) quality when ADPF is activated to adjust graphics settings. This change is gradual and not noticeable by users during gameplay.
![](https://developer.android.com/static/images/cards/distribute/stories/arm-figure2.png)**Figure 2:**Game with ADPF integration: split screen.

A split screen view of the highest graphics settings on the left (Blue Robot) side, and lowest graphics settings on the right (Red Robot) side.
![](https://developer.android.com/static/images/cards/distribute/stories/arm-figure3.png)**Figure 3:**Game with ADPF Integration: side-by-side details comparison.![](https://developer.android.com/static/images/cards/distribute/stories/arm-figure4.png)**Figure 4:**Game with ADPF Integration: side by side.

In the previous figures 3 and 4, the same view of the robot can be seen side by side. If a closer look is taken, the graphics settings adjusted by using ADPF is seen. Notice the floor of the ring, the shoulder of the robot, the ropes of the ring and the crowd? All of them seem to be at a slightly lower quality, which was done by using ADPF.

When throttling was imminent, these effects were scaled down in the SteelArms demo. It is hard to spot these small reductions in post processing and visual effects. Also, users will generally not notice them when playing. This means you can maintain most of the visual experience for the game without a hit to the gameplay experience. You can do all this while maintaining the power performance of your game and the battery life of your device.

As mentioned earlier, for demonstration purposes, we are comparing the highest with the lowest quality settings images. This is why the difference can still be seen when looked at carefully. However, when downscaled during gameplay, it is hardly noticeable to the user, while maintaining a stable gameplay experience.

### Results

![](https://developer.android.com/static/images/cards/distribute/stories/arm-figure5-1.png)![](https://developer.android.com/static/images/cards/distribute/stories/arm-figure5-2.png)![](https://developer.android.com/static/images/cards/distribute/stories/arm-figure5-3.png)![](https://developer.android.com/static/images/cards/distribute/stories/arm-figure5-4.png)**Figure 5:**Comparisons of FPS, Device Temperature, Thermal State \& Headroom when ADPF is enabled/disabled \~57% improvement in frame rates

The device avoids overheating and keeps within 1.0 thermal headroom.

## Power Consumption

![](https://developer.android.com/static/images/cards/distribute/stories/arm-figure6.png)**Figure 6:**Comparison of Power Consumption with ADPF enabled/disabled

## ADPF results

The results from ADPF being off and on can be seen in the figures shown previously. Showing that there is a difference in the frame rate of the game, and power consumption of the cores. Up to a 57% improvement in the frame rate is seen when ADPF is on. When ADPF is off, the GPU draws a significant amount of power. The big CPU core then has power spikes that are consistent with the GPU workload. As it is catching up with the amount of processing that it is being asked to do. In comparison, when ADPF is on, the big CPU core responds to throttling and brings down the overall power consumption of all cores in the device.

## Conclusion

ADPF can significantly improve the power consumption of games. This ultimately means longer playtime for gamers, with improved battery life and lower temperature for the device being used. From a developer perspective, ADPF maintains the correct frame rate of the game. While giving them the flexibility to scale down quality settings and still providing the user with a great gameplay experience.

Newer and older devices can benefit from using ADPF. It allows games to run to a high standard on previous generations of devices without additional optimization work.