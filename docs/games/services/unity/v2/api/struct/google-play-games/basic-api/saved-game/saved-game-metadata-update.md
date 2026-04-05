---
title: GooglePlayGames.BasicApi.SavedGame.SavedGameMetadataUpdate Struct Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.




# GooglePlayGames.BasicApi.SavedGame.SavedGameMetadataUpdate

A struct representing the mutation of saved game metadata.

## Summary

Fields can either have a new value or be untouched (in which case the corresponding field in the saved game metadata will be untouched). Instances must be built using [SavedGameMetadataUpdate.Builder](/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update/builder#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update_1_1_builder) and once created, these instances are immutable and threadsafe.

| Properties | |
| --- | --- |
| `IsCoverImageUpdated` | `bool`  Gets whether the cover image has been updated in the metadata. |
| `IsDescriptionUpdated` | `bool`  Gets whether the description has been updated in the metadata. |
| `IsPlayedTimeUpdated` | `bool`  Gets whether the played time has been updated in the metadata. |
| `UpdatedDescription` | `string`  Gets the updated description for the saved game, if it has been changed. |
| `UpdatedPlayedTime` | `TimeSpan`  Gets the updated played time, if it has been changed. |
| `UpdatedPngCoverImage` | `byte[]`  Gets the updated PNG cover image, if it has been changed. |

| Structs | |
| --- | --- |
| [GooglePlayGames.BasicApi.SavedGame.SavedGameMetadataUpdate.Builder](/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update/builder) | A builder for constructing instances of [SavedGameMetadataUpdate](/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update). |

## Properties

### IsCoverImageUpdated

```
bool GooglePlayGames::BasicApi::SavedGame::SavedGameMetadataUpdate::IsCoverImageUpdated
```

Gets whether the cover image has been updated in the metadata.

### IsDescriptionUpdated

```
bool GooglePlayGames::BasicApi::SavedGame::SavedGameMetadataUpdate::IsDescriptionUpdated
```

Gets whether the description has been updated in the metadata.

### IsPlayedTimeUpdated

```
bool GooglePlayGames::BasicApi::SavedGame::SavedGameMetadataUpdate::IsPlayedTimeUpdated
```

Gets whether the played time has been updated in the metadata.

### UpdatedDescription

```
string GooglePlayGames::BasicApi::SavedGame::SavedGameMetadataUpdate::UpdatedDescription
```

Gets the updated description for the saved game, if it has been changed.

### UpdatedPlayedTime

```
TimeSpan GooglePlayGames::BasicApi::SavedGame::SavedGameMetadataUpdate::UpdatedPlayedTime
```

Gets the updated played time, if it has been changed.

### UpdatedPngCoverImage

```
byte[] GooglePlayGames::BasicApi::SavedGame::SavedGameMetadataUpdate::UpdatedPngCoverImage
```

Gets the updated PNG cover image, if it has been changed.