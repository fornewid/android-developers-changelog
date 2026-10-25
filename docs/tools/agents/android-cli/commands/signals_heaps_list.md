---
title: https://developer.android.com/tools/agents/android-cli/commands/signals_heaps_list
url: https://developer.android.com/tools/agents/android-cli/commands/signals_heaps_list
source: md.txt
---

Lists heap dumps with their collection time, app version, device, API level, and
size.

## Usage

    android signals heaps list [-h] [--api-level=PARAM] [--app-version=PARAM] [--device=PARAM] [--format=PARAM] [--kind=PARAM] [--limit=PARAM] [--sort-by=PARAM] [--timeframe=PARAM]

## Options

- `--api-level=PARAM` - Filters by Android API level or OS version (for example, '34', 'API 34', or 'Android 14').
- `--app-version=PARAM` - Filters by app version (version name or build version, for example '1.2.3' or '1.2.3 (1042)').
- `--device=PARAM` - Filters by device marketing name, model code, or manufacturer (for example, 'Pixel 8' or 'Samsung'; repeatable).
- `--format=PARAM` - Output format ('text' or 'json'; default: 'text').
- `-h,--help` - Shows the help message for the specified command.
- `--kind=PARAM` - Selects the kind of low-memory event ('oom', 'mlk', or 'all'; default: 'all').
- `--limit=PARAM` - Maximum number of results to return (1-5000; default: 100).
- `--sort-by=PARAM` - Sorts heap dumps in descending order ('time' or 'size'; default: 'time').
- `--timeframe=PARAM` - Time window to query ('24h', '7d', '30d', '60d', '90d'; default: '7d').

`heaps` options:

- `--firebase-app=PARAM` - Firebase app ID to query in Crashlytics (e.g. '1::android:').

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Description

`android signals heaps list` lists the heap dumps collected on low-memory events
for your app, with their collection time, kind (`OOM` or `MLK`), app version,
device, API level, and file size. By default, it lists up to 100 heap dumps from
the last seven days.

Pass the `Heap ID` (for example, `firebase/<session-id>`) of a row to
[`android signals heaps describe`](https://developer.android.com/tools/agents/android-cli/commands/signals_heaps_describe) to inspect the
associated crash event, or to
[`android signals heaps download`](https://developer.android.com/tools/agents/android-cli/commands/signals_heaps_download) to download the
Perfetto trace.

Pass `--firebase-app` or configure it in `~/.androidrc` to specify the app to
query.

### Filter and sort heap dumps

- `--kind`: Filters by kind of low-memory event (`oom`, `mlk`, or `all`; default: `all`).
- `--timeframe`: Restricts the query to a time window, for example `24h`, `7d`, `30d`, `60d`, or `90d`.
- `--app-version`, `--device`, `--api-level`: Restrict the query to heap dumps from a specific app version, device, or API level.
- `--sort-by`: Sorts the heap dumps by `time` or `size` in descending order (default: `time`).
- `--limit`: Caps the number of heap dumps that are printed (default: 100).
- `--format=json`: Prints the heap dumps as JSON, which is useful for scripts and agents.

### Examples

List the heap dumps of the last seven days:

    android signals heaps list --firebase-app=1:123456789012:android:0123456789abcdef

List out-of-memory heap dumps from the last 24 hours:

    android signals heaps list --firebase-app=1:123456789012:android:0123456789abcdef --kind=oom --timeframe=24h

List the 10 largest heap dumps:

    android signals heaps list --firebase-app=1:123456789012:android:0123456789abcdef --sort-by=size --limit=10