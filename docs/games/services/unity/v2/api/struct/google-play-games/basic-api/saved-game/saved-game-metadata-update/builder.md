---
title: GooglePlayGames.BasicApi.SavedGame.SavedGameMetadataUpdate.Builder Struct Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update/builder
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.




# GooglePlayGames.BasicApi.SavedGame.SavedGameMetadataUpdate.Builder

A builder for constructing instances of [SavedGameMetadataUpdate](/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update).

## Summary

| Public functions | |
| --- | --- |
| `Build()` | `SavedGameMetadataUpdate`  Builds a new [SavedGameMetadataUpdate](/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update) instance with the configured updates. |
| `WithUpdatedDescription(string description)` | `Builder`  Sets the description to be updated in the saved game metadata. |
| `WithUpdatedPlayedTime(TimeSpan newPlayedTime)` | `Builder`  Sets the played time to be updated in the saved game metadata. |
| `WithUpdatedPngCoverImage(byte[] newPngCoverImage)` | `Builder`  Sets the PNG cover image to be updated in the saved game metadata. |

## Public functions

### Build

```
SavedGameMetadataUpdate GooglePlayGames::BasicApi::SavedGame::SavedGameMetadataUpdate::Builder::Build()
```

Builds a new [SavedGameMetadataUpdate](/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update) instance with the configured updates.

Details | || **Returns** | A new instance of [SavedGameMetadataUpdate](/games/services/unity/v2/api/struct/google-play-games/basic-api/saved-game/saved-game-metadata-update#struct_google_play_games_1_1_basic_api_1_1_saved_game_1_1_saved_game_metadata_update). |

### WithUpdatedDescription

```
Builder GooglePlayGames::BasicApi::SavedGame::SavedGameMetadataUpdate::Builder::WithUpdatedDescription(
  string description
)
```

Sets the description to be updated in the saved game metadata.

Details | || Parameters | |  |  | | --- | --- | | `description` | The new description to set. | |
| **Returns** | The builder with the updated description. |

### WithUpdatedPlayedTime

```
Builder GooglePlayGames::BasicApi::SavedGame::SavedGameMetadataUpdate::Builder::WithUpdatedPlayedTime(
  TimeSpan newPlayedTime
)
```

Sets the played time to be updated in the saved game metadata.

Details | || Parameters | |  |  | | --- | --- | | `newPlayedTime` | The new played time to set. | |
| Exceptions | |  |  | | --- | --- | | `InvalidOperationException` | Thrown if the played time exceeds the maximum allowed value. | |
| **Returns** | The builder with the updated played time. |

### WithUpdatedPngCoverImage

```
Builder GooglePlayGames::BasicApi::SavedGame::SavedGameMetadataUpdate::Builder::WithUpdatedPngCoverImage(
  byte[] newPngCoverImage
)
```

Sets the PNG cover image to be updated in the saved game metadata.

Details | || Parameters | |  |  | | --- | --- | | `newPngCoverImage` | The new PNG image data for the cover image. | |
| **Returns** | The builder with the updated cover image. |