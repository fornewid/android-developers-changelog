---
title: https://developer.android.com/android-performance-analyzer/case-study/netmarble-perf-analyzer
url: https://developer.android.com/android-performance-analyzer/case-study/netmarble-perf-analyzer
source: md.txt
---

As the graphics processing capabilities of mobile devices advance rapidly,
today's mobile games offer console-level expansive worlds and sophisticated
visuals. However, extracting maximum performance across diverse GPU
architectures and device environments while optimizing power consumption remains
one of the most daunting challenges for Android game developers.

To solve these developer pain points, Google provides Android Performance
Analyzer, a GPU performance analysis tool that is available as a beta
release.

## What is the Android Performance Analyzer?

Android Performance Analyzer is a performance analysis tool. Built to handle
complex [Perfetto](https://perfetto.dev/docs/) traces efficiently, it provides game developers with deep,
actionable visibility into rendering pipelines and GPU workloads. Key
capabilities include:

- **Visual screenshot scrubbing:** Rapidly navigate through trace frames visually on the timeline to locate specific rendering events or frame drops.
- **Custom Perfetto SQL queries:** Extract tailored performance metrics (such as ratios, minimum or maximum values) specific to your game's unique architecture without manual data parsing.
- **Side-by-side A/B testing:** Compare multiple traces directly within the IDE using side-by-side tabs to seamlessly validate optimization efforts.
- **Vulkan CPU timing layer integration:** Gain granular insights into CPU execution time of [Vulkan](https://developer.android.com/games/develop/vulkan/overview) API calls.
- **In-depth GPU workload profiling:** Conduct sophisticated analysis of GPU loads through a broad range of hardware-level render stage timings and counters for precise performance tuning.

## Partner case study: Optimizing 'Seven Deadly Sins: Origin'

The Games DevRel team closely collaborated with **Netmarble** . Netmarble
integrated Android Performance Analyzer into the optimization process for their
game, **[The Seven Deadly Sins: Origin](https://play.google.com/store/apps/details?id=com.netmarble.nanaori)**, which launched on March
24, 2026.
![](https://developer.android.com/static/images/cards/distribute/stories/netmarble_apa_game_scene1.png) Netmarble: Seven Deadly Sins: Origin #1 ![](https://developer.android.com/static/images/cards/distribute/stories/netmarble_apa_game_scene2.png) Netmarble: Seven Deadly Sins: Origin #2

The Seven Deadly Sins: Origin is an open-world RPG that brings the anime IP to
life with high-fidelity visuals and seamless exploration. To
maintain its industry-leading graphics on mobile, Netmarble used the Android
Performance Analyzer to analyze and resolve GPU bottlenecks. By optimizing
complex rendering tasks and thermal efficiency, they delivered a high quality
experience that remains fluid and stable for players worldwide.

Using Android Performance Analyzer, Netmarble verified and validated
performance changes across the following key optimization scenarios:

### Before and after 'Disable world rendering in the UI scenes'

Finding the exact moment a frame drop occurs within massive trace logs is
difficult. The team used Android Performance Analyzer's **visual screenshot
scrubbing** functionality to rapidly navigate and verify
exactly when the 'Disable world rendering in the UI Scenes' logic was applied,
allowing them to instantly observe the resulting performance changes visually
and through data.
![](https://developer.android.com/static/images/cards/distribute/stories/netmarble_apa_ui_scene1.gif) Netmarble: ui scene #1

Android Performance Analyzer's screenshot feature makes it straightforward to
identify which specific scene corresponds to the collected traces and data.
While the screenshot resolution is kept low for efficiency, it is more than
sufficient to distinguish between different environments---such as a complex
village scene versus a UI scene.
![](https://developer.android.com/static/images/cards/distribute/stories/netmarble_apa_ui_scene2.png) Netmarble: ui scene #2

Using this feature, they discovered a critical anomaly: **GPU utilization in
simple UI scenes was nearly identical to that of high-complexity scenes.** This
insight
revealed that the game world was still being rendered behind the UI, causing
significant and unnecessary GPU overhead. As shown in the following image, once
world rendering was disabled for UI screens, all GPU hardware counters showed a
significant and immediate decrease.

### Before and after "Early Z"

Every game requires different metrics to monitor. By using **generic
Perfetto SQL queries** , the team constructed custom performance data to rapidly
identify bottleneck areas. This data-oriented approach allowed them to clearly
validate the efficiency and performance gains of implementing the [Early Z](https://developer.android.com/games/optimize/optimization-tips#early-z-acceleration)
pass.
![](https://developer.android.com/static/images/cards/distribute/stories/netmarble_apa_early_z_1.png) Netmarble: early-Z #1 ![](https://developer.android.com/static/images/cards/distribute/stories/netmarble_apa_early_z_2.png) Netmarble: early-Z #2

### Before and after for the shader precision change

Android Performance Analyzer allows quick access to multiple trace files and
provides an environment to compare them by opening them in **side-by-side
tabs** . Netmarble heavily used this feature to conduct detailed comparative
analyses on the GPU load and rendering times before and after adjusting [shader
precision](https://developer.android.com/games/optimize/optimization-tips#optimize-shader-precision).

*The following images show screens comparing shader precision change.*
![](https://developer.android.com/static/images/cards/distribute/stories/netmarble_apa_shader_precision_1.png) Netmarble: shader precision #1 ![](https://developer.android.com/static/images/cards/distribute/stories/netmarble_apa_shader_precision_2.png) Netmarble: shader precision #2

### Before and after using upscaling

Using the same side-by-side comparison tabs, Netmarble clearly validated pre-
and post-optimization performance changes for their upscaling implementation. By
synthesizing FPS analysis, specific GPU counters, and event data obtained
through the **Vulkan CPU timing layer**, they measured the exact performance
benefits and overhead of using upscaling across different scenes.
![](https://developer.android.com/static/images/cards/distribute/stories/netmarble_apa_upscaling_1.png) Netmarble: upscaling #1 ![](https://developer.android.com/static/images/cards/distribute/stories/netmarble_apa_upscaling_2.png) Netmarble: upscaling #2

### Broad GPU compatibility and stability

To address the diverse hardware fragmentation of the Android ecosystem, Android
Performance Analyzer supports all major GPU vendors. Using Android
Performance Analyzer's device connection
stability, Netmarble performed cross-validation across various GPU chipsets
across a wide range of Android devices.

## Get started

Android Performance Analyzer has transformed the complex GPU profiling process
into a highly visual and data-driven experience. As demonstrated by Netmarble's
game 'Seven Deadly Sins: Origin', Android Performance Analyzer can help
your game achieve peak performance on target devices.

Experience the Android Performance Analyzer Beta today. For detailed
installation instructions and a deeper dive key features, check out the official
[Android Developer documentation](https://developer.android.com/android-performance-analyzer).