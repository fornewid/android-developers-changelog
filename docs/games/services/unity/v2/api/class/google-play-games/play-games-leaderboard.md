---
title: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-leaderboard
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-leaderboard
source: md.txt
---

# GooglePlayGames.PlayGamesLeaderboard

Represents a Google Play Games leaderboard.

## Summary

The class provides a way to configure and store data for a specific leaderboard. Implements Unity's generic `ILeaderboard` interface.

### Inheritance

Inherits from: ILeaderboard

| ### Constructors and Destructors ||
|---|---|
| [PlayGamesLeaderboard](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-leaderboard#class_google_play_games_1_1_play_games_leaderboard_1a53c739109490d79593d3570fa64325b8)`(string id)` Initializes a new instance of the [PlayGamesLeaderboard](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-leaderboard#class_google_play_games_1_1_play_games_leaderboard) class. ||

| ### Properties ||
|---|---|
| [ScoreCount](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-leaderboard#class_google_play_games_1_1_play_games_leaderboard_1ad64d9c13ce47230bb948baf56c2d2f74) | `int` Gets the number of scores currently loaded. |
| [id](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-leaderboard#class_google_play_games_1_1_play_games_leaderboard_1a60647b76c5b1512e9e5508cd0f585474) | `string` Gets or sets the leaderboard ID. |
| [loading](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-leaderboard#class_google_play_games_1_1_play_games_leaderboard_1a70122280028fd8ef12996d7255bc5173) | `bool` Gets a value indicating whether the leaderboard scores are currently loading. |
| [localUserScore](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-leaderboard#class_google_play_games_1_1_play_games_leaderboard_1a598ac74d7a1c60c9ab42a8eace6a36f4) | `IScore` Gets the local user's score on this leaderboard. |
| [maxRange](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-leaderboard#class_google_play_games_1_1_play_games_leaderboard_1a1c1eb6071f7032bf169f4d192200e72a) | `uint` Gets the approximate number of total scores in the leaderboard. |
| [range](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-leaderboard#class_google_play_games_1_1_play_games_leaderboard_1af14eb81a2dafc0b8f5e81641e2f33637) | `Range` Gets or sets the rank range for the scores to be loaded. |
| [scores](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-leaderboard#class_google_play_games_1_1_play_games_leaderboard_1a880e8d9618d05ea437c0fee26a882423) | `IScore[]` Gets the array of loaded scores. |
| [timeScope](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-leaderboard#class_google_play_games_1_1_play_games_leaderboard_1abe5ff4265350e20fd55551cf66ebf4b7) | `TimeScope` Gets or sets the time scope for the scores to be loaded. |
| [title](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-leaderboard#class_google_play_games_1_1_play_games_leaderboard_1a4c9c7aaae26fd69b97bb09a7625e6eaa) | `string` Gets the title of the leaderboard. |
| [userScope](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-leaderboard#class_google_play_games_1_1_play_games_leaderboard_1aa7f3c830cba20836ad8e300fc93552ed) | `UserScope` Gets or sets the user scope for the scores to be loaded. |

| ### Public functions ||
|---|---|
| [LoadScores](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-leaderboard#class_google_play_games_1_1_play_games_leaderboard_1abb667a61a32de4ce314a41130b92786f)`(System.Action< bool > callback)` | `void` Initiates the loading of scores from the Google Play Games platform. |
| [SetUserFilter](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-leaderboard#class_google_play_games_1_1_play_games_leaderboard_1aa85c25944650dda81b203c38c953b8ca)`(string[] userIDs)` | `void` Sets a filter to load scores only for a specific set of users. |

## Properties

### ScoreCount

```c#
int ScoreCount
```  
Gets the number of scores currently loaded.

The score count.  

### id

```c#
string id
```  
Gets or sets the leaderboard ID.

The leaderboard ID.  

### loading

```c#
bool loading
```  
Gets a value indicating whether the leaderboard scores are currently loading.

`true` if loading; otherwise, `false`.  

### localUserScore

```c#
IScore localUserScore
```  
Gets the local user's score on this leaderboard.

The local user's score.  

### maxRange

```c#
uint maxRange
```  
Gets the approximate number of total scores in the leaderboard.

The maximum range of scores.  

### range

```c#
Range range
```  
Gets or sets the rank range for the scores to be loaded.

The rank range.  

### scores

```c#
IScore[] scores
```  
Gets the array of loaded scores.

The scores.  

### timeScope

```c#
TimeScope timeScope
```  
Gets or sets the time scope for the scores to be loaded.

The time scope.  

### title

```c#
string title
```  
Gets the title of the leaderboard.

The title.  

### userScope

```c#
UserScope userScope
```  
Gets or sets the user scope for the scores to be loaded.

The user scope.

## Public functions

### LoadScores

```c#
void LoadScores(
  System.Action< bool > callback
)
```  
Initiates the loading of scores from the Google Play Games platform.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `callback` | A callback that will be invoked with a boolean indicating the success of the operation. | |

### PlayGamesLeaderboard

```c#
 PlayGamesLeaderboard(
  string id
)
```  
Initializes a new instance of the [PlayGamesLeaderboard](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-leaderboard#class_google_play_games_1_1_play_games_leaderboard) class.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `id` | The leaderboard ID. | |

### SetUserFilter

```c#
void SetUserFilter(
  string[] userIDs
)
```  
Sets a filter to load scores only for a specific set of users.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `userIDs` | The array of user IDs to filter by. | |