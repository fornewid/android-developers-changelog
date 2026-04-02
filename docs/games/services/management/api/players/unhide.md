---
title: Players: unhide  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/management/api/players/unhide
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

# Players: unhide Stay organized with collections Save and categorize content based on your preferences.



**Requires [authorization](#auth)**

Unhide the given player's leaderboard scores from the given application. This method is only available to user accounts for your Play Console and may take up to a day to take effect.

## Request

### HTTP request

```
DELETE https://www.googleapis.com/games/v1management/applications/applicationId/players/hidden/playerId
```

### Parameters

| Parameter name | Value | Description |
| --- | --- | --- |
| **Path parameters** | | |
| `applicationId` | `string` | The application ID from the Google Play Console. |
| `playerId` | `string` | A player ID. A value of `me` may be used in place of the authenticated player's ID. |

### Authorization

This request requires authorization with the following scope ([read more about authentication and authorization](/accounts/docs/OAuth2)).

| Scope |
| --- |
| `https://www.googleapis.com/auth/games` |

### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns an empty response body.