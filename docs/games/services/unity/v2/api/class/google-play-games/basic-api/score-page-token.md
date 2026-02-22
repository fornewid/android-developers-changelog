---
title: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/score-page-token
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/score-page-token
source: md.txt
---

# GooglePlayGames.BasicApi.ScorePageToken Class Reference

# GooglePlayGames.BasicApi.ScorePageToken

Score page token.

## Summary

This holds the internal token used to page through the score pages. The id, collection, and timespan are added as a convenience, and not actually part of the page token returned from the SDK.

|                                                                                                                                                                                                                                  ### Properties                                                                                                                                                                                                                                  ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Collection](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/score-page-token#class_google_play_games_1_1_basic_api_1_1_score_page_token_1a1eb75c47667e76deedb31d83d4225e3c)    | [LeaderboardCollection](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1a33fac2add308ad7414106822f66bc681) Gets the collection type of the leaderboard.  |
| [Direction](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/score-page-token#class_google_play_games_1_1_basic_api_1_1_score_page_token_1a5e88241ce3b5eca9921b8d593118d15e)     | [ScorePageDirection](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1a41534fba1862817cf8000c1711c1306f) Gets the direction of the score page navigation. |
| [LeaderboardId](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/score-page-token#class_google_play_games_1_1_basic_api_1_1_score_page_token_1a91837b7f2682b55701b9f58e15fdaf55) | `string` Gets the leaderboard ID associated with this token.                                                                                                                                                                                        |
| [TimeSpan](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/score-page-token#class_google_play_games_1_1_basic_api_1_1_score_page_token_1a08e4f8654bbe0bc73e76a647d3c56164)      | [LeaderboardTimeSpan](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1a8d9a7be92fea2b7a31420b073558fbce) Gets the timespan of the leaderboard.           |

## Properties

### Collection

```c#
LeaderboardCollection Collection
```  
Gets the collection type of the leaderboard.

For example, public or social.  

### Direction

```c#
ScorePageDirection Direction
```  
Gets the direction of the score page navigation.

For example, forward or backward.  

### LeaderboardId

```c#
string LeaderboardId
```  
Gets the leaderboard ID associated with this token.  

### TimeSpan

```c#
LeaderboardTimeSpan TimeSpan
```  
Gets the timespan of the leaderboard.

For example, daily or all-time.