---
title: https://developer.android.com/topic/performance/memory/app-memory-budgets
url: https://developer.android.com/topic/performance/memory/app-memory-budgets
source: md.txt
---

App memory budgets let apps declare a memory budget for themselves, which tells
the system to trim their memory use when the app uses more than its set
budget. This is especially useful for system and bundled apps or for apps
targeting memory-constrained devices, where the developer knows their expected
memory working set (the memory the app actively needs for what the user is
currently doing) and wants to ensure their app doesn't use too much of the
system's shared RAM resources.

The budget is kept balanced by using [memory eviction and swap](https://developer.android.com/topic/performance/memory/guide/reclaim) to
remove memory pages that weren't recently used, focusing the app's memory
footprint on its current working set. When an app exceeds its declared budget,
the operating system targets reclaim specifically at that app:

1. **Clean file-backed pages** (such as inactive code and mapped assets) are evicted first because they can be re-read from storage if needed.
2. **Dirty file-backed pages** are written back to storage and evicted.
3. **Anonymous memory pages** (such as heap allocations) are compressed and swapped to zRAM.

As long as the working set doesn't exceed the budget, the app will work well
while using no more memory than is in its set budget. The operating system
evicts unused memory and compresses inactive heap pages to swap so that memory
allocations remain bounded without terminating the process.

> [!NOTE]
> **Note:** App memory budgets and `<memory-budget>` declarations are supported starting in **Android 17 QPR2 (minor SDK release, API level 37.2)** . You'll want to test this feature using the [Android 17 QPR2 Beta](https://developer.android.com/about/versions/17/qpr2) system images or the Android Emulator in Android Studio.

> [!NOTE]
> **Note:** Apply `<memory-budget>` declarations only to release (optimized) builds. Unoptimized debug builds carry additional code instrumentation, logging, and debugger allocations that use significantly more memory, which can lead to frequent swap churn and test failures.

## What happens when an app exceeds its budget

Exceeding a memory budget doesn't cause the system to terminate or crash your
app. Instead, when an app uses more memory than its budget allows, the OS finds
memory that the app hasn't used in some time and safely puts it away until it's
needed again. This makes way for new app memory allocations and keeps the
overall app's memory use within budget.

As long as there is headroom between what the app needs at any given time (its
working set) and the set budget, the app continues to run normally. If an app
sets a budget that is smaller than its working set, the app's performance at
runtime can slow down as a result.

To learn how the OS tracks and reclaims memory, see the
[memory architecture guide](https://developer.android.com/topic/performance/memory/guide):

- [Memory reclaim and swap](https://developer.android.com/topic/performance/memory/guide/reclaim): Explains how the OS charges private anonymous heap and file-backed pages to your app and reclaims cold pages when over budget.
- [Fundamental concepts](https://developer.android.com/topic/performance/memory/guide/concepts): Explains why shared [Zygote
  memory](https://developer.android.com/topic/performance/memory/guide/concepts#zygote-process-model) is excluded from your app's budget and how resident budgets relate to [anonymous RSS + swap](https://developer.android.com/topic/performance/memory/guide/concepts#rss-pss-uss) in field telemetry.
- [Bitmaps and memory](https://developer.android.com/topic/performance/memory/guide/bitmaps): Explains how GPU-backed [hardware
  bitmaps](https://developer.android.com/topic/performance/memory/guide/bitmaps#hardware-bitmaps) and [DMA-BUF allocations](https://developer.android.com/topic/performance/memory/guide/bitmaps#system-app-challenges) are accounted outside your app's heap and memory budget.

> [!NOTE]
> **Note:** App memory budgets are distinct from the platform's system-wide [app memory limits](https://developer.android.com/about/versions/17/behavior-changes-all#app-memory-limits) ([Memory Limiter](https://source.android.com/docs/core/perf/memory-limiter#standard-platform-limits)), which enforce much higher device-RAM ceilings (such as 2 GB in the foreground and 1 GB in the background on 4 GB devices) to terminate processes with runaway memory leaks.

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

> [!NOTE]
> **Note:** A manifest budget can't exceed system memory limits. If a declared budget exceeds the device's system limit, the system limit is applied instead.

### Vary budgets by process state

An app requires different amounts of memory depending on its user visibility:

- **Foreground**: The process is hosting a visible Activity interacting with the user. This state typically has the largest footprint due to active UI and graphics.
- **Perceptible**: The process is perceptible to the user but doesn't host a visible window (for example, hosting a media playback foreground service, an active background download, turn-by-turn navigation, or an active input method).
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

A base clause without `android:state` isn't required; if you only specify
state-specific clauses (for example, `android:state="background"`), other states
remain unconstrained by an app budget. When included, a clause without
`android:state` acts as the default fallback for unspecified states (such as
foreground), which subsequent more restrictive clauses override when the app
transitions into `perceptible` or `background` states.

When sizing budgets for each state, target the active working set of that state
rather than the peak resident memory (RSS high-water mark):

- **Size `foreground` budgets for smooth frame rendering** : Give foreground UI enough headroom for its active working set so synchronous reclaim doesn't delay frame rendering. If your app includes a memory-intensive standalone workflow (such as a high-resolution image or video editor), consider moving that activity into a [dedicated process](https://developer.android.com/guide/components/processes-and-threads#Processes) (see [Multi-process apps](https://developer.android.com/topic/performance/memory/app-memory-budgets#multi-process-budgets)) so its allocations are budgeted independently and torn down when the user exits.
- **Size `background` budgets tightly for headless work** : High background RSS in field telemetry often reflects UI allocations retained after leaving the foreground (see [Co-locating a bound service with a memory-intensive
  UI](https://developer.android.com/topic/performance/memory/guide/service-bindings#colocated-service-ui) and [Release memory in response to
  events](https://developer.android.com/topic/performance/memory/manage-app-memory#release)) or one-time file reads during background indexing and syncs. Because headless background work has no frame deadlines, evicting one-time file cache pages and swapping inactive heap pages to zRAM when a background sync briefly allocates beyond its budget causes no user-visible jank while preventing background spikes from evicting the user's foreground app.

For a step-by-step workflow, see [Measure your working set and calibrate
budgets](https://developer.android.com/topic/performance/memory/app-memory-budgets#calibrate-budgets).

#### How budget states map to process states

The platform maps manifest budget states to runtime process states based on
[`RunningAppProcessInfo.importance`](https://developer.android.com/reference/android/app/ActivityManager.RunningAppProcessInfo), which
Activity Manager computes from both the process's own active components and any
incoming [service bindings](https://developer.android.com/topic/performance/memory/guide/service-bindings#impact-service-bindings) or content provider
queries from other apps:

- **`foreground`**: Active, visible user interactions, such as hosting a resumed Activity, maintaining the top app state when the screen turns off, or hosting a service or content provider actively bound or queried by the top foreground app.
- **`perceptible`** : Workloads that are perceptible to the user without a visible window, such as active media playback, turn-by-turn navigation, camera or microphone capture, active background downloads, data sync foreground services, or services bound by a foreground client using flags such as [`BIND_NOT_FOREGROUND`](https://developer.android.com/reference/android/content/Context#BIND_NOT_FOREGROUND) (see [Controlling
  inheritance with BIND flags](https://developer.android.com/topic/performance/memory/guide/service-bindings#controlling-inheritance-bind-flags)). While internal platform metrics might label some of these workloads `PROCESS_STATE_IMPORTANT_FOREGROUND`, that internal constant doesn't signify a visible window and is governed by the `perceptible` budget.
- **`background`**: Work that isn't immediately perceptible to the user, such as background jobs, alarms, and broadcast receivers.

The following table shows how runtime importance levels map to manifest states:

| Manifest `android:state` | Runtime importance (`RunningAppProcessInfo`) | Typical components |
|---|---|---|
| `foreground` | `IMPORTANCE_FOREGROUND` `IMPORTANCE_TOP_SLEEPING` | Resumed visible Activity, top app with screen locked, service or content provider bound by the top app |
| `perceptible` | `IMPORTANCE_FOREGROUND_SERVICE` `IMPORTANCE_VISIBLE` | Active media playback, navigation, downloads, or sync foreground services; service bound with foreground-service or visible flags |
| `background` | `IMPORTANCE_PERCEPTIBLE` `IMPORTANCE_CANT_SAVE_STATE` `IMPORTANCE_SERVICE` | Background jobs, receivers, background sync |

For details on how client bindings elevate a service or provider host process
and how the process transitions back to `background` or `cached` after the
client unbinds or moves off-screen, see [Service bindings and process
states](https://developer.android.com/topic/performance/memory/guide/service-bindings).

When a process enters a cached state (`IMPORTANCE_CACHED`) with no active
components, the platform releases its active memory budget and manages its
memory through standard cached-process reclamation.

#### Inspect your app's process state and budget

One way to inspect your app's active process state and importance during
development is by querying Activity Manager using ADB:

    adb shell dumpsys activity processes <package-name>

The following abbreviated example shows the process record and OOM control
entries for an app running a foreground service:

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

In this output:

- `curProcState=4` and `state: cur=FGS` reflect that the process is in the foreground service state. If your app is hosting an active visible activity, this appears as `TOP`. If it is running an important foreground component (such as a download or sync), it appears as `IMPF`.
- In the Process OOM control table, `prcp` indicates that the process is evaluated under the perceptible priority tier, which corresponds to the `perceptible` budget.

To inspect your app's current resident memory usage:

    adb shell dumpsys meminfo <package-name>

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

### Scale budgets for high-density displays

For applications whose memory footprint scales significantly with how many
pixels there are to draw on the display at once---such as a photo gallery app
caching bitmaps sized to the screen---Android provides two alternative mechanisms
to scale budgets dynamically with display specifications:

- **Scale by display density bucket (`android:additionalMbPerDensity`)** : Adds
  megabytes proportionally to the square of the display's
  [density ratio](https://developer.android.com/guide/practices/screens_support#density-independence) relative to `mdpi` (1.0x / 160 dpi),
  because 2D raster drawables and UI assets scale across both width and
  height:

      <!-- Baseline 180MB + 16MB multiplied by (density ratio)^2 -->
      <memory-budget
          android:maxMb="180"
          android:additionalMbPerDensity="16" />

  On an `mdpi` display (1.0x), the budget is
  180 + 16 × 1^2^ = 196 MB. On an `xxhdpi` display (3.0x),
  the budget scales to 180 + 16 × 3^2^ = 324 MB.
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

All memory size attributes are expressed in megabytes (MB) and map to Linux
cgroup `memory.current` charge (which excludes shared memory like the Zygote).

| Attribute | Format | Default | Description |
|---|---|---|---|
| `android:maxMb` | Integer (\> 0) | **Required** | The baseline resident memory budget limit in MB. |
| `android:state` | Enum | Any | The process state this budget applies to: `foreground`, `perceptible`, or `background`. If omitted, the clause acts as a fallback for any unspecified state. |
| `android:additionalMbPerDensity` | Integer (≥ 0) | `0` | Additional megabytes multiplied by the square of the [display density ratio](https://developer.android.com/guide/practices/screens_support#density-independence) relative to `mdpi` (1.0x). |
| `android:additionalBytesPerDisplayPixel` | Integer (≥ 0) | `0` | Additional bytes allocated per physical display pixel (Width × Height), useful for surface buffers and bitmaps. |
| `android:feature` | String | Any | Restricts the clause to devices declaring specific hardware features: `watch`, `automotive`, or `leanback`. |

## Measure your working set and calibrate budgets

A good budget sits just above your app's working set for a given state, not at
its unconstrained peak. To find that point, run a realistic user flow, lower
the budget step by step, and watch for the moment your app starts paying for
it.

### Understand working set versus resident memory

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

### Prepare your test environment

Set up a repeatable test that behaves like production:

- Calibrate the same R8-optimized, non-debuggable release build that you ship. Debug builds use more memory, so a budget tuned on a debug build is too high for release.
- Test on a device or emulator running Android 17 QPR2 (API level 37.2) or higher. A `userdebug` build or an emulator image without Google Play is best, because some devices only let you read the cgroup files in the following sections after you run `adb root`.
- Script a 30 to 60 second user flow with [Jetpack
  Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview), UI Automator, or `adb shell input`, once for each state that you plan to budget. An idle app tells you nothing about its working set.
  - **`foreground`**: scroll dense lists and media grids, move between your main destinations, open menus and dialogs, and run animations
  - **`perceptible`**: leave the visible window while perceptible work continues (for example, audio playback or a download), let it run for 10 to 15 seconds, and then return to the app
  - **`background`** : trigger a sync, a `WorkManager` job (for example, with `adb shell cmd jobscheduler run -f <package-name> <job-id>`), a started service, or a broadcast receiver while the app has no visible UI

Measure a `background` budget while the background work is running. Once the
process becomes cached, the platform releases its budget (see [How budget
states map to process states](https://developer.android.com/topic/performance/memory/app-memory-budgets#process-state-mapping)), so an idle cached
process doesn't tell you anything about your `background` budget.

### Measure your baseline

Start with runs that have no budget at all, so you know what normal looks like.
Use a build without `<memory-budget>` declarations, and start each run from a
fresh process (`adb shell am force-stop <package-name>`).

Each app process has its own cgroup v2 memory controller. Look up its path from
the `0::` line of `/proc/<PID>/cgroup` instead of building the path yourself,
because the cgroup layout can differ between devices. Pass each device command
to `adb shell` as a single quoted string so that the device shell sees the
quotes:

    PID=$(adb shell pidof -s <package-name>)
    CG=/sys/fs/cgroup$(adb shell "sed -n 's/^0:://p' /proc/$PID/cgroup")
    adb shell "cat $CG/memory.current $CG/memory.swap.current"
    adb shell "grep -E '^(anon|file|workingset_refault_.*) ' $CG/memory.stat"

Reading these files is cheap and doesn't disturb your app, so you can sample
them every second during a run:

- **`memory.current`** : resident memory charged to the process, in bytes. This is the number that `<memory-budget>` limits.
- **`memory.swap.current`**: memory compressed into zRAM swap, in bytes
- **`anon` and `file` in `memory.stat`**: resident anonymous and file-backed memory, in bytes
- **`workingset_refault_anon` and `workingset_refault_file` in
  `memory.stat`**: running counts of swapped-out or evicted pages that your app needed again. These counters are your main sign that a budget is too tight.

If you get a permission error, run `adb root` and try again. If you can't get
root, `adb shell dumpsys meminfo <package-name>` gives you a coarser view. In
`App Summary`, `Java Heap`, `Native Heap`, and `Stack` are mostly anonymous
memory, and `Code` is file-backed. Software bitmaps count toward `Native Heap`
and your budget, while [hardware bitmaps](https://developer.android.com/topic/performance/memory/guide/bitmaps#hardware-bitmaps) and `Graphics`
don't. Don't run `dumpsys meminfo` in a loop while you measure frame timing. It
forces a garbage collection in your app and walks all of its memory mappings,
which changes what you're trying to measure.

### Sweep candidate budgets

You can try candidate budgets without rebuilding your app. Use
[`am memory-limiter manual`](https://source.android.com/docs/core/perf/memory-limiter#manual) to set a budget for a
running process, and `none` to remove it:

    adb shell am memory-limiter manual <PID> 120MB
    adb shell am memory-limiter manual <PID> none

A manual override lasts for the lifetime of that process instance, across
process state changes, so clear it or restart the process before you move on.
It also sets the process's hard limit (`memory.max`) to the same value, so a
candidate budget below your app's working set can get the process killed
instead of just slowing it down. Treat that as a failed budget.

You can also sweep from a benchmark build by reading a candidate value from an
instrumentation argument and setting
[`MemoryBudgetManager.processBudgetBytes`](https://developer.android.com/topic/performance/memory/app-memory-budgets#set-clear-budget). A runtime budget
can only tighten a manifest budget, so sweep on a build without
`<memory-budget>` declarations. It also stays in force across process state
changes until you call `clearProcessBudget`.

Start at the highest `memory.current` from your baseline and step down 10 to
15 MB at a time. For each candidate budget:

1. Start a fresh process, drive it into the target state, and apply the budget.
2. Run the user flow once as a warm-up. Applying a budget evicts cold startup pages once, and you want to measure steady state rather than that transition.
3. Reset frame stats, and record the starting refault counters and the
   process CPU time (`utime` and `stime`, in clock ticks):

       adb shell dumpsys gfxinfo <package-name> reset
       adb shell "grep -E '^workingset_refault_(anon|file) ' $CG/memory.stat"
       adb shell "cut -d ' ' -f 14,15 /proc/$PID/stat"

4. Run the measured pass of your user flow.

5. Record `memory.current`, `anon`, `file`, the refault counters, and CPU time
   again, and collect frame stats. `dumpsys gfxinfo` can print the same stats
   more than once, so take the first match, which covers the whole app:

       adb shell "dumpsys gfxinfo <package-name>" | grep -m 1 'Janky frames:'
       adb shell "dumpsys gfxinfo <package-name>" | grep -m 1 '95th percentile'

Repeat each candidate at least three times, and interleave candidates rather
than running all repetitions of one candidate back to back. Compare each
result with the spread of your baseline runs, not with a single run.

### Read the results

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

### Pick your budget

Set `android:maxMb` 10% to 20% above the knee, so that differences in user
data, locales, and allocation bursts don't push your app below it. In the
preceding example, the knee is at 110 MB, so 125 MB is a good choice.

Then install a release build with the new `<memory-budget>` declarations, run
your user flow again, and check that the pass criteria still hold. `dumpsys
meminfo` shows the active budget and its source in its Memory Budget section.

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

Before you access `MemoryBudgetManager`, check that the device runs
Android 17 QPR2 or higher by checking [`SDK_INT_FULL`](https://developer.android.com/reference/android/os/Build.VERSION#SDK_INT_FULL). If
your app's `minSdk` is lower than 36, check [`SDK_INT`](https://developer.android.com/reference/android/os/Build.VERSION#SDK_INT) first so
devices running Android 15 (API level 35) or lower don't throw
`NoSuchFieldError` when reading `SDK_INT_FULL`:

    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.BAKLAVA &&
        Build.VERSION.SDK_INT_FULL >= Build.VERSION_CODES_FULL.CINNAMON_BUN_2
    ) {
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
        // Thrown if the budget is <= 0 or exceeds the manifest ceiling or system limit
        Log.e(TAG, "Requested budget exceeds manifest or system ceiling", e)
    }

    // Clear the dynamic process budget to restore the manifest limit (or unconstrained baseline)
    budgetManager.clearProcessBudget()

> [!NOTE]
> **Note:** Declaring a budget in the manifest isn't required to use runtime budgets. However, if a manifest budget is declared, a runtime budget can only tighten (reduce) memory limits within that manifest ceiling. In all cases, a runtime budget can't exceed system memory limits. Attempting to set a budget higher than the active ceiling throws an `IllegalArgumentException`.

Unlike `<memory-budget>` manifest clauses, which automatically switch budgets
whenever the process transitions between `foreground`, `perceptible`, and
`background` states, a dynamic budget set through `MemoryBudgetManager` applies
a single ceiling until your code updates or clears it. If you use the runtime
API to run field experiments or manage state-specific limits, update or clear
the dynamic budget across lifecycle transitions (for example, using
[`ProcessLifecycleOwner`](https://developer.android.com/reference/androidx/lifecycle/ProcessLifecycleOwner) or activity lifecycle
callbacks, as shown in the [Adaptive image editor example](https://developer.android.com/topic/performance/memory/app-memory-budgets#example-sdk)).

#### Performance and idempotency

When working with `MemoryBudgetManager` at runtime, keep the following
characteristics in mind:

- **Idempotency** : All budget mutation APIs are idempotent. Calling `clearProcessBudget()` or `clearPackageBudget()` repeatedly or when no dynamic budget is active is a safe no-op. Similarly, setting `setProcessBudgetBytes()` or `setPackageBudgetBytes()` to the same value consecutively doesn't trigger redundant system reconfigurations.
- **Calling frequency**: Setting, updating, or clearing a budget makes a cross-process call to the system service to update the operating system memory controller for the process. While lightweight, it isn't completely free. Call these APIs during discrete lifecycle transitions and task milestones (such as entering or leaving an activity, starting or completing background processing, or handling speech requests), and avoid calling them in tight loops, audio processing threads, or per-frame render routines.
- **Query frequency** : The query properties `processCurrentUsageBytes` and `packageCurrentUsageBytes` fetch live memory usage from the system service. While fast, queries should be invoked on demand (such as during task transitions or inside `OnOverBudgetListener` callbacks) rather than polled in continuous loops.

#### Listen for over-budget pressure callbacks

Apps can register a listener to be notified when memory usage exceeds the
budget threshold. This allows the app to perform proactive app-level cleanup
(such as clearing in-memory bitmap caches) while the operating system reclaims
memory to keep the process or package within its budget:

    val cleanupThread = HandlerThread("MemoryBudgetCleanup").apply { start() }

    val listener = MemoryBudgetManager.OnOverBudgetListener { budgetBytes ->
        Log.w(TAG, "Process exceeded memory budget of $budgetBytes bytes")
        // Proactively evict thread-safe caches on the background Looper
        imageTileCache.evictAll()
    }

    // Register on a background Looper before tightening a dynamic budget
    budgetManager.registerProcessOverBudgetListener(cleanupThread.looper, listener)

    // When done (for example, in onStop)
    budgetManager.unregisterProcessOverBudgetListener(listener)

> [!NOTE]
> **Note:** Over-budget callbacks only fire when an active budget is configured for the process or package (either declared using `<memory-budget>` in `AndroidManifest.xml` or set at runtime using `setProcessBudgetBytes` or `setPackageBudgetBytes`). If no manifest or runtime budget is active, `OnOverBudgetListener` won't be invoked.

**Best practices for over-budget callbacks:**

- **Use a background `Looper`** : Pass a background [`HandlerThread`](https://developer.android.com/reference/android/os/HandlerThread) `Looper` to `registerProcessOverBudgetListener` or `registerPackageOverBudgetListener` whenever possible. Running cache eviction or file cleanup on a background thread avoids contending with frame rendering on the UI thread while the process is under memory pressure. Reserve `Looper.getMainLooper` for listeners that only touch main-thread-bound UI state.
- **Expect repeated callbacks** : Over-budget callbacks aren't one-shot notifications. When usage exceeds the budget, the operating system reclaims cold pages first, and if pressure continues, the system keeps reclaiming memory and invoking your listener at most once every second. Make your callback idempotent. If your app only needs a single notification or wants a longer cooldown between cleanup passes, call `unregisterProcessOverBudgetListener` (or `unregisterPackageOverBudgetListener`) inside the callback, or guard your cleanup with a cooldown timestamp or [`AtomicBoolean`](https://developer.android.com/reference/java/util/concurrent/atomic/AtomicBoolean).
- **Register before tightening a budget** : If current memory usage already exceeds a new budget when you call `setProcessBudgetBytes` or `setPackageBudgetBytes`, an over-budget event is triggered as soon as the new budget is applied. Register your listener before setting the budget so your app doesn't miss that initial over-budget notification.
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

    // Clear the dynamic budget to resume manifest limits (or unconstrained baseline)
    AMemoryBudgetManager_clearProcessBudget();

> [!NOTE]
> **Note:** Like their SDK counterparts, native budget operations are idempotent and make a cross-process call to the system service. They are designed for discrete lifecycle milestones rather than high-frequency game engine render loops or audio thread callbacks.

#### Monitor memory pressure events

The NDK provides two ways to monitor memory events:

1. **High-Level Watcher (`AMemoryBudgetManager_Watcher_create`)** : Monitors events on an `ALooper` with automatic debouncing.
2. **Low-Level File Descriptor** : `AMemoryBudgetManager_getProcessMemoryPressureFd` returns a native file descriptor that can be integrated directly into a custom `epoll` engine loop.

    void onMemoryPressure(int32_t event_mask, const AMemoryBudgetEvents* events, void* userdata) {
        // High-yield eviction of unused native textures or geometry caches
        purgeNativeTextureCaches();
    }

    // Register watcher on a background worker ALooper with a 1000ms debounce interval
    AMemoryBudgetManagerWatcher* watcher = AMemoryBudgetManager_Watcher_create(
        background_looper,
        AMEMORY_BUDGET_MANAGER_EVENT_PROCESS,
        1000 /* debounce_ms */,
        &onMemoryPressure,
        NULL /* userdata */
    );

    // When done:
    AMemoryBudgetManager_Watcher_destroy(watcher);

Bind the watcher to a background worker thread's `ALooper`, rather than your
main UI or render thread, so that cache eviction doesn't contend with frame
rendering. Create the watcher before tightening a budget with
`AMemoryBudgetManager_setProcessBudget` or
`AMemoryBudgetManager_setPackageBudget` so your app doesn't miss the initial
over-budget event.
While the process or package remains over budget and the operating system
continues reclaiming memory, the watcher invokes the callback repeatedly (at
most once per `debounce_ms` interval). Make your callback idempotent, or call
`AMemoryBudgetManager_Watcher_destroy` (which is safe to call from inside the
callback) if your app only needs a one-shot notification.

## Runtime API examples

The following examples demonstrate how to implement the runtime APIs using the
Android SDK API (written in Kotlin) and the Native NDK API (written in C++).

### Android SDK example: Adaptive image editor

This example shows an image editing app (`com.example.imageeditor`) whose
manifest declares a 256MB ceiling to accommodate its multi-layer canvas:

    <manifest ... >
        <application ... >
            <!-- Manifest ceiling accommodates the heaviest editing workload -->
            <memory-budget android:maxMb="256" />
        </application>
    </manifest>

When the user is browsing the lightweight thumbnail gallery, the app uses the
Android SDK API in Kotlin to dynamically tighten its process budget to 96MB.
When the user opens the multi-layer editing canvas, the app clears the dynamic
budget to restore the full 256MB manifest ceiling. It also registers an
`OnOverBudgetListener` on a background [`HandlerThread`](https://developer.android.com/reference/android/os/HandlerThread)
`Looper` before applying the gallery budget to evict cached preview bitmaps
under pressure without blocking the UI thread.

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

### NDK C++ example: Native 3D engine

This example shows a native C++ game engine managing memory budgets based on the
active graphics quality level, assuming the application's manifest declares a
512MB ceiling to accommodate High quality graphics (`android:maxMb="512"`). The
engine starts `AMemoryBudgetManager_Watcher_create` on a background worker
thread's `ALooper` before tightening the budget for lower quality presets, and
unloads texture mipmaps when over budget.

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

        // Call on a background worker ALooper before tightening the budget with setQualityBudget
        bool startMonitoring(ALooper* backgroundLooper) {
            if (!backgroundLooper) return false;

            // Monitor process budget events, debounced to at most once every 1000ms
            mWatcher = AMemoryBudgetManager_Watcher_create(
                backgroundLooper,
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
            // Fast, idempotent, high-yield eviction without allocating memory
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