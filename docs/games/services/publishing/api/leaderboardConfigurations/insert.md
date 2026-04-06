---
title: https://developer.android.com/games/services/publishing/api/leaderboardConfigurations/insert
url: https://developer.android.com/games/services/publishing/api/leaderboardConfigurations/insert
source: md.txt
---

# LeaderboardConfigurations: insert

**Requires[authorization](https://developer.android.com/games/services/publishing/api/leaderboardConfigurations/insert#auth)**

Insert a new leaderboard configuration in this application.

## Request

### HTTP request

```
POST https://www.googleapis.com/games/v1configuration/applications/applicationId/leaderboards
```

### Parameters

| Parameter name  |  Value   |                   Description                    |
|-----------------|----------|--------------------------------------------------|
| **Path parameters**                                                         |||
| `applicationId` | `string` | The application ID from the Google Play Console. |

### Authorization

This request requires authorization with the following scope ([read more about authentication and authorization](https://developer.android.com/accounts/docs/OAuth2)).

|                       Scope                        |
|----------------------------------------------------|
| `https://www.googleapis.com/auth/androidpublisher` |

### Request body

In the request body, supply a[LeaderboardConfigurations resource](https://developer.android.com/games/services/publishing/api/leaderboardConfigurations#resource).

## Response

If successful, this method returns a[LeaderboardConfigurations resource](https://developer.android.com/games/services/publishing/api/leaderboardConfigurations#resource)in the response body.