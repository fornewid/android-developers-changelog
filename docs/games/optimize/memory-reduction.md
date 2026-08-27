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

## Reduce memory in Unreal Engine

In Unreal Engine, high-fidelity rendering pipelines and complex object
dependency graphs can significantly drive up both anonymous RSS and file-backed
memory pressure. In particular, relying on hard references and deep Blueprint
inheritance hierarchies forces unused connected assets to be loaded into memory.
Furthermore, excessive shader permutations, unoptimized texture streaming pools,
and uncompressed ELF relocation tables contribute to high baseline memory
footprints, increasing the risk of low memory killer (LMK) terminations.

Therefore, Unreal Engine memory optimization must be approached through three
core pillars tailored to these engine behaviors:

- Decouple data and logic, replacing hard or strong references with soft or weak references.
- Strip unused mobile lighting features and permutation options to minimize pipeline state objects (PSOs) and redundant render targets, while applying ASTC compression and customizing texture streaming pools with device profiles.
- Enable RELR and APS Relocation Table Compression to shrink the ELF binary size and reduce the runtime physical memory footprint.

For more information, see [Unreal memory optimization](https://developer.android.com/games/engines/unreal/unreal-reduce-memory).

## Multi-process optimization

Memory usage of cached processes is excluded from memory limits accounting
because it has no impact on active apps. Running the service in a separate
isolated process helps the main process transition to a cached state as quickly
as possible, thereby improving the health of your game.

For more information, see [How to track process state and memory](https://developer.android.com/topic/performance/memory/manage-app-memory#track), [How to
isolate a service process with Unity](https://developer.android.com/games/engines/unity/unity-perceptible-service), and [How to isolate a service process
with Unreal](https://developer.android.com/games/engines/unreal/unreal-perceptible-service).

## Reduce memory usage in user-perceived services

Your game might need to run logic in a user-perceived service for use cases like
completing a large download or for background voice chat systems. These
strategies can help you manage and reduce memory usage during these scenarios.

### Strategies for large downloads

These strategies might apply to large downloads that you want to continue even
after the user has minimized your game.

#### 1. Isolate the download process

**What:** Ensure that the OS can immediately reclaim memory your app isn't
using by performing the download in a separate process, since it's possible
the memory allocator may hold on to memory pool pages and keep Anonymous RSS
memory artificially high even after freeing arrays. When you terminate or exit
the service and process explicitly, the memory is returned to the OS pool and
your main process will remain unaffected.

- **In Unity:** Offload the download to a native Android `Service` declared
  with a process like `android:process=":downloader"` in a custom Manifest and
  invoke it with Unity's `AndroidJavaClass` JNI. Make sure to terminate the
  process when the download completes. See
  [Run a perceptible service in a separate process with Unity](https://developer.android.com/games/engines/unity/unity-perceptible-service) for more
  detailed guidance.

- **In Unreal:** Declare a custom Android `Service` with a process like
  `android:process=":downloader"` using Unreal Plugin Language, and trigger it
  with C++ JNI. Make sure to terminate the process when the download completes.
  See [Run a perceptible service in a separate process with Unreal](https://developer.android.com/games/engines/unreal/unreal-perceptible-service) for more
  detailed guidance.

- **For Native Android:** Declare a `Service` in the `AndroidManifest` with a
  process like `android:process=":downloader"`. Run the download in this
  isolated process, and call `Process.killProcess(Process.myPid())` when the
  download completes.

**How this helps:** Reduces the duration that memory is held, and allows the
download to continue while releasing memory used by the larger main process.

#### 2. Stream downloads directly to disk

**What:** Stream data directly from the network socket to the disk by using a
small, fixed-size reusable buffer rather than accumulating network responses
into a large array before writing it.

- **In Unity:** Avoid using [`DownloadHandlerBuffer`](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Networking.DownloadHandlerBuffer.html) for asset bundles or
  large files, since it allocates a native memory buffer equivalent to the file
  size (Anonymous RSS memory). Instead, use [`DownloadHandlerFile`](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Networking.DownloadHandlerFile.html) to stream
  bytes natively to disk on a background thread.

- **In Unreal:** Pipe incoming chunks of data directly into an `FArchive`
  (file-backed archive using Unreal's File Manager) with
  [`SetResponseBodyReceiveStream()`](https://dev.epicgames.com/documentation/unreal-engine/API/Runtime/HTTP/IHttpRequest/SetResponseBodyReceiveStream) rather than appending payloads from an
  [`IHttpRequest`](https://dev.epicgames.com/documentation/unreal-engine/API/Runtime/HTTP/IHttpRequest) into a `TArray<uint8>`.

- **For Native Android:** Pipe the [`InputStream`](https://developer.android.com/reference/java/io/InputStream) to a
  [`FileOutputStream`](https://developer.android.com/reference/java/io/FileOutputStream) using a pooled buffer rather than calling
  `.readBytes()` or `.string()` on an HTTP response.

**How this helps:** Reduces peak memory usage

#### 3. Stream downloaded file decompression

**What:** If your download is compressed, wrap your network input stream in a
streaming decompressor like [`ZipInputStream`](https://developer.android.com/reference/java/util/zip/ZipInputStream) rather than downloading the
file, loading it into RAM, and then extracting it.

**How this helps:** Reduces peak memory usage

#### 4. Delegate to the OS

**What:** To avoid managing background memory altogether, delegate the work to
Android's native APIs.

- [**`WorkManager`**](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started) is the modern, recommended wrapper around the
  OS-level `JobScheduler`. For Android 14+, `WorkManager` automatically handles
  user-triggered downloads as a User-Initiated Data Transfer (UIDT) job. This
  runs inside your app's process, so you must still stream directly to disk to
  minimize memory usage. UIDT protects your app from Low Memory crashes by
  allowing the OS to gracefully pause and resume your download if system
  resources become limited.

- [**`DownloadManager`**](https://developer.android.com/reference/android/app/DownloadManager) runs in a separate system process and doesn't
  attribute memory usage for the download to your app. Your app will receive a
  broadcast notification when the file is downloaded and ready.

  > [!NOTE]
  > **Note:** Make sure to choose an appropriate destination directory if your download needs to be kept private to the user or other apps.

**How this helps:** `WorkManager` helps deal with low memory scenarios, and
`DownloadManager` reduces your app's memory usage.

### Strategies for auxiliary services

These strategies might apply to auxiliary services that a game runs in parallel
with the main game process, such as background voice chat.

#### 1. Isolate the process

**What:** Decouple the feature, for example your voice chat solution, from the
main game engine. For example, you could run the microphone capture and
network streaming inside an Android foreground service assigned to a separate
process (declared in the Manifest, such as with `android:process=":voice"`).

**How this helps:** When the app is minimized, the heavy main game process can
drop into a lower-priority cached state while the lighter-weight auxiliary
service continues in user-perceived service state.

#### 2. Trim unused in-process memory

**What:** If the auxiliary service is too deeply integrated into the game
engine to separate, try to shed as much weight from the process as soon as the
game is backgrounded/minimized. Consider flushing texture caches, unloading
non-essential scenes, dropping the engine tick and render rates to 0, and
explicitly calling garbage collection.

- **In Unity:** Perform this trimming when [`OnApplicationPause()`](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/MonoBehaviour.OnApplicationPause.html) fires.
  [`Resources.UnloadUnusedAssets()`](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Resources.UnloadUnusedAssets.html) may be helpful.

- **In Unreal:** Bind trimming logic to the
  [`ApplicationWillEnterBackgroundDelegate`](https://dev.epicgames.com/documentation/unreal-engine/API/Runtime/Core/FCoreDelegates?application_version=5.8&lang=en-US#:%7E:text=ApplicationWillEnterBackgroundDelegate) delegate.

- **For Native Android:** Perform trimming in [`onPause()`](https://developer.android.com/guide/components/activities/activity-lifecycle#onpause) or
  [`onStop()`](https://developer.android.com/guide/components/activities/activity-lifecycle#onstop) as appropriate. The OS may try to call your implementation of
  [`onTrimMemory()`](https://developer.android.com/topic/performance/memory#release) before resorting to killing processes using high
  memory.

**How this helps:** Reduces memory usage that isn't needed when the game isn't
foregrounded.