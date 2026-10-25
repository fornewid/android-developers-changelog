---
title: https://developer.android.com/tools/agents/android-cli/commands/profiler_systemtrace_start
url: https://developer.android.com/tools/agents/android-cli/commands/profiler_systemtrace_start
source: md.txt
---

Start trace recording segment.

## Usage

    android profiler systemtrace start [-h] [--activity=PARAM] [--device=PARAM] [--disable=PARAM] [--duration=PARAM] [--enable=PARAM] [--keep-session] [--launch] [--output=PARAM] [--package=PARAM] [--preset=PARAM] [--session=PARAM] [--wait]

## Options

- `--activity=PARAM` - Activity to launch with --launch; defaults to the launcher activity. Only when 'start' creates the session (not allowed after 'prepare').
- `--device=PARAM` - Device serial or AVD name.
- `--disable=PARAM` - Trace options not to record: a group (cpu, gpu, vulkan) or an individual option (cpu.freq, cpu.sched, cpu.syscalls, cpu.slices, gpu.freq, gpu.memory, gpu.work-period, gpu.frame-lifecycle, gpu.counters, vulkan.cpu-timing, vulkan.debug-names, vulkan.screenshots); repeatable or comma-separated. Individual options take precedence over groups, e.g. --enable cpu --disable cpu.syscalls. Only when 'start' creates the session (not allowed after 'prepare').
- `--duration=PARAM` - Duration in seconds (auto-stops trace and restores device if --keep-session is false).
- `--enable=PARAM` - Trace options to record on top of the preset: a group (cpu, gpu, vulkan) or an individual option (cpu.freq, cpu.sched, cpu.syscalls, cpu.slices, gpu.freq, gpu.memory, gpu.work-period, gpu.frame-lifecycle, gpu.counters, vulkan.cpu-timing, vulkan.debug-names, vulkan.screenshots); repeatable or comma-separated. Individual options take precedence over groups, e.g. --enable cpu --disable cpu.syscalls. Only when 'start' creates the session (not allowed after 'prepare').
- `-h,--help` - Shows the help message for the specified command.
- `--keep-session` - Keep the session alive after the recording ends (requires --duration or --wait); for manual recordings pass --keep-session to 'stop'.
- `--launch` - Launch target application after trace buffer settles.
- `-o,--output=PARAM` - Directory or file path to save output trace.
- `--package=PARAM` - Package name of the app to trace; omit for a system-wide trace. Only when 'start' creates the session (not allowed after 'prepare').
- `--preset=PARAM` - Recording configuration template to start from (default, graphics); omit for default. Adjust it with --enable and --disable. Only when 'start' creates the session (not allowed after 'prepare').
- `--session=PARAM` - Session ID for background daemon.
- `--wait` - Block until the recording ends.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Description

`android profiler systemtrace start` starts recording a system trace. If no
session is active, it starts one first; otherwise, it records in the active
session, such as one started by
[`android profiler systemtrace prepare`](https://developer.android.com/tools/agents/android-cli/commands/profiler_systemtrace_prepare).

Pass `--package` to trace an app, or omit it for a system-wide trace. The trace
is saved to the file or directory passed in `-o, --output`, or to the current
directory if it's omitted.

### Choose what to record (`--preset`, `--enable`, and `--disable`)

A preset is the set of trace options to start from:

- `default`: CPU scheduling, thread slices, CPU frequency and idle states, and the frame lifecycle. Used if `--preset` is omitted.
- `graphics`: Everything in `default`, plus GPU frequency, GPU memory, GPU work periods, GPU counters, and Vulkan CPU timing. Requires `--package`.

Pass `--enable` and `--disable` to add or remove trace options, either a group
(such as `cpu`) or an individual option (such as `cpu.syscalls`). Individual
options take precedence over groups. The `vulkan` options require `--package`.

These options set up the session, so you can only pass them when `start` starts
the session.

### Launch the app (`--launch` and `--activity`)

Pass `--launch` to launch the app after the recording starts, which captures the
app startup. By default, the launcher activity of the app is launched; pass
`--activity` to launch a different one.

### End the recording (`--duration` and `--wait`)

By default, `start` returns as soon as the recording starts, and the recording
continues until you run [`android profiler systemtrace stop`](https://developer.android.com/tools/agents/android-cli/commands/profiler_systemtrace_stop).
You can also end it as follows:

- `--duration`: Stops the recording after the given number of seconds and saves the trace.
- `--wait`: Blocks until the recording ends. Press `Ctrl+C` to stop the recording early and save the trace.

When the recording ends, the session ends and the device is restored. To record
again in the same session, pass `--keep-session` together with `--duration` or
`--wait`, or pass `--keep-session` to `stop`.

### Examples

Trace the startup of an app until you stop the recording:

    android profiler systemtrace start --package=com.example.app --launch --output=startup.perfetto-trace

Record a 10-second system-wide trace, and wait for the trace to be saved:

    android profiler systemtrace start --duration=10 --wait --output=system.perfetto-trace

Record the `graphics` preset for an app, with system calls and without GPU
counters:

    android profiler systemtrace start --package=com.example.app --preset=graphics --enable=cpu.syscalls --disable=gpu.counters