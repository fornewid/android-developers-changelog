---
title: https://developer.android.com/topic/performance/memory/guide/locality
url: https://developer.android.com/topic/performance/memory/guide/locality
source: md.txt
---

While memory is often thought of as a single, uniform pool of storage, its
physical organization and the way the CPU accesses it have a profound impact on
application performance. Understanding **memory locality** is key to writing
high-performance code that makes efficient use of the CPU's cache hierarchy.

## The CPU cache hierarchy

A modern mobile CPU is much faster than the system's main RAM (DRAM). To bridge
this performance gap, CPUs use several levels of small, extremely fast memory
called **caches**.

> [!NOTE]
> **Note:** The hierarchies and latencies listed below are representative examples intended to establish relative proportions. These values are subject to change as CPU architectures evolve.

- **L1 Cache (Level 1)**: The smallest and fastest (\~1ns). On a 3GHz CPU, this is about 3 clock cycles.
- **L2 Cache (Level 2)**: Larger and slightly slower (\~3-5ns, or \~10-15 cycles).
- **L3 Cache (Level 3)**: The largest cache (\~10-20ns, or \~30-60 cycles).
- **Main Memory (DRAM)**: The largest and slowest (\~100ns+, or \~300+ cycles).

![Memory Latency Pyramid](https://developer.android.com/static/topic/performance/memory/guide/images/locality/pyramid.png)

### Contextualizing latency: the cost of a stall

To understand the impact of these numbers, consider a modern superscalar CPU
that can retire 4 to 8 instructions per clock cycle.

If the CPU misses all caches and must wait 100ns (300 cycles) for a DRAM read:

- **Cycles Lost**: \~300 cycles.
- **Instructions "Wasted"** : Between **1,200 and 2,400 instructions** that could have been executed if the data were already in a local register or the L1 cache.

When your code has poor memory locality, the CPU isn't necessarily busy with
complex math; it is frequently "stalled," sitting idle for thousands of
instruction-equivalents while waiting for the memory subsystem.

### Instructions per cycle (IPC)

A key metric for measuring this efficiency is **Instructions Per Cycle (IPC)**.
IPC represents how many instructions the CPU successfully "retires" (completes)
on average during each clock cycle.

- **High IPC (e.g., 3.0 - 5.0)**: The CPU is running at high efficiency, likely finding most of its data in L1/L2 caches or registers.
- **Low IPC (e.g., \< 0.5)** : The CPU is severely bottlenecked. Even if the CPU is at 100% "usage" in system monitors, it is actually spent mostly waiting for memory---a state known as a **memory stall**.

Memory locality is the primary factor that determines whether a data-intensive
loop runs at high IPC or collapses into a series of stalls.

### Cache lines

CPUs do not load single bytes from memory. Instead, they load fixed-size blocks
called **cache lines**, which are typically 64 bytes. When you access a single
variable, the CPU fetches the entire 64-byte chunk containing it into the cache.

![Cache Line Mechanics](https://developer.android.com/static/topic/performance/memory/guide/images/locality/cache_line.png)

### TLB (translation lookaside buffer)

Android uses virtual memory. Every memory access requires translating a virtual
address to a physical address. The **TLB** is a specialized cache that stores
recent translations. A **TLB miss** requires the kernel to walk page tables in
main memory, which is a **relatively expensive** operation compared to a TLB
hit.

*** ** * ** ***

## Hardware profile: Pixel 10 Pro Fold

For the following exercises, we used a **Pixel 10 Pro Fold** hardware device.
This device features a **Google Tensor G5** SoC.

### Interrogating the hardware

To understand the memory subsystem, we first examine the CPU configuration and
cache parameters.

> [!NOTE]
> **Note:** The following commands require **root access** (`adb root`).

    # Check CPU architecture and core parts
    adb shell cat /proc/cpuinfo | grep 'CPU part' | sort -u
    # Output:
    # CPU part  : 0xd8b
    # CPU part  : 0xd8c
    # CPU part  : 0xd90

    # Check cache line size
    adb shell getconf -a | grep CACHE_LINESIZE
    # Output:
    # LEVEL1_ICACHE_LINESIZE             64
    # LEVEL1_DCACHE_LINESIZE             64

### Decoding CPU parts

The `CPU part` values in `/proc/cpuinfo` are hexadecimal identifiers for ARM CPU
cores. For the Laguna SoC found in the Pixel 10 Pro Fold, these map to:

- **`0xd8b`** : ARM **Cortex-A520** (Efficiency cores)
- **`0xd90`** : ARM **Cortex-A720** (Performance cores)
- **`0xd8c`** : ARM **Cortex-X4** (Prime core)

This 4+3+1 configuration is common in modern mobile SoCs, where different
clusters may have different cache sizes and latencies.

*** ** * ** ***

## Types of locality

Efficient software design relies on two main types of locality:

1. **Spatial Locality**: If a memory location is accessed, nearby memory locations are likely to be accessed soon. Sequential array traversal is the classic example. Because the CPU loads an entire cache line, accessing the next element in an array is almost "free" if it's already in the cache line.
2. **Temporal Locality**: If a memory location is accessed, the same location is likely to be accessed again soon. Good algorithms reuse data while it is still "hot" in the cache.

*** ** * ** ***

## Hands-on exercise: measuring locality with simpleperf

In this exercise, we will use `simpleperf` to monitor hardware performance
counters while running two different traversals of a 256MB matrix.

1. **Row-major Traversal**: Accesses the matrix elements in the order they are stored in memory. This is cache-friendly and exploits spatial locality.
2. **Column-major Traversal**: Jumps across memory to access elements by column. This frequently misses the cache and the TLB, forcing the CPU to stall.

> [!NOTE]
> **Note:** `simpleperf` requires your device be running a userdebug

### 1. Run with Simpleperf

Push the binary, ensure it is executable, and use `simpleperf stat` to measure
cache and TLB events. We use the `:u` suffix to measure events in userspace.
These commands require `adb root` to access hardware PMU counters on most
devices.

    adb root
    adb shell "chmod +x /data/local/tmp/LocalityLab"

**Profile Row-major:**

    adb shell "simpleperf stat -e cpu-cycles:u,instructions:u,cache-misses:u,L1-dcache-load-misses:u,dTLB-load-misses:u /data/local/tmp/LocalityLab row"

**Profile Column-major:**

    adb shell "simpleperf stat -e cpu-cycles:u,instructions:u,cache-misses:u,L1-dcache-load-misses:u,dTLB-load-misses:u /data/local/tmp/LocalityLab col"

### 2. Sample measurements (Pixel 10 Pro Fold)

The following results were measured on a Pixel 10 Pro Fold hardware device:

| Metric | Row-major (Friendly) | Column-major (Unfriendly) | Difference |
|---|---|---|---|
| **Execution Time** | **0.83 seconds** | **68.3 seconds** | **\~82x slower** |
| **Instructions** | 5.27 Billion | 10.20 Billion | \~1.9x more |
| **CPU Cycles** | 1.20 Billion | 62.18 Billion | **\~52x more** |
| **Instructions Per Cycle (IPC)** | **4.40** | **0.16** | **27x lower efficiency** |
| **L1 Data Cache Misses** | 210 Million | 3,369 Million | **16x more misses** |
| **dTLB Load Misses** | 0.13 Million | 2,888 Million | **22,000x more misses** |

> [!NOTE]
> **Note:** In this exercise, we explicitly disabled SIMD auto-vectorization using `#pragma clang loop vectorize(disable)`. This ensures that the performance gap we measure is strictly due to memory subsystem bottlenecks (cache and TLB) rather than a difference between SIMD and scalar instruction throughput.

### 3. Analysis of results

- **The IPC Crash** : In the row-major test, the CPU achieves an IPC of 4.40, indicating it is efficiently executing multiple instructions per cycle. In the column-major test, IPC drops to 0.16. This means the CPU is **stalled
  96% of the time**, waiting for data to arrive from DRAM.
- **The TLB Bottleneck** : The most dramatic difference is in **dTLB-load-misses**. Sequential access (row-major) stays within the same memory pages, resulting in very few TLB misses. Jumping across columns (column-major) causes the CPU to constantly reference new pages, overwhelming the TLB and forcing expensive page table walks.
- **Cache Efficiency**: The column-major traversal generates 16x more L1 cache misses, forcing the CPU to fetch data from much slower L3 or DRAM constantly.

**Observation:** Even though both traversals performed the same logical
operation on the same data, the column-major traversal was **over 80 times
slower**. This massive difference is entirely due to how the access pattern
interacts with the physical reality of the CPU's memory subsystem.

*** ** * ** ***

**[← Threads](https://developer.android.com/topic/performance/memory/guide/threads) \| [↑ Up](https://developer.android.com/topic/performance/memory/guide) \| [Service bindings →](https://developer.android.com/topic/performance/memory/guide/service-bindings)**