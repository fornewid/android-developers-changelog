---
title: https://developer.android.com/games/optimize/memory-reduction
url: https://developer.android.com/games/optimize/memory-reduction
source: md.txt
---

Once you understand Android memory management and have set up tools to measure
your game's memory use, the next step is to actively reduce and optimize it.
Staying within Android's strict limits helps prevent the system from closing
your game, stops long startup times, and ensures your game runs well on all
devices.

This guide provides practical techniques to trim your game's memory footprint,
specifically focusing on asset-level optimization, engine-specific
configurations, and memory management best practices.

## Reduce memory in Unity

Due to the architectural design of Unity, once native block allocators and the
managed heap expand, the engine tends to retain those memory pages for reuse
rather than immediately returning them to the operating system (OS), even after
assets are released. Specifically, the virtual address space (reserved memory)
remains reserved for the lifetime of the process, and physical memory (RSS)
isn't reclaimed right away until several garbage collection (GC) and trimming
cycles have occurred. Consequently, a temporary memory peak can cause resident
memory to stay inflated for a long time even after actual usage drops. This
behavior increases the risk of out-of-memory (OOM) crashes on low-end devices
and degrades overall runtime stability.

Therefore, Unity memory optimization must be approached through three core
pillars tailored to these engine behaviors:

- Control active memory usage to prevent peak memory spikes in the first place.
- Manage texture formats and shader variants to ensure unnecessary assets and native resources aren't instantiated.
- Refactor runtime code structures to eliminate unnecessary allocations on the managed heap to minimize GC frequency and heap expansion.

For more information, see [Unity memory optimization](https://developer.android.com/games/engines/unity/unity-reduce-memory).