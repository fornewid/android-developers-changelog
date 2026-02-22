---
title: https://developer.android.com/games/playgames/development-readiness
url: https://developer.android.com/games/playgames/development-readiness
source: md.txt
---

The Game Readiness Checker is a tool that helps validate your game against review
requirements locally in the Google Play Games on PC Developer Emulator. Running your game
through this tool helps shorten review time by highlighting common issues before
submitting your game for [Official Review](https://developer.android.com/games/playgames/checklist).

## How does it work?

1. Launch your game in the Google Play Games on PC Developer Emulator.
2. Open the Game Readiness Checker using the "Validate Game Readiness" icon in the system tray context menu (right-click the Google Play Games on PC system tray icon).
3. In the Game Readiness Checker, select the package name of the game from the testing.
4. Click **Run tests**.
5. Wait 20 seconds for testing to finish.

When this is done, you get a list of all the test results (either pass or fail).
Failing tests have a description of the problem and a link to this developer
documentation on the right. These links help you diagnose the problem and
work out a solution.

![A screenshot of the Game Readiness Checker with several results shown. There
are three columns labelled "Test", "Status", and "Details". Status has green
text "Test passed" and or red text "Test failed".](https://developer.android.com/static/images/games/playgames/self-audit-tool.png "Screenshot of the Game Readiness Checker")

## Google Play Games on PC compatibility tests

This is a list of the tests the Game Readiness Checker runs and how to address
any issues it discovers.

### Android features test

- **What it tests:** this test looks for features that are not supported on Google Play Games on PC but are present in the game's `AndroidManifest.xml` file.
- **How to address test failures:** [remove or make optional](https://developer.android.com/games/playgames/pc-compatibility#unsupported-android-features) any features that are not supported by the Google Play Games on PC to ensure players can install and play your game.

### Supported ABI test

- **What it tests:** this makes sure that the game supports an x86, x86-64, or any ARM ABI. This is required to be able to run on Google Play Games on PC
- **How to address test failures:** [ensure that your game and its supporting
  libraries](https://developer.android.com/games/playgames/pc-compatibility#x86-requirement) are built for x86-64.

### x86 ABI test

- **What it tests:** this makes sure that the game supports an x86-64 ABI, which is recommended for Google Play Games on PC.
- **How to address test failures:** [ensure that your game and its supporting
  libraries](https://developer.android.com/games/playgames/pc-compatibility#x86-requirement) are built for x86-64.

### Unsupported OpenGL version test

- **What it tests:** the OpenGL version specified in the manifest is supported on Google Play Games on PC.
- **How to address test failures:** make sure your game supports [the minimum
  OpenGL ES or Vulkan versions](https://developer.android.com/games/playgames/graphics#opengles-version) for Google Play Games on PC and update your `AndroidManifest.xml` accordingly.

### Play Games Services v2 SDK integration test

- **What it tests:** if the Play Games Services SDK v2 SDK can be found in the `AndroidManifest.xml`.
- **How to address test failures:** [read about the continuity requirements](https://developer.android.com/games/playgames/identity#game-identity) and make sure you've integrated the latest Play Games Services SDK.

### Play Games Services v2 SDK sign-in test

- **What it tests:** whether the player was signed in with the Play Games Services SDK v2 SDK.
- **How to address test failures** [read about the continuity requirements](https://developer.android.com/games/playgames/identity#game-identity) and ensure that you're signing in the player at launch.

### Input SDK test

- **What it tests:** if the game has integrated with the input mapping service using the Input SDK.
- **How to address test failures:** [read about the Input SDK](https://developer.android.com/games/playgames/input-sdk) and make sure you're annotating action bindings in your game.

### FPS Stability Test

- **What it tests:**
  - Game did not produce enough frames for calculating stable FPS.
  - Game did not consistently produce \>30 FPS.
- **How to address test failures:** Ensure that your game meets [the frame rate
  requirements](https://developer.android.com/games/playgames/graphics#increase-max-frame-rate) for Google Play Games on PC and keeps the frame rate stable.

### Permissions test

- **What it tests:** whether the game requests permissions that are not supported on Google Play Games on PC.
- **How to address test failures:** [Read about features not present on
  Google Play Games on PC](https://developer.android.com/games/playgames/pc-compatibility#unsupported-android-features) and make sure that they're optional.

### ANR test

- **What it tests:** whether an "Application Not Responding" (ANR) error was detected while the game was running.
- **How to address test failures** : [Read about how to detect ANRs and the most
  common kind](https://developer.android.com/topic/performance/vitals/anr), and address any issues that may have occurred when running the Game Readiness Checker.

### App crash test

- **What it tests:** if the game crashed.
- **How to address test failures:** [Diagnose and repair](https://developer.android.com/topic/performance/vitals/crash) any crashes that may have occurred when running the Game Readiness Checker.