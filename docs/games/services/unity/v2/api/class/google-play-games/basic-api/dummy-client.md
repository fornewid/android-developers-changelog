---
title: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client
source: md.txt
---

# GooglePlayGames.BasicApi.DummyClient Class Reference

# GooglePlayGames.BasicApi.DummyClient

Dummy client used in Editor.

## Summary

Google Play Game Services are not supported in the Editor environment, so this client is used as a placeholder.

### Inheritance

Inherits from:[GooglePlayGames.BasicApi.IPlayGamesClient](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client)

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AskForLoadFriendsResolution](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a4696d9b1e229559aac3a9dc65084fb44)`(Action< `[UIStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1aab0aa7dedba9c8167fff3a0deafaae52)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `void` Requests the load friends resolution UI.                                                                                                                                                                                                                                |
| [Authenticate](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1abd15fd3c84f1c77777e3c66c086c58dc)`(Action< `[SignInStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1a7ac5abd21359fbbe3ea826b40143e5c6)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `void` Authenticates the user.                                                                                                                                                                                                                                                 |
| [GetEventsClient](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a3ed38e21343f1a2d2ab421b12c2ac46c)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [GooglePlayGames.BasicApi.Events.IEventsClient](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/events/i-events-client#interface_google_play_games_1_1_basic_api_1_1_events_1_1_i_events_client) Retrieves the events client.  |
| [GetFriends](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a822f36e66bec9390c800bcfd54cb1502)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `IUserProfile[]` Retrieves the list of friends for the current user.                                                                                                                                                                                                           |
| [GetFriendsListVisibility](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a2d42ff21e0665be8a1fc9c1dcdf4f948)`(bool forceReload, Action< `[FriendsListVisibilityStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1ae51eb6918fd8949e31a7d7888c93e664)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `void` Retrieves the visibility status of the friends list.                                                                                                                                                                                                                    |
| [GetLastLoadFriendsStatus](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1ab63351c7e273789ee2ac1fc9cc4c1cf9)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | [LoadFriendsStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1ac4592ce0c250daf4bf07792776f63708) Retrieves the last load friends status.                                      |
| [GetPlayerStats](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a228a826bce001a5c75b5b4b5e986f73a)`(Action< `[CommonStatusCodes](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1abaf59665136d25cef9ddd68d2069c603)`, `[PlayerStats](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `void` Retrieves the player statistics.                                                                                                                                                                                                                                        |
| [GetSavedGameClient](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a9730debd760cff8a23073bf8d484e8c1)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | [SavedGame.ISavedGameClient](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-saved-game-client#interface_google_play_games_1_1_basic_api_1_1_saved_game_1_1_i_saved_game_client) Retrieves the saved game client. |
| [GetUserDisplayName](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1ad843844c9ce425ad23266e5216b5e33f)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `string` Retrieves the user's display name.                                                                                                                                                                                                                                    |
| [GetUserId](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a1ad01978e163f303d7c42358219a5b9d)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `string` Retrieves the user ID.                                                                                                                                                                                                                                                |
| [GetUserImageUrl](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1acf75737a3c38dea371c089e6d4a98dd9)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `string` Retrieves the user's image URL.                                                                                                                                                                                                                                       |
| [IncrementAchievement](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a5351f44a29eb2a2daf1c6c26959dc34b)`(string achId, int steps, Action< bool > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `void` Increments the specified achievement by a number of steps.                                                                                                                                                                                                              |
| [IsAuthenticated](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a3a2634f40272d8fea4d6a08a71978069)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `bool` Checks if the user is authenticated.                                                                                                                                                                                                                                    |
| [LeaderboardMaxResults](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a9a5a7ae1b234f4f733737909b619e772)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `int` Retrieves the maximum number of leaderboard results that can be loaded.                                                                                                                                                                                                  |
| [LoadAchievements](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a2613773789d913588a34b921e6328dd7)`(Action< `[Achievement](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement)`[]> callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `void` Loads achievements for the current user.                                                                                                                                                                                                                                |
| [LoadFriends](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1afe81a29eea984b7d469a9ffef3ab6d77)`(int pageSize, bool forceReload, Action< `[LoadFriendsStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1ac4592ce0c250daf4bf07792776f63708)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `void` Loads friends with paging options.                                                                                                                                                                                                                                      |
| [LoadFriends](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a6abd9cfecd33ebae05e3f408d76d42ee)`(Action< bool > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `void` Loads friends with a simple boolean flag indicating success or failure.                                                                                                                                                                                                 |
| [LoadMoreFriends](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a758064dd7d4f93fc687c1fc832e5c226)`(int pageSize, Action< `[LoadFriendsStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1ac4592ce0c250daf4bf07792776f63708)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `void` Loads additional friends if available.                                                                                                                                                                                                                                  |
| [LoadMoreScores](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a073d844a140aebe468bf2ad5449fbbb3)`(`[ScorePageToken](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/score-page-token#class_google_play_games_1_1_basic_api_1_1_score_page_token)` token, int rowCount, Action< `[LeaderboardScoreData](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/leaderboard-score-data#class_google_play_games_1_1_basic_api_1_1_leaderboard_score_data)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `void` Loads more leaderboard scores based on the provided pagination token.                                                                                                                                                                                                   |
| [LoadScores](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a5cc62b6b9c0f21637ec5c3e4a3650125)`(string leaderboardId, `[LeaderboardStart](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1abccf096f9fcbe7a3e572b64290675d18)` start, int rowCount, `[LeaderboardCollection](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1a33fac2add308ad7414106822f66bc681)` collection, `[LeaderboardTimeSpan](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1a8d9a7be92fea2b7a31420b073558fbce)` timeSpan, Action< `[LeaderboardScoreData](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/leaderboard-score-data#class_google_play_games_1_1_basic_api_1_1_leaderboard_score_data)` > callback)` | `void` Loads the leaderboard scores based on the specified parameters.                                                                                                                                                                                                         |
| [LoadUsers](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a3fc341874edbc7b8729a9e07ec13a11b)`(string[] userIds, Action< IUserProfile[]> callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `void` Loads user profiles for the given user IDs.                                                                                                                                                                                                                             |
| [ManuallyAuthenticate](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1aed5b866564d9b654ccae8b2f4f54f903)`(Action< `[SignInStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1a7ac5abd21359fbbe3ea826b40143e5c6)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `void` Manually authenticates the user.                                                                                                                                                                                                                                        |
| [RequestRecallAccessToken](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a28f2871ccc27c0fa6131d5fea57ddc56)`(Action< `[RecallAccess](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/recall-access#class_google_play_games_1_1_basic_api_1_1_recall_access)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `void` Requests recall of the access token.                                                                                                                                                                                                                                    |
| [RequestServerSideAccess](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a63568dd288681f326cb2440a16e379c2)`(bool forceRefreshToken, Action< string > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `void` Requests server-side access with a refresh token.                                                                                                                                                                                                                       |
| [RequestServerSideAccess](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a88400aaed601505223788db9a5ab7f5b)`(bool forceRefreshToken, List< `[AuthScope](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1ab5415b6b4ad0724108f447b203380e44)` > scopes, Action< `[AuthResponse](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/auth-response#class_google_play_games_1_1_basic_api_1_1_auth_response)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `void` Requests server-side access with specific scopes.                                                                                                                                                                                                                       |
| [RevealAchievement](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a9556e1b3f0cb66e75b63c768de7b2355)`(string achId, Action< bool > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `void` Reveals the specified achievement.                                                                                                                                                                                                                                      |
| [SetStepsAtLeast](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a6218d7098e653063c6bfbd728eab5966)`(string achId, int steps, Action< bool > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `void` Sets the steps of the specified achievement to at least a certain number.                                                                                                                                                                                               |
| [ShowAchievementsUI](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1ac67850f82b900ba371c79d8a0d09fb09)`(Action< `[UIStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1aab0aa7dedba9c8167fff3a0deafaae52)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `void` Displays the achievements UI.                                                                                                                                                                                                                                           |
| [ShowCompareProfileWithAlternativeNameHintsUI](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a94a9dc92a31a71893382750bc084ae59)`(string userId, string otherPlayerInGameName, string currentPlayerInGameName, Action< `[UIStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1aab0aa7dedba9c8167fff3a0deafaae52)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `void` Displays the compare profile UI for a player.                                                                                                                                                                                                                           |
| [ShowLeaderboardUI](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a45db875a3d343f38431399142d543be4)`(string leaderboardId, `[LeaderboardTimeSpan](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1a8d9a7be92fea2b7a31420b073558fbce)` span, Action< `[UIStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1aab0aa7dedba9c8167fff3a0deafaae52)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `void` Displays the leaderboard UI for a specific leaderboard.                                                                                                                                                                                                                 |
| [SubmitScore](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a529633005221eb7881067d6c2685e99f)`(string leaderboardId, long score, Action< bool > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `void` Submits a score to a specific leaderboard.                                                                                                                                                                                                                              |
| [SubmitScore](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1a89285177708880150e49f0b1f2b653a9)`(string leaderboardId, long score, string metadata, Action< bool > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `void` Submits a score with additional metadata to a specific leaderboard.                                                                                                                                                                                                     |
| [UnlockAchievement](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client#class_google_play_games_1_1_basic_api_1_1_dummy_client_1ac3628001f81f860f63db035a899bc377)`(string achId, Action< bool > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `void` Unlocks the specified achievement.                                                                                                                                                                                                                                      |

## Public functions

### AskForLoadFriendsResolution

```c#
void AskForLoadFriendsResolution(
  Action< UIStatus > callback
)
```  
Requests the load friends resolution UI.

<br />

|                                                      Details                                                      ||
|------------|-------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-----------------------------------| | `callback` | Callback to handle the UI status. | |

### Authenticate

```c#
void Authenticate(
  Action< SignInStatus > callback
)
```  
Authenticates the user.

<br />

|                                                           Details                                                           ||
|------------|-----------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|----------------------------------------| | `callback` | Callback to handle the sign-in status. | |

### GetEventsClient

```c#
GooglePlayGames.BasicApi.Events.IEventsClient GetEventsClient()
```  
Retrieves the events client.

<br />

|                            Details                             ||
|-------------|---------------------------------------------------|
| **Returns** | Returns null since no events client is available. |

### GetFriends

```c#
IUserProfile[] GetFriends()
```  
Retrieves the list of friends for the current user.

<br />

|                             Details                              ||
|-------------|-----------------------------------------------------|
| **Returns** | Returns an empty array since no friends are loaded. |

### GetFriendsListVisibility

```c#
void GetFriendsListVisibility(
  bool forceReload,
  Action< FriendsListVisibilityStatus > callback
)
```  
Retrieves the visibility status of the friends list.

<br />

|                                                                                                                   Details                                                                                                                    ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------|--------------------------------------------------------| | `forceReload` | Flag to force reload the friends list visibility.      | | `callback`    | Callback to handle the friends list visibility status. | |

### GetLastLoadFriendsStatus

```c#
LoadFriendsStatus GetLastLoadFriendsStatus()
```  
Retrieves the last load friends status.

<br />

|                         Details                          ||
|-------------|---------------------------------------------|
| **Returns** | Returns the last known load friends status. |

### GetPlayerStats

```c#
void GetPlayerStats(
  Action< CommonStatusCodes, PlayerStats > callback
)
```  
Retrieves the player statistics.

<br />

|                                                                  Details                                                                  ||
|------------|-------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-----------------------------------------------| | `callback` | Callback to handle the player stats response. | |

### GetSavedGameClient

```c#
SavedGame.ISavedGameClient GetSavedGameClient()
```  
Retrieves the saved game client.

<br />

|                              Details                               ||
|-------------|-------------------------------------------------------|
| **Returns** | Returns null since no saved game client is available. |

### GetUserDisplayName

```c#
string GetUserDisplayName()
```  
Retrieves the user's display name.

<br />

|                  Details                   ||
|-------------|-------------------------------|
| **Returns** | Returns a dummy display name. |

### GetUserId

```c#
string GetUserId()
```  
Retrieves the user ID.

<br />

|                Details                ||
|-------------|--------------------------|
| **Returns** | Returns a dummy user ID. |

### GetUserImageUrl

```c#
string GetUserImageUrl()
```  
Retrieves the user's image URL.

<br />

|                        Details                         ||
|-------------|-------------------------------------------|
| **Returns** | Returns null since no image is available. |

### IncrementAchievement

```c#
void IncrementAchievement(
  string achId,
  int steps,
  Action< bool > callback
)
```  
Increments the specified achievement by a number of steps.

<br />

|                                                                                                                                         Details                                                                                                                                         ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|---------------------------------------------------| | `achId`    | The achievement ID to increment.                  | | `steps`    | The number of steps to increment the achievement. | | `callback` | Callback to handle the increment result.          | |

### IsAuthenticated

```c#
bool IsAuthenticated()
```  
Checks if the user is authenticated.

<br />

|                             Details                              ||
|-------------|-----------------------------------------------------|
| **Returns** | Returns false indicating user is not authenticated. |

### LeaderboardMaxResults

```c#
int LeaderboardMaxResults()
```  
Retrieves the maximum number of leaderboard results that can be loaded.

<br />

|                             Details                             ||
|-------------|----------------------------------------------------|
| **Returns** | Returns the maximum number of leaderboard results. |

### LoadAchievements

```c#
void LoadAchievements(
  Action< Achievement[]> callback
)
```  
Loads achievements for the current user.

<br />

|                                                                 Details                                                                 ||
|------------|-----------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|----------------------------------------------| | `callback` | Callback to handle the achievement response. | |

### LoadFriends

```c#
void LoadFriends(
  int pageSize,
  bool forceReload,
  Action< LoadFriendsStatus > callback
)
```  
Loads friends with paging options.

<br />

|                                                                                                                                   Details                                                                                                                                   ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------|---------------------------------------------| | `pageSize`    | The number of friends to load per page.     | | `forceReload` | Flag to force reload of the friends list.   | | `callback`    | Callback to handle the load friends status. | |

### LoadFriends

```c#
void LoadFriends(
  Action< bool > callback
)
```  
Loads friends with a simple boolean flag indicating success or failure.

<br />

|                                                        Details                                                        ||
|------------|-----------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-------------------------------------| | `callback` | Callback to handle the load result. | |

### LoadMoreFriends

```c#
void LoadMoreFriends(
  int pageSize,
  Action< LoadFriendsStatus > callback
)
```  
Loads additional friends if available.

<br />

|                                                                                              Details                                                                                               ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|---------------------------------------------| | `pageSize` | The number of additional friends to load.   | | `callback` | Callback to handle the load friends status. | |

### LoadMoreScores

```c#
void LoadMoreScores(
  ScorePageToken token,
  int rowCount,
  Action< LeaderboardScoreData > callback
)
```  
Loads more leaderboard scores based on the provided pagination token.

<br />

|                                                                                                                                   Details                                                                                                                                   ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|------------------------------------------------| | `token`    | The token used for pagination.                 | | `rowCount` | The number of scores to load.                  | | `callback` | Callback to handle the leaderboard score data. | |

### LoadScores

```c#
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

<br />

|                                                                                                                                                                                                                                                    Details                                                                                                                                                                                                                                                     ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------|------------------------------------------------| | `leaderboardId` | The ID of the leaderboard to load scores from. | | `start`         | The start position for loading scores.         | | `rowCount`      | The number of scores to load.                  | | `collection`    | The collection type (e.g., public or social).  | | `timeSpan`      | The time span for the leaderboard scores.      | | `callback`      | Callback to handle the leaderboard score data. | |

### LoadUsers

```c#
void LoadUsers(
  string[] userIds,
  Action< IUserProfile[]> callback
)
```  
Loads user profiles for the given user IDs.

<br />

|                                                                                                 Details                                                                                                  ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-----------------------------------------------| | `userIds`  | List of user IDs.                             | | `callback` | Callback to handle the user profile response. | |

### ManuallyAuthenticate

```c#
void ManuallyAuthenticate(
  Action< SignInStatus > callback
)
```  
Manually authenticates the user.

<br />

|                                                           Details                                                           ||
|------------|-----------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|----------------------------------------| | `callback` | Callback to handle the sign-in status. | |

### RequestRecallAccessToken

```c#
void RequestRecallAccessToken(
  Action< RecallAccess > callback
)
```  
Requests recall of the access token.

<br />

|                                                            Details                                                            ||
|------------|-------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-----------------------------------------| | `callback` | Callback to handle the recall response. | |

### RequestServerSideAccess

```c#
void RequestServerSideAccess(
  bool forceRefreshToken,
  Action< string > callback
)
```  
Requests server-side access with a refresh token.

<br />

|                                                                                           Details                                                                                            ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------|----------------------------------| | `forceRefreshToken` | Flag to force refresh the token. | | `callback`          | Callback to handle the response. | |

### RequestServerSideAccess

```c#
void RequestServerSideAccess(
  bool forceRefreshToken,
  List< AuthScope > scopes,
  Action< AuthResponse > callback
)
```  
Requests server-side access with specific scopes.

<br />

|                                                                                                                                       Details                                                                                                                                       ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------|-----------------------------------------| | `forceRefreshToken` | Flag to force refresh the token.        | | `scopes`            | List of requested authorization scopes. | | `callback`          | Callback to handle the response.        | |

### RevealAchievement

```c#
void RevealAchievement(
  string achId,
  Action< bool > callback
)
```  
Reveals the specified achievement.

<br />

|                                                                                     Details                                                                                      ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|---------------------------------------| | `achId`    | The achievement ID to reveal.         | | `callback` | Callback to handle the reveal result. | |

### SetStepsAtLeast

```c#
void SetStepsAtLeast(
  string achId,
  int steps,
  Action< bool > callback
)
```  
Sets the steps of the specified achievement to at least a certain number.

<br />

|                                                                                                                                             Details                                                                                                                                             ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-----------------------------------------------------| | `achId`    | The achievement ID to update.                       | | `steps`    | The number of steps to set.                         | | `callback` | Callback to handle the result of setting the steps. | |

### ShowAchievementsUI

```c#
void ShowAchievementsUI(
  Action< UIStatus > callback
)
```  
Displays the achievements UI.

<br />

|                                                      Details                                                      ||
|------------|-------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-----------------------------------| | `callback` | Callback to handle the UI status. | |

### ShowCompareProfileWithAlternativeNameHintsUI

```c#
void ShowCompareProfileWithAlternativeNameHintsUI(
  string userId,
  string otherPlayerInGameName,
  string currentPlayerInGameName,
  Action< UIStatus > callback
)
```  
Displays the compare profile UI for a player.

<br />

|                                                                                                                                                                                       Details                                                                                                                                                                                       ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------------|-----------------------------------------| | `userId`                  | The user ID of the player to compare.   | | `otherPlayerInGameName`   | The in-game name of the other player.   | | `currentPlayerInGameName` | The in-game name of the current player. | | `callback`                | Callback to handle the UI status.       | |

### ShowLeaderboardUI

```c#
void ShowLeaderboardUI(
  string leaderboardId,
  LeaderboardTimeSpan span,
  Action< UIStatus > callback
)
```  
Displays the leaderboard UI for a specific leaderboard.

<br />

|                                                                                                                     Details                                                                                                                     ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------|------------------------------------| | `leaderboardId` | The ID of the leaderboard.         | | `span`          | The time span for the leaderboard. | | `callback`      | Callback to handle the UI status.  | |

### SubmitScore

```c#
void SubmitScore(
  string leaderboardId,
  long score,
  Action< bool > callback
)
```  
Submits a score to a specific leaderboard.

<br />

|                                                                                                                                               Details                                                                                                                                               ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------|-------------------------------------------------| | `leaderboardId` | The ID of the leaderboard.                      | | `score`         | The score to submit.                            | | `callback`      | Callback to handle the score submission result. | |

### SubmitScore

```c#
void SubmitScore(
  string leaderboardId,
  long score,
  string metadata,
  Action< bool > callback
)
```  
Submits a score with additional metadata to a specific leaderboard.

<br />

|                                                                                                                                                                                  Details                                                                                                                                                                                  ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------|-------------------------------------------------| | `leaderboardId` | The ID of the leaderboard.                      | | `score`         | The score to submit.                            | | `metadata`      | Additional metadata to submit with the score.   | | `callback`      | Callback to handle the score submission result. | |

### UnlockAchievement

```c#
void UnlockAchievement(
  string achId,
  Action< bool > callback
)
```  
Unlocks the specified achievement.

<br />

|                                                                                     Details                                                                                      ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|---------------------------------------| | `achId`    | The achievement ID to unlock.         | | `callback` | Callback to handle the unlock result. | |