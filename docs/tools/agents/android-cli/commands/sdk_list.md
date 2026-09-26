---
title: https://developer.android.com/tools/agents/android-cli/commands/sdk_list
url: https://developer.android.com/tools/agents/android-cli/commands/sdk_list
source: md.txt
---

Lists installed and available SDK packages.

## Usage

    android sdk list [-h] [--all] [--all-versions] [--beta] [--canary] [<pattern>]

## Options

- `--all` - Show all packages available in the repository.
- `--all-versions` - Show all versions for each package.
- `--beta` - Include beta packages.
- `--canary` - Include canary packages.
- `-h,--help` - Shows the help message for the specified command.

`sdk` options:

- `--ignore-outdated-xmls` - When installing or updating packages, do not update other packages' XML files.
- `--platform=PARAM` - Target platform `<os>_<arch>` (for example, `linux_x86_64`, `mac_arm64`, or `windows_x86`); defaults to the current host.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<pattern>` - Filter packages by pattern (supports `*`).

## Description

`android sdk list` displays currently installed SDK packages and available packages in the repository.

### Filter package listings

- `--all`: Includes available packages from the remote repository alongside installed packages.
- `--all-versions`: Displays all available versions for each package instead of only the latest version.
- `<pattern>`: Filters package paths using glob patterns (for example, `platforms/*` or `*emulator*`).
- `--canary`: Includes packages from the Canary channel in available package listings.
- `--beta`: Includes packages from the Beta channel in available package listings.

### Format package paths

Standard package paths use slashes (`/`) as the delimiter (for example, `platforms/android-34`). Semicolon paths (for example, `platforms;android-34`) are also supported for compatibility.

### Understand the output

    Installed packages:
      cmdline-tools/latest    12.0                   Android SDK Command-line Tools (latest)
      platforms/android-34    3.0        ->  3.1     Android SDK Platform 34

    Available packages:
      build-tools/34.0.0      34.0.0                 Android SDK Build-Tools 34
      emulator                33.1.24                Android Emulator

In the preceding output:

- Installed packages show the current version and available updates (indicated by `->`).
- Color coding highlights outdated packages.

### Examples

List installed packages:

    android sdk list

List all available packages matching a pattern:

    android sdk list --all "platforms/*"

List all available package versions including canary builds:

    android sdk list --all --all-versions --canary