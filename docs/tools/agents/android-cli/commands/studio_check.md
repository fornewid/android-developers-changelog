---
title: https://developer.android.com/tools/agents/android-cli/commands/studio_check
url: https://developer.android.com/tools/agents/android-cli/commands/studio_check
source: md.txt
---

Checks the status of running Android Studio instances.

## Usage

    android studio check [-h]

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Description

`android studio check` verifies the connection between Android CLI and any running Android Studio instances, listing each instance's process ID (`pid`), IDE version, and open projects.

Requires Android Studio Quail 2 or higher.

### Understand the output

When connected to a running instance, `android studio check` outputs the process ID, IDE version, and project readiness status:

    pid: 32942
    version: Android Studio Quail
    Projects:
        READY     MyApplication /Users/username/AndroidStudioProjects/MyApplication

### Examples

Check the status of running Android Studio instances:

    android studio check