---
title: https://developer.android.com/games/services/management/api/rooms/resetForAllPlayers
url: https://developer.android.com/games/services/management/api/rooms/resetForAllPlayers
source: md.txt
---

# Rooms: resetForAllPlayers

**Requires[authorization](https://developer.android.com/games/services/management/api/rooms/resetForAllPlayers#auth)**

Deletes rooms where the only room participants are from whitelisted tester accounts for your application. This method is only available to user accounts for your developer console.

## Request

### HTTP request

```
POST https://www.googleapis.com/games/v1management/rooms/resetForAllPlayers
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