---
title: Events: resetAll  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/management/api/events/resetAll
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

# Events: resetAll Stay organized with collections Save and categorize content based on your preferences.




**Requires [authorization](#auth)**

Resets all player progress on all events for the currently authenticated player. This method is only accessible to whitelisted tester accounts for your application.

## Request

### HTTP request

```
POST https://www.googleapis.com/games/v1management/events/reset
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