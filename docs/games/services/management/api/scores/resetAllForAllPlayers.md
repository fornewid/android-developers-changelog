---
title: https://developer.android.com/games/services/management/api/scores/resetAllForAllPlayers
url: https://developer.android.com/games/services/management/api/scores/resetAllForAllPlayers
source: md.txt
---

# Scores: resetAllForAllPlayers

**Requires[authorization](https://developer.android.com/games/services/management/api/scores/resetAllForAllPlayers#auth)**

Resets scores for all draft leaderboards for all players. This method is only available to user accounts for your developer console.

## Request

### HTTP request

```
POST https://www.googleapis.com/games/v1management/scores/resetAllForAllPlayers
```

### Authorization

This request requires authorization with the following scope ([read more about authentication and authorization](https://developer.android.com/accounts/docs/OAuth2)).

|                  Scope                  |
|-----------------------------------------|
| `https://www.googleapis.com/auth/games` |

### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns an empty response body.