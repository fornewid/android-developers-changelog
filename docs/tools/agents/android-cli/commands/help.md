---
title: https://developer.android.com/tools/agents/android-cli/commands/help
url: https://developer.android.com/tools/agents/android-cli/commands/help
source: md.txt
---

Shows the help information for a specified command.

## Usage

    android help [-h] [COMMAND]

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `COMMAND` - The command to show help for.

## Description

`android help` displays usage syntax, available options, and subcommands for Android CLI or for a specific top-level command.

If `COMMAND` is omitted, `android help` prints the top-level CLI summary followed by the help summary of every available command. You can also pass `-h` or `--help` to any command or subcommand (for example, `android sdk install --help`).

### Examples

Display help for all commands:

    android help

Display help for a specific command:

    android help emulator