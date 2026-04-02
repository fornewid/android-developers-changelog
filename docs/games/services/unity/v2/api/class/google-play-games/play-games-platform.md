---
title: GooglePlayGames.PlayGamesPlatform Class Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# GooglePlayGames.PlayGamesPlatform

Provides access to the Google Play Games platform.

## Summary

This is an implementation of UnityEngine.SocialPlatforms.ISocialPlatform. Activate this platform by calling the [Activate](/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1afc68980eb29743625ae7ea74c1e99327) method, then authenticate by calling the [Authenticate](/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a2743441943ae1a4f5916c47c6a93b0df) method. After authentication completes, you may call the other methods of this class. This is not a complete implementation of the ISocialPlatform interface. Methods lacking an implementation or whose behavior is at variance with the standard are noted as such.

### Inheritance

Inherits from: ISocialPlatform

| Properties | |
| --- | --- |
| `DebugLogEnabled` | `static bool`  Gets or sets a value indicating whether debug logs are enabled. |
| `Events` | `IEventsClient`  Gets the events client object. |
| `Instance` | `static PlayGamesPlatform`  Gets the singleton instance of the Play Games platform. |
| `Nearby` | `static INearbyConnectionClient`  Gets the nearby connection client. |
| `SavedGame` | `ISavedGameClient`  Gets the saved game client object. |
| `localUser` | `ILocalUser`  Gets the local user. |

| Public static functions | |
| --- | --- |
| `Activate()` | `PlayGamesPlatform`  Activates the Play Games platform as the implementation of Social.Active. |
| `InitializeNearby(Action< INearbyConnectionClient > callback)` | `void`  Initializes the nearby connection platform. |

| Public functions | |
| --- | --- |
| `AddIdMapping(string fromId, string toId)` | `void`  Specifies that the ID `fromId` should be implicitly replaced by `toId` on any calls that take a leaderboard or achievement ID. |
| `AskForLoadFriendsResolution(Action< UIStatus > callback)` | `void`  Shows the appropriate platform-specific friends sharing UI. |
| `Authenticate(Action< SignInStatus > callback)` | `void`  Returns the result of the automatic sign-in attempt. |
| `Authenticate(ILocalUser unused, Action< bool > callback)` | `void`  Provided for compatibility with ISocialPlatform. |
| `Authenticate(ILocalUser unused, Action< bool, string > callback)` | `void`  Provided for compatibility with ISocialPlatform. |
| `CreateAchievement()` | `IAchievement`  Creates an achievement object which may be subsequently used to report an achievement. |
| `CreateLeaderboard()` | `ILeaderboard`  Returns a leaderboard object that can be configured to load scores. |
| `GetFriendsListVisibility(bool forceReload, Action< FriendsListVisibilityStatus > callback)` | `void`  Returns if the user has allowed permission for the game to access the friends list. |
| `GetLastLoadFriendsStatus()` | `LoadFriendsStatus`  Gets status of the last call to load friends. |
| `GetLoading(ILeaderboard board)` | `bool`  Check if the leaderboard is currently loading. |
| `GetPlayerStats(Action< CommonStatusCodes, PlayerStats > callback)` | `void`  Gets the player stats. |
| `GetUserDisplayName()` | `string`  Returns the user's display name. |
| `GetUserId()` | `string`  Returns the user's Google ID. |
| `GetUserImageUrl()` | `string`  Returns the user's avatar URL if they have one. |
| `IncrementAchievement(string achievementID, int steps, Action< bool > callback)` | `void`  Increments an achievement. |
| `IsAuthenticated()` | `bool`  Determines whether the user is authenticated. |
| `LoadAchievementDescriptions(Action< IAchievementDescription[]> callback)` | `void`  Loads the Achievement descriptions. |
| `LoadAchievements(Action< IAchievement[]> callback)` | `void`  Loads the achievement state for the current user. |
| `LoadFriends(ILocalUser user, Action< bool > callback)` | `void`  Loads the friends that also play this game. |
| `LoadFriends(int pageSize, bool forceReload, Action< LoadFriendsStatus > callback)` | `void`  Loads the first page of the user's friends. |
| `LoadMoreFriends(int pageSize, Action< LoadFriendsStatus > callback)` | `void`  Loads the friends list page |
| `LoadMoreScores(ScorePageToken token, int rowCount, Action< LeaderboardScoreData > callback)` | `void`  Loads more scores. |
| `LoadScores(string leaderboardId, Action< IScore[]> callback)` | `void`  Loads the scores relative the player. |
| `LoadScores(string leaderboardId, LeaderboardStart start, int rowCount, LeaderboardCollection collection, LeaderboardTimeSpan timeSpan, Action< LeaderboardScoreData > callback)` | `void`  Loads the scores using the provided parameters. |
| `LoadScores(ILeaderboard board, Action< bool > callback)` | `void`  Loads the leaderboard based on the constraints in the leaderboard object. |
| `LoadUsers(string[] userIds, Action< IUserProfile[]> callback)` | `void`  Loads the users. |
| `ManuallyAuthenticate(Action< SignInStatus > callback)` | `void`  Manually requests that your game performs sign in with Play Games Services. |
| `ReportProgress(string achievementID, double progress, Action< bool > callback)` | `void`  Reports the progress of an achievement (reveal, unlock or increment). |
| `ReportScore(long score, string board, Action< bool > callback)` | `void`  Reports a score to a leaderboard. |
| `ReportScore(long score, string board, string metadata, Action< bool > callback)` | `void`  Submits the score for the currently signed-in player to the leaderboard associated with a specific id and metadata (such as something the player did to earn the score). |
| `RequestRecallAccess(Action< RecallAccess > callback)` | `void`  Requests access to the recall API. |
| `RequestServerSideAccess(bool forceRefreshToken, Action< string > callback)` | `void`  Requests server-side access to Player Games Services for the currently signed in player. |
| `RequestServerSideAccess(bool forceRefreshToken, List< AuthScope > scopes, Action< AuthResponse > callback)` | `void`  Requests server-side access to Player Games Services for the currently signed in player. |
| `RevealAchievement(string achievementID, Action< bool > callback)` | `void`  Reveals the achievement with the passed identifier. |
| `SetDefaultLeaderboardForUI(string lbid)` | `void`  Sets the default leaderboard for the leaderboard UI. |
| `SetStepsAtLeast(string achievementID, int steps, Action< bool > callback)` | `void`  Set an achievement to have at least the given number of steps completed. |
| `ShowAchievementsUI()` | `void`  Shows the standard Google Play Games achievements user interface, which allows the player to browse their achievements. |
| `ShowAchievementsUI(Action< UIStatus > callback)` | `void`  Shows the standard Google Play Games achievements user interface, which allows the player to browse their achievements. |
| `ShowCompareProfileWithAlternativeNameHintsUI(string userId, string otherPlayerInGameName, string currentPlayerInGameName, Action< UIStatus > callback)` | `void`  Shows the Player Profile UI for the given user identifier. |
| `ShowLeaderboardUI()` | `void`  Shows the standard Google Play Games leaderboards user interface, which allows the player to browse their leaderboards. |
| `ShowLeaderboardUI(string leaderboardId)` | `void`  Shows the standard Google Play Games leaderboard UI for the given leaderboard. |
| `ShowLeaderboardUI(string leaderboardId, Action< UIStatus > callback)` | `void`  Shows the leaderboard UI and calls the specified callback upon completion. |
| `ShowLeaderboardUI(string leaderboardId, LeaderboardTimeSpan span, Action< UIStatus > callback)` | `void`  Shows the leaderboard UI and calls the specified callback upon completion. |
| `UnlockAchievement(string achievementID, Action< bool > callback)` | `void`  Unlocks the achievement with the passed identifier. |

## Properties

### DebugLogEnabled

```
static bool DebugLogEnabled
```

Gets or sets a value indicating whether debug logs are enabled.

This property may be set before calling [Activate](/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1afc68980eb29743625ae7ea74c1e99327) method.

Details | || **Returns** | `true` if debug log enabled; otherwise, `false`. |

### Events

```
IEventsClient Events
```

Gets the events client object.

The events client.

### Instance

```
static PlayGamesPlatform Instance
```

Gets the singleton instance of the Play Games platform.

Details | || **Returns** | The instance. |

### Nearby

```
static INearbyConnectionClient Nearby
```

Gets the nearby connection client.

NOTE: Can be null until the nearby client is initialized. Call InitializeNearby to use callback to be notified when initialization is complete.

The nearby.

### SavedGame

```
ISavedGameClient SavedGame
```

Gets the saved game client object.

The saved game client.

### localUser

```
ILocalUser localUser
```

Gets the local user.

Details | || **Returns** | The local user. |

## Public static functions

### Activate

```
PlayGamesPlatform Activate()
```

Activates the Play Games platform as the implementation of Social.Active.

After calling this method, you can call methods on Social.Active. For example, `Social.Active.Authenticate()`.

Details | || **Returns** | The singleton [PlayGamesPlatform](/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform) instance. |

### InitializeNearby

```
void InitializeNearby(
  Action< INearbyConnectionClient > callback
)
```

Initializes the nearby connection platform.

This call initializes the nearby connection platform. This is independent of the Play Game Services initialization. Multiple calls to this method are ignored.

Details | || Parameters | |  |  | | --- | --- | | `callback` | Callback invoked when complete. | |

## Public functions

### AddIdMapping

```
void AddIdMapping(
  string fromId,
  string toId
)
```

Specifies that the ID `fromId` should be implicitly replaced by `toId` on any calls that take a leaderboard or achievement ID.

After a mapping is registered, you can use `fromId` instead of `toId` when making a call. For example, the following two snippets are equivalent: `ReportProgress("Cfiwjew894_AQ", 100.0, callback);` is equivalent to: `AddIdMapping("super-combo", "Cfiwjew894_AQ");``ReportProgress("super-combo", 100.0, callback);`

Details | || Parameters | |  |  | | --- | --- | | `fromId` | The identifier to map. | | `toId` | The identifier that `fromId` will be mapped to. | |

### AskForLoadFriendsResolution

```
void AskForLoadFriendsResolution(
  Action< UIStatus > callback
)
```

Shows the appropriate platform-specific friends sharing UI.

Details | || Parameters | |  |  | | --- | --- | | `callback` | The callback to invoke when complete. If null, no callback is called. | |

### Authenticate

```
void Authenticate(
  Action< SignInStatus > callback
)
```

Returns the result of the automatic sign-in attempt.

Play Games SDK automatically prompts users to sign in when the game is started. This API is useful for understanding if your game has access to Play Games Services and should be used when your game is started in order to conditionally enable or disable your Play Games Services integration.

Details | || Parameters | |  |  | | --- | --- | | `callback` | The callback to call when authentication finishes. | |

### Authenticate

```
void Authenticate(
  ILocalUser unused,
  Action< bool > callback
)
```

Provided for compatibility with ISocialPlatform.

**See also:**Authenticate(Action<bool>,bool)

Details | || Parameters | |  |  | | --- | --- | | `unused` | Unused parameter for this implementation. | | `callback` | Callback invoked when complete. | |

### Authenticate

```
void Authenticate(
  ILocalUser unused,
  Action< bool, string > callback
)
```

Provided for compatibility with ISocialPlatform.

**See also:**Authenticate(Action<bool>,bool)

Details | || Parameters | |  |  | | --- | --- | | `unused` | Unused parameter for this implementation. | | `callback` | Callback invoked when complete. | |

### CreateAchievement

```
IAchievement CreateAchievement()
```

Creates an achievement object which may be subsequently used to report an achievement.

Details | || **Returns** | The achievement object. |

### CreateLeaderboard

```
ILeaderboard CreateLeaderboard()
```

Returns a leaderboard object that can be configured to load scores.

Details | || **Returns** | The leaderboard object. |

### GetFriendsListVisibility

```
void GetFriendsListVisibility(
  bool forceReload,
  Action< FriendsListVisibilityStatus > callback
)
```

Returns if the user has allowed permission for the game to access the friends list.

Details | || Parameters | |  |  | | --- | --- | | `forceReload` | If `true`, this call will clear any locally cached data and attempt to fetch the latest data from the server. Normally, this should be set to `false` to gain advantages of data caching. | | `callback` | Callback invoked upon completion. | |

### GetLastLoadFriendsStatus

```
LoadFriendsStatus GetLastLoadFriendsStatus()
```

Gets status of the last call to load friends.

### GetLoading

```
bool GetLoading(
  ILeaderboard board
)
```

Check if the leaderboard is currently loading.

Details | || Parameters | |  |  | | --- | --- | | `board` | The leaderboard to check for loading in progress | |
| **Returns** | `true`, if loading was gotten, `false` otherwise. |

### GetPlayerStats

```
void GetPlayerStats(
  Action< CommonStatusCodes, PlayerStats > callback
)
```

Gets the player stats.

Details | || Parameters | |  |  | | --- | --- | | `callback` | Callback invoked when completed. | |

### GetUserDisplayName

```
string GetUserDisplayName()
```

Returns the user's display name.

Details | || **Returns** | The user display name. For example, "Bruno Oliveira" |

### GetUserId

```
string GetUserId()
```

Returns the user's Google ID.

Details | || **Returns** | The user's Google ID. No guarantees are made as to the meaning or format of this identifier except that it is unique to the user who is signed in. |

### GetUserImageUrl

```
string GetUserImageUrl()
```

Returns the user's avatar URL if they have one.

Details | || **Returns** | The URL, or null if the user is not authenticated or does not have an avatar. |

### IncrementAchievement

```
void IncrementAchievement(
  string achievementID,
  int steps,
  Action< bool > callback
)
```

Increments an achievement.

This is a Play Games extension of the ISocialPlatform API.

Details | || Parameters | |  |  | | --- | --- | | `achievementID` | The ID of the achievement to increment. This can be a raw Google Play Games achievement ID (alphanumeric string), or an alias that was previously configured by a call to [AddIdMapping](/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a5f3b14568fa25fb25f2012549540b835). | | `steps` | The number of steps to increment the achievement by. | | `callback` | The callback to call to report the success or failure of the operation. The callback will be called with `true` to indicate success or `false` for failure. | |

### IsAuthenticated

```
bool IsAuthenticated()
```

Determines whether the user is authenticated.

Details | || **Returns** | `true` if the user is authenticated; otherwise, `false`. |

### LoadAchievementDescriptions

```
void LoadAchievementDescriptions(
  Action< IAchievementDescription[]> callback
)
```

Loads the Achievement descriptions.

Details | || Parameters | |  |  | | --- | --- | | `callback` | The callback to receive the descriptions | |

### LoadAchievements

```
void LoadAchievements(
  Action< IAchievement[]> callback
)
```

Loads the achievement state for the current user.

Details | || Parameters | |  |  | | --- | --- | | `callback` | The callback to receive the achievements | |

### LoadFriends

```
void LoadFriends(
  ILocalUser user,
  Action< bool > callback
)
```

Loads the friends that also play this game.

See loadConnectedPlayers.

This is a callback variant of LoadFriends. When completed, the friends list set in the user object, so they can accessed via the friends property as needed.

Details | || Parameters | |  |  | | --- | --- | | `user` | The current local user | | `callback` | Callback invoked when complete. | |

### LoadFriends

```
void LoadFriends(
  int pageSize,
  bool forceReload,
  Action< LoadFriendsStatus > callback
)
```

Loads the first page of the user's friends.

Details | || Parameters | |  |  | | --- | --- | | `pageSize` | The number of entries to request for this initial page. Note that if cached data already exists, the returned buffer may contain more than this size, but it is guaranteed to contain at least this many if the collection contains enough records. | | `forceReload` | If true, this call will clear any locally cached data and attempt to fetch the latest data from the server. This would commonly be used for something like a user-initiated refresh. Normally, this should be set to `false` to gain advantages of data caching. | | `callback` | Callback invoked upon completion with the status. | |

### LoadMoreFriends

```
void LoadMoreFriends(
  int pageSize,
  Action< LoadFriendsStatus > callback
)
```

Loads the friends list page

Details | || Parameters | |  |  | | --- | --- | | `pageSize` | The number of entries to request for this initial page. Note that if cached data already exists, the returned buffer may contain more than this size, but it is guaranteed to contain at least this many if the collection contains enough records. | | `callback` |  | |

### LoadMoreScores

```
void LoadMoreScores(
  ScorePageToken token,
  int rowCount,
  Action< LeaderboardScoreData > callback
)
```

Loads more scores.

This call may fail when trying to load friends with ResponseCode.ResolutionRequired if the user has not share the friends list with the game. In this case, use AskForLoadFriendsResolution to request access.

This is used to load the next "page" of scores.

Details | || Parameters | |  |  | | --- | --- | | `token` | Token used to recording the loading. | | `rowCount` | Row count. | | `callback` | Callback invoked when complete. | |

### LoadScores

```
void LoadScores(
  string leaderboardId,
  Action< IScore[]> callback
)
```

Loads the scores relative the player.

This returns the 25 (which is the max results returned by the SDK per call) scores that are around the player's score on the Public, all time leaderboard. Use the overloaded methods which are specific to GPGS to modify these parameters.

Details | || Parameters | |  |  | | --- | --- | | `leaderboardId` | Leaderboard Id | | `callback` | Callback to invoke when completed. | |

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

Loads the scores using the provided parameters.

This call may fail when trying to load friends with ResponseCode.ResolutionRequired if the user has not share the friends list with the game. In this case, use AskForLoadFriendsResolution to request access.

Details | || Parameters | |  |  | | --- | --- | | `leaderboardId` | Leaderboard identifier. | | `start` | Start either top scores, or player centered. | | `rowCount` | Row count. the number of rows to return. | | `collection` | Collection. social or public | | `timeSpan` | Time span. daily, weekly, all-time | | `callback` | Callback to invoke when completed. | |

### LoadScores

```
void LoadScores(
  ILeaderboard board,
  Action< bool > callback
)
```

Loads the leaderboard based on the constraints in the leaderboard object.

Details | || Parameters | |  |  | | --- | --- | | `board` | The leaderboard object. This is created by calling [CreateLeaderboard()](/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a3f61a6cd7ed0864955972c76d346180d), and then initialized appropriately. | | `callback` | Callback invoked when complete. | |

### LoadUsers

```
void LoadUsers(
  string[] userIds,
  Action< IUserProfile[]> callback
)
```

Loads the users.

Details | || Parameters | |  |  | | --- | --- | | `userIds` | User identifiers. | | `callback` | Callback invoked when complete. | |

### ManuallyAuthenticate

```
void ManuallyAuthenticate(
  Action< SignInStatus > callback
)
```

Manually requests that your game performs sign in with Play Games Services.

Note that a sign-in attempt will be made automatically when your game's application started. For this reason most games will not need to manually request to perform sign-in unless the automatic sign-in attempt failed and your game requires access to Play Games Services.

Details | || Parameters | |  |  | | --- | --- | | `callback` |  | |

### ReportProgress

```
void ReportProgress(
  string achievementID,
  double progress,
  Action< bool > callback
)
```

Reports the progress of an achievement (reveal, unlock or increment).

This method attempts to implement the expected behavior of `ISocialPlatform.ReportProgress` as closely as possible, as described below. Although this method works with incremental achievements for compatibility purposes, calling this method for incremental achievements is not recommended, since the Play Games API exposes incremental achievements in a very different way than the interface presented by `ISocialPlatform.ReportProgress`. The implementation of this method for incremental achievements attempts to produce the correct result, but may be imprecise. If possible, call [IncrementAchievement](/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a00118ca719d9b61a9e62154ca9a99899) instead.

Details | || Parameters | |  |  | | --- | --- | | `achievementID` | The ID of the achievement to unlock, reveal or increment. This can be a raw Google Play Games achievement ID (alphanumeric string), or an alias that was previously configured by a call to [AddIdMapping](/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a5f3b14568fa25fb25f2012549540b835). | | `progress` | Progress of the achievement. If the achievement is standard (not incremental), then a progress of 0.0 will reveal the achievement and 100.0 will unlock it. Behavior of other values is undefined. If the achievement is incremental, then this value is interpreted as the total percentage of the achievement's progress that the player should have as a result of this call (regardless of the progress they had before). So if the player's previous progress was 30% and this call specifies 50.0, the new progress will be 50% (not 80%). | | `callback` | Callback that will be called to report the result of the operation: `true` on success, `false` otherwise. | |

### ReportScore

```
void ReportScore(
  long score,
  string board,
  Action< bool > callback
)
```

Reports a score to a leaderboard.

Details | || Parameters | |  |  | | --- | --- | | `score` | The score to report. | | `board` | The ID of the leaderboard on which the score is to be posted. This may be a raw Google Play Games leaderboard ID or an alias configured through a call to [AddIdMapping](/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a5f3b14568fa25fb25f2012549540b835). | | `callback` | The callback to call to report the success or failure of the operation. The callback will be called with `true` to indicate success or `false` for failure. | |

### ReportScore

```
void ReportScore(
  long score,
  string board,
  string metadata,
  Action< bool > callback
)
```

Submits the score for the currently signed-in player to the leaderboard associated with a specific id and metadata (such as something the player did to earn the score).

Details | || Parameters | |  |  | | --- | --- | | `score` | Score to report. | | `board` | leaderboard id. | | `metadata` | metadata about the score. | | `callback` | Callback invoked upon completion. | |

### RequestRecallAccess

```
void RequestRecallAccess(
  Action< RecallAccess > callback
)
```

Requests access to the recall API.

Details | || Parameters | |  |  | | --- | --- | | `callback` | The callback to invoke with the recall access. | |

### RequestServerSideAccess

```
void RequestServerSideAccess(
  bool forceRefreshToken,
  Action< string > callback
)
```

Requests server-side access to Player Games Services for the currently signed in player.

When requested an authorization code is returned that can be used by your game-server to exchange for an access token and conditionally a refresh token (when `forceRefreshToken` is true). The access token may then be used by your game-server to access the Play Games Services web APIs. This is commonly used to complete a sign-in flow by verifying the Play Games Services player id.

If `forceRefreshToken` is true, when exchanging the authorization code a refresh token will be returned in addition to the access token. The refresh token allows the game-server to request additional access tokens, allowing your game-server to continue accesses Play Games Services while the user is not actively playing your app.

Details | || Parameters | |  |  | | --- | --- | | `forceRefreshToken` | If set to `true`, a refresh token will be returned along with the access token. | | `callback` | The callback to invoke with the server authorization code. | |

### RequestServerSideAccess

```
void RequestServerSideAccess(
  bool forceRefreshToken,
  List< AuthScope > scopes,
  Action< AuthResponse > callback
)
```

Requests server-side access to Player Games Services for the currently signed in player.

When requested an authorization code is returned that can be used by your game-server to exchange for an access token and conditionally a refresh token (when `forceRefreshToken` is true). The access token may then be used by your game-server to access the Play Games Services web APIs. This is commonly used to complete a sign-in flow by verifying the Play Games Services player id.

If `forceRefreshToken` is true, when exchanging the authorization code a refresh token will be returned in addition to the access token. The refresh token allows the game-server to request additional access tokens, allowing your game-server to continue accesses Play Games Services while the user is not actively playing your app.

Details | || Parameters | |  |  | | --- | --- | | `forceRefreshToken` | If set to `true`, a refresh token will be returned along with the access token. | | `scopes` | The OAuth 2.0 scopes to request access to. | | `callback` | The callback to invoke with the AuthResponse. | |

### RevealAchievement

```
void RevealAchievement(
  string achievementID,
  Action< bool > callback
)
```

Reveals the achievement with the passed identifier.

This is a Play Games extension of the ISocialPlatform API.

If the operation succeeds, the callback will be invoked on the game thread with `true`. If the operation fails, the callback will be invoked with `false`. This operation will immediately fail if the user is not authenticated (the callback will immediately be invoked with false). If the achievement is already in a revealed state, this call will succeed immediately.

Details | || Parameters | |  |  | | --- | --- | | `achievementID` | The ID of the achievement to increment. This can be a raw Google Play Games achievement ID (alphanumeric string), or an alias that was previously configured by a call to [AddIdMapping](/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a5f3b14568fa25fb25f2012549540b835). | | `callback` | The callback to call to report the success or failure of the operation. The callback will be called with `true` to indicate success or `false` for failure. | |

### SetDefaultLeaderboardForUI

```
void SetDefaultLeaderboardForUI(
  string lbid
)
```

Sets the default leaderboard for the leaderboard UI.

After calling this method, a call to [ShowLeaderboardUI](/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a89d9409cc48dadfa19ba73df80e8db4d) will show only the specified leaderboard instead of showing the list of all leaderboards.

Details | || Parameters | |  |  | | --- | --- | | `lbid` | The ID of the leaderboard to display on the default UI. This may be a raw Google Play Games leaderboard ID or an alias configured through a call to [AddIdMapping](/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a5f3b14568fa25fb25f2012549540b835). | |

### SetStepsAtLeast

```
void SetStepsAtLeast(
  string achievementID,
  int steps,
  Action< bool > callback
)
```

Set an achievement to have at least the given number of steps completed.

Calling this method while the achievement already has more steps than the provided value is a no-op. Once the achievement reaches the maximum number of steps, the achievement is automatically unlocked, and any further mutation operations are ignored.

Details | || Parameters | |  |  | | --- | --- | | `achievementID` | The ID of the achievement to increment. This can be a raw Google Play Games achievement ID (alphanumeric string), or an alias that was previously configured by a call to [AddIdMapping](/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a5f3b14568fa25fb25f2012549540b835). | | `steps` | The number of steps to increment the achievement by. | | `callback` | The callback to call to report the success or failure of the operation. The callback will be called with `true` to indicate success or `false` for failure. | |

### ShowAchievementsUI

```
void ShowAchievementsUI()
```

Shows the standard Google Play Games achievements user interface, which allows the player to browse their achievements.

### ShowAchievementsUI

```
void ShowAchievementsUI(
  Action< UIStatus > callback
)
```

Shows the standard Google Play Games achievements user interface, which allows the player to browse their achievements.

Details | || Parameters | |  |  | | --- | --- | | `callback` | If non-null, the callback is invoked when the achievement UI is dismissed | |

### ShowCompareProfileWithAlternativeNameHintsUI

```
void ShowCompareProfileWithAlternativeNameHintsUI(
  string userId,
  string otherPlayerInGameName,
  string currentPlayerInGameName,
  Action< UIStatus > callback
)
```

Shows the Player Profile UI for the given user identifier.

Details | || Parameters | |  |  | | --- | --- | | `userId` | User Identifier. | | `otherPlayerInGameName` | The game's own display name of the player referred to by userId. | | `currentPlayerInGameName` | The game's own display name of the current player. | | `callback` | Callback invoked upon completion. | |

### ShowLeaderboardUI

```
void ShowLeaderboardUI()
```

Shows the standard Google Play Games leaderboards user interface, which allows the player to browse their leaderboards.

If you have configured a specific leaderboard as the default through a call to [SetDefaultLeaderboardForUI](/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1afc9822ee9fee41d589a7ef79933d6408), the UI will show that specific leaderboard only. Otherwise, a list of all the leaderboards will be shown.

### ShowLeaderboardUI

```
void ShowLeaderboardUI(
  string leaderboardId
)
```

Shows the standard Google Play Games leaderboard UI for the given leaderboard.

Details | || Parameters | |  |  | | --- | --- | | `leaderboardId` | The ID of the leaderboard to display. This may be a raw Google Play Games leaderboard ID or an alias configured through a call to [AddIdMapping](/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a5f3b14568fa25fb25f2012549540b835). | |

### ShowLeaderboardUI

```
void ShowLeaderboardUI(
  string leaderboardId,
  Action< UIStatus > callback
)
```

Shows the leaderboard UI and calls the specified callback upon completion.

Details | || Parameters | |  |  | | --- | --- | | `leaderboardId` | leaderboard ID, can be null meaning all leaderboards. | | `callback` | Callback to call. If null, nothing is called. | |

### ShowLeaderboardUI

```
void ShowLeaderboardUI(
  string leaderboardId,
  LeaderboardTimeSpan span,
  Action< UIStatus > callback
)
```

Shows the leaderboard UI and calls the specified callback upon completion.

Details | || Parameters | |  |  | | --- | --- | | `leaderboardId` | leaderboard ID, can be null meaning all leaderboards. | | `span` | Timespan to display scores in the leaderboard. | | `callback` | Callback to call. If null, nothing is called. | |

### UnlockAchievement

```
void UnlockAchievement(
  string achievementID,
  Action< bool > callback
)
```

Unlocks the achievement with the passed identifier.

This is a Play Games extension of the ISocialPlatform API.

If the operation succeeds, the callback will be invoked on the game thread with `true`. If the operation fails, the callback will be invoked with false. This operation will immediately fail if the user is not authenticated (the callback will immediately be invoked with `false`). If the achievement is already unlocked, this call will succeed immediately.

Details | || Parameters | |  |  | | --- | --- | | `achievementID` | The ID of the achievement to increment. This can be a raw Google Play Games achievement ID (alphanumeric string), or an alias that was previously configured by a call to [AddIdMapping](/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a5f3b14568fa25fb25f2012549540b835). | | `callback` | The callback to call to report the success or failure of the operation. The callback will be called with `true` to indicate success or `false` for failure. | |