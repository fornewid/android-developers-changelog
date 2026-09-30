---
title: https://developer.android.com/tools/agents/android-cli/commands/auth_login
url: https://developer.android.com/tools/agents/android-cli/commands/auth_login
source: md.txt
---

Log in to Google services for Android CLI.

## Usage

    android auth login [-h] [--no-use-keyring]

## Options

- `-h,--help` - Shows the help message for the specified command.
- `--no-use-keyring` - Do not use keyring for storing tokens.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Description

`android auth login` signs you in to your Google account. It opens the Google sign-in page in your default browser and waits up to 5 minutes for you to authorize Android CLI. If the browser can't be opened automatically, the command prints the URL so that you can open it manually.

After you sign in, Android CLI stores a refresh token so that later commands can authenticate without prompting you again. The token is stored in the system keyring when one is available. Otherwise, it's stored in a plaintext file readable only by you, and the command prints a warning. On Linux, install `libsecret-tools` and log in again to use the keyring.

### Configure login options

- `--no-use-keyring`: Stores the refresh token in a file readable only by you instead of the system keyring, without checking whether a keyring is available.

### Examples

Sign in with your Google account:

    android auth login

Sign in without using the system keyring:

    android auth login --no-use-keyring