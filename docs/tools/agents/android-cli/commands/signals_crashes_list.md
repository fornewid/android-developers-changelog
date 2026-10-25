---
title: https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_list
url: https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_list
source: md.txt
---

Lists field-reported crash, ANR, and non-fatal issue clusters with affected user
and event counts.

## Usage

    android signals crashes list [-h] [--api-level=PARAM] [--app-version=PARAM] [--device=PARAM] [--format=PARAM] [--limit=PARAM] [--min-event-count=PARAM] [--min-user-count=PARAM] [--sort-by=PARAM] [--timeframe=PARAM] [--type=PARAM]

## Options

- `--api-level=PARAM` - Filters by Android API level or OS version (for example, '34', 'API 34', or 'Android 14').
- `--app-version=PARAM` - Filters by app version (version name or build version, for example '1.2.3' or '1.2.3 (1042)').
- `--device=PARAM` - Filters by device marketing name, model code, or manufacturer (for example, 'Pixel 8' or 'Samsung'; repeatable).
- `--format=PARAM` - Output format ('text' or 'json'; default: 'text').
- `-h,--help` - Shows the help message for the specified command.
- `--limit=PARAM` - Maximum number of results to return (1-5000; default: 100).
- `--min-event-count=PARAM` - Only includes issues with at least the specified number of events (\>= 0).
- `--min-user-count=PARAM` - Only includes issues affecting at least the specified number of users (\>= 0).
- `--sort-by=PARAM` - Sorts issues by count in descending order ('users' or 'events').
- `--timeframe=PARAM` - Time window to query ('24h', '7d', '30d', '60d', '90d'; default: '7d').
- `--type=PARAM` - Filters by issue type ('crash' or 'fatal', 'anr', 'non-fatal'; default: all types).

`crashes` options:

- `--firebase-app=PARAM` - Firebase app ID to query in Crashlytics (e.g. '1::android:').

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Description

`android signals crashes list` prints a table of the issue clusters reported for
your app, with the type of each issue (crash, ANR, or non-fatal), the number of
users and events that it affects, and its title. By default, it lists up to 100
issues of all types from the last seven days.

Pass the `Issue ID` (prefixed with `firebase/`) of a row to
[`android signals crashes describe`](https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_describe) to inspect the
issue, or to [`android signals crashes samples`](https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_samples) to
list its individual events.

Pass `--firebase-app` or configure it in `~/.androidrc` to specify the app to
query.

Memory issues are tagged `[OOM]` (Out of Memory) or `[MLK]` (Memory Limiter
Kill). Run [`android signals heaps list`](https://developer.android.com/tools/agents/android-cli/commands/signals_heaps_list) to inspect the
heap dumps collected for them.

### Filter and sort the issues

- `--timeframe`: Restricts the query to a time window, for example `24h`, `7d`, `30d`, `60d`, or `90d`.
- `--type`: Restricts the query to `crash`, `anr`, or `non-fatal` issues.
- `--app-version`, `--device`, `--api-level`: Restrict the query to the events of a build, a device, or an Android version. Run [`android signals crashes facets`](https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_facets) to list the values that match events.
- `--min-user-count`, `--min-event-count`: Hide the issues that affect fewer users or events than the given number.
- `--sort-by`: Sorts the issues by `users` or `events`, in descending order.
- `--limit`: Caps the number of issues that are printed.
- `--format=json`: Prints the issues as JSON, which is useful for scripts and agents.

### Examples

List the issues of the last seven days:

    android signals crashes list --firebase-app=1:123456789012:android:0123456789abcdef

List the 10 ANRs that affected the most users:

    android signals crashes list --firebase-app=1:123456789012:android:0123456789abcdef --type=anr --sort-by=users --limit=10

List the crashes of version `1.2.3` on Pixel 8 devices running API level 34:

    android signals crashes list --firebase-app=1:123456789012:android:0123456789abcdef --app-version=1.2.3 --device="Pixel 8" --api-level=34

List the issues of the last 24 hours as JSON:

    android signals crashes list --firebase-app=1:123456789012:android:0123456789abcdef --timeframe=24h --format=json