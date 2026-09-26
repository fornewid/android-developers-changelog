---
title: https://developer.android.com/tools/agents/android-cli/commands/skills_find
url: https://developer.android.com/tools/agents/android-cli/commands/skills_find
source: md.txt
---

Searches for available skills in the repository matching a keyword.

## Usage

    android skills find [-h] keyword

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `keyword` - Keyword to search for.

## Description

`android skills find` searches the official Android skills catalog for skills whose name or description matches the given `keyword`.

### Examples

Search for skills related to performance:

    android skills find performance

Search for skills related to Jetpack Compose:

    android skills find compose