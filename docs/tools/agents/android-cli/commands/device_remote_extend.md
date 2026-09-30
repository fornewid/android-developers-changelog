---
title: https://developer.android.com/tools/agents/android-cli/commands/device_remote_extend
url: https://developer.android.com/tools/agents/android-cli/commands/device_remote_extend
source: md.txt
---

Extends a remote device reservation.

## Usage

    android device remote extend [-h] [--duration=PARAM] <reservation-id>

## Options

- `--duration=PARAM` - Minutes for which the reservation is to be extended.
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

`android device remote extend` adds time to a reservation that hasn't ended and prints its new end time.

### Configure extension options

- `--duration`: Number of minutes to add to the reservation.

### Examples

Extend reservation `abc123` by 30 minutes:

    android device remote extend abc123 --duration=30 --project=my-project