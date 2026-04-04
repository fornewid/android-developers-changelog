---
title: https://developer.android.com/games/playgames/input-sdk
url: https://developer.android.com/games/playgames/input-sdk
source: md.txt
---

> [!NOTE]
> **Note:** Games that are played with only the left-mouse button are not required to integrate the Input SDK. These games are supported using with the [compatibility mode](https://developer.android.com/games/playgames/input#compatibility-mode). This document applies to all other games that need more than the left-mouse button.

The Input SDK provides a unified interface that allows players to
view and change the mouse and keyboard bindings for any game they wish to play
on Google Play Games on PC. At any point during gameplay, a player can summon
the Google Play Games on PC overlay as seen in this screenshot:

![A screenshot showing the Input SDK rendered over a sample game](https://developer.android.com/static/images/games/playgames/input-sdk-overlay.png)

This SDK is **required** for games that use keyboard on Google Play Games on PC
because Android mobile games are designed around a touchscreen for player input.
When developing for PCs, games need to support a mouse and keyboard instead. You
should only enable this SDK on Google Play Games on PC.

> [!NOTE]
> **Note:** For information about the other Google Play Games on PC requirements, see [Get started with Google Play Games on PC](https://developer.android.com/games/playgames/start).

The Input SDK is an important element for keeping players happy and
engaged with your game on different platforms. The experience afforded by
a mouse and keyboard is different from touchscreens. When you integrate your game
with the Input SDK you will enable players to remap the default controls
in Google Play Games on PC.

For a more immersive experience, you can take more advantage of the remapping
feature offered by Google Play Games on PC by setting different scheme controls
for your menus, main game and minigames, or by updating your UI to match your
user's custom control maps. You can disable or enable remapping for individual
keys or groups of keys, or decide what keys are allowed to be remapped in your
game.

When using the remapping feature, Android will detect when the user is typing text
into a text field and disable remapping, so your game doesn't have to
manually disable remapping for these scenarios.

For more information, see [best practices](https://developer.android.com/games/playgames/input-sdk-start#input-sdk-best-practices)
and [restrictions](https://developer.android.com/games/playgames/input-sdk-start#remapping-restrictions) of the Input SDK to help build the best PC experience possible for your game.

## Integration guide

For information about integrating the Input SDK, see
[Get started with the Input SDK](https://developer.android.com/games/playgames/input-sdk-start).

## Sample games

For examples of how to integrate with the Input SDK, see
[AGDK Tunnel](https://github.com/android/games-samples/tree/main/agdk/agdktunnel)
for Kotlin or Java games and
[Trivial Kart](https://github.com/android/games-samples/tree/main/trivialkart/trivialkart-unity)
for Unity games.

## Download the Input SDK

Before you download the Input SDK, read the following Google Input SDK terms of service and data collection requirements.

### Google APIs Terms of Service

The [Google APIs Terms of Service](https://developers.google.com/terms) governs
your use of the Google Input SDK.

### Data collection

The Google Input SDK may collect performance and stability data to
improve our product, including the following data:

- Number of calls to the Input SDK methods.
- Number of non-successful calls to Input SDK methods.
- InputMap aggregated information like:
  - Number of defined actions and groups.
  - Number of defined single-key, multi-key and mouse actions.
  - Number of defined mouse actions.
  - Number of remappable actions and groups.
  - Number of remapping-reserved keys.
  - InputMap remapping option (enabled/disabled).
- Game's package name.
- Game's version number.
- Game's version name.
- Input SDK version.
- Client variants such as Google Play Games on PC or other clients.

The Input SDK is
[available on the Google Maven Repository](https://maven.google.com/web/index.html#com.google.android.libraries.play.games:inputmapping).
See the [Getting Started Guide](https://developer.android.com/games/playgames/input-sdk-start#adding-the-sdk) for instructions
on how to your Java or Kotlin project.

Download the Input SDK for Unity from the
[Play Unity Plugins repository](https://developers.google.com/unity/packages#input_sdk).