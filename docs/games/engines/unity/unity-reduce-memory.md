---
title: https://developer.android.com/games/engines/unity/unity-reduce-memory
url: https://developer.android.com/games/engines/unity/unity-reduce-memory
source: md.txt
---

Although the physical RAM capacity of modern mobile devices continues to grow,
game memory consumption is outpacing this growth due to high-resolution assets
and complex rendering pipelines.

### Key issues caused by excessive memory usage

- **Low memory killer (LMK) terminations**: The OS forcibly closes background or even foreground apps to resolve system-wide memory shortages.
- **Frame drops and stuttering (jank)**: Frequent garbage collection (GC) spikes in the Managed Heap or OS-level memory swapping create processing bottlenecks.
- **Thermal throttling and battery drain**: Continuous memory allocation, deallocation, and memory page commits incur significant CPU overhead, leading to increased heat and faster battery depletion.

### Android memory management updates

- **Android 17: Introduction of `MemoryLimiter`** : Android 17 introduces [**`MemoryLimiter`**](https://source.android.com/docs/core/perf/memory-limiter) that actively monitors application memory consumption against device-specific thresholds. Apps exceeding their memory limit are immediately terminated at the system level. Because this mechanism is stricter than the traditional LMK, managing **peak memory usage
  is now more critical** than ever.

## Reduce memory usage in Unity

In Unity, once the engine expands its internal memory pools (**Native Block
Allocators** and the **Managed Heap** ) to accommodate a high peak load, it
retains those memory pages rather than immediately returning them to the OS.
Consequently, even after heavy assets are unloaded, the baseline **Resident
Memory** remains inflated, making the application highly vulnerable to Android
OS process terminations (such as **LMK** or **`MemoryLimiter`**).

To prevent OS-level enforcement, memory optimization must be approached through
three key pillars:

- **Category A: Reduce peak memory usage**
- **Category B: Eliminate unnecessary asset and system footprints**
- **Category C: Eliminate unnecessary GC allocations**

## Category A: Reduce peak memory usage

Unity's allocators retain freed memory pages for reuse instead of returning them
to the OS right away, so baseline memory tends to reflect the highest peak
reached rather than current usage. Preventing spikes in the first place is
therefore more effective than relying on cleanup after the fact.

### 1. Avoid overly large AssetBundles

Due to Unity's **Bundle Loading** mechanism, giant AssetBundles lead to severe
memory bloat and OOM crashes. Keep bundles modular to ensure efficient resource
management.

**Key issues**

- **High memory overhead**: Requesting a single tiny asset forces Unity to load the entire bundle file (including headers, metadata, and streaming buffers) into RAM.
- **The unload trap** : If *any* asset within a bundle is actively in use, the **entire bundle can't be unloaded**, trapping unused data in RAM.

**Best practices**

- **Keep bundles modular**: Group assets logically by scene or lifecycle.
- **Unity 6.6+ tip** : Use [**Content Directories**](https://docs.unity3d.com/6000.6/Documentation/Manual/content-directories-introduction.html) to prevent unintended cross-bundle dependencies.

### 2. Optimize asset references in `ScriptableObjects`

Direct `UnityEngine.Object` serialized fields in a `ScriptableObject` create
direct hard references, forcing all referenced assets to load into RAM as soon
as the `ScriptableObject` itself is loaded or instantiated.

    // BEFORE: Loading SceneRequiredAssets forces _worldAsset and _spawnSettings into RAM immediately
    public class SceneRequiredAssets : ScriptableObject
    {
        public string sceneName;
        public Object _worldAsset;
        public Object _spawnSettings;
    }

    // AFTER: Use AssetReference to enable asynchronous, on-demand loading using Addressables
    public class SceneRequiredAssets : ScriptableObject
    {
        public string sceneName;
        public AssetReference _worldAsset;
        public AssetReference _spawnSettings;
    }

### 3. Configure audio clip load types

Loading all audio clips uncompressed directly into memory creates large,
permanent memory peaks. Audio load settings should be configured based on their
usage profile:

| Audio category | Load type | Reason |
|---|---|---|
| **BGM (Background Music)** | Streaming | Streams audio from disk in small buffers to eliminate memory spikes. |
| **Long SFX** | Compressed In Memory | Keeps RAM overhead low and decompresses audio on the fly during playback. |
| **Short \& Frequent SFX** | Decompress On Load | Decompresses audio into RAM upon loading to avoid runtime CPU overhead during playback. |

### 4. Implement object pooling and release strategies

Unreleased instances remaining inside Object Pools across scene transitions hold
onto Reserved Memory indefinitely, keeping the baseline memory footprint
unnecessarily inflated.

- **Action**: Periodically clear or trim unused pooled objects during scene transitions or low-activity periods, allowing Unity to return or reuse that reserved space for other allocations.

## Category B: Eliminate unnecessary memory usage

Eliminating redundant graphic assets and rendering target buffers directly
lowers the baseline memory footprint.

### 1. Optimize render textures and camera depth

- **Remove depth/stencil buffers** : Set the Depth Stencil Format to **None** for Render Textures that only require color data.
- **Disable UI camera depth texture** : For UI cameras where depth data is unnecessary, disable depth texture generation in URP camera settings to eliminate the `CopyDepth` Pass and associated GPU texture memory.

### 2. Optimize textures and meshes

| Category | Optimization guideline |
|---|---|
| **Texture compression** | Always apply target platform compression formats (for example, ASTC for Android). |
| **Read/Write enabled** | Keep disabled unless necessary. Enabling this duplicates texture memory across CPU and GPU RAM. |
| **Mipmaps** | Disable Mipmaps for UI textures or objects fixed at a constant camera distance, saving \~33% texture memory. |
| **Mesh complexity** | Reduce unnecessary polygon counts and vertex streams to lower GPU and native memory footprint. |

### 3. Strip shader variants and optimize memory

Uber-shaders (for example, URP Lit Shader) encapsulate numerous features using
`#multi_compile` and `shader_feature` keywords. Without optimization,
combinatorial explosion creates tens of thousands of unique
**shader variants**, leading to inflated build sizes, massive native memory
consumption, and GPU driver compilation hitches during gameplay.

**A. Mechanics of shader variant memory overhead**

- **Combinatorial explosion**: Total possible variants grow exponentially with each added keyword group.
- **Chunk allocation architecture** : Unity groups compiled binary variants into compressed memory blocks called **Chunks** (default: 4 MB).
- **Native memory bloat** : When runtime code requests even a single variant inside a chunk, **the entire 4 MB chunk is decompressed into RAM**. If unoptimized, thousands of unused variants packaged in those chunks permanently occupy native memory.

**B. Unity built-in multi-stage stripping pipeline** : Unity automatically strips
unnecessary variants at build time based on target platform graphics
settings and unused engine features (for example, Fog, Lightmaps, and XR
settings). Additionally, `shader_feature` variants are automatically
filtered out if their keywords aren't actively used by any material in the
project, whereas `#multi_compile` variants are forcibly included regardless
of usage.

**C. Custom automated stripping architecture
([`IPreprocessShaders`](https://docs.unity3d.com/6000.5/Documentation/ScriptReference/Build.IPreprocessShaders.OnProcessShader.html))** Because static analysis can't
detect keywords modified dynamically using runtime C# scripts
(`Material.EnableKeyword`), standard stripping is often insufficient. To
ensure only actually used variants are included, you can collect variants
during QA test suites using **Player.log** (enabling
**Log Shader Compilation** in Editor settings) or **Profiler Traces**
(`Shader.CreateGPUProgram` markers). Then, implement
`IPreprocessShaders.OnProcessShader` in an Editor script to filter out
variants that were never executed during runtime, keeping only the necessary
ones in the build.

## Category C: Eliminate unnecessary GC allocations

Garbage Collection (GC) allocations in the Managed Heap lead to memory
fragmentation, heap expansions that never shrink, and severe frame drops during
GC pauses.

### 1. Prevent lambda closure allocations

When a lambda expression captures outer local variables, C# generates an
implicit display class on the Heap. Executing this inside `Update` allocates
closure instances every frame.

    // Bad: Capturing local variable 'targetId' allocates a new closure object on the Heap every frame
    void Update()
    {
        int targetId = 100;
        Monster target = monsterList.Find(m => m.Id == targetId);
    }

    // Good 1: Replace with a standard 'for' loop (Recommended: 0 B allocation)
    void Update()
    {
        int targetId = 100;
        Monster target = null;
        for (int i = 0; i < monsterList.Count; i++)
        {
            if (monsterList[i].Id == targetId)
            {
                target = monsterList[i];
                break;
            }
        }
    }

    // Good 2: Use a static lambda (C# 9.0+) if no outer variables are captured
    Monster target = monsterList.Find(static m => m.Id == 100);

### 2. Use stackalloc and Span

Avoid Heap allocations for short-lived temporary arrays by using Stack memory.

    // Before: Allocates an array on the Heap every call (GC Target)
    Vector2[] pos = new Vector2[4];

    // After: Utilizes Stack memory using System.Span (0 B Heap Allocation)
    System.Span<Vector2> pos = stackalloc Vector2[4];

### 3. Optimize collection iteration

Avoid boxing and Enumerator heap allocations caused by LINQ extensions or
ReadOnlyCollection accessors.

    // Before: LINQ Count() causes internal GetEnumerator() heap allocations
    bool hasData = component != null && component.parameters.Count(parameter => parameter.overrideState) > 0;

    // After: Replaced with indexer and direct loop iteration
    bool hasData = HasDataOptimized(component);

    private bool HasDataOptimized(TestComponent component)
    {
        if (component == null) return false;

        var count = component.parameters.Count;
        for (var i = 0; i < count; ++i)
        {
            if (component.parameters[i].overrideState)
                return true;
        }
        return false;
    }

### 4. Additional GC allocation prevention rules

- **Avoid** using `Camera.allCameras` because it generates a new `Camera[]` array on the heap on every call. Instead, cache a camera array and pass it to `Camera.GetAllCameras(_allCameras)`.
- **Avoid `foreach` on `IReadOnlyList<T>`** : Iterating over an interface causes struct enumerator boxing, generating GC allocations. Use a standard `for` loop instead.
- **Cache coroutine objects** : Cache `WaitForSeconds` instances instead of instantiating `yield return new WaitForSeconds(time);` repeatedly.
- **Custom struct keys in dictionaries** : Using custom structs as Dictionary keys calls the default `Equals`, triggering object boxing. Implement `IEqualityComparer<T>` and pass it to the Dictionary constructor.

    public struct TypeKey
    {
        public int v1;
        public int v2;

        public class TypeKeyComparer : IEqualityComparer<TypeKey>
        {
            public bool Equals(TypeKey x, TypeKey y) => x.v1 == y.v1 && x.v2 == y.v2;
            public int GetHashCode(TypeKey obj) => obj.v1.GetHashCode() ^ obj.v2.GetHashCode();
        }
    }

    // Pass custom comparer during Dictionary initialization to prevent boxing
    public readonly Dictionary<TypeKey, int> _typeKeyDictionary = new(new TypeKey.TypeKeyComparer());

### 5. Minimize generic and reflection usage

While generic methods provide excellent code reuse and maintainability,
overusing them can negatively affect your project in the context of Unity IL2CPP
(Intermediate Language to C++) backend.

- **IL2CPP code bloat**: For every unique generic type combination, IL2CPP generates a specialized version of the code. Excessive use of complex generics can lead to a "combinatorial explosion" of generated C++ code, significantly increasing the application's binary size and native memory footprint.
- **Reflection overhead** : Methods using reflection, such as `System.Reflection` APIs, are inherently slow and often cause heap allocations during runtime.
- **Best practice** : Use generics judiciously---prioritize them for architectural clarity rather than broad, indiscriminate application. Where performance is critical, favor concrete types or interface-based polymorphism. For reflection, cache results such as `MethodInfo` or `FieldInfo` during initialization instead of querying them in the update loop.

### 6. Avoid leaked managed shells

Every `UnityEngine.Object`, such as `MonoBehaviour`, `Texture`, or `GameObject`,
has a C# "Managed Shell" wrapper that communicates with the native C++ engine.

- **The issue**: If a Managed Shell is held in memory by a static reference, a persistent event subscription, or an uncleaned closure, the GC can't reclaim the memory. Even if the native object is destroyed, the managed wrapper persists, leading to "ghost" memory leaks that bloat the Managed Heap.
- **Resolution** : Always implement robust cleanup patterns. When destroying objects or transitioning scenes, explicitly unsubscribe from events using the `-=` operator and nullify static references to `UnityEngine.Object` types. This cleanup ensures the GC can successfully collect the wrapper once the native engine has released its handle.