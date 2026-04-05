---
title: Achievements: resetAll  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/management/api/achievements/resetAll
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

# Achievements: resetAll Stay organized with collections Save and categorize content based on your preferences.




**Requires [authorization](#auth)**

Resets all achievements for the currently authenticated player for your application. This method is only accessible to whitelisted tester accounts for your application.

## Request

### HTTP request

```
POST https://www.googleapis.com/games/v1management/achievements/reset
```

### Authorization

This request requires authorization with the following scope ([read more about authentication and authorization](/accounts/docs/OAuth2)).

| Scope |
| --- |
| `https://www.googleapis.com/auth/games` |

### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns a response body with the following structure:

```
{
  "kind": "gamesManagement#achievementResetAllResponse",
  "results": [
    {
      "kind": "gamesManagement#achievementResetResponse",
      "definitionId": string,
      "updateOccurred": boolean,
      "currentState": string
    }
  ]
}
```

| Property name | Value | Description | Notes |
| --- | --- | --- | --- |
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#achievementResetAllResponse`. |  |
| `results[]` | `list` | The achievement reset results. |  |
| `results[].kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#achievementResetResponse`. |  |
| `results[].definitionId` | `string` | The ID of an achievement for which player state has been updated. |  |
| `results[].updateOccurred` | `boolean` | Flag to indicate if the requested update actually occurred. |  |
| `results[].currentState` | `string` | The current state of the achievement. This is the same as the initial state of the achievement.  Possible values are:  * "`HIDDEN`"- Achievement is hidden. * "`REVEALED`" - Achievement is revealed. * "`UNLOCKED`" - Achievement is unlocked. |  |