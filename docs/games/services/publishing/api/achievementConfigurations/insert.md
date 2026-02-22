---
title: https://developer.android.com/games/services/publishing/api/achievementConfigurations/insert
url: https://developer.android.com/games/services/publishing/api/achievementConfigurations/insert
source: md.txt
---

# AchievementConfigurations: insert

**Requires[authorization](https://developer.android.com/games/services/publishing/api/achievementConfigurations/insert#auth)**

Insert a new achievement configuration in this application.

## Request

### HTTP request

```
POST https://www.googleapis.com/games/v1configuration/applications/applicationId/achievements
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

In the request body, supply an[AchievementConfigurations resource](https://developer.android.com/games/services/publishing/api/achievementConfigurations#resource).

## Response

If successful, this method returns an[AchievementConfigurations resource](https://developer.android.com/games/services/publishing/api/achievementConfigurations#resource)in the response body.