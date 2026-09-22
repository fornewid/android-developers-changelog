---
title: https://developer.android.com/topic/performance/issues
url: https://developer.android.com/topic/performance/issues
source: md.txt
---

Delivering a smooth, stable, and battery-efficient app experience requires
identifying and resolving common performance bottlenecks across stability, UI
rendering, memory consumption, background work, startup latency, and build
optimization.

The guides in this section explain the underlying Android platform behavior for
each type of issue and walk through how to diagnose, profile, and remediate
them using tools such as Android Studio Profiler, Perfetto, Logcat, and
`ApplicationExitInfo`.

> [!NOTE]
> **Note:** If you distribute your app on Google Play, see [Android vitals](https://developer.android.com/google/play/vitals) to learn how Google Play tracks these metrics in the field, evaluates bad behavior thresholds, and surfaces alerts in Play Console.

## Stability

- **[ANRs](https://developer.android.com/topic/performance/issues/anr):** Diagnose and fix Application Not Responding (ANR) errors caused by blocked UI threads, main-thread I/O, lock contention, or slow broadcast receivers.
- **[Crashes](https://developer.android.com/topic/performance/issues/crash):** Read stack traces, inspect Logcat output, and prevent unhandled exceptions and native signals.

## Rendering and startup

- **[Slow rendering](https://developer.android.com/topic/performance/issues/render):** Identify and fix dropped or frozen UI frames (`>16ms` and `>700ms`) caused by expensive layouts, bind passes, or main-thread stalls.
- **[Slow sessions (games only)](https://developer.android.com/topic/performance/issues/slow-session):** Measure frame pacing with `SurfaceFlinger` and optimize game frame rates using Android Frame Pacing (Swappy), Vulkan, and the Android Dynamic Performance Framework (ADPF).
- **[App startup time](https://developer.android.com/topic/performance/issues/launch-time):** Understand cold, warm, and hot launch internals, measure Time to Initial Display (TTID) and Time to Full Display (TTFD), and optimize startup work.

## Memory management

- **[Low memory killers (LMKs)](https://developer.android.com/topic/performance/issues/lmk):** Understand how the Android Low Memory Killer daemon (`lmkd`) prioritizes processes via `oom_adj_score` and profile memory footprint in Android Studio, Unity, and Unreal Engine.
- **[Memory usage (Anonymous RSS + swap)](https://developer.android.com/topic/performance/issues/memory-usage):** Measure and reduce your app's anonymous Resident Set Size (RSS) and swap memory footprint across foreground, service, and background states.
- **[Bitmap memory usage](https://developer.android.com/topic/performance/issues/bitmap-memory-usage):** Diagnose oversized or leaked bitmap allocations and release graphic buffers when UI components move to the background.

## Battery and background work

- **[Excessive wake locks](https://developer.android.com/topic/performance/issues/excessive-wakelock):** Avoid holding partial wake locks for extended periods and migrate background tasks to `WorkManager` or `JobScheduler`.
- **[Stuck partial wake locks](https://developer.android.com/topic/performance/issues/stuck-wakelock):** Ensure every acquired partial wake lock is properly released across all execution and error paths.
- **[Excessive wakeups](https://developer.android.com/topic/performance/issues/wakeup):** Reduce exact alarm wakeups and batch or defer scheduled background work.
- **[Excessive background Wi-Fi scans](https://developer.android.com/topic/performance/issues/bg-wifi):** Minimize background Wi-Fi scanning frequency and use passive or batched location and connectivity APIs.
- **[Excessive background network usage](https://developer.android.com/topic/performance/issues/bg-network-usage):** Batch and defer background mobile network transfers using `WorkManager` constraints.
- **[Excessive battery usage](https://developer.android.com/topic/performance/issues/excessive-battery-usage):** Diagnose high battery drain on mobile and Wear OS devices by profiling CPU, sensor, and radio activity.

## Permissions and build optimization

- **[Permission denials](https://developer.android.com/topic/performance/issues/permissions):** Request runtime permissions in context and explain permission rationale clearly to users.
- **[DEX code optimization](https://developer.android.com/topic/performance/issues/code-optimization):** Configure R8 shrinking, obfuscation, and optimization rules to reduce DEX size and improve runtime performance.