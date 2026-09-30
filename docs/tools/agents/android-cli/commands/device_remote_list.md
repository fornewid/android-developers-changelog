---
title: https://developer.android.com/tools/agents/android-cli/commands/device_remote_list
url: https://developer.android.com/tools/agents/android-cli/commands/device_remote_list
source: md.txt
---

Lists remote device reservations.

## Usage

    android device remote list [-h] [--all] [--short] [<reservation-id>]

## Options

- `--all` - Prints all reservations irrespective of their state.
- `-h,--help` - Shows the help message for the specified command.
- `--short` - Prints only the ID of each reservation.

`remote` options:

- `--project=PARAM` - The Google Cloud project ID.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<reservation-id>` - Restricts the output to the reservation with this ID.

## Description

`android device remote list` prints a table of your reservations with their state, end time, and device details. By default, only reservations that haven't ended are listed.

Pass a `<reservation-id>` to print only that reservation, regardless of its state.

### Configure listing options

- `--all`: Includes reservations that have already ended.
- `--short`: Prints only the ID of each reservation, one per line, which is useful for scripting.

### Examples

List your active reservations:

    android device remote list --project=my-project

List the IDs of all reservations, including the ones that have ended:

    android device remote list --all --short --project=my-project

Show the details of a single reservation:

    android device remote list abc123 --project=my-project