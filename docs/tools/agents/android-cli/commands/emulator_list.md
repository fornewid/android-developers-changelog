---
title: https://developer.android.com/tools/agents/android-cli/commands/emulator_list
url: https://developer.android.com/tools/agents/android-cli/commands/emulator_list
source: md.txt
---

Lists available virtual devices.

## Usage

    android emulator list [-h] [--long]

## Options

- `-h,--help` - Shows the help message for the specified command.
- `--long` - Give more detailed information.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Description

`android emulator list` lists all configured Android Virtual Devices (AVDs) on your machine.

Pass `--long` to include detailed metadata (AVD ID, AVD Name, API Level, Status, and Serial) for each AVD.

### Examples

List all available virtual devices:

    android emulator list

List virtual devices with detailed configuration information:

    android emulator list --long