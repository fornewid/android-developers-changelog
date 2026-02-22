---
title: https://developer.android.com/games/services/publishing/api/leaderboardConfigurations/delete
url: https://developer.android.com/games/services/publishing/api/leaderboardConfigurations/delete
source: md.txt
---

# LeaderboardConfigurations: delete

**Requires[authorization](https://developer.android.com/games/services/publishing/api/leaderboardConfigurations/delete#auth)**

Delete the leaderboard configuration with the given ID.

## Request

### HTTP request

```
DELETE https://www.googleapis.com/games/v1configuration/leaderboards/leaderboardId
```

### Parameters

| Parameter name  |  Value   |        Description         |
|-----------------|----------|----------------------------|
| **Path parameters**                                   |||
| `leaderboardId` | `string` | The ID of the leaderboard. |

### Authorization

This request requires authorization with the following scope ([read more about authentication and authorization](https://developer.android.com/accounts/docs/OAuth2)).

|                       Scope                        |
|----------------------------------------------------|
| `https://www.googleapis.com/auth/androidpublisher` |

### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns an empty response body.