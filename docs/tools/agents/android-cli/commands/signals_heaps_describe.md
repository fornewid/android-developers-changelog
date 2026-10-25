---
title: https://developer.android.com/tools/agents/android-cli/commands/signals_heaps_describe
url: https://developer.android.com/tools/agents/android-cli/commands/signals_heaps_describe
source: md.txt
---

Describes a heap dump with the issue, metadata, custom keys, and logs of its
Crashlytics event, without the stack trace.

## Usage

    android signals heaps describe [-h] [--format=PARAM] [--include=PARAM] <heap-id>

## Options

- `--format=PARAM` - Output format ('text' or 'json'; default: 'text').
- `-h,--help` - Shows the help message for the specified command.
- `--include=PARAM` - Comma-separated event sections to include ('all', 'keys', 'logs'; default: 'all').

`heaps` options:

- `--firebase-app=PARAM` - Firebase app ID to query in Crashlytics (e.g. '1::android:').

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<heap-id>` - Heap dump to describe (as returned by 'heaps list', for example 'firebase/6aa1776301a300013390aca1f5bfc99f').

## Description

`android signals heaps describe` displays detailed information about a heap
dump: its collection time, kind, size, app version, device, and API level,
alongside the issue, event metadata, custom keys, and logs of its crash session.

Get the `<heap-id>` from the output of
[`android signals heaps list`](https://developer.android.com/tools/agents/android-cli/commands/signals_heaps_list). Pass `--firebase-app` or
configure it in `~/.androidrc`.

The stack trace and issue distributions are omitted because they are not
specific to the individual heap dump. To view the stack trace, run
[`android signals crashes describe`](https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_describe) with
`--sample-id` set to the event ID of the session.

To download the heap dump file, run
[`android signals heaps download`](https://developer.android.com/tools/agents/android-cli/commands/signals_heaps_download).

### Select the sections to include (`--include`)

Pass `--include` with a comma-separated list of sections to print: `keys`,
`logs`, or `all` (default: `all`).

### Examples

Describe a heap dump:

    android signals heaps describe firebase/<heap-id> --firebase-app=1:123456789012:android:0123456789abcdef

Describe a heap dump including only custom keys:

    android signals heaps describe firebase/<heap-id> --firebase-app=1:123456789012:android:0123456789abcdef --include=keys

Describe a heap dump as JSON:

    android signals heaps describe firebase/<heap-id> --firebase-app=1:123456789012:android:0123456789abcdef --format=json