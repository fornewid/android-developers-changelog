---
title: https://developer.android.com/tools/agents/android-cli/commands/signals
url: https://developer.android.com/tools/agents/android-cli/commands/signals
source: md.txt
---

Queries app stability and field telemetry from Crashlytics.

## Usage

    android signals [-h]

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Subcommands

- **[`context`](https://developer.android.com/tools/agents/android-cli/commands/signals_context)** - Lists accessible Crashlytics projects and apps.
- **[`crashes`](https://developer.android.com/tools/agents/android-cli/commands/signals_crashes)** - Lists, describes, and analyzes field-reported crash, ANR, and non-fatal issues.
- **[`heaps`](https://developer.android.com/tools/agents/android-cli/commands/signals_heaps)** - Lists, describes, and downloads heap dumps collected on low-memory events.

## Description

The `android signals` command set queries the stability and field telemetry of
your app from [Firebase Crashlytics](https://firebase.google.com/docs/crashlytics), and manages low-memory heap
dumps, so that you can find, triage, and investigate crashes, ANRs, and
non-fatal issues from your terminal.

Before you start, run `android auth login` to sign in with an account that has
access to your Firebase projects and apps.

### Typical workflow

Here is the sequence of commands for a typical workflow to investigate a crash:

1. Run [`android signals context`](https://developer.android.com/tools/agents/android-cli/commands/signals_context) to list the Firebase projects and apps that your account can access, and to find the app IDs to query.
2. Run [`android signals crashes list`](https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_list) with `--firebase-app` (or configure it in `~/.androidrc`) to list the issue clusters reported for your app with the number of users and events that each one affects, and note the `Issue ID` of the issue to investigate.
3. Run [`android signals crashes describe <issue-id>`](https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_describe) to print the stack trace, the API level and device distributions, and the metadata of a sample event of that issue.
4. Run [`android signals crashes facets <dimension...>`](https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_facets) to break down the crash events by app version, API level, or device, and pass the values that it prints back as filters to narrow down the other commands.
5. Run [`android signals crashes samples <issue-id>`](https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_samples) to list the individual events of the issue, and run `android signals crashes describe <issue-id> --sample-id=<sample-id>` with the `Sample ID` of one of them to inspect that specific event.

### Low-memory events and heap dumps

For out-of-memory crashes and memory limiter kills, Crashlytics collects heap
dumps and stores them in Cloud Storage. Use
[`android signals heaps`](https://developer.android.com/tools/agents/android-cli/commands/signals_heaps) to list and download them:

1. Run [`android signals heaps list`](https://developer.android.com/tools/agents/android-cli/commands/signals_heaps_list) with `--firebase-app` to view collected heap dumps.
2. Run [`android signals heaps describe <heap-id>`](https://developer.android.com/tools/agents/android-cli/commands/signals_heaps_describe) to view event details associated with a heap dump.
3. Run [`android signals heaps download <heap-id...>`](https://developer.android.com/tools/agents/android-cli/commands/signals_heaps_download) to download heap dumps as Perfetto traces for local inspection.

### Select an app

Pass `--firebase-app=<app-id>` (for example,
`1:<project_number>:android:<hash>`) to query an app in Firebase Crashlytics.

Issue IDs returned by `crashes list` are prefixed with `firebase/`.

### Configure defaults (`~/.androidrc`)

To avoid passing the app every time, add defaults to your `~/.androidrc` file:

    signals crashes --firebase-app=1:123456789012:android:0123456789abcdef

### Examples

Find the crash that affects the most users, and print its stack trace:

    android signals crashes list --firebase-app=1:123456789012:android:0123456789abcdef --type=crash --sort-by=users --limit=5
    android signals crashes describe firebase/<issue-id> --firebase-app=1:123456789012:android:0123456789abcdef --include=stack

Break down the events reported for an app by app version:

    android signals crashes facets app-version --firebase-app=1:123456789012:android:0123456789abcdef

List and download low-memory heap dumps:

    android signals heaps list --firebase-app=1:123456789012:android:0123456789abcdef
    android signals heaps download firebase/<heap-id> --output=heaps --firebase-app=1:123456789012:android:0123456789abcdef