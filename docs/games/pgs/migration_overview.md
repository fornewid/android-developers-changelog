---
title: https://developer.android.com/games/pgs/migration_overview
url: https://developer.android.com/games/pgs/migration_overview
source: md.txt
---

Google Play Games Services, games v1 SDK relies on Google Sign-In for Android which is
deprecated and will be removed from the [Google Play services Auth
SDK](https://maven.google.com/web/index.html?q=play-services-auth#com.google.android.gms:play-services-auth)
(`com.google.android.gms:play-services-auth`) in 2025. New games apps can use
games v1 until 2025. The Google Sign-In removal introduces dependency issues for
existing games apps. Migrate existing games apps from the [games v1
SDK](https://developers.google.com/android/games_v1/reference/com/google/android/gms/games/package-summary)
to the [games v2
SDK](https://developers.google.com/android/reference/com/google/android/gms/games/package-summary)
resolves dependency issues introduced by the Google Sign-In removal.

Google Play Games Services v1 to v2 migration is a significant update that simplifies
development and supports cross-platform gaming. Google Play Games Services v2 decouples
platform and in-game identity, acting as a platform-level identity system that
automatically authenticates players at launch. Platform identity is now separate
from the primary in-game account system, which you must manage independently
using tools like Sign in with Google or proprietary backends. The
Play Games Services v2 SDK integration uses the player ID for
platform features like achievements and leaderboards without altering existing
onboarding or login flows.

This document helps you understand the interactions between the games
application and various SDKs.
Because of the official deprecation timeline, you must follow this migration
guide's architectural principles, pathways, and player communication strategies
to ensure player continuity.

## SDK interactions

The diagrams illustrate the interaction between a games application on
Android, Google Mobile Services (GMS) Core, Play Games Services,
and a third-party (3P) games server. It highlights how the application uses
Google's services for authentication and game features, while also
interacting with a separate third-party system.

### games v2 (Current)

[![Interaction between a Games Application on
Android, GMS Core, Play Games Services,
and a third-party (3P) games server.](https://developer.android.com/static/images/games/pgs/gamesv2.png)](https://developer.android.com/static/images/games/pgs/gamesv2.png) Interaction between a Games Application on Android, GMS Core, Play Games Services, and a third-party (3P) game server. (click to enlarge).

### games v1 (Legacy)

[![Interaction between a Games Application on
Android, GMS Core, Play Games Services,
and a third-party (3P) games server.](https://developer.android.com/static/images/games/pgs/gamesv1.png)](https://developer.android.com/static/images/games/pgs/gamesv1.png) Interaction between a Games Application on Android, GMS Core, Play Games Services, and a third-party (3P) games server. (click to enlarge).

The following is a brief overview of the components and SDKs:

- **Games Application.**
  - This represents the user's game application running on an Android-powered device.
  - It contains two primary components:
    - **games v1 or games v2 SDK.** The client-side SDK responsible for interacting with Play Games Services.
    - **Auth SDK.** Google Play services Auth SDK is responsible for handling user authentication and authorization flows in games v1.
  - Both SDKs communicate using AIDL (Android Interface Definition Language), indicating a communication pattern between different processes or services.
- **GMS Core also called as Google Play Services.**
  - This is the Google-proprietary layer on Android.
  - The games application uses two GMS Core modules:
    - **Games Module.** provides game-specific features, such as leaderboards, achievements, and game state management.
    - **Auth Module.** Handles user authentication and authorization operations.
  - The Games and Auth SDKs in the games application communicate with the corresponding modules using [AIDL](https://developer.android.com/develop/background-work/services/aidl) interfaces, indicating inter-process communication (IPC).

  <br />

- **Play Games Services gateway.**
  - A logical gateway that mediates communication between the GMS Core and the Play Games Services server.
  - Handles API requests, data transformation, and authentication for the server communication.
- **Play Games Services server.**
  - Represents Play Games Services backend services responsible for storing game data, managing user accounts, and facilitating multiplayer features.
- **Third-party games gateway.**
  - If your games application qualifies as a third-party (3P) application, the client library communicates with the Play Games Services servers through the third-party games servers.
  - Implies that the application can also authenticate with a different service provider.
- **Third-party games server.**
  - Represents an optional external server the games application can interact with, likely for custom features or data management.
  - Communication with the application occurs through the third-party games gateway.

<br />

## Why migrate your title to Play Games Services v2

The transition from Play Games Services v1 to v2 is a major architectural
modernization that simplifies development and supports cross-platform gaming.

Unlike v1, which served as a primary in-game identity system, Play Games Services
v2 decouples platform and in-game identity. It acts as a *platform-level
identity system* that automatically authenticates players at launch to manage
features like achievements and leaderboards.

You must now manage your game's primary in-game account system independently
using tools such as Sign in with Google or proprietary backends.
The Play Games Services v2 SDK lets games use the
Play Games Services player ID to access platform features without changing
existing onboarding or login flows. This document guides you through the
migration, covering architectural principles, pathways, and player communication
strategies. Adherence is critical for player continuity given the official
deprecation timeline.

## Compare platform authentication and in-game authentication

In Play Games Services v2, the concept of "logging in" is decoupled into two
distinct layers:

- **Platform identity.** SDK handles platform authentication.
- **In-game identity.**

### Platform authentication

Play Games Services functions strictly as a platform engagement layer. It manages
the player's relationship with the Google Play Games ecosystem (Achievements,
Leaderboards, and Events) rather than with authenticating into a specific game
account or inventory.

- **Silent \& Automatic:** Authentication happens automatically in the background when the game launches. There is no manual "Sign in" button required for Play Games Services itself.
- **The Player ID:** Upon successful platform authentication, Play Games Services provides a stable **Player ID**. This ID is consistent across devices for the same game but should be used primarily to track platform stats (like Achievement progress).
- **Decoupled:** Play Games Services v2 must **not** be used as your game's primary identity system for managing player's in-game account with their game progress or inventory. Play Games Services v2 acts strictly as a secondary, persistent platform identifier.

### In-game authentication

Developers are responsible for managing the "In-Game Account" (IGA). This is the
identity system that binds a player's progress, inventory, and currency within
your game.

- **Primary Identity:** You may use your own backend, Sign in with Google (SiWG), or other providers as the primary login method.
- **Independence:** A player can be signed into Play Games Services (Platform Identity) to earn achievements while being logged into any specific In-Game Account. For example, a guest account, or a specific SiWG account.
- **Management of Multiple In-Game Accounts:** Play Games Services is responsible for only the platform authentication with your game managing the primary authentication of players into their in-game accounts (IGAs). This means that there would be no change to your game's existing flows about how players switch between their in-game accounts. While the players do so, they would still remain authenticated to the Play Games platform using Play Games Services and you would continue sending their data related to achievements and other Play Games Services features against the persistent Player ID.

## Migration requirement: Bind in-game accounts with Google Open ID instead of Play Games Services Player ID

In Play Games Services v1, developers used Play Games Services as the primary
identity provider. A "Google Play" button would link a player's In-Game Account
(IGA) directly to their `Player ID`.

Play Games Services v2 shifts this by providing automatic, silent **platform
authentication** at launch. The resulting `Player ID` is now used exclusively
for platform features like leaderboards and achievements, separate from the main
account login.

Games must now manage **primary identity** independently through a dedicated
login screen offering methods like "Sign in with Google" (SiWG) or other social
accounts.
Crucially, **Play Games Services v2 must not be used as a primary identity
system**.

This architectural shift requires a corresponding change in how developers
structure their account data. The In-Game Account (IGA) must be decoupled from
being primarily bound to the `Player ID`.

Instead, the IGA must now be bound to a stable, primary identifier that is
independent of Play Games Services. The recommended identifier is the
`Open ID` provided by the Sign in with Google (SiWG) flow. This
`Open ID` serves as the unique, persistent key for the player's primary account
within your system.

However, the IGA could *still* be linked to the `Player ID` as a secondary
binding. This secondary link serves two critical functions:

1. It allows the game to continue tracking and updating progress for Play Games features (achievements, etc.) associated with that specific player.
2. It enables the "Seamless Restore" functionality, allowing the game to automatically log a player into their most recently used IGA only on a new device or after a reinstall.

Understanding this decoupled identity model is the key to unlocking the correct
technical migration path for your game.

## Feature comparison

This table gives you a feature comparison between the games v1 and games v2
SDKs:

| **Feature** | **games v1 SDK** | **games v2 SDK** |
|---|---|---|
| Authentication | Integration with `play-services-auth` required. | Simplified and streamlined; no `play-services-auth` required. |
| Authorization | Additional code for success, failures, and retries. | Managed by the SDK |
| Server Access Token | Can request additional [OAuth 2.0 scopes](https://developers.google.com/identity/protocols/oauth2/scopes#oauth2) with `GoogleSigninClient`. <br /> Additional code for error handling during authentication. | Can request three basic OAuth 2.0 identity scopes with `GamesSignInClient` when requesting server-side access to Play Games Services web APIs. For more information, see [Server-side access to Play Games Services](https://developer.android.com/games/pgs/android/server-access) and [Retrieve server authentication codes](https://developer.android.com/games/pgs/unity/unity-start#retrieve-auth-codes). |
| Sign-in process | Uses `GoogleSigninClient`. <br /> Additional code for handling of boilerplate code for automatic authentication and error handling. | Uses `GamesSignInClient`. <br /> SDK handles boilerplate code, automatic authentication, and error handling. The "signing in" is separated into two distinct layers: - Platform authentication: handled by the Play Games Services v2 SDK. - In-game authentication: handled by the game. |
| Welcome Popup | Additional code required. Developers can control its placement and timing. | No Additional code required. Consistent user interface across all games configured with games v2 SDK. |
| Dependencies | Requires `play-services-auth`. | The Games module takes care of authorization and authentication. You need not add any additional dependencies. |
| Sign-out | Uses `GoogleSignInClient.signOut`. | Sign-out API is not required because Play Games Services v2 is a persistent platform identity. |
| Multiple Play Games Services accounts and per-game settings | Account management is possible within your game. | Users can change the Play Games Services profile in the mobile device settings. For more information, see [how to switch Play Games profiles on mobile](https://support.google.com/googleplay/answer/14754238). |