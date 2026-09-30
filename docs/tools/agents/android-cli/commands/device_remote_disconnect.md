---
title: https://developer.android.com/tools/agents/android-cli/commands/device_remote_disconnect
url: https://developer.android.com/tools/agents/android-cli/commands/device_remote_disconnect
source: md.txt
---

Disconnects a remote device.

## Usage

    android device remote disconnect [-h] <reservation-id>

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

`android device remote disconnect` disconnects the device of a reservation from `adb` and stops the background connection. The reservation isn't removed, so you can connect to the device again with `android device remote connect`.

### Examples

Disconnect the device of reservation `abc123`:

    android device remote disconnect abc123 --project=my-project