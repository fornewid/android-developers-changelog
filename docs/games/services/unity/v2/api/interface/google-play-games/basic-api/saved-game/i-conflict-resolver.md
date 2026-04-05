---
title: GooglePlayGames.BasicApi.SavedGame.IConflictResolver Interface Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-conflict-resolver
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# GooglePlayGames.BasicApi.SavedGame.IConflictResolver

An interface that allows developers to resolve metadata conflicts that may be encountered while opening saved games.

## Summary

| Public functions | |
| --- | --- |
| `ChooseMetadata(ISavedGameMetadata chosenMetadata)` | `void`  Resolves the conflict by choosing the passed metadata to be canonical. |
| `ResolveConflict(ISavedGameMetadata chosenMetadata, SavedGameMetadataUpdate metadataUpdate, byte[] updatedData)` | `void`  Resolves the conflict and updates the data. |

## Public functions

### ChooseMetadata

```
void ChooseMetadata(
  ISavedGameMetadata chosenMetadata
)
```

Resolves the conflict by choosing the passed metadata to be canonical.

The passed metadata must be one of the two instances passed as parameters into [ConflictCallback](/games/services/unity/v2/api/namespace/google-play-games/basic-api/saved-game#namespace_google_play_games_1_1_basic_api_1_1_saved_game_1a788cd50d6c6a4d82d3eef9b51fbd246a) - this instance will be kept as the cannonical value in the cloud.

Details | || Parameters | |  |  | | --- | --- | | `chosenMetadata` | The chosen metadata. This metadata must be open. If it is not open, the invocation of NativeSavedGameClient.OpenWithManualConflictResolution that produced this ConflictResolver will immediately fail with SelectUIStatus.BadInputError. | |

### ResolveConflict

```
void ResolveConflict(
  ISavedGameMetadata chosenMetadata,
  SavedGameMetadataUpdate metadataUpdate,
  byte[] updatedData
)
```

Resolves the conflict and updates the data.

Details | || Parameters | |  |  | | --- | --- | | `chosenMetadata` | Metadata for the chosen version. This is either the original or unmerged metadata provided when the callback is invoked. | | `metadataUpdate` | Metadata update, same as when committing changes. | | `updatedData` | Updated data to use when resolving the conflict. | |