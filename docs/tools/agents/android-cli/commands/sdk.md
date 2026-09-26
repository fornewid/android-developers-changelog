---
title: https://developer.android.com/tools/agents/android-cli/commands/sdk
url: https://developer.android.com/tools/agents/android-cli/commands/sdk
source: md.txt
---

Manages the Android SDK installation. Includes commands to install, update, remove, and list available and installed SDK packages.

## Usage

    android sdk [-h] [--ignore-outdated-xmls] [--platform=PARAM]

## Options

- `-h,--help` - Shows the help message for the specified command.
- `--ignore-outdated-xmls` - When installing or updating packages, do not update other packages' XML files.
- `--platform=PARAM` - Target platform `<os>_<arch>` (for example, `linux_x86_64`, `mac_arm64`, or `windows_x86`); defaults to the current host.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Subcommands

- **[`install`](https://developer.android.com/tools/agents/android-cli/commands/sdk_install)** - Installs SDK packages.
- **[`list`](https://developer.android.com/tools/agents/android-cli/commands/sdk_list)** - Lists installed and available SDK packages.
- **[`remove`](https://developer.android.com/tools/agents/android-cli/commands/sdk_remove)** - Removes packages from the SDK.
- **[`update`](https://developer.android.com/tools/agents/android-cli/commands/sdk_update)** - Updates one or all packages to the latest version.

## Description

The `android sdk` command set provides tools to inspect and manage installed and available Android SDK packages.

### Format package paths

Package paths are designated using slashes (`/`) as the standard nomenclature (for example, `platforms/android-34`, `build-tools/34.0.0`, `cmdline-tools/latest`). Semicolon-delimited paths (for example, `platforms;android-34`) are also supported for backward compatibility with legacy SDK tools.

### Select a release channel

Packages are published across different stability channels:

- **Stable** (default): Recommended for general development.
- **Beta**: Feature-complete previews.
- **Canary**: Bleeding-edge experimental builds.

Use the `--canary` or `--beta` options with `list`, `install`, or `update` to access packages from preview channels.