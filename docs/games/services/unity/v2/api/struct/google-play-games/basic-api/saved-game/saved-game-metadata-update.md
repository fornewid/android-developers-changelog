---
title: https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update
url: https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update
source: md.txt
---

# GooglePlayGames.BasicApi.SavedGame.SavedGameMetadataUpdate Struct Reference

# GooglePlayGames.BasicApi.SavedGame.SavedGameMetadataUpdate

A struct representing the mutation of saved game metadata.

## Summary

Fields can either have a new value or be untouched (in which case the corresponding field in the saved game metadata will be untouched). Instances must be built using[SavedGameMetadataUpdate.Builder](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update/builder#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update_1_1_builder)and once created, these instances are immutable and threadsafe.

|                                                                                                                                                                            ### Properties                                                                                                                                                                             ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [IsCoverImageUpdated](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update_1ad5ddd9143a1fb3ecbd25c56d36e214c3)  | `bool` Gets whether the cover image has been updated in the metadata.             |
| [IsDescriptionUpdated](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update_1ae274f71aad12e19188662829363cb124) | `bool` Gets whether the description has been updated in the metadata.             |
| [IsPlayedTimeUpdated](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update_1aee1f647b792f96df8792645626432067)  | `bool` Gets whether the played time has been updated in the metadata.             |
| [UpdatedDescription](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update_1abfb9c2685b0f0532a2962455c77198b2)   | `string` Gets the updated description for the saved game, if it has been changed. |
| [UpdatedPlayedTime](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update_1a00f74abaf52d18aa844104dc6912cc19)    | `TimeSpan` Gets the updated played time, if it has been changed.                  |
| [UpdatedPngCoverImage](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update_1a8cb1e52bd352883f8874677baf8fd20c) | `byte[]` Gets the updated PNG cover image, if it has been changed.                |

|                                                                                                                                                                                                                                                 ### Structs                                                                                                                                                                                                                                                  ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GooglePlayGames.BasicApi.SavedGame.SavedGameMetadataUpdate.Builder](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update/builder) | A builder for constructing instances of[SavedGameMetadataUpdate](https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update). |

## Properties

### IsCoverImageUpdated

```c#
bool GooglePlayGames::BasicApi::SavedGame::SavedGameMetadataUpdate::IsCoverImageUpdated
```  
Gets whether the cover image has been updated in the metadata.  

### IsDescriptionUpdated

```c#
bool GooglePlayGames::BasicApi::SavedGame::SavedGameMetadataUpdate::IsDescriptionUpdated
```  
Gets whether the description has been updated in the metadata.  

### IsPlayedTimeUpdated

```c#
bool GooglePlayGames::BasicApi::SavedGame::SavedGameMetadataUpdate::IsPlayedTimeUpdated
```  
Gets whether the played time has been updated in the metadata.  

### UpdatedDescription

```c#
string GooglePlayGames::BasicApi::SavedGame::SavedGameMetadataUpdate::UpdatedDescription
```  
Gets the updated description for the saved game, if it has been changed.  

### UpdatedPlayedTime

```c#
TimeSpan GooglePlayGames::BasicApi::SavedGame::SavedGameMetadataUpdate::UpdatedPlayedTime
```  
Gets the updated played time, if it has been changed.  

### UpdatedPngCoverImage

```c#
byte[] GooglePlayGames::BasicApi::SavedGame::SavedGameMetadataUpdate::UpdatedPngCoverImage
```  
Gets the updated PNG cover image, if it has been changed.