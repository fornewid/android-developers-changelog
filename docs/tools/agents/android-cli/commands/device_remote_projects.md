---
title: https://developer.android.com/tools/agents/android-cli/commands/device_remote_projects
url: https://developer.android.com/tools/agents/android-cli/commands/device_remote_projects
source: md.txt
---

Lists Google Cloud projects available for device streaming.

## Usage

    android device remote projects [-h] [--all]

## Options

- `--all` - Include projects that are not ready yet for streaming.
- `-h,--help` - Shows the help message for the specified command.

`remote` options:

- `--project=PARAM` - The Google Cloud project ID.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Description

`android device remote projects` lists the Google Cloud projects that your account can use for device streaming. A project is ready when the required APIs are enabled, your account has the required permissions, and billing is enabled.

By default, only projects that are ready for streaming are listed. If you have more than 10 projects, their readiness isn't checked and all of them are listed.

### Configure listing options

- `--all`: Lists all projects in a table with their API, permission, and billing status, followed by the issues that prevent each project from being ready.

### Examples

List the projects that are ready for streaming:

    android device remote projects

List all projects and the issues that prevent them from being ready:

    android device remote projects --all