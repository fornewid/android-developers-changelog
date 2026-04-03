---
title: Achievements: reset  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/management/api/achievements/reset
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

# Achievements: reset Stay organized with collections Save and categorize content based on your preferences.



**Requires [authorization](#auth)**

Resets the achievement with the given ID for the currently authenticated player. This method is only accessible to whitelisted tester accounts for your application.

## Request

### HTTP request

```
POST https://www.googleapis.com/games/v1management/achievements/achievementId/reset
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

If successful, this method returns a response body with the following structure:

```
{
  "kind": "gamesManagement#achievementResetResponse",
  "definitionId": string,
  "updateOccurred": boolean,
  "currentState": string
}
```

| Property name | Value | Description | Notes |
| --- | --- | --- | --- |
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#achievementResetResponse`. |  |
| `definitionId` | `string` | The ID of an achievement for which player state has been updated. |  |
| `updateOccurred` | `boolean` | Flag to indicate if the requested update actually occurred. |  |
| `currentState` | `string` | The current state of the achievement. This is the same as the initial state of the achievement.  Possible values are:  * "`HIDDEN`"- Achievement is hidden. * "`REVEALED`" - Achievement is revealed. * "`UNLOCKED`" - Achievement is unlocked. |  |