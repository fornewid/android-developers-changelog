---
title: https://developer.android.com/games/services/management/api/scores/resetForAllPlayers
url: https://developer.android.com/games/services/management/api/scores/resetForAllPlayers
source: md.txt
---

# Scores: resetForAllPlayers

**Requires[authorization](https://developer.android.com/games/services/management/api/scores/resetForAllPlayers#auth)**

Resets scores for the leaderboard with the given ID for all players. This method is only available to user accounts for your developer console. Only draft leaderboards can be reset.

## Request

### HTTP request

```
POST https://www.googleapis.com/games/v1management/leaderboards/leaderboardId/scores/resetForAllPlayers
```

### Parameters

| Parameter name  |  Value   |        Description         |
|-----------------|----------|----------------------------|
| **Path parameters**                                   |||
| `leaderboardId` | `string` | The ID of the leaderboard. |

### Authorization

This request requires authorization with the following scope ([read more about authentication and authorization](https://developer.android.com/accounts/docs/OAuth2)).

|                  Scope                  |
|-----------------------------------------|
| `https://www.googleapis.com/auth/games` |

### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns an empty response body.