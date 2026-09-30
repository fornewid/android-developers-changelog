---
title: https://developer.android.com/tools/agents/android-cli/commands/auth_status
url: https://developer.android.com/tools/agents/android-cli/commands/auth_status
source: md.txt
---

Prints the currently signed-in account.

## Usage

    android auth status [-h]

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Description

`android auth status` prints the name and email address of the signed-in Google account. If no account is signed in, it prints a hint to run `android auth login` and exits with a non-zero exit code, which makes it useful for checking authentication in scripts.

### Examples

Show the signed-in account:

    android auth status