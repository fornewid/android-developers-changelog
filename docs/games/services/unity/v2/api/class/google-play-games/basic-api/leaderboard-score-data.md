---
title: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/leaderboard-score-data
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/leaderboard-score-data
source: md.txt
---

# GooglePlayGames.BasicApi.LeaderboardScoreData Class Reference

# GooglePlayGames.BasicApi.LeaderboardScoreData

Leaderboard score data.

## Summary

This is the callback data when loading leaderboard scores. There are several SDK API calls needed to be made to collect all the required data, so this class is used to simplify the response.

|                                                                                                                                                                                                                                            ### Properties                                                                                                                                                                                                                                            ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ApproximateCount](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/leaderboard-score-data#class_google_play_games_1_1_basic_api_1_1_leaderboard_score_data_1a22e39433461f65361454259749245f23) | `ulong` Gets or sets the approximate count of scores in the leaderboard.                                                                                                                                                                                 |
| [Id](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/leaderboard-score-data#class_google_play_games_1_1_basic_api_1_1_leaderboard_score_data_1a69e8bcc9e5e9dadf7332b98def5be4c5)               | `string` Gets or sets the unique identifier of the leaderboard.                                                                                                                                                                                          |
| [NextPageToken](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/leaderboard-score-data#class_google_play_games_1_1_basic_api_1_1_leaderboard_score_data_1ad5ffb17923a2a32df7079a5b3e479490)    | [ScorePageToken](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/score-page-token#class_google_play_games_1_1_basic_api_1_1_score_page_token) Gets or sets the token for the next page of scores.            |
| [PlayerScore](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/leaderboard-score-data#class_google_play_games_1_1_basic_api_1_1_leaderboard_score_data_1a1ae2e9d33131efb1f941a72924053475)      | `IScore` Gets or sets the player's score in the leaderboard.                                                                                                                                                                                             |
| [PrevPageToken](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/leaderboard-score-data#class_google_play_games_1_1_basic_api_1_1_leaderboard_score_data_1a524bcd556159e132edf8d47d46ee86f4)    | [ScorePageToken](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/score-page-token#class_google_play_games_1_1_basic_api_1_1_score_page_token) Gets or sets the token for the previous page of scores.        |
| [Scores](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/leaderboard-score-data#class_google_play_games_1_1_basic_api_1_1_leaderboard_score_data_1a62488970b6531faf907113f24df60cb7)           | `IScore[]` Gets an array of the scores in the leaderboard.                                                                                                                                                                                               |
| [Status](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/leaderboard-score-data#class_google_play_games_1_1_basic_api_1_1_leaderboard_score_data_1a7f2d5bd39f97821a194f448084337c57)           | [ResponseStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1afc173c0f78ea77552386c8f699526dea) Gets or sets the status of the leaderboard data response. |
| [Title](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/leaderboard-score-data#class_google_play_games_1_1_basic_api_1_1_leaderboard_score_data_1a833d636f7549b0bc1e651d23c5a21f55)            | `string` Gets or sets the title of the leaderboard.                                                                                                                                                                                                      |
| [Valid](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/leaderboard-score-data#class_google_play_games_1_1_basic_api_1_1_leaderboard_score_data_1a57b3a848e5ed55d657543afd3a0a27ae)            | `bool` Gets a value indicating whether the leaderboard data is valid.                                                                                                                                                                                    |

|                                                                                                                                                   ### Public functions                                                                                                                                                   ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [ToString](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/leaderboard-score-data#class_google_play_games_1_1_basic_api_1_1_leaderboard_score_data_1a5bcfc2e3a64bb70692c71c067629e63f)`()` | `override string` Returns a string representation of the leaderboard score data. |

## Properties

### ApproximateCount

```c#
ulong ApproximateCount
```  
Gets or sets the approximate count of scores in the leaderboard.  

### Id

```c#
string Id
```  
Gets or sets the unique identifier of the leaderboard.  

### NextPageToken

```c#
ScorePageToken NextPageToken
```  
Gets or sets the token for the next page of scores.  

### PlayerScore

```c#
IScore PlayerScore
```  
Gets or sets the player's score in the leaderboard.  

### PrevPageToken

```c#
ScorePageToken PrevPageToken
```  
Gets or sets the token for the previous page of scores.  

### Scores

```c#
IScore[] Scores
```  
Gets an array of the scores in the leaderboard.  

### Status

```c#
ResponseStatus Status
```  
Gets or sets the status of the leaderboard data response.  

### Title

```c#
string Title
```  
Gets or sets the title of the leaderboard.  

### Valid

```c#
bool Valid
```  
Gets a value indicating whether the leaderboard data is valid.

## Public functions

### ToString

```c#
override string ToString()
```  
Returns a string representation of the leaderboard score data.

<br />

|                          Details                          ||
|-------------|----------------------------------------------|
| **Returns** | A string that represents the current object. |