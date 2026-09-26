---
title: https://developer.android.com/tools/agents/android-cli/commands/studio
url: https://developer.android.com/tools/agents/android-cli/commands/studio
source: md.txt
---

Connects Android CLI to a running Android Studio instance to analyze files, find declarations and usages, render Compose previews, and look up library versions.

## Usage

    android studio [-h]

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Subcommands

- **[`analyze-file`](https://developer.android.com/tools/agents/android-cli/commands/studio_analyze-file)** - Analyzes a file in Android Studio.
- **[`check`](https://developer.android.com/tools/agents/android-cli/commands/studio_check)** - Checks the status of running Android Studio instances.
- **[`find-declaration`](https://developer.android.com/tools/agents/android-cli/commands/studio_find-declaration)** - Finds the declaration of a symbol.
- **[`find-usages`](https://developer.android.com/tools/agents/android-cli/commands/studio_find-usages)** - Finds usages of a symbol.
- **[`open-file`](https://developer.android.com/tools/agents/android-cli/commands/studio_open-file)** - Opens a file in Android Studio.
- **[`render-compose-preview`](https://developer.android.com/tools/agents/android-cli/commands/studio_render-compose-preview)** - Renders a Compose preview in Android Studio.
- **[`version-lookup`](https://developer.android.com/tools/agents/android-cli/commands/studio_version-lookup)** - Looks up the latest available versions of Maven artifacts, Android versions, and SDK tools.

## Description

The `android studio` command set connects Android CLI to a running instance of Android Studio. By delegating to the active IDE, you can run semantic code analysis, navigate symbol declarations and usages, open files in the editor, render Jetpack Compose `@Preview` functions, and query the latest library and tool versions.

### Verify IDE requirements

To use the `android studio` commands, you must have your project open in Android Studio Quail 2 or higher.

### Select an instance and project (`--pid` and `--project`)

Run [`android studio check`](https://developer.android.com/tools/agents/android-cli/commands/studio_check) first to verify connectivity and inspect open projects. If only one Android Studio instance is running or you invoke a command from inside an open project's directory, `--pid` and `--project` are automatically inferred.