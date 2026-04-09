---
title: Achievements: resetMultipleForAllPlayers  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/management/api/achievements/resetMultipleForAllPlayers
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

# Achievements: resetMultipleForAllPlayers Stay organized with collections Save and categorize content based on your preferences.




**Requires [authorization](#auth)**

Resets achievements with the given IDs for all players. This method is only available to user accounts for your developer console. Only draft achievements may be reset.

## Request

### HTTP request

```
POST https://www.googleapis.com/games/v1management/achievements/resetMultipleForAllPlayers
```

### Authorization

This request requires authorization with the following scope ([read more about authentication and authorization](/accounts/docs/OAuth2)).

| Scope |
| --- |
| `https://www.googleapis.com/auth/games` |

### Request body

In the request body, supply data with the following structure:

```
{
  "kind": "gamesManagement#achievementResetMultipleForAllRequest",
  "achievement_ids": [
    string
  ]
}
```

| Property name | Value | Description | Notes |
| --- | --- | --- | --- |
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#achievementResetMultipleForAllRequest`. |  |
| `achievement_ids[]` | `list` | The IDs of achievements to reset. |  |

## Response

If successful, this method returns an empty response body.