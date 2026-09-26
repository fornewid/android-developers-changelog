---
title: https://developer.android.com/tools/agents/android-cli/commands/studio_find-usages
url: https://developer.android.com/tools/agents/android-cli/commands/studio_find-usages
source: md.txt
---

Finds usages of a symbol.

## Usage

    android studio find-usages [-h] [--context-file=PARAM] [--pid=PARAM] [--project=PARAM] [--short] <symbol>

## Options

- `--context-file=PARAM` - Optional path to a file containing a reference to the symbol, relative to the current directory or absolute.
- `-h,--help` - Shows the help message for the specified command.
- `--pid=PARAM` - The PID of the Android Studio instance to connect to.
- `--project=PARAM` - The name or path of the project open in Android Studio to query. Use [`android studio check`](https://developer.android.com/tools/agents/android-cli/commands/studio_check) to get the names of available projects.
- `--short` - Only show the location in files with matches.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<symbol>` - The symbol to find usages for.

## Description

`android studio find-usages` finds all references and call sites of a symbol across the open project using Android Studio's semantic analysis engine.

Requires Android Studio Quail 2 or higher.

Pass `--context-file=<path>` to disambiguate overloaded or identically named symbols, and pass `--short` to output only the matched file locations.

### Examples

Find all usages of `HotelDetailScreen` in compact format:

    android studio find-usages --short HotelDetailScreen