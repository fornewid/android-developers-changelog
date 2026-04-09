---
title: GooglePlayGames.BasicApi.Achievement Class Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/achievement
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.




# GooglePlayGames.BasicApi.Achievement

Data interface for retrieving achievement information.

## Summary

There are 3 states an achievement can be in:

Hidden - indicating the name and description of the achievement is not visible to the player.

Revealed - indicating the name and description of the achievement is visible to the player. Unlocked - indicating the player has unlocked, or achieved, the achievment.

Achievements has two types, standard which is unlocked in one step, and incremental, which require multiple steps to unlock.

| Constructors and Destructors | |
| --- | --- |
| `Achievement()` | |

| Properties | |
| --- | --- |
| `CurrentSteps` | `int`  The number of steps the user has gone towards unlocking this achievement. |
| `Description` | `string`  The description of this achievement. |
| `Id` | `string`  The ID string of this achievement. |
| `IsIncremental` | `bool`  Indicates whether this achievement is incremental. |
| `IsRevealed` | `bool`  Indicates whether the achievement is revealed or not (hidden). |
| `IsUnlocked` | `bool`  Indicates whether the achievement is unlocked or not. |
| `LastModifiedTime` | `DateTime`  The date and time the state of the achievement was modified. |
| `Name` | `string`  The name of this achievement. |
| `Points` | `ulong`  The number of experience points earned for unlocking this [Achievement](/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement). |
| `RevealedImageUrl` | `string`  The URL to the image to display when the achievement is revealed. |
| `TotalSteps` | `int`  The total number of steps needed to unlock this achievement. |
| `UnlockedImageUrl` | `string`  The URL to the image to display when the achievement is unlocked. |

| Public functions | |
| --- | --- |
| `ToString()` | `override string`  Returns a System.String that represents the current [GooglePlayGames.BasicApi.Achievement](/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement). |

## Properties

### CurrentSteps

```
int CurrentSteps
```

The number of steps the user has gone towards unlocking this achievement.

### Description

```
string Description
```

The description of this achievement.

### Id

```
string Id
```

The ID string of this achievement.

### IsIncremental

```
bool IsIncremental
```

Indicates whether this achievement is incremental.

### IsRevealed

```
bool IsRevealed
```

Indicates whether the achievement is revealed or not (hidden).

### IsUnlocked

```
bool IsUnlocked
```

Indicates whether the achievement is unlocked or not.

### LastModifiedTime

```
DateTime LastModifiedTime
```

The date and time the state of the achievement was modified.

The value is invalid (-1 long) if the achievement state has never been updated.

### Name

```
string Name
```

The name of this achievement.

### Points

```
ulong Points
```

The number of experience points earned for unlocking this [Achievement](/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement).

### RevealedImageUrl

```
string RevealedImageUrl
```

The URL to the image to display when the achievement is revealed.

### TotalSteps

```
int TotalSteps
```

The total number of steps needed to unlock this achievement.

### UnlockedImageUrl

```
string UnlockedImageUrl
```

The URL to the image to display when the achievement is unlocked.

## Public functions

### Achievement

```
 Achievement()
```

### ToString

```
override string ToString()
```

Returns a System.String that represents the current [GooglePlayGames.BasicApi.Achievement](/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement).

Details | || **Returns** | A System.String that represents the current [GooglePlayGames.BasicApi.Achievement](/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement). |