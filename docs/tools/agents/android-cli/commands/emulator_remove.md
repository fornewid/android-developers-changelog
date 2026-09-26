---
title: https://developer.android.com/tools/agents/android-cli/commands/emulator_remove
url: https://developer.android.com/tools/agents/android-cli/commands/emulator_remove
source: md.txt
---

Deletes a virtual device.

## Usage

    android emulator remove [-h] [--force] <device>

## Options

- `--force` - Forces removal of the `.ini` file even if the corresponding `.avd` directory doesn't exist.
- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<device>` - The Android Virtual Device (AVD) to remove. Use [`android emulator list`](https://developer.android.com/tools/agents/android-cli/commands/emulator_list) to see available devices.

## Description

`android emulator remove` deletes an Android Virtual Device (AVD) and removes its configuration and disk images from your machine.

Pass `--force` to remove an orphaned `.ini` configuration file even if the corresponding `.avd` directory no longer exists.

### Examples

Remove the `medium_phone` virtual device:

    android emulator remove medium_phone

Force remove a broken or partially deleted virtual device:

    android emulator remove --force medium_phone