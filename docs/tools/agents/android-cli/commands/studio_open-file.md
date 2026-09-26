---
title: https://developer.android.com/tools/agents/android-cli/commands/studio_open-file
url: https://developer.android.com/tools/agents/android-cli/commands/studio_open-file
source: md.txt
---

Opens a file in Android Studio.

## Usage

    android studio open-file [-h] [--pid=PARAM] [--project=PARAM] <path>

## Options

- `-h,--help` - Shows the help message for the specified command.
- `--pid=PARAM` - The PID of the Android Studio instance to connect to.
- `--project=PARAM` - The name or path of the project open in Android Studio to query. Use [`android studio check`](https://developer.android.com/tools/agents/android-cli/commands/studio_check) to get the names of available projects.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<path>` - The path of the file to open, relative to the current directory or absolute.

## Description

`android studio open-file` opens the specified source or resource file directly in the active editor window of a running Android Studio instance.

Requires Android Studio Quail 2 or higher.

### Examples

Open a Kotlin source file in the active Android Studio editor:

    android studio open-file app/src/main/java/com/example/myapp/ui/DetailScreen.kt