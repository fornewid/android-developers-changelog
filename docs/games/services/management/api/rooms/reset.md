---
title: https://developer.android.com/games/services/management/api/rooms/reset
url: https://developer.android.com/games/services/management/api/rooms/reset
source: md.txt
---

# Rooms: reset

**Requires[authorization](https://developer.android.com/games/services/management/api/rooms/reset#auth)**

Reset all rooms for the currently authenticated player for your application. This method is only accessible to whitelisted tester accounts for your application.

## Request

### HTTP request

```
POST https://www.googleapis.com/games/v1management/rooms/reset
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