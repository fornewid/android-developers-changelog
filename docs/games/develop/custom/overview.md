---
title: About customizing or porting game engines  |  Android game development  |  Android Developers
url: https://developer.android.com/games/develop/custom/overview
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Games dev center](https://developer.android.com/games)
* [Guides](https://developer.android.com/games/guides)

Send feedback

# About customizing or porting game engines Stay organized with collections Save and categorize content based on your preferences.




![Tools, stars, planet](/static/images/games/custom-game-engine.svg)
If you're using C or C++ to develop or customize a game engine, the following
requirements are critical to integrating Android support into your game engine.

* Take advantage of Android development tools
* Construct an activity
* Draw to the screen
* Process input events
* Output audio
* Manage memory
* Test and polish
* Publish to Google Play

The requirements described on this page do not teach you how to develop a game
engine from scratch, but rather identify the areas where Android is relatively
unique compared to other platforms.

**Note:** If you're using Unity, Unreal, Defold or Godot, see [Game engines on
Android](/games/engines/engines-overview) for resources on developing for
Android using one of these game engines.

## Take advantage of Android development tools

[Android Studio](/games/develop/develop-as) includes tools you can use to:

* Configure your project
* Build, debug, and package your game
* Examine the performance of your game using system, CPU, and memory profilers
* Inspect the contents of your game’s package or application bundle
* Integrate additional features of the Android SDK and NDK

[Android Graphics Inspector](/agi) can characterize the rendering performance
of your game and help you investigate the details of rendered frames using frame
profiling.

If you're primarily using Microsoft Visual Studio, you can use
the [Android Game Development Extension](/games/agde) (AGDE) to add an Android
target to existing projects. AGDE supports native debugging in Visual Studio and
includes standalone versions of many of the Android Studio profiling tools.

## Construct an activity

Your game needs to construct and interact with an
[`Activity`](/reference/android/app/Activity). Learn about the
[Activity Lifecycle](/guide/components/activities/activity-lifecycle)
on Android to understand when an Activity is created, started, resumed, paused,
stopped, and destroyed.

Read about the [`GameActivity`](/games/agdk/game-activity) library,
which integrates and meets the `Activity`-related needs (game window,
lifecycle, rendering, handling events) of native C or C++ game engines.

## Draw to the screen

Your game needs to draw objects and sprites on the screen. Learn about the
Android [`SurfaceView`](/reference/android/view/SurfaceView) and how
to [configure graphics](/games/agdk/configure-graphics) in your game engine.

Android devices support different display refresh rates. Learn about
[rendering in game loops](/games/develop/gameloops) to prevent frame drops and
frame buffers glitches.

Read about how to [achieve frame pacing](/games/sdk/frame-pacing) for smooth
rendering in OpenGL and Vulkan.
[Optimize your frame rate](/games/sdk/performance-tuner) with Performance Tuner.

Use multisample anti-aliasing (MSAA) to improve the quality of your rendering.
MSAA can be used with very little overhead. To learn more, see the blog post
[Multisampled Anti-aliasing For Almost Free — On Tile-Based Rendering Hardware](https://medium.com/androiddevelopers/multisampled-anti-aliasing-for-almost-free-on-tile-based-rendering-hardware-21794c479cb9).

## Process input events

A game engine receives input events from a variety of sources. For an
immersive gaming experience, learn to support different Android input sources:

* [Touch](/games/agdk/add-touch-support)
* [Software keyboard](/games/agdk/add-support-for-text-input)
* [Game controllers](/games/sdk/game-controller)
* [Mouse](/games/sdk/game-controller/mouse)
* [Sensors](/guide/topics/sensors/sensors_overview)

## Output audio

Your game engine needs to output audio across different devices and Android
versions. Learn about Oboe, our open-source C++ audio library to
[incorporate high-performance audio](/games/sdk/oboe) in your game.

Use Oboe to achieve the lowest latency, avoid specific audio bugs, and auto
select the best available native library (such as AAudio or OpenSL ES).

## Manage memory

On Android devices, the system tries to use as much system memory (RAM) as
possible and performs various memory optimizations to free up space when needed.
Learn to [manage memory usage](/games/optimize/memory-allocation) to avoid
slowing down or exiting your game.

## Test and polish

An Android app crashes whenever there’s an unexpected exit caused by an
unhandled exception or signal. Learn about how to
[detect and diagnose crashes](/games/optimize/crash), read stack traces,
memory and networking exceptions, how to use logcat, and how to understand
Java and Kotlin-specific errors.

## Publish to Google Play

Players download your game with various Android devices in different countries,
network conditions, and data plans. Learn how to use Google Play to
[deliver app bundles and asset packs](/guide/playcore/asset-delivery)
for large games with the benefits of a content delivery network.






Send feedback