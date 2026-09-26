---
title: https://developer.android.com/tools/agents/android-cli/commands/install
url: https://developer.android.com/tools/agents/android-cli/commands/install
source: md.txt
---

Installs an Android app (one or more APKs) on a connected device or emulator without activating any components, using incremental optimizations for faster deployment than `adb`.

## Usage

    android install [-h] [--apks=PARAM] [--device=PARAM] [--install-options=PARAM] [--use-delta-install]

## Options

- `--apks=PARAM` - The paths to the APKs, comma separated.
- `--device=PARAM` - The device serial number.
- `-h,--help` - Shows the help message for the specified command.
- `--install-options=PARAM` - Additional options or flags to pass to package manager install (for example, `-g`, `-d`).
- `--use-delta-install` - Use fast delta install (speeds up incremental updates by transferring only modified code and resources; default: `true`).

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Description

`android install` deploys one or more pre-built APK files to a connected Android device or emulator without launching any activities or services.

Unlike [`android run`](https://developer.android.com/tools/agents/android-cli/commands/run), `android install` only performs the package installation step. By default, it uses incremental delta installation to push only the bytes that changed since the previous deployment, making iterative updates faster than `adb install`.

### Toggle delta installation (`--no-delta`)

Delta installation is enabled by default. Pass `--no-delta` to disable incremental patching and perform a full APK installation instead.

### Specify a target device (`--device`)

If multiple physical devices or emulators are connected, pass `--device=<serial-number>` (as reported by `adb devices`) to select the target device.

### Examples

Install a single debug APK onto the connected device:

    android install --apks=app/build/outputs/apk/debug/app-debug.apk

Install multiple split APKs onto a specific emulator without delta patching:

    android install --no-delta --device=emulator-5554 --apks=base.apk,config.hdpi.apk