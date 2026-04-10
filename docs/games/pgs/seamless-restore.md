---
title: https://developer.android.com/games/pgs/seamless-restore
url: https://developer.android.com/games/pgs/seamless-restore
source: md.txt
---

Seamless restore is the mechanism by which a returning player is immediately
reconnected to their progress upon installing the game on a new device or
reinstalling the game, removing the friction of a login screen.
Ideally, a game should restore the latest played in-game account by the player
in the scenarios where seamless restore is applicable.

Seamless restore is a recommended guideline for the [Level Up](https://play.google.com/console/about/levelup/) program.

A game restores the player's latest played in-game account in the following
scenarios:

## Implementation guidelines

Refer to the following guidelines about how to use seamless restore:

### When to use seamless restore?

1. **New Device / Fresh Install:** When a returning player installs the game on a new device, the game should restore the last played in-game account (IGA) linked to Google Play Games Services Player ID. Players expect to continue playing with their last saved progress.
2. **Re-install:** When a returning player installs the game on any device, treat this as a new device installation and implement seamless restore.

### When not to use seamless restore?

1. **App Update:** If a player updates the app, local data should already exist (for example, the player updated the app through Google Play). In this situation, don't trigger seamless restore, and respect the local state. However, if no local data is available and a last played IGA is associated with a PGS Player ID, the game can restore this IGA or present the player with the game's login screen.
2. **Explicit Sign-Out:** If a player explicitly signs out of the IGA, their most likely intent is to either switch accounts or remain signed out of the game. In this situation, don't force restore the previous account on the next launch. Instead, show the login screen. This lets players switch between multiple in-game accounts.

## Conflict Resolution:

If your game implements the [user experience guideline for ideal authentication
flow](https://developer.android.com/games/pgs/platform-authentication#ux-auth-guidelines) and follows the seamless restore [implementation guidelines](https://developer.android.com/games/pgs/seamless-restore#implementation-guidelines), the
game won't encounter any conflict resolution. However, if the game encounters a
situation where a player has a local `Guest` account with significant progress,
but also has a cloud backup of the last played IGA linked to PGS, the game
shouldn't automatically overwrite the local data. Instead, present a prompt to
the player to choose between the two states.

For example, present a prompt:
**"Cloud save found. Do you want to restore Level 50 or keep local Level 5?"**.

## Bind last played IGA with PGS Player ID

In order to implement seamless restore, the game must verify that there is an
association between the latest IGA played by the player and their authenticated
PGS Player ID. You may do this by any of the following methods:

1. **Own Backend**: You may maintain the association of Player ID with your in-game identifier in your backend, additionally mapping the last played state with an in-game identifier so that you can retrieve the last played IGA for a player as soon as you get the Player ID after platform authentication.
2. **Recall API (Recommended)** : The [Recall API](https://developer.android.com/games/pgs/recall) is the recommended
   method for implementing seamless restore if you don't have your own robust
   identity backend. It allows Google to store the link between a user's
   Player ID and your internal In-Game Account ID (Persona).
   How Recall API works:

   1. **Store:** When a user plays, send a "Recall Token"
      (encrypted link to their IGA) to Google.

   2. **Retrieve:** On a new device, after PGS auth, you query
      the Recall API. If a token exists, you decrypt it to find the IGA
      ID and restore progress immediately.