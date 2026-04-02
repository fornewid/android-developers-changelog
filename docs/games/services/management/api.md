---
title: https://developer.android.com/games/services/management/api
url: https://developer.android.com/games/services/management/api
source: md.txt
---

# API Reference

This API reference is organized by resource type. Each resource type has one or more data representations and one or more methods.

## Resource types

1. [Achievements](https://developer.android.com/games/services/management/api#Achievements)
2. [Applications](https://developer.android.com/games/services/management/api#Applications)
3. [Events](https://developer.android.com/games/services/management/api#Events)
4. [Players](https://developer.android.com/games/services/management/api#Players)
5. [Rooms](https://developer.android.com/games/services/management/api#Rooms)
6. [Scores](https://developer.android.com/games/services/management/api#Scores)
7. [TurnBasedMatches](https://developer.android.com/games/services/management/api#TurnBasedMatches)

## Achievements

For Achievements Resource details, see the[resource representation](https://developer.android.com/games/services/management/api/achievements#resource)page.

|                                                              Method                                                               |                                            HTTP request                                            |                                                                                Description                                                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| URIs relative to https://www.googleapis.com/games/v1management, unless otherwise noted                                                                                                                                                                                                                                                                                                                            |||
| [reset](https://developer.android.com/games/services/management/api/achievements/reset)                                           | `POST /achievements/`<var class="apiparam" translate="no">achievementId</var>`/reset`              | Resets the achievement with the given ID for the currently authenticated player. This method is only accessible to whitelisted tester accounts for your application.       |
| [resetAll](https://developer.android.com/games/services/management/api/achievements/resetAll)                                     | `POST /achievements/reset`                                                                         | Resets all achievements for the currently authenticated player for your application. This method is only accessible to whitelisted tester accounts for your application.   |
| [resetForAllPlayers](https://developer.android.com/games/services/management/api/achievements/resetForAllPlayers)                 | `POST /achievements/`<var class="apiparam" translate="no">achievementId</var>`/resetForAllPlayers` | Resets the achievement with the given ID for all players. This method is only available to user accounts for your developer console. Only draft achievements can be reset. |
| [resetAllForAllPlayers](https://developer.android.com/games/services/management/api/achievements/resetAllForAllPlayers)           | `POST /achievements/resetAllForAllPlayers`                                                         | Resets all draft achievements for all players. This method is only available to user accounts for your developer console.                                                  |
| [resetMultipleForAllPlayers](https://developer.android.com/games/services/management/api/achievements/resetMultipleForAllPlayers) | `POST /achievements/resetMultipleForAllPlayers`                                                    | Resets achievements with the given IDs for all players. This method is only available to user accounts for your developer console. Only draft achievements may be reset.   |

## Applications

For Applications Resource details, see the[resource representation](https://developer.android.com/games/services/management/api/applications#resource)page.

|                                              Method                                               |                                         HTTP request                                          |                                                              Description                                                              |
|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| URIs relative to https://www.googleapis.com/games/v1management, unless otherwise noted                                                                                                                                                                                                                                                  |||
| [listHidden](https://developer.android.com/games/services/management/api/applications/listHidden) | `GET /applications/`<var class="apiparam" translate="no">applicationId</var>`/players/hidden` | Get the list of players hidden from the given application. This method is only available to user accounts for your developer console. |

## Events

For Events Resource details, see the[resource representation](https://developer.android.com/games/services/management/api/events#resource)page.

|                                                           Method                                                            |                                      HTTP request                                      |                                                                                      Description                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| URIs relative to https://www.googleapis.com/games/v1management, unless otherwise noted                                                                                                                                                                                                                                                                                                                     |||
| [reset](https://developer.android.com/games/services/management/api/events/reset)                                           | `POST /events/`<var class="apiparam" translate="no">eventId</var>`/reset`              | Resets all player progress on the event with the given ID for the currently authenticated player. This method is only accessible to whitelisted tester accounts for your application. |
| [resetAll](https://developer.android.com/games/services/management/api/events/resetAll)                                     | `POST /events/reset`                                                                   | Resets all player progress on all events for the currently authenticated player. This method is only accessible to whitelisted tester accounts for your application.                  |
| [resetForAllPlayers](https://developer.android.com/games/services/management/api/events/resetForAllPlayers)                 | `POST /events/`<var class="apiparam" translate="no">eventId</var>`/resetForAllPlayers` | Resets the event with the given ID for all players. This method is only available to user accounts for your developer console. Only draft events can be reset.                        |
| [resetAllForAllPlayers](https://developer.android.com/games/services/management/api/events/resetAllForAllPlayers)           | `POST /events/resetAllForAllPlayers`                                                   | Resets all draft events for all players. This method is only available to user accounts for your developer console.                                                                   |
| [resetMultipleForAllPlayers](https://developer.android.com/games/services/management/api/events/resetMultipleForAllPlayers) | `POST /events/resetMultipleForAllPlayers`                                              | Resets events with the given IDs for all players. This method is only available to user accounts for your developer console. Only draft events may be reset.                          |

## Players

For Players Resource details, see the[resource representation](https://developer.android.com/games/services/management/api/players#resource)page.

|                                        Method                                        |                                                                     HTTP request                                                                     |                                                                                         Description                                                                                         |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| URIs relative to https://www.googleapis.com/games/v1management, unless otherwise noted                                                                                                                                                                                                                                                                                                                                                  |||
| [hide](https://developer.android.com/games/services/management/api/players/hide)     | `POST /applications/`<var class="apiparam" translate="no">applicationId</var>`/players/hidden/`<var class="apiparam" translate="no">playerId</var>   | Hide the given player's leaderboard scores from the given application. This method is only available to user accounts for your developer console.                                           |
| [unhide](https://developer.android.com/games/services/management/api/players/unhide) | `DELETE /applications/`<var class="apiparam" translate="no">applicationId</var>`/players/hidden/`<var class="apiparam" translate="no">playerId</var> | Unhide the given player's leaderboard scores from the given application. This method is only available to user accounts for your developer console and may take up to a day to take effect. |

## Rooms

For Rooms Resource details, see the[resource representation](https://developer.android.com/games/services/management/api/rooms#resource)page.

|                                                   Method                                                   |           HTTP request           |                                                                                     Description                                                                                      |
|------------------------------------------------------------------------------------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| URIs relative to https://www.googleapis.com/games/v1management, unless otherwise noted                                                                                                                                                                                                                                             |||
| [reset](https://developer.android.com/games/services/management/api/rooms/reset)                           | `POST /rooms/reset`              | Reset all rooms for the currently authenticated player for your application. This method is only accessible to whitelisted tester accounts for your application.                     |
| [resetForAllPlayers](https://developer.android.com/games/services/management/api/rooms/resetForAllPlayers) | `POST /rooms/resetForAllPlayers` | Deletes rooms where the only room participants are from whitelisted tester accounts for your application. This method is only available to user accounts for your developer console. |

## Scores

For Scores Resource details, see the[resource representation](https://developer.android.com/games/services/management/api/scores#resource)page.

|                                                           Method                                                            |                                               HTTP request                                                |                                                                                       Description                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| URIs relative to https://www.googleapis.com/games/v1management, unless otherwise noted                                                                                                                                                                                                                                                                                                                                          |||
| [reset](https://developer.android.com/games/services/management/api/scores/reset)                                           | `POST /leaderboards/`<var class="apiparam" translate="no">leaderboardId</var>`/scores/reset`              | Resets scores for the leaderboard with the given ID for the currently authenticated player. This method is only accessible to whitelisted tester accounts for your application.         |
| [resetForAllPlayers](https://developer.android.com/games/services/management/api/scores/resetForAllPlayers)                 | `POST /leaderboards/`<var class="apiparam" translate="no">leaderboardId</var>`/scores/resetForAllPlayers` | Resets scores for the leaderboard with the given ID for all players. This method is only available to user accounts for your developer console. Only draft leaderboards can be reset.   |
| [resetAll](https://developer.android.com/games/services/management/api/scores/resetAll)                                     | `POST /scores/reset`                                                                                      | Resets all scores for all leaderboards for the currently authenticated players. This method is only accessible to whitelisted tester accounts for your application.                     |
| [resetAllForAllPlayers](https://developer.android.com/games/services/management/api/scores/resetAllForAllPlayers)           | `POST /scores/resetAllForAllPlayers`                                                                      | Resets scores for all draft leaderboards for all players. This method is only available to user accounts for your developer console.                                                    |
| [resetMultipleForAllPlayers](https://developer.android.com/games/services/management/api/scores/resetMultipleForAllPlayers) | `POST /scores/resetMultipleForAllPlayers`                                                                 | Resets scores for the leaderboards with the given IDs for all players. This method is only available to user accounts for your developer console. Only draft leaderboards may be reset. |

## TurnBasedMatches

For TurnBasedMatches Resource details, see the[resource representation](https://developer.android.com/games/services/management/api/turnBasedMatches#resource)page.

|                                                        Method                                                         |                HTTP request                 |                                                                                            Description                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| URIs relative to https://www.googleapis.com/games/v1management, unless otherwise noted                                                                                                                                                                                                                                                                                 |||
| [reset](https://developer.android.com/games/services/management/api/turnBasedMatches/reset)                           | `POST /turnbasedmatches/reset`              | Reset all turn-based match data for a user. This method is only accessible to whitelisted tester accounts for your application.                                                                    |
| [resetForAllPlayers](https://developer.android.com/games/services/management/api/turnBasedMatches/resetForAllPlayers) | `POST /turnbasedmatches/resetForAllPlayers` | Deletes turn-based matches where the only match participants are from whitelisted tester accounts for your application. This method is only available to user accounts for your developer console. |