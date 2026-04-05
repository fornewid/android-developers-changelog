---
title: GooglePlayGames.BasicApi.LeaderboardScoreData Class Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/leaderboard-score-data
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# GooglePlayGames.BasicApi.LeaderboardScoreData

Leaderboard score data.

## Summary

This is the callback data when loading leaderboard scores. There are several SDK API calls needed to be made to collect all the required data, so this class is used to simplify the response.

| Properties | |
| --- | --- |
| `ApproximateCount` | `ulong`  Gets or sets the approximate count of scores in the leaderboard. |
| `Id` | `string`  Gets or sets the unique identifier of the leaderboard. |
| `NextPageToken` | `ScorePageToken`  Gets or sets the token for the next page of scores. |
| `PlayerScore` | `IScore`  Gets or sets the player's score in the leaderboard. |
| `PrevPageToken` | `ScorePageToken`  Gets or sets the token for the previous page of scores. |
| `Scores` | `IScore[]`  Gets an array of the scores in the leaderboard. |
| `Status` | `ResponseStatus`  Gets or sets the status of the leaderboard data response. |
| `Title` | `string`  Gets or sets the title of the leaderboard. |
| `Valid` | `bool`  Gets a value indicating whether the leaderboard data is valid. |

| Public functions | |
| --- | --- |
| `ToString()` | `override string`  Returns a string representation of the leaderboard score data. |

## Properties

### ApproximateCount

```
ulong ApproximateCount
```

Gets or sets the approximate count of scores in the leaderboard.

### Id

```
string Id
```

Gets or sets the unique identifier of the leaderboard.

### NextPageToken

```
ScorePageToken NextPageToken
```

Gets or sets the token for the next page of scores.

### PlayerScore

```
IScore PlayerScore
```

Gets or sets the player's score in the leaderboard.

### PrevPageToken

```
ScorePageToken PrevPageToken
```

Gets or sets the token for the previous page of scores.

### Scores

```
IScore[] Scores
```

Gets an array of the scores in the leaderboard.

### Status

```
ResponseStatus Status
```

Gets or sets the status of the leaderboard data response.

### Title

```
string Title
```

Gets or sets the title of the leaderboard.

### Valid

```
bool Valid
```

Gets a value indicating whether the leaderboard data is valid.

## Public functions

### ToString

```
override string ToString()
```

Returns a string representation of the leaderboard score data.

Details | || **Returns** | A string that represents the current object. |