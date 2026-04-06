---
title: GooglePlayGames.BasicApi.DummyClient Class Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# GooglePlayGames.BasicApi.DummyClient

Dummy client used in Editor.

## Summary

Google Play Game Services are not supported in the Editor environment, so this client is used as a placeholder.

### Inheritance

Inherits from: [GooglePlayGames.BasicApi.IPlayGamesClient](/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client)

| Public functions | |
| --- | --- |
| `AskForLoadFriendsResolution(Action< UIStatus > callback)` | `void`  Requests the load friends resolution UI. |
| `Authenticate(Action< SignInStatus > callback)` | `void`  Authenticates the user. |
| `GetEventsClient()` | `GooglePlayGames.BasicApi.Events.IEventsClient`  Retrieves the events client. |
| `GetFriends()` | `IUserProfile[]`  Retrieves the list of friends for the current user. |
| `GetFriendsListVisibility(bool forceReload, Action< FriendsListVisibilityStatus > callback)` | `void`  Retrieves the visibility status of the friends list. |
| `GetLastLoadFriendsStatus()` | `LoadFriendsStatus`  Retrieves the last load friends status. |
| `GetPlayerStats(Action< CommonStatusCodes, PlayerStats > callback)` | `void`  Retrieves the player statistics. |
| `GetSavedGameClient()` | `SavedGame.ISavedGameClient`  Retrieves the saved game client. |
| `GetUserDisplayName()` | `string`  Retrieves the user's display name. |
| `GetUserId()` | `string`  Retrieves the user ID. |
| `GetUserImageUrl()` | `string`  Retrieves the user's image URL. |
| `IncrementAchievement(string achId, int steps, Action< bool > callback)` | `void`  Increments the specified achievement by a number of steps. |
| `IsAuthenticated()` | `bool`  Checks if the user is authenticated. |
| `LeaderboardMaxResults()` | `int`  Retrieves the maximum number of leaderboard results that can be loaded. |
| `LoadAchievements(Action< Achievement[]> callback)` | `void`  Loads achievements for the current user. |
| `LoadFriends(int pageSize, bool forceReload, Action< LoadFriendsStatus > callback)` | `void`  Loads friends with paging options. |
| `LoadFriends(Action< bool > callback)` | `void`  Loads friends with a simple boolean flag indicating success or failure. |
| `LoadMoreFriends(int pageSize, Action< LoadFriendsStatus > callback)` | `void`  Loads additional friends if available. |
| `LoadMoreScores(ScorePageToken token, int rowCount, Action< LeaderboardScoreData > callback)` | `void`  Loads more leaderboard scores based on the provided pagination token. |
| `LoadScores(string leaderboardId, LeaderboardStart start, int rowCount, LeaderboardCollection collection, LeaderboardTimeSpan timeSpan, Action< LeaderboardScoreData > callback)` | `void`  Loads the leaderboard scores based on the specified parameters. |
| `LoadUsers(string[] userIds, Action< IUserProfile[]> callback)` | `void`  Loads user profiles for the given user IDs. |
| `ManuallyAuthenticate(Action< SignInStatus > callback)` | `void`  Manually authenticates the user. |
| `RequestRecallAccessToken(Action< RecallAccess > callback)` | `void`  Requests recall of the access token. |
| `RequestServerSideAccess(bool forceRefreshToken, Action< string > callback)` | `void`  Requests server-side access with a refresh token. |
| `RequestServerSideAccess(bool forceRefreshToken, List< AuthScope > scopes, Action< AuthResponse > callback)` | `void`  Requests server-side access with specific scopes. |
| `RevealAchievement(string achId, Action< bool > callback)` | `void`  Reveals the specified achievement. |
| `SetStepsAtLeast(string achId, int steps, Action< bool > callback)` | `void`  Sets the steps of the specified achievement to at least a certain number. |
| `ShowAchievementsUI(Action< UIStatus > callback)` | `void`  Displays the achievements UI. |
| `ShowCompareProfileWithAlternativeNameHintsUI(string userId, string otherPlayerInGameName, string currentPlayerInGameName, Action< UIStatus > callback)` | `void`  Displays the compare profile UI for a player. |
| `ShowLeaderboardUI(string leaderboardId, LeaderboardTimeSpan span, Action< UIStatus > callback)` | `void`  Displays the leaderboard UI for a specific leaderboard. |
| `SubmitScore(string leaderboardId, long score, Action< bool > callback)` | `void`  Submits a score to a specific leaderboard. |
| `SubmitScore(string leaderboardId, long score, string metadata, Action< bool > callback)` | `void`  Submits a score with additional metadata to a specific leaderboard. |
| `UnlockAchievement(string achId, Action< bool > callback)` | `void`  Unlocks the specified achievement. |

## Public functions

### AskForLoadFriendsResolution

```
void AskForLoadFriendsResolution(
  Action< UIStatus > callback
)
```

Requests the load friends resolution UI.

Details | || Parameters | |  |  | | --- | --- | | `callback` | Callback to handle the UI status. | |

### Authenticate

```
void Authenticate(
  Action< SignInStatus > callback
)
```

Authenticates the user.

Details | || Parameters | |  |  | | --- | --- | | `callback` | Callback to handle the sign-in status. | |

### GetEventsClient

```
GooglePlayGames.BasicApi.Events.IEventsClient GetEventsClient()
```

Retrieves the events client.

Details | || **Returns** | Returns null since no events client is available. |

### GetFriends

```
IUserProfile[] GetFriends()
```

Retrieves the list of friends for the current user.

Details | || **Returns** | Returns an empty array since no friends are loaded. |

### GetFriendsListVisibility

```
void GetFriendsListVisibility(
  bool forceReload,
  Action< FriendsListVisibilityStatus > callback
)
```

Retrieves the visibility status of the friends list.

Details | || Parameters | |  |  | | --- | --- | | `forceReload` | Flag to force reload the friends list visibility. | | `callback` | Callback to handle the friends list visibility status. | |

### GetLastLoadFriendsStatus

```
LoadFriendsStatus GetLastLoadFriendsStatus()
```

Retrieves the last load friends status.

Details | || **Returns** | Returns the last known load friends status. |

### GetPlayerStats

```
void GetPlayerStats(
  Action< CommonStatusCodes, PlayerStats > callback
)
```

Retrieves the player statistics.

Details | || Parameters | |  |  | | --- | --- | | `callback` | Callback to handle the player stats response. | |

### GetSavedGameClient

```
SavedGame.ISavedGameClient GetSavedGameClient()
```

Retrieves the saved game client.

Details | || **Returns** | Returns null since no saved game client is available. |

### GetUserDisplayName

```
string GetUserDisplayName()
```

Retrieves the user's display name.

Details | || **Returns** | Returns a dummy display name. |

### GetUserId

```
string GetUserId()
```

Retrieves the user ID.

Details | || **Returns** | Returns a dummy user ID. |

### GetUserImageUrl

```
string GetUserImageUrl()
```

Retrieves the user's image URL.

Details | || **Returns** | Returns null since no image is available. |

### IncrementAchievement

```
void IncrementAchievement(
  string achId,
  int steps,
  Action< bool > callback
)
```

Increments the specified achievement by a number of steps.

Details | || Parameters | |  |  | | --- | --- | | `achId` | The achievement ID to increment. | | `steps` | The number of steps to increment the achievement. | | `callback` | Callback to handle the increment result. | |

### IsAuthenticated

```
bool IsAuthenticated()
```

Checks if the user is authenticated.

Details | || **Returns** | Returns false indicating user is not authenticated. |

### LeaderboardMaxResults

```
int LeaderboardMaxResults()
```

Retrieves the maximum number of leaderboard results that can be loaded.

Details | || **Returns** | Returns the maximum number of leaderboard results. |

### LoadAchievements

```
void LoadAchievements(
  Action< Achievement[]> callback
)
```

Loads achievements for the current user.

Details | || Parameters | |  |  | | --- | --- | | `callback` | Callback to handle the achievement response. | |

### LoadFriends

```
void LoadFriends(
  int pageSize,
  bool forceReload,
  Action< LoadFriendsStatus > callback
)
```

Loads friends with paging options.

Details | || Parameters | |  |  | | --- | --- | | `pageSize` | The number of friends to load per page. | | `forceReload` | Flag to force reload of the friends list. | | `callback` | Callback to handle the load friends status. | |

### LoadFriends

```
void LoadFriends(
  Action< bool > callback
)
```

Loads friends with a simple boolean flag indicating success or failure.

Details | || Parameters | |  |  | | --- | --- | | `callback` | Callback to handle the load result. | |

### LoadMoreFriends

```
void LoadMoreFriends(
  int pageSize,
  Action< LoadFriendsStatus > callback
)
```

Loads additional friends if available.

Details | || Parameters | |  |  | | --- | --- | | `pageSize` | The number of additional friends to load. | | `callback` | Callback to handle the load friends status. | |

### LoadMoreScores

```
void LoadMoreScores(
  ScorePageToken token,
  int rowCount,
  Action< LeaderboardScoreData > callback
)
```

Loads more leaderboard scores based on the provided pagination token.

Details | || Parameters | |  |  | | --- | --- | | `token` | The token used for pagination. | | `rowCount` | The number of scores to load. | | `callback` | Callback to handle the leaderboard score data. | |

### LoadScores

```
void LoadScores(
  string leaderboardId,
  LeaderboardStart start,
  int rowCount,
  LeaderboardCollection collection,
  LeaderboardTimeSpan timeSpan,
  Action< LeaderboardScoreData > callback
)
```

Loads the leaderboard scores based on the specified parameters.

Details | || Parameters | |  |  | | --- | --- | | `leaderboardId` | The ID of the leaderboard to load scores from. | | `start` | The start position for loading scores. | | `rowCount` | The number of scores to load. | | `collection` | The collection type (e.g., public or social). | | `timeSpan` | The time span for the leaderboard scores. | | `callback` | Callback to handle the leaderboard score data. | |

### LoadUsers

```
void LoadUsers(
  string[] userIds,
  Action< IUserProfile[]> callback
)
```

Loads user profiles for the given user IDs.

Details | || Parameters | |  |  | | --- | --- | | `userIds` | List of user IDs. | | `callback` | Callback to handle the user profile response. | |

### ManuallyAuthenticate

```
void ManuallyAuthenticate(
  Action< SignInStatus > callback
)
```

Manually authenticates the user.

Details | || Parameters | |  |  | | --- | --- | | `callback` | Callback to handle the sign-in status. | |

### RequestRecallAccessToken

```
void RequestRecallAccessToken(
  Action< RecallAccess > callback
)
```

Requests recall of the access token.

Details | || Parameters | |  |  | | --- | --- | | `callback` | Callback to handle the recall response. | |

### RequestServerSideAccess

```
void RequestServerSideAccess(
  bool forceRefreshToken,
  Action< string > callback
)
```

Requests server-side access with a refresh token.

Details | || Parameters | |  |  | | --- | --- | | `forceRefreshToken` | Flag to force refresh the token. | | `callback` | Callback to handle the response. | |

### RequestServerSideAccess

```
void RequestServerSideAccess(
  bool forceRefreshToken,
  List< AuthScope > scopes,
  Action< AuthResponse > callback
)
```

Requests server-side access with specific scopes.

Details | || Parameters | |  |  | | --- | --- | | `forceRefreshToken` | Flag to force refresh the token. | | `scopes` | List of requested authorization scopes. | | `callback` | Callback to handle the response. | |

### RevealAchievement

```
void RevealAchievement(
  string achId,
  Action< bool > callback
)
```

Reveals the specified achievement.

Details | || Parameters | |  |  | | --- | --- | | `achId` | The achievement ID to reveal. | | `callback` | Callback to handle the reveal result. | |

### SetStepsAtLeast

```
void SetStepsAtLeast(
  string achId,
  int steps,
  Action< bool > callback
)
```

Sets the steps of the specified achievement to at least a certain number.

Details | || Parameters | |  |  | | --- | --- | | `achId` | The achievement ID to update. | | `steps` | The number of steps to set. | | `callback` | Callback to handle the result of setting the steps. | |

### ShowAchievementsUI

```
void ShowAchievementsUI(
  Action< UIStatus > callback
)
```

Displays the achievements UI.

Details | || Parameters | |  |  | | --- | --- | | `callback` | Callback to handle the UI status. | |

### ShowCompareProfileWithAlternativeNameHintsUI

```
void ShowCompareProfileWithAlternativeNameHintsUI(
  string userId,
  string otherPlayerInGameName,
  string currentPlayerInGameName,
  Action< UIStatus > callback
)
```

Displays the compare profile UI for a player.

Details | || Parameters | |  |  | | --- | --- | | `userId` | The user ID of the player to compare. | | `otherPlayerInGameName` | The in-game name of the other player. | | `currentPlayerInGameName` | The in-game name of the current player. | | `callback` | Callback to handle the UI status. | |

### ShowLeaderboardUI

```
void ShowLeaderboardUI(
  string leaderboardId,
  LeaderboardTimeSpan span,
  Action< UIStatus > callback
)
```

Displays the leaderboard UI for a specific leaderboard.

Details | || Parameters | |  |  | | --- | --- | | `leaderboardId` | The ID of the leaderboard. | | `span` | The time span for the leaderboard. | | `callback` | Callback to handle the UI status. | |

### SubmitScore

```
void SubmitScore(
  string leaderboardId,
  long score,
  Action< bool > callback
)
```

Submits a score to a specific leaderboard.

Details | || Parameters | |  |  | | --- | --- | | `leaderboardId` | The ID of the leaderboard. | | `score` | The score to submit. | | `callback` | Callback to handle the score submission result. | |

### SubmitScore

```
void SubmitScore(
  string leaderboardId,
  long score,
  string metadata,
  Action< bool > callback
)
```

Submits a score with additional metadata to a specific leaderboard.

Details | || Parameters | |  |  | | --- | --- | | `leaderboardId` | The ID of the leaderboard. | | `score` | The score to submit. | | `metadata` | Additional metadata to submit with the score. | | `callback` | Callback to handle the score submission result. | |

### UnlockAchievement

```
void UnlockAchievement(
  string achId,
  Action< bool > callback
)
```

Unlocks the specified achievement.

Details | || Parameters | |  |  | | --- | --- | | `achId` | The achievement ID to unlock. | | `callback` | Callback to handle the unlock result. | |