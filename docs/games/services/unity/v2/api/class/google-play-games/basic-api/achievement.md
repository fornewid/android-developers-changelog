---
title: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/achievement
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/achievement
source: md.txt
---

# GooglePlayGames.BasicApi.Achievement Class Reference

# GooglePlayGames.BasicApi.Achievement

Data interface for retrieving achievement information.

## Summary

There are 3 states an achievement can be in:

Hidden - indicating the name and description of the achievement is not visible to the player.

Revealed - indicating the name and description of the achievement is visible to the player. Unlocked - indicating the player has unlocked, or achieved, the achievment.

Achievements has two types, standard which is unlocked in one step, and incremental, which require multiple steps to unlock.

| ### Constructors and Destructors ||
|---|---|
| [Achievement](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement_1a1193041cda991247f0486ad4029cfd0f)`()` ||

|                                                                                                                                                                                                                            ### Properties                                                                                                                                                                                                                            ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CurrentSteps](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement_1aea9db469548bd48be786748cd87aaad8)     | `int` The number of steps the user has gone towards unlocking this achievement.                                                                                                                                                                |
| [Description](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement_1a0f78cafc13451ddc8e2a29c7e801012c)      | `string` The description of this achievement.                                                                                                                                                                                                  |
| [Id](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement_1abf4691050479270c816ffff02713931a)               | `string` The ID string of this achievement.                                                                                                                                                                                                    |
| [IsIncremental](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement_1aee0b644e3e172d7888a56c9d6216c8da)    | `bool` Indicates whether this achievement is incremental.                                                                                                                                                                                      |
| [IsRevealed](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement_1a66525357f78e550f0d3e0cf8a68c449e)       | `bool` Indicates whether the achievement is revealed or not (hidden).                                                                                                                                                                          |
| [IsUnlocked](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement_1aecc9cc9f855dd45dda6a0f02838db05b)       | `bool` Indicates whether the achievement is unlocked or not.                                                                                                                                                                                   |
| [LastModifiedTime](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement_1a79268bc334d62d884ebed7d10e814cf0) | `DateTime` The date and time the state of the achievement was modified.                                                                                                                                                                        |
| [Name](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement_1a67c30fdc0e4cd601f01ee54b9a2d5ece)             | `string` The name of this achievement.                                                                                                                                                                                                         |
| [Points](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement_1aeae19820a01eae718f966cd521b299de)           | `ulong` The number of experience points earned for unlocking this[Achievement](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement). |
| [RevealedImageUrl](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement_1a882d2ab5a3f29fd72310fb96edea0e69) | `string` The URL to the image to display when the achievement is revealed.                                                                                                                                                                     |
| [TotalSteps](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement_1a7dfc4adc76dbe76c71204906caaf754d)       | `int` The total number of steps needed to unlock this achievement.                                                                                                                                                                             |
| [UnlockedImageUrl](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement_1ac97eb8b768076ebef515fb55bf406c70) | `string` The URL to the image to display when the achievement is unlocked.                                                                                                                                                                     |

|                                                                                                                                                                                                                                     ### Public functions                                                                                                                                                                                                                                      ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ToString](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement_1a34080a315bf18bdbc7d2947cc655aa06)`()` | `override string` Returns a System.String that represents the current[GooglePlayGames.BasicApi.Achievement](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement). |

## Properties

### CurrentSteps

```c#
int CurrentSteps
```  
The number of steps the user has gone towards unlocking this achievement.  

### Description

```c#
string Description
```  
The description of this achievement.  

### Id

```c#
string Id
```  
The ID string of this achievement.  

### IsIncremental

```c#
bool IsIncremental
```  
Indicates whether this achievement is incremental.  

### IsRevealed

```c#
bool IsRevealed
```  
Indicates whether the achievement is revealed or not (hidden).  

### IsUnlocked

```c#
bool IsUnlocked
```  
Indicates whether the achievement is unlocked or not.  

### LastModifiedTime

```c#
DateTime LastModifiedTime
```  
The date and time the state of the achievement was modified.

The value is invalid (-1 long) if the achievement state has never been updated.  

### Name

```c#
string Name
```  
The name of this achievement.  

### Points

```c#
ulong Points
```  
The number of experience points earned for unlocking this[Achievement](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement).  

### RevealedImageUrl

```c#
string RevealedImageUrl
```  
The URL to the image to display when the achievement is revealed.  

### TotalSteps

```c#
int TotalSteps
```  
The total number of steps needed to unlock this achievement.  

### UnlockedImageUrl

```c#
string UnlockedImageUrl
```  
The URL to the image to display when the achievement is unlocked.

## Public functions

### Achievement

```c#
 Achievement()
```  

### ToString

```c#
override string ToString()
```  
Returns a System.String that represents the current[GooglePlayGames.BasicApi.Achievement](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement).

<br />

|                                                                                                                            Details                                                                                                                             ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A System.String that represents the current[GooglePlayGames.BasicApi.Achievement](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement). |