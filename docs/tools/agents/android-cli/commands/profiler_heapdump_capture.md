---
title: https://developer.android.com/tools/agents/android-cli/commands/profiler_heapdump_capture
url: https://developer.android.com/tools/agents/android-cli/commands/profiler_heapdump_capture
source: md.txt
---

Capture a JVM heap snapshot (requires API 29+).

## Usage

    android profiler heapdump capture [-h] [--device=PARAM] [--gc] [--output=PARAM] [--pid=PARAM] [--process=PARAM] [--session=PARAM] [--timeout=PARAM]

## Options

- `--device=PARAM` - Device serial or AVD name (requires API 29+).
- `--gc` - Trigger GC before dumping heap.
- `-h,--help` - Shows the help message for the specified command.
- `-o,--output=PARAM` - Directory or file path to save the .hprof heap dump.
- `--pid=PARAM` - PID of the process to capture.
- `--process=PARAM` - Name of the process to capture, e.g. com.example.app or com.example.app:service.
- `--session=PARAM` - Name for this capture's session. The session ends when the capture finishes; use the name to check or cancel an in-progress capture from another terminal.
- `--timeout=PARAM` - Maximum time in seconds to wait for the heap dump to be written on the device.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Description

`android profiler heapdump capture` captures a heap dump of a process running on
a connected Android device or emulator, and saves it as an `.hprof` file. It
blocks until the heap dump is saved, and requires a device running Android 10
(API level 29) or higher. The app must be debuggable (for example, a debug
build), unless the device runs a `userdebug` or `eng` build of Android.

The heap dump is saved to the file or directory passed in `-o, --output`, or to
the current directory if it's omitted.

### Select the process (`--process` and `--pid`)

Pass exactly one of the following options:

- `--process`: The name of the process, such as `com.example.app` for the main process of an app, or `com.example.app:service` for another process of the app.
- `--pid`: The process ID.

### Run garbage collection (`--gc`)

Pass `--gc` to run garbage collection before capturing the heap dump, which
frees the objects that are no longer reachable.

### Cancel a capture (`--session` and `--timeout`)

Each capture runs in its own profiling session, which ends when the capture
finishes. Pass `--session` to name the session, so you can check or cancel the
capture from another terminal with the
[`android profiler session`](https://developer.android.com/tools/agents/android-cli/commands/profiler_session) commands.

If the heap dump isn't written on the device within the number of seconds passed
in `--timeout`, the capture is cancelled. Increase it for apps with a large
heap.

### Examples

Capture a heap dump of the main process of an app:

    android profiler heapdump capture --process=com.example.app --output=dump.hprof

Capture a heap dump of the process with ID `1234` on a specific emulator, after
garbage collection:

    android profiler heapdump capture --device=emulator-5554 --pid=1234 --gc --output=dump.hprof

Capture a heap dump in a session named `my-dump`:

    android profiler heapdump capture --process=com.example.app --session=my-dump

While the capture is running, check its status from another terminal:

    android profiler session status --session=my-dump