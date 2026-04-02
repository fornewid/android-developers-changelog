---
title: Rooms: resetForAllPlayers  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/management/api/rooms/resetForAllPlayers
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

# Rooms: resetForAllPlayers Stay organized with collections Save and categorize content based on your preferences.



**Requires [authorization](#auth)**

Deletes rooms where the only room participants are from whitelisted tester accounts for your application. This method is only available to user accounts for your developer console.

## Request

### HTTP request

```
POST https://www.googleapis.com/games/v1management/rooms/resetForAllPlayers
```

### Authorization

This request requires authorization with the following scope ([read more about authentication and authorization](/accounts/docs/OAuth2)).

| Scope |
| --- |
| `https://www.googleapis.com/auth/games` |

### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns an empty response body.