---
title: https://developer.android.com/games/pgs/platform-authentication
url: https://developer.android.com/games/pgs/platform-authentication
source: md.txt
---

> [!NOTE]
> **Note:** This guide is for the Play Games Services v2 SDK. For information on the previous version of this SDK, see the [Play Games Services v1
> documentation](https://developer.android.com/games/pgs/v1/signin).

The first step in integrating your game with Google Play Games Services (PGS) is
implementing Platform Authentication. This is required to access all other
features such as achievements, leaderboards, and events.

Since Play Games Services SDK automatically performs platform authentication at
the game launch, you need to integrate PGS v2 SDK with your game and implement
the recommended authentication flow, so that your game is ready to implement and
satisfy the Google Play Games Level Up [user experience guidelines](https://developer.android.com/games/guidelines).

## Authentication concepts

In Play Games Services v2, the concept of "signing in" is separated into two
distinct layers:
**platform authentication** and **in-game authentication**.

### Platform authentication

Play Games Services provides a platform engagement layer. It manages your
player's relationship with the Google Play Games ecosystem using
[Gamer Profile](https://play.google.com/games/profile), to access
features such as achievements, leaderboards, and quests. Platform authentication
has the following key characteristics:

- **Silent and automatic:** Authentication occurs automatically in the background when the game launches. Play Games Services doesn't require a manual **Sign in** button.
- **Player ID:** After successful platform authentication, Play Games Services provides a stable **Player ID**. This ID is consistent across devices for the same game. Use this ID primarily to track platform features, such as achievement progress.
- **Decoupled:** You must not use Play Games Services as your game's primary identity system to manage your player's in-game account (IGA), game progress, or inventory. Play Games Services serves as a persistent platform identifier.

### Player ID

A player ID is an identifier for a Play Games Services player account. Your
game can retrieve a player ID for any player that signs into your game using
Play Games Services authentication. Your [game client integration](https://developer.android.com/games/pgs/android/server-access#get-auth-code),
[game server integration](https://developer.android.com/games/guidelines#gameplay-continuity), and
[cloud-save service](https://developer.android.com/games/pgs/savedgames) can use the ID to securely access
player data from Play Games Services.

A player ID is consistent for a user when they play your game on multiple
devices. However, it is not always consistent between games.
For more information, see [next generation Player IDs](https://developer.android.com/games/pgs/next-gen-player-ids).

### In-game authentication

You manage the in-game account (IGA), which is the identity system that binds
player progress, inventory, and currency within your game.

- **Primary Identity:** You can use your own backend, Sign in with Google (SiWG), or other providers as the primary sign-in method.
- **Independence:** Players can sign in to Play Games Services (Platform Identity) to earn achievements while signed in to any specific IGA (for example, a guest account or a specific SiWG account).
- **Management of multiple IGAs:** Play Games Services handles only platform authentication. Your game manages the primary authentication of players into their IGAs. This means there is no change to your game's existing flows for players to switch between their IGAs. When players switch accounts, they remain authenticated to the Play Games platform through PGS, and you continue sending their data related to achievements and other PGS features against the persistent **Player ID**.

### Cross-platform continuity with SiWG

To help players carry their progress across Android, iOS, and web, use **Sign in
with Google** as a primary in-game authentication method. Consider the
following:

- **Sign in with Google button:** In PGS v1, the **Google Play** button often handled both platform and game sign-in. In v2, these are separate processes. Implement a standard **Sign in with Google** button for players to authenticate and access their IGA.
- **Google Sign-in SDKs:**
  - For both Android and iOS, use the standard Google Sign-in SDKs to authenticate players into their IGAs.
  - Use Google Open ID as the primary identifier for a player's in-game account.
  - Use the Play Games Services **Player ID** to report a player's progress on Play Games features, such as achievements.

## Recommended integration

To integrate your game with Play Games Services, follow these recommended steps:

### Initialization and authentication

This step is required to initialize and authenticate your game:

Implement platform authentication by initializing the Play Games Services v2 SDK
on startup. For more information, see
[platform authentication for Android games](https://developer.android.com/games/pgs/android/android-signin).
This step is required to access Play Games Services features, such as
achievements and leaderboards.

Authentication runs as a silent background process during game launch. Existing
Play Games Services users see a welcome message after successful authentication.
Users who don't have a Play Games Services profile are prompted to
[create a profile](https://developer.android.com/games/pgs/platform-authentication#automatic-sign-in) during SDK initialization.

![Automatic sign-in prompt](https://developer.android.com/static/images/games/pgs/automatic-sign-in.gif)

### Profile creation

Players need a Play Games Services profile to engage with the platform. Some
players might not have a Play Games Services profile when they start your game.
These players will be asked to create one.

Auto-triggered profile creation prompts appear automatically by default when you
launch a game without a Play Games Services profile.
[![Profile creation prompt when you launch a game.](https://developer.android.com/static/images/games/pgs/profileprompt.png)](https://developer.android.com/static/images/games/pgs/profileprompt.png) Profile creation prompt when you launch a game (click to enlarge).

### In-game authentication

Once platform authentication has been successfully executed, developers should
implement the following steps for players to access their IGAs,
depending on the current game state:

1. If an active game session exists on the device, allow the player to resume their current session.
2. If no active game session is present:
   1. In the case of a [seamless restore](https://developer.android.com/games/pgs/seamless-restore) scenario where a last played IGA is associated with the PGS Player ID, proceed to automatically restore the associated IGA.
   2. Otherwise, present the player with your application's designated login or account creation screen. Players can then choose their preferred authentication method to establish or log into an existing IGA.

### OAuth scopes

Play Games Services relies on the
[OAuth system](https://developers.google.com/identity/protocols/OAuth2)
to allow players to give your game access to their account. Play Games Services
has a unique scope for games (`games-lite`) and relies on another scope
(`drive.appdata`) if your game uses the saved games feature. The saved games
feature gives access to the user's Google Drive account, which is where the game
data is stored.

When using the Play Games Services v2 SDK, you can request extra
[OAuth scopes](https://developers.google.com/identity/protocols/googlescopes).
If you need extra OAuth scopes, we recommend calling `requestServerSideAccess`.
For more information, see
[get the server auth code](https://developer.android.com/games/pgs/android/server-access#get-auth-code) or [retrieve server authentication codes](https://developer.android.com/games/pgs/unity/unity-start#retrieve-auth-codes).

## User experience guideline for ideal authentication flow

The following guidelines explain the recommended authentication flow with PGS v2
integration. They cover scenarios for new, existing, and returning users, and
guest mode.

### New player

This flow applies to a user launching the game for the very first time on a
device with no prior play history with the game.

1. Upon launch, the PGS SDK initializes to authenticate the user's platform identity (PGS Player ID).
2. After this background handshake, the game displays IGA creation options to the player, for example, **Create new account** , **Sign in with Google**, or other social login methods.
3. Once the player creates or selects an IGA, the game binds this account to the chosen primary identifier in their backend.
4. The game also binds this chosen IGA to the PGS Player ID, marking it as the last played IGA for [seamless restore](https://developer.android.com/games/pgs/seamless-restore).

[![New Player with signed in PGS Profile](https://developer.android.com/static/images/games/pgs/scenario1a.png)](https://developer.android.com/static/images/games/pgs/scenario1a.png) New Player with signed in PGS Profile (click to enlarge). [![New Player with no PGS profile](https://developer.android.com/static/images/games/pgs/scenario1b.png)](https://developer.android.com/static/images/games/pgs/scenario1b.png) New Player with no PGS profile (click to enlarge). [![New Player with signed in PGS profile](https://developer.android.com/static/images/games/pgs/scenario1c.png)](https://developer.android.com/static/images/games/pgs/scenario1c.png) New Player with signed in PGS profile (click to enlarge).

### Players with active sessions

This scenario describes players launching the game on a device where they
already have an active session. The goal is to provide a seamless entry
experience.

1. When the player launches the app, PGS silently authenticates in the background providing you with Player ID to track progress against achievements and other play games features.
2. Simultaneously, where applicable, the game bypasses login screens and immediately signs the player into their active IGA session or the last played IGA associated with their Player ID, so they can resume gameplay immediately.

[![Launch game on same device with signed-in PGS profile](https://developer.android.com/static/images/games/pgs/scenario2a.png)](https://developer.android.com/static/images/games/pgs/scenario2a.png) Launch game on same device with signed-in PGS profile (click to enlarge). [![Launch game on same device with signed-out PGS profile](https://developer.android.com/static/images/games/pgs/scenario2b.png)](https://developer.android.com/static/images/games/pgs/scenario2b.png) Launch game on same device with signed-out PGS profile (click to enlarge). [![Launch game on same device with no PGS profile](https://developer.android.com/static/images/games/pgs/scenario2c.png)](https://developer.android.com/static/images/games/pgs/scenario2c.png) Launch game on same device with no PGS profile (click to enlarge). [![Launch game on new device with signed-in PGS profile and a linked IGA](https://developer.android.com/static/images/games/pgs/scenario2d.png)](https://developer.android.com/static/images/games/pgs/scenario2d.png) Launch game on new device with signed-in PGS profile and a linked IGA (click to enlarge). [![Launch game on new device with signed-in PGS profile and no linked IGA](https://developer.android.com/static/images/games/pgs/scenario2e.png)](https://developer.android.com/static/images/games/pgs/scenario2e.png) Launch game on new device with signed-in PGS profile and no linked IGA (click to enlarge). [![Launch game on new device with signed-out PGS profile](https://developer.android.com/static/images/games/pgs/scenario2f.png)](https://developer.android.com/static/images/games/pgs/scenario2f.png) Launch game on new device with signed-out PGS profile (click to enlarge). [![Launch game on new device with no PGS profile](https://developer.android.com/static/images/games/pgs/scenario2g.png)](https://developer.android.com/static/images/games/pgs/scenario2g.png) Launch game on new device with no PGS profile (click to enlarge).

### Players switching accounts

This flow occurs when a player with an active session navigates to the game
settings to switch accounts.
For example, signing out of a main account to use an alternate account.

1. The player signs out of the current IGA, but the PGS platform connection remains active.
2. When the player logs in with a different IGA, the game binds this new account to the current PGS Player ID as the last played IGA only for seamless restore.

[![Switch to an IGA not bound with any PGS profile](https://developer.android.com/static/images/games/pgs/scenario3.png)](https://developer.android.com/static/images/games/pgs/scenario3.png) Switch to an IGA not bound with any PGS profile (click to enlarge). [![Switch to an IGA bound with same signed-in PGS profile](https://developer.android.com/static/images/games/pgs/scenario3b.png)](https://developer.android.com/static/images/games/pgs/scenario3b.png) Switch to an IGA bound with same signed-in PGS profile (click to enlarge). [![Switch to an IGA bound with different PGS profile](https://developer.android.com/static/images/games/pgs/scenario3c.png)](https://developer.android.com/static/images/games/pgs/scenario3c.png) Switch to an IGA bound with different PGS profile (click to enlarge). [![Switching IGA with no PGS profile on device](https://developer.android.com/static/images/games/pgs/scenario3d.png)](https://developer.android.com/static/images/games/pgs/scenario3d.png) Switching IGA with no PGS profile on device (click to enlarge). [![Switching IGA with signed-out PGS profile](https://developer.android.com/static/images/games/pgs/scenario3e.png)](https://developer.android.com/static/images/games/pgs/scenario3e.png) Switching IGA with signed-out PGS profile (click to enlarge). [![Switch to IGA that does not exist](https://developer.android.com/static/images/games/pgs/scenario3f.png)](https://developer.android.com/static/images/games/pgs/scenario3f.png) Switch to IGA that does not exist (click to enlarge).

### Seamless restore for returning players

This scenario applies when a player launches the game after an inactive period,
a re-install, or on a completely new device. The game is recommended to
implement [seamless restore](https://developer.android.com/games/pgs/seamless-restore).

1. Upon launch, PGS authenticates the user and provides the PGS Player ID to the game.
2. The game checks its backend (or retrieved recall token if using [Recall](https://developer.android.com/games/pgs/recall) API) to see if a last played IGA is already linked to this PGS ID.
3. If a link is found, the game automatically restores the player's progress and logs them in, skipping the manual login screen entirely.
4. Else, the game presents the player with their login screen
   1. The player then chooses a login method and signs into an IGA
   2. The game then binds this IGA with PGS player ID as the last played IGA for seamless restore.

[![Returning Player with signed out PGS profile](https://developer.android.com/static/images/games/pgs/scenario4a.png)](https://developer.android.com/static/images/games/pgs/scenario4a.png) Returning Player with signed out PGS profile (click to enlarge). [![Returning Player with signed in PGS profile and linked IGA](https://developer.android.com/static/images/games/pgs/scenario4b.png)](https://developer.android.com/static/images/games/pgs/scenario4b.png) Returning Player with signed in PGS profile and linked IGA (click to enlarge). [![Returning Player with signed in PGS profile and no linked IGA](https://developer.android.com/static/images/games/pgs/scenario4c.png)](https://developer.android.com/static/images/games/pgs/scenario4c.png) Returning Player with signed in PGS profile and no linked IGA (click to enlarge). [![Returning Player with no PGS profile](https://developer.android.com/static/images/games/pgs/scenario4d.png)](https://developer.android.com/static/images/games/pgs/scenario4d.png) Returning Player with no PGS profile (click to enlarge).

### Guest mode

Players can launch the game and play using a local guest account.
PGS still authenticates in the background. If the player chooses to **Save
Progress**, the game converts the guest session into a permanent IGA and binds
it to the PGS Player ID.
[![Guest Mode - No IGA created](https://developer.android.com/static/images/games/pgs/scenario5a.png)](https://developer.android.com/static/images/games/pgs/scenario5a.png) Guest Mode - No IGA created (click to enlarge). [![Guest Mode - IGA created](https://developer.android.com/static/images/games/pgs/scenario5b.png)](https://developer.android.com/static/images/games/pgs/scenario5b.png) Guest Mode - IGA created (click to enlarge).