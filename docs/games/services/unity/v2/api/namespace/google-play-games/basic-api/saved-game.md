---
title: GooglePlayGames.BasicApi.SavedGame Namespace  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api/saved-game
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.




# GooglePlayGames.BasicApi.SavedGame

## Summary

| Enumerations | |
| --- | --- |
| `ConflictResolutionStrategy{   UseLongestPlaytime,   UseOriginal,   UseUnmerged,   UseManual,   UseLastKnownGood,   UseMostRecentlySaved }` | enum An enum for the different strategies that can be used to resolve saved game conflicts (i.e. |
| `SavedGameRequestStatus{   TimeoutError = -1,   InternalError = -2,   AuthenticationError = -3,   BadInputError = -4 }` | enum An enum for the different statuses that can be returned by the saved game client. |
| `SelectUIStatus{   SavedGameSelected = 1,   UserClosedUI = 2,   InternalError = -1,   TimeoutError = -2,   AuthenticationError = -3,   BadInputError = -4 }` | enum An enum for the different UI statuses that can be returned by the saved game client. |

| Functions | |
| --- | --- |
| `ConflictCallback(IConflictResolver resolver, ISavedGameMetadata original, byte[] originalData, ISavedGameMetadata unmerged, byte[] unmergedData)` | `delegate void`  A delegate that is invoked when we encounter a conflict during execution of [ISavedGameClient.OpenWithAutomaticConflictResolution](/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-saved-game-client#interface_google_play_games_1_1_basic_api_1_1_saved_game_1_1_i_saved_game_client_1ae90da5dda5a18768926a3eb70bd17c9f). |

| Structs | |
| --- | --- |
| [GooglePlayGames.BasicApi.SavedGame.SavedGameMetadataUpdate](/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update) | A struct representing the mutation of saved game metadata. |

| Interfaces | |
| --- | --- |
| [GooglePlayGames.BasicApi.SavedGame.IConflictResolver](/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-conflict-resolver) | An interface that allows developers to resolve metadata conflicts that may be encountered while opening saved games. |
| [GooglePlayGames.BasicApi.SavedGame.ISavedGameClient](/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-saved-game-client) | The main entry point for interacting with saved games. |
| [GooglePlayGames.BasicApi.SavedGame.ISavedGameMetadata](/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-saved-game-metadata) | Interface representing the metadata for a saved game. |

## Enumerations

### ConflictResolutionStrategy

```
 ConflictResolutionStrategy
```

An enum for the different strategies that can be used to resolve saved game conflicts (i.e.

conflicts produced by two or more separate writes to the same saved game at once).

| Properties | |
| --- | --- |
| `UseLastKnownGood` | The use last known good snapshot to resolve conflicts automatically. |
| `UseLongestPlaytime` | Choose which saved game should be used on the basis of which one has the longest recorded play time.  In other words, in the case of a conflicting write, the saved game with the longest play time will be considered cannonical. If play time has not been provided by the developer, or in the case of two saved games with equal play times, [UseOriginal](/games/services/unity/v2/api/namespace/google-play-games/basic-api/saved-game#namespace_google_play_games_1_1_basic_api_1_1_saved_game_1aaa9aaacffc574c503e5c6ed30b9da6e4aa206b51e4d573017d23e73ffaafe56bc) will be used instead. |
| `UseManual` | Manual resolution, no automatic resolution is attempted. |
| `UseMostRecentlySaved` | The use most recently saved snapshot to resolve conflicts automatically. |
| `UseOriginal` | Choose the version of the saved game that existed before any conflicting write occurred.  Consider the following case:  * An initial version of a save game ("X") is written from a device ("Dev\_A") * The save game X is downloaded by another device ("Dev\_B"). * Dev\_A writes a new version of the save game to the cloud ("Y") * Dev\_B does not see the new save game Y, and attempts to write a new save game ("Z"). * Since Dev\_B is performing a write using out of date information, a conflict is generated.  In this situation, we can resolve the conflict by declaring either keeping Y as the canonical version of the saved game (i.e. choose "original" aka [UseOriginal](/games/services/unity/v2/api/namespace/google-play-games/basic-api/saved-game#namespace_google_play_games_1_1_basic_api_1_1_saved_game_1aaa9aaacffc574c503e5c6ed30b9da6e4aa206b51e4d573017d23e73ffaafe56bc)), or by overwriting it with conflicting value, Z (i.e. choose "unmerged" aka [UseUnmerged](/games/services/unity/v2/api/namespace/google-play-games/basic-api/saved-game#namespace_google_play_games_1_1_basic_api_1_1_saved_game_1aaa9aaacffc574c503e5c6ed30b9da6e4a1a212ed8a6522ad73399c3c991d4c03e)). |
| `UseUnmerged` | See the documentation for [UseOriginal](/games/services/unity/v2/api/namespace/google-play-games/basic-api/saved-game#namespace_google_play_games_1_1_basic_api_1_1_saved_game_1aaa9aaacffc574c503e5c6ed30b9da6e4aa206b51e4d573017d23e73ffaafe56bc) |

### SavedGameRequestStatus

```
 SavedGameRequestStatus
```

An enum for the different statuses that can be returned by the saved game client.

| Properties | |
| --- | --- |
| `AuthenticationError` | A error related to authentication.  This is probably due to the user being signed out before the request could be issued. |
| `BadInputError` | The request failed because it was given bad input (e.g.  a filename with 200 characters). |
| `InternalError` | An unexpected internal error.  Check the log for error messages. |
| `TimeoutError` | The request failed due to a timeout. |

### SelectUIStatus

```
 SelectUIStatus
```

An enum for the different UI statuses that can be returned by the saved game client.

| Properties | |
| --- | --- |
| `AuthenticationError` | An error related to authentication.  This error could be due to the user being signed out before the request could be issued. |
| `BadInputError` | The request failed due to invalid input.  For example, the filename exceeded the 200 character limit.. |
| `InternalError` | An unexpected internal error.  Check the log for error messages. |
| `SavedGameSelected` | The user selected a saved game. |
| `TimeoutError` | There was a timeout while displaying the UI. |
| `UserClosedUI` | The user closed the UI without selecting a saved game. |

## Functions

### ConflictCallback

```
delegate void ConflictCallback(
  IConflictResolver resolver,
  ISavedGameMetadata original,
  byte[] originalData,
  ISavedGameMetadata unmerged,
  byte[] unmergedData
)
```

A delegate that is invoked when we encounter a conflict during execution of [ISavedGameClient.OpenWithAutomaticConflictResolution](/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-saved-game-client#interface_google_play_games_1_1_basic_api_1_1_saved_game_1_1_i_saved_game_client_1ae90da5dda5a18768926a3eb70bd17c9f).

The caller must resolve the conflict using the passed [IConflictResolver](/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-conflict-resolver#interface_google_play_games_1_1_basic_api_1_1_saved_game_1_1_i_conflict_resolver). All passed metadata is open. If [ISavedGameClient.OpenWithAutomaticConflictResolution](/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-saved-game-client#interface_google_play_games_1_1_basic_api_1_1_saved_game_1_1_i_saved_game_client_1ae90da5dda5a18768926a3eb70bd17c9f) was invoked with `prefetchDataOnConflict` set to `true`, the *originalData* and *unmergedData* will be equal to the binary data of the "original" and "unmerged" saved game respectively (and null otherwise). Since conflict files may be generated by other clients, it is possible that neither of the passed saved games were originally written by the current device. Consequently, any conflict resolution strategy should not rely on local data that is not part of the binary data of the passed saved games - this data will not be present if conflict resolution occurs on a different device. In addition, since a given saved game may have multiple conflicts, this callback must be designed to handle multiple invocations.