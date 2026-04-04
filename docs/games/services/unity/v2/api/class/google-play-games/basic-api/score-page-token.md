---
title: GooglePlayGames.BasicApi.ScorePageToken Class Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/score-page-token
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# GooglePlayGames.BasicApi.ScorePageToken

Score page token.

## Summary

This holds the internal token used to page through the score pages. The id, collection, and timespan are added as a convenience, and not actually part of the page token returned from the SDK.

| Properties | |
| --- | --- |
| `Collection` | `LeaderboardCollection`  Gets the collection type of the leaderboard. |
| `Direction` | `ScorePageDirection`  Gets the direction of the score page navigation. |
| `LeaderboardId` | `string`  Gets the leaderboard ID associated with this token. |
| `TimeSpan` | `LeaderboardTimeSpan`  Gets the timespan of the leaderboard. |

## Properties

### Collection

```
LeaderboardCollection Collection
```

Gets the collection type of the leaderboard.

For example, public or social.

### Direction

```
ScorePageDirection Direction
```

Gets the direction of the score page navigation.

For example, forward or backward.

### LeaderboardId

```
string LeaderboardId
```

Gets the leaderboard ID associated with this token.

### TimeSpan

```
LeaderboardTimeSpan TimeSpan
```

Gets the timespan of the leaderboard.

For example, daily or all-time.