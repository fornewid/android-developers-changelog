---
title: https://developer.android.com/tools/agents/android-cli/commands/run
url: https://developer.android.com/tools/agents/android-cli/commands/run
source: md.txt
---

Builds, deploys, and launches an Android app on a connected device or emulator.

## Usage

    android run [-h] [--activity=PARAM] [--apks=PARAM] [--debug] [--device=PARAM] [--install-options=PARAM] [--type=PARAM] [--use-delta-install]

## Options

- `--activity=PARAM` - The activity name.
- `--apks=PARAM` - The paths to the APKs, comma separated.
- `--debug` - Run in debug mode.
- `--device=PARAM` - The device serial number.
- `-h,--help` - Shows the help message for the specified command.
- `--install-options=PARAM` - Additional options or flags to pass to package manager install (for example, `-g`, `-d`).
- `--type=PARAM` - The component type (`ACTIVITY`, `WATCH_FACE`, `TILE`, `COMPLICATION`, `DECLARATIVE_WATCH_FACE`, `WEAR_WIDGET`).
- `--use-delta-install` - Use fast delta install (speeds up incremental updates by transferring only modified code and resources; default: `true`).

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Description

`android run` deploys one or more APK files to a connected Android device or emulator and immediately launches the target app component.

> [!NOTE]
> **Note:** `android run` does not compile source code; you must pass the paths to pre-built APK files using `--apks`. To locate APK output paths in an Android project, run [`android describe`](https://developer.android.com/tools/agents/android-cli/commands/describe).

### Specify what to run (`--type` and `--activity`)

By default, `android run` launches the default main activity declared in the app manifest. You can override what gets started using the following options:

- `--activity`: Specifies the activity or component class name to launch (required if the APK declares multiple launchable activities).
- `--type`: Specifies the [component type](https://developer.android.com/guide/topics/manifest/manifest-intro#components) to start instead of a standard UI activity. Supported values include `ACTIVITY`, `WATCH_FACE`, `TILE`, `COMPLICATION`, `DECLARATIVE_WATCH_FACE`, and `WEAR_WIDGET`.
- `--debug`: Launches the app in [debug mode](https://developer.android.com/studio/debug) and waits for a debugger from Android Studio or a command-line tool to attach.

### Examples

Deploy a single debug APK and launch its main activity on the default connected device:

    android run --apks=app/build/outputs/apk/debug/app-debug.apk

Deploy multiple split APKs to a specific emulator:

    android run --device=emulator-5554 --apks=base.apk,density-hdpi.apk,lang-en.apk

Deploy an APK and launch a specific activity in debug mode:

    android run --debug --activity=.ui.MainActivity --apks=app-debug.apk