---
title: https://developer.android.com/tools/agents/android-cli/commands/signals_heaps
url: https://developer.android.com/tools/agents/android-cli/commands/signals_heaps
source: md.txt
---

> Documentation index: https://developer.android.com/tools/agents/android-cli/commands/llms.txt

Lists, describes, and downloads heap dumps collected on low-memory events.

## Usage

```bash
android signals heaps [-h] --firebase-app=PARAM
```

## Options

- `--firebase-app=PARAM` - Firebase app ID to query in Crashlytics (e.g. '1::android:').
- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Subcommands

- **[`describe`](https://developer.android.com/tools/agents/android-cli/commands/signals_heaps_describe.md.txt)** - Describes a heap dump with the issue, metadata, custom keys, and logs of its Crashlytics event, without the stack trace.
- **[`download`](https://developer.android.com/tools/agents/android-cli/commands/signals_heaps_download.md.txt)** - Downloads heap dumps as Perfetto traces into a local directory.
- **[`list`](https://developer.android.com/tools/agents/android-cli/commands/signals_heaps_list.md.txt)** - Lists heap dumps with their collection time, app version, device, API level, and size.

## Description

The `android signals heaps` command set lists, inspects, and downloads heap
dumps collected on low-memory events (such as out-of-memory crashes and memory
limiter kills) and stored in Cloud Storage.

### Typical workflow

Here is the sequence of commands for a typical workflow:

1. Identify low-memory issues in [`android signals crashes list`](https://developer.android.com/tools/agents/android-cli/commands/signals_crashes_list.md.txt) (tagged `[OOM]` or `[MLK]`), or run [`android signals heaps list`](https://developer.android.com/tools/agents/android-cli/commands/signals_heaps_list.md.txt) to view all available heap dumps for your app.
2. Run [`android signals heaps describe <heap-id>`](https://developer.android.com/tools/agents/android-cli/commands/signals_heaps_describe.md.txt) to inspect a heap dump alongside the metadata, custom keys, and logs from its crash session.
3. Run [`android signals heaps download <heap-id...>`](https://developer.android.com/tools/agents/android-cli/commands/signals_heaps_download.md.txt) to download heap dumps as Perfetto traces into a local directory for analysis.

### Select an app (`--firebase-app`)

Pass `--firebase-app=<app-id>` (for example,
`1:<project_number>:android:<hash>`) to identify the app, or configure it in
`~/.androidrc`.

### Examples

List low-memory heap dumps:

```bash
android signals heaps list --firebase-app=1:123456789012:android:0123456789abcdef
```

Describe a heap dump:

```bash
android signals heaps describe firebase/<heap-id> --firebase-app=1:123456789012:android:0123456789abcdef
```

Download a heap dump into the `./heaps` directory:

```bash
android signals heaps download firebase/<heap-id> --output=./heaps --firebase-app=1:123456789012:android:0123456789abcdef
```