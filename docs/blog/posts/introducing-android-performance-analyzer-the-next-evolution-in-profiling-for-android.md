---
title: https://developer.android.com/blog/posts/introducing-android-performance-analyzer-the-next-evolution-in-profiling-for-android
url: https://developer.android.com/blog/posts/introducing-android-performance-analyzer-the-next-evolution-in-profiling-for-android
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Introducing Android Performance Analyzer - The Next Evolution in Profiling for Android

5 min read ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo_Strapi_2000x1000_5793c01e36_ZVoYvg.webp) 19 May 2026 [![View Mayank Jain's profile](https://developer.android.com/static/blog/assets/unnamed_2_feee4f83eb_13HwUT.webp)](https://developer.android.com/blog/authors/blog-author) [Mayank Jain](https://developer.android.com/blog/authors/blog-author) Product Manager

### What is Android Performance Analyzer?

**Android Performance Analyzer (APA)** is Android's new profiler and performance analysis tool for the Android mobile ecosystem.

APA is intended as a profiling tool for any developer building for Android who needs to make their app or game run better and faster. It is helpful for all performance-minded engineers, especially those using Vulkan in their game engines who want to squeeze every bit of performance out of their code.

APA aims to be the tool that helps you optimize apps and games for all modern Android devices and simplifies your most common workflows, with a simple interface that anyone on your team can quickly learn and be productive.

Available today in **open beta**is APA's new System Profiler that you can use to analyze the CPU, GPU, Memory, and power usage of your app or game - and see how it interacts with system behavior.
[Video](https://www.youtube.com/watch?v=peplbYt0Ohg)

Developed in collaboration with Samsung Austin Research Center (SARC) and LunarG, APA relies on [Perfetto](https://perfetto.dev/)for system tracing and its upcoming frame profiling/debugging features (stay tuned!) are powered by LunarG's GFXReconstruct technology for graphics capture and replay.

Devices running Android 12+ will provide the best experience for capturing system-wide performance and GPU counters and render stages.

We're also working across the Android ecosystem with our esteemed industry partners to bring more profiling \& optimization related data into APA.
![01-apa-hero.png](https://developer.android.com/static/blog/assets/01_apa_hero_c03f05cb0d_Su8od.webp)

### How to get Android Performance Analyzer

APA ships in two different forms, and you can download whichever one suits your needs best

- As a [lightweight standalone desktop app](https://developer.android.com/android-performance-analyzer).
- And also integrated directly into Android Studio as the updated System Trace viewer (available in [Panda 4 canary builds](https://developer.android.com/studio/preview) and later).

The standalone desktop app is intended to be used without an Android Studio project or Gradle build - and provides deep customization of recording configuration, built-in Vulkan layers for graphics analysis, deep inspection of GPU counters and much more.

APA is also cross-platform: works natively on Windows, MacOS, and Linux.

## Features in this release

### Basic profiling functionality

**Capturing your profile data**

You don't always want to take a capture immediately at application or game launch. APA allows you to choose, and capture traces from your device at launch or triggered manually. The user interface allows you to select which GPU counters and other data is captured in a trace - and if you have more complex needs, you can provide your own custom [Perfetto configuration](https://perfetto.dev/docs/concepts/config).

**Deep-Dive System Analysis**

With APA, you can analyze the entire system's behavior in one view. For example, you can easily examine CPU cores - both their frequencies and the work scheduled on them or inspect processes \& their thread activity.

For graphics-heavy apps, APA provides GPU performance counter data across hardware from Qualcomm, Arm, Imagination, and Samsung. You can even track battery and power consumption to see the impact of your code on power consumption.

To understand exactly where frames are spending time, SurfaceFlinger events provide deep visibility into the rendering and display composition pipeline, from initial code acquisition to final display. And with the new screenshots feature, you can visually scrub through to easily find the exact areas where you want to focus your attention.

You can open existing Perfetto traces, zoom through the timeline for precise detail, and use rulers to measure the duration of work and events. APA also lets you bookmark and annotate interesting findings, and you can pin critical tracks to the top of your screen to keep your focus exactly where it needs to be as you optimize.

### Workflow features

**Tabbed interface and split windows**: You can open multiple traces in side-by-side tabs or split a single trace into two windows to compare different regions of the same trace simultaneously.
![02-apa-side-by-side-tabs.png](https://developer.android.com/static/blog/assets/02_apa_side_by_side_tabs_8d692be1db_1tghjD.webp)

**Project-based workflow:** APA uses a project model that allows you to keep track of multiple traces from the project sidebar. This is especially useful for gathering the results of A/B testing and longitudinal tests, and keeping all of your results together for comparison \& quick access purposes.
![03-apa-workspace-management.png](https://developer.android.com/static/blog/assets/03_apa_workspace_management_c755c4a790_ZfwzCV.webp)

**Navigate visually using screenshots**: APA lets you capture screenshots during a trace (without any noticeable performance overhead) to home in on areas where you saw something affect performance by scrubbing through the timeline. Or even just to get your bearings.
![04-apa-netmarble-.gif](https://developer.android.com/static/blog/assets/04_apa_netmarble_62ea3ae1c6_Z1vkf7O.webp)

**Persistent view customizations:** When you pin or vertically resize tracks, we save those customizations so that they persist the next time you open the trace.

### Analysis tools \& new skills for AI agents

**Vulkan debug trace markers for render passes:** We support Vulkan debug annotations for render passes - which allow you to view Render Pass names you set from your codebase directly in the tracks and slices shown in APA.

This immensely helps you to make logical connections between the workloads you see in the profiler to where they are originating from in your codebase.
![05-vulkan-debug-markers.png](https://developer.android.com/static/blog/assets/05_vulkan_debug_markers_7032b9b1f2_29pn3K.webp)

**Use AI to build SQL queries for custom analysis work**: APA supports trace analysis via SQL queries and ships with a new Perfetto SQL skill for use with your favorite AI agents. This makes it easier to build queries without needing to remember Perfetto SQL schemas or the SQL syntax.
![06-apa-sql-queries.png](https://developer.android.com/static/blog/assets/06_apa_sql_queries_708d5e839f_GBDEJ.webp)

**Ask Gemini to analyze traces for you:**We've also added another Perfetto Analysis skill to answer high-level questions for you - like "Why is my app startup slow?" - helping you to find starting points when analyzing complex traces, using your favorite AI agent to pinpoint the answers.
![07-apa-sql-analysis.png](https://developer.android.com/static/blog/assets/07_apa_sql_analysis_3d7b6c6536_Z1K97Bg.webp)

**FPS and Frame Duration times :** You can review the FPS and Frame duration time at a glance in the tracks to correlate it with other activity happening in your trace.
![08-apa-fps-track.png](https://developer.android.com/static/blog/assets/08_apa_fps_track_1e661cbe2c_Z1fmdN.webp)

## Speed \& robustness improvements

**Speed and robustness improvements:** Rendering a trace is now typically 6x to 26x faster than Android GPU Inspector, and APA is significantly more stable when working with large traces.

### Case studies

We've worked with our early access partners to create detailed case studies showcasing how APA could be used to improve performance for Vulkan apps \& games.

## The Forge Interactive

[The Forge](https://theforge.dev/) used Android Performance Analyzer to identify the need to batch calls to vkCmdBindDescriptorSets, which reduced CPU setup costs by \~50%. This, in turn, slowed heat production on their device by 2-3x, leading to longer session times. They also used APA to identify opportunities to move font and UI rendering work over to the GPU, improving scalability.

You can read the full [case study from The Forge here](https://developer.android.com/android-performance-analyzer/case-study/the-forge).

**Note:** This case study demonstrates how to use custom SQL queries in the profiler to generate a total rendering cost metric.
![09-apa-the-forge.png](https://developer.android.com/static/blog/assets/09_apa_the_forge_fe64ec5d23_ZGuUMM.webp)

## NetMarble -- Seven Deadly Sins: Origin

[Netmarble](https://www.netmarble.com/) used Android Performance Analyzer to fine-tune their game [*Seven Deadly Sins: Origin*](https://play.google.com/store/apps/details?id=com.netmarble.nanaori), focusing particularly on improving performance by making changes to the precision of their shaders, and exploring the impact of upscaling on the performance of their renderer.

This allowed them to reduce the GPU cost of rendering some scenes by up to 90%.

Read the full [NetMarble case study here](https://developer.android.com/android-performance-analyzer/case-study/netmarble-perf-analyzer).
![10-apa-netmarble.png](https://developer.android.com/static/blog/assets/10_apa_netmarble_00c3912087_sY2pC.webp)

## Profiling model complexity in Google's Filament engine

Google has been improving the [Filament](https://github.com/google/filament) glTF Viewer, our physically-based rendering engine.

We spent some time digging into the viewer with a variety of scenes, and showed how to use Android Performance Analyzer to identify scenes that are too complex for the GPU, and how to trim them down to hit a target 60FPS, by improving texture compression and optimizing geometry. Memory consumption was also reduced in this process.

You can read [our exploration of Filament here](https://developer.android.com/android-performance-analyzer/case-study/filament).
![11-apa-filament-02.png](https://developer.android.com/static/blog/assets/11_apa_filament_02_2c8ffaff8c_3068G.webp)

### Try out the Android Performance Analyzer Beta today!

The Android Performance Analyzer is available for you to try out and use today:

- **Standalone profiler:** [https://developer.android.com/android-performance-analyzer](https://developer.android.com/android-performance-analyzer)
- **Android Studio Canary Build (Panda 4 canary builds and later):** [https://developer.android.com/studio/preview](https://developer.android.com/studio/preview)

This is beta software, which means that you might run into an occasional bug -- please report it to us if you find any (**Help Menu \> Submit a bug report**).

We're excited to see how you use the new Android Performance Analyzer, and how it will help your project's performance and reliability.

Explore this announcement and all Google I/O 2026 updates on [io.google](https://io.google/2026/?utm_source=blogpost&utm_medium=pr&utm_campaign=devblogs&utm_content).
Written by:

-

  ## [Mayank Jain](https://developer.android.com/blog/authors/blog-author)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/blog-author) ![View Mayank Jain's profile](https://developer.android.com/static/blog/assets/unnamed_2_feee4f83eb_13HwUT.webp) ![View Mayank Jain's profile](https://developer.android.com/static/blog/assets/unnamed_2_feee4f83eb_13HwUT.webp)
Continue reading
- [![View Raghavendra Hareesh Pottamsetty's profile](https://developer.android.com/static/blog/assets/Raghavendra_Hareesh_Pottamsetty_72fdb063a0_1h0S85.webp)](https://developer.android.com/blog/authors/raghavendra-hareesh-pottamsetty) 26 Aug 2026 26 Aug 2026 ![](https://developer.android.com/static/blog/assets/Raising_the_bar_Google_Play_Strapi_2_a80695bf12_Z2jxf1k.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Elevating app quality: Reducing memory usage and improving device migration](https://developer.android.com/blog/posts/elevating-app-quality-reducing-memory-usage-and-improving-device-migration)

  [arrow_forward](https://developer.android.com/blog/posts/elevating-app-quality-reducing-memory-usage-and-improving-device-migration) Maintaining a healthy Android ecosystem is a shared commitment where every app and game has a role to play.
  [Raghavendra Hareesh Pottamsetty](https://developer.android.com/blog/authors/raghavendra-hareesh-pottamsetty) • 4 min read
- [![View Ron Aquino's profile](https://developer.android.com/static/blog/assets/unnamed_18_8bd07de9bd_9wUet.webp)](https://developer.android.com/blog/authors/ron-aquino) 25 Aug 2026 25 Aug 2026 ![](https://developer.android.com/static/blog/assets/Ensuring_a_safe_Gen_AI_ecosystem_on_Google_Play_Scrapi_a8fa6da415_ZsHups.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Ensuring Safety in the Generative AI Ecosystem: Protecting Users from Non-Consensual Intimate Content](https://developer.android.com/blog/posts/ensuring-safety-in-the-generative-ai-ecosystem-protecting-users-from-non-consensual-intimate-content)

  [arrow_forward](https://developer.android.com/blog/posts/ensuring-safety-in-the-generative-ai-ecosystem-protecting-users-from-non-consensual-intimate-content) At Google Play, user safety and developer success go hand in hand. We continue to see growth in apps with AI generated features, and indeed, adding generative AI into your apps is a great way to unlock incredible creative possibilities.
  [Ron Aquino](https://developer.android.com/blog/authors/ron-aquino) • 4 min read
- 3 Authors 24 Aug 2026 24 Aug 2026 ![](https://developer.android.com/static/blog/assets/Android_1_Strapi_6f49d09922_ZVXnJg.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [AAOS SDV - Secure by Design](https://developer.android.com/blog/posts/aaos-sdv-secure-by-design)

  [arrow_forward](https://developer.android.com/blog/posts/aaos-sdv-secure-by-design) At Google, we believe our products should be secure by design, which is why we built the Android Automotive Operating System for Software Defined Vehicle (AAOS SDV) on existing, market-proven platforms, leveraging virtualization technologies like Cuttlefish.
  [Markus Vill](https://developer.android.com/blog/authors/markus-vill), [Sean Keys](https://developer.android.com/blog/authors/sean-keys), [István Nádor](https://developer.android.com/blog/authors/istvan-nador) • 5 min read
  - [#Android Auto](https://developer.android.com/blog/topics/android-auto)
  - [#Security](https://developer.android.com/blog/topics/security)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)