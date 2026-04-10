---
title: https://developer.android.com/stories/games/new-state-mobile
url: https://developer.android.com/stories/games/new-state-mobile
source: md.txt
---

# NEW STATE Mobile reduces GPU usage by 22% with Android GPU Inspector

## Background

[NEW STATE Mobile](https://play.google.com/store/apps/details?id=com.pubg.newstate)is a battle royale game from Krafton that launched Nov 2021 worldwide, and reached 45M+ downloads in the first month of launch. KRAFTON, Inc. is a collective of independent game development studios brought together to create innovative and engaging entertainment experiences for gamers across the world. The company consists of PUBG Studios, Bluehole Studio, Striking Distance Studios, RisingWings, Dreamotion, and Unknown Worlds, each with its own unique expertise. NEW STATE Mobile was created with Unreal Engine 4, and various attempts have been made to reduce heat and battery consumption caused by high GPU usage from their distinctive gaming features.

Gamers can play long range battles, so the game engine needs to be able to render scenes from quite a distance. Also, numerous vegetations are present in the battleground, leading the overdraw of these vegetations to have a substantial impact on decreasing performance. This led the team to[Android GPU Inspector](http://developer.android.com/agi)(AGI) to help optimize the game's GPU usage and eliminate bottlenecks.

![Screenshot from NEW STATE Mobile](https://developer.android.com/static/images/cards/distribute/stories/newstate-mobile.jpg "Figure 1: Screenshot from NEW STATE Mobile")

**Figure 1**: Screenshot from NEW STATE Mobile

## What they did

NEW STATE Mobile used AGI to access loads of GPU counter information and optimize their GPU usage accordingly. They identified unnecessary render passes with the help of the GPU activity profiling data provided by AGI. After identifying which segments were taking up GPU usage and memory bandwidth, they continued to check the optimization progress using the GPU Counter and GPU activity back and forth to check if they were headed in the right direction.

![Screenshot from NEW STATE Mobile](https://developer.android.com/static/images/cards/distribute/stories/newstate-mobile-2.jpg "Figure 2: Screenshot from NEW STATE Mobile")

**Figure 2**: Screenshot from NEW STATE Mobile

Here are a few things they learned about the game's performance using AGI:

- **Base pass optimization**: Depth prepass, which is a technology that increases usage of Early-z, helped decrease the use of fragment shading. Depth prepass was specifically used for LOD0 which takes up most of the screen space, minimizing the burden that can come from additional draw calls. Also, using the 32-bit scenecolor format can increase the performance of the entire render pass. Default SceneColor format of UnrealEngine4 is FloatRGBA, which is 64-bit. If a 32-bit format is used, memory bandwidth can be reduced by half.

- **Impact measured**: After applying depth prepass, GPU utilization dropped by 7.5%. Due to the depth prepass, more Fragments could be Early-Z. The rate of time required for fragment shading has decreased by 2%. Through the 32-bit scenecolor format, GPU utilization was reduced by 5.3%. Shaders Busy decreased by 2%, and total GPU read from system memory decreased 330 MB/s. The amount the GPU writes to system memory was reduced by 78 MB/s and Texture memory read was also reduced by 43 MB/s.

- **Shadow pass optimization**: When meshes are used as shadow casters, using high polygon LOD does not really make a difference in quality. It is preferred to use low polygon LOD which helps reduce the number of triangles. In Unreal Engine 4, low polygon LOD can be used via the console command 'ForceLODShadow'.

- **Impact measured**: The number of triangles used for shadows decreased by about 120,000. The GPU counter data in AGI showed that GPU usage decreased about 2%, the amount of the GPU memory read from the system memory decreased 130MB/s, and the amount written from the GPU to the system memory decreased about 23MBs.

- **Auto-instancing**: Auto-instancing, which can be applied for both shadow pass and base pass optimization, allows you to merge the same render commands at runtime and then be rendered all at once. This allowed NEWSTATE mobile to apply global illumination to individual objects without losing performance. Auto-instancing is a basic feature provided by UnrealEngine4.

- **Impact measured**: Draw calls were reduced by 500. It reduced about 48% of the draw calls. GPU utilization decreased about 3.5%. These measurements were taken using OpenGL.

![Internal data showing GPU usage reduction](https://developer.android.com/static/images/cards/distribute/stories/newstate-data.jpg "Figure 3: Screenshot from NEW STATE Mobile")

**Figure 3**: Internal data showing GPU usage reduction

## Results

By using AGI, NEW STATE Mobile reduced its GPU usage by 22%. From depth prepass and shadow pass optimization, GPU usage was down by 19% and 3% respectively. Draw calls and the total memory read and written by GPU from system memory was also substantially reduced.

## Get started

Learn how to analyze the impact of your game on Android devices by identifying performance issues and areas to optimize with the[Android GPU Inspector](https://developer.android.com/agi)(AGI).