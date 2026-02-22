---
title: https://developer.android.com/games/agdk/overview
url: https://developer.android.com/games/agdk/overview
source: md.txt
---

# Android Game Development Kit

![](https://developer.android.com/static/images/logos/agdk.svg)

The Android Game Development Kit (AGDK) is a set of tools and libraries that help you develop and optimize Android games while integrating with existing game development platforms and workflows.

## Use, develop, or extend game engines

AGDK provides tools and libraries for adding Android support when you[create or extend](https://developer.android.com/games/develop/custom/overview)a game engine. It also provides plugins and integration that supports Android development on many[existing game engines](https://developer.android.com/games/engines/engines-overview).

## Develop in Visual Studio

You can build Android games in Visual Studio on Windows by using the[Android Game Development Extension](https://developer.android.com/games/agde)for Visual Studio (AGDE). AGDE is a Visual Studio extension that allows you to use your existing Visual Studio projects to build Android games.

## Libraries

The AGDK libraries allow you to develop and optimize your game in C or C++ while accessing Android app development libraries and services.

### Frame Pacing

Helps games deliver frames at a consistent pace, and adjusts the pace based on the performance.  
[**Reference**](https://developer.android.com/games/sdk/reference/frame-pacing)[**User Guide**](https://developer.android.com/games/sdk/frame-pacing)

### Game Activity

Supports game development in C or C++ with access to Android Jetpack and dependent services.  
[**Reference**](https://developer.android.com/reference/games/game-activity)[**User Guide**](https://developer.android.com/games/agdk/game-activity)

### Game Controller

Manages game controllers by accessing connections, features, device information, and input data.  
[**Reference**](https://developer.android.com/reference/games/game-controller)[**User Guide**](https://developer.android.com/games/sdk/game-controller)

### Game Text Input

Displays and hides the soft keyboard, and manages text updates.  
[**Reference**](https://developer.android.com/reference/games/game-text-input)[**User Guide**](https://developer.android.com/games/agdk/add-support-for-text-input)

### Memory Advice API (Beta)

Helps Android apps stay within safety limits for memory use by estimating memory use and notifying apps if thresholds are exceeded.  
[**Reference**](https://developer.android.com/reference/games/memory-advice/group/memory-advice)[**User Guide**](https://developer.android.com/games/sdk/memory-advice/overview)

### Oboe High-performance audio

Reduces audio latency, while avoiding device and platform audio issues.  
[**Reference**](https://google.github.io/oboe/namespaceoboe.html)[**User Guide**](https://developer.android.com/games/sdk/oboe)

### Android Performance Tuner

Identifies performance issues related to quality settings, scenes, load times, and device models.  
[**Reference**](https://developer.android.com/games/sdk/reference/performance-tuner/custom-engine)[**User Guide**](https://developer.android.com/games/sdk/performance-tuner)

### Android Performance Tuner Unity plugin

Integrates Android Performance Tuner with Unity.  
[**Reference**](https://developer.android.com/games/sdk/reference/performance-tuner/unity)[**User Guide**](https://developer.android.com/games/sdk/performance-tuner/unity)

## Optimization

In addition to[Android Performance Tuner](https://developer.android.com/games/sdk/performance-tuner), AGDK includes the[Android GPU Inspector](https://developer.android.com/agi)(AGI), which is a tool that provides advanced GPU and system profiling for graphic intensive games.

For a complete list of Android game optimization tools and best practices, see the[optimization overview](https://developer.android.com/games/optimize/overview).

## Adaptability

Adaptability is a new pillar of the AGDK focused on helping your game understand, respond to, and influence changes in the devices thermal and performance state.

### CPU performance hints

Enables your game to influence dynamic CPU performance behavior without overheating the device and wasting power.

[**User Guide**](https://developer.android.com/games/optimize/adpf#cpu-hints)

### Thermal-state monitoring

Achieve performance goals by understanding the thermal state and limitations of a device.

[**User Guide**](https://developer.android.com/games/optimize/adpf#thermal)

### Game Mode

Optimize gameplay by prioritizing characteristics, such as performance or battery life, based on user preferences.

[**User Guide**](https://developer.android.com/games/gamemode/about-API-and-interventions)

### Game Manager API

Update the game mode of your app, enabling Android OS to adjust to meet your performance needs.

[**Reference**](https://developer.android.com/reference/android/app/GameManager)