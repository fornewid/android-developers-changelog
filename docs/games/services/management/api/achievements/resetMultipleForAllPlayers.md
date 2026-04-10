---
title: https://developer.android.com/games/services/management/api/achievements/resetMultipleForAllPlayers
url: https://developer.android.com/games/services/management/api/achievements/resetMultipleForAllPlayers
source: md.txt
---

**Requires [authorization](https://developer.android.com/games/services/management/api/achievements/resetMultipleForAllPlayers#auth)**

Resets achievements with the given IDs for all players. This method is only available to user accounts for your developer console. Only draft achievements may be reset.

## Request

### HTTP request

```
POST https://www.googleapis.com/games/v1management/achievements/resetMultipleForAllPlayers
```

### Authorization

This request requires authorization with the following scope ([read more about authentication and authorization](https://developer.android.com/accounts/docs/OAuth2)).

| Scope |
|---|
| `https://www.googleapis.com/auth/games` |

### Request body

In the request body, supply data with the following structure:

```scdoc
{
  "kind": "gamesManagement#achievementResetMultipleForAllRequest",
  "achievement_ids": [
    string
  ]
}
```

| Property name | Value | Description | Notes |
|---|---|---|---|
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#achievementResetMultipleForAllRequest`. |   |
| `achievement_ids[]` | `list` | The IDs of achievements to reset. |   |

## Response

If successful, this method returns an empty response body.