---
title: https://developer.android.com/games/services/publishing/api/achievementConfigurations/delete
url: https://developer.android.com/games/services/publishing/api/achievementConfigurations/delete
source: md.txt
---

# AchievementConfigurations: delete

**Requires[authorization](https://developer.android.com/games/services/publishing/api/achievementConfigurations/delete#auth)**

Delete the achievement configuration with the given ID.

## Request

### HTTP request

```
DELETE https://www.googleapis.com/games/v1configuration/achievements/achievementId
```

### Parameters

| Parameter name  |  Value   |                  Description                   |
|-----------------|----------|------------------------------------------------|
| **Path parameters**                                                       |||
| `achievementId` | `string` | The ID of the achievement used by this method. |

### Authorization

This request requires authorization with the following scope ([read more about authentication and authorization](https://developer.android.com/accounts/docs/OAuth2)).

|                       Scope                        |
|----------------------------------------------------|
| `https://www.googleapis.com/auth/androidpublisher` |

### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns an empty response body.