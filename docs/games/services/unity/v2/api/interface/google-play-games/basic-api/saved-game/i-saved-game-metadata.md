---
title: https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-saved-game-metadata
url: https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-saved-game-metadata
source: md.txt
---

# GooglePlayGames.BasicApi.SavedGame.ISavedGameMetadata Interface Reference

# GooglePlayGames.BasicApi.SavedGame.ISavedGameMetadata

Interface representing the metadata for a saved game.

## Summary

These instances are also used as handles for reading and writing the content of the underlying file.

|                                                                                                                                                                                 ### Properties                                                                                                                                                                                  ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [CoverImageURL](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-saved-game-metadata#interface_google_play_games_1_1_basic_api_1_1_saved_game_1_1_i_saved_game_metadata_1a582f4e061a570ae06830de1483eaf709)         | `string` A URL corresponding to the PNG-encoded image corresponding to this saved game.        |
| [Description](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-saved-game-metadata#interface_google_play_games_1_1_basic_api_1_1_saved_game_1_1_i_saved_game_metadata_1a31a06cb7611b2ab2771e9159467d0bae)           | `string` Returns a human-readable description of what the saved game contains.                 |
| [Filename](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-saved-game-metadata#interface_google_play_games_1_1_basic_api_1_1_saved_game_1_1_i_saved_game_metadata_1a1c604918b8d9451efd27262edb5886f7)              | `string` Returns the filename for this saved game.                                             |
| [IsOpen](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-saved-game-metadata#interface_google_play_games_1_1_basic_api_1_1_saved_game_1_1_i_saved_game_metadata_1ae203925fc56f0eb392727b47ea8d26f5)                | `bool` Returns true if this metadata can be used for operations related to raw file data (i.e. |
| [LastModifiedTimestamp](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-saved-game-metadata#interface_google_play_games_1_1_basic_api_1_1_saved_game_1_1_i_saved_game_metadata_1ac7b2b0cbb564e2c42e02095111671273) | `DateTime` A timestamp corresponding to the last modification to the underlying saved game.    |
| [TotalTimePlayed](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-saved-game-metadata#interface_google_play_games_1_1_basic_api_1_1_saved_game_1_1_i_saved_game_metadata_1aab87940b43f701129355e3668f812fe4)       | `TimeSpan` Returns the total time played by the player for this saved game.                    |

## Properties

### CoverImageURL

```c#
string CoverImageURL
```  
A URL corresponding to the PNG-encoded image corresponding to this saved game.

null if the saved game does not have a cover image.

The cover image URL.  

### Description

```c#
string Description
```  
Returns a human-readable description of what the saved game contains.

This may be null.

The description.  

### Filename

```c#
string Filename
```  
Returns the filename for this saved game.

A saved game filename will only consist of non-URL reserved characters (i.e. a-z, A-Z, 0-9, or the symbols "-", ".", "_", or "\~") and will between 1 and 100 characters in length (inclusive).

The filename.  

### IsOpen

```c#
bool IsOpen
```  
Returns true if this metadata can be used for operations related to raw file data (i.e.

the binary data contained in the underlying file). Metadata returned by Open operations will be "Open". After an update to the file is committed or the metadata is used to resolve a conflict, the corresponding Metadata is closed, and IsOpen will return false.

`true`if this instance is open; otherwise,`false`.  

### LastModifiedTimestamp

```c#
DateTime LastModifiedTimestamp
```  
A timestamp corresponding to the last modification to the underlying saved game.

If the saved game is newly created, this value will correspond to the time the first Open occurred. Otherwise, this corresponds to time the last successful write occurred (either by CommitUpdate or Resolve methods).

The last modified timestamp.  

### TotalTimePlayed

```c#
TimeSpan TotalTimePlayed
```  
Returns the total time played by the player for this saved game.

This value is developer-specified and may be tracked in any way that is appropriate to the game. Note that this value is specific to this specific saved game (unless the developer intentionally sets the same value on all saved games). If the value was not set, this will be equal to`TimeSpan.FromMilliseconds(0)`

The total time played.