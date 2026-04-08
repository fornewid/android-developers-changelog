---
title: LeaderboardConfigurations: insert  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/publishing/api/leaderboardConfigurations/insert
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

# LeaderboardConfigurations: insert Stay organized with collections Save and categorize content based on your preferences.



**Requires [authorization](#auth)**

Insert a new leaderboard configuration in this application.

## Request

### HTTP request

```
POST https://www.googleapis.com/games/v1configuration/applications/applicationId/leaderboards
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

In the request body, supply a [LeaderboardConfigurations resource](/games/services/publishing/api/leaderboardConfigurations#resource).

## Response

If successful, this method returns a [LeaderboardConfigurations resource](/games/services/publishing/api/leaderboardConfigurations#resource) in the response body.