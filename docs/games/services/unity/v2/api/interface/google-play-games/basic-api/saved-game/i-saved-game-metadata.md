---
title: GooglePlayGames.BasicApi.SavedGame.ISavedGameMetadata Interface Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-saved-game-metadata
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# GooglePlayGames.BasicApi.SavedGame.ISavedGameMetadata

Interface representing the metadata for a saved game.

## Summary

These instances are also used as handles for reading and writing the content of the underlying file.

| Properties | |
| --- | --- |
| `CoverImageURL` | `string`  A URL corresponding to the PNG-encoded image corresponding to this saved game. |
| `Description` | `string`  Returns a human-readable description of what the saved game contains. |
| `Filename` | `string`  Returns the filename for this saved game. |
| `IsOpen` | `bool`  Returns true if this metadata can be used for operations related to raw file data (i.e. |
| `LastModifiedTimestamp` | `DateTime`  A timestamp corresponding to the last modification to the underlying saved game. |
| `TotalTimePlayed` | `TimeSpan`  Returns the total time played by the player for this saved game. |

## Properties

### CoverImageURL

```
string CoverImageURL
```

A URL corresponding to the PNG-encoded image corresponding to this saved game.

null if the saved game does not have a cover image.

The cover image URL.

### Description

```
string Description
```

Returns a human-readable description of what the saved game contains.

This may be null.

The description.

### Filename

```
string Filename
```

Returns the filename for this saved game.

A saved game filename will only consist of non-URL reserved characters (i.e. a-z, A-Z, 0-9, or the symbols "-", ".", "\_", or "~") and will between 1 and 100 characters in length (inclusive).

The filename.

### IsOpen

```
bool IsOpen
```

Returns true if this metadata can be used for operations related to raw file data (i.e.

the binary data contained in the underlying file). Metadata returned by Open operations will be "Open". After an update to the file is committed or the metadata is used to resolve a conflict, the corresponding Metadata is closed, and IsOpen will return false.

`true` if this instance is open; otherwise, `false`.

### LastModifiedTimestamp

```
DateTime LastModifiedTimestamp
```

A timestamp corresponding to the last modification to the underlying saved game.

If the saved game is newly created, this value will correspond to the time the first Open occurred. Otherwise, this corresponds to time the last successful write occurred (either by CommitUpdate or Resolve methods).

The last modified timestamp.

### TotalTimePlayed

```
TimeSpan TotalTimePlayed
```

Returns the total time played by the player for this saved game.

This value is developer-specified and may be tracked in any way that is appropriate to the game. Note that this value is specific to this specific saved game (unless the developer intentionally sets the same value on all saved games). If the value was not set, this will be equal to `TimeSpan.FromMilliseconds(0)`

The total time played.