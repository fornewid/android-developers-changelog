---
title: https://developer.android.com/games/develop/custom/overview
url: https://developer.android.com/games/develop/custom/overview
source: md.txt
---

# About customizing or porting game engines

![Tools, stars, planet](https://developer.android.com/static/images/games/custom-game-engine.svg)If you're using C or C++ to develop or customize a game engine, the following requirements are critical to integrating Android support into your game engine.

- Take advantage of Android development tools
- Construct an activity
- Draw to the screen
- Process input events
- Output audio
- Manage memory
- Test and polish
- Publish to Google Play

The requirements described on this page do not teach you how to develop a game engine from scratch, but rather identify the areas where Android is relatively unique compared to other platforms.
| **Note:** If you're using Unity, Unreal, Defold or Godot, see[Game engines on Android](https://developer.android.com/games/engines/engines-overview)for resources on developing for Android using one of these game engines.

## Take advantage of Android development tools

[Android Studio](https://developer.android.com/games/develop/develop-as)includes tools you can use to:

- Configure your project
- Build, debug, and package your game
- Examine the performance of your game using system, CPU, and memory profilers
- Inspect the contents of your game's package or application bundle
- Integrate additional features of the Android SDK and NDK

[Android Graphics Inspector](https://developer.android.com/agi)can characterize the rendering performance of your game and help you investigate the details of rendered frames using frame profiling.

If you're primarily using Microsoft Visual Studio, you can use the[Android Game Development Extension](https://developer.android.com/games/agde)(AGDE) to add an Android target to existing projects. AGDE supports native debugging in Visual Studio and includes standalone versions of many of the Android Studio profiling tools.

## Construct an activity

Your game needs to construct and interact with an[`Activity`](https://developer.android.com/reference/android/app/Activity). Learn about the[Activity Lifecycle](https://developer.android.com/guide/components/activities/activity-lifecycle)on Android to understand when an Activity is created, started, resumed, paused, stopped, and destroyed.

Read about the[`GameActivity`](https://developer.android.com/games/agdk/game-activity)library, which integrates and meets the`Activity`-related needs (game window, lifecycle, rendering, handling events) of native C or C++ game engines.

## Draw to the screen

Your game needs to draw objects and sprites on the screen. Learn about the Android[`SurfaceView`](https://developer.android.com/reference/android/view/SurfaceView)and how to[configure graphics](https://developer.android.com/games/agdk/configure-graphics)in your game engine.

Android devices support different display refresh rates. Learn about[rendering in game loops](https://developer.android.com/games/develop/gameloops)to prevent frame drops and frame buffers glitches.

Read about how to[achieve frame pacing](https://developer.android.com/games/sdk/frame-pacing)for smooth rendering in OpenGL and Vulkan.[Optimize your frame rate](https://developer.android.com/games/sdk/performance-tuner)with Performance Tuner.

Use multisample anti-aliasing (MSAA) to improve the quality of your rendering. MSAA can be used with very little overhead. To learn more, see the blog post[Multisampled Anti-aliasing For Almost Free --- On Tile-Based Rendering Hardware](https://medium.com/androiddevelopers/multisampled-anti-aliasing-for-almost-free-on-tile-based-rendering-hardware-21794c479cb9).

## Process input events

A game engine receives input events from a variety of sources. For an immersive gaming experience, learn to support different Android input sources:

- [Touch](https://developer.android.com/games/agdk/add-touch-support)
- [Software keyboard](https://developer.android.com/games/agdk/add-support-for-text-input)
- [Game controllers](https://developer.android.com/games/sdk/game-controller)
- [Mouse](https://developer.android.com/games/sdk/game-controller/mouse)
- [Sensors](https://developer.android.com/guide/topics/sensors/sensors_overview)

## Output audio

Your game engine needs to output audio across different devices and Android versions. Learn about Oboe, our open-source C++ audio library to[incorporate high-performance audio](https://developer.android.com/games/sdk/oboe)in your game.

Use Oboe to achieve the lowest latency, avoid specific audio bugs, and auto select the best available native library (such as AAudio or OpenSL ES).

## Manage memory

On Android devices, the system tries to use as much system memory (RAM) as possible and performs various memory optimizations to free up space when needed. Learn to[manage memory usage](https://developer.android.com/games/optimize/memory-allocation)to avoid slowing down or exiting your game.

## Test and polish

An Android app crashes whenever there's an unexpected exit caused by an unhandled exception or signal. Learn about how to[detect and diagnose crashes](https://developer.android.com/games/optimize/crash), read stack traces, memory and networking exceptions, how to use logcat, and how to understand Java and Kotlin-specific errors.

## Publish to Google Play

Players download your game with various Android devices in different countries, network conditions, and data plans. Learn how to use Google Play to[deliver app bundles and asset packs](https://developer.android.com/guide/playcore/asset-delivery)for large games with the benefits of a content delivery network.