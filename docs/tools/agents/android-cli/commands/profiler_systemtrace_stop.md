---
title: https://developer.android.com/tools/agents/android-cli/commands/profiler_systemtrace_stop
url: https://developer.android.com/tools/agents/android-cli/commands/profiler_systemtrace_stop
source: md.txt
---

Stop trace recording segment and pull artifact.

## Usage

    android profiler systemtrace stop [-h] [--device=PARAM] [--keep-session] [--session=PARAM]

## Options

- `--device=PARAM` - Device serial or AVD name.
- `-h,--help` - Shows the help message for the specified command.
- `--keep-session` - Preserve session daemon active after recording stops.
- `--session=PARAM` - Session ID for background daemon.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Description

`android profiler systemtrace stop` stops the recording of the active session,
pulls the trace file from the device, and saves it to the output passed to
[`android profiler systemtrace start`](https://developer.android.com/tools/agents/android-cli/commands/profiler_systemtrace_start).

### Keep the session alive (`--keep-session`)

By default, the session ends after the recording stops, and the device and the
app are restored. Pass `--keep-session` to keep the session alive, so you can
run `start` again to record another trace with the same setup. When you are
done, run [`android profiler session terminate`](https://developer.android.com/tools/agents/android-cli/commands/profiler_session_terminate) to end the
session.

### Examples

Stop the recording and end the session:

    android profiler systemtrace stop

Stop the recording of the session named `my-session`, and keep the session
alive:

    android profiler systemtrace stop --session=my-session --keep-session