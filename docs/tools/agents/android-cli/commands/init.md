---
title: https://developer.android.com/tools/agents/android-cli/commands/init
url: https://developer.android.com/tools/agents/android-cli/commands/init
source: md.txt
---

Initializes the environment for Android CLI. Sets up required configurations, directories, and default skills.

## Usage

    android init [-h]

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Description

`android init` initializes your development environment for AI agents by installing the bundled `android-cli` skill into all detected agent skill directories.

> [!NOTE]
> **Note:** To install additional Android skills or manage skills for specific agents and projects, use [`android skills add`](https://developer.android.com/tools/agents/android-cli/commands/skills_add).

### Examples

Initialize the `android-cli` skill for your environment:

    android init