---
title: https://developer.android.com/games/services/management/api/scores/resetMultipleForAllPlayers
url: https://developer.android.com/games/services/management/api/scores/resetMultipleForAllPlayers
source: md.txt
---

**Requires [authorization](https://developer.android.com/games/services/management/api/scores/resetMultipleForAllPlayers#auth)**

Resets scores for the leaderboards with the given IDs for all players. This method is only available to user accounts for your developer console. Only draft leaderboards may be reset.

## Request

### HTTP request

```
POST https://www.googleapis.com/games/v1management/scores/resetMultipleForAllPlayers
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
  "kind": "gamesManagement#scoresResetMultipleForAllRequest",
  "leaderboard_ids": [
    string
  ]
}
```

| Property name | Value | Description | Notes |
|---|---|---|---|
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#scoresResetMultipleForAllRequest`. |   |
| `leaderboard_ids[]` | `list` | The IDs of leaderboards to reset. |   |

## Response

If successful, this method returns an empty response body.