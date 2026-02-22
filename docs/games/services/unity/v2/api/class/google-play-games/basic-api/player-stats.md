---
title: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats
source: md.txt
---

# GooglePlayGames.BasicApi.PlayerStats Class Reference

# GooglePlayGames.BasicApi.PlayerStats

[Player](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player#class_google_play_games_1_1_basic_api_1_1_player)stats.

## Summary

See<https://developers.google.com/games/services/android/stats>

| ### Constructors and Destructors ||
|---|---|
| [PlayerStats](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats_1a708e634d5395073b31cf275335f03956)`(int numberOfPurchases, float avgSessionLength, int daysSinceLastPlayed, int numberOfSessions, float sessPercentile, float spendPercentile, float spendProbability, float churnProbability, float highSpenderProbability, float totalSpendNext28Days)` ||
| [PlayerStats](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats_1ab4c9e7f89387d5a611cc22ffca2f5b65)`()` ||

|                                                                                                                                                                                                                 ### Properties                                                                                                                                                                                                                  ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AvgSessionLength](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats_1a156c4d1c48dcf0fba3e26b3bfb5ca65f)       | `float` The length of the avg session in minutes.                                                                                                                                                                 |
| [ChurnProbability](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats_1af3fa832287cae297d4034537e97175a8)       | `float` The approximate probability of the player not returning to play the game.                                                                                                                                 |
| [DaysSinceLastPlayed](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats_1a0ac4aa40052463a40fe3769fd55648d6)    | `int` The days since last played.                                                                                                                                                                                 |
| [HighSpenderProbability](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats_1a08d387035ae717429f5f3e4d636d06a5) | `float` The high spender probability of this player.                                                                                                                                                              |
| [NumberOfPurchases](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats_1a7be79e5e32dccd476a3988f2dcf1a8a9)      | `int` The number of in-app purchases.                                                                                                                                                                             |
| [NumberOfSessions](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats_1abbae891490044745e3dc49e66f416893)       | `int` The number of sessions based on sign-ins.                                                                                                                                                                   |
| [SessPercentile](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats_1a41bec79dfc9e38a86a26fcdc3a9c9111)         | `float` The approximation of sessions percentile for the player.                                                                                                                                                  |
| [SpendPercentile](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats_1a975db0cd80a8dbb505f35c8350814856)        | `float` The approximate spend percentile of the player.                                                                                                                                                           |
| [SpendProbability](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats_1a1d0d81dd1b6be2ca100013b2a7561e2c)       | `float` The approximate probability of the player choosing to spend in this game.                                                                                                                                 |
| [TotalSpendNext28Days](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats_1a3077c9ad772c871c05d28fe1fce2da8d)   | `float` The predicted total spend of this player over the next 28 days.                                                                                                                                           |
| [Valid](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats_1a00c5ef77216b28580a94837b2dd0789a)                  | `bool` If this[PlayerStats](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats)object is valid (i.e. |

|                                                                                                                                           ### Public functions                                                                                                                                           ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| [HasAvgSessionLength](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats_1a1b82ff099f971737424bc1c9097b653f)`()`       | `bool` Determines whether this instance has AvgSessionLength.       |
| [HasChurnProbability](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats_1ae1f6fd49b252fdff60030d5754e6b5c7)`()`       | `bool` Determines whether this instance has ChurnProbability.       |
| [HasDaysSinceLastPlayed](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats_1ae05b04318b429d436822839951dd0041)`()`    | `bool` Determines whether this instance has DaysSinceLastPlayed.    |
| [HasHighSpenderProbability](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats_1a59641dd4759378a1702f2da206f1a941)`()` | `bool` Determines whether this instance has HighSpenderProbability. |
| [HasNumberOfPurchases](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats_1a0178776f4eba230e11fda8a69758886a)`()`      | `bool` Determines whether this instance has NumberOfPurchases.      |
| [HasNumberOfSessions](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats_1a0c8ee4545b0fac275f59ee9abcc768d2)`()`       | `bool` Determines whether this instance has NumberOfSessions.       |
| [HasSessPercentile](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats_1a8dbb91514c0dbd0b4c9f12fe6f7b7236)`()`         | `bool` Determines whether this instance has SessPercentile.         |
| [HasSpendPercentile](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats_1aa3692770ec337e01aeb026303987f7a3)`()`        | `bool` Determines whether this instance has SpendPercentile.        |
| [HasTotalSpendNext28Days](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats_1a40efab512d7beadef7967e6e24b52e01)`()`   | `bool` Determines whether this instance has TotalSpendNext28Days.   |

## Properties

### AvgSessionLength

```c#
float AvgSessionLength
```  
The length of the avg session in minutes.  

### ChurnProbability

```c#
float ChurnProbability
```  
The approximate probability of the player not returning to play the game.

Higher values indicate that a player is less likely to return. A return value less than zero indicates this value is not available.  

### DaysSinceLastPlayed

```c#
int DaysSinceLastPlayed
```  
The days since last played.  

### HighSpenderProbability

```c#
float HighSpenderProbability
```  
The high spender probability of this player.  

### NumberOfPurchases

```c#
int NumberOfPurchases
```  
The number of in-app purchases.  

### NumberOfSessions

```c#
int NumberOfSessions
```  
The number of sessions based on sign-ins.  

### SessPercentile

```c#
float SessPercentile
```  
The approximation of sessions percentile for the player.

This value is given as a decimal value between 0 and 1 (inclusive). It indicates how many sessions the current player has played in comparison to the rest of this game's player base. Higher numbers indicate that this player has played more sessions. A return value less than zero indicates this value is not available.  

### SpendPercentile

```c#
float SpendPercentile
```  
The approximate spend percentile of the player.

This value is given as a decimal value between 0 and 1 (inclusive). It indicates how much the current player has spent in comparison to the rest of this game's player base. Higher numbers indicate that this player has spent more. A return value less than zero indicates this value is not available.  

### SpendProbability

```c#
float SpendProbability
```  
The approximate probability of the player choosing to spend in this game.

This value is given as a decimal value between 0 and 1 (inclusive). Higher values indicate that a player is more likely to spend. A return value less than zero indicates this value is not available.  

### TotalSpendNext28Days

```c#
float TotalSpendNext28Days
```  
The predicted total spend of this player over the next 28 days.  

### Valid

```c#
bool Valid
```  
If this[PlayerStats](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats)object is valid (i.e.

successfully retrieved from games services).

Note that a[PlayerStats](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats)with all stats unset may still be valid.

## Public functions

### HasAvgSessionLength

```c#
bool HasAvgSessionLength()
```  
Determines whether this instance has AvgSessionLength.

<br />

|                                   Details                                    ||
|-------------|-----------------------------------------------------------------|
| **Returns** | `true`if this instance has AvgSessionLength; otherwise,`false`. |

### HasChurnProbability

```c#
bool HasChurnProbability()
```  
Determines whether this instance has ChurnProbability.

<br />

|                                   Details                                    ||
|-------------|-----------------------------------------------------------------|
| **Returns** | `true`if this instance has ChurnProbability; otherwise,`false`. |

### HasDaysSinceLastPlayed

```c#
bool HasDaysSinceLastPlayed()
```  
Determines whether this instance has DaysSinceLastPlayed.

<br />

|                                     Details                                     ||
|-------------|--------------------------------------------------------------------|
| **Returns** | `true`if this instance has DaysSinceLastPlayed; otherwise,`false`. |

### HasHighSpenderProbability

```c#
bool HasHighSpenderProbability()
```  
Determines whether this instance has HighSpenderProbability.

<br />

|                                      Details                                       ||
|-------------|-----------------------------------------------------------------------|
| **Returns** | `true`if this instance has HighSpenderProbability; otherwise,`false`. |

### HasNumberOfPurchases

```c#
bool HasNumberOfPurchases()
```  
Determines whether this instance has NumberOfPurchases.

<br />

|                                    Details                                    ||
|-------------|------------------------------------------------------------------|
| **Returns** | `true`if this instance has NumberOfPurchases; otherwise,`false`. |

### HasNumberOfSessions

```c#
bool HasNumberOfSessions()
```  
Determines whether this instance has NumberOfSessions.

<br />

|                                   Details                                    ||
|-------------|-----------------------------------------------------------------|
| **Returns** | `true`if this instance has NumberOfSessions; otherwise,`false`. |

### HasSessPercentile

```c#
bool HasSessPercentile()
```  
Determines whether this instance has SessPercentile.

<br />

|                                  Details                                   ||
|-------------|---------------------------------------------------------------|
| **Returns** | `true`if this instance has SessPercentile; otherwise,`false`. |

### HasSpendPercentile

```c#
bool HasSpendPercentile()
```  
Determines whether this instance has SpendPercentile.

<br />

|                                   Details                                   ||
|-------------|----------------------------------------------------------------|
| **Returns** | `true`if this instance has SpendPercentile; otherwise,`false`. |

### HasTotalSpendNext28Days

```c#
bool HasTotalSpendNext28Days()
```  
Determines whether this instance has TotalSpendNext28Days.

<br />

|                                     Details                                      ||
|-------------|---------------------------------------------------------------------|
| **Returns** | `true`if this instance has TotalSpendNext28Days; otherwise,`false`. |

### PlayerStats

```c#
 PlayerStats(
  int numberOfPurchases,
  float avgSessionLength,
  int daysSinceLastPlayed,
  int numberOfSessions,
  float sessPercentile,
  float spendPercentile,
  float spendProbability,
  float churnProbability,
  float highSpenderProbability,
  float totalSpendNext28Days
)
```  

### PlayerStats

```c#
 PlayerStats()
```