---
title: https://developer.android.com/tools/agents/android-cli/commands/profiler
url: https://developer.android.com/tools/agents/android-cli/commands/profiler
source: md.txt
---

> Documentation index: https://developer.android.com/tools/agents/android-cli/commands/llms.txt

Profiles Android apps, games, and devices.

## Usage

```bash
android profiler [-h]
```

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Subcommands

- **[`heapdump`](https://developer.android.com/tools/agents/android-cli/commands/profiler_heapdump.md.txt)** - Capture Android JVM heap dump snapshots (requires API 31+ for --type=perfetto, or API 29+ with --type=hprof).
- **[`session`](https://developer.android.com/tools/agents/android-cli/commands/profiler_session.md.txt)** - Manage profiling sessions of any type: list them, query their status, or terminate them.
- **[`systemtrace`](https://developer.android.com/tools/agents/android-cli/commands/profiler_systemtrace.md.txt)** - System tracing tools. Captures CPU scheduling, thread slices, frame lifecycle, GPU counters, Vulkan timing, and Jetpack Compose composition into a Perfetto trace file.