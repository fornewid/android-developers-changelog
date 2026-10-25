---
title: https://developer.android.com/tools/agents/android-cli/commands/profiler_systemtrace
url: https://developer.android.com/tools/agents/android-cli/commands/profiler_systemtrace
source: md.txt
---

System tracing tools. Captures CPU scheduling, thread slices, frame lifecycle,
GPU counters, and Vulkan timing into a Perfetto trace file.

## Usage

    android profiler systemtrace [-h]

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Subcommands

- **[`prepare`](https://developer.android.com/tools/agents/android-cli/commands/profiler_systemtrace_prepare)** - Put the device and app into profiling state without starting a recording. Use --launch to launch the package/activity now; alternatively, launch the app yourself, or pass --launch to 'start' instead.
- **[`start`](https://developer.android.com/tools/agents/android-cli/commands/profiler_systemtrace_start)** - Start trace recording segment.
- **[`stop`](https://developer.android.com/tools/agents/android-cli/commands/profiler_systemtrace_stop)** - Stop trace recording segment and pull artifact.

## Description

The `android profiler systemtrace` command set records system traces from a
connected Android device or emulator. A system trace captures CPU scheduling,
thread slices, the frame lifecycle, GPU counters, and Vulkan timing into a
[Perfetto](https://perfetto.dev/docs/) trace file.

Each recording runs in a profiling session, which a background daemon keeps
alive between commands. The session puts the device and the app into a profiling
state, and restores them when it ends. If you omit `--session`, commands use the
only active session.

### Typical workflow

Here is the sequence of commands for a typical workflow:

1. Optional: Run [`android profiler systemtrace prepare`](https://developer.android.com/tools/agents/android-cli/commands/profiler_systemtrace_prepare) to put the device and the app into a profiling state before you record. This lets you launch the app and navigate to the screen you want to trace first.
2. Run [`android profiler systemtrace start`](https://developer.android.com/tools/agents/android-cli/commands/profiler_systemtrace_start) to start a recording.
3. Run [`android profiler systemtrace stop`](https://developer.android.com/tools/agents/android-cli/commands/profiler_systemtrace_stop) to stop the recording and pull the trace file from the device.

If a session gets stuck, run
[`android profiler session terminate`](https://developer.android.com/tools/agents/android-cli/commands/profiler_session_terminate) to end it and restore
the device.

### Examples

Trace the startup of an app, stopping the recording manually:

    android profiler systemtrace start --package=com.example.app --launch --output=startup.perfetto-trace
    android profiler systemtrace stop

Trace an app that is already running, or the whole system if you omit
`--package`:

    android profiler systemtrace start --package=com.example.app --output=trace.perfetto-trace
    android profiler systemtrace stop

Launch the app and interact with it yourself, then trace a single interaction:

    android profiler systemtrace prepare --package=com.example.app
    # Launch the app and navigate to the target screen.
    android profiler systemtrace start --output=interaction.perfetto-trace
    # Perform the interaction.
    android profiler systemtrace stop

Record more than one trace in the same session:

    android profiler systemtrace start --package=com.example.app --launch --output=segment1.perfetto-trace
    android profiler systemtrace stop --keep-session
    android profiler systemtrace start --output=segment2.perfetto-trace
    android profiler systemtrace stop --keep-session
    android profiler session terminate

End a stuck session and restore the device:

    android profiler session terminate