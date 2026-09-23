---
title: https://developer.android.com/topic/performance/memory/app-memory-budgets
url: https://developer.android.com/topic/performance/memory/app-memory-budgets
source: md.txt
---

App memory budgets let apps declare a memory budget for themselves, which tells
the system to trim their memory use when the app uses more than its set
budget. This is especially useful for system and bundled apps or for apps
targeting memory-constrained devices, where the developer knows their expected
memory working set and wants to ensure their app doesn't use too much of the
system's shared RAM resources.

The budget is kept balanced by using [memory eviction and swap](https://developer.android.com/topic/performance/memory/guide/reclaim) to
remove memory pages that were not recently used, focusing the app's memory
footprint on its current working set. When an app exceeds its declared budget,
the operating system targets reclaim specifically at that app:

1. **Clean file-backed pages** (such as inactive code and mapped assets) are evicted first because they can be re-read from storage if needed.
2. **Dirty file-backed pages** are written back to storage and evicted.
3. **Anonymous memory pages** (such as heap allocations) are compressed and swapped to zRAM.

As long as the budget doesn't exceed the working set, the app will work well
while using no more memory than is in its set budget. The operating system
evicts unused memory and compresses inactive heap pages to swap so that memory
allocations remain bounded without terminating the process.

> [!NOTE]
> **Note:** App memory budgets and `<memory-budget>` declarations are supported starting in **Android 17 QPR2 (minor SDK release, API level 37.2)** . You'll want to test this feature using the [Android 17 QPR2 Beta](https://developer.android.com/about/versions/17/qpr2) system images or the Android Emulator in Android Studio.

> [!NOTE]
> **Note:** Apply `<memory-budget>` declarations only to release (optimized) builds. Unoptimized debug builds carry additional code instrumentation, logging, and debugger allocations that use significantly more memory, which can lead to frequent swap churn and test failures.

## Declare budgets in the Android manifest

Declaring your memory budgets in your `AndroidManifest.xml` is the primary and
recommended method for defining budgets. It requires no runtime code, takes
effect immediately upon process startup, and provides a clear contract for the
operating system.

`<memory-budget>` declarations take effect on devices running Android 17 QPR2
(API level 37.2) and higher. On lower Android versions, the platform manifest
parser safely ignores unrecognized XML elements, so you can adopt
`<memory-budget>` without affecting backward compatibility.

### Declare a baseline budget

For most apps, defining a single budget for the application is all that is
needed. Declare a `<memory-budget>` element directly inside the `<application>`
tag:

    <manifest xmlns:android="http://schemas.android.com/apk/res/android"
        package="com.example.simpleapp">

        <application
            android:label="@string/app_name">

            <!-- Baseline budget for the application -->
            <memory-budget android:maxMb="256" />

        </application>
    </manifest>

This sets a 256MB resident memory budget across all processes and states for
the package. When the app's memory footprint exceeds 256MB, the operating
system trims inactive memory pages using eviction and swap.

### Vary budgets by process state

An app requires different amounts of memory depending on its user visibility:

- **Foreground**: The process is hosting a visible Activity interacting with the user. This state typically has the largest footprint due to active UI and graphics.
- **Perceptible**: The process is perceptible to the user but doesn't host a visible window (for example, hosting a media playback foreground service, turn-by-turn navigation, or an active input method).
- **Background**: The process is running background jobs, receivers, or data syncs. It is expected to maintain a minimal footprint.

You can declare multiple `<memory-budget>` clauses to match these states:

    <manifest xmlns:android="http://schemas.android.com/apk/res/android"
        package="com.example.simpleapp">

        <application
            android:label="@string/app_name">

            <!-- Default budget for visible foreground UI -->
            <memory-budget android:maxMb="200" />

            <!-- Tighter budget when playing audio in background -->
            <memory-budget
                android:maxMb="120"
                android:state="perceptible" />

            <!-- Minimal budget when fully in background -->
            <memory-budget
                android:maxMb="48"
                android:state="background" />

        </application>
    </manifest>

You don't need to specify `android:state="foreground"` on the first clause. A
clause without `android:state` acts as the default fallback for all states. The
more restrictive clauses below it override the budget when the app transitions
into `perceptible` or `background` states.

### Multi-process apps

If your application divides its work across multiple processes, configure
dedicated process budgets using the `<process>` tag inside `<processes>`.

For example, consider a streaming music app (`com.example.radio`):

1. **Main process** : Hosts the visible UI and the audio playback engine ([`MediaSessionService`](https://developer.android.com/reference/androidx/media3/session/MediaSessionService) with a `mediaPlayback` foreground service). When visible, the process operates under the 180MB foreground budget. When the user leaves the app while music continues playing, the process enters the `perceptible` state, where a 64MB budget is sufficient for the playback engine and audio buffer.
2. **Sync process (`:sync`)** : Dedicated process running background metadata synchronization and download indexing. Because this process is only ever active in the background, you don't need to explicitly declare `state="background"`; a single budget applies.

    <manifest xmlns:android="http://schemas.android.com/apk/res/android"
        package="com.example.radio">

        <application
            android:label="@string/app_name">

            <!-- Package baseline: main process with UI and audio playback -->
            <memory-budget android:maxMb="180" />

            <!-- Tighter budget when audio plays in the background -->
            <memory-budget
                android:maxMb="64"
                android:state="perceptible" />

            <!-- Dedicated background sync process -->
            <processes>
                <process android:process=":sync">
                    <memory-budget android:maxMb="32" />
                </process>
            </processes>

            <service
                android:name=".playback.AudioPlayerService"
                android:foregroundServiceType="mediaPlayback"
                android:exported="false" />

            <service
                android:name=".sync.PlaylistSyncService"
                android:process=":sync"
                android:exported="false" />

        </application>
    </manifest>

Memory use in any subprocess counts against both its process budget and the
enclosing package budget. A process experiences memory pressure at runtime if it
breaches either its process budget or the package budget, whichever threshold
is reached first.

### Scale budgets for high-density displays

For applications whose memory footprint scales significantly with how many
pixels there are to draw on the display at once---such as a photo gallery app
caching bitmaps sized to the screen---Android provides two alternative mechanisms
to scale budgets dynamically with display specifications:

- **Scale by display density bucket (`android:additionalMbPerDensity`)** : Adds
  megabytes proportionally to the display's [density ratio](https://developer.android.com/guide/practices/screens_support#density-independence)
  relative to `mdpi` (1.0x / 160 dpi). This is suitable when memory use
  scales with UI density buckets, such as caching higher-resolution raster
  drawables or UI assets:

      <!-- Baseline 180MB + 16MB per 1.0x density ratio -->
      <memory-budget
          android:maxMb="180"
          android:additionalMbPerDensity="16" />

  On an `mdpi` display (1.0x), the budget is
  180 + 16 × 1 = 196 MB. On an `xxhdpi` display (3.0x), the
  budget scales to 180 + 16 × 3 = 228 MB.
- **Scale by physical display resolution**
  (`android:additionalBytesPerDisplayPixel`): Adds bytes directly per
  physical display pixel (Width × Height). This is ideal for
  applications allocating full-screen graphics surfaces, render buffers, or
  full-resolution photo caches where memory consumption scales directly with
  raw display pixel count rather than UI density buckets:

      <!-- Baseline 128MB + 16 bytes per physical display pixel -->
      <!-- For example, a 4-byte RGBA full-screen buffer with double or quadruple buffering -->
      <memory-budget
          android:maxMb="128"
          android:additionalBytesPerDisplayPixel="16" />

  On a 1080p display (1080 × 2400 ≈ 2.59M pixels), this
  adds ≈ 41.4 MB to the baseline budget. On a 1440p display
  (1440 × 3120 ≈ 4.49M pixels), it adds
  ≈ 71.8 MB.

These two attributes are alternatives. Choose the attribute that matches your
app's primary scaling factor, and avoid combining both in the same clause.

### Specialize for device form factors

When shipping an APK across phones, tablets, and Wear OS, use the
`android:feature` attribute to adjust budgets for different hardware targets.

On Wear OS watches, RAM is constrained, and the app's UI and feature set is
much simpler. You can declare a tighter budget specialized for the `watch`
feature:

    <!-- General phone and tablet baseline -->
    <memory-budget android:maxMb="180" />

    <!-- Wear OS override: simpler UI and constrained hardware -->
    <memory-budget
        android:maxMb="48"
        android:feature="watch" />

### Resolution rule: last applicable clause takes effect

When defining multiple `<memory-budget>` elements for an application or
process, the system evaluates them in the order they are declared in the
manifest. The **last applicable** budget clause is the one that is enforced.

Because the last applicable budget wins, ordering matters. Always place the
most general baseline budget first, followed by more specific overrides (such
as state-specific or hardware-specific clauses).

### XML attribute reference

All memory size attributes are expressed in Megabytes (MB) and map to Linux
cgroup `memory.current` charge (which excludes shared memory like the Zygote).

| Attribute | Format | Default | Description |
|---|---|---|---|
| `android:maxMb` | Integer (\> 0) | **Required** | The baseline resident memory budget limit in MB. |
| `android:state` | Enum | Any | The process state this budget applies to: `foreground`, `perceptible`, or `background`. |
| `android:additionalMbPerDensity` | Integer (≥ 0) | `0` | Additional Megabytes to add per unit of [display density ratio](https://developer.android.com/guide/practices/screens_support#density-independence) relative to `mdpi` (1.0x). |
| `android:additionalBytesPerDisplayPixel` | Integer (≥ 0) | `0` | Additional bytes allocated per physical display pixel (Width × Height), useful for surface buffers and bitmaps. |
| `android:feature` | String | Any | Restricts the clause to devices declaring specific hardware features: `watch`, `automotive`, or `leanback`. |

## Runtime APIs (secondary dynamic option)

Declaring budgets statically in `AndroidManifest.xml` is the preferred solution
for almost all apps. However, for applications with dynamic workloads or for
runtime experimentation, Android provides runtime SDK and NDK APIs as a
secondary option.

The runtime API lets you:

- Query current memory usage and effective budgets.
- Dynamically adjust your process budget downward.
- Listen for over-budget events to proactively trim caches before the operating system triggers direct reclaim.

### Android SDK API (`MemoryBudgetManager`)

The [`MemoryBudgetManager`](https://developer.android.com/reference/android/app/MemoryBudgetManager) system service is available to apps written
in Kotlin and Java starting in Android 17 QPR2 (minor SDK release, API level
37.2 / `Build.VERSION_CODES_FULL.CINNAMON_BUN_2`).

#### Retrieve the service

Before you access `MemoryBudgetManager`, check that the device isn't running
a lower version than Android 17 QPR2 by using `SDK_INT_FULL`:

    if (Build.VERSION.SDK_INT_FULL >= Build.VERSION_CODES_FULL.CINNAMON_BUN_2) {
        val budgetManager = context.getSystemService(MemoryBudgetManager::class.java)
    }

#### Query usage and budgets

    // Query current memory charged to this process and the package UID
    val processUsageBytes = budgetManager.processCurrentUsageBytes
    val packageUsageBytes = budgetManager.packageCurrentUsageBytes

    // Query effective budgets (returns LIMIT_IS_DISABLED if unconstrained)
    val processBudgetBytes = budgetManager.processBudgetBytes
    val packageBudgetBytes = budgetManager.packageBudgetBytes

#### Dynamically set or clear budgets

You can set a tighter budget at runtime to constrain memory during lightweight
tasks, or clear it when the task finishes:

    // Set a tighter dynamic budget on the current process (e.g., 96 MB)
    try {
        budgetManager.processBudgetBytes = 96L * 1024L * 1024L
    } catch (e: IllegalArgumentException) {
        // Thrown if the budget is <= 0 or exceeds the manifest-declared ceiling
        Log.e(TAG, "Requested budget exceeds manifest or system ceiling", e)
    }

    // Clear the dynamic process budget to restore the manifest limit
    budgetManager.clearProcessBudget()

> [!NOTE]
> **Note:** A runtime budget can't exceed the budget declared in your manifest or the system memory limit. Attempting to set a budget higher than the manifest limit throws an `IllegalArgumentException`.

#### Listen for over-budget pressure callbacks

Apps can register a listener to be notified when memory usage exceeds the
budget threshold. This allows the app to perform proactive application-level
cleanup (such as clearing in-memory bitmap caches) before the operating system
triggers direct reclaim latency:

    val listener = MemoryBudgetManager.OnOverBudgetListener { budgetBytes ->
        Log.w(TAG, "Process exceeded memory budget of $budgetBytes bytes")
        // Proactively evict caches to release memory
        imageTileCache.evictAll()
    }

    // Register on the main Looper
    budgetManager.registerProcessOverBudgetListener(mainLooper, listener)

    // When done (e.g., in onStop)
    budgetManager.unregisterProcessOverBudgetListener(listener)

**Best practices for over-budget callbacks:**

- **Be quick**: Reclaim operations must offer immediate relief. Complex computations during pressure worsen performance.
- **Avoid allocations**: Don't allocate new objects or start new threads inside the callback, as doing so can trigger immediate operating system direct reclaim.
- **Focus on high-yield targets**: Evicting large Bitmaps, render buffers, or closing memory-mapped files is much more effective than releasing many small objects.

### Native NDK API (`<android/memory_budget_manager.h>`)

Native apps can use the C NDK API exposed by `libandroid.so` starting in
Android 17 QPR2 (API level 37.2).

#### CMake configuration

    find_library(android-lib android)
    target_link_libraries(my_native_engine PRIVATE ${android-lib})

#### Include header and query usage

    #include <android/memory_budget_manager.h>

    // Query current memory usage
    int64_t process_usage = AMemoryBudgetManager_getProcessCurrentUsageBytes();
    int64_t package_usage = AMemoryBudgetManager_getPackageCurrentUsageBytes();

    // Query current budget
    int64_t process_budget = 0;
    AMemoryBudgetResult result = AMemoryBudgetManager_getProcessBudget(&process_budget);
    if (result == AMEMORY_BUDGET_RESULT_SUCCESS) {
        // Current budget available in process_budget
    } else if (result == AMEMORY_BUDGET_RESULT_LIMIT_IS_DISABLED) {
        // No budget is currently active
    }

#### Dynamically configure native budget

    // Set a tighter process budget (e.g. 160MB)
    AMemoryBudgetResult result = AMemoryBudgetManager_setProcessBudget(160LL * 1024 * 1024);
    if (result != AMEMORY_BUDGET_RESULT_SUCCESS) {
        const char* error_msg = AMemoryBudgetManager_resultToString(result);
        // Handle error (e.g. AMEMORY_BUDGET_RESULT_ERROR_EXCEEDS_MANIFEST_LIMIT)
    }

    // Clear the dynamic budget to resume manifest limits
    AMemoryBudgetManager_clearProcessBudget();

#### Monitor memory pressure events

The NDK provides two ways to monitor memory events:

1. **High-Level Watcher (`AMemoryBudgetManager_Watcher_create`)** : Monitors events on an `ALooper` with automatic debouncing.
2. **Low-Level File Descriptor** : `AMemoryBudgetManager_getProcessMemoryPressureFd` returns a native file descriptor that can be integrated directly into a custom `epoll` engine loop.

    void onMemoryPressure(int32_t event_mask, const AMemoryBudgetEvents* events, void* userdata) {
        // High-yield eviction of unused native textures or geometry caches
        purgeNativeTextureCaches();
    }

    // Register watcher on an ALooper with a 1000ms debounce interval
    AMemoryBudgetManagerWatcher* watcher = AMemoryBudgetManager_Watcher_create(
        looper,
        AMEMORY_BUDGET_MANAGER_EVENT_PROCESS,
        1000 /* debounce_ms */,
        &onMemoryPressure,
        NULL /* userdata */
    );

    // When done:
    AMemoryBudgetManager_Watcher_destroy(watcher);

## Runtime API examples

The following examples demonstrate how to implement the runtime APIs using the
Android SDK API (written in Kotlin) and the Native NDK API (written in C++).

### Android SDK example: Adaptive image editor

This example shows an image editing app (`com.example.imageeditor`) using the
Android SDK API in Kotlin to dynamically raise its memory budget when the user
opens a multi-layer editing canvas, and clear the dynamic budget when returning
to the thumbnail gallery view. It also registers an `OnOverBudgetListener` to
evict cached preview bitmaps under pressure.

    package com.example.imageeditor.ui

    import android.app.Activity
    import android.app.MemoryBudgetManager
    import android.graphics.Bitmap
    import android.os.Bundle
    import android.util.Log
    import android.util.LruCache

    class ImageEditorActivity : Activity() {

        private lateinit var budgetManager: MemoryBudgetManager

        // In-memory cache for rendered preview tiles (32MB limit)
        private val previewCache = object : LruCache<String, Bitmap>(32 * 1024 * 1024) {
            override fun sizeOf(key: String, value: Bitmap): Int = value.byteCount
        }

        private val overBudgetListener = MemoryBudgetManager.OnOverBudgetListener { budgetBytes ->
            Log.w(TAG, "Process memory pressure detected (budget: ${budgetBytes / 1048576}MB). Evicting preview cache.")
            previewCache.evictAll()
        }

        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            budgetManager = getSystemService(MemoryBudgetManager::class.java)
        }

        override fun onStart() {
            super.onStart()
            // Register listener for process-level memory breaches
            budgetManager.registerProcessOverBudgetListener(mainLooper, overBudgetListener)
        }

        override fun onStop() {
            super.onStop()
            budgetManager.unregisterProcessOverBudgetListener(overBudgetListener)
        }

        /**
         * Called when the user enters the high-resolution editing canvas.
         */
        fun enterEditingCanvas() {
            try {
                // Dynamically set budget to 256MB for the editing canvas
                budgetManager.processBudgetBytes = 256L * 1024L * 1024L
                Log.i(TAG, "Dynamic budget applied: 256MB")
            } catch (e: IllegalArgumentException) {
                Log.e(TAG, "Could not apply dynamic budget", e)
            }
        }

        /**
         * Called when the user exits the editor back to the thumbnail gallery.
         */
        fun exitToGallery() {
            previewCache.trimToSize(8 * 1024 * 1024)
            // Clear dynamic budget; restores the baseline manifest budget
            budgetManager.clearProcessBudget()
        }

        companion object {
            private const val TAG = "ImageEditor"
        }
    }

### NDK C++ example: Native 3D engine

This example shows a native C++ game engine managing memory budgets based on the
active graphics quality level, using `AMemoryBudgetManager_Watcher_create` on an
`ALooper` to unload texture mipmaps when over budget.

    #include <android/memory_budget_manager.h>
    #include <android/looper.h>
    #include <android/log.h>

    #define LOG_TAG "Native3DEngineMemory"
    #define LOGI(...) __android_log_print(ANDROID_LOG_INFO, LOG_TAG, __VA_ARGS__)
    #define LOGW(...) __android_log_print(ANDROID_LOG_WARN, LOG_TAG, __VA_ARGS__)

    class MemoryGovernor {
    public:
        MemoryGovernor() : mWatcher(nullptr) {}

        ~MemoryGovernor() {
            stopMonitoring();
        }

        // Configures process budget based on user graphics quality settings
        bool setQualityBudget(int qualityLevel) {
            int64_t targetBytes = 0;
            switch (qualityLevel) {
                case 0: // Low (budget: 128MB)
                    targetBytes = 128LL * 1024 * 1024;
                    break;
                case 1: // Medium (budget: 256MB)
                    targetBytes = 256LL * 1024 * 1024;
                    break;
                case 2: // High (budget: 512MB)
                    targetBytes = 512LL * 1024 * 1024;
                    break;
                default:
                    // Clear dynamic override and restore manifest limit
                    AMemoryBudgetManager_clearProcessBudget();
                    return true;
            }

            AMemoryBudgetResult result = AMemoryBudgetManager_setProcessBudget(targetBytes);
            if (result != AMEMORY_BUDGET_RESULT_SUCCESS) {
                LOGW("Could not set quality budget: %s", AMemoryBudgetManager_resultToString(result));
                return false;
            }
            return true;
        }

        bool startMonitoring(ALooper* looper) {
            if (!looper) return false;

            // Monitor process budget events, debounced to at most once every 1000ms
            mWatcher = AMemoryBudgetManager_Watcher_create(
                looper,
                AMEMORY_BUDGET_MANAGER_EVENT_PROCESS,
                1000,
                &MemoryGovernor::onPressureEvent,
                this
            );
            return mWatcher != nullptr;
        }

        void stopMonitoring() {
            if (mWatcher) {
                AMemoryBudgetManager_Watcher_destroy(mWatcher);
                mWatcher = nullptr;
            }
        }

        void unloadUnusedTextures() {
            LOGW("Memory pressure callback triggered. Purging cached texture mipmaps...");
            // Fast, high-yield eviction without allocating memory
        }

    private:
        static void onPressureEvent(
            int32_t event_mask,
            const AMemoryBudgetEvents* events,
            void* userdata
        ) {
            auto* governor = static_cast<MemoryGovernor*>(userdata);
            governor->unloadUnusedTextures();
        }

        AMemoryBudgetManagerWatcher* mWatcher;
    };