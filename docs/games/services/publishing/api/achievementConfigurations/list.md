---
title: AchievementConfigurations: list  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/publishing/api/achievementConfigurations/list
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

# AchievementConfigurations: list Stay organized with collections Save and categorize content based on your preferences.




**Requires [authorization](#auth)**

Returns a list of the achievement configurations in this application.

## Request

### HTTP request

```
GET https://www.googleapis.com/games/v1configuration/applications/applicationId/achievements
```

### Parameters

| Parameter name | Value | Description |
| --- | --- | --- |
| **Path parameters** | | |
| `applicationId` | `string` | The application ID from the Google Play Console. |
| **Optional query parameters** | | |
| `maxResults` | `integer` | The maximum number of resource configurations to return in the response, used for paging. For any response, the actual number of resources returned may be less than the specified `maxResults`. Acceptable values are `1` to `200`, inclusive. |
| `pageToken` | `string` | The token returned by the previous request. |

### Authorization

This request requires authorization with the following scope ([read more about authentication and authorization](/accounts/docs/OAuth2)).

| Scope |
| --- |
| `https://www.googleapis.com/auth/androidpublisher` |

### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns a response body with the following structure:

```
{
  "kind": "gamesConfiguration#achievementConfigurationListResponse",
  "nextPageToken": string,
  "items": [
    achievementConfigurations Resource
  ]
}
```

| Property name | Value | Description | Notes |
| --- | --- | --- | --- |
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `games#achievementConfigurationListResponse`. |  |
| `nextPageToken` | `string` | The pagination token for the next page of results. |  |
| `items[]` | `list` | The achievement configurations. |  |