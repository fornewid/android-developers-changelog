---
title: https://developer.android.com/topic/performance/rendering
url: https://developer.android.com/topic/performance/rendering
source: md.txt
---

# Rendering

A key aspect of your app that influences your users' perception of quality is the smoothness with which it renders images and text to the screen. It's important to avoid jank and sluggish responsiveness when your app is drawing to the screen.

This section shows several ways to optimize your app's rendering performance: reducing overdraw, optimizing view hierarchies, and taking advantage of the Profile GPU tool. See[Jetpack Compose performance](https://developer.android.com/jetpack/compose/performance)to learn about rendering in Jetpack Compose.

## Render actions

**[Reduce overdraw](https://developer.android.com/topic/performance/rendering/overdraw)**
:   Minimize the number of times your app redraws the same pixel in a single frame.

**[Performance and view hierarchies](https://developer.android.com/topic/performance/rendering/optimizing-view-hierarchies)**
:   Make sure your layout and measurement are executing efficiently, and avoid double taxation.

**[Analyze with Profile GPU Rendering](https://developer.android.com/topic/performance/rendering/profile-gpu)**
:   Take advantage of this on-device tool to identify bottlenecks that might slow your app's rendering.