---
title: https://developer.android.com/tools/agents/android-cli/commands/device_hub
url: https://developer.android.com/tools/agents/android-cli/commands/device_hub
source: md.txt
---

Launches a desktop window for real-time screen mirroring and interactive control
of a connected Android device or emulator.

## Usage

    android device hub [-h] [--codec=PARAM] [--device=PARAM]

## Options

- `--codec=PARAM` - Video streaming codec to request from physical devices ('avc' or 'h264', 'hevc', 'vp8', 'vp9', 'av01'; default: 'avc').
- `--device=PARAM` - Target Android device or emulator serial number (such as 'emulator-5554', 'localhost:44767', or an adb serial). If omitted, selects an online device or emulator automatically.
- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Description

`android device hub` launches Android Device Hub in the background, opening a
desktop window that mirrors and controls connected physical Android devices
(including remote devices connected with
[`android device remote connect`](https://developer.android.com/tools/agents/android-cli/commands/device_remote_connect)) and Android emulators
(including headless virtual devices started with
[`android emulator start`](https://developer.android.com/tools/agents/android-cli/commands/emulator_start)).

It streams live displays and audio, forwards touch and mouse gestures,
orientation rotation, and hardware keyboard input, and provides device controls
(including extended emulator controls such as battery, cellular, microphone,
fingerprint, and multi-display settings). You can also switch between connected
devices and emulators directly from the window.

On first run, Android CLI downloads and installs the `device-hub` extension pack
automatically. Process output is appended to `device-hub.log` in the Android
user home directory (`~/.android/device-hub.log` by default).

### Target a device or emulator (`--device`)

If `--device` is omitted, Android Device Hub discovers connected physical
devices and running emulators and selects an online target automatically. Pass
`--device=<serial>` to connect to a specific target, such as an emulator serial
(`emulator-5554`), a USB `adb` serial, or a `localhost:<port>` remote
reservation endpoint.

### Examples

Open Android Device Hub and connect to an online device or emulator
automatically:

    android device hub

Open Android Device Hub connected to a running emulator:

    android device hub --device=emulator-5554

Mirror a specific physical device using the `vp9` video codec:

    android device hub --device=localhost:44767 --codec=vp9