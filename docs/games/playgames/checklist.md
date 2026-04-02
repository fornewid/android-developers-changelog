---
title: https://developer.android.com/games/playgames/checklist
url: https://developer.android.com/games/playgames/checklist
source: md.txt
---

Your game may be badged to users as untested, playable, or optimized in
Google Play Games on PC based on whether the game has been through our
review process and what the outcome was.

The badges describe how well a game runs on Windows PCs, ranging from
*untested* (not reviewed yet, but may work) to *playable* (works well) to
*optimized* (designed for the best PC experience).

Users find games badged as *Playable on PC* by:

- Browsing Google Play Games on PC
- Text search in Google Play Games on PC
- Navigating to your game details page on the Play Store on mobile or web

Users find and install games badged as *Untested on PC*
by:

- Text search in Google Play Games on PC

## Requirements for untested games

For a game to be available on Google Play Games on PC, an ARM or x86-64 build
must be enabled for the "Google Play Games on PC" form factor.

While your game might work well on PC, it will be badged as *untested* in
Google Play Games on PC until it goes through our playability review process.
If you'd like us to test the game for playability,
[contact us](https://support.google.com/googleplay/games-on-pc-developer/contact/request_updated_label).

Untested games are represented to users with the following message
and icon:

| Message | Icon |
|---|---|
| This game is untested on Windows PCs but may still be playable. | ![untested](https://developer.android.com/static/images/games/playgames/untested_icon.png) *Icon is subject to change* |

<br />

## Requirements for playable games

To be badged as playable, builds must meet these requirements:

- The game must play well:
  - Game is stable and does not crash
  - Does not generate significant ANR's
  - FPS is stable and \>= 30fps
  - Supports mouse and / or keyboard
- The game supports PC Compatibility by:
  - [Disabling unsupported Android features and permissions](https://developer.android.com/games/playgames/pc-compatibility#unsupported-android-features)
  - [Disabling unsupported Google APIs](https://developer.android.com/games/playgames/pc-compatibility#unsupported-google-apis)
  - [Using scoped storage for file system access](https://developer.android.com/games/playgames/pc-compatibility#scoped-storage)

Games with ARM-only builds are available on Intel CPU machines only.
Providing an x86-64 build is strongly encouraged, but not required
(See [Include x86-64 ABI architecture](https://developer.android.com/games/playgames/pc-compatibility#x86-requirement)).

Playable games represented to the users with the following message
and icon:

| Message | Icon |
|---|---|
| This game is playable, but has not been optimized for Windows PCs. Some aspects of the experience might need improvement. | ![playable](https://developer.android.com/static/images/games/playgames/playable_icon.png) *Icon is subject to change* |

<br />

## Requirements for optimized builds

The review team runs through the following requirements
to ensure your game meets our quality standards for the
best possible gameplay experience.

- Platform Requirements
  - [Support x86-64 ABI](https://developer.android.com/games/playgames/pc-compatibility#x86-requirement)
- PC Compatibility
  - [Support mouse and keyboard](https://developer.android.com/games/playgames/input#input-support)
  - [Integrate the Input SDK](https://developer.android.com/games/playgames/input-sdk)
  - [Disable unsupported Android features and permissions](https://developer.android.com/games/playgames/pc-compatibility#unsupported-android-features)
  - [Disable unsupported Google APIs](https://developer.android.com/games/playgames/pc-compatibility#unsupported-google-apis)
  - [Use scoped storage for file system access](https://developer.android.com/games/playgames/pc-compatibility#scoped-storage)
- Display and Visual Assets
  - [Use high resolution assets and textures on PC](https://developer.android.com/games/playgames/graphics#high-resolution-assets)
  - [Support PC-specific aspect ratios](https://developer.android.com/games/playgames/graphics#aspect-ratios)
  - [Scale UI elements appropriately for a larger screen](https://developer.android.com/games/playgames/graphics#ui-scaling)
  - [Render at 60Hz](https://developer.android.com/games/playgames/graphics#increase-max-frame-rate)
  - Audio playback is smooth and in sync
- Google Play Games Services sign in and game sync for the PC
  - [Automatically sign-in with Google Play Games Services on PC](https://developer.android.com/games/playgames/identity#game-identity)
  - [Automatically sync save games on PC](https://developer.android.com/games/playgames/identity#cloud-save)
  - The production version of your mobile build must use Google Play Games Services V2.

Optimized games represented to the users with the following message
and icon:

| Message | Icon |
|---|---|
| This game was optimized by the developer to run on PCs. | ![optimized](https://developer.android.com/static/images/games/playgames/optimized_icon.png) *Icon is subject to change* |

<br />