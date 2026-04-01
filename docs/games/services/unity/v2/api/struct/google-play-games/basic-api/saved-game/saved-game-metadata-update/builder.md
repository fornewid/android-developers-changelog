---
title: https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update/builder
url: https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update/builder
source: md.txt
---

# GooglePlayGames.BasicApi.SavedGame.SavedGameMetadataUpdate.Builder Struct Reference

# GooglePlayGames.BasicApi.SavedGame.SavedGameMetadataUpdate.Builder

A builder for constructing instances of[SavedGameMetadataUpdate](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update).

## Summary

|                                                                                                                                                                                                                                                                                                                                                                                                                                     ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                                      ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Build](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update/builder#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update_1_1_builder_1a3f15a9ddf2da2741bf67b89ec3263313)`()`                                           | [SavedGameMetadataUpdate](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update) Builds a new[SavedGameMetadataUpdate](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update)instance with the configured updates. |
| [WithUpdatedDescription](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update/builder#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update_1_1_builder_1aaccf5270e93c9a1abda476150848e0f4)`(string description)`        | [Builder](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update/builder#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update_1_1_builder) Sets the description to be updated in the saved game metadata.                                                                                                                                                                                                                                  |
| [WithUpdatedPlayedTime](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update/builder#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update_1_1_builder_1a41181b5ef671236ff58dcbac8281a442)`(TimeSpan newPlayedTime)`     | [Builder](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update/builder#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update_1_1_builder) Sets the played time to be updated in the saved game metadata.                                                                                                                                                                                                                                  |
| [WithUpdatedPngCoverImage](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update/builder#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update_1_1_builder_1ab3184b724289eda5e079b7a1bad6e1f0)`(byte[] newPngCoverImage)` | [Builder](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update/builder#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update_1_1_builder) Sets the PNG cover image to be updated in the saved game metadata.                                                                                                                                                                                                                              |

## Public functions

### Build

```c#
SavedGameMetadataUpdate GooglePlayGames::BasicApi::SavedGame::SavedGameMetadataUpdate::Builder::Build()
```  
Builds a new[SavedGameMetadataUpdate](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update)instance with the configured updates.

<br />

|                                                                                                                                      Details                                                                                                                                      ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A new instance of[SavedGameMetadataUpdate](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update). |

### WithUpdatedDescription

```c#
Builder GooglePlayGames::BasicApi::SavedGame::SavedGameMetadataUpdate::Builder::WithUpdatedDescription(
  string description
)
```  
Sets the description to be updated in the saved game metadata.

<br />

|                                                   Details                                                    ||
|-------------|-------------------------------------------------------------------------------------------------|
| Parameters  | |---------------|-----------------------------| | `description` | The new description to set. | |
| **Returns** | The builder with the updated description.                                                       |

### WithUpdatedPlayedTime

```c#
Builder GooglePlayGames::BasicApi::SavedGame::SavedGameMetadataUpdate::Builder::WithUpdatedPlayedTime(
  TimeSpan newPlayedTime
)
```  
Sets the played time to be updated in the saved game metadata.

<br />

|                                                                                                  Details                                                                                                   ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-----------------|-----------------------------| | `newPlayedTime` | The new played time to set. |                                                                                           |
| Exceptions  | |-----------------------------|--------------------------------------------------------------| | `InvalidOperationException` | Thrown if the played time exceeds the maximum allowed value. | |
| **Returns** | The builder with the updated played time.                                                                                                                                                     |

### WithUpdatedPngCoverImage

```c#
Builder GooglePlayGames::BasicApi::SavedGame::SavedGameMetadataUpdate::Builder::WithUpdatedPngCoverImage(
  byte[] newPngCoverImage
)
```  
Sets the PNG cover image to be updated in the saved game metadata.

<br />

|                                                                        Details                                                                         ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------------------|---------------------------------------------| | `newPngCoverImage` | The new PNG image data for the cover image. | |
| **Returns** | The builder with the updated cover image.                                                                                                 |