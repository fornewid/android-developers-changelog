---
title: https://developer.android.com/tools/agents/android-cli/commands/emulator_create
url: https://developer.android.com/tools/agents/android-cli/commands/emulator_create
source: md.txt
---

Creates a virtual device.

## Usage

    android emulator create [-h] [--list-profiles] [<profile>]

## Options

- `-h,--help` - Shows the help message for the specified command.
- `--list-profiles` - Lists the device profiles that can be used to create a device.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<profile>` - Creates a device with a specified profile. Creates the appropriate device for the selected profile (for example, phone, tablet, or desktop).

## Description

`android emulator create` creates a new Android Virtual Device (AVD) configured for the specified device profile. If `<profile>` is omitted, the default `medium_phone` profile is created.

### List device profiles (`--list-profiles`)

Pass `--list-profiles` to display all supported hardware profiles (such as phones, tablets, and desktops) without creating an AVD.

### Examples

List all available device profiles:

    android emulator create --list-profiles

Create a virtual device using the default `medium_phone` profile:

    android emulator create

Create a virtual device using the `large_desktop` profile:

    android emulator create large_desktop