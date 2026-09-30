---
title: https://developer.android.com/tools/agents/android-cli/commands/auth_logout
url: https://developer.android.com/tools/agents/android-cli/commands/auth_logout
source: md.txt
---

Log out from Google services for Android CLI.

## Usage

    android auth logout [-h]

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Description

`android auth logout` signs you out of your Google account. It revokes the refresh token on the server and deletes it from your machine. If the token can't be revoked on the server, it's still deleted locally, and the command prints a link where you can revoke access manually.

### Examples

Sign out:

    android auth logout