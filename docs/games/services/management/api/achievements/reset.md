---
title: https://developer.android.com/games/services/management/api/achievements/reset
url: https://developer.android.com/games/services/management/api/achievements/reset
source: md.txt
---

**Requires [authorization](https://developer.android.com/games/services/management/api/achievements/reset#auth)**

Resets the achievement with the given ID for the currently authenticated player. This method is only accessible to whitelisted tester accounts for your application.

## Request

### HTTP request

```
POST https://www.googleapis.com/games/v1management/achievements/achievementId/reset
```

### Parameters

| Parameter name | Value | Description |
|---|---|---|
| **Path parameters** |||
| `achievementId` | `string` | The ID of the achievement used by this method. |

### Authorization

This request requires authorization with the following scope ([read more about authentication and authorization](https://developer.android.com/accounts/docs/OAuth2)).

| Scope |
|---|
| `https://www.googleapis.com/auth/games` |

### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns a response body with the following structure:

```text
{
  "kind": "gamesManagement#achievementResetResponse",
  "definitionId": string,
  "updateOccurred": boolean,
  "currentState": string
}
```

| Property name | Value | Description | Notes |
|---|---|---|---|
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#achievementResetResponse`. |   |
| `definitionId` | `string` | The ID of an achievement for which player state has been updated. |   |
| `updateOccurred` | `boolean` | Flag to indicate if the requested update actually occurred. |   |
| `currentState` | `string` | The current state of the achievement. This is the same as the initial state of the achievement. Possible values are: - "`HIDDEN`"- Achievement is hidden. - "`REVEALED`" - Achievement is revealed. - "`UNLOCKED`" - Achievement is unlocked. |   |