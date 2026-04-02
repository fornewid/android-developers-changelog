---
title: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-score
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-score
source: md.txt
---

# GooglePlayGames.PlayGamesScore Class Reference

# GooglePlayGames.PlayGamesScore

Represents a score on a Google Play Games leaderboard.

## Summary

Implements the Unity`IScore`interface.

### Inheritance

Inherits from: IScore

|                                                                                                                                      ### Properties                                                                                                                                      ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [date](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-score#class_google_play_games_1_1_play_games_score_1af911623bfd163f919819beac7610e01a)           | `DateTime` Gets the date and time this score was achieved.                         |
| [formattedValue](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-score#class_google_play_games_1_1_play_games_score_1a5d1e7e39d12533da12621368180be33e) | `string` Gets the score value as a formatted string.                               |
| [leaderboardID](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-score#class_google_play_games_1_1_play_games_score_1aed8e96577d94e857540c0d4eda4c089f)  | `string` Gets or sets the ID of the leaderboard this score is for.                 |
| [metaData](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-score#class_google_play_games_1_1_play_games_score_1a100ef41cbb61d778dcdb67539d5e0424)       | `string` Gets the metadata associated with this score (also known as a score tag). |
| [rank](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-score#class_google_play_games_1_1_play_games_score_1a286fc07d22d2abda846421d17597825a)           | `int` Gets the rank of this score in the leaderboard.                              |
| [userID](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-score#class_google_play_games_1_1_play_games_score_1ac40ac391c61e9f41e7a20557c3c9963f)         | `string` Gets the ID of the user who achieved this score.                          |
| [value](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-score#class_google_play_games_1_1_play_games_score_1a1044600e530e02458627df717528c107)          | `long` Gets or sets the score value.                                               |

|                                                                                                                                    ### Public functions                                                                                                                                    ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| [ReportScore](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-score#class_google_play_games_1_1_play_games_score_1a2848d7c555e8e78bcf7de42b2b255560)`(Action< bool > callback)` | `void` Reports this score to the Google Play Games services. |

## Properties

### date

```c#
DateTime date
```  
Gets the date and time this score was achieved.  

### formattedValue

```c#
string formattedValue
```  
Gets the score value as a formatted string.  

### leaderboardID

```c#
string leaderboardID
```  
Gets or sets the ID of the leaderboard this score is for.  

### metaData

```c#
string metaData
```  
Gets the metadata associated with this score (also known as a score tag).  

### rank

```c#
int rank
```  
Gets the rank of this score in the leaderboard.  

### userID

```c#
string userID
```  
Gets the ID of the user who achieved this score.  

### value

```c#
long value
```  
Gets or sets the score value.

## Public functions

### ReportScore

```c#
void ReportScore(
  Action< bool > callback
)
```  
Reports this score to the Google Play Games services.

This is equivalent to calling[PlayGamesPlatform.ReportScore](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a9a51e50e3de344ec7c896d89ca600b1d).

<br />

|                                                                                                     Details                                                                                                     ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|----------------------------------------------------------------------------------| | `callback` | A callback to be invoked with a boolean indicating the success of the operation. | |