---
title: Playability review process for Google Play Games on PC  |  Android game development  |  Android Developers
url: https://developer.android.com/games/playgames/checklist
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Games dev center](https://developer.android.com/games)
* [Guides](https://developer.android.com/games/guides)

Send feedback

# Playability review process for Google Play Games on PC Stay organized with collections Save and categorize content based on your preferences.



Your game may be badged to users as untested, playable, or optimized in
Google Play Games on PC based on whether the game has been through our
review process and what the outcome was.

The badges describe how well a game runs on Windows PCs, ranging from
*untested* (not reviewed yet, but may work) to *playable* (works well) to
*optimized* (designed for the best PC experience).

Users find games badged as *Playable on PC* by:

* Browsing Google Play Games on PC
* Text search in Google Play Games on PC
* Navigating to your game details page on the Play Store on mobile or web

Users find and install games badged as *Untested on PC*
by:

* Text search in Google Play Games on PC

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
| --- | --- |
| This game is untested on Windows PCs but may still be playable. | untested  *Icon is subject to change* |

## Requirements for playable games

To be badged as playable, builds must meet these requirements:

* The game must play well:
  + Game is stable and does not crash
  + Does not generate significant ANR's
  + FPS is stable and >= 30fps
  + Supports mouse and / or keyboard
* The game supports PC Compatibility by:
  + [Disabling unsupported Android features and permissions](/games/playgames/pc-compatibility#unsupported-android-features)
  + [Disabling unsupported Google APIs](/games/playgames/pc-compatibility#unsupported-google-apis)
  + [Using scoped storage for file system access](/games/playgames/pc-compatibility#scoped-storage)

Games with ARM-only builds are available on Intel CPU machines only.
Providing an x86-64 build is strongly encouraged, but not required
(See [Include x86-64 ABI architecture](/games/playgames/pc-compatibility#x86-requirement)).

Playable games represented to the users with the following message
and icon:

| Message | Icon |
| --- | --- |
| This game is playable, but has not been optimized for Windows PCs. Some aspects of the experience might need improvement. | playable  *Icon is subject to change* |

## Requirements for optimized builds

The review team runs through the following requirements
to ensure your game meets our quality standards for the
best possible gameplay experience.

* Platform Requirements
  + [Support x86-64 ABI](/games/playgames/pc-compatibility#x86-requirement)
* PC Compatibility
  + [Support mouse and keyboard](/games/playgames/input#input-support)
  + [Integrate the Input SDK](/games/playgames/input-sdk)
  + [Disable unsupported Android features and permissions](/games/playgames/pc-compatibility#unsupported-android-features)
  + [Disable unsupported Google APIs](/games/playgames/pc-compatibility#unsupported-google-apis)
  + [Use scoped storage for file system access](/games/playgames/pc-compatibility#scoped-storage)
* Display and Visual Assets
  + [Use high resolution assets and textures on PC](/games/playgames/graphics#high-resolution-assets)
  + [Support PC-specific aspect ratios](/games/playgames/graphics#aspect-ratios)
  + [Scale UI elements appropriately for a larger screen](/games/playgames/graphics#ui-scaling)
  + [Render at 60Hz](/games/playgames/graphics#increase-max-frame-rate)
  + Audio playback is smooth and in sync
* Google Play Games Services sign in and game sync for the PC
  + [Automatically sign-in with Google Play Games Services on PC](/games/playgames/identity#game-identity)
  + [Automatically sync save games on PC](/games/playgames/identity#cloud-save)
  + The production version of your mobile build must use
    Google Play Games Services V2.

Optimized games represented to the users with the following message
and icon:

| Message | Icon |
| --- | --- |
| This game was optimized by the developer to run on PCs. | optimized  *Icon is subject to change* |




Send feedback