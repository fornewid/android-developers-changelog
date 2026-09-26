---
title: https://developer.android.com/tools/agents/android-cli/commands/emulator_start
url: https://developer.android.com/tools/agents/android-cli/commands/emulator_start
source: md.txt
---

Launches the specified virtual device. This command returns when the emulator is fully started and ready to use.

## Usage

    android emulator start [-h] [--cold] [--headless] <device>

## Options

- `--cold` - Starts the emulator without loading from a snapshot.
- `--headless` - Starts the emulator without a window.
- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<device>` - The Android Virtual Device (AVD) to start. Use [`android emulator list`](https://developer.android.com/tools/agents/android-cli/commands/emulator_list) to see available devices.

## Description

`android emulator start` boots the specified Android Virtual Device (AVD) and blocks until the device has finished booting and is ready to accept `adb` and CLI commands.

### Configure boot options

- `--cold`: Performs a cold boot from scratch instead of loading from a saved quick-boot snapshot.
- `--headless`: Runs the emulator in the background without opening a graphical window---ideal for automated agent workflows.

### Examples

Start the `medium_phone` virtual device:

    android emulator start medium_phone

Cold-boot the `medium_phone` virtual device in headless mode:

    android emulator start --cold --headless medium_phone