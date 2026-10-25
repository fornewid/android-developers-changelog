---
title: https://developer.android.com/tools/agents/android-cli/commands/signals_context
url: https://developer.android.com/tools/agents/android-cli/commands/signals_context
source: md.txt
---

Lists accessible Crashlytics projects and apps.

## Usage

    android signals context [-h] [--firebase-project=PARAM] [--format=PARAM]

## Options

- `--firebase-project=PARAM` - Firebase project ID to list Android apps for in Crashlytics (for example, 'my-firebase-project').
- `--format=PARAM` - Output format ('text' or 'json'; default: 'text').
- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Description

`android signals context` lists the Firebase projects and apps that your account
can access in Firebase Crashlytics. Run it first to find the Firebase app IDs
(`--firebase-app`) to pass to the other `android signals` commands or to
configure in `~/.androidrc`.

### List the apps of a Firebase project (`--firebase-project`)

When your account can access more than 10 Firebase projects, their apps aren't
listed automatically. Pass `--firebase-project=<project-id>` to list the Android
apps of a single project, along with the app ID that you can pass to
`--firebase-app`.

### Examples

List accessible Firebase projects and apps:

    android signals context

List the Android apps of the `my-firebase-project` Firebase project:

    android signals context --firebase-project=my-firebase-project

Print the context as JSON:

    android signals context --format=json