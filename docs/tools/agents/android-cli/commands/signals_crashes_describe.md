---
title: https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_describe
url: https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_describe
source: md.txt
---

Displays detailed metadata, OS and device distributions, stack traces, custom
keys, and logs for an issue cluster.

## Usage

    android signals crashes describe [-h] [--format=PARAM] [--include=PARAM] [--sample-id=PARAM] [--timeframe=PARAM] <issue-id>

## Options

- `--format=PARAM` - Output format ('text' or 'json'; default: 'text').
- `-h,--help` - Shows the help message for the specified command.
- `--include=PARAM` - Comma-separated sections to include ('all', 'stack', 'distributions', 'metadata', 'logs', 'keys'; default: 'all').
- `--sample-id=PARAM` - Selects a specific sample crash event ID to inspect (as returned by 'crashes samples'; default: a sample event of the issue).
- `--timeframe=PARAM` - Time window to query ('24h', '7d', '30d', '60d', '90d'; default: '7d').

`crashes` options:

- `--firebase-app=PARAM` - Firebase app ID to query in Crashlytics (e.g. '1::android:').

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<issue-id>` - The unique identifier for the issue cluster, prefixed with its source as returned by 'crashes list' (for example, 'firebase/abc123').

## Description

`android signals crashes describe` prints the details of one issue cluster: its
status and when it was first and last seen, its stack trace, the distribution of
its events across API levels and devices, and the metadata of a sample event, as
well as the custom keys and logs recorded with the sample event.

Get the `<issue-id>` from the output of
[`android signals crashes list`](https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_list). The issue ID must be
prefixed with `firebase/`. The `--firebase-app` option must be provided or
configured in `~/.androidrc`.

By default, the stack trace and the metadata come from a sample event of the
issue. Pass `--sample-id` with a `Sample ID` printed by
[`android signals crashes samples`](https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_samples) to inspect a
specific event instead.

For memory issues (tagged `[OOM]` or `[MLK]`), the output points to
[`android signals heaps list`](https://developer.android.com/tools/agents/android-cli/commands/signals_heaps_list) to inspect the associated
heap dumps.

### Select the sections to print (`--include`)

Pass `--include` with a comma-separated list of sections to print only some of
them: `stack`, `distributions`, `metadata`, `logs`, and `keys`. The default,
`all`, prints every section.

### Examples

Describe an issue:

    android signals crashes describe firebase/<issue-id> --firebase-app=1:123456789012:android:0123456789abcdef

Print only the stack trace of an issue:

    android signals crashes describe firebase/<issue-id> --firebase-app=1:123456789012:android:0123456789abcdef --include=stack

Describe a specific event of an issue, with its logs and custom keys:

    android signals crashes describe firebase/<issue-id> --firebase-app=1:123456789012:android:0123456789abcdef --sample-id=<sample-id> --include=stack,logs,keys