---
title: https://developer.android.com/games/services/publishing/api
url: https://developer.android.com/games/services/publishing/api
source: md.txt
---

# API Reference

This API reference is organized by resource type. Each resource type has one or more data representations and one or more methods.

## Resource types

1. [AchievementConfigurations](https://developer.android.com/games/services/publishing/api#AchievementConfigurations)
2. [ImageConfigurations](https://developer.android.com/games/services/publishing/api#ImageConfigurations)
3. [LeaderboardConfigurations](https://developer.android.com/games/services/publishing/api#LeaderboardConfigurations)

## AchievementConfigurations

For AchievementConfigurations Resource details, see the[resource representation](https://developer.android.com/games/services/publishing/api/achievementConfigurations#resource)page.

|                                                 Method                                                 |                                         HTTP request                                         |                                Description                                 |
|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| URIs relative to https://www.googleapis.com/games/v1configuration, unless otherwise noted                                                                                                                                                                                        |||
| [delete](https://developer.android.com/games/services/publishing/api/achievementConfigurations/delete) | `DELETE /achievements/`<var class="apiparam" translate="no">achievementId</var>              | Delete the achievement configuration with the given ID.                    |
| [get](https://developer.android.com/games/services/publishing/api/achievementConfigurations/get)       | `GET /achievements/`<var class="apiparam" translate="no">achievementId</var>                 | Retrieves the metadata of the achievement configuration with the given ID. |
| [insert](https://developer.android.com/games/services/publishing/api/achievementConfigurations/insert) | `POST /applications/`<var class="apiparam" translate="no">applicationId</var>`/achievements` | Insert a new achievement configuration in this application.                |
| [list](https://developer.android.com/games/services/publishing/api/achievementConfigurations/list)     | `GET /applications/`<var class="apiparam" translate="no">applicationId</var>`/achievements`  | Returns a list of the achievement configurations in this application.      |
| [update](https://developer.android.com/games/services/publishing/api/achievementConfigurations/update) | `PUT /achievements/`<var class="apiparam" translate="no">achievementId</var>                 | Update the metadata of the achievement configuration with the given ID.    |

## ImageConfigurations

For ImageConfigurations Resource details, see the[resource representation](https://developer.android.com/games/services/publishing/api/imageConfigurations#resource)page.

|                                              Method                                              |                                                                                          HTTP request                                                                                          |                                                                                            Description                                                                                             |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| URIs relative to https://www.googleapis.com/games/v1configuration, unless otherwise noted                                                                                                                                                                                                                                                                                                                                                                                                            |||
| [upload](https://developer.android.com/games/services/publishing/api/imageConfigurations/upload) | `POST` `https://www.googleapis.com/upload/games/v1configuration/images/`<var class="apiparam" translate="no">resourceId</var>`/imageType/`<var class="apiparam" translate="no">imageType</var> | | **Deprecated:**This API is deprecated and is being removed, so you shouldn't use it. Attempting to use this API causes errors. Uploads an image for a resource with the given ID and image type. |

## LeaderboardConfigurations

For LeaderboardConfigurations Resource details, see the[resource representation](https://developer.android.com/games/services/publishing/api/leaderboardConfigurations#resource)page.

|                                                 Method                                                 |                                         HTTP request                                         |                                Description                                 |
|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| URIs relative to https://www.googleapis.com/games/v1configuration, unless otherwise noted                                                                                                                                                                                        |||
| [delete](https://developer.android.com/games/services/publishing/api/leaderboardConfigurations/delete) | `DELETE /leaderboards/`<var class="apiparam" translate="no">leaderboardId</var>              | Delete the leaderboard configuration with the given ID.                    |
| [get](https://developer.android.com/games/services/publishing/api/leaderboardConfigurations/get)       | `GET /leaderboards/`<var class="apiparam" translate="no">leaderboardId</var>                 | Retrieves the metadata of the leaderboard configuration with the given ID. |
| [insert](https://developer.android.com/games/services/publishing/api/leaderboardConfigurations/insert) | `POST /applications/`<var class="apiparam" translate="no">applicationId</var>`/leaderboards` | Insert a new leaderboard configuration in this application.                |
| [list](https://developer.android.com/games/services/publishing/api/leaderboardConfigurations/list)     | `GET /applications/`<var class="apiparam" translate="no">applicationId</var>`/leaderboards`  | Returns a list of the leaderboard configurations in this application.      |
| [update](https://developer.android.com/games/services/publishing/api/leaderboardConfigurations/update) | `PUT /leaderboards/`<var class="apiparam" translate="no">leaderboardId</var>                 | Update the metadata of the leaderboard configuration with the given ID.    |