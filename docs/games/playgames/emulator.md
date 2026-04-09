---
title: https://developer.android.com/games/playgames/emulator
url: https://developer.android.com/games/playgames/emulator
source: md.txt
---

[Download Stable Edition](https://dl.google.com/tag/s/appguid=%7BC601E9A4-03B0-4188-843E-80058BF16EF9%7D&appname=GPG_Developer_Emulator_Stable&needsadmin=true&ap=prod/play/games/Install-GooglePlayGames-DeveloperEmulator-Stable.exe)
[Other Downloads](https://developer.android.com/games/playgames/emulator#other-downloads)

The Google Play Games on PC Developer Emulator is a developer focused emulator for
Google Play Games on PC. It features a configurable emulator and surrounding
tooling to make it easy to build, test, and debug your PC title. This emulator
is useful for [testing and developing](https://developer.android.com/games/playgames/pg-emulator) games for Google Play Games on PC.

## Terms and Conditions

By downloading and using the Google Play Games on PC, you agree to the
[Google Terms of Service](https://play.google.com/about/play-terms/) and the [Google Play Terms of
Service](https://play.google.com/about/play-terms/) and acknowledge that Google may collect data in
accordance with the [Google Privacy Policy](https://policies.google.com/privacy) (please see the Data
Collection section for more info). Additionally, you agree that you will only
use Google Play Games on PC and related tools for the development and
testing of games for the Play Games for PC platform and only in connection with
games that you are authorized to access for development and testing purposes.
You must be 18 years of age or older to use the Google Play Games on PC.

## System Requirements

Verify your system meets the minimum requirements [here](https://support.google.com/googleplay/answer/11358071).

## Release Notes

Read the current [release notes](https://support.google.com/googleplay?p=games_pc_release_notes).

## Differences from the consumer experience

The development emulator is backed by the same underlying technology as the
consumer Google Play Games on PC experience, but is optimized for developer
based workflows. This means that the developer emulator:

- Boots to a typical Android launcher
- Can toggle the graphics stack between Vulkan and DirectX
- Can force the aspect ratio for testing
- Provides manual control over whether the mouse sends mouse or emulated touch events
- Supports debugging and sideloading games
- Does not return `MEETS_VIRTUAL_INTEGRITY` from [Play Integrity Protection](https://developer.android.com/games/playgames/integrity)

## Enabling Virtualization

The Google Play Games on PC Developer Emulator requires Hyper-V to function. If you get
an error, follow the instructions [here](https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/) to enable the feature.
Note that on some motherboards, you may have to also enable virtualization in
your BIOS/Firmware.

## Data Collection

The Google Play Games on PC Developer Emulator may collect performance and stability data
to improve our product. Developers cannot opt out of the data collection. The
following list contains what the Google Play Games on PC.

### Crash Reports

When the HPE or the HPE Service's program encounters a problem and crashes, a
"minidump" file which contains a subset of the crashing process and shared lib's
memory snapshot, is created and sent to Google.

Along with the dump file, we also collect the following metadata:

- OS Name and version: E.g. Windows NT, 10.0.19041 804
- CPU Architecture: E.g.amd64, family 6 model 165 stepping 2
- Gpu name: E.g., Intel(R) UHD Graphics
- Gpu driver file: E.g. igdumdim64.dll
- Gpu driver version: E.g.: 27.20.100.8729
- Gpu gdi device name: E.g.: \\.\\DISPLAY1

### Metrics (performance and stability)

HPE collects performance and stability metrics which help HPE developers analyse
and improve HPE. The list of metrics we collect include the following:

- Emulator's main process cpu usage in percentage
- Emulator's main process memory usage in mb
- Emulator's displayed frame(s) per second
- Emulator's janky frame(s) per second
- Emulator's network transfer rate in bytes/sec
- Emulator's network receive rate in bytes/sec
- Emulator process is closed unexpectedly
- Emulator process is closed as expected
- Emulator process is closed due to an error exiting an app
- Launching an app
- Successfully launched an app
- Successfully stopped an app
- Attempting sign-in
- Successfully signed in
- Sign in failed
- Attempting to refresh sign-in
- Successfully refreshed sign-in
- Refreshing sign-in failed
- Attempting to check sign-in status
- Successfully checked sign-in status
- Checking sign-in status failed
- Emulator starting time
- Emulator launching successfully time
- Emulator launching unsuccessfully time
- Attempting to install an app
- Successfully installed an app
- Installing an app failed
- Installing app attempt ignored
- Installing an app resulted in a retriable failure
- Installing an app resulted in terminal failure
- Sign-in timeout
- Emulator running unhealthy
- Service running time span
- Emulator running time span
- Emulator exit code
- Launching an app is cancelled
- App package name (if applicable)
- HPE version number
- Hardware information
  - CPU name
  - GPU name
  - Disk drive type
  - Page file size

## Developer Emulator Downloads

The developer emulator has two tracks to choose from. Most developers should
download and develop on the *Stable* release track. It can be advantageous to
use the *Beta* track to validate your game against the upcoming release and
address any concerns before the new client is released to players.

### How to switch tracks

To switch the current track for your developer emulator:

1. Quit the Google Play Games on PC Developer Emulator from the task bar icon if it's running
2. Fully uninstall the current Google Play Games on PC Developer Emulator
3. Run the installer for the specific track you plan to develop with (below)

Google Play Games on PC Developer Emulator only allows a single track to be installed on a
machine at any given time. You can't switch tracks in the installer, nor can
the track be switched after installation.

### Downloads

- [Stable](https://dl.google.com/tag/s/appguid=%7BC601E9A4-03B0-4188-843E-80058BF16EF9%7D&appname=GPG_Developer_Emulator_Stable&needsadmin=true&ap=prod/play/games/Install-GooglePlayGames-DeveloperEmulator-Stable.exe) - the current stable release with 100% rollout.
- [Beta](https://dl.google.com/tag/s/appguid=%7BC601E9A4-03B0-4188-843E-80058BF16EF9%7D&appname=GPG_Developer_Emulator_Beta&needsadmin=true&ap=dogfood/play/games/Install-GooglePlayGames-DeveloperEmulator-Beta.exe) - the upcoming release. Ensure your game works on the next release.