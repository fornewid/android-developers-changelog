---
title: https://developer.android.com/topic/performance/tracing/profiling-manager/debug-mode
url: https://developer.android.com/topic/performance/tracing/profiling-manager/debug-mode
source: md.txt
---

When testing your `ProfilingManager` integration locally, requests might be
throttled by [rate limiting](https://developer.android.com/topic/performance/tracing/profiling-manager/will-my-profile-always-be-collected#how-rate-limiting-works) or background traces might not be active when
testing triggers. Use the `adb` commands on this page to disable throttling,
pull profiles, retain unredacted traces, trigger captures, and inspect service
state on a test device.

## Disable the rate limiter

To disable the app process and system rate limiters for [`requestProfiling`](https://developer.android.com/reference/android/os/ProfilingManager#requestProfiling(int,%20android.os.Bundle,%20java.lang.String,%20android.os.CancellationSignal,%20java.util.concurrent.Executor,%20java.util.function.Consumer%3Candroid.os.ProfilingResult%3E))
requests during local testing, run the following `device_config` command:

    adb shell device_config put profiling_testing rate_limiter.disabled true

When you finish testing, reset the flag:

    adb shell device_config delete profiling_testing rate_limiter.disabled

> [!NOTE]
> **Note:** `rate_limiter.disabled` applies only to app-driven `requestProfiling` calls. When you test triggers locally, set `system_triggered_profiling.testing_package_name` to force a continuous background trace and bypass the system-level rate limiter, as shown in [Force-enable background traces for trigger testing](https://developer.android.com/topic/performance/tracing/profiling-manager/debug-mode#debug-triggers).

## Pull profiles using ADB

To inspect a redacted profile locally on a device with root access, run `adb
pull` with the path returned by [`getResultFilePath`](https://developer.android.com/reference/android/os/ProfilingResult#getResultFilePath()):

    # Pull a profile
    adb pull /data/user/0/<com.example.myapp>/files/profiling/<profile-file-name>

> [!NOTE]
> **Note:** If you don't have root access, you can configure `ProfilingManager` to retain profiles in `/data/misc/perfetto-traces/profiling/`, which is accessible using `adb pull` on all build types on Android 16 (API level 36) and higher. See [Retain temporary and unredacted results](https://developer.android.com/topic/performance/tracing/profiling-manager/debug-mode#enable-unredacted-traces).

## Retain temporary and unredacted results

When testing profiling locally, you can retain results in the temporary
directory at `/data/misc/perfetto-traces/profiling/`. Comparing an unredacted
system trace with its redacted counterpart helps you understand what data is
dropped during redaction.

How temporary and unredacted results are retained depends on the Android version
your device runs:

- **Android 16 (API level 36) and higher** : You can retain both unredacted
  (where applicable) and redacted results in the temporary directory, which
  was expanded in Android 16 to be accessible using `adb pull` on all build
  types without root access (whereas Android 15 requires root access to read
  `/data/misc/perfetto-traces/profiling/`). To prevent the system from
  deleting temporary results, run the following command:

      adb shell device_config put profiling_testing delete_temporary_results.disabled true

- **Android 15 (API level 35)** : In the temporary directory, you can retain
  only the unredacted result, which is accessible over `adb` only on builds
  with root access. (Your app still receives the redacted profile in its own
  `/data/user/0/<app>/files/profiling/` directory, which your app code can
  read or copy on any build, though pulling directly from `/data/user/0/...`
  with `adb pull` requires root access, or `adb shell run-as <app>` on a
  debuggable build.) To prevent the system from deleting unredacted traces,
  run the following command:

      adb shell device_config put profiling_testing delete_unredacted_trace.disabled true

After capturing a profile, pull the retained file from the temporary directory:

    # Pull a retained redacted profile (Android 16 and higher)
    adb pull /data/misc/perfetto-traces/profiling/<trace-name>.<profile-type-ext>

    # Pull an unredacted system trace
    adb pull /data/misc/perfetto-traces/profiling/<trace-name>.perfetto-trace-unredacted

In these commands, `<trace-name>` is the base filename (without extension) from
the path returned by `ProfilingResult.getResultFilePath`, and the unredacted
system trace copy appends `-unredacted` to the `.perfetto-trace` extension. For
details on the filename structure and `<profile-type-ext>` values, see [File
locations and naming formats](https://developer.android.com/topic/performance/tracing/profiling-manager/upload-worker#file-locations-and-naming).

> [!NOTE]
> **Note:** Retaining temporary and unredacted results is disabled by default to conserve device storage and is intended only for local testing. Unredacted system traces use more storage space because they include system-wide process activity. When you finish testing, re-enable automatic deletion:

    adb shell device_config delete profiling_testing delete_temporary_results.disabled
    adb shell device_config delete profiling_testing delete_unredacted_trace.disabled

## Force-enable background traces for trigger testing

Because system background traces run at random intervals in production, testing
[trigger-based profiling](https://developer.android.com/topic/performance/tracing/profiling-manager/trigger-based-capture) locally can be difficult. To force the system to
run a continuous background trace and bypass the system-level rate limiter for
your app's triggers, set `system_triggered_profiling.testing_package_name`:

    adb shell device_config put profiling_testing system_triggered_profiling.testing_package_name <com.example.myapp>

Any per-trigger cooldown configured with [`setRateLimitingPeriodHours`](https://developer.android.com/reference/android/os/ProfilingTrigger.Builder#setRateLimitingPeriodHours(int)) still
applies. Because this mode runs continuously until you clear it, remove the
flag when you finish testing:

    adb shell device_config delete profiling_testing system_triggered_profiling.testing_package_name

## Useful debugging commands

On Android 16 (API level 36) and higher with a recent `Profiling` module
version, you can use the `cmd profiling_service` tool over `adb` to enable
verbose logging, trigger on-demand profile collections, and test triggers
directly from the command line.

> [!TIP]
> **Tip:** Additional options might exist or be added over time. Run `adb shell cmd
> profiling_service help` to see all available debugging commands, flags, and usage details.

### Enable verbose debug logging

To enable detailed `ProfilingService` logs in `logcat` and diagnose request
handling and delivery, run the following command:

    adb shell cmd profiling_service enable-logs true

### Request an on-demand profile collection

To start an immediate profile capture for a specific package from the command
line, run the following command:

    adb shell cmd profiling_service request-profiling <profiling_type> <com.example.myapp> [--user <user_id>] [--duration <duration_ms>] [--sources <sources>]

In this command, `<profiling_type>` is the integer constant value from
`ProfilingManager` (`1` for a Java heap dump, `2` for a heap profile, `3` for
stack sampling, or `4` for a system trace). The target app process must be
running for memory and stack profiles, the request is subject to the rate
limiter unless disabled, and the completed `ProfilingResult` is delivered only
to global listeners registered with `registerForAllProfilingResults`.

### Register and simulate triggers

To register a trigger or fire a simulated trigger event for a package and verify
your trigger callback handling, run the following commands:

    adb shell cmd profiling_service add-trigger <trigger_type> <com.example.myapp> [--user <user_id>]
    adb shell cmd profiling_service trigger <trigger_type> <com.example.myapp> [--user <user_id>]

In these commands, `<trigger_type>` is the integer constant value from
[`ProfilingTrigger`](https://developer.android.com/reference/android/os/ProfilingTrigger) (for example, `1` for `TRIGGER_TYPE_APP_FULLY_DRAWN`,
`2` for `TRIGGER_TYPE_ANR`, or `7` for `TRIGGER_TYPE_OOM`). Running
`add-trigger` registers the trigger with a `0`-hour cooldown, overriding any
existing registration for that trigger type. Simulating triggers that save a
snapshot of the background trace (such as `1` or `2`) requires an active
background trace (see [Force-enable background traces for trigger testing](https://developer.android.com/topic/performance/tracing/profiling-manager/debug-mode#debug-triggers)).

## Collect overall ProfilingManager state

On Android 16 (API level 36) and higher with a recent `Profiling` module
version, you can run `dumpsys` against `profiling_service` to diagnose issues
and inspect the current state of `ProfilingManager`:

    adb shell dumpsys profiling_service

The `dumpsys profiling_service` output is intended only for informational and
debugging purposes, and its format is subject to change. It provides a snapshot
of the service's internal state, including:

- Active throttles and rate limiter status.
- Active device configurations.
- Registered app triggers and their rate-limiting cooldowns.
- Active and queued profiling sessions.
- Recent profiling requests, trigger occurrences, and result delivery events.

> [!TIP]
> **Tip:** To retain a longer history of recent events in the `dumpsys` output during extended debugging sessions, run `adb shell cmd profiling_service enable-long-dumpsys true`.