---
title: https://developer.android.com/games/services/management/api/achievements/resetForAllPlayers
url: https://developer.android.com/games/services/management/api/achievements/resetForAllPlayers
source: md.txt
---

**Requires [authorization](https://developer.android.com/games/services/management/api/achievements/resetForAllPlayers#auth)**

Resets the achievement with the given ID for all players. This method is only available to user accounts for your developer console. Only draft achievements can be reset.

## Request

### HTTP request

```
POST https://www.googleapis.com/games/v1management/achievements/achievementId/resetForAllPlayers
```

### Parameters

| Parameter name | Value | Description |
|---|---|---|
| **Path parameters** |||
| `achievementId` | `string` | The ID of the achievement used by this method. |

### Authorization

This request requires authorization with the following scope ([read more about authentication and authorization](https://developers.google.com/identity/protocols/oauth2)).

| Scope |
|---|
| `https://www.googleapis.com/auth/games` |

### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns an empty response body.