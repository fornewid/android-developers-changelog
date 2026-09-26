---
title: https://developer.android.com/tools/agents/android-cli/commands/emulator
url: https://developer.android.com/tools/agents/android-cli/commands/emulator
source: md.txt
---

Manages Android Virtual Devices (AVDs). Includes commands to start, stop, list, and view details about emulators.

## Usage

    android emulator [-h]

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Subcommands

- **[`create`](https://developer.android.com/tools/agents/android-cli/commands/emulator_create)** - Creates a virtual device.
- **[`list`](https://developer.android.com/tools/agents/android-cli/commands/emulator_list)** - Lists available virtual devices.
- **[`remove`](https://developer.android.com/tools/agents/android-cli/commands/emulator_remove)** - Deletes a virtual device.
- **[`start`](https://developer.android.com/tools/agents/android-cli/commands/emulator_start)** - Launches the specified virtual device. This command returns when the emulator is fully started and ready to use.
- **[`stop`](https://developer.android.com/tools/agents/android-cli/commands/emulator_stop)** - Stops the specified virtual device.

## Description

The `android emulator` command set creates, inspects, launches, stops, and deletes Android Virtual Devices (AVDs) from the command line.

### Typical workflow

Here is the sequence of commands for a typical workflow:

1. Run [`android emulator create`](https://developer.android.com/tools/agents/android-cli/commands/emulator_create) to create a virtual device from a standard hardware profile (such as `medium_phone` or `large_desktop`).
2. Run [`android emulator list`](https://developer.android.com/tools/agents/android-cli/commands/emulator_list) to inspect configured AVDs.
3. Run [`android emulator start <device>`](https://developer.android.com/tools/agents/android-cli/commands/emulator_start) to launch the virtual device and wait until it finishes booting.
4. Run [`android emulator stop`](https://developer.android.com/tools/agents/android-cli/commands/emulator_stop) to shut down a running emulator instance.