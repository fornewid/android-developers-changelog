---
title: https://developer.android.com/tools/agents/android-cli/commands/device_remote_create
url: https://developer.android.com/tools/agents/android-cli/commands/device_remote_create
source: md.txt
---

Creates a reservation for a remote device.

## Usage

    android device remote create [-h] [--connect] [<codename>/<api>]

## Options

- `--connect` - Connects to the device once the reservation is created.
- `-h,--help` - Shows the help message for the specified command.

`remote` options:

- `--project=PARAM` - The Google Cloud project ID.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<codename>/<api>` - Device to create a reservation for, for example tokay/34.

## Description

`android device remote create` reserves a physical device and prints the ID of the new reservation and when it ends. Specify the device as `<codename>/<api>`, as shown by `android device remote models`. If the device is not valid or not available, the command prints the list of available devices.

By default, the command then waits for the reservation to be ready and connects the device to `adb`, as `android device remote connect` does.

### Configure creation options

- `--connect`: Connects to the device once the reservation is created. Defaults to `true`. Pass `--connect=false` to only create the reservation and print the command to connect to it later.

### Examples

Reserve a `tokay` device running API level 34 in the `my-project` project and connect to it:

    android device remote create tokay/34 --project=my-project

Reserve a `tokay` device running API level 34 without connecting to it:

    android device remote create tokay/34 --connect=false --project=my-project