---
title: https://developer.android.com/tools/agents/android-cli/commands/sdk_remove
url: https://developer.android.com/tools/agents/android-cli/commands/sdk_remove
source: md.txt
---

Removes packages from the SDK.

## Usage

    android sdk remove [-h] <package>

## Options

- `-h,--help` - Shows the help message for the specified command.

`sdk` options:

- `--ignore-outdated-xmls` - When installing or updating packages, do not update other packages' XML files.
- `--platform=PARAM` - Target platform `<os>_<arch>` (for example, `linux_x86_64`, `mac_arm64`, or `windows_x86`); defaults to the current host.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<package>` - Names of the packages to remove.

## Description

`android sdk remove` uninstalls one or more packages from your SDK installation directory.

### Format package paths

Package names use slashes (`/`) as the delimiter (for example, `platforms/android-33`, `build-tools/33.0.0`). Semicolon-delimited paths (`platforms;android-33`) are also supported.

### Examples

Remove an installed platform SDK:

    android sdk remove platforms/android-33

Remove multiple packages at once:

    android sdk remove build-tools/30.0.3 platforms/android-30