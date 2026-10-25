---
title: https://developer.android.com/tools/agents/android-cli/commands/device
url: https://developer.android.com/tools/agents/android-cli/commands/device
source: md.txt
---

Manage Android devices. Mirror connected devices or emulators in a desktop
window and manage remote physical device reservations.

## Usage

    android device [-h]

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Subcommands

- **[`hub`](https://developer.android.com/tools/agents/android-cli/commands/device_hub)** - Launches a desktop window for real-time screen mirroring and interactive control of a connected Android device or emulator.
- **[`remote`](https://developer.android.com/tools/agents/android-cli/commands/device_remote)** - Manage remote physical devices. Includes commands to list, reserve, connect to, and manage remote device reservations.

## Description

The `android device` command set manages connected Android devices, emulators,
and remote device reservations.

Use [`android device hub`](https://developer.android.com/tools/agents/android-cli/commands/device_hub) to open a desktop window for real-time
screen mirroring and interactive control of a connected physical device or
emulator.

Use the [`android device remote`](https://developer.android.com/tools/agents/android-cli/commands/device_remote) commands to reserve physical
devices hosted in Google data centers and connect to them through `adb` as if
they were attached to your machine.