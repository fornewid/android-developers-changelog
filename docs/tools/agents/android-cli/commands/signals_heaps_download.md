---
title: https://developer.android.com/tools/agents/android-cli/commands/signals_heaps_download
url: https://developer.android.com/tools/agents/android-cli/commands/signals_heaps_download
source: md.txt
---

Downloads heap dumps as Perfetto traces into a local directory.

## Usage

    android signals heaps download [-h] [--force] [--format=PARAM] [--output=PARAM] <heap-id...>

## Options

- `--force` - Downloads heap dumps again even if their files already exist.
- `--format=PARAM` - Output format ('text' or 'json'; default: 'text').
- `-h,--help` - Shows the help message for the specified command.
- `--output=PARAM` - Directory to download the heap dumps into (created if missing).

`heaps` options:

- `--firebase-app=PARAM` - Firebase app ID to query in Crashlytics (e.g. '1::android:').

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<heap-id...>` - Heap dumps to download (as returned by 'heaps list', for example 'firebase/6aa1776301a300013390aca1f5bfc99f').

## Description

`android signals heaps download` downloads one or more low-memory heap dumps
from Cloud Storage into a local directory as Perfetto traces.

Pass one or more heap dump IDs (as printed by
[`android signals heaps list`](https://developer.android.com/tools/agents/android-cli/commands/signals_heaps_list), for example
`firebase/<session-id>`) to download.

Pass `--output` to specify the local directory to store the downloaded traces.
The directory is created if it does not already exist.

Pass `--force` to re-download heap dumps that have already been saved locally.

### Examples

Download a single heap dump:

    android signals heaps download firebase/<heap-id> --output=./heaps --firebase-app=1:123456789012:android:0123456789abcdef

Download multiple heap dumps, overwriting existing files:

    android signals heaps download firebase/<id-1> firebase/<id-2> --output=./heaps --force --firebase-app=1:123456789012:android:0123456789abcdef

Download a heap dump as JSON output:

    android signals heaps download firebase/<heap-id> --output=./heaps --firebase-app=1:123456789012:android:0123456789abcdef --format=json