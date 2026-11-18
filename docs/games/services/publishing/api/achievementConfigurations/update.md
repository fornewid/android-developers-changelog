---
title: https://developer.android.com/games/services/publishing/api/achievementConfigurations/update
url: https://developer.android.com/games/services/publishing/api/achievementConfigurations/update
source: md.txt
---

> Documentation index: https://developer.android.com/games/services/publishing/api/achievementConfigurations/llms.txt

**Requires [authorization](https://developer.android.com/games/services/publishing/api/achievementConfigurations/update.md.txt#auth)**

Update the metadata of the achievement configuration with the given ID.

## Request

### HTTP request

```
PUT https://www.googleapis.com/games/v1configuration/achievements/achievementId
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
| `https://www.googleapis.com/auth/androidpublisher` |

### Request body

In the request body, supply an [AchievementConfigurations resource](https://developer.android.com/games/services/publishing/api/achievementConfigurations.md.txt#resource).

## Response

If successful, this method returns an [AchievementConfigurations resource](https://developer.android.com/games/services/publishing/api/achievementConfigurations.md.txt#resource) in the response body.