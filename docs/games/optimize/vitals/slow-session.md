---
title: https://developer.android.com/games/optimize/vitals/slow-session
url: https://developer.android.com/games/optimize/vitals/slow-session
source: md.txt
---

# Slow Sessions is a new Android vitals metric in Google Play console. A slow session is a session in which more than 25% of the frames are slow. A frame is slow if it is not presented less than 50ms after the previous frame (equivalent to 20 FPS). Android vitals also reports a second Slow Sessions metric with a target of 34ms (equivalent to 30FPS). Using Slow Sessions, you can understand the frame-rate performance of your game, which impacts how smooth and fluid your game feels to users.

In due course, Play will start steering users away from games that cannot achieve 20 FPS on their phones. Note that Android vitals only begins monitoring frame rate after your game has been running for one minute.

Visit our[Help Center](https://support.google.com/googleplay/android-developer/answer/9844486#slow_frames&zippy=%2Cslow-session-rate-fps-or-fps-games-only%2Cexcessive-slow-frames-apps-only)for more details about the metric.
![Pie chart-like graphics that show the number of slow frames and non-slow frames.](https://developer.android.com/static/topic/performance/vitals/images/slow-session.png)**Figure 1.**A slow session in Android vitals.**Note:** The Slow Sessions metric is computed with data collected from[SurfaceFlinger](https://source.android.com/docs/core/graphics/surfaceflinger-windowmanager#surfaceflinger). More concretely, the frame rate of a session is estimated based on the time in between frames drawn on surfaces owned by the app. The estimated frame rate includes frames rendered by OpenGL, Vulkan, as well as Android UI toolkit. This metric is available only for games. If your apps use the`View`-based UI toolkit, where the user-visible portion of the app is drawn from[`Canvas`](https://developer.android.com/reference/android/graphics/Canvas)or the`View`hierarchy, refer to[Slow Rendering](https://developer.android.com/games/optimize/vitals/render)

## How to measure FPS and detect slow frames

The Android`dumpsys surfaceflinger timestats`command provides average FPS and*present to present* timing histogram for all layers that are being rendered. The*present to present*time of a frame is the interval between the current frame and previous frame being drawn. Here are steps by steps to use the command to collect your game's FPS:

1. Run the command with the flags`enable`and`clear`to start capturing information:

       adb shell dumpsys SurfaceFlinger --timestats -clear -enable

2. When the game is played long enough, run the command again with flag`dump`to dump information:

       adb shell dumpsys SurfaceFlinger --timestats -dump

   The dumped information provides total frames and presentToPresent histogram for all layers rendered by[SurfaceFlinger](https://source.android.com/docs/core/graphics/surfaceflinger-windowmanager#surfaceflinger).**You must find the section of your game by filtering based on`layerName`**:  

       layerName = SurfaceView[com.google.test/com.devrel.MainActivity]@0(BLAST)#132833

   Slow frame rate of the session could be calculated based on the information of each layer.

   For example, 20 FPS slow frame percentage = (sum of values from 54 ms to 1000 ms) / totalFrames x 100  

       totalFrames = 274
       ...
       presentToPresent histogram is as below:
       0ms=0 1ms=0 2ms=0 3ms=0 4ms=0 5ms=0 6ms=0 7ms=0 8ms=0 9ms=0 10ms=0 11ms=0 12ms=0
       13ms=0 14ms=0 15ms=0 16ms=1 17ms=0 18ms=0 19ms=0 20ms=0 21ms=0 22ms=0 23ms=0
       24ms=0 25ms=0 26ms=0 27ms=0 28ms=0 29ms=0 30ms=0 31ms=0 32ms=0 33ms=269 34ms=0
       36ms=0 38ms=0 40ms=0 42ms=0 44ms=0 46ms=0 48ms=0 50ms=1 54ms=0 58ms=0 62ms=0
       66ms=0 70ms=1 74ms=0 78ms=0 82ms=0 86ms=0 90ms=0 94ms=0 98ms=0 102ms=0 106ms=0
       110ms=0 114ms=0 118ms=0 122ms=0 126ms=0 130ms=0 134ms=0 138ms=0 142ms=0 146ms=0
       150ms=0 200ms=0 250ms=0 300ms=0 350ms=0 400ms=0 450ms=0 500ms=0 550ms=0 600ms=0
       650ms=0 700ms=0 750ms=0 800ms=0 850ms=0 900ms=0 950ms=0 1000ms=0

   Average FPS of each layer is also shown in the dump:  

       ...
       averageFPS = 30.179
       ...

3. After collecting all the information, you should disable the timestats by using flag`disable`:

       adb shell dumpsys SurfaceFlinger --timestats -disable

## Slow frame causes and solutions

There are many reasons a frame might present or render longer on the screen than the developer's target. The game could be**CPU/GPU bound** . Or the device is**overheating and activates a throttled thermal state** . Or there's**a mismatch in the game's framerate and the device's display refresh rate**.

Use[Android Frame Pacing (Swappy)](https://developer.android.com/games/optimize/vitals/slow-session#what_is_swappy),[Vulkan](https://developer.android.com/games/optimize/vitals/slow-session#what_is_vulkan), and[ADPF](https://developer.android.com/games/optimize/vitals/slow-session#what_is_adpf)to address these issues and improve your game's performance.

## What is Swappy

The Android[Frame Pacing library](https://developer.android.com/games/sdk/frame-pacing), also known as Swappy, is part of the[AGDK libraries](https://developer.android.com/games/agdk#game-libraries). Swappy helps OpenGL and Vulkan games achieve smooth rendering and correct frame pacing on Android.

Frame pacing is the synchronization of a game's logic and rendering loop with an OS's display subsystem and the underlying display hardware. The Android display subsystem was designed to avoid visual artifacts (known as tearing) that can occur when the display hardware switches to a new frame partway through an update. To avoid these artifacts, the display subsystem does the following:

- Buffers past frames internally
- Detects late frame submissions
- Repeats the display of past frames when late frames are detected

Learn how[Mir 2 used Swappy to reduce their slow session rate from 40% to 10%](https://developer.android.com/stories/games/swappy).

#### How to use Swappy in native projects

See the following guides to integrate the Android Frame Pacing library into your game:

- [Integrate Android Frame Pacing into your OpenGL renderer](https://developer.android.com/games/sdk/frame-pacing/opengl)
- [Integrate Android Frame Pacing into your Vulkan renderer](https://developer.android.com/games/sdk/frame-pacing/vulkan)

### How to use Swappy in Unity game engine

Unity has integrated Android Frame Pacing into their engine. To enable this feature in[Unity 2019.2](https://unity.com/kr/releases/editor/alpha/2019.2.0a6)or higher, check the Optimized Frame Pacing checkbox under*Project Settings \> Player \> Settings* for*Android \> Resolution and Presentation*:
![Project settings dialog.](https://developer.android.com/static/topic/performance/vitals/images/unity-frame-pacing.png)**Figure 2.**Enable Frame Pacing in Unity Engine.

Alternatively, programmatically enable[Optimized Frame Pacing option](https://docs.unity3d.com/ScriptReference/PlayerSettings.Android-optimizedFramePacing.html)in your logic code to allow Unity to evenly distribute frames for less variance in frame rate, creating smoother gameplay.

### How to use Swappy in Unreal game engine

Unreal 4.25 and higher integrate the[Android Frame Pacing Library](https://developer.android.com/games/sdk/frame-pacing), which is part of the[Android Game Development Kit](https://developer.android.com/games/agdk). The[Mobile Frame Pacing](https://docs.unrealengine.com/SharingAndReleasing/Mobile/Rendering/MobileFramePacing/)article explains how to enable the Android Frame Pacing Library and how to control frame pacing from C++ code.

## What is Vulkan

[Vulkan](https://www.vulkan.org/)is a modern cross-platform 3D graphics API designed to minimize abstraction between device graphics hardware and your game. Vulkan is the primary low-level graphics API on Android, replacing[OpenGL ES](https://www.khronos.org/opengles/). OpenGL ES is still supported on Android, but is no longer under active feature development.

Vulkan offers the following advantages over OpenGL ES:

- A more efficient architecture with lower CPU overhead in the graphics driver
- New optimization strategies to improve CPU performance
- New graphics features not available in OpenGL ES, such as bindless APIs and ray tracing

### How to use Vulkan in native Android projects

The[Getting started with Vulkan on Android](https://developer.android.com/codelabs/beginning-vulkan-on-android)codelab guides you through setting up your Vulkan rendering pipeline and then rendering a textured, rotating triangle on the screen. Use the codelab to learn how to render your game graphics.

### How to use Vulkan in Unity game engine

To enable automatic device selection on Unity, follow the steps to configure[Auto Graphics API](https://developer.android.com/games/engines/unity/start-in-unity#auto_graphics_api).
![Project settings dialog.](https://developer.android.com/static/topic/performance/vitals/images/unity-vulkan.png)**Figure 3.**Enable Unity Auto Graphics API.

Alternatively, you can enable Vulkan manually by disabling*Auto Graphics API* , and put Vulkan in the highest priority in the*Graphics APIs*list. If you're using Unity 2021.1 or a previous version, this is the only way to use Vulkan.
![Project settings dialog.](https://developer.android.com/static/topic/performance/vitals/images/unity-vulkan-2.png)**Figure 4.**Manually choose Vulkan as main Graphics API in Unity.

Use the[VkQuality Unity engine plugin](https://developer.android.com/games/engines/unity/unity-vkquality)to provide launch-time recommendations of the graphics API for your game to use on specific devices.

### How to use Vulkan in Unreal game engine

To enable the Vulkan graphics API, navigate to*Project Settings \> Platforms \> Android \> Build* and select*Support Vulkan* . When you select both*Support Vulkan* and*Support OpenGL ES3.2*, Unreal uses Vulkan by default. If the device doesn't support Vulkan, Unreal falls back to OpenGL ES 3.2.
![Project settings dialog.](https://developer.android.com/static/topic/performance/vitals/images/unreal-vulkan.png)**Figure 5.**Enable Vulkan in Unreal Engine.

If you are using specific Vulkan features that are known to behave badly on certain devices, you can customize your`BaseDeviceProfile.ini`file to exclude those devices. Check out[Customizing Device Profiles and Scalability for Android](https://dev.epicgames.com/documentation/en-us/unreal-engine/customizing-device-profiles-and-scalability-in-unreal-engine-projects-for-android#androiddeviceprofiles)to learn how to customize`BaseDeviceProfile.ini`. As new device drivers might fix previously known bad devices, keep your*BaseDeviceProfile.ini*file updated to get all the optimizations.

## What is ADPF

The[Android Dynamic Performance Framework (ADPF)](https://developer.android.com/games/optimize/adpf)optimizes games based on the dynamic thermal, CPU, and GPU management features on Android. The focus is on games, but you can also use the features for other performance-intensive apps.

ADPF is a set of APIs that allow games and performance-intensive apps to interact more directly with power and thermal systems of Android devices. With these APIs, you can monitor the dynamic behavior on Android systems and optimize game performance at a sustainable level that doesn't overheat devices.

Here are the main ADPF features:

- [Thermal API](https://developer.android.com/games/optimize/adpf/thermal): Monitor the thermal state of a device so that the application can proactively adjust workload before it becomes unsustainable.
- [CPU Performance Hint API](https://developer.android.com/games/optimize/adpf/performance-hint-api): Provide performance hints that let Android choose the right performance settings (for example, CPU operating point or core) for the workload.
- [Game Mode API and Game State API](https://developer.android.com/games/optimize/adpf/gamemode/about-API-and-interventions): Enable game play optimization by prioritizing performance or battery life characteristics, based on user's settings and game specific configurations.
- [Fixed Performance Mode](https://developer.android.com/games/optimize/adpf/fixed-performance-mode): Enable fixed-performance mode on a device during benchmarking to get measurements that aren't altered by dynamic CPU clocking.
- [Power Efficiency Mode](https://developer.android.com/reference/android/os/PerformanceHintManager.Session#setPreferPowerEfficiency(boolean)): Tells the session that the threads in Performance Hint Session can be safely scheduled to prefer power efficiency over performance. Available in Android 15 (API leve 35).

### How to use ADPF in native Android projects

The[Integrating Adaptability Features Into Your Native Game](https://developer.android.com/adaptability-codelab)codelab guides you to integrate ADPF features into your game with steps that you can follow at your own pace. At the end of the codelab, you will have integrated the following features:

- [Thermal API](https://developer.android.com/games/optimize/adpf#thermal): Listen to device thermal condition and react before the device falls into thermal throttling state.
- [Game Mode API](https://developer.android.com/games/optimize/adpf/gamemode/about-API-and-interventions): Understand player optimization preferences (maximize performance or preserve battery) and adjust accordingly.
- [Game State API](https://developer.android.com/reference/android/app/GameState): Let the system know the state of your game (loading, playing, UI, etc.), and the system can adjust resources accordingly (boost I/O, or CPU, GPU, etc.).
- [Performance Hint API](https://developer.android.com/reference/android/os/PerformanceHintManager): Let the system know your threading model and workload so that the system can allocate resources accordingly.

### How to use ADPF in Unity game engine

[Unity's Adaptive Performance](https://docs.unity3d.com/Packages/com.unity.adaptiveperformance@5.0/manual/installing-and-configuring.html)is a tool for game developers looking to optimize their games on mobile devices, particularly for the diverse Android ecosystem. Adaptive Performance enables your game to adapt to the device's performance and thermal characteristics in real-time, ensuring a smooth and efficient gaming experience.

[Adaptive Performance Android provider](https://docs.unity3d.com/Packages/com.unity.adaptiveperformance.google.android@1.2/manual/index.html)guides you through the steps to implement ADPF in Unity.
![Project settings dialog.](https://developer.android.com/static/topic/performance/vitals/images/unity-adpf.png)**Figure 6.**Integrate ADPF in Unity Engine.

### How to use ADPF in Unreal game engine

![Project settings dialog.](https://developer.android.com/static/topic/performance/vitals/images/unreal-adpf.png)**Figure 7.**Integrate ADPF in Unreal Engine.

1. Download the[plugin](https://github.com/android/adpf-unreal-plugin)
2. Copy the plugin into the project plugin folder
3. Enable the ADPF Unreal Engine plugin in the Unreal editor
4. Relaunch Unreal editor
5. [Build and cook](https://dev.epicgames.com/documentation/en-us/unreal-engine/cooking-content-in-unreal-engine?application_version=5.0)the game

The[Android Dynamic Performance Framework](https://developer.android.com/games/optimize/adpf)(ADPF) plugin for[Unreal Engine](https://www.unrealengine.com/en-US)provides stable performance and prevents thermal throttling.[Download the plugin](https://github.com/android/adpf-unreal-plugin)from GitHub. This plugin changes features by setting[Unreal console values](https://docs.unrealengine.com/4.26/en-US/ProductionPipelines/DevelopmentSetup/Tools/ConsoleManager/).