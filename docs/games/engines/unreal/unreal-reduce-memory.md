---
title: https://developer.android.com/games/engines/unreal/unreal-reduce-memory
url: https://developer.android.com/games/engines/unreal/unreal-reduce-memory
source: md.txt
---

Memory usage is critical in Android game development.
When developing games using Unreal Engine, you must [continuously
analyze and track the memory state](https://developer.android.com/games/engines/unreal/unreal-memory-usage) to satisfy these memory constraints,
preventing memory leaks and excessive memory allocations.

## Memory savings through shader permutation reduction

By removing unused options in `Lighting` or `Mobile Shader Permutation
Reduction`, you can minimize the number of shader permutations. This
significantly reduces the app packaging size, lowers the
number of pipeline state objects (PSOs), and prevents the creation of unused
render targets or dummy textures, leading to reduced runtime memory and
better performance.

For more information, see the **Misc Lighting and Shader Permutation
Reduction Settings for Mobile** section in
[Performance Guidelines for Mobile Devices](https://dev.epicgames.com/documentation/unreal-engine/performance-guidelines-for-mobile-devices-in-unreal-engine?application_version=5.8).

## Asset loading optimization

When loading assets using hard references, connected content that isn't even
used in the game is loaded into memory simultaneously, causing unnecessary
memory consumption. In particular, when inheritance is misused in Blueprints,
unnecessary CDOs (Class Default Objects) from parents are allocated, wasting a
significant amount of memory. In such cases, apply the following techniques to
optimize memory usage.

- **C++ code definition and data separation** : Define core functionalities using `UCLASS(Abstract)` in C++ code, separating them from actual data.
- **Minimize inheritance**: Perform data setup and asset loading only in leaf-node Blueprints.
- **Use indirect references** : Apply indirect property references using `TSoftObjectPtr` to avoid hard references, and asynchronously load assets strictly when needed at runtime.
- **Precautions** : When using Async Asset Loading, ensure that validity checks (`IsValid`) are performed during the loading completion callback to prevent dangling pointers or crashes.

For more information, see [Referencing Assets](https://dev.epicgames.com/documentation/unreal-engine/referencing-assets-in-unreal-engine) and [Building Mobile Games
with UE5](https://dev.epicgames.com/community/learning/talks-and-demos/9y5P/unreal-engine-building-mobile-games-with-ue5-unreal-fest-2023).

## Smart pointers and garbage collection (GC) tuning

Using smart pointers (such as `TSharedPtr` and `TWeakPtr`) during C++
development prevents dangling pointers and memory leaks. Furthermore, using
`TWeakPtr` avoids creating strong references to objects, so the garbage
collector doesn't increment reference counts when collecting objects. This
prevents unnecessary object survival and lowers the complexity of the reference
graph that GC needs to traverse, significantly reducing GC overhead. Garbage
collection can be effectively managed in mobile environments by triggering
`ForceGarbageCollection` during level transitions or periods of inactivity, such
as when there's no user interaction. Additionally, it can be triggered when the
game is in a perceptible state or backgrounded (for example, `onStop`
callbacks), ensuring that garbage collection is performed without affecting the
active gameplay experience.

For more information, see [Garbage Collection](https://dev.epicgames.com/community/learning/courses/45V/c-introduction-to-unreal-engine-for-programmers/Evw6/unreal-engine-garbage-collection) and [Smart Pointer](https://dev.epicgames.com/community/learning/courses/45V/c-introduction-to-unreal-engine-for-programmers/v7BB/unreal-engine-smart-pointers).

## Optimization using relocation table compression

[Relocation Table Compression](https://android.googlesource.com/platform/ndk/+/master/docs/BuildSystemMaintainers.md#relr-and-relocation-packing) is an optimization method that compresses the
Relocation Table size in ELF binaries to [reduce Android binary size](https://dev.epicgames.com/documentation/unreal-engine/reducing-android-binary-size-in-unreal-engine-projects). When
the Android minSDKVersion is 23 or higher, APS Relocation Table Compression is
supported; when minSDKVersion is 28 or higher, RELR Relocation Table Compression
is additionally supported, significantly reducing the size of the .so file. This
not only decreases download size, but also reduces the memory footprint of
the .so mmap at runtime, mitigating overall physical memory pressure.

**AndroidToolChain.cs**

    if (MinSDKVersion >= 28)
    {
      Result += " -Wl,--pack-dyn-relocs=android+relr,--use-android-relr-tags";
    }
    else if (MinSDKVersion >= 23)
    {
      Result += " -Wl,--pack-dyn-relocs=android";
    }

To apply this optimization, verify that **Enable compression of relocation
tables** in Project Settings or the `bEnableAdvancedBinaryCompression` variable
is enabled.

To check whether RELR compression is properly applied to the binary, use the
`llvm-readelf` tool from the Android NDK.

    llvm-readelf -d libUnreal.so | grep RELR

In practice, building Unreal Engine's `ThirdPerson` template and measuring using
`dumpsys meminfo` confirms a reduction in PSS and RSS usage for .so mmap.

| Category | PSS Total | Private Dirty | Private Clean | Swap Dirty | RSS Total |
|---|---|---|---|---|---|
| .so mmap **Before compression** | **170,210** | 24,360 | **141,564** | 0 | **242,204** |
| .so mmap **After compression** | **138,031** | 24,748 | **108,976** | 0 | **210,140** |

## Texture compression

Use appropriate texture compression to reduce the memory footprint of overall
graphics resources. Using [Adaptive Scalable Texture Compression (ASTC)](https://developer.android.com/games/optimize/textures#astc), the
mobile standard, provides superior visual quality compared to ETC2 at the same
size, or achieves higher compression ratios with lower memory consumption under
the same visual quality target.

## Texture streaming optimization

In mobile environments, using the default Unreal Engine [texture streaming
pool](https://dev.epicgames.com/community/learning/tutorials/56mX/unreal-engine-managing-the-texture-streaming-pool) size directly can pre-allocate an excessively large memory pool
relative to device specifications. Therefore, it's ideal to define mobile Device
Profiles and select an appropriate texture streaming pool size according to
device memory limits. Additionally, use the Editor's **Statistic** feature to
check texture stats and identify high-memory-consuming textures occupying
extreme resolutions at runtime. Pair this with the **Required Texture
Resolution** feature to enforce limits or reduce maximum resolutions on
demanding textures, keeping resource usage controlled within the allocated
texture memory buffer.