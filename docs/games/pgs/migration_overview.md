---
title: https://developer.android.com/games/pgs/migration_overview
url: https://developer.android.com/games/pgs/migration_overview
source: md.txt
---

Google Play Games Services, games v1 SDK relies on Google Sign-In for Android which is
deprecated and will be removed from the
[Google Play services Auth SDK](https://maven.google.com/web/index.html?q=play-services-auth#com.google.android.gms:play-services-auth)
(`com.google.android.gms:play-services-auth`) in 2025.
New games apps can use games v1 until 2025. The Google Sign-In removal
introduces dependency issues for existing games apps. Migrate existing games
apps from the [games v1
SDK](https://developers.google.com/android/games_v1/reference/com/google/android/gms/games/package-summary)
to the [games v2 SDK](https://developers.google.com/android/reference/com/google/android/gms/games/package-summary)
resolves dependency issues introduced by the Google Sign-In removal.

This document helps you understand the interactions between the games
application and various SDKs. This document also compares the application's
features with those of the Play Games Services games v1 and games v2 SDKs.

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

## Feature comparison

This table gives you a feature comparison between the games v1 and games v2
SDKs:

| **Feature** | **games v1 SDK** | **games v2 SDK** |
|---|---|---|
| Authentication | Integration with `play-services-auth` required. | Simplified and streamlined; no `play-services-auth` required. |
| Authorization | Additional code for success, failures, and retries. | Managed by the SDK |
| Server Access Token | Can request additional [OAuth 2.0 scopes](https://developers.google.com/identity/protocols/oauth2/scopes#oauth2) with `GoogleSigninClient`. <br /> Additional code for error handling during authentication. | Can request three basic OAuth 2.0 identity scopes with `GamesSignInClient` when requesting server-side access to Play Games Services web APIs. For more information, see [Server-side access to Play Games Services](https://developer.android.com/games/pgs/android/server-access) and [Retrieve server authentication codes](https://developer.android.com/games/pgs/unity/unity-start#retrieve-auth-codes). |
| Sign-in Process | Uses `GoogleSigninClient`. <br /> Additional code for handling of boilerplate code for automatic authentication and error handling. | Uses `GamesSignInClient`. <br /> SDK handles boilerplate code, automatic authentication, and error handling. |
| Welcome Popup | Additional code required. Developers can control its placement and timing. | No Additional code required. Consistent user interface across all games configured with games v2 SDK. |
| Dependencies | Requires `play-services-auth`. | The Games module takes care of authorization and authentication. You need not add any additional dependencies. |
| Sign-out | Uses `GoogleSignInClient.signOut`. | Sign-out API is not supported. |
| Multiple Play Games Services accounts and per-game settings | Account management is possible within your game. | Users can change the Play Games Services profile in the mobile device settings. For more information, see [how to switch Play Games profiles on mobile](https://support.google.com/googleplay/answer/14754238). |