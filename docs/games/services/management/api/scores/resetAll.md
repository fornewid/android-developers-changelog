---
title: https://developer.android.com/games/services/management/api/scores/resetAll
url: https://developer.android.com/games/services/management/api/scores/resetAll
source: md.txt
---

**Requires [authorization](https://developer.android.com/games/services/management/api/scores/resetAll#auth)**

Resets all scores for all leaderboards for the currently authenticated players. This method is only accessible to whitelisted tester accounts for your application.

## Request

### HTTP request

```
POST https://www.googleapis.com/games/v1management/scores/reset
```

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
  "kind": "gamesManagement#playerScoreResetAllResponse",
  "results": [
    {
      "kind": "gamesManagement#playerScoreResetResponse",
      "definitionId": string,
      "resetScoreTimeSpans": [
        string
      ]
    }
  ]
}
```

| Property name | Value | Description | Notes |
|---|---|---|---|
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#playerScoreResetResponse`. |   |
| `results[]` | `list` | The leaderboard reset results. |   |
| `results[].kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#playerScoreResetResponse`. |   |
| `results[].definitionId` | `string` | The ID of an leaderboard for which player state has been updated. |   |
| `results[].resetScoreTimeSpans[]` | `list` | The time spans of the updated score. Possible values are: - "`ALL_TIME`" - The score is an all-time score. - "`WEEKLY`" - The score is a weekly score. - "`DAILY`" - The score is a daily score. |   |