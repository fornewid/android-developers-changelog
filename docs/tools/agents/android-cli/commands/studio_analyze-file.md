---
title: https://developer.android.com/tools/agents/android-cli/commands/studio_analyze-file
url: https://developer.android.com/tools/agents/android-cli/commands/studio_analyze-file
source: md.txt
---

Analyzes a file in Android Studio.

## Usage

    android studio analyze-file [-h] [--pid=PARAM] [--project=PARAM] <path>

## Options

- `-h,--help` - Shows the help message for the specified command.
- `--pid=PARAM` - The PID of the Android Studio instance to connect to.
- `--project=PARAM` - The name or path of the project open in Android Studio to query. Use [`android studio check`](https://developer.android.com/tools/agents/android-cli/commands/studio_check) to get the names of available projects.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<path>` - The path of the file to analyze, relative to the current directory or absolute.

## Description

`android studio analyze-file` analyzes a Kotlin, Java, or XML file in Android Studio for compiler errors, warnings, and Android Lint inspections using the IDE's live inspection engine.

Requires Android Studio Quail 2 or higher.

### Examples

Analyze `MainActivity.kt` in the `MyApplication` project:

    android studio analyze-file \
      --project=MyApplication \
      app/src/main/java/com/example/myapp/MainActivity.kt