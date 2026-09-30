---
title: https://developer.android.com/tools/agents/android-cli/commands/device_remote_connect
url: https://developer.android.com/tools/agents/android-cli/commands/device_remote_connect
source: md.txt
---

Connects to a reserved remote device.

## Usage

    android device remote connect [-h] <reservation-id>

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

`android device remote connect` waits for a reservation to be ready and connects the device to `adb` on a local port. The connection is kept alive by a background process, so the command returns as soon as the device is connected and the device stays available to `adb`, `android run`, `android install`, and other device commands.

The command prints the port that the device is connected on and the path of the background process log file.

### Examples

Connect to the device of reservation `abc123`:

    android device remote connect abc123 --project=my-project