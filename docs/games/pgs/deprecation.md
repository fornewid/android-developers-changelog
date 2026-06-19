---
title: https://developer.android.com/games/pgs/deprecation
url: https://developer.android.com/games/pgs/deprecation
source: md.txt
---

This document lists the deprecation schedule for the Play Games Services v1 SDK.

Following the deprecation of [Google Sign-in (GSI)](https://developer.android.com/identity/legacy/gsi) API and
[planned shutdown](https://android-developers.googleblog.com/2024/09/streamlining-android-authentication-credential-manager-replaces-legacy-apis.html) we are deprecating the Play Games Services v1 SDK and APIs.
You must migrate your game to the Play Games Services v2 SDK to get the latest
features.

The deprecation timelines are as follows:

| Date | Deprecation milestone | Impact | Developer action |
|---|---|---|---|
| Q3 2026 | GSI API Removal | If a game adds new features, such as liveops, missions, or maps, that don't rely on Google authentication except for Play Games Services v1 API these features will continue to work. <br /> If your game uses a third-party SDK or a Google SDK other than Play Games Services v1 that requires an authentication upgrade, upgrading to the latest version of that SDK might cause compilation errors. | 1. Follow the resolution path mentioned here when facing compilation error. 2. Ensure you migrate to Play Games Services v2 as per the solution path mentioned here right after the solution is released towards the end of Q2 2026. |
| June 2026 | Play Games Services v1 API removals | A new Play Games Services v1 SDK with removed GSI APIs will be published with no further bug fixes or updates to existing Play Games Services v1 features. If an existing v1 title ends up upgrading to latest Play Games Services v1 version, the Play Games Services functionalities on this new version will stop working. | 1. Games on Play Games Services v1 must not upgrade their v1 SDK to `com.google.android.gms:play-services-games:25.0.0`, which removes v1 APIs. 2. Any game that hasn't migrated to Play Games Services v2 might experience compilation errors because `play-services-auth` no longer provides GSI as of May 2026. 3. Following the timeline mentioned in previous section, games can maintain vigilance about upgrading other SDKs and ensure that other SDKs are not using the new Credential Manager SDK until they are migrated to Play Games Services v2. |
| May 2027 | Play Games Services v1 shutdown | All traffic from Play Games Services v1 blocked with no compilation of a game. Existing Play Games Services v1 APIs stop working in the production environment. | Only option is to migrate to Play Games Services v2 before this deadline to avoid player onboarding and login disruptions. |

- After September 2025, the games v1 SDK and APIs are deprecated. Existing
  titles with previous v1 integrations continue to function. Google Play
  prevents publishing new titles that use the v1 SDK and APIs.

- From June 15, 2026, the deprecated APIs will be removed from the SDK.

- From June 2027, the games v1 SDK will be removed. Calls to these APIs
  will fail, even if you're using previous versions of the SDK.

The following table lists the games v1 (SDK) versions, its deprecation dates,
and migration guides:

| SDK version | Release date | Migration guide |
|---|---|---|
| [play-services-games:v24.0.0](https://mvnrepository.com/artifact/com.google.android.gms/play-services-games) | September 12, 2025 Deprecated | [Migrate to v2(Java or Kotlin)](https://developer.android.com/games/pgs/android/migrate-to-v2) |
| [v0.10.15 Unity](https://github.com/playgameservices/play-games-plugin-for-unity/releases) | September 17, 2025 Deprecated | [Migrate to v2(Unity)](https://developer.android.com/games/pgs/unity/migrate-to-v2) |
| [play-services-games:v25.0.0](https://mvnrepository.com/artifact/com.google.android.gms/play-services-games) | June 15, 2026 Play Games Services v1 API removed from the SDK. | [Migrate to v2(Java or Kotlin)](https://developer.android.com/games/pgs/android/migrate-to-v2) |

## Sample impact of GSI API removal

Consider a scenario where an SDK, SDK1, retrieves a list of friends from a
player's Google Account. To use this feature, players must authenticate their
Google Account using the Google authentication SDK.

You might need to update the Google Authentication SDK in the following
situations:

- Resolve a critical bug in the authentication flow.
- Implement new passkey experiences offered by the Credential Manager SDK.

The following table describes the three scenarios for updating your game's
authentication integration:

- **Scenario 1:** SDK1 upgrades to the latest Google Authentication SDK.
- **Scenario 2:** SDK1 integrates with Credential Manager, leaving the Google Authentication SDK unchanged.
- **Scenario 3:** SDK1 integrates with Credential Manager and removes the Google Authentication SDK.

| Feature | Scenario 1 | Scenario 2 | Scenario 3 |
|---|---|---|---|
| Auth upgrade scenarios | 1. Not aware of GSI APIs removal, game upgrades to latest auth SDK. 2. Existing auth functionality breaks and SDK1 is forced to integrate Credential Manager SDK. 3. Game releases latest version with latest auth SDK and Credential Manager SDK. | Aware of GSI API removal, SDK1 does not upgrade the auth SDK but powers their Google authentication functionality using the Credential Manager SDK in their latest version. | In their latest version, SDK1 powers the Google authentication functionality using Credential Manager SDK and completely removes the auth SDK. |
| Play Games Services v1 SDK | Unchanged | Unchanged | Unchanged |
| What happens when game compiles | 1. Play Games Services v1 requires separate auth SDK integration -\> Since the auth SDK is upgraded with no GSI APIs, Play Games Services v1 will break. 2. Game gets compile time errors. 3. The game then tries to follow the resolution path. | Game gets compile time errors | The game then tries to follow the resolution path. |
| Possible Player experience | N/A. Since game is not able to compile so no publishing. | 1. Player sees the Play Games Services account selector when authenticating using Play Games Services v1. 2. Player sees Credential Manager bottom sheet when authenticating to SDK1 feature. | 1. Player sees the Play Games Services account selector when authenticating using Play Games Services v1. 2. Player sees Credential Manager bottom sheet when authenticating to SDK1 feature. |
| Resolution path for game developer | 1. Find out which SDK is causing the auth SDK upgrade. 2. Revert the SDK version of SDK1. 3. Re-compile their game with their feature. 4. If the new game feature requires an upgrade to SDK1, talk to SDK1 to adopt scenarios 2 or 3 for their version. | 1. Nothing 2. However, if you are also using a **Sign in with Google** button, you might have to use two types of **Google Sign In** flows for players. | 1. Nothing 2. However, if you are also using a **Sign in with Google** button, you might have to use two types of **Google Sign In** flows for players. |
| Eventual outcome for Play Games Services v1 | Game does not need to upgrade to Play Games Services v2, but SDK1 remains out of date. | Game does not need to upgrade from Play Games Services v1 to v2. | Game does not need to upgrade from Play Games Services v1 to v2. |