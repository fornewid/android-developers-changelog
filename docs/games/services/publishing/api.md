---
title: API Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/publishing/api
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

# API Reference Stay organized with collections Save and categorize content based on your preferences.




This API reference is organized by resource type. Each resource type has one or more data representations and one or more methods.

## Resource types

1. [AchievementConfigurations](#AchievementConfigurations)
2. [ImageConfigurations](#ImageConfigurations)
3. [LeaderboardConfigurations](#LeaderboardConfigurations)

## AchievementConfigurations

For AchievementConfigurations Resource details, see the [resource representation](/games/services/publishing/api/achievementConfigurations#resource) page.

| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to https://www.googleapis.com/games/v1configuration, unless otherwise noted | | |
| [delete](/games/services/publishing/api/achievementConfigurations/delete) | `DELETE  /achievements/achievementId` | Delete the achievement configuration with the given ID. |
| [get](/games/services/publishing/api/achievementConfigurations/get) | `GET  /achievements/achievementId` | Retrieves the metadata of the achievement configuration with the given ID. |
| [insert](/games/services/publishing/api/achievementConfigurations/insert) | `POST  /applications/applicationId/achievements` | Insert a new achievement configuration in this application. |
| [list](/games/services/publishing/api/achievementConfigurations/list) | `GET  /applications/applicationId/achievements` | Returns a list of the achievement configurations in this application. |
| [update](/games/services/publishing/api/achievementConfigurations/update) | `PUT  /achievements/achievementId` | Update the metadata of the achievement configuration with the given ID. |

## ImageConfigurations

For ImageConfigurations Resource details, see the [resource representation](/games/services/publishing/api/imageConfigurations#resource) page.

| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to https://www.googleapis.com/games/v1configuration, unless otherwise noted | | |
| [upload](/games/services/publishing/api/imageConfigurations/upload) | `POST https://www.googleapis.com/upload/games/v1configuration/images/resourceId/imageType/imageType` | **Deprecated:** This API is deprecated and is being removed, so you shouldn't use it. Attempting to use this API causes errors. Uploads an image for a resource with the given ID and image type. |

## LeaderboardConfigurations

For LeaderboardConfigurations Resource details, see the [resource representation](/games/services/publishing/api/leaderboardConfigurations#resource) page.

| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to https://www.googleapis.com/games/v1configuration, unless otherwise noted | | |
| [delete](/games/services/publishing/api/leaderboardConfigurations/delete) | `DELETE  /leaderboards/leaderboardId` | Delete the leaderboard configuration with the given ID. |
| [get](/games/services/publishing/api/leaderboardConfigurations/get) | `GET  /leaderboards/leaderboardId` | Retrieves the metadata of the leaderboard configuration with the given ID. |
| [insert](/games/services/publishing/api/leaderboardConfigurations/insert) | `POST  /applications/applicationId/leaderboards` | Insert a new leaderboard configuration in this application. |
| [list](/games/services/publishing/api/leaderboardConfigurations/list) | `GET  /applications/applicationId/leaderboards` | Returns a list of the leaderboard configurations in this application. |
| [update](/games/services/publishing/api/leaderboardConfigurations/update) | `PUT  /leaderboards/leaderboardId` | Update the metadata of the leaderboard configuration with the given ID. |