---
title: https://developer.android.com/topic/performance/memory/app-memory-budgets
url: https://developer.android.com/topic/performance/memory/app-memory-budgets
source: md.txt
---

> Documentation index: https://developer.android.com/topic/performance/memory/llms.txt

App memory budgets let your app set a soft limit on how much memory it keeps
resident. When your app goes over its budget, the system doesn't terminate it.
Instead, it reclaims memory that your app hasn't used recently, so your app
keeps its working set (the memory it actively needs for what the user is doing)
and returns the rest to the device.

Budgets are most useful when you know your app's working set and want to keep
its footprint in check, such as for system and bundled apps or for apps that
target memory-constrained devices.

> [!NOTE]
> **Note:** App memory budgets are supported starting in **Android 17 QPR2 (minor SDK
> release, API level 37.2)** . Test them using the [Android 17 QPR2
> Beta](https://developer.android.com/about/versions/17/qpr2) system images or the Android Emulator in Android Studio.

This page covers the following topics:

- [How memory budgets work](https://developer.android.com/topic/performance/memory/app-memory-budgets.md.txt#over-budget-behavior): learn what happens when your app goes over its budget.
- [Declare budgets in the Android manifest](https://developer.android.com/topic/performance/memory/app-memory-budgets.md.txt#declare-budgets-manifest): set steady-state budgets for each process state. This is the recommended approach.
- [Runtime APIs](https://developer.android.com/topic/performance/memory/app-memory-budgets.md.txt#runtime-apis): query usage, tighten budgets at run time, and listen for memory pressure from Kotlin or Java.
- [Calibrate, test, and release budgets](https://developer.android.com/topic/performance/memory/app-memory-budgets.md.txt#calibrate-test-release): find the right budget for your app, test it, and release it in stages.

## How memory budgets work

The budget is kept balanced by using [memory eviction and swap](https://developer.android.com/topic/performance/memory/guide/reclaim.md.txt) to
remove memory pages that weren't recently used, focusing the app's memory
footprint on its current working set. When an app exceeds its declared budget,
the operating system targets reclaim specifically at that app:

1. **Clean file-backed pages** (such as inactive code and mapped assets) are evicted first because they can be re-read from storage if needed.
2. **Dirty file-backed pages** are written back to storage and evicted.
3. **Anonymous memory pages** (such as heap allocations) are compressed and swapped to zRAM.

Reclaim makes room for new allocations and keeps your app's memory use within
its budget.

As long as there is headroom between what the app needs at any given time (its
working set) and the set budget, the app continues to run normally. If an app
sets a budget that is smaller than its working set, the app's performance at
runtime can slow down as a result.

To learn how the OS tracks and reclaims memory, see the
[memory architecture guide](https://developer.android.com/topic/performance/memory/guide.md.txt):

- [Memory reclaim and swap](https://developer.android.com/topic/performance/memory/guide/reclaim.md.txt): Explains how the OS charges private anonymous heap and file-backed pages to your app and reclaims cold pages when over budget.
- [Fundamental concepts](https://developer.android.com/topic/performance/memory/guide/concepts.md.txt): Explains why shared [Zygote
  memory](https://developer.android.com/topic/performance/memory/guide/concepts#zygote-process-model) is excluded from your app's budget and how resident budgets relate to [anonymous RSS + swap](https://developer.android.com/topic/performance/memory/guide/concepts.md.txt#rss-pss-uss) in field telemetry.
- [Bitmaps and memory](https://developer.android.com/topic/performance/memory/guide/bitmaps.md.txt): Explains how GPU-backed [hardware
  bitmaps](https://developer.android.com/topic/performance/memory/guide/bitmaps#hardware-bitmaps) and [DMA-BUF allocations](https://developer.android.com/topic/performance/memory/guide/bitmaps.md.txt#system-app-challenges) are accounted outside your app's heap and memory budget.

> [!NOTE]
> **Note:** App memory budgets are distinct from the platform's system-wide [app memory limits](https://developer.android.com/about/versions/17/behavior-changes-all.md.txt#app-memory-limits) ([Memory Limiter](https://source.android.com/docs/core/perf/memory-limiter#standard-platform-limits)), which enforce much higher device-RAM ceilings (such as 2 GB in the foreground and 1 GB in the background on 4 GB devices) to terminate processes with runaway memory leaks.

## Declare budgets in the Android manifest

Use `AndroidManifest.xml` to declare your steady-state memory budgets,
which are the baseline budgets at which your app operates during normal use.
Manifest declarations require no runtime code, take effect upon process
startup, and switch budgets across `foreground`, `perceptible`, and
`background` states. [`PackageManager.getMemoryBudgets`](https://developer.android.com/reference/android/content/pm/PackageManager.md.txt#getMemoryBudgets(android.content.pm.ApplicationInfo)) exposes
static `<application>` budget declarations. To test budgets and release them
with remote rollback before committing them to your manifest, see
[Calibrate, test, and release budgets](https://developer.android.com/topic/performance/memory/app-memory-budgets.md.txt#calibrate-test-release).

`<memory-budget>` declarations take effect on devices running Android 17 QPR2
(API level 37.2) and higher. On lower Android versions, the platform manifest
parser ignores unrecognized XML elements, so you can adopt `<memory-budget>`
without affecting backward compatibility.

> [!NOTE]
> **Note:** Apply `<memory-budget>` declarations only to release (optimized) builds. Unoptimized debug builds carry additional code instrumentation, logging, and debugger allocations that use significantly more memory, which can lead to frequent swap churn and test failures.

### Configure your build

You don't need to raise `minSdk` or `targetSdk` to adopt app memory budgets.
Declaring per-process budgets inside `<processes>` requires Android Gradle
plugin 9.5.0 or higher. To compile `<memory-budget>` manifest attributes,
[`MemoryBudgetManager`](https://developer.android.com/reference/android/app/MemoryBudgetManager.md.txt), and
`Build.VERSION_CODES_FULL.CINNAMON_BUN_2`, set `compileSdk` to API level 37
with `minorApiLevel = 2` in your module's `build.gradle.kts` or `build.gradle`
file:

### Kotlin

```kotlin
android {
    compileSdk {
        version = release(37) {
            minorApiLevel = 2
        }
    }
}
```

### Groovy

```groovy
android {
    compileSdk {
        version = release(37) {
            it.minorApiLevel = 2
        }
    }
}
```

### Declare a baseline budget

For most apps, defining a single budget for the application is all that is
needed. Declare a `<memory-budget>` element directly inside the `<application>`
tag:

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.simpleapp">

    <application
        android:label="@string/app_name">

        <!-- Baseline budget for the application -->
        <memory-budget android:maxMb="256" />

    </application>
</manifest>
```

This sets a 256MB resident memory budget across all processes and states for
the package. When the app's memory footprint exceeds 256MB, the operating
system trims inactive memory pages using eviction and swap.

> [!NOTE]
> **Note:** A manifest budget can't exceed system memory limits. If a declared budget exceeds the device's system limit, the system limit is applied instead.

### Vary budgets by process state

An app requires different amounts of memory depending on its user visibility:

- **Foreground**: The process is hosting a visible Activity interacting with the user. This state typically has the largest footprint due to active UI and graphics.
- **Perceptible**: The process is perceptible to the user but doesn't host a visible window (for example, hosting a media playback foreground service, an active background download, turn-by-turn navigation, or an active input method).
- **Background**: The process is running background jobs, receivers, or data syncs. It is expected to maintain a minimal footprint.

You can declare multiple `<memory-budget>` clauses to match these states:

```xml
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
```

A foreground or omitted-state clause isn't required. If you declare only
`perceptible` or `background` clauses, higher-importance states such as
`foreground` remain unconstrained by an app budget. Omitting `android:state`
defaults to `foreground`, which cascades to `perceptible` and `background`
unless a later clause overrides those states. For details on clause ordering,
see [Resolution rule: last applicable clause takes effect](https://developer.android.com/topic/performance/memory/app-memory-budgets.md.txt#resolution-rule).

When sizing budgets for each state, target the active working set of that state
rather than the peak resident memory (RSS high-water mark):

- **Size `foreground` budgets for smooth frame rendering** : Give foreground UI enough headroom for its active working set so synchronous reclaim doesn't delay frame rendering. Suppose your app pairs an everyday UI with a memory-intensive workflow, such as a photo viewer with a high-resolution photo editor or a text messaging app with video calling. Run the memory-intensive activity in a [dedicated process](https://developer.android.com/guide/components/processes-and-threads.md.txt#Processes) so its allocations and loaded code are budgeted independently, and the system can terminate that process after it becomes cached when the user exits. For more information, see [Isolate memory-intensive
  workflows](https://developer.android.com/topic/performance/memory/app-memory-budgets#isolate-memory-intensive-workflows).
- **Size `background` budgets tightly for headless work** : High background RSS in field telemetry often reflects UI allocations retained after leaving the foreground (see [Co-locating a bound service with a memory-intensive
  UI](https://developer.android.com/topic/performance/memory/guide/service-bindings#colocated-service-ui) and [Release memory in response to
  events](https://developer.android.com/topic/performance/memory/manage-app-memory#release)) or one-time file reads during background indexing and syncs. Because headless background work has no frame deadlines, evicting one-time file cache pages and swapping inactive heap pages to zRAM when a background sync briefly allocates beyond its budget causes no user-visible jank while preventing background spikes from evicting the user's foreground app.

For a step-by-step workflow, see [Calibrate your budgets](https://developer.android.com/topic/performance/memory/app-memory-budgets.md.txt#calibrate-budgets).

#### How budget states map to process states

The platform maps manifest budget states to runtime process states based on
[`RunningAppProcessInfo.importance`](https://developer.android.com/reference/android/app/ActivityManager.RunningAppProcessInfo.md.txt), which
Activity Manager computes from both the process's own active components and any
incoming [service bindings](https://developer.android.com/topic/performance/memory/guide/service-bindings.md.txt#impact-service-bindings) or content provider
queries from other apps:

- **`foreground`**: Active, visible user interactions, such as hosting a resumed Activity, maintaining the top app state when the screen turns off, or hosting a service or content provider actively bound or queried by the top foreground app.
- **`perceptible`** : Workloads that are perceptible to the user without a visible window, such as active media playback, turn-by-turn navigation, camera or microphone capture, active background downloads, data sync foreground services, or services bound by a foreground client using flags such as [`BIND_NOT_FOREGROUND`](https://developer.android.com/reference/android/content/Context.md.txt#BIND_NOT_FOREGROUND) (see [Controlling
  inheritance with BIND flags](https://developer.android.com/topic/performance/memory/guide/service-bindings#controlling-inheritance-bind-flags)). While internal platform metrics might label some of these workloads `PROCESS_STATE_IMPORTANT_FOREGROUND`, that internal constant doesn't signify a visible window and is governed by the `perceptible` budget.
- **`background`**: Work that isn't immediately perceptible to the user, such as background jobs, alarms, and broadcast receivers.

The following table shows how runtime importance levels map to manifest states:

| Manifest `android:state` | Runtime importance (`RunningAppProcessInfo`) | Typical components |
|---|---|---|
| `foreground` | `IMPORTANCE_FOREGROUND` `IMPORTANCE_TOP_SLEEPING` | Resumed visible Activity, top app with screen locked, service or content provider bound by the top app |
| `perceptible` | `IMPORTANCE_FOREGROUND_SERVICE` `IMPORTANCE_VISIBLE` | Active media playback, navigation, downloads, or sync foreground services; service bound with foreground-service or visible flags |
| `background` | `IMPORTANCE_PERCEPTIBLE` `IMPORTANCE_CANT_SAVE_STATE` `IMPORTANCE_SERVICE` `IMPORTANCE_CACHED` | Background jobs, receivers, background sync, and cached processes |

For details on how client bindings elevate a service or provider host process
and how the process transitions back to `background` or `cached` after the
client unbinds or moves off-screen, see [Service bindings and process
states](https://developer.android.com/topic/performance/memory/guide/service-bindings).

When a process enters a cached state (`IMPORTANCE_CACHED`) with no active
components, the platform continues to enforce its `background` memory budget
alongside cached-process freezing and reclamation, keeping the process bounded
even if freezing or compaction doesn't occur.

#### Inspect your app's process state and budget

One way to inspect your app's active process state and importance during
development is by querying Activity Manager using ADB:

```bash
adb shell dumpsys activity processes <package-name>
```

The following abbreviated example shows the process record and OOM control
entries for an app running a foreground service:

```text
ACTIVITY MANAGER RUNNING PROCESSES (dumpsys activity processes)
  All known processes:
  *APP* UID 10123 ProcessRecord{edf056c 3919:com.example.app/u0a123}
    pid=3919
    oom adj: max=1001 curRaw=200 setRaw=200 cur=200 set=200
    curProcState=4 mRepProcState=4 setProcState=4 lastStateTime=-42s360ms
    hasStartedServices=true
    mHasForegroundServices=true forcingToImportant=null
...
  Process OOM control (48 total):
    Proc #22: prcp  F/S/FGS  ---NFU-TI  t: 0 3919:com.example.app/u0a123 (fg-service)
        oom: max=1001 curRaw=200 setRaw=200 cur=200 set=200
        state: cur=FGS  set=FGS  lastRss=0.00 lastCachedRss=0.00
```

In this output:

- `curProcState=4` and `state: cur=FGS` reflect that the process is in the foreground service state. If your app is hosting an active visible activity, this appears as `TOP`. If it is running an important foreground component (such as a download or sync), it appears as `IMPF`.
- In the Process OOM control table, `prcp` indicates that the process is evaluated under the perceptible priority tier, which corresponds to the `perceptible` budget.

To inspect your app's current resident memory usage:

```bash
adb shell dumpsys meminfo <package-name>
```

### Multi-process apps

If your application divides its work across multiple processes, configure
dedicated process budgets using the `<process>` tag inside `<processes>`.

For example, consider a streaming music app (`com.example.radio`):

1. **Main process** : Hosts the visible UI and the audio playback engine ([`MediaSessionService`](https://developer.android.com/reference/androidx/media3/session/MediaSessionService.md.txt) with a `mediaPlayback` foreground service). When visible, the process operates under the 180MB foreground budget. When the user leaves the app while music continues playing, the process enters the `perceptible` state, where a 64MB budget is sufficient for the playback engine and audio buffer.
2. **Sync process (`:sync`)** : Dedicated process running background metadata synchronization and download indexing. Because this process is only ever active in the background, you don't need to explicitly declare `state="background"`; a single budget applies.

```xml
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

        <processes>
            <!-- Dedicated background sync process -->
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
```

When you declare a `<processes>` block in your manifest, list `<process>`
entries only for the processes that declare a `<memory-budget>`. If you want to
budget only specific subprocesses while leaving the rest of the app at the
system limit for the device, you can omit the `<memory-budget>` elements
directly under `<application>`.

> [!NOTE]
> **Note:** Declaring per-process memory budgets in `<processes>` requires Android Gradle Plugin 9.5.0 (or 9.6.0-alpha01) or higher.

Memory use in any subprocess counts against both its process budget and the
enclosing package budget. A process experiences memory pressure at runtime if it
breaches either its process budget or the package budget, whichever threshold
is reached first.

#### Isolate memory-intensive workflows

Many apps combine frequent lightweight tasks with an occasional
memory-intensive workflow, such as browsing a photo gallery and editing a
high-resolution photo, or reading text conversations and running a video call.
Keeping both in the main process forces a difficult trade-off: a tight
`foreground` budget throttles the editor or video call, whereas a generous
`foreground` budget leaves everyday browsing and messaging with unneeded memory
slack.

When a memory-intensive workflow runs in its own activity, assign that activity
to a dedicated process using `android:process`, configure per-process budgets
inside `<processes>`, and omit package-level `<memory-budget>` elements directly
under `<application>`:

- **Independent static budgets** : Your main process keeps a tight steady-state budget for everyday browsing or messaging, whereas the `:editor` or `:call` process declares a separate higher budget without raising the main process ceiling. Because `<application>` budgets cap the combined memory of all processes in the package, omit `<memory-budget>` directly under `<application>` whenever a subprocess requires a larger budget than the main process.
- **Full code and runtime cleanup** : Loaded code and runtime metadata stay in a process for its lifetime, as explained in [App code is memory](https://developer.android.com/topic/performance/memory/guide/app-code.md.txt). Native `.so` shared libraries for image filters or real-time audio and video codecs stay mapped after they load, and the Android Runtime retains loaded classes, initialized `static` fields, and JIT code caches. Running the editor or video call in a dedicated process lets the operating system terminate that process after it becomes cached when the user exits and reclaim its code mappings, runtime state, and native allocator arenas.
- **Bounded memory leaks**: Complex rendering, editing, and real-time media pipelines can introduce Java or native memory leaks over time. Isolating those workflows in a dedicated process bounds the lifetime of any leaked allocations to that session instead of carrying them into your long-lived main process.

The following example shows a messaging app (`com.example.messaging`) that
budgets its default process tightly for text conversations and isolates video
calls in `:call`:

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.messaging">

    <application
        android:name=".MessagingApplication"
        android:label="@string/app_name">

        <!-- Omit package-level <memory-budget> under <application> so the
             tighter main-process ceiling doesn't cap the :call process. -->
        <processes>
            <!-- Default process: everyday text messaging UI and sync -->
            <process>
                <memory-budget android:maxMb="160" />
                <memory-budget
                    android:maxMb="48"
                    android:state="background" />
            </process>

            <!-- Dedicated process for real-time video calls -->
            <process android:process=":call">
                <memory-budget android:maxMb="320" />
                <memory-budget
                    android:maxMb="48"
                    android:state="background" />
            </process>
        </processes>

        <activity
            android:name=".MainActivity"
            android:exported="true" />

        <activity
            android:name=".call.VideoCallActivity"
            android:process=":call"
            android:exported="false" />

    </application>
</manifest>
```

Android instantiates your `Application` class in every process spawned for your
package. In Android 9 (API level 28) and higher, check
[`Application.getProcessName`](https://developer.android.com/reference/android/app/Application.md.txt#getProcessName()) in `Application.onCreate`
so your everyday UI process doesn't initialize video or editing libraries, and
your `:call` or `:editor` process initializes only what that workflow requires.
For more information, see [Keep background work alive with a lean
process](https://developer.android.com/topic/performance/memory/guide/process-splitting).

### Scale budgets for high-density displays

For apps whose memory footprint scales significantly with how many pixels there
are to draw at a time, such as a photo gallery app caching bitmaps sized to the
window, Android provides two alternative mechanisms to scale budgets dynamically
with display specifications:

- **Scale by display density bucket (`android:additionalMbPerDensity`)** : Adds
  megabytes proportionally to the square of the display's
  [density ratio](https://developer.android.com/guide/practices/screens_support.md.txt#density-independence) relative to `mdpi` (1.0x / 160 dpi),
  because 2D raster drawables and UI assets scale across both width and
  height:

  ```xml
  <!-- Baseline 180MB + 16MB multiplied by (density ratio)^2 -->
  <memory-budget
      android:maxMb="180"
      android:additionalMbPerDensity="16" />
  ```

  On an `mdpi` display (1.0x), the budget is
  180 + 16 × 1^2^ = 196 MB. On an `xxhdpi` display (3.0x),
  the budget scales to 180 + 16 × 3^2^ = 324 MB.
- **Scale by window pixel count**
  (`android:additionalBytesPerDisplayPixel`): Adds bytes per pixel in the
  active window bounds (`WindowMetrics.getBounds` width × height). This
  fits apps allocating full-window graphics surfaces, render buffers, or
  high-resolution photo caches where memory consumption scales directly with
  raw pixel count rather than UI density buckets:

  ```xml
  <!-- Baseline 128MB + 16 bytes per window pixel -->
  <!-- For example, a 4-byte RGBA full-window buffer with double or quadruple
       buffering -->
  <memory-budget
      android:maxMb="128"
      android:additionalBytesPerDisplayPixel="16" />
  ```

  On a full-screen 1080p window (1080 × 2400 ≈ 2.59M pixels),
  this adds 41,472,000 bytes (≈ 39.6 MB, where 1 MB =
  1,048,576 bytes) to the baseline budget. On a 1440p window
  (1440 × 3120 ≈ 4.49M pixels), it adds 71,884,800 bytes
  (≈ 68.6 MB).

These two attributes are alternatives. Choose the attribute that matches your
app's primary scaling factor, and avoid combining both in the same clause.

### Specialize for device form factors

When shipping an APK across phones, tablets, and Wear OS, use the
`android:feature` attribute to adjust budgets for different hardware targets.

On Wear OS watches, RAM is constrained, and the app's UI and feature set is
much simpler. You can declare a tighter budget specialized for the `watch`
feature:

```xml
<!-- General phone and tablet baseline -->
<memory-budget android:maxMb="180" />

<!-- Wear OS override: simpler UI and constrained hardware -->
<memory-budget
    android:maxMb="48"
    android:feature="watch" />
```

### Resolution rule: last applicable clause takes effect

When defining multiple `<memory-budget>` elements for an app or process, the
system evaluates them in the order they appear in the manifest and enforces the
*last applicable* budget clause.

An omitted `android:state` defaults to `foreground`, which also cascades to
`perceptible` and `background` unless overridden by a later clause for those
states. Order clauses from `foreground` (or omitted `android:state`) to
`perceptible` to `background`, and place `android:feature` overrides within the
matching state group so a trailing omitted-state override doesn't shadow earlier
`perceptible` or `background` clauses.

### XML attribute reference

All megabyte (MB) attributes use binary units (1 MB = 1,048,576 bytes)
and map to the Linux cgroup `memory.current` charge (which excludes shared
memory from the Zygote).

| Attribute | Format | Default | Description |
|---|---|---|---|
| `android:maxMb` | Integer (\> 0) | **Required** | The baseline resident memory budget limit in MB. |
| `android:state` | Enum | `foreground` | The process state this budget applies to: `foreground`, `perceptible`, or `background`. If omitted, defaults to `foreground` and cascades to `perceptible` and `background` unless overridden by a later clause. |
| `android:additionalMbPerDensity` | Integer (≥ 0) | `0` | Additional megabytes multiplied by the square of the [display density ratio](https://developer.android.com/guide/practices/screens_support.md.txt#density-independence) relative to `mdpi` (1.0x). |
| `android:additionalBytesPerDisplayPixel` | Integer (≥ 0) | `0` | Additional bytes allocated per window pixel (`WindowMetrics.getBounds` width × height), useful for surface buffers and bitmaps. |
| `android:feature` | String | Any | Restricts the clause to devices declaring specific hardware features: `watch`, `automotive`, or `leanback`. |

## Runtime APIs

Alongside declarative `<memory-budget>` manifest clauses, Android provides a
runtime SDK API for the following tasks:

- Validate candidate budgets behind remote configuration before committing them to `AndroidManifest.xml`, as described in [Release budgets in
  stages](https://developer.android.com/topic/performance/memory/app-memory-budgets#staged-rollout).
- Query live cgroup memory usage and effective budgets in-process.
- Tighten a process or package budget dynamically during lightweight tasks.
- Listen for over-budget events to trim caches when the operating system reclaims memory.

### Android SDK API (`MemoryBudgetManager`)

The [`MemoryBudgetManager`](https://developer.android.com/reference/android/app/MemoryBudgetManager.md.txt) system service is available to apps written
in Kotlin and Java starting in Android 17 QPR2 (minor SDK release, API level
37.2 / `Build.VERSION_CODES_FULL.CINNAMON_BUN_2`).

#### Retrieve the service

Before you access `MemoryBudgetManager`, check that the device runs
Android 17 QPR2 or higher by checking [`SDK_INT_FULL`](https://developer.android.com/reference/android/os/Build.VERSION.md.txt#SDK_INT_FULL). If
your app's `minSdk` is lower than 36, check [`SDK_INT`](https://developer.android.com/reference/android/os/Build.VERSION.md.txt#SDK_INT) first so
devices running Android 15 (API level 35) or lower don't throw
`NoSuchFieldError` when reading `SDK_INT_FULL`:

```kotlin
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.BAKLAVA &&
    Build.VERSION.SDK_INT_FULL >= Build.VERSION_CODES_FULL.CINNAMON_BUN_2
) {
    val budgetManager = context.getSystemService(MemoryBudgetManager::class.java)
}
```

#### Query usage and budgets

```kotlin
// Query current memory charged to this process and the package UID
val processUsageBytes = budgetManager.processCurrentUsageBytes
val packageUsageBytes = budgetManager.packageCurrentUsageBytes

// Query process-scope and package-scope limits (LIMIT_IS_DISABLED if unset)
val processBudgetBytes = budgetManager.processBudgetBytes
val packageBudgetBytes = budgetManager.packageBudgetBytes
```

#### Dynamically set or clear budgets

You can set a tighter budget at runtime to constrain memory during lightweight
tasks, or clear it when the task finishes:

```kotlin
// Set a tighter dynamic budget on the current process (for example, 96 MB)
try {
    budgetManager.processBudgetBytes = 96L * 1024L * 1024L
} catch (e: IllegalArgumentException) {
    // Thrown if the budget is <= 0 or exceeds a manifest or system limit.
    Log.e(TAG, "Requested budget exceeds manifest or system ceiling", e)
}

// Clear the dynamic process budget to restore the manifest limit (or unconstrained baseline)
budgetManager.clearProcessBudget()
```

> [!NOTE]
> **Note:** You can set runtime budgets without declaring a manifest budget, but declaring your app's steady-state budgets in the manifest is the recommended approach, as described in [Release budgets in stages](https://developer.android.com/topic/performance/memory/app-memory-budgets.md.txt#staged-rollout). If `<memory-budget>` clauses are declared in `AndroidManifest.xml`, a runtime budget can only tighten limits within the declared manifest ceilings, and in all cases a runtime budget can't exceed system memory limits. Passing zero, a negative value, or a budget that exceeds an applicable manifest or system limit throws an `IllegalArgumentException`.

Unlike `<memory-budget>` manifest clauses, which specify separate limits for
`foreground`, `perceptible`, and `background` states, a dynamic budget set
through `MemoryBudgetManager` applies a single runtime ceiling until your code
updates or clears it. If you use the runtime API to run field experiments or
manage state-specific limits, update or clear the dynamic budget across
lifecycle transitions, such as through
[`ProcessLifecycleOwner`](https://developer.android.com/reference/androidx/lifecycle/ProcessLifecycleOwner.md.txt) or activity lifecycle
callbacks, as shown in the [Adaptive image editor example](https://developer.android.com/topic/performance/memory/app-memory-budgets.md.txt#example-sdk).

#### Performance and idempotency

When working with `MemoryBudgetManager` at runtime, keep the following
characteristics in mind:

- **Idempotency** : All budget mutation APIs are idempotent. Calling `clearProcessBudget()` or `clearPackageBudget()` repeatedly or when no dynamic budget is active is a safe no-op. Similarly, setting `setProcessBudgetBytes()` or `setPackageBudgetBytes()` to the same value consecutively doesn't trigger redundant system reconfigurations.
- **Calling frequency**: Setting, updating, or clearing a budget makes a cross-process call to the system service to update the operating system memory controller for the process. While lightweight, it isn't completely free. Call these APIs during discrete lifecycle transitions and task milestones (such as entering or leaving an activity, starting or completing background processing, or handling speech requests), and avoid calling them in tight loops, audio processing threads, or per-frame render routines.
- **Query frequency** : The query properties `processCurrentUsageBytes`, `packageCurrentUsageBytes`, `processBudgetBytes`, and `packageBudgetBytes` read live cgroup limits and usage in-process through local native calls rather than calling the system service. Although these queries are fast, invoke them on demand (such as during task transitions or inside `OnOverBudgetListener` callbacks) rather than polling in tight loops.

#### Listen for over-budget pressure callbacks

Apps can register a listener to be notified when memory usage exceeds the
budget threshold. The listener lets the app perform proactive cleanup, such as
clearing in-memory bitmap caches, when the operating system reclaims memory to
keep the process or package within its budget.

If the callback acquires locks, performs I/O, or collects process memory
snapshots, don't register an over-budget listener on `Looper.getMainLooper` or
pass `null` (which defaults to `Looper.getMainLooper`), because blocking the UI
thread can cause Application Not Responding (ANR) errors:

```kotlin
// Avoid: Passing null or Looper.getMainLooper() runs repeated callbacks on the
// UI thread. Background threads stalled in memory reclaim might hold locks in
// logging backends, dependency injection containers, or databases, causing UI
// freezes and ANR errors. Avoid capturing full-process /proc memory snapshots
// inside the callback when the process is already over budget.
budgetManager.registerProcessOverBudgetListener(Looper.getMainLooper()) { _ ->
    structuredLogger.logWarning("Over budget")
    telemetryRecorder.captureProcessMemorySnapshot()
}
```

Instead, dispatch over-budget callbacks on the `Looper` of a background
[`HandlerThread`](https://developer.android.com/reference/android/os/HandlerThread.md.txt):

```kotlin
val cleanupThread = HandlerThread("MemoryBudgetCleanup").apply { start() }

val listener = MemoryBudgetManager.OnOverBudgetListener { budgetBytes ->
    Log.w(TAG, "Process exceeded memory budget of $budgetBytes bytes")
    // Proactively evict thread-safe caches on the background Looper.
    imageTileCache.evictAll()
}

// Register on a background Looper before tightening a dynamic budget.
budgetManager.registerProcessOverBudgetListener(cleanupThread.looper, listener)

// When done, such as in onStop, unregister the listener.
budgetManager.unregisterProcessOverBudgetListener(listener)
```

> [!NOTE]
> **Note:** Over-budget callbacks only fire when an active budget is configured for the process or package (either declared using `<memory-budget>` in `AndroidManifest.xml` or set at runtime using `setProcessBudgetBytes` or `setPackageBudgetBytes`). If no manifest or runtime budget is active, `OnOverBudgetListener` won't be invoked.

Follow these recommendations for over-budget callbacks:

- **Use a background `Looper`** : Pass the `Looper` of a background `HandlerThread` to `registerProcessOverBudgetListener` and `registerPackageOverBudgetListener`. Don't pass `null` (which defaults to `Looper.getMainLooper`) or `Looper.getMainLooper` itself unless your callback updates only lock-free, main-thread UI state. When a process exceeds its budget, operating system memory reclaim can pause background threads that hold locks in logging frameworks, dependency injection containers, or databases. Acquiring locks or performing disk or Binder I/O on the main thread inside `onOverBudget` can then block the UI thread and cause ANR errors.
- **Expect repeated callbacks** : Over-budget callbacks aren't one-shot notifications. When usage exceeds the budget, the operating system reclaims cold pages first, and if pressure continues, the system keeps reclaiming memory and invoking your listener at most once every second. Make your callback idempotent. If your app only needs a single notification or wants a longer cooldown between cleanup passes, call `unregisterProcessOverBudgetListener` (or `unregisterPackageOverBudgetListener`) inside the callback, or guard your cleanup with a cooldown timestamp or [`AtomicBoolean`](https://developer.android.com/reference/java/util/concurrent/atomic/AtomicBoolean.md.txt).
- **Register before tightening a budget** : If current memory usage already exceeds a new budget when you call `setProcessBudgetBytes` or `setPackageBudgetBytes`, an over-budget event is triggered as soon as the new budget is applied. Register your listener before setting the budget so your app doesn't miss that initial over-budget notification.
- **Keep callbacks lock-free and lightweight** : Callbacks must provide immediate relief. Don't acquire contended locks, perform disk or Binder I/O, or capture full-process `/proc` memory snapshots inside `onOverBudget`, because repeated callbacks run when the process is already under memory pressure.
- **Avoid allocations**: Don't allocate new objects or start new threads inside the callback, because doing so can trigger immediate operating system direct reclaim.
- **Focus on high-yield targets**: Evicting large Bitmaps, render buffers, or closing memory-mapped files is much more effective than releasing many small objects.

### Runtime API example

The following example demonstrates how to implement the runtime API using the
Android SDK API in Kotlin:

#### Android SDK example: Adaptive image editor

When a memory-intensive workflow such as a photo editor or video call runs in
its own activity, prefer isolating it in a dedicated process. That lets the
system enforce your smaller everyday `<process>` budget from startup without
runtime mode tracking and terminate the workflow process after it becomes
cached when the user exits, reclaiming its loaded code, runtime metadata, and
any leaked allocations. For more information, see [Isolate memory-intensive
workflows](https://developer.android.com/topic/performance/memory/app-memory-budgets#isolate-memory-intensive-workflows).

When a lightweight mode and a memory-intensive mode share a single process,
remember that `setProcessBudgetBytes` can only tighten limits under your
manifest ceiling and can't raise them. Declare the memory-intensive mode's
ceiling in `AndroidManifest.xml`, call `setProcessBudgetBytes` to enforce the
tighter everyday budget, and call `clearProcessBudget` when entering the
memory-intensive mode. The higher manifest ceiling applies until your code calls
`setProcessBudgetBytes` and is the static `<application>` value returned by
[`PackageManager.getMemoryBudgets`](https://developer.android.com/reference/android/content/pm/PackageManager.md.txt#getMemoryBudgets(android.content.pm.ApplicationInfo)). Your app is also
responsible for tracking mode and lifecycle transitions across back stacks,
picture-in-picture windows, and activity restarts so the tighter budget is
reapplied whenever the memory-intensive mode ends.

This example shows an image editing app (`com.example.imageeditor`) whose
manifest declares a 256 MB ceiling to accommodate its multi-layer canvas:

```xml
<manifest ... >
    <application ... >
        <!-- Manifest ceiling accommodates the heaviest editing workload -->
        <memory-budget android:maxMb="256" />
    </application>
</manifest>
```

When the user is browsing the lightweight thumbnail gallery, the app uses the
Android SDK API in Kotlin to dynamically tighten its process budget to 96MB.
When the user opens the multi-layer editing canvas, the app clears the dynamic
budget to restore the full 256MB manifest ceiling. It also registers an
`OnOverBudgetListener` on a background [`HandlerThread`](https://developer.android.com/reference/android/os/HandlerThread.md.txt)
`Looper` before applying the gallery budget to evict cached preview bitmaps
under pressure without blocking the UI thread.

```kotlin
package com.example.imageeditor.ui

import android.app.Activity
import android.app.MemoryBudgetManager
import android.graphics.Bitmap
import android.os.Bundle
import android.os.HandlerThread
import android.util.Log
import android.util.LruCache

class ImageEditorActivity : Activity() {

    private lateinit var budgetManager: MemoryBudgetManager
    private lateinit var cleanupThread: HandlerThread

    // Thread-safe in-memory cache for rendered preview tiles (32MB limit)
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
        cleanupThread = HandlerThread("MemoryBudgetCleanup").apply { start() }
    }

    override fun onStart() {
        super.onStart()
        // Register listener on a background Looper before tightening the budget
        budgetManager.registerProcessOverBudgetListener(cleanupThread.looper, overBudgetListener)
        // Constrain memory during lightweight gallery browsing
        applyGalleryBudget()
    }

    override fun onStop() {
        super.onStop()
        budgetManager.unregisterProcessOverBudgetListener(overBudgetListener)
        // Clear the activity-scoped gallery budget when leaving the activity.
        budgetManager.clearProcessBudget()
    }

    override fun onDestroy() {
        cleanupThread.quitSafely()
        super.onDestroy()
    }

    /**
     * Called when the user enters the high-resolution editing canvas.
     * Clears the dynamic budget, restoring the full 256MB manifest ceiling.
     */
    fun enterEditingCanvas() {
        // Clear the tighter dynamic budget to restore the full manifest ceiling (256MB)
        budgetManager.clearProcessBudget()
        Log.i(TAG, "Restored manifest budget ceiling (256MB) for editing canvas")
    }

    /**
     * Called when the user exits the editor back to the thumbnail gallery.
     * Re-applies the tighter dynamic budget.
     */
    fun exitToGallery() {
        previewCache.trimToSize(8 * 1024 * 1024)
        applyGalleryBudget()
    }

    private fun applyGalleryBudget() {
        try {
            // Dynamically tighten budget to 96MB for the lightweight gallery view
            budgetManager.processBudgetBytes = 96L * 1024L * 1024L
            Log.i(TAG, "Tighter dynamic budget applied for gallery: 96MB")
        } catch (e: IllegalArgumentException) {
            Log.e(TAG, "Could not apply dynamic budget", e)
        }
    }

    companion object {
        private const val TAG = "ImageEditor"
    }
}
```

## Calibrate, test, and release budgets

Correctly implementing a memory budget takes three steps:

1. [Calibrate the budget](https://developer.android.com/topic/performance/memory/app-memory-budgets.md.txt#calibrate-budgets) for each process state.
2. [Test it thoroughly](https://developer.android.com/topic/performance/memory/app-memory-budgets.md.txt#test-budgets) before you release it.
3. [Release it in stages](https://developer.android.com/topic/performance/memory/app-memory-budgets.md.txt#staged-rollout): validate it behind remote configuration, graduate it to your manifest, and keep measuring.

### Calibrate your budgets

A good budget sits just above your app's working set for a given state, not at
its unconstrained peak. To find that point, run a realistic user flow, lower
the budget step by step, and watch for the moment your app starts paying for
it.

> [!NOTE]
> **Note:** If you're a device manufacturer or platform engineer calibrating preinstalled apps, see [Calibrate app memory budgets automatically](https://source.android.com/docs/core/perf/app-memory-budgets) to automate working-set sweeps and size `<memory-budget>` declarations across process states and display sizes.

#### Understand working set versus resident memory

Without a budget, your app's resident footprint (`memory.current`) holds two
kinds of memory:

- **The working set**: the Java, Kotlin, and native heap and the hot file-backed pages (DEX code, native libraries, and assets) that the current user flow touches over and over
- **Cold slack**: bitmap caches from earlier screens, one-time startup buffers, heap slack left over after an allocation burst, and file pages that were read once and never touched again

A budget at your unconstrained peak never reclaims the cold slack. A budget
below your working set makes the kernel swap out heap pages and evict code
pages that your app immediately faults back in. These *working-set refaults*
cost CPU time and battery, and once they land on the UI thread, they cost
frames too.

What you're looking for is the *knee*: the lowest budget where reclaim removes
only cold slack, so refaults, CPU time, and frame times stay where they were
without a budget.

#### Prepare your test environment

Set up a repeatable test that behaves like production:

- Calibrate the same R8-optimized, non-debuggable release build that you ship. Debug builds use more memory, so a budget tuned on a debug build is too high for release.
- Test on a device or emulator running Android 17 QPR2 (API level 37.2) or higher. A `userdebug` build or an emulator image without Google Play is convenient when sampling cgroup files from `adb shell`, because reading an app's cgroup directory from the shell can require `adb root`. An app can read its own process cgroup usage in-process through `MemoryBudgetManager` even on production builds.
- Script a 30 to 60 second user flow with [Jetpack
  Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview), UI Automator, or `adb shell input`, once for each state that you plan to budget. An idle app tells you nothing about its working set.
  - **`foreground`**: scroll dense lists and media grids, move between your main destinations, open menus and dialogs, and run animations
  - **`perceptible`**: leave the visible window while perceptible work continues (for example, audio playback or a download), let it run for 10 to 15 seconds, and then return to the app
  - **`background`** : trigger a sync, a `WorkManager` job (for example, with `adb shell cmd jobscheduler run -f <package-name> <job-id>`), a started service, or a broadcast receiver while the app has no visible UI

Measure a `background` budget while the background work is actively running,
rather than while the process is idle in a cached state (`IMPORTANCE_CACHED`).
Even though the `background` budget remains in effect while cached, an idle
cached process isn't executing background work and doesn't reflect the working
set of your background jobs or receivers.

#### Measure your baseline

Start with runs that have no budget at all, so you know what normal looks like.
Use a build without `<memory-budget>` declarations, and start each run from a
fresh process (`adb shell am force-stop <package-name>`).

Each app process has its own cgroup v2 memory controller. Look up its path from
the `0::` line of `/proc/<PID>/cgroup` instead of hardcoding the path. Pass each
device command to `adb shell` as a single quoted string so that the device
shell sees the quotes:

```bash
PID=$(adb shell pidof -s <package-name>)
CG=/sys/fs/cgroup$(adb shell "sed -n 's/^0:://p' /proc/$PID/cgroup")
adb shell "cat $CG/memory.current $CG/memory.swap.current"
adb shell "grep -E '^(anon|file|workingset_refault_.*) ' $CG/memory.stat"
```

Reading these files is cheap and doesn't disturb your app, so you can sample
them every second during a run:

- **`memory.current`** : resident memory charged to the process, in bytes. This is the number that `<memory-budget>` limits.
- **`memory.swap.current`**: memory compressed into zRAM swap, in bytes
- **`anon` and `file` in `memory.stat`**: resident anonymous and file-backed memory, in bytes
- **`workingset_refault_anon` and `workingset_refault_file` in
  `memory.stat`**: running counts of swapped-out or evicted pages that your app needed again. These counters are your main sign that a budget is too tight.

If you get a permission error when reading an app's cgroup files from `adb
shell`, run `adb root` on a `userdebug` build or an emulator image without
Google Play, and then try again. On production `user` builds where `adb root`
isn't available, query `MemoryBudgetManager.processCurrentUsageBytes` from
inside your app, or use `adb shell dumpsys meminfo <package-name>` for a
coarser view.
In `App Summary`, `Java Heap`, `Native Heap`, and `Stack` are mostly anonymous
memory, and `Code` is file-backed. Software bitmaps count toward `Native Heap`
and your budget, while [hardware bitmaps](https://developer.android.com/topic/performance/memory/guide/bitmaps.md.txt#hardware-bitmaps) and `Graphics`
don't. Don't run `dumpsys meminfo` in a loop while you measure frame timing. It
forces a garbage collection in your app and walks all of its memory mappings,
which changes what you're trying to measure.

#### Sweep candidate budgets

You can try candidate budgets without rebuilding your app. Use
[`am memory-limiter manual`](https://source.android.com/docs/core/perf/memory-limiter#manual) to set a budget for a
running process, and `none` to remove it:

```bash
adb shell am memory-limiter manual <PID> 120MB
adb shell am memory-limiter manual <PID> none
```

A manual override lasts for the lifetime of that process instance, across
process state changes, so clear it or restart the process before you move on.
It also sets the process's hard limit (`memory.max`) to the same value, so a
candidate budget below your app's working set can get the process killed
instead of just slowing it down. Treat that as a failed budget.

You can also sweep from a benchmark build by reading a candidate value from an
instrumentation argument and setting
[`MemoryBudgetManager.processBudgetBytes`](https://developer.android.com/topic/performance/memory/app-memory-budgets.md.txt#set-clear-budget). A runtime budget
can only tighten a manifest budget, so sweep on a build without
`<memory-budget>` declarations. It also stays in force across process state
changes until you call `clearProcessBudget`.

Start at the highest `memory.current` from your baseline and step down 10 to
15 MB at a time. For each candidate budget:

1. Start a fresh process, drive it into the target state, and apply the budget.
2. Run the user flow once as a warm-up. Applying a budget evicts cold startup pages once, and you want to measure steady state rather than that transition.
3. Reset frame stats, and record the starting refault counters and the
   process CPU time (`utime` and `stime`, in clock ticks):

   ```bash
   adb shell dumpsys gfxinfo <package-name> reset
   adb shell "grep -E '^workingset_refault_(anon|file) ' $CG/memory.stat"
   adb shell "cut -d ' ' -f 14,15 /proc/$PID/stat"
   ```
4. Run the measured pass of your user flow.

5. Record `memory.current`, `anon`, `file`, the refault counters, and CPU time
   again, and collect frame stats. `dumpsys gfxinfo` can print the same stats
   more than once, so take the first match, which covers the whole app:

   ```bash
   adb shell "dumpsys gfxinfo <package-name>" | grep -m 1 'Janky frames:'
   adb shell "dumpsys gfxinfo <package-name>" | grep -m 1 '95th percentile'
   ```

Repeat each candidate at least three times, and interleave candidates rather
than running all repetitions of one candidate back to back. Compare each
result with the spread of your baseline runs, not with a single run.

#### Read the results

As the budget drops, your app goes through three regimes:

- **Above the knee** : `memory.current` follows the budget down by shedding cold `file` pages and idle heap. `anon` stays flat, refaults stay near baseline, and CPU time and frame times don't move. This is where you want to be.
- **Below the knee**: The cold pages are gone, so the kernel starts swapping out heap pages that your app still uses. Refaults jump by hundreds or thousands of pages per run and CPU time goes up. Frame times might barely move on an otherwise idle test device, but your app now spends CPU time and battery compressing and decompressing its own working set.
- **Well below the knee** : Reclaim and swap-in faults land on the UI thread and `RenderThread`, and jank, frame times, and warm resume times all go up.

Compared with your unconstrained baseline, a candidate budget passes if it
meets all of the following, which are a reasonable starting point:

- The process survives the run
- Refault deltas stay close to baseline
- Process CPU time rises by no more than 5%
- Janky frames rise by no more than 1 percentage point
- P95 frame time rises by no more than 3 ms
- Warm resume time (`TotalTime` from `adb shell am start -W`) rises by no more than 15%, for `perceptible` and `background` budgets

The knee is the lowest candidate budget that passes. For example, here's a
foreground sweep for a hypothetical app with a 138 MB unconstrained peak:

| Candidate budget | `memory.current` | `anon` | `file` | Refaults (pages) | P95 frame time | Regime |
|---|---|---|---|---|---|---|
| None | 138 MB | 75 MB | 63 MB | 0 | 10.5 ms | Baseline |
| 125 MB | 121 MB | 74 MB | 47 MB | 10 | 10.5 ms | Above the knee |
| 110 MB | 110 MB | 75 MB | 35 MB | 15 | 10.8 ms | Knee |
| 95 MB | 95 MB | 74 MB | 21 MB | 176 | 11.2 ms | Below the knee |
| 85 MB | 85 MB | 68 MB | 17 MB | 2,050 | 12.8 ms | Below the knee |
| 70 MB | 70 MB | 54 MB | 16 MB | 8,771 | 16.5 ms | Well below the knee |

#### Pick your budget

Set `android:maxMb` 10% to 20% above the knee, so that differences in user
data, locales, and allocation bursts don't push your app below it. In the
preceding example, the knee is at 110 MB, so 125 MB is a good choice.

Then install a release build with the new `<memory-budget>` declarations, run
your user flow again, and check that the pass criteria still hold. To confirm
the active budget at run time, query `MemoryBudgetManager.processBudgetBytes` or
`MemoryBudgetManager.packageBudgetBytes`.

#### Validate non-foreground budgets with a warm return

A tight `perceptible` or `background` budget can look fine while your app is in
that state and then cost you when the user comes back. Test the return trip
too:

1. Run the foreground flow, move the app into the target state, and apply the candidate budget with `am memory-limiter manual`.
2. Let the perceptible or background work run for 10 to 15 seconds.
3. Clear the override (`adb shell am memory-limiter manual <PID> none`), then immediately bring the app back with `adb shell am start -W` and record `TotalTime`. If you set the candidate through `MemoryBudgetManager` instead, call `clearProcessBudget` before the app returns.
4. Run a short foreground interaction and check refaults and frame stats against the pass criteria.

Pick the lowest budget that passes both while the app is in that state and on
the warm return, and add the same 10% to 20% headroom.

#### Calibrate display scaling

If you use `android:additionalBytesPerDisplayPixel`, find the foreground knee on
two displays with different resolutions, such as 1080 × 2400
(≈ 2.59M pixels) and 1440 × 3120 (≈ 4.49M pixels).
Divide the difference between the two knees, in bytes, by the difference in
pixel count to get `android:additionalBytesPerDisplayPixel`. Subtract that
per-pixel amount for the smaller display from its knee to get the
resolution-independent base, and add headroom to get `android:maxMb`.

### Test your budgets

Before you release a new or tighter budget, check the following:

- **Release builds** : Test the build you ship, as described in [Prepare your test environment](https://developer.android.com/topic/performance/memory/app-memory-budgets.md.txt#prepare-calibration).
- **Every budgeted state** : Run your foreground, perceptible, and background flows, and [validate the warm return](https://developer.android.com/topic/performance/memory/app-memory-budgets.md.txt#validate-warm-return) for each non-foreground budget.
- **Low-RAM devices**: Include at least one device from your lowest supported RAM tier.
- **Window sizes** : If you use `android:additionalBytesPerDisplayPixel`, test split-screen and resizable windows as well as full screen, because the scaled budget is computed from the app's window size.
- **Realistic data**: Test with large accounts, long lists, and many media items, and with the locales you ship in, because working sets grow with additional data.
- **Multi-process apps** : Exercise each process that has its own `<memory-budget>` clause.
- **Regression gates** : Run your existing [Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview.md.txt) startup and jank tests with and without the budget, and fail the test if the budgeted run regresses beyond the [pass criteria](https://developer.android.com/topic/performance/memory/app-memory-budgets.md.txt#three-regimes).

### Release budgets in stages

A runtime budget set through `MemoryBudgetManager` can only tighten limits
within your declared `<memory-budget>` manifest ceilings. It can't raise a
manifest budget at run time. Don't ship aggressive `<memory-budget>` values in
`AndroidManifest.xml` and plan to relax them from a server flag. Instead,
release new budgets in two phases:

1. **Validate behind remote configuration** : Ship your APK with a single generous `<memory-budget>` safety ceiling and no `perceptible` or `background` clauses (recommended), or without `<memory-budget>`. Gate candidate budgets behind your server-side experiment or remote configuration flag, and apply the target state's budget across lifecycle transitions, such as through [`ProcessLifecycleOwner`](https://developer.android.com/reference/androidx/lifecycle/ProcessLifecycleOwner.md.txt). Catch `IllegalArgumentException`, which is thrown when an experiment's runtime budget exceeds a static or window-scaled manifest ceiling or the system memory limit on a low-RAM device. In the `catch` block, call `clearProcessBudget` or `clearPackageBudget` so a tighter runtime budget from a previous state doesn't stay active. Compare experiment arms by device RAM tier on the metrics that budgets can move: frame timing, startup and warm resume time, CPU time, and battery.
2. **Graduate proven budgets to the manifest** : After field data shows that the candidate budgets meet your pass criteria across device RAM tiers, move your steady-state `foreground`, `perceptible`, and `background` budgets into `<memory-budget>` clauses. Release that version in stages and watch the same metrics.

During runtime validation, your remote configuration flag is your kill switch.
When you turn the flag off, newly started processes skip setting runtime
budgets, and calling `clearProcessBudget` or `clearPackageBudget` clears any
active runtime budget in a running process. Your app returns to its manifest
safety ceiling, or to no app budget if you declared none, with no app update.
Keep this flag in your own app and server configuration rather than relying on
the device or OS to turn budgets off.

Treat budgets set only at run time as a temporary rollout step. Manifest
budgets ship inside your signed APK and apply from process startup without app
code. You can also inspect them without running your app by calling
[`PackageManager.getMemoryBudgets`](https://developer.android.com/reference/android/content/pm/PackageManager.md.txt#getMemoryBudgets(android.content.pm.ApplicationInfo)), which reads only static
`<application>` declarations. Loosening a manifest budget later requires an app
update, but you can still run experiments that tighten budgets at run time
below the manifest ceiling.