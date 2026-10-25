---
title: https://developer.android.com/tools/agents/android-cli/commands/profiler_heapdump
url: https://developer.android.com/tools/agents/android-cli/commands/profiler_heapdump
source: md.txt
---

Capture Android JVM heap dump snapshots (requires API 29+).

## Usage

    android profiler heapdump [-h]

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Subcommands

- **[`capture`](https://developer.android.com/tools/agents/android-cli/commands/profiler_heapdump_capture)** - Capture a JVM heap snapshot (requires API 29+).

## Description

The `android profiler heapdump` command set captures heap dumps of apps running
on a connected Android device or emulator. A heap dump is a snapshot of the
objects in the Java heap of a process, saved as an `.hprof` file that you can
open in the [Android Studio Memory Profiler](https://developer.android.com/studio/profile/capture-heap-dump). It requires a
device running Android 10 (API level 29) or higher. The app must be debuggable
(for example, a debug build), unless the device runs a `userdebug` or `eng`
build of Android.

To capture a heap dump, run
[`android profiler heapdump capture`](https://developer.android.com/tools/agents/android-cli/commands/profiler_heapdump_capture). Each capture runs in
its own profiling session, which ends when the capture finishes.

### Examples

Capture a heap dump of a running app:

    android profiler heapdump capture --process=com.example.app --output=dump.hprof

Run garbage collection first, which frees the objects that are no longer
reachable:

    android profiler heapdump capture --process=com.example.app --gc --output=dump.hprof

Cancel a stuck capture:

    android profiler session terminate