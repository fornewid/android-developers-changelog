---
title: https://developer.android.com/games/services/management/api/turnBasedMatches/resetForAllPlayers
url: https://developer.android.com/games/services/management/api/turnBasedMatches/resetForAllPlayers
source: md.txt
---

# TurnBasedMatches: resetForAllPlayers

**Requires[authorization](https://developer.android.com/games/services/management/api/turnBasedMatches/resetForAllPlayers#auth)**

Deletes turn-based matches where the only match participants are from whitelisted tester accounts for your application. This method is only available to user accounts for your developer console.

## Request

### HTTP request

```
POST https://www.googleapis.com/games/v1management/turnbasedmatches/resetForAllPlayers
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