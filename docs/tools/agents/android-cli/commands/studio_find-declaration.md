---
title: https://developer.android.com/tools/agents/android-cli/commands/studio_find-declaration
url: https://developer.android.com/tools/agents/android-cli/commands/studio_find-declaration
source: md.txt
---

Finds the declaration of a symbol.

## Usage

    android studio find-declaration [-h] [--context-file=PARAM] [--pid=PARAM] [--project=PARAM] [--short] <symbol>

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

- `<symbol>` - The symbol to find the declaration for.

## Description

`android studio find-declaration` locates the exact declaration site of a symbol (class, method, function, property, field, constant, or Android resource) across the open project using Android Studio's semantic index.

Requires Android Studio Quail 2 or higher.

If multiple symbols share the same name across modules or packages, pass `--context-file=<path>` pointing to a source file that references the symbol so Android Studio can resolve the symbol using that file's imports and scope. Pass `--short` to output only the matched file path and line number.

### Examples

Find the declaration of `HotelDetailScreen` in compact format:

    android studio find-declaration --short HotelDetailScreen

Find a declaration using a context file to disambiguate imports:

    android studio find-declaration --context-file=app/src/main/java/com/example/myapp/MainActivity.kt HotelDetailScreen