---
title: https://developer.android.com/games/playgames/start
url: https://developer.android.com/games/playgames/start
source: md.txt
---

Your game must meet playability requirements before you can release the game on
[Google Play Games on PC](https://developer.android.com/games/playgames/overview). Once the game is on the
platform, you can work toward full certification by adding platform features
that delight players, such as seamless continuity of play, platform input
controls, and improved performance.

## Playability Requirements

You must meet the minimum playable requirements to ship your mobile game to PCs.
These requirements are designed to ensure your game can be played on the
platform. Once available to PCs you can continue to develop your game to become
fully certified on the platform.

Playability Checklist:

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

You can use the following methods to test your game's input playability:

- ChromeOS: Chromebooks offer a native PC-like experience with mouse and keyboard. This provides the closest experience to Google Play Games on PC.
- Mobile with mouse and keyboard: You can attach a mouse and keyboard to a mobile device to see how well it plays.

### Game ABI Architecture

Google Play Games on PC supports games build with ARM or x86-64 ABI binaries.
Including x86-64 binaries is recommended for improved game performance and
expanded device reach. An x86-64 build of the game is also required for full
certification.

#### ARM binaries

Google has partnered with Intel to enable ARM-based games on Intel-based PCs
using Intel Bridge Technology. This means that after your mobile game has met
the playability requirements it can be distributed on Google Play Games on PC
to Intel-based PCs.

#### x86-64 binaries

Providing an x86-64 version of your mobile game provides performance
improvements to your players because it can be executed directly on the native
hardware. This also expands your game's distribution to non-Intel PCs.

Providing an x86-64 version of your game should be your first step in optimizing
your game for Google Play Games on PC. It improves your game's performance and
expands its distribution reach.

## Certification requirements

Certified games are optimized to use the Google Play Games on PC features and
capabilities to delight their players. To certify your game you must have met
all of the basic playability requirements in addition to the following
requirements.

- Platform requirements
  - [Support x86-64 ABI Architecture](https://developer.android.com/games/playgames/pc-compatibility#x86-requirement)
- Playability requirements
  - [Disable unsupported Android features and permissions](https://developer.android.com/games/playgames/pc-compatibility#unsupported-android-features)
  - [Disable unsupported Google APIs](https://developer.android.com/games/playgames/pc-compatibility#unsupported-google-apis)
  - [Use scoped storage for filesystem access](https://developer.android.com/games/playgames/pc-compatibility#scoped-storage)
- Graphics
  - [Use high resolution assets and textures on Windows](https://developer.android.com/games/playgames/graphics#high-resolution-assets)
  - [Support Windows aspect ratios](https://developer.android.com/games/playgames/graphics#aspect-ratios)
  - [Scale UI elements for larger screens](https://developer.android.com/games/playgames/graphics#ui-scaling)
  - [Render at 60Hz](https://developer.android.com/games/playgames/graphics#increase-max-frame-rate)
  - Audio playback is smooth and in sync
- Device input
  - [Support mouse and keyboard input](https://developer.android.com/games/playgames/input#input-support)
  - [Integrate the Input SDK](https://developer.android.com/games/playgames/input-sdk)
- Cross-Platform play
  - [Integrate the Sign-in service for Google Play Games Services v2 on mobile
    and PC](https://developer.android.com/games/playgames/identity#game-identity)
  - [Automatically sync save games between mobile and PC](https://developer.android.com/games/playgames/identity#cloud-save)

For more information about when these requirements need to be integrated and how
they are tested, see the [milestone checklist](https://developer.android.com/games/playgames/checklist) page.

## Minimum requirements for players

For information about the minimum requirements for players to run Google Play Games on PC on a PC, see [minimum PC requirements](https://support.google.com/googleplay?p=pc_requirements) in
Google Help Center.

## Get the developer emulator

Once you have a compatible build of your game, you can test it in the
developer-focused build of the emulator. The developer emulator includes the
same Google Play Games on PC features, SDKs, and optimizations as the user
experience. Additionally, it includes some additional controls that make it
easier to test your game on Windows.

You can sideload an APK to the emulator through [Android Studio](https://developer.android.com/studio) or the
[Android Debug Bridge](https://developer.android.com/studio/command-line/adb).

See [Use the developer emulator](https://developer.android.com/games/playgames/pg-emulator) for more
information.