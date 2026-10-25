---
title: https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_samples
url: https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_samples
source: md.txt
---

Lists individual sample crash events with timestamps, devices, and API levels
for an issue cluster.

## Usage

    android signals crashes samples [-h] [--api-level=PARAM] [--app-version=PARAM] [--device=PARAM] [--format=PARAM] [--limit=PARAM] [--timeframe=PARAM] <issue-id>

## Options

- `--api-level=PARAM` - Filters by Android API level or OS version (for example, '34', 'API 34', or 'Android 14').
- `--app-version=PARAM` - Filters by app version (version name or build version, for example '1.2.3' or '1.2.3 (1042)').
- `--device=PARAM` - Filters by device marketing name, model code, or manufacturer (for example, 'Pixel 8' or 'Samsung'; repeatable).
- `--format=PARAM` - Output format ('text' or 'json'; default: 'text').
- `-h,--help` - Shows the help message for the specified command.
- `--limit=PARAM` - Maximum number of results to return (1-5000; default: 100).
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

`android signals crashes samples` lists the individual crash events reported for
an issue cluster, with the time at which each one happened, the device that it
happened on, and its API level. By default, it lists up to 100 events from the
last seven days.

Get the `<issue-id>` from the output of
[`android signals crashes list`](https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_list). The issue ID must be
prefixed with `firebase/`. The corresponding app option (`--firebase-app`) must
be provided or configured in `~/.androidrc`.

Run
[`android signals crashes describe <issue-id> --sample-id=<sample-id>`](https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_describe)
with the `Sample ID` of an event to print the stack trace and the metadata of
that specific event, for example the oldest one or one that happened on a given
device.

### Examples

List the events of an issue:

    android signals crashes samples firebase/<issue-id> --firebase-app=1:123456789012:android:0123456789abcdef

List the events of an issue that happened on Samsung devices in the last 24
hours:

    android signals crashes samples firebase/<issue-id> --firebase-app=1:123456789012:android:0123456789abcdef --device=Samsung --timeframe=24h

List the events of an issue as JSON:

    android signals crashes samples firebase/<issue-id> --firebase-app=1:123456789012:android:0123456789abcdef --format=json