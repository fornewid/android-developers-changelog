---
title: https://developer.android.com/tools/agents/android-cli/commands/profiler_systemtrace_prepare
url: https://developer.android.com/tools/agents/android-cli/commands/profiler_systemtrace_prepare
source: md.txt
---

Put the device and app into profiling state without starting a recording. Use
--launch to launch the package/activity now; alternatively, launch the app
yourself, or pass --launch to 'start' instead.

## Usage

    android profiler systemtrace prepare [-h] [--activity=PARAM] [--device=PARAM] [--disable=PARAM] [--enable=PARAM] [--launch] [--package=PARAM] [--preset=PARAM] [--session=PARAM]

## Options

- `--activity=PARAM` - Activity name to launch; if omitted, launches default activity.
- `--device=PARAM` - Device serial or AVD name.
- `--disable=PARAM` - Trace options not to record: a group (cpu, gpu, vulkan) or an individual option (cpu.freq, cpu.sched, cpu.syscalls, cpu.slices, gpu.freq, gpu.memory, gpu.work-period, gpu.frame-lifecycle, gpu.counters, vulkan.cpu-timing, vulkan.debug-names, vulkan.screenshots); repeatable or comma-separated. Individual options take precedence over groups, e.g. --enable cpu --disable cpu.syscalls.
- `--enable=PARAM` - Trace options to record on top of the preset: a group (cpu, gpu, vulkan) or an individual option (cpu.freq, cpu.sched, cpu.syscalls, cpu.slices, gpu.freq, gpu.memory, gpu.work-period, gpu.frame-lifecycle, gpu.counters, vulkan.cpu-timing, vulkan.debug-names, vulkan.screenshots); repeatable or comma-separated. Individual options take precedence over groups, e.g. --enable cpu --disable cpu.syscalls.
- `-h,--help` - Shows the help message for the specified command.
- `--launch` - Launch target application upfront after device preparation.
- `--package=PARAM` - Package name of the app to profile.
- `--preset=PARAM` - Recording configuration template to start from (default, graphics); omit for default. Adjust it with --enable and --disable.
- `--session=PARAM` - Session ID for background daemon.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Description

`android profiler systemtrace prepare` starts a profiling session and puts the
device and the app into a profiling state, without starting a recording. Use it
when you want to launch the app or navigate to a specific screen before you
record. When the session is ready, run
[`android profiler systemtrace start`](https://developer.android.com/tools/agents/android-cli/commands/profiler_systemtrace_start) to start recording.

Pass `--package` to choose the app to profile, and `--preset`, `--enable`, and
`--disable` to choose what to record. These options set up the session, so you
can't pass them to `start` after `prepare`. See
[`android profiler systemtrace start`](https://developer.android.com/tools/agents/android-cli/commands/profiler_systemtrace_start) for a description of
the trace options.

### Launch the app (`--launch` and `--activity`)

Pass `--launch` to launch the app as soon as the device is prepared. By default,
the launcher activity of the app is launched; pass `--activity` to launch a
different one. Alternatively, launch the app yourself, or pass `--launch` to
`start` instead to trace the app startup.

### Examples

Prepare a session for an app, then launch the app yourself:

    android profiler systemtrace prepare --package=com.example.app

Prepare a session to record the `graphics` preset for an app, and launch the
app:

    android profiler systemtrace prepare --package=com.example.app --preset=graphics --launch