---
title: https://developer.android.com/topic/performance/memory/guide
url: https://developer.android.com/topic/performance/memory/guide
source: md.txt
---

Memory is a critical and finite resource on Android-powered devices. As an
Android platform developer or OEM, understanding how memory works at every
level---from the Java runtime down to the Linux kernel---is essential for building a
performant and stable system.

This guide provides a comprehensive overview of Android memory architecture, the
tools available for analysis, and hands-on exercises to help you identify and
resolve memory-related issues.

## Objectives

After completing this guide, you will be able to:

- Explain the fundamental concepts of Android memory, including the Zygote process model and memory-mapped files.
- Differentiate between Resident Set Size (RSS), Proportional Set Size (PSS), and Unique Set Size (USS).
- Use standard command-line tools like `dumpsys meminfo` and `showmap` to quickly assess memory usage.
- Capture and analyze Java heap dumps using AHAT to find leaks and excessive allocations.
- Use Perfetto and `heapprofd` to profile both Java and native memory across the entire system.
- Understand system-wide memory pressure indicators like Pressure Stall Information (PSI) and monitor Low Memory Killer (LMK) activity.
- Observe kernel-level reclaim activity, including ZRAM swap and page cache eviction.

## Guide structure

This guide is organized into the following sections, designed to be read
sequentially:

1. **[Fundamental concepts](https://developer.android.com/topic/performance/memory/guide/concepts)**: The core technical principles of Android memory.
2. **[Quick assessment tools](https://developer.android.com/topic/performance/memory/guide/tools-overview)** : Using `meminfo`, `showmap`, and `procstats` for rapid triage.
3. **[Analyzing Java memory](https://developer.android.com/topic/performance/memory/guide/java-memory)**: Deep dives into the Java heap with AHAT.
4. **[Bitmaps and memory](https://developer.android.com/topic/performance/memory/guide/bitmaps)**: Understanding how images impact RAM and using tools to profile them.
5. **[Analyzing native memory](https://developer.android.com/topic/performance/memory/guide/native-memory)** : Profiling C/C++ memory with Perfetto and `heapprofd`.
6. **[WebView and memory](https://developer.android.com/topic/performance/memory/guide/webview-memory)**: Understanding the multi-process architecture and memory footprint of WebViews.
7. **[App code is memory](https://developer.android.com/topic/performance/memory/guide/app-code)**: Understanding how class loading and dex bloat impact RAM.
8. **[Threads and memory](https://developer.android.com/topic/performance/memory/guide/threads)**: Analyzing the cost of native thread stacks.
9. **[Memory locality and performance](https://developer.android.com/topic/performance/memory/guide/locality)**: Understanding how data access patterns affect CPU performance.
10. **[Service bindings and process states](https://developer.android.com/topic/performance/memory/guide/service-bindings)**: Understanding how cross-process dependencies affect OOM scores.
11. **[System-wide troubleshooting](https://developer.android.com/topic/performance/memory/guide/system-wide-memory)**: Monitoring PSI, LMK, ZRAM swap, and page cache eviction.
12. **[Memory reclaim: eviction and swap](https://developer.android.com/topic/performance/memory/guide/reclaim)** : Understanding memcg, charge, and proactive reclaim with `memory.reclaim`.
13. **[kswapd and lmkd interaction](https://developer.android.com/topic/performance/memory/guide/kswapd-lmkd-interaction)**: Understanding how kswapd and lmkd work together under pressure.

## Prerequisites and environment

This guide presents reference workflows, benchmark data, and case studies
demonstrating how to diagnose and resolve Android memory issues.

- **Analysis tools** : The techniques in this guide primarily use standard Android performance tools, including [Perfetto](https://perfetto.dev/), `dumpsys meminfo`, `showmap`, and [AHAT](https://android.googlesource.com/platform/art/+/main/tools/ahat/).
- **Root privileges** : Some system-level diagnostic workflows (such as inspecting kernel memory pressure or hardware PMU counters) require elevated root privileges (`adb root`) on a userdebug device or emulator build.

*** ** * ** ***

**Start Here: [Fundamental concepts](https://developer.android.com/topic/performance/memory/guide/concepts)**