---
title: https://developer.android.com/tools/agents/android-cli/commands/device_remote_remove
url: https://developer.android.com/tools/agents/android-cli/commands/device_remote_remove
source: md.txt
---

Removes a remote device reservation.

## Usage

    android device remote remove [-h] <reservation-id>

## Options

- `-h,--help` - Shows the help message for the specified command.

`remote` options:

- `--project=PARAM` - The Google Cloud project ID.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<reservation-id>` - ID of the reservation.

## Description

`android device remote remove` ends a reservation and releases the device. Remove reservations as soon as you are done to stop being billed for the device.

### Examples

Remove reservation `abc123`:

    android device remote remove abc123 --project=my-project