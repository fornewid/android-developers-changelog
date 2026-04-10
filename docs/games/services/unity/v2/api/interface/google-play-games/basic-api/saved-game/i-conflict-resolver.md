---
title: https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-conflict-resolver
url: https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-conflict-resolver
source: md.txt
---

# GooglePlayGames.BasicApi.SavedGame.IConflictResolver Interface Reference

# GooglePlayGames.BasicApi.SavedGame.IConflictResolver

An interface that allows developers to resolve metadata conflicts that may be encountered while opening saved games.

## Summary

|                                                                                                                                                                                                                                                                                                                                                                                                                                            ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                                             ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [ChooseMetadata](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-conflict-resolver#interface_google_play_games_1_1_basic_api_1_1_saved_game_1_1_i_conflict_resolver_1af9d8ede0686c12c429468522120ea1a7)`(`[ISavedGameMetadata](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-saved-game-metadata#interface_google_play_games_1_1_basic_api_1_1_saved_game_1_1_i_saved_game_metadata)` chosenMetadata)`                                                                                                                                                                                                                                                                                           | `void` Resolves the conflict by choosing the passed metadata to be canonical. |
| [ResolveConflict](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-conflict-resolver#interface_google_play_games_1_1_basic_api_1_1_saved_game_1_1_i_conflict_resolver_1a992cd337b5a7ddb9cac39e7ca54bb5ff)`(`[ISavedGameMetadata](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-saved-game-metadata#interface_google_play_games_1_1_basic_api_1_1_saved_game_1_1_i_saved_game_metadata)` chosenMetadata, `[SavedGameMetadataUpdate](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update)` metadataUpdate, byte[] updatedData)` | `void` Resolves the conflict and updates the data.                            |

## Public functions

### ChooseMetadata

```c#
void ChooseMetadata(
  ISavedGameMetadata chosenMetadata
)
```  
Resolves the conflict by choosing the passed metadata to be canonical.

The passed metadata must be one of the two instances passed as parameters into[ConflictCallback](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api/saved-game#namespace_google_play_games_1_1_basic_api_1_1_saved_game_1a788cd50d6c6a4d82d3eef9b51fbd246a)- this instance will be kept as the cannonical value in the cloud.

<br />

|                                                                                                                                                                                                                                                                    Details                                                                                                                                                                                                                                                                    ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `chosenMetadata` | The chosen metadata. This metadata must be open. If it is not open, the invocation of NativeSavedGameClient.OpenWithManualConflictResolution that produced this ConflictResolver will immediately fail with SelectUIStatus.BadInputError. | |

### ResolveConflict

```c#
void ResolveConflict(
  ISavedGameMetadata chosenMetadata,
  SavedGameMetadataUpdate metadataUpdate,
  byte[] updatedData
)
```  
Resolves the conflict and updates the data.

<br />

|                                                                                                                                                                                                                                                                                                   Details                                                                                                                                                                                                                                                                                                   ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------------|--------------------------------------------------------------------------------------------------------------------------| | `chosenMetadata` | Metadata for the chosen version. This is either the original or unmerged metadata provided when the callback is invoked. | | `metadataUpdate` | Metadata update, same as when committing changes.                                                                        | | `updatedData`    | Updated data to use when resolving the conflict.                                                                         | |