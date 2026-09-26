---
title: https://developer.android.com/tools/agents/android-cli/commands/emulator_stop
url: https://developer.android.com/tools/agents/android-cli/commands/emulator_stop
source: md.txt
---

Stops the specified virtual device.

## Usage

    android emulator stop [-h] [<device>]

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<device>` - The emulator name or serial number to stop. Optional if only one emulator is running.

## Description

`android emulator stop` shuts down a running Android Virtual Device (AVD).

If only a single emulator is currently running, `<device>` is optional. If multiple emulators are running, specify either the AVD name (for example, `medium_phone`) or its `adb` serial number (for example, `emulator-5554`).

### Examples

Stop the only running emulator:

    android emulator stop

Stop a specific emulator by its serial number:

    android emulator stop emulator-5554