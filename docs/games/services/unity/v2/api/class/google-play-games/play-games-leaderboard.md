---
title: GooglePlayGames.PlayGamesLeaderboard Class Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-leaderboard
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# GooglePlayGames.PlayGamesLeaderboard

Represents a Google Play Games leaderboard.

## Summary

The class provides a way to configure and store data for a specific leaderboard. Implements Unity's generic `ILeaderboard` interface.

### Inheritance

Inherits from: ILeaderboard

| Constructors and Destructors | |
| --- | --- |
| `PlayGamesLeaderboard(string id)`   Initializes a new instance of the [PlayGamesLeaderboard](/games/services/unity/v2/api/class/google-play-games/play-games-leaderboard#class_google_play_games_1_1_play_games_leaderboard) class. | |

| Properties | |
| --- | --- |
| `ScoreCount` | `int`  Gets the number of scores currently loaded. |
| `id` | `string`  Gets or sets the leaderboard ID. |
| `loading` | `bool`  Gets a value indicating whether the leaderboard scores are currently loading. |
| `localUserScore` | `IScore`  Gets the local user's score on this leaderboard. |
| `maxRange` | `uint`  Gets the approximate number of total scores in the leaderboard. |
| `range` | `Range`  Gets or sets the rank range for the scores to be loaded. |
| `scores` | `IScore[]`  Gets the array of loaded scores. |
| `timeScope` | `TimeScope`  Gets or sets the time scope for the scores to be loaded. |
| `title` | `string`  Gets the title of the leaderboard. |
| `userScope` | `UserScope`  Gets or sets the user scope for the scores to be loaded. |

| Public functions | |
| --- | --- |
| `LoadScores(System.Action< bool > callback)` | `void`  Initiates the loading of scores from the Google Play Games platform. |
| `SetUserFilter(string[] userIDs)` | `void`  Sets a filter to load scores only for a specific set of users. |

## Properties

### ScoreCount

```
int ScoreCount
```

Gets the number of scores currently loaded.

The score count.

### id

```
string id
```

Gets or sets the leaderboard ID.

The leaderboard ID.

### loading

```
bool loading
```

Gets a value indicating whether the leaderboard scores are currently loading.

`true` if loading; otherwise, `false`.

### localUserScore

```
IScore localUserScore
```

Gets the local user's score on this leaderboard.

The local user's score.

### maxRange

```
uint maxRange
```

Gets the approximate number of total scores in the leaderboard.

The maximum range of scores.

### range

```
Range range
```

Gets or sets the rank range for the scores to be loaded.

The rank range.

### scores

```
IScore[] scores
```

Gets the array of loaded scores.

The scores.

### timeScope

```
TimeScope timeScope
```

Gets or sets the time scope for the scores to be loaded.

The time scope.

### title

```
string title
```

Gets the title of the leaderboard.

The title.

### userScope

```
UserScope userScope
```

Gets or sets the user scope for the scores to be loaded.

The user scope.

## Public functions

### LoadScores

```
void LoadScores(
  System.Action< bool > callback
)
```

Initiates the loading of scores from the Google Play Games platform.

Details | || Parameters | |  |  | | --- | --- | | `callback` | A callback that will be invoked with a boolean indicating the success of the operation. | |

### PlayGamesLeaderboard

```
 PlayGamesLeaderboard(
  string id
)
```

Initializes a new instance of the [PlayGamesLeaderboard](/games/services/unity/v2/api/class/google-play-games/play-games-leaderboard#class_google_play_games_1_1_play_games_leaderboard) class.

Details | || Parameters | |  |  | | --- | --- | | `id` | The leaderboard ID. | |

### SetUserFilter

```
void SetUserFilter(
  string[] userIDs
)
```

Sets a filter to load scores only for a specific set of users.

Details | || Parameters | |  |  | | --- | --- | | `userIDs` | The array of user IDs to filter by. | |