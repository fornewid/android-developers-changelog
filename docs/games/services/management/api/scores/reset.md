---
title: Scores: reset  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/management/api/scores/reset
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

# Scores: reset Stay organized with collections Save and categorize content based on your preferences.




**Requires [authorization](#auth)**

Resets scores for the leaderboard with the given ID for the currently authenticated player. This method is only accessible to whitelisted tester accounts for your application.

## Request

### HTTP request

```
POST https://www.googleapis.com/games/v1management/leaderboards/leaderboardId/scores/reset
```

### Parameters

| Parameter name | Value | Description |
| --- | --- | --- |
| **Path parameters** | | |
| `leaderboardId` | `string` | The ID of the leaderboard. |

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
  "kind": "gamesManagement#playerScoreResetResponse",
  "definitionId": string,
  "resetScoreTimeSpans": [
    string
  ]
}
```

| Property name | Value | Description | Notes |
| --- | --- | --- | --- |
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#playerScoreResetResponse`. |  |
| `resetScoreTimeSpans[]` | `list` | The time spans of the updated score.  Possible values are:  * "`ALL_TIME`" - The score is an all-time score. * "`WEEKLY`" - The score is a weekly score. * "`DAILY`" - The score is a daily score. |  |
| `definitionId` | `string` | The ID of an leaderboard for which player state has been updated. |  |