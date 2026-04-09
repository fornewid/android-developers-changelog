---
title: GooglePlayGames.BasicApi.PlayerStats Class Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# GooglePlayGames.BasicApi.PlayerStats

[Player](/games/services/unity/v2/api/class/google-play-games/basic-api/player#class_google_play_games_1_1_basic_api_1_1_player) stats.

## Summary

See <https://developers.google.com/games/services/android/stats>

| Constructors and Destructors | |
| --- | --- |
| `PlayerStats(int numberOfPurchases, float avgSessionLength, int daysSinceLastPlayed, int numberOfSessions, float sessPercentile, float spendPercentile, float spendProbability, float churnProbability, float highSpenderProbability, float totalSpendNext28Days)` | |
| `PlayerStats()` | |

| Properties | |
| --- | --- |
| `AvgSessionLength` | `float`  The length of the avg session in minutes. |
| `ChurnProbability` | `float`  The approximate probability of the player not returning to play the game. |
| `DaysSinceLastPlayed` | `int`  The days since last played. |
| `HighSpenderProbability` | `float`  The high spender probability of this player. |
| `NumberOfPurchases` | `int`  The number of in-app purchases. |
| `NumberOfSessions` | `int`  The number of sessions based on sign-ins. |
| `SessPercentile` | `float`  The approximation of sessions percentile for the player. |
| `SpendPercentile` | `float`  The approximate spend percentile of the player. |
| `SpendProbability` | `float`  The approximate probability of the player choosing to spend in this game. |
| `TotalSpendNext28Days` | `float`  The predicted total spend of this player over the next 28 days. |
| `Valid` | `bool`  If this [PlayerStats](/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats) object is valid (i.e. |

| Public functions | |
| --- | --- |
| `HasAvgSessionLength()` | `bool`  Determines whether this instance has AvgSessionLength. |
| `HasChurnProbability()` | `bool`  Determines whether this instance has ChurnProbability. |
| `HasDaysSinceLastPlayed()` | `bool`  Determines whether this instance has DaysSinceLastPlayed. |
| `HasHighSpenderProbability()` | `bool`  Determines whether this instance has HighSpenderProbability. |
| `HasNumberOfPurchases()` | `bool`  Determines whether this instance has NumberOfPurchases. |
| `HasNumberOfSessions()` | `bool`  Determines whether this instance has NumberOfSessions. |
| `HasSessPercentile()` | `bool`  Determines whether this instance has SessPercentile. |
| `HasSpendPercentile()` | `bool`  Determines whether this instance has SpendPercentile. |
| `HasTotalSpendNext28Days()` | `bool`  Determines whether this instance has TotalSpendNext28Days. |

## Properties

### AvgSessionLength

```
float AvgSessionLength
```

The length of the avg session in minutes.

### ChurnProbability

```
float ChurnProbability
```

The approximate probability of the player not returning to play the game.

Higher values indicate that a player is less likely to return. A return value less than zero indicates this value is not available.

### DaysSinceLastPlayed

```
int DaysSinceLastPlayed
```

The days since last played.

### HighSpenderProbability

```
float HighSpenderProbability
```

The high spender probability of this player.

### NumberOfPurchases

```
int NumberOfPurchases
```

The number of in-app purchases.

### NumberOfSessions

```
int NumberOfSessions
```

The number of sessions based on sign-ins.

### SessPercentile

```
float SessPercentile
```

The approximation of sessions percentile for the player.

This value is given as a decimal value between 0 and 1 (inclusive). It indicates how many sessions the current player has played in comparison to the rest of this game's player base. Higher numbers indicate that this player has played more sessions. A return value less than zero indicates this value is not available.

### SpendPercentile

```
float SpendPercentile
```

The approximate spend percentile of the player.

This value is given as a decimal value between 0 and 1 (inclusive). It indicates how much the current player has spent in comparison to the rest of this game's player base. Higher numbers indicate that this player has spent more. A return value less than zero indicates this value is not available.

### SpendProbability

```
float SpendProbability
```

The approximate probability of the player choosing to spend in this game.

This value is given as a decimal value between 0 and 1 (inclusive). Higher values indicate that a player is more likely to spend. A return value less than zero indicates this value is not available.

### TotalSpendNext28Days

```
float TotalSpendNext28Days
```

The predicted total spend of this player over the next 28 days.

### Valid

```
bool Valid
```

If this [PlayerStats](/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats) object is valid (i.e.

successfully retrieved from games services).

Note that a [PlayerStats](/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats) with all stats unset may still be valid.

## Public functions

### HasAvgSessionLength

```
bool HasAvgSessionLength()
```

Determines whether this instance has AvgSessionLength.

Details | || **Returns** | `true` if this instance has AvgSessionLength; otherwise, `false`. |

### HasChurnProbability

```
bool HasChurnProbability()
```

Determines whether this instance has ChurnProbability.

Details | || **Returns** | `true` if this instance has ChurnProbability; otherwise, `false`. |

### HasDaysSinceLastPlayed

```
bool HasDaysSinceLastPlayed()
```

Determines whether this instance has DaysSinceLastPlayed.

Details | || **Returns** | `true` if this instance has DaysSinceLastPlayed; otherwise, `false`. |

### HasHighSpenderProbability

```
bool HasHighSpenderProbability()
```

Determines whether this instance has HighSpenderProbability.

Details | || **Returns** | `true` if this instance has HighSpenderProbability; otherwise, `false`. |

### HasNumberOfPurchases

```
bool HasNumberOfPurchases()
```

Determines whether this instance has NumberOfPurchases.

Details | || **Returns** | `true` if this instance has NumberOfPurchases; otherwise, `false`. |

### HasNumberOfSessions

```
bool HasNumberOfSessions()
```

Determines whether this instance has NumberOfSessions.

Details | || **Returns** | `true` if this instance has NumberOfSessions; otherwise, `false`. |

### HasSessPercentile

```
bool HasSessPercentile()
```

Determines whether this instance has SessPercentile.

Details | || **Returns** | `true` if this instance has SessPercentile; otherwise, `false`. |

### HasSpendPercentile

```
bool HasSpendPercentile()
```

Determines whether this instance has SpendPercentile.

Details | || **Returns** | `true` if this instance has SpendPercentile; otherwise, `false`. |

### HasTotalSpendNext28Days

```
bool HasTotalSpendNext28Days()
```

Determines whether this instance has TotalSpendNext28Days.

Details | || **Returns** | `true` if this instance has TotalSpendNext28Days; otherwise, `false`. |

### PlayerStats

```
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

```
 PlayerStats()
```