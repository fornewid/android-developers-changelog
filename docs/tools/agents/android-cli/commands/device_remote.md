---
title: https://developer.android.com/tools/agents/android-cli/commands/device_remote
url: https://developer.android.com/tools/agents/android-cli/commands/device_remote
source: md.txt
---

Manage remote physical devices. Includes commands to list, reserve, connect to, and manage remote device reservations.

## Usage

    android device remote [-h] [--project=PARAM]

## Options

- `-h,--help` - Shows the help message for the specified command.
- `--project=PARAM` - The Google Cloud project ID.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Subcommands

- **[`connect`](https://developer.android.com/tools/agents/android-cli/commands/device_remote_connect)** - Connects to a reserved remote device.
- **[`create`](https://developer.android.com/tools/agents/android-cli/commands/device_remote_create)** - Creates a reservation for a remote device.
- **[`disconnect`](https://developer.android.com/tools/agents/android-cli/commands/device_remote_disconnect)** - Disconnects a remote device.
- **[`extend`](https://developer.android.com/tools/agents/android-cli/commands/device_remote_extend)** - Extends a remote device reservation.
- **[`list`](https://developer.android.com/tools/agents/android-cli/commands/device_remote_list)** - Lists remote device reservations.
- **[`models`](https://developer.android.com/tools/agents/android-cli/commands/device_remote_models)** - Lists available remote device models.
- **[`projects`](https://developer.android.com/tools/agents/android-cli/commands/device_remote_projects)** - Lists Google Cloud projects available for device streaming.
- **[`remove`](https://developer.android.com/tools/agents/android-cli/commands/device_remote_remove)** - Removes a remote device reservation.

## Description

The `android device remote` command set reserves physical Android devices hosted in Google data centers and connects them to `adb` on your machine, so that you can install, run, and debug apps on real hardware you don't have.

Remote devices are billed to a Google Cloud project. Before you start, run `android auth login` to sign in with an account that has access to a project with device streaming enabled.

### Typical workflow

Here is the sequence of commands for a typical workflow:

1. Run [`android device remote projects`](https://developer.android.com/tools/agents/android-cli/commands/device_remote_projects) to find a Google Cloud project that is ready for device streaming.
2. Run [`android device remote models`](https://developer.android.com/tools/agents/android-cli/commands/device_remote_models) to find the `<codename>/<api>` of the device you want.
3. Run [`android device remote create <codename>/<api>`](https://developer.android.com/tools/agents/android-cli/commands/device_remote_create) to reserve the device and connect it to `adb`.
4. If you passed `--connect=false` to `create`, run [`android device remote connect <reservation-id>`](https://developer.android.com/tools/agents/android-cli/commands/device_remote_connect) to connect the device to `adb`.
5. Use the device with `android run`, `android install`, `adb`, and other device commands.
6. Run [`android device remote disconnect <reservation-id>`](https://developer.android.com/tools/agents/android-cli/commands/device_remote_disconnect) and [`android device remote remove <reservation-id>`](https://developer.android.com/tools/agents/android-cli/commands/device_remote_remove) when you are done.

### Select a project (`--project`)

Pass `--project=<project-id>` to choose the Google Cloud project to use. It's required by most commands that work with reservations. If it's omitted, the command prints the projects that are ready for streaming.

To avoid passing `--project` every time, add a default to your `~/.androidrc` file. It's picked up by all `android device remote` commands:

    device remote --project my-project