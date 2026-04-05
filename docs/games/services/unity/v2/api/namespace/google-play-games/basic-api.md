---
title: GooglePlayGames.BasicApi Namespace  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.




# GooglePlayGames.BasicApi

## Summary

| Enumerations | |
| --- | --- |
| `AuthScope{   EMAIL,   PROFILE,   OPEN_ID }` | enum Represents type-safe constants for the specific OAuth 2.0 authorization scopes used when requesting server-side access to Play Games Services web APIs. |
| `CommonStatusCodes{   SuccessCached = -1,   Success = 0,   ServiceMissing = 1,   ServiceVersionUpdateRequired = 2,   ServiceDisabled = 3,   SignInRequired = 4,   InvalidAccount = 5,   ResolutionRequired = 6,   NetworkError = 7,   InternalError = 8,   ServiceInvalid = 9,   DeveloperError = 10,   LicenseCheckFailed = 11,   Error = 13,   Interrupted = 14,   Timeout = 15,   Canceled = 16,   ApiNotConnected = 17,   AuthApiInvalidCredentials = 3000,   AuthApiAccessForbidden = 3001,   AuthApiClientError = 3002,   AuthApiServerError = 3003,   AuthTokenError = 3004,   AuthUrlResolution = 3005 }` | enum Common status codes. |
| `DataSource{   ReadCacheOrNetwork,   ReadNetworkOnly }` | enum A enum describing where game data can be fetched from. |
| `FriendsListVisibilityStatus{   Unknown = 0,   Visible = 1,   ResolutionRequired = 2,   Unavailable = 3,   NetworkError = -4,   NotAuthorized = -5 }` | enum Values specifying the visibility status of the friends list. |
| `LeaderboardCollection{   Public = 1,   Social = 2 }` | enum Values specifying which leaderboard collection to use. |
| `LeaderboardStart{   TopScores = 1,   PlayerCentered = 2 }` | enum Values specifying the start location for fetching scores. |
| `LeaderboardTimeSpan{   Daily = 1,   Weekly = 2,   AllTime = 3 }` | enum Values specifying which leaderboard timespan to use. |
| `LoadFriendsStatus{   Unknown = 0,   Completed = 1,   LoadMore = 2,   ResolutionRequired = -3,   InternalError = -4,   NotAuthorized = -5,   NetworkError = -6 }` | enum Values specifying the status of the friends list. |
| `ResponseStatus{   Success = 1,   SuccessWithStale = 2,   LicenseCheckFailed = -1,   InternalError = -2,   NotAuthorized = -3,   VersionUpdateRequired = -4,   Timeout = -5,   ResolutionRequired = -6 }` | enum Native response status codes |
| `ScorePageDirection{   Forward = 1,   Backward = 2 }` | enum Enum representing the direction of score page navigation. |
| `SignInInteractivity{   NoPrompt,   CanPromptAlways,   CanPromptOnce }` | enum Enum to specify the interactivity of the sign in flow. |
| `SignInStatus{   Success,   InternalError,   Canceled }` | enum Enum to specify the sign in status. |
| `UIStatus{   Valid = 1,   InternalError = -2,   NotAuthorized = -3,   VersionUpdateRequired = -4,   Timeout = -5,   UserClosedUI = -6,   NetworkError = -20 }` | enum Native response status codes for UI operations. |

| Classes | |
| --- | --- |
| [GooglePlayGames.BasicApi.Achievement](/games/services/unity/v2/api/class/google-play-games/basic-api/achievement) | Data interface for retrieving achievement information. |
| [GooglePlayGames.BasicApi.AuthResponse](/games/services/unity/v2/api/class/google-play-games/basic-api/auth-response) | Represents the response received from Play Games Services when requesting a server-side OAuth 2.0 authorization code for the signed-in player. |
| [GooglePlayGames.BasicApi.AuthScopeExtensions](/games/services/unity/v2/api/class/google-play-games/basic-api/auth-scope-extensions) | Extensions for the AuthScope enum. |
| [GooglePlayGames.BasicApi.CommonTypesUtil](/games/services/unity/v2/api/class/google-play-games/basic-api/common-types-util) | Utility class for common types. |
| [GooglePlayGames.BasicApi.DummyClient](/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client) | Dummy client used in Editor. |
| [GooglePlayGames.BasicApi.LeaderboardScoreData](/games/services/unity/v2/api/class/google-play-games/basic-api/leaderboard-score-data) | Leaderboard score data. |
| [GooglePlayGames.BasicApi.Player](/games/services/unity/v2/api/class/google-play-games/basic-api/player) | Represents a player. |
| [GooglePlayGames.BasicApi.PlayerProfile](/games/services/unity/v2/api/class/google-play-games/basic-api/player-profile) | Represents a player, a real-world person (tied to a Games account). |
| [GooglePlayGames.BasicApi.PlayerStats](/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats) | [Player](/games/services/unity/v2/api/class/google-play-games/basic-api/player#class_google_play_games_1_1_basic_api_1_1_player) stats. |
| [GooglePlayGames.BasicApi.RecallAccess](/games/services/unity/v2/api/class/google-play-games/basic-api/recall-access) | Recall Access data. |
| [GooglePlayGames.BasicApi.ScorePageToken](/games/services/unity/v2/api/class/google-play-games/basic-api/score-page-token) | Score page token. |

| Interfaces | |
| --- | --- |
| [GooglePlayGames.BasicApi.IPlayGamesClient](/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client) | Defines an abstract interface for a Play Games Client. |

| Namespaces | |
| --- | --- |
| [GooglePlayGames.BasicApi.Events](/games/services/unity/v2/api/namespace/google-play-games/basic-api/events) |  |
| [GooglePlayGames.BasicApi.Nearby](/games/services/unity/v2/api/namespace/google-play-games/basic-api/nearby) |  |
| [GooglePlayGames.BasicApi.SavedGame](/games/services/unity/v2/api/namespace/google-play-games/basic-api/saved-game) |  |

## Enumerations

### AuthScope

```
 AuthScope
```

Represents type-safe constants for the specific OAuth 2.0 authorization scopes used when requesting server-side access to Play Games Services web APIs.

| Properties | |
| --- | --- |
| `EMAIL` | See your primary Google Account email address. |
| `OPEN_ID` | Associate you with your personal info on Google. |
| `PROFILE` | See your personal info, including any personal info you've made publicly available. |

### CommonStatusCodes

```
 CommonStatusCodes
```

Common status codes.

See <https://developers.google.com/android/reference/com/google/android/gms/common/api/CommonStatusCodes>

| Properties | |
| --- | --- |
| `ApiNotConnected` | The client attempted to call a method from an API that failed to connect. |
| `AuthApiAccessForbidden` | Access is forbidden. |
| `AuthApiClientError` | Error related to the client. |
| `AuthApiInvalidCredentials` | Invalid credentials were provided. |
| `AuthApiServerError` | Error related to the server. |
| `AuthTokenError` | Error related to token. |
| `AuthUrlResolution` | Error related to auth URL resolution. |
| `Canceled` | The result was canceled either due to client disconnect or cancel(). |
| `DeveloperError` | The application is misconfigured. |
| `Error` | The operation failed with no more detailed information. |
| `InternalError` | An internal error occurred. |
| `Interrupted` | A blocking call was interrupted while waiting and did not run to completion. |
| `InvalidAccount` | The client attempted to connect to the service with an invalid account name specified. |
| `LicenseCheckFailed` | The application is not licensed to the user. |
| `NetworkError` | A network error occurred. |
| `ResolutionRequired` | Completing the operation requires some form of resolution. |
| `ServiceDisabled` | The installed version of Google Play services has been disabled on this device. |
| `ServiceInvalid` | The version of the Google Play services installed on this device is not authentic. |
| `ServiceMissing` | Google Play services is missing on this device. |
| `ServiceVersionUpdateRequired` | The installed version of Google Play services is out of date. |
| `SignInRequired` | The client attempted to connect to the service but the user is not signed in. |
| `Success` | The operation was successful. |
| `SuccessCached` | The operation was successful, but the device's cache was used. |
| `Timeout` | Timed out while awaiting the result. |

### DataSource

```
 DataSource
```

A enum describing where game data can be fetched from.

| Properties | |
| --- | --- |
| `ReadCacheOrNetwork` | Allow a read from either a local cache, or the network.  Values from the cache may be stale (potentially producing more write conflicts), but reading from cache may still allow reads to succeed if the device does not have internet access and may complete more quickly (as the reads can occur locally rather requiring network roundtrips). |
| `ReadNetworkOnly` | Primarily attempts to read data from the network.  This option prioritizes fetching the latest data from the network. However, if the network is unavailable, it may fall back to reading from the local cache to ensure the operation can complete. As a result, the data returned might not be the most up-to-date version from the server, and a successful call does not guarantee that the network was accessible at that moment. |

### FriendsListVisibilityStatus

```
 FriendsListVisibilityStatus
```

Values specifying the visibility status of the friends list.

| Properties | |
| --- | --- |
| `NetworkError` | An network error occurred. |
| `NotAuthorized` | The player is not authorized to perform the operation. |
| `ResolutionRequired` | Constant indicating that the developer does not have access to the friends list, but can call the AskForLoadFriendsResolution API to show a consent dialog. |
| `Unavailable` | Constant indicating that the friends list is currently unavailable for this user, and it is not possible to request access at this time, either because the user has permanently declined or the friends feature is not available to them.  In this state, any attempts to request access to the friends list will be unsuccessful. |
| `Unknown` | Constant indicating that currently it's unknown if the friends list is visible to the game, game can ask for permission from user. |
| `Visible` | Constant indicating that the friends list is currently visible to the game. |

### LeaderboardCollection

```
 LeaderboardCollection
```

Values specifying which leaderboard collection to use.

| Properties | |
| --- | --- |
| `Public` | Public leaderboards contain the scores of players who are sharing their gameplay publicly. |
| `Social` | Social leaderboards contain the scores of players in the viewing player's circles. |

### LeaderboardStart

```
 LeaderboardStart
```

Values specifying the start location for fetching scores.

| Properties | |
| --- | --- |
| `PlayerCentered` | Start fetching relative to the player's score. |
| `TopScores` | Start fetching scores from the top of the list. |

### LeaderboardTimeSpan

```
 LeaderboardTimeSpan
```

Values specifying which leaderboard timespan to use.

| Properties | |
| --- | --- |
| `AllTime` | All time scores. |
| `Daily` | Daily scores. The day resets at 11:59 PM PST. |
| `Weekly` | Weekly scores. The week resets at 11:59 PM PST on Sunday. |

### LoadFriendsStatus

```
 LoadFriendsStatus
```

Values specifying the status of the friends list.

| Properties | |
| --- | --- |
| `Completed` | All the friends have been loaded. |
| `InternalError` | An internal error occurred. |
| `LoadMore` | There are more friends to load. |
| `NetworkError` | An network error occurred. |
| `NotAuthorized` | The player is not authorized to perform the operation. |
| `ResolutionRequired` | The game doesn't have permission to access the player's friends list.  No friends loaded. |
| `Unknown` | An unknown value to return when loadFriends is not available. |

### ResponseStatus

```
 ResponseStatus
```

Native response status codes

These values are returned by the native SDK API. NOTE: These values are different than the CommonStatusCodes.

| Properties | |
| --- | --- |
| `InternalError` | An internal error occurred. |
| `LicenseCheckFailed` | The application is not licensed to the user. |
| `NotAuthorized` | The player is not authorized to perform the operation. |
| `ResolutionRequired` | Constant indicating that the developer does not have access to the friends list, but can call the AskForLoadFriendsResolution API to show a consent dialog. |
| `Success` | The operation was successful. |
| `SuccessWithStale` | The operation was successful, but the device's cache was used. |
| `Timeout` | Timed out while awaiting the result. |
| `VersionUpdateRequired` | The installed version of Google Play services is out of date. |

### ScorePageDirection

```
 ScorePageDirection
```

Enum representing the direction of score page navigation.

| Properties | |
| --- | --- |
| `Backward` | Represents the backward direction (previous page). |
| `Forward` | Represents the forward direction (next page). |

### SignInInteractivity

```
 SignInInteractivity
```

Enum to specify the interactivity of the sign in flow.

| Properties | |
| --- | --- |
| `CanPromptAlways` | This may show UIs, consent dialogs, etc.  At the end of the process, callback will be invoked to notify of the result. Once the callback returns true, the user is considered to be authenticated. |
| `CanPromptOnce` | When this is selected, [PlayGamesPlatform.Authenticate](/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a2743441943ae1a4f5916c47c6a93b0df) does the following in order:  1. Attempt to silent sign in. 2. If silent sign in fails, check if user has previously declined to sign in and don’t prompt interactive sign in if they have. 3. Check the internet connection and fail with NO\_INTERNET\_CONNECTION if there is no internet connection. 4. Prompt interactive sign in. 5. If the interactive sign in is not successful (user declines or cancels), then remember this for step 2 the next time the user opens the game and don’t ask for sign-in. |
| `NoPrompt` | no UIs will be shown (if UIs are needed, it will fail rather than show them). |

### SignInStatus

```
 SignInStatus
```

Enum to specify the sign in status.

| Properties | |
| --- | --- |
| `Canceled` | The sign in was canceled. |
| `InternalError` | An internal error occurred. |
| `Success` | The operation was successful. |

### UIStatus

```
 UIStatus
```

Native response status codes for UI operations.

These values are returned by the native SDK API.

| Properties | |
| --- | --- |
| `InternalError` | An internal error occurred. |
| `NetworkError` | An network error occurred. |
| `NotAuthorized` | The player is not authorized to perform the operation. |
| `Timeout` | Timed out while awaiting the result. |
| `UserClosedUI` | UI closed by user. |
| `Valid` | The result is valid. |
| `VersionUpdateRequired` | The installed version of Google Play services is out of date. |