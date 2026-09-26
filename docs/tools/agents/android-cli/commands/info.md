---
title: https://developer.android.com/tools/agents/android-cli/commands/info
url: https://developer.android.com/tools/agents/android-cli/commands/info
source: md.txt
---

Prints environment information including SDK location, connected devices, and configuration variables.

## Usage

    android info [-h] [<field>]

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<field>` - The specific field to print the value of. If omitted, prints all fields.

## Description

`android info` displays environment and configuration details for your Android CLI installation, including the active Android SDK path (`sdk`) and CLI version (`version`).

To temporarily override the active Android SDK path for a single command, pass the global `--sdk=<path-to-sdk>` option, or add `--sdk=<path-to-sdk>` to your `~/.androidrc` configuration file.

### Query a specific field

Provide an optional `<field>` argument (such as `sdk` or `version`) to print only the raw value of that field---useful for shell scripts and automation.

### Examples

Print all environment information:

    android info

Print only the default Android SDK path:

    android info sdk