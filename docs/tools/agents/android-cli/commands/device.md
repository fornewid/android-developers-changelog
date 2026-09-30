---
title: https://developer.android.com/tools/agents/android-cli/commands/device
url: https://developer.android.com/tools/agents/android-cli/commands/device
source: md.txt
---

Manage physical Android devices. Create remote physical device reservations.

## Usage

    android device [-h]

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Subcommands

- **[`remote`](https://developer.android.com/tools/agents/android-cli/commands/device_remote)** - Manage remote physical devices. Includes commands to list, reserve, connect to, and manage remote device reservations.

## Description

The `android device` command set manages remote physical Android devices.

Use the [`android device remote`](https://developer.android.com/tools/agents/android-cli/commands/device_remote) commands to reserve physical devices hosted in Google data centers and connect to them through `adb` as if they were attached to your machine.