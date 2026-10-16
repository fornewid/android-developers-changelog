---
title: https://developer.android.com/tools/agents/android-cli/commands/input_key
url: https://developer.android.com/tools/agents/android-cli/commands/input_key
source: md.txt
---

Press a hardware button, navigation key, or Android keycode.

## Usage

    android input key [-h] [--alt] [--ctrl] [--shift] <key>

## Options

- `--alt` - Press key with Alt modifier.
- `--ctrl` - Press key with Ctrl modifier.
- `-h,--help` - Shows the help message for the specified command.
- `--shift` - Press key with Shift modifier.

`input` options:

- `--device=PARAM` - Device serial number or emulator ID (as reported by 'adb devices').

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<key>` - Key name (back, home, recents, power, volume-up, volume-down, enter, tab, esc) or Android keycode.