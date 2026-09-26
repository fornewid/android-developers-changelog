---
title: https://developer.android.com/tools/agents/android-cli/commands/sdk_install
url: https://developer.android.com/tools/agents/android-cli/commands/sdk_install
source: md.txt
---

Installs SDK packages.

## Usage

    android sdk install [-h] [--beta] [--canary] [--force] <package>[@<version>]

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

- `<package>[@<version>]` - The packages to install; `<version>` defaults to `latest`.

## Description

`android sdk install` installs one or more SDK packages into your SDK directory. To browse available package paths before installing, run [`android sdk list --all`](https://developer.android.com/tools/agents/android-cli/commands/sdk_list).

Packages are specified as `<package>[@<version>]` where `<package>` is the SDK package path. If `@<version>` is omitted, the latest version available in the selected channel is installed.

### Select a release channel (`--canary` and `--beta`)

By default, `install` only looks for packages in the **Stable** channel.

- `--canary`: Includes packages from Canary, Beta, and Stable channels.
- `--beta`: Includes packages from Beta and Stable channels.

### Force downgrade a package (`--force`)

If the requested package version is older than what is currently installed, pass `--force` to allow downgrading.

### Examples

Install the latest Android Emulator and Platform 34 from the stable channel:

    android sdk install emulator platforms/android-34

Revert to version 1 of the Android SDK Platform 33 package from the stable channel:

    android sdk install --force platforms/android-33@1

Install a canary release of platform tools:

    android sdk install platform-tools --canary