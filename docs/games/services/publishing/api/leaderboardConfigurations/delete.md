---
title: LeaderboardConfigurations: delete  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/publishing/api/leaderboardConfigurations/delete
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

# LeaderboardConfigurations: delete Stay organized with collections Save and categorize content based on your preferences.



**Requires [authorization](#auth)**

Delete the leaderboard configuration with the given ID.

## Request

### HTTP request

```
DELETE https://www.googleapis.com/games/v1configuration/leaderboards/leaderboardId
```

### Parameters

| Parameter name | Value | Description |
| --- | --- | --- |
| **Path parameters** | | |
| `leaderboardId` | `string` | The ID of the leaderboard. |

### Authorization

This request requires authorization with the following scope ([read more about authentication and authorization](/accounts/docs/OAuth2)).

| Scope |
| --- |
| `https://www.googleapis.com/auth/androidpublisher` |

### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns an empty response body.