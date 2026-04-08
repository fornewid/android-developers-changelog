---
title: Events: resetMultipleForAllPlayers  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/management/api/events/resetMultipleForAllPlayers
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

# Events: resetMultipleForAllPlayers Stay organized with collections Save and categorize content based on your preferences.




**Requires [authorization](#auth)**

Resets events with the given IDs for all players. This method is only available to user accounts for your developer console. Only draft events may be reset.

## Request

### HTTP request

```
POST https://www.googleapis.com/games/v1management/events/resetMultipleForAllPlayers
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
  "kind": "gamesManagement#eventsResetMultipleForAllRequest",
  "event_ids": [
    string
  ]
}
```

| Property name | Value | Description | Notes |
| --- | --- | --- | --- |
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#eventsResetMultipleForAllRequest`. |  |
| `event_ids[]` | `list` | The IDs of events to reset. |  |

## Response

If successful, this method returns an empty response body.