---
title: AchievementConfigurations: insert  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/publishing/api/achievementConfigurations/insert
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

# AchievementConfigurations: insert Stay organized with collections Save and categorize content based on your preferences.



**Requires [authorization](#auth)**

Insert a new achievement configuration in this application.

## Request

### HTTP request

```
POST https://www.googleapis.com/games/v1configuration/applications/applicationId/achievements
```

### Parameters

| Parameter name | Value | Description |
| --- | --- | --- |
| **Path parameters** | | |
| `applicationId` | `string` | The application ID from the Google Play Console. |

### Authorization

This request requires authorization with the following scope ([read more about authentication and authorization](/accounts/docs/OAuth2)).

| Scope |
| --- |
| `https://www.googleapis.com/auth/androidpublisher` |

### Request body

In the request body, supply an [AchievementConfigurations resource](/games/services/publishing/api/achievementConfigurations#resource).

## Response

If successful, this method returns an [AchievementConfigurations resource](/games/services/publishing/api/achievementConfigurations#resource) in the response body.