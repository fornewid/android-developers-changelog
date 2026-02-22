---
title: https://developer.android.com/games/engines/unity/unity-lmks
url: https://developer.android.com/games/engines/unity/unity-lmks
source: md.txt
---

Solving[LMKs](https://developer.android.com/games/optimize/vitals/lmk)in your Unity game is a systematic process:
![](https://developer.android.com/static/images/games/engines/unity/unity-lmk-flowchart.jpg)**Figure 1.**Steps to solve Low Memory Kills (LMKs) in Unity games.

## Obtain a memory snapshot

Use the[Unity Profiler](https://docs.unity3d.com/6000.1/Documentation/Manual/Profiler.html)to get a Unity-managed memory snapshot. Figure 2 shows the memory management layers Unity uses to handle memory in your game.
![](https://developer.android.com/static/images/games/engines/unity/unity-lmk-memory-management.jpg)**Figure 2.**Unity's memory management overview.

### Managed memory

Unity's memory management implements a[controlled memory layer](https://docs.unity3d.com/Manual/performance-managed-memory-introduction.html)that uses a managed heap and a[garbage collector](https://docs.unity3d.com/6000.1/Documentation/Manual/performance-garbage-collector.html)to allocate and assign memory automatically. The managed memory system is a C# scripting environment based on[Mono](https://docs.unity3d.com/6000.1/Documentation/Manual/scripting-backends-mono.html)or[IL2CPP](https://docs.unity3d.com/6000.1/Documentation/Manual/scripting-backends-il2cpp.html). The benefit of the managed memory system is that it utilizes a garbage collector to automatically free memory allocations.

### C# unmanaged memory

The[unmanaged C# memory layer](https://docs.unity3d.com/Manual/performance-unmanaged-memory.html)provides access to the native memory layer, enabling precise control over memory allocations while using C# code. This memory management layer can be accessed through the[Unity.Collections](https://docs.unity3d.com/Packages/com.unity.collections@latest)namespace and by functions such as[UnsafeUtility.Malloc](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.UnsafeUtility.Malloc.html)and[UnsafeUtility.Free](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.UnsafeUtility.Free.html).

### Native memory

Unity's internal C/C++ core uses a[native memory system](https://docs.unity3d.com/Manual/performance-native-memory.html)to manage scenes, assets, graphics APIs, drivers, subsystems, and plug-in buffers. While direct access is restricted, you can safely manipulate data with Unity's C# API and benefit from efficient native code. Native memory rarely requires direct interaction, but you can monitor native memory impact on performance using the Profiler and adjust[settings](https://docs.unity3d.com/Manual//ProfilerWindow.html)to optimize performance.

Memory is not shared between C# and native code as shown in figure 3. Data required by C# is allocated in the managed memory space each time it is needed.

For the managed game's code (C#) to access the engine's native memory data, for instance, a call to[*GameObject.transform*](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/GameObject-transform.html)makes a native call to access memory data in the native area and then returns values to C# using[*Bindings*](https://github.com/Unity-Technologies/UnityCsReference/blob/master/Runtime/Transform/ScriptBindings/Transform.bindings.cs). Bindings ensure proper calling conventions for each platform and handle automatic marshalling of managed types into their native equivalents.

This happens only the first time, as the[managed shell](https://docs.unity.cn/Packages/com.unity.memoryprofiler@1.1/manual/managed-shell-objects.html)for accessing the*transform*property is preserved in native code. Caching the transform property can reduce the number of back-and-forth calls between managed and native code, but the usefulness of caching depends on how often the property is used. Also, note that Unity does not copy parts of native memory into managed memory when you access these APIs.
![](https://developer.android.com/static/images/games/engines/unity/unity-lmk-native-memory.jpg)**Figure 3.**Accessing native memory from the C# managed code.

To learn more, refer to[Memory in Unity introduction](https://docs.unity3d.com/6000.1/Documentation/Manual/performance-memory-overview.html).

In addition, establishing a memory budget is crucial to keep your game running smoothly, and implementing a memory consumption analytics or reporting system ensures that each new release does not exceed the memory budget. Integrating[Play Mode tests](https://docs.unity3d.com/6000.2/Documentation/Manual/test-framework/edit-mode-vs-play-mode-tests.html)with your continuous integration (CI) to verify memory consumption in specific areas of the game is another strategy to gain better insight.

## Manage assets

This is the most impactful and actionable part of memory consumption. Profile as early as possible.

Memory usage in Android games can vary significantly depending on the type of game, number and types of assets, and memory optimization strategies. However, common contributors to memory usage typically include textures, meshes, audio files, shaders, animations, and scripts.

### Detect duplicated assets

The first step is to detect poorly[configured assets](https://unity.com/blog/engine-platform/inspecting-memory-with-the-new-memory-profiler-package#:%7E:text=DLLs%20and%20executables.-,Detecting%20poorly%20configured%20assets,-The%20Unity%20Objects)and[duplicated assets](https://unity.com/blog/engine-platform/inspecting-memory-with-the-new-memory-profiler-package#:%7E:text=this%20example%2C%20easier.-,Locating%20unintentional%20duplicate%20objects,-A%20common%20mistake)using the memory profiler, a build report tool, or the[Project Auditor](https://docs.unity3d.com/Packages/com.unity.project-auditor@1.0/manual/index.html).

### Textures

Analyze your game's device support and decide the correct[texture format](https://developer.android.com/guide/playcore/asset-delivery/texture-compression). You can split the texture bundles for high-end and low-end devices using[Play Asset Delivery](https://developer.android.com/guide/playcore/asset-delivery/integrate-unity),[Addressable](https://docs.unity3d.com/Packages/com.unity.addressables.android@1.0/manual/index.html), or a more manual process with an[AssetBundle](https://developer.android.com/guide/playcore/asset-delivery/integrate-unity).

Follow the most well-known recommendations available in the[Optimize Your Mobile Game Performance](https://create.unity.com/optimize-mobile-game-eBook)and in the[Optimising Unity Texture Import Settings](https://discussions.unity.com/t/optimising-unity-texture-import-settings/1631377)discussion post. Then try these solutions:

- Compress textures with[ASTC formats for a reduced memory footprint](https://developer.arm.com/documentation/102449/0200/Texture-size--color-space--and-compression)and experiment with a higher block rate, such as 8x8.

  If using ETC2 is required, pack your textures in Atlas. Placing multiple textures into a single texture ensures its Power of Two (POT), can reduce draw calls, and can speed up rendering.
- Optimize[RenderTarget](https://docs.unity3d.com/ScriptReference/Graphics.SetRenderTarget.html)texture format and size. Avoid unnecessarily high-resolution textures. Using smaller textures on mobile devices saves memory.

- Use[Texture channel packing](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.3/manual/Mask-Map-and-Detail-Map.html)to save texture memory.

### Meshes and models

Start by checking the[fundamental settings](https://create.unity.com/optimize-mobile-game-eBook)(page 27) and verify these mesh importing settings:

- Merge redundant and smaller meshes.
- Reduce the vertex count for objects in scenes (for example, static or distant objects).
- Generate Level of Detail (LOD) groups for high-geometry assets.

### Materials and shaders

- Strip unused shader variants programmatically during the build process.
- Consolidate frequently used shader variants into uber shaders to avoid shader duplication.
- Enable dynamic shader loading to address the large memory footprint of preloaded shaders in VRAM/RAM. However, pay attention if shader compilation is causing frame hiccups.
- Use dynamic shader loading to prevent all the variants from being loaded. For more information, refer to the[Improvements to shader build times and memory usage](https://unity.com/blog/engine-platform/2021-lts-improvements-to-shader-build-times-and-memory-usage)blog post.
- Use material instancing properly by leveraging`MaterialPropertyBlocks`.

### Audio

Start by checking the[fundamental settings](https://create.unity.com/optimize-mobile-game-eBook)(page 41), and verify these mesh importing settings:

- Remove unused or redundant`AudioClip`references when employing third-party audio engines like FMOD or Wwise.
- Preload audio data. Disable preload for clips that are not immediately required during runtime or scene startup. This helps reduce memory overhead during scene initialization.

#### Animations

- Adjust Unity's[animation compression settings](https://docs.unity3d.com/6000.1/Documentation/Manual/class-AnimationClip.html)to minimize the number of keyframes and eliminate redundant data.
  - Keyframe reduction: Automatically removes unnecessary keyframes
  - Quaternion compression: Compresses rotation data to reduce memory usage

You can adjust compression settings in the**Animation Import Settings** under the**Rig** or**Animation**tab.

- Reuse animation clips instead of duplicating animation clips for different objects.

  Use[Animator Override Controllers](https://docs.unity3d.com/Manual/AnimatorOverrideController.html)to reuse an Animator Controller and replace specific clips for different characters.
- Bake physics-based animations: If your animations are physics driven or procedural, bake them into animation clips to avoid runtime calculations.

- Optimize skeleton rig: Use fewer bones in your rig to reduce complexity and memory consumption.

  - Avoid excessive bones for small or static objects.
  - If certain bones are not animated or needed, remove them from the rig.
- Reduce animation clip length.

  - Trim animation clips to include only the necessary frames. Avoid storing unused or excessively long animations.
  - Use looping animations instead of creating long clips for repeated movements.
- Ensure only one animation component is attached or activated. For example, disable or remove[Legacy animation](https://docs.unity3d.com/Manual/Animations.html)components if you're using[Animator](https://docs.unity3d.com/Manual/AnimationOverview.html).

- Avoid using the Animator if it's unnecessary. For simple VFX, use tweening libraries or implement the visual effect in a script. The animator system can be resource intensive, particularly on low-end mobile devices.

- Use the[Job System](https://docs.unity3d.com/Manual/job-system-overview.html)for animations when handling a large number of animations, as that system has been fully redesigned to be more memory efficient.

### Scenes

When new scenes are loaded, they bring in assets as dependencies. However, without proper[asset lifecycle management](https://unity.com/resources/how-to-use-unity-asset-manager), these dependencies are not monitored by reference counters. As a result, assets may remain in memory even after the unused scenes have been unloaded cause memory fragmentation.

- Use[Unity's Object Pooling](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/Pool.ObjectPool_1.html)to reuse GameObject instances for recurring gameplay elements because object pooling uses a stack to hold a collection of object instances for reuse and is not thread safe. Minimizing`Instantiate`and`Destroy`improves both CPU performance and memory stability.
- Unloading assets:
  - Unload assets strategically during less critical moments, like splash screens or loading screens.
  - Frequent use of[`Resources.UnloadUnusedAssets`](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/Resources.UnloadUnusedAssets.html)causes spikes in CPU processing due to large internal dependency monitoring operations.
  - Check for large CPU spikes in the[GC.MarkDependencies](https://discussions.unity.com/t/how-to-avoid-gc-markdependencies/589376)profile marker. Remove or reduce its execution frequency, and manually unload specific resources instead using[Resources.UnloadAsset](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/Resources.UnloadAsset.html)rather than relying on the all-encompassing[`Resources.UnloadUnusedAssets()`](https://docs.unity3d.com/ScriptReference/Resources.UnloadUnusedAssets.html).
- Restructure scenes rather than constantly using Resources.UnloadUnusedAssets.
- Calling[`Resources.UnloadUnusedAssets()`](https://docs.unity3d.com/ScriptReference/Resources.UnloadUnusedAssets.html)for[`Addressables`](https://docs.unity3d.com/Packages/com.unity.addressables@2.6/manual/index.html)can unintentionally unload dynamically loaded bundles. Carefully manage the lifecycle of dynamically loaded assets.

### Miscellaneous

- Fragmentation caused by scene transitions --- When the method[`Resources.UnloadUnusedAssets()`](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/Resources.UnloadUnusedAssets.html)is called, Unity does the following:

  - Frees memory for assets no longer in use
  - Runs a garbage collector--like operation to check the managed and native object heap for unused assets and unloads them
  - Cleans up texture, mesh, and asset memory provided that no active reference exists
- `AssetBundle`or`Addressable`- making changes in this area is complex and demands a collective effort from the team to implement the strategies. However, once these strategies are mastered, they significantly improve memory usage, reduce download size, and lower cloud costs. For more information on asset management in Unity with, see[`Addressables`](https://docs.unity3d.com/Packages/com.unity.addressables@2.6/manual/index.html).

- Centralized shared dependencies \&mdash: Group shared dependencies, such as shaders, textures, and fonts, systematically into dedicated bundles or`Addressable`groups. This reduces duplication and ensures that unnecessary assets are unloaded efficiently.

- Use`Addressables`for dependency tracking -[Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@2.6/manual/index.html)simplify loading and unloading can automatically unload dependencies that are no longer referenced. Transitioning to`Addressables`for content management and dependency resolution may be a viable solution, depending on the game's specific case. Analyze dependency chains with the Analyze[tool](https://docs.unity3d.com/Packages/com.unity.addressables@2.5/manual/editor/tools/AnalyzeTool.html)to identify unnecessary duplicates or dependencies. Alternatively, refer to the Unity Data Tools if you're using AssetBundles.

- `TypeTrees`- if your game's`Addressables`and`AssetBundles`are built and deployed using the same version of Unity as the player and do not require backward compatibility with other player builds, consider[disabling writing`TypeTree`](https://docs.unity3d.com/Packages/com.unity.addressables@2.3/manual/memory-assetbundles.html#typetrees), which should reduce bundle size and serialized file object memory footprint. Modify the build process in the local**Addressables** package setting[ContentBuildFlags](https://docs.unity3d.com/2022.3/Documentation/ScriptReference/Build.Content.ContentBuildFlags.DisableWriteTypeTree.html)to**DisableWriteTypeTree**.

## Write garbage collector--friendly code

Unity utilizes[garbage collection (GC)](https://docs.unity3d.com/Manual/performance-garbage-collector.html)to manage memory by automatically identifying and freeing up unused memory. While GC is essential, it can cause performance issues (for example, frame rate spikes) if not handled properly, as this process can momentarily pause the game, leading to performance hiccups and a suboptimal user experience.

Refer to the[Unity manual](https://docs.unity3d.com/Manual/performance-reference-types.html)for useful techniques on reducing the frequency of managed heap allocations and to the[UnityPerformanceTuningBible](https://github.com/CyberAgentGameEntertainment/UnityPerformanceTuningBible/releases), page 271, for examples.

- Reduce garbage collector allocations:

  - Avoid LINQ, lambdas, and closures, which allocate heap memory.
  - Use`StringBuilder`for mutable strings in place of string concatenation.
  - Reuse collections by calling`COLLECTIONS.Clear()`rather than re-instantiating them.

  More information is available in the[Ultimate Guide to Profiling Unity games](https://unity.com/resources/ultimate-guide-to-profiling-unity-games?isGated=true)e-book.
- Manage UI canvas updates:

  - Dynamic changes to UI elements --- When UI elements like Text, Image, or`RectTransform`properties are updated (for example, changing text content, resizing elements, or animating positions), the engine may allocate memory for temporary objects.
  - String allocations --- UI elements like Text often require string updates, since strings are immutable in most programming languages.
  - Dirty canvas --- When something on a canvas changes (for example, resizing, enabling and disabling elements, or modifying layout properties), the entire canvas or a portion of it may be marked as*dirty*and be rebuilt. This can trigger the creation of temporary data structures (for example, mesh data, vertex buffers, or layout calculations), which adds to garbage generation.
  - Comples or frequent updates --- If the canvas has a large number of elements or is updated frequently (for example, every frame), these rebuilds can lead to significant memory churn.
- [Enable incremental GC](https://docs.unity3d.com/Manual/performance-incremental-garbage-collection.html)to reduce large collection spikes by spreading allocation cleanups over multiple frames. Profile to verify whether this option improves your game's performance and memory footprint.

- If your game requires a controlled approach, set the[garbage collection mode to manual](https://docs.unity3d.com/Manual/performance-disabling-garbage-collection.html#disable-incremental-garbage-collection). Then, on a level change or at another moment without active gameplay, call the garbage collection.

- Invoke manual garbage collection[GC.Collect()](https://discussions.unity.com/t/what-is-gc-collect-and-why-is-it-slowing-down-my-game/820494)calls for game state transitions (for example, level switching).

- Optimize[arrays](https://docs.unity3d.com/Manual/performance-optimizing-arrays.html)starting from simple code practices and, if necessary, by using native arrays or other native containers for large arrays.

- Monitor managed objects using tools like the Unity Memory Profiler to track unmanaged object references that persist after destruction.

  Use a[Profiler Marker](https://docs.unity3d.com/ScriptReference/Unity.Profiling.ProfilerMarker.html)to submit to the[Performance Reporting Tool](https://docs.unity3d.com/560/Documentation/Manual/UnityPerformanceReporting.html#:%7E:text=Unity%20Performance%20Reporting%20captures%20and,Play%20Mode%20within%20the%20Editor.)for an automated approach.

## Avoid memory leaks and fragmentation

### Memory leaks

In C# code, when a reference to a[Unity Object](https://docs.unity3d.com/6000.1/Documentation/Manual/GameObjects.html)exists after the object has been destroyed, the managed wrapper object, known as the[Managed Shell](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@1.1/manual/managed-shell-objects.html), remains in memory. The native memory associated with the reference is released when the scene is unloaded or when the GameObject the memory is attached to, or any of its parent objects, are destroyed through the`Destroy()`method. However, if other references to the Scene or GameObject were not cleared, the managed memory[may persist as a Leaked Shell Object](https://youtu.be/UIwQmpQTtA4?t=265). For further details on Managed Shell Objects, consult the[Managed Shell Objects](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@1.1/manual/managed-shell-objects.html)manual.

Additionally, memory leaks can be caused by event subscriptions, lambdas and closures, string concatenations, and improper management of pooled objects:

- To get started, see[Find memory leaks](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@1.1/manual/find-memory-leaks.html)to compare Unity memory snapshots properly.
- Check for event subscriptions and memory leaks. If objects subscribe to events (for example, by delegates or UnityEvents) but do not properly unsubscribe before being destroyed, the event manager or publisher may retain references to those objects. This prevents those objects from being garbage collected, leading to memory leaks.
- Monitor global or singleton class events that aren't unregistered on object destruction. For example, unsubscribe or unhook delegates in object destructors.
- Ensure destruction of pooled objects fully nullifies references to[text mesh components](https://docs.unity3d.com/Packages/com.unity.ugui@3.0/manual/TextMeshPro/index.html)%7B:.external%7D), textures, and parent GameObjects.
- Keep in mind that when comparing Unity Memory Profiler snapshots and observing a[difference in memory consumption without a clear reason](https://discussions.unity.com/t/unable-to-determine-cause-of-memory-leak-in-unity-when-using-addressables-can-anyone-give-suggestions-on-what-the-cause-might-be/1591429/3), the difference may be caused by the graphics driver or the operating system itself.

### Memory fragmentation

Memory fragmentation occurs when many small allocations are freed in a random order. Heap allocations are made sequentially, which means new memory chunks are created when the previous chunk runs out of space. Consequently, new objects do not fill the empty areas of old chunks, leading to fragmentation. Additionally, large temporary allocations can cause permanent fragmentation for the duration of a game's session.

This issue is particularly problematic when short-lived large allocations are made near long-lived ones.

Group allocations based on their lifespan; ideally, long-lived allocations should be made together, early in the application's lifecycle.

#### Observers and event managers

- In addition to the problem mentioned in the (Memory Leaks)[77](https://developer.android.com/games/engines/unity/%7B:#memory-leaks%7D)section, over time, memory leaks can contribute to fragmentation by leaving unused memory allocated to objects that are no longer in use.
- Ensure destruction of pooled objects fully nullifies references to[text mesh components](https://docs.unity3d.com/Packages/com.unity.ugui@3.0/manual/TextMeshPro/index.html)%7B:.external%7D), textures, and parent`GameObjects`.
- Event managers often create and store lists or dictionaries to manage event subscriptions. If these grow and shrink dynamically during runtime, they can contribute to memory fragmentation due to frequent allocations and deallocations.

#### Code

- [Coroutines](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/Coroutine.html)sometimes allocate memory, which can be easily avoided by caching the return statement of the[IEnumerator](https://discussions.unity.com/t/ienumerator/892998/2)instead of declaring a new one every time.
- Continuously monitor the lifecycle states of pooled objects to avoid keeping`UnityEngine.Object`ghost references.

#### Assets

- Use dynamic fallback systems for text-driven game experiences to avoid preloading all fonts for multilanguage cases.
- Organize assets (for example, textures and particles) together by type and expected lifecycle.
- Condense assets with idle lifecycle attributes, like redundant UI images and static meshes.

#### [Lifetime-based allocations](https://docs.unity3d.com/Packages/com.unity.collections@1.3/manual/allocation.html)

- Allocate long-lived assets at the start of the application lifecycle to ensure compact allocations.
- Use[NativeCollections](https://docs.unity3d.com/Packages/com.unity.collections@1.0/manual/index.html)or custom allocators for memory-intensive or transient data structures (for example, physics clusters).

## Code-related and executables memory action

Game executable and plugins also affect the memory usage.

### IL2CPP Metadata

[IL2CPP](https://docs.unity3d.com/6000.1/Documentation/Manual/scripting-backends-il2cpp.html)generates metadata for every type (for example, classes, generics, and delegates) at build time, which is then used at runtime for reflection, type checking, and other runtime-specific operations. This metadata is stored in memory and can contribute significantly to the total memory footprint of the application. IL2CPP's metadata cache makes a significant contribution to initialization and loading times. Additionally, IL2CPP doesn't deduplicate certain metadata elements (for example, generic types or serialized information), which can result in bloated memory usage. This is exacerbated by repetitive or redundant type usage in the project.

IL2CPP metadata can be reduced by:

- Avoiding the use of[reflection APIs](https://learn.microsoft.com/en-us/dotnet/csharp/advanced-topics/reflection-and-attributes/), as they can be a significant contributor to IL2CPP metadata allocations
- Disabling[built-in packages](https://docs.unity3d.com/2023.2/Documentation/Manual/upm-ui-disable.html)
- Implementing Unity 2022[full generic sharing](https://blog.unity.com/engine-platform/il2cpp-full-generic-sharing-in-unity-2022-1-beta), which should help reduce the overhead caused by generics. However, to help reduce allocations even further, reduce the use of generics.

### Code stripping

Beyond reducing the size of the build, code stripping also decreases the memory usage. When building against the IL2CPP scripting backend, managed bytecode stripping (which is activated by default) removes unused code from managed assemblies. The process works by defining root assemblies and then using static code analysis to determine what other managed code those root assemblies use. Any code that is not reachable is removed. For more information about Managed Code Stripping, see the[TTales from the optimization trenches: Better managed code stripping with Unity 2020 LTS](https://unity.com/blog/engine-platform/tales-from-the-optimization-trenches-better-managed-code-stripping-with-unity-2020)blog post and the[Managed code stripping](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-stripping.html)documentation.

### Native allocators

Experiment with native[memory allocators](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-allocators.html)to fine-tune memory allocators. If the game is low on memory, use smaller memory blocks, even if this involves slower allocators. See Dynamic[heap allocator example](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-dynamic-heap-allocator.html)to learn more.

## Manage native plugins and SDKs

- Find the problematic plugin --- Remove each plugin and compare the game memory snapshots. This involves disabling a lot of code functionality with[Scripting Define Symbols](https://docs.unity3d.com/6000.1/Documentation/Manual/custom-scripting-symbols.html)and refactoring highly coupled classes with interfaces. Check[Level up your code with game programming patterns](https://unity.com/resources/level-up-your-code-with-game-programming-patterns)to facilitate the process of disabling external dependencies without making your game unplayable.

- Contact the plugin or SDK author --- Most of the plugins are not open source.

- Reproduce the plugin memory usage --- You can write a simple plugin (use this[Unity plugin](https://github.com/android/games-samples/tree/main/unity)as reference) that does memory allocations. Inspect the memory snapshots using Android Studio (as Unity doesn't track these allocations) or call the[`MemoryInfo`](https://developer.android.com/reference/android/app/ActivityManager.MemoryInfo)class and[`Runtime.totalMemory()`](https://developer.android.com/reference/java/lang/Runtime#totalMemory())method in the same project.

A Unity plugin allocates Java and native memory; here's how to do it:

**Java**  

    byte[] largeObject = new byte[1024 * 1024 * megaBytes];
    list.add(largeObject);

**Native**  

    char* buffer = new char[megabytes * 1024 * 1024];

    // Random data to fill the buffer
    for (int i = 1; i < megabytes * 1024 * 1024; ++i) {
       buffer[i] = 'A' + (i % 26); // Fill with letters A-Z
    }