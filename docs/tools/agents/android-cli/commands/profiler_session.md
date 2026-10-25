---
title: https://developer.android.com/tools/agents/android-cli/commands/profiler_session
url: https://developer.android.com/tools/agents/android-cli/commands/profiler_session
source: md.txt
---

Manage profiling sessions of any type: list them, query their status, or
terminate them.

## Usage

    android profiler session [-h]

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Subcommands

- **[`list`](https://developer.android.com/tools/agents/android-cli/commands/profiler_session_list)** - List active profiling sessions.
- **[`status`](https://developer.android.com/tools/agents/android-cli/commands/profiler_session_status)** - Query profiling session status.
- **[`terminate`](https://developer.android.com/tools/agents/android-cli/commands/profiler_session_terminate)** - Terminate profiling session and restore device.