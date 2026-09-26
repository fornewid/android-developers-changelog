---
title: https://developer.android.com/tools/agents/android-cli/commands/sdk_update
url: https://developer.android.com/tools/agents/android-cli/commands/sdk_update
source: md.txt
---

Updates one or all packages to the latest version.

## Usage

    android sdk update [-h] [--beta] [--canary] [--force] [<package>]

## Options

- `--beta` - Include beta packages.
- `--canary` - Include canary packages.
- `--force` - Force downgrading to an older version.
- `-h,--help` - Shows the help message for the specified command.

`sdk` options:

- `--ignore-outdated-xmls` - When installing or updating packages, do not update other packages' XML files.
- `--platform=PARAM` - Target platform `<os>_<arch>` (for example, `linux_x86_64`, `mac_arm64`, or `windows_x86`); defaults to the current host.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<package>` - Name of the package to update (optional).

## Description

`android sdk update` updates installed packages to their latest available versions.

If no package name is supplied, all installed packages are evaluated for updates. Specify a package name to update only that specific package.

### Format package paths

The standard path separator is `/` (for example, `platforms/android-34`). Semicolon-delimited syntax (for example, `platforms;android-34`) is also accepted.

### Select a release channel (`--canary` and `--beta`)

By default, `update` checks for updates in the **Stable** channel.

- `--canary`: Checks Canary, Beta, and Stable channels for newer versions.
- `--beta`: Checks Beta and Stable channels for newer versions.

### Force downgrade packages (`--force`)

If a package was previously installed from a Canary channel, running `android sdk update` without `--canary` attempts to update to the latest Stable package. Because the Stable version may have a lower version number than the Canary package, this is considered a downgrade. In such cases, the update fails with a warning unless `--force` is supplied.

### Examples

Update all installed packages to the latest stable versions:

    android sdk update

Update only the emulator package:

    android sdk update emulator

Update packages including Canary releases:

    android sdk update --canary

Force downgrade canary packages to the stable release:

    android sdk update --force