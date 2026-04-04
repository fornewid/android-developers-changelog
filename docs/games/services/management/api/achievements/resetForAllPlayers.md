---
title: Achievements: resetForAllPlayers  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/management/api/achievements/resetForAllPlayers
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

# Achievements: resetForAllPlayers Stay organized with collections Save and categorize content based on your preferences.



**Requires [authorization](#auth)**

Resets the achievement with the given ID for all players. This method is only available to user accounts for your developer console. Only draft achievements can be reset.

## Request

### HTTP request

```
POST https://www.googleapis.com/games/v1management/achievements/achievementId/resetForAllPlayers
```

### Parameters

| Parameter name | Value | Description |
| --- | --- | --- |
| **Path parameters** | | |
| `achievementId` | `string` | The ID of the achievement used by this method. |

### Authorization

This request requires authorization with the following scope ([read more about authentication and authorization](/accounts/docs/OAuth2)).

| Scope |
| --- |
| `https://www.googleapis.com/auth/games` |

### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns an empty response body.