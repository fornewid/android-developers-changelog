---
title: https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_facets
url: https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_facets
source: md.txt
---

Breaks down crash event counts across one or more dimensions ('app-version',
'api-level', 'device') and lists valid filter values.

## Usage

    android signals crashes facets [-h] [--api-level=PARAM] [--app-version=PARAM] [--device=PARAM] [--format=PARAM] [--limit=PARAM] [--timeframe=PARAM] [--type=PARAM] <dimension...>

## Options

- `--api-level=PARAM` - Filters by Android API level or OS version (for example, '34', 'API 34', or 'Android 14').
- `--app-version=PARAM` - Filters by app version (version name or build version, for example '1.2.3' or '1.2.3 (1042)').
- `--device=PARAM` - Filters by device marketing name, model code, or manufacturer (for example, 'Pixel 8' or 'Samsung'; repeatable).
- `--format=PARAM` - Output format ('text' or 'json'; default: 'text').
- `-h,--help` - Shows the help message for the specified command.
- `--limit=PARAM` - Maximum number of top-level results to return (1-5000; default: 100; multi-dimension queries cap at 10 for 2 dimensions and 5 for 3 dimensions).
- `--timeframe=PARAM` - Time window to query ('24h', '7d', '30d', '60d', '90d'; default: '7d').
- `--type=PARAM` - Filters by issue type ('crash' or 'fatal', 'anr', 'non-fatal'; default: all types).

`crashes` options:

- `--firebase-app=PARAM` - Firebase app ID to query in Crashlytics (e.g. '1::android:').

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<dimension...>` - One or more dimensions to break down ('app-version' or 'version', 'api-level' or 'os', 'device').

## Description

`android signals crashes facets` counts the crash events of your app across one
or more dimensions and prints the result as a tree, with the number of events
for each value. It answers questions like "which app version crashes the most?"
or "is this ANR specific to one device?".

The dimensions are `app-version` (or `version`), `api-level` (or `os`), and
`device`. Pass several of them, separated by spaces or commas, to nest the
breakdown. For example, `app-version device` lists the devices with the most
events for each app version.

The values that the tree prints are valid filter values. Pass them back to
`--app-version`, `--api-level`, and `--device` to narrow down
[`android signals crashes list`](https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_list) and the other
`android signals crashes` commands to the events of that app version, API level,
or device.

Pass `--firebase-app` or configure it in `~/.androidrc` to specify the app to
query.

### Examples

Break down the crash events of the last seven days by app version:

    android signals crashes facets app-version --firebase-app=1:123456789012:android:0123456789abcdef

Break down the ANRs of the last 24 hours by API level, then by device:

    android signals crashes facets api-level device --firebase-app=1:123456789012:android:0123456789abcdef --type=anr --timeframe=24h

Break down the crash events of version `1.2.3` by device:

    android signals crashes facets device --firebase-app=1:123456789012:android:0123456789abcdef --app-version=1.2.3