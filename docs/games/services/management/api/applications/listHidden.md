---
title: https://developer.android.com/games/services/management/api/applications/listHidden
url: https://developer.android.com/games/services/management/api/applications/listHidden
source: md.txt
---

**Requires [authorization](https://developer.android.com/games/services/management/api/applications/listHidden#auth)**

Get the list of players hidden from the given application. This method is only available to user accounts for your developer console.

## Request

### HTTP request

```
GET https://www.googleapis.com/games/v1management/applications/applicationId/players/hidden
```

### Parameters

| Parameter name | Value | Description |
|---|---|---|
| **Path parameters** |||
| `applicationId` | `string` | The application ID from the Google Play Console. |
| **Optional query parameters** |||
| `maxResults` | `integer` | The maximum number of player resources to return in the response, used for paging. For any response, the actual number of player resources returned may be less than the specified `maxResults`. Acceptable values are `1` to `15`, inclusive. |
| `pageToken` | `string` | The token returned by the previous request. |

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
  "kind": "gamesManagement#hiddenPlayerList",
  "nextPageToken": string,
  "items": [
    {
      "kind": "gamesManagement#hiddenPlayer",
      "player": {
        "kind": "gamesManagement#player",
        "playerId": string,
        "displayName": string,
        "avatarImageUrl": string,
        "lastPlayedWith": {
          "timeMillis": long,
          "autoMatched": boolean
        },
        "name": {
          "familyName": string,
          "givenName": string
        },
        "experienceInfo": {
          "currentExperiencePoints": long,
          "lastLevelUpTimestampMillis": long,
          "currentLevel": {
            "level": integer,
            "minExperiencePoints": long,
            "maxExperiencePoints": long
          },
          "nextLevel": {
            "level": integer,
            "minExperiencePoints": long,
            "maxExperiencePoints": long
          }
        },
        "title": string
      },
      "hiddenTimeMillis": long
    }
  ]
}
```

| Property name | Value | Description | Notes |
|---|---|---|---|
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#hiddenPlayerList`. |   |
| `nextPageToken` | `string` | The pagination token for the next page of results. |   |
| `items[]` | `list` | The players. |   |
| `items[].kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#hiddenPlayer`. |   |
| `items[].player` | `nested object` | The player information. |   |
| `items[].player.kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesManagement#player`. |   |
| `items[].player.playerId` | `string` | The ID of the player. |   |
| `items[].player.displayName` | `string` | The name to display for the player. |   |
| `items[].player.avatarImageUrl` | `string` | The base URL for the image that represents the player. |   |
| `items[].player.lastPlayedWith` | `nested object` | Details about the last time this player played a multiplayer game with the currently authenticated player. Populated for PLAYED_WITH player collection members. |   |
| `items[].player.lastPlayedWith.timeMillis` | `long` | The last time the player played the game in milliseconds since the epoch in UTC. |   |
| `items[].player.lastPlayedWith.autoMatched` | `boolean` | True if the player was auto-matched with the currently authenticated user. |   |
| `items[].player.name` | `object` | An object representation of the individual components of the player's name. For some players, these fields may not be present. |   |
| `items[].player.name.familyName` | `string` | The family name of this player. In some places, this is known as the last name. |   |
| `items[].player.name.givenName` | `string` | The given name of this player. In some places, this is known as the first name. |   |
| `items[].player.experienceInfo` | `nested object` | An object to represent Play Game experience information for the player. |   |
| `items[].player.experienceInfo.currentExperiencePoints` | `long` | The current number of experience points for the player. |   |
| `items[].player.experienceInfo.lastLevelUpTimestampMillis` | `long` | The timestamp when the player was leveled up, in millis since Unix epoch UTC. |   |
| `items[].player.experienceInfo.currentLevel` | `nested object` | The current level of the player. |   |
| `items[].player.experienceInfo.currentLevel.level` | `integer` | The level for the user. |   |
| `items[].player.experienceInfo.currentLevel.minExperiencePoints` | `long` | The minimum experience points for this level. |   |
| `items[].player.experienceInfo.currentLevel.maxExperiencePoints` | `long` | The maximum experience points for this level. |   |
| `items[].player.experienceInfo.nextLevel` | `nested object` | The next level of the player. If the current level is the maximum level, this should be same as the current level. |   |
| `items[].player.experienceInfo.nextLevel.level` | `integer` | The level for the user. |   |
| `items[].player.experienceInfo.nextLevel.minExperiencePoints` | `long` | The minimum experience points for this level. |   |
| `items[].player.experienceInfo.nextLevel.maxExperiencePoints` | `long` | The maximum experience points for this level. |   |
| `items[].player.title` | `string` | The player's title rewarded for their game activities. |   |
| `items[].hiddenTimeMillis` | `long` | The time this player was hidden. |   |