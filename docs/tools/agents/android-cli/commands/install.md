---
title: https://developer.android.com/tools/agents/android-cli/commands/install
url: https://developer.android.com/tools/agents/android-cli/commands/install
source: md.txt
---

Installs an Android app (one or more APKs) on a connected device or emulator
without activating any components, using incremental optimizations for faster
deployment than `adb`.

## Usage

    android install [-h] [--apks=PARAM] [--device=PARAM] [--install-options=PARAM] [--use-delta-install] [<apks_or_reference>] [-- <build_args>]

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

## Positional arguments

- `<apks_or_reference>` - APK file path(s) or a build reference (\[system://\]\[path\]?\[target\]).
- `-- <build_args>` - Arguments passed verbatim to the build system. Use -- to separate from other arguments.

## Description

`android install` deploys one or more APK files to a connected Android device or
emulator without launching any activities or services.

Pass a build reference (`[system://][path]?[target]`) to build and deploy from
source, or pass pre-built APK file paths (in `<apks_or_reference>` or with
`--apks`).

Unlike [`android run`](https://developer.android.com/tools/agents/android-cli/commands/run), `android install` only performs the package
installation step. By default, it uses incremental delta installation to push
only the bytes that changed since the previous deployment, making iterative
updates faster than `adb install`.

### Toggle delta installation (`--use-delta-install`)

Delta installation is enabled by default. Pass `--use-delta-install=false` to
disable incremental patching and perform a full APK installation instead.

### Specify a target device (`--device`)

If multiple physical devices or emulators are connected, pass
`--device=<serial-number>` (as reported by `adb devices`) to select the target
device.

### Examples

Build and install the default debug variant of `:app` in the current Gradle
workspace:

    android install :app

Build and install the `debug` variant of `:app` (`:app@debug`) from the Gradle
workspace at `$HOME/my-app`, passing extra arguments to Gradle:

    android install $HOME/my-app?:app@debug -- --offline

Install a single debug APK onto the connected device:

    android install --apks=app/build/outputs/apk/debug/app-debug.apk

Install multiple split APKs onto a specific emulator without delta patching:

    android install --use-delta-install=false --device=emulator-5554 --apks=base.apk,config.hdpi.apk