---
title: https://developer.android.com/tools/agents/android-cli/commands/auth
url: https://developer.android.com/tools/agents/android-cli/commands/auth
source: md.txt
---

Authentication commands. Log in/out of Google services for Android CLI.

## Usage

    android auth [-h]

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Subcommands

- **[`login`](https://developer.android.com/tools/agents/android-cli/commands/auth_login)** - Log in to Google services for Android CLI.
- **[`logout`](https://developer.android.com/tools/agents/android-cli/commands/auth_logout)** - Log out from Google services for Android CLI.
- **[`status`](https://developer.android.com/tools/agents/android-cli/commands/auth_status)** - Prints the currently signed-in account.

## Description

The `android auth` command set signs Android CLI in to your Google account so that it can call the Google services that require authentication, such as [remote devices](https://developer.android.com/tools/agents/android-cli/commands/device_remote).

### Typical workflow

Here is the sequence of commands for a typical workflow:

1. Run [`android auth login`](https://developer.android.com/tools/agents/android-cli/commands/auth_login) to sign in with your Google account in a browser.
2. Run [`android auth status`](https://developer.android.com/tools/agents/android-cli/commands/auth_status) to confirm which account is signed in.
3. Run [`android auth logout`](https://developer.android.com/tools/agents/android-cli/commands/auth_logout) to sign out and revoke the stored credentials.