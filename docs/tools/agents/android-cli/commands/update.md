---
title: https://developer.android.com/tools/agents/android-cli/commands/update
url: https://developer.android.com/tools/agents/android-cli/commands/update
source: md.txt
---

Updates Android CLI to the latest version.

## Usage

    android update [-h] [--url=PARAM]

## Options

- `-h,--help` - Shows the help message for the specified command.
- `--url=PARAM` - The URL to download the update from.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Description

`android update` checks for a newer release of Android CLI and updates the binary in place.

### Examples

Update Android CLI to the latest release:

    android update