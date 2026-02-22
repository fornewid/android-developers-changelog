---
title: https://developer.android.com/games/services/publishing/api/leaderboardConfigurations/update
url: https://developer.android.com/games/services/publishing/api/leaderboardConfigurations/update
source: md.txt
---

# LeaderboardConfigurations: update

**Requires[authorization](https://developer.android.com/games/services/publishing/api/leaderboardConfigurations/update#auth)**

Update the metadata of the leaderboard configuration with the given ID.

## Request

### HTTP request

```
PUT https://www.googleapis.com/games/v1configuration/leaderboards/leaderboardId
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

In the request body, supply a[LeaderboardConfigurations resource](https://developer.android.com/games/services/publishing/api/leaderboardConfigurations#resource).

## Response

If successful, this method returns a[LeaderboardConfigurations resource](https://developer.android.com/games/services/publishing/api/leaderboardConfigurations#resource)in the response body.