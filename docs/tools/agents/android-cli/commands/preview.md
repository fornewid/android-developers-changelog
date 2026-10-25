---
title: https://developer.android.com/tools/agents/android-cli/commands/preview
url: https://developer.android.com/tools/agents/android-cli/commands/preview
source: md.txt
---

Renders Jetpack Compose @Preview functions to PNG images and optionally exports
component tree JSON files. Runs without a device or an IDE.

## Usage

    android preview [-h]

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Subcommands

- **[`list`](https://developer.android.com/tools/agents/android-cli/commands/preview_list)** - Lists available Jetpack Compose @Preview functions in a target.
- **[`render`](https://developer.android.com/tools/agents/android-cli/commands/preview_render)** - Builds a target and renders its Jetpack Compose @Preview functions to PNG images and optional component tree JSON files.

## Description

The `android preview` command set builds an Android target and lists or renders
its Jetpack Compose `@Preview` functions headlessly on the host machine (without
a running device, emulator, or Android Studio instance).

- Run [`android preview list`](https://developer.android.com/tools/agents/android-cli/commands/preview_list) to discover available `@Preview` functions in a target.
- Run [`android preview render`](https://developer.android.com/tools/agents/android-cli/commands/preview_render) to render one or more `@Preview` functions to PNG images and optional component tree JSON files.