---
title: https://developer.android.com/games/playgames/start
url: https://developer.android.com/games/playgames/start
source: md.txt
---

Your game must meet the [playability requirements](https://developer.android.com/games/playgames/start#playability-requirements)
before you can release the game on
[Google Play Games on PC](https://developer.android.com/games/playgames/overview). Once the game is on the
platform, you can work towards [full certification](https://developer.android.com/games/playgames/start#requirements-checklist) by
adding platform features that delight players, such as seamless continuity of
play, platform input controls, and improved performance.

## Playability requirements

You must meet the minimum playable requirements to ship your mobile game to PCs.
These requirements are designed to ensure your game can be played on the
platform. Once available to PCs you can continue to develop your game to become
fully certified on the platform.

Playability checklist:

- The game is playable on PCs with a mouse and keyboard. Note that direct support for mouse and keyboard is not required to meet this requirement. Games that are playable in compatibility mode are sufficient.
- Gameplay cannot be blocked by unsupported permissions.
- Gameplay cannot be blocked by unsupported Google APIs.
- Game cannot require unsupported features.
- The game must support OpenGL ES (3.2 or below) or Vulkan (1.1 or below).

### Testing for playability

There are several different ways to test your game to determine if it meets the
basic playability requirements. The most important thing to test is input
handling and that gameplay is not blocked by unsupported features or
permissions. The compatibility mode in the platform might be sufficient for a
single-click game. If your game is more complex, for example it requires two
hands to play, then additional mouse and keyboard support might be required.
Here are a couple of things to consider:

- Use the mouse scroll wheel for scrolling or zooming.
- Vertical swipes requires more work than horizontal swipes when done with a mouse. Although horizontal swiping translates well using the compatibility mode, consider keyboard shortcuts for vertical swiping.
- Support multi-touch gestures with keyboard shortcuts.
- Add keyboard shortcuts for common actions such as an enter press to accept dialogs or an escape press to cancel.

Use the [developer emulator](https://developer.android.com/games/playgames/start#get-emulator) to test the playability of your
game.

### Game ABI architecture

Google Play Games on PC works with Android games built using either the ARM or
x86-64 ABI. Whenever possible, game developers should ship x86-64 binaries for
Google Play Games on PC but ARM games will still receive certification if they
meet the performance and stability requirements.

#### ARM binaries

Google has partnered with Intel to bring ARM based games to both Intel- and AMD-
based PCs using Intel Bridge Technology. This means that once your mobile game
meets the playability requirements, it can be distributed on
Google Play Games on PC to most x86 based PCs.

#### x86-64 binaries

Providing an x86-64 version of your mobile game provides performance
improvements to your players because it can be executed directly on the
built-in hardware.

## Certification requirements

Certified games are optimized to use the Google Play Games on PC features and
capabilities to delight their players. To certify your game you must have met
all of the basic playability requirements in addition to the following
requirements.

- Performance and stability
  - Maintain a stable smooth framerate
    - 30 FPS on a lower-tier PC
    - 60 FPS on a higher-end PC
  - No crashes over 20+ minutes of continuous gameplay
- Playability requirements
  - [Disable unsupported Android features and permissions](https://developer.android.com/games/playgames/pc-compatibility#unsupported-android-features)
  - [Disable unsupported Google APIs](https://developer.android.com/games/playgames/pc-compatibility#unsupported-google-apis)
  - [Use scoped storage for file system access](https://developer.android.com/games/playgames/pc-compatibility#scoped-storage)
- Graphics \& Audio
  - [Use high resolution assets and textures](https://developer.android.com/games/playgames/graphics#high-resolution-assets), such that there is no blurriness and text is readable when played at 1440p resolution
  - [Support 16:9 aspect ratio](https://developer.android.com/games/playgames/graphics#aspect-ratios) (or 9:16 for portrait). This means that there aren't any black bars when running in this aspect ratio.
  - [Scale UI elements for larger screens](https://developer.android.com/games/playgames/graphics#ui-scaling)
  - Audio playback is smooth and in sync
- Device input
  - [Support mouse and keyboard input](https://developer.android.com/games/playgames/input#input-support)
  - [Integrate the Input SDK](https://developer.android.com/games/playgames/input-sdk)
- Cross-Platform play
  - [Support cross-device and cross-platform progress sync](https://developer.android.com/games/playgames/identity#cloud-save) including PC, Android, and iOS

For more information about when these requirements need to be integrated and
how they are tested, see the [milestone checklist](https://developer.android.com/games/playgames/checklist) page.

## Recommendations (NOT requirements)

To further improve the player experience, we recommend the following:

- [Include x86-64 ABI architecture](https://developer.android.com/games/playgames/pc-compatibility#x86-requirement)
- [Integrate the Sign-in service for Google Play Games Services v2 on mobile and PC](https://developer.android.com/games/playgames/identity#game-identity)
- Controller / Gamepad support
  - For most games, controllers provide a better user experience on larger screens, and may be the input of choice for some players.

## Hardware Performance Tiers

For certification purposes

| Hardware | lower-tier PC | higher-end PC |
|---|---|---|
| CPU | quad-core with hyperthreading (8 logical cores) | 8-core with hyperthreading (16 logical cores) |
| GPU | typical integrated GPU such as Intel Iris Xe | typical discrete GPU such as GeForce RTX 3060 |

## Minimum requirements for players

For information about the minimum requirements for players to run Google Play Games on PC on a PC, see [minimum PC requirements](https://support.google.com/googleplay?p=pc_requirements) in
Google Help Center.

## Get the developer emulator

Once you have a compatible build of your game, you can test it in the
developer-focused build of the emulator. The developer emulator includes the
same Google Play Games on PC features, SDKs, and optimizations as the user
experience. Additionally, it includes some additional controls that make it
easier to test your game on Windows.

You can sideload an APK to the emulator through [Android Studio](https://developer.android.com/studio)
or the [Android Debug Bridge](https://developer.android.com/studio/command-line/adb).

See [Developing with the Google Play Games on PC Developer Emulator](https://developer.android.com/games/playgames/pg-emulator) for more information.