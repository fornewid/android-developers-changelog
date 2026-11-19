---
title: https://developer.android.com/tools/agents/android-cli/commands/emulator_create
url: https://developer.android.com/tools/agents/android-cli/commands/emulator_create
source: md.txt
---

> Documentation index: https://developer.android.com/tools/agents/android-cli/commands/llms.txt

Creates a virtual device.

## Usage

```bash
android emulator create [-h] [--list-profiles] [<profile>]
```

## Options

- `-h,--help` - Shows the help message for the specified command.
- `--list-profiles` - Lists the device profiles that can be used to create a device.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<profile>` - Creates the appropriate device for the selected profile (for example, phone, foldable, tablet, or desktop).

## Description

`android emulator create` creates a new Android Virtual Device (AVD) configured
for the specified device profile. If `<profile>` is omitted, the default
`medium_phone` profile is created.

### List device profiles (`--list-profiles`)

Pass `--list-profiles` to display all supported hardware profiles (such as
phones, foldables, tablets, and desktops) without creating an AVD.

### Examples

List all available device profiles:

```bash
android emulator create --list-profiles
```

Create a virtual device using the default `medium_phone` profile:

```bash
android emulator create
```

Create foldable virtual devices with 1:1 and 4:3 inner displays:

```bash
android emulator create foldable_1_1
android emulator create foldable_4_3
```

Create a virtual device using the `large_desktop` profile:

```bash
android emulator create large_desktop
```