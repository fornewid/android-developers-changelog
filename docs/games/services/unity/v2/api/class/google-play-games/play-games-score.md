---
title: GooglePlayGames.PlayGamesScore Class Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-score
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# GooglePlayGames.PlayGamesScore

Represents a score on a Google Play Games leaderboard.

## Summary

Implements the Unity `IScore` interface.

### Inheritance

Inherits from: IScore

| Properties | |
| --- | --- |
| `date` | `DateTime`  Gets the date and time this score was achieved. |
| `formattedValue` | `string`  Gets the score value as a formatted string. |
| `leaderboardID` | `string`  Gets or sets the ID of the leaderboard this score is for. |
| `metaData` | `string`  Gets the metadata associated with this score (also known as a score tag). |
| `rank` | `int`  Gets the rank of this score in the leaderboard. |
| `userID` | `string`  Gets the ID of the user who achieved this score. |
| `value` | `long`  Gets or sets the score value. |

| Public functions | |
| --- | --- |
| `ReportScore(Action< bool > callback)` | `void`  Reports this score to the Google Play Games services. |

## Properties

### date

```
DateTime date
```

Gets the date and time this score was achieved.

### formattedValue

```
string formattedValue
```

Gets the score value as a formatted string.

### leaderboardID

```
string leaderboardID
```

Gets or sets the ID of the leaderboard this score is for.

### metaData

```
string metaData
```

Gets the metadata associated with this score (also known as a score tag).

### rank

```
int rank
```

Gets the rank of this score in the leaderboard.

### userID

```
string userID
```

Gets the ID of the user who achieved this score.

### value

```
long value
```

Gets or sets the score value.

## Public functions

### ReportScore

```
void ReportScore(
  Action< bool > callback
)
```

Reports this score to the Google Play Games services.

This is equivalent to calling [PlayGamesPlatform.ReportScore](/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a9a51e50e3de344ec7c896d89ca600b1d).

Details | || Parameters | |  |  | | --- | --- | | `callback` | A callback to be invoked with a boolean indicating the success of the operation. | |