---
title: https://developer.android.com/tools/agents/android-cli/commands/signals_crashes
url: https://developer.android.com/tools/agents/android-cli/commands/signals_crashes
source: md.txt
---

Lists, describes, and analyzes field-reported crash, ANR, and non-fatal issues.

## Usage

    android signals crashes [-h] [--firebase-app=PARAM]

## Options

- `--firebase-app=PARAM` - Firebase app ID to query in Crashlytics (e.g. '1::android:').
- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Subcommands

- **[`describe`](https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_describe)** - Displays detailed metadata, OS and device distributions, stack traces, custom keys, and logs for an issue cluster.
- **[`facets`](https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_facets)** - Breaks down crash event counts across one or more dimensions ('app-version', 'api-level', 'device') and lists valid filter values.
- **[`list`](https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_list)** - Lists field-reported crash, ANR, and non-fatal issue clusters with affected user and event counts.
- **[`samples`](https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_samples)** - Lists individual sample crash events with timestamps, devices, and API levels for an issue cluster.

## Description

The `android signals crashes` command set lists and investigates the crash, ANR,
and non-fatal issues that your app reports in the field, grouped into issue
clusters.

### Typical workflow

Here is the sequence of commands for a typical workflow:

1. Run [`android signals crashes list`](https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_list) to find the issues that affect the most users, and note the `Issue ID` of the issue to investigate.
2. Run [`android signals crashes describe <issue-id>`](https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_describe) to print its stack trace, its distributions, and the metadata of a sample event.
3. Run [`android signals crashes facets <dimension...>`](https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_facets) to see how the crash events are spread across app versions, API levels, and devices, and pass the values that it prints back as filters to the other commands.
4. Run [`android signals crashes samples <issue-id>`](https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_samples) to list the individual events of the issue, and inspect one of them with `android signals crashes describe <issue-id> --sample-id=<sample-id>`.

For out-of-memory crashes and memory limiter kills, inspect the heap dumps
collected for them using [`android signals heaps`](https://developer.android.com/tools/agents/android-cli/commands/signals_heaps).

### Select an app (`--firebase-app`)

Pass `--firebase-app=<app-id>` (for example,
`1:<project_number>:android:<hash>`) to query an app in Crashlytics. To avoid
passing the app every time, add defaults to your `~/.androidrc` file. Run
[`android signals context`](https://developer.android.com/tools/agents/android-cli/commands/signals_context) to list the apps that your account
can access.

Issue IDs returned by `list` are prefixed with `firebase/`. The `describe` and
`samples` commands infer the source from this prefix.

Crashlytics filters app versions by version name or code, reports non-fatal
issues, and records custom keys and logs.

### Examples

List the issues of an app:

    android signals crashes list --firebase-app=1:123456789012:android:0123456789abcdef

Describe an issue:

    android signals crashes describe firebase/<issue-id> --firebase-app=1:123456789012:android:0123456789abcdef