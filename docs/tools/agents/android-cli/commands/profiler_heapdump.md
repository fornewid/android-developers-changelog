---
title: https://developer.android.com/tools/agents/android-cli/commands/profiler_heapdump
url: https://developer.android.com/tools/agents/android-cli/commands/profiler_heapdump
source: md.txt
---

> Documentation index: https://developer.android.com/tools/agents/android-cli/commands/llms.txt

Capture Android JVM heap dump snapshots (requires API 31+ for --type=perfetto,
or API 29+ with --type=hprof).

## Usage

```bash
android profiler heapdump [-h]
```

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Subcommands

- **[`capture`](https://developer.android.com/tools/agents/android-cli/commands/profiler_heapdump_capture.md.txt)** - Capture a JVM heap snapshot (requires API 31+ for --type=perfetto, or API 29+ with --type=hprof).

## Description

The `android profiler heapdump` command set captures heap dumps of apps running
on a connected Android device or emulator. A heap dump is a snapshot of the
objects in the JVM heap of a process. By default, it's saved as an `.hprof`
file. Capturing an `.hprof` file requires a device running Android 10 (API
level 29) or higher, and a debuggable app (for example, a debug build), unless
the device runs a `userdebug` or `eng` build of Android. You can also record a
Perfetto heap dump, which is saved as a `.perfetto-java-heap-dump` file and has
different requirements: see
[`android profiler heapdump capture`](https://developer.android.com/tools/agents/android-cli/commands/profiler_heapdump_capture.md.txt). You can open both
`.hprof` and `.perfetto-java-heap-dump` files in the [Android Studio Memory
Profiler](https://developer.android.com/studio/profile/capture-heap-dump).

To capture a heap dump, run
[`android profiler heapdump capture`](https://developer.android.com/tools/agents/android-cli/commands/profiler_heapdump_capture.md.txt). Each capture runs in
its own profiling session, which ends when the capture finishes.

### Examples

Capture a heap dump of a running app:

```bash
android profiler heapdump capture --process=com.example.app --output=dump.hprof
```

Run garbage collection first, which frees the objects that are no longer
reachable:

```bash
android profiler heapdump capture --process=com.example.app --gc --output=dump.hprof
```

Capture a heap dump as a Perfetto trace:

```bash
android profiler heapdump capture --process=com.example.app --type=perfetto --output=dump.perfetto-java-heap-dump
```

Cancel a stuck capture:

```bash
android profiler session terminate
```