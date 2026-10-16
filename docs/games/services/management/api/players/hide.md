---
title: https://developer.android.com/games/services/management/api/players/hide
url: https://developer.android.com/games/services/management/api/players/hide
source: md.txt
---

# Players: hide

**Requires[authorization](https://developer.android.com/games/services/management/api/players/hide#auth)**

Hide the given player's leaderboard scores from the given application. This method is only available to user accounts for your Play Console.

## Request

### HTTP request

```
POST https://www.googleapis.com/games/v1management/applications/applicationId/players/hidden/playerId
```

### Parameters

| Parameter name  |  Value   |                                    Description                                    |
|-----------------|----------|-----------------------------------------------------------------------------------|
| **Path parameters**                                                                                          |||
| `applicationId` | `string` | The application ID from the Google Play Console.                                  |
| `playerId`      | `string` | A player ID. A value of`me`may be used in place of the authenticated player's ID. |

### Authorization

This request requires authorization with the following scope ([read more about authentication and authorization](https://developer.android.com/accounts/docs/OAuth2)).

|                  Scope                  |
|-----------------------------------------|
| `https://www.googleapis.com/auth/games` |

### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns an empty response body.