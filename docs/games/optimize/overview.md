---
title: https://developer.android.com/games/optimize/overview
url: https://developer.android.com/games/optimize/overview
source: md.txt
---

Android optimization tools and APIs are designed to find performance bottlenecks
and determine device limitations while maximizing performance at sustainable
levels for games and graphic-intensive apps.

- [Android GPU Inspector (AGI)](https://developer.android.com/agi): An Android system profiling tool that
  provides advanced GPU tracing and analysis for games and graphic intensive
  apps.

- [Android Performance Tuner (APT)](https://developer.android.com/games/sdk/performance-tuner): Find
  performance issues related to quality settings, scenes, load times, and
  device models in your game.

- [Android Dynamic Performance Framework (ADPF)](https://developer.android.com/games/optimize/adpf):
  Optimize games based on the dynamic thermal, CPU, and GPU management features
  of each device.

- [Memory Advice API](https://developer.android.com/games/sdk/memory-advice/overview): Provide memory use
  estimates and threshold notifications to your game so it can stay at optimal
  levels that avoid LMKs.

- [Game Mode API](https://developer.android.com/games/gamemode): Optimize gameplay by prioritizing
  characteristics, such as performance or battery life based on users settings
  or game specific configurations.

- [Perfetto](https://perfetto.dev/docs/): Collects system-wide
  performance information and displays it in a web-based UI.

- [Systrace](https://developer.android.com/topic/performance/tracing): Records system activity and generates
  reports that help identify performance issues.)

- [CPU Profiler](https://developer.android.com/studio/profile): Inspect your app's CPU
  usage and thread activity, either in real time or from recorded traces.

- [`Meminfo` class](https://developer.android.com/reference/android/os/Debug.MemoryInfo): Records a
  snapshot of your app's memory allocation. You can also use this feature through the
  [`meminfo dumpsys`](https://developer.android.com/studio/command-line/dumpsys#meminfo) command.

- [Bug report](https://developer.android.com/studio/debug/bug-report): View device logs, stack traces, and
  other diagnostic information to help you find and fix bugs in your app.