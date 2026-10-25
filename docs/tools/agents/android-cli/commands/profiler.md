---
title: https://developer.android.com/tools/agents/android-cli/commands/profiler
url: https://developer.android.com/tools/agents/android-cli/commands/profiler
source: md.txt
---

Profiles Android apps, games, and devices.

## Usage

    android profiler [-h]

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Subcommands

- **[`heapdump`](https://developer.android.com/tools/agents/android-cli/commands/profiler_heapdump)** - Capture Android JVM heap dump snapshots (requires API 29+).
- **[`session`](https://developer.android.com/tools/agents/android-cli/commands/profiler_session)** - Manage profiling sessions of any type: list them, query their status, or terminate them.
- **[`systemtrace`](https://developer.android.com/tools/agents/android-cli/commands/profiler_systemtrace)** - System tracing tools. Captures CPU scheduling, thread slices, frame lifecycle, GPU counters, and Vulkan timing into a Perfetto trace file.