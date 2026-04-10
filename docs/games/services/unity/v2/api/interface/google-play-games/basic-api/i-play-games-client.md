---
title: https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client
url: https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client
source: md.txt
---

# GooglePlayGames.BasicApi.IPlayGamesClient Interface Reference

# GooglePlayGames.BasicApi.IPlayGamesClient

Defines an abstract interface for a Play Games Client.

## Summary

Concrete implementations might be, for example, the client for Android or for iOS. One fundamental concept that implementors of this class must adhere to is stable authentication state. This means that once[Authenticate()](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1a9b851169eae40c1ccf1d602488b88987)returns true through its callback, the user is considered to be forever after authenticated while the app is running. The implementation must make sure that this is the case for example, it must try to silently re-authenticate the user if authentication is lost or wait for the authentication process to get fixed if it is temporarily in a bad state (such as when the Activity in Android has just been brought to the foreground and the connection to the Games services hasn't yet been established). To the user of this interface, once the user is authenticated, they're forever authenticated. Unless, of course, there is an unusual permanent failure such as the underlying service dying, in which it's acceptable that API method calls will fail.

All methods can be called from the game thread. The user of this interface DOES NOT NEED to call them from the UI thread of the game. Transferring to the UI thread when necessary is a responsibility of the implementors of this interface.

CALLBACKS: all callbacks must be invoked in Unity's main thread. Implementors of this interface must guarantee that (suggestion: use PlayGamesHelperObject.RunOnGameThread(System.Action)).

### Inheritance

Direct Known Subclasses:[GooglePlayGames.BasicApi.DummyClient](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/dummy-client)

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AskForLoadFriendsResolution](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1aa522829fc4cb218d8a21627dbaaf16a0)`(Action< `[UIStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1aab0aa7dedba9c8167fff3a0deafaae52)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `void` Shows the appropriate platform-specific friends sharing UI.                                                                                                                                                                                                        |
| [Authenticate](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1a9b851169eae40c1ccf1d602488b88987)`(Action< `[SignInStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1a7ac5abd21359fbbe3ea826b40143e5c6)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `void` Returns the result of the automatic sign-in attempt.                                                                                                                                                                                                               |
| [GetEventsClient](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1af9cd51134ce06b89ecba5816f059c840)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [Events.IEventsClient](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/events/i-events-client#interface_google_play_games_1_1_basic_api_1_1_events_1_1_i_events_client) Gets the events client.                           |
| [GetFriends](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1a3c3ac49d0a1919c924d0735906a19d79)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `IUserProfile[]`                                                                                                                                                                                                                                                          |
| [GetFriendsListVisibility](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1abba414b396bad30836d863fd7a4dbb8d)`(bool forceReload, Action< `[FriendsListVisibilityStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1ae51eb6918fd8949e31a7d7888c93e664)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `void` Returns if the user has allowed permission for the game to access the friends list.                                                                                                                                                                                |
| [GetLastLoadFriendsStatus](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1a556a7037262558ac8671bb6a4a69ff30)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | [LoadFriendsStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1ac4592ce0c250daf4bf07792776f63708) Returns the latest LoadFriendsStatus obtained from loading friends.     |
| [GetPlayerStats](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1ab74427302d6f75820dca361580962ef4)`(Action< `[CommonStatusCodes](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1abaf59665136d25cef9ddd68d2069c603)`, `[PlayerStats](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `void` Gets the player stats.                                                                                                                                                                                                                                             |
| [GetSavedGameClient](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1a94ed10522f37fbf451920b6bf52b054d)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | [SavedGame.ISavedGameClient](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-saved-game-client#interface_google_play_games_1_1_basic_api_1_1_saved_game_1_1_i_saved_game_client) Gets the saved game client. |
| [GetUserDisplayName](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1ab73931373ec5c8cac82d9c9473fb2a5a)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `string` Returns a human readable name for the user, if they are logged in.                                                                                                                                                                                               |
| [GetUserId](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1afe95282825393e5c9a4594a593572572)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `string` Returns the authenticated user's ID.                                                                                                                                                                                                                             |
| [GetUserImageUrl](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1a4595636b0d588b8f541ba5db4d6e167b)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `string` Returns the user's avatar url, if they are logged in and have an avatar.                                                                                                                                                                                         |
| [IncrementAchievement](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1a4134f05ec30cf26ab47e8391cc1a5b68)`(string achievementId, int steps, Action< bool > successOrFailureCalllback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `void` Increments the achievement with the passed identifier.                                                                                                                                                                                                             |
| [IsAuthenticated](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1a069a963afa9c57f21cab868343459c00)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `bool` Returns whether or not user is authenticated.                                                                                                                                                                                                                      |
| [LeaderboardMaxResults](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1aaabdaa71c7675239edd56e63c54c2835)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `int` Returns the max number of scores returned per call.                                                                                                                                                                                                                 |
| [LoadAchievements](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1ae39a4fce664cc22abe30c484dd23db9b)`(Action< `[Achievement](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/achievement#class_google_play_games_1_1_basic_api_1_1_achievement)`[]> callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `void` Loads the achievements for the current signed in user and invokes the callback.                                                                                                                                                                                    |
| [LoadFriends](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1adc6837dc1f3cb7fa337a270081469830)`(Action< bool > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `void` Loads friends of the authenticated user.                                                                                                                                                                                                                           |
| [LoadFriends](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1a7df2db28ed9663fb48da427b43bf88a8)`(int pageSize, bool forceReload, Action< `[LoadFriendsStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1ac4592ce0c250daf4bf07792776f63708)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `void` Loads the first page of the user's friends                                                                                                                                                                                                                         |
| [LoadMoreFriends](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1ad23e1f61bf451989e6a8fca63bc98f2c)`(int pageSize, Action< `[LoadFriendsStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1ac4592ce0c250daf4bf07792776f63708)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `void` Loads the friends list page                                                                                                                                                                                                                                        |
| [LoadMoreScores](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1a1ded461301835090530c076eae609d6e)`(`[ScorePageToken](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/score-page-token#class_google_play_games_1_1_basic_api_1_1_score_page_token)` token, int rowCount, Action< `[LeaderboardScoreData](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/leaderboard-score-data#class_google_play_games_1_1_basic_api_1_1_leaderboard_score_data)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `void` Loads the more scores for the leaderboard.                                                                                                                                                                                                                         |
| [LoadScores](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1ac2f86d3ff84fede458823a521d896ae0)`(string leaderboardId, `[LeaderboardStart](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1abccf096f9fcbe7a3e572b64290675d18)` start, int rowCount, `[LeaderboardCollection](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1a33fac2add308ad7414106822f66bc681)` collection, `[LeaderboardTimeSpan](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1a8d9a7be92fea2b7a31420b073558fbce)` timeSpan, Action< `[LeaderboardScoreData](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/leaderboard-score-data#class_google_play_games_1_1_basic_api_1_1_leaderboard_score_data)` > callback)` | `void` Loads the score data for the given leaderboard.                                                                                                                                                                                                                    |
| [LoadUsers](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1a6f50cb8475832cb948f414506b0f90a8)`(string[] userIds, Action< IUserProfile[]> callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `void` Loads the users specified.                                                                                                                                                                                                                                         |
| [ManuallyAuthenticate](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1a5e866a2292900a7a27c293edbbb55cdd)`(Action< `[SignInStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1a7ac5abd21359fbbe3ea826b40143e5c6)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `void` Manually requests that your game performs sign in with Play Games Services.                                                                                                                                                                                        |
| [RequestRecallAccessToken](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1ab8b1780c4d07319a6fa40ba312499c81)`(Action< `[RecallAccess](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/recall-access#class_google_play_games_1_1_basic_api_1_1_recall_access)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `void` Requests Recall Access to[Player](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player#class_google_play_games_1_1_basic_api_1_1_player)Games Services for the currently signed in account                           |
| [RequestServerSideAccess](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1ad528750025ee1125247f1cbea5e67efb)`(bool forceRefreshToken, Action< string > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `void` Requests server-side access to[Player](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player#class_google_play_games_1_1_basic_api_1_1_player)Games Services for the currently signed in player.                      |
| [RequestServerSideAccess](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1a14bd73fe7da28520eb783756c7a79a66)`(bool forceRefreshToken, List< `[AuthScope](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1ab5415b6b4ad0724108f447b203380e44)` > scopes, Action< `[AuthResponse](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/auth-response#class_google_play_games_1_1_basic_api_1_1_auth_response)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `void` Requests server-side access to Play Games Services for the currently signed in player.                                                                                                                                                                             |
| [RevealAchievement](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1a38d1c13c432a9a5bd5f5b5d970d979e5)`(string achievementId, Action< bool > successOrFailureCalllback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `void` Reveals the achievement with the passed identifier.                                                                                                                                                                                                                |
| [SetStepsAtLeast](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1a29ddb2b651beed3cb89d5916b9357249)`(string achId, int steps, Action< bool > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `void` Set an achievement to have at least the given number of steps completed.                                                                                                                                                                                           |
| [ShowAchievementsUI](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1a937c012d3da71695633e03a5b13b4ec0)`(Action< `[UIStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1aab0aa7dedba9c8167fff3a0deafaae52)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `void` Shows the appropriate platform-specific achievements UI.                                                                                                                                                                                                           |
| [ShowCompareProfileWithAlternativeNameHintsUI](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1abaaa7573af0160dbec1df442bf8053eb)`(string otherUserId, string otherPlayerInGameName, string currentPlayerInGameName, Action< `[UIStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1aab0aa7dedba9c8167fff3a0deafaae52)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `void` Shows the Play Games[Player](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player#class_google_play_games_1_1_basic_api_1_1_player)Profile UI for a specific user identifier.                                        |
| [ShowLeaderboardUI](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1a6fe5e62558dce82013eeb0996b7abeeb)`(string leaderboardId, `[LeaderboardTimeSpan](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1a8d9a7be92fea2b7a31420b073558fbce)` span, Action< `[UIStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1aab0aa7dedba9c8167fff3a0deafaae52)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `void` Shows the leaderboard UI for a specific leaderboard.                                                                                                                                                                                                               |
| [SubmitScore](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1a93e905df0fc4e5d81ecc8313473a8b82)`(string leaderboardId, long score, Action< bool > successOrFailureCalllback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `void` Submits the passed score to the passed leaderboard.                                                                                                                                                                                                                |
| [SubmitScore](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1a69e69d9c714fb383c8b6bb220cb090f4)`(string leaderboardId, long score, string metadata, Action< bool > successOrFailureCalllback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `void` Submits the score for the currently signed-in player.                                                                                                                                                                                                              |
| [UnlockAchievement](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1ab0dcf55acc3dc8f109f6971d83f84106)`(string achievementId, Action< bool > successOrFailureCalllback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `void` Unlocks the achievement with the passed identifier.                                                                                                                                                                                                                |

## Public functions

### AskForLoadFriendsResolution

```c#
void AskForLoadFriendsResolution(
  Action< UIStatus > callback
)
```  
Shows the appropriate platform-specific friends sharing UI.

<br />

|                                                                                          Details                                                                                          ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-----------------------------------------------------------------------| | `callback` | The callback to invoke when complete. If null, no callback is called. | |

### Authenticate

```c#
void Authenticate(
  Action< SignInStatus > callback
)
```  
Returns the result of the automatic sign-in attempt.

This returns the result

<br />

|                             Details                             ||
|------------|-----------------------------------------------------|
| Parameters | |------------|----------| | `callback` | Callback | |

### GetEventsClient

```c#
Events.IEventsClient GetEventsClient()
```  
Gets the events client.

<br />

|             Details             ||
|-------------|--------------------|
| **Returns** | The events client. |

### GetFriends

```c#
IUserProfile[] GetFriends()
```  

### GetFriendsListVisibility

```c#
void GetFriendsListVisibility(
  bool forceReload,
  Action< FriendsListVisibilityStatus > callback
)
```  
Returns if the user has allowed permission for the game to access the friends list.

<br />

|                                                                                                                                                                                                                                                                                                                  Details                                                                                                                                                                                                                                                                                                                  ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `forceReload` | If true, this call will clear any locally cached data and attempt to fetch the latest data from the server. Normally, this should be set to`false`to gain advantages of data caching. | | `callback`    | Callback invoked upon completion.                                                                                                                                                     | |

### GetLastLoadFriendsStatus

```c#
LoadFriendsStatus GetLastLoadFriendsStatus()
```  
Returns the latest LoadFriendsStatus obtained from loading friends.  

### GetPlayerStats

```c#
void GetPlayerStats(
  Action< CommonStatusCodes, PlayerStats > callback
)
```  
Gets the player stats.

<br />

|                                           Details                                           ||
|------------|---------------------------------------------------------------------------------|
| Parameters | |------------|------------------------| | `callback` | Callback for response. | |

### GetSavedGameClient

```c#
SavedGame.ISavedGameClient GetSavedGameClient()
```  
Gets the saved game client.

<br />

|               Details               ||
|-------------|------------------------|
| **Returns** | The saved game client. |

### GetUserDisplayName

```c#
string GetUserDisplayName()
```  
Returns a human readable name for the user, if they are logged in.

<br />

|                                   Details                                   ||
|-------------|----------------------------------------------------------------|
| **Returns** | The user's human-readable name. null if they are not logged in |

### GetUserId

```c#
string GetUserId()
```  
Returns the authenticated user's ID.

Note that this value may change if a user signs out and signs in with a different account.

<br />

|                            Details                             ||
|-------------|---------------------------------------------------|
| **Returns** | The user's ID, null if the user is not logged in. |

### GetUserImageUrl

```c#
string GetUserImageUrl()
```  
Returns the user's avatar url, if they are logged in and have an avatar.

<br />

|                                    Details                                    ||
|-------------|------------------------------------------------------------------|
| **Returns** | The URL to load the avatar image. null if they are not logged in |

### IncrementAchievement

```c#
void IncrementAchievement(
  string achievementId,
  int steps,
  Action< bool > successOrFailureCalllback
)
```  
Increments the achievement with the passed identifier.

If the operation succeeds, the callback will be invoked on the game thread with true. If the operation fails, the callback will be invoked with false. This operation will immediately fail if the user is not authenticated (i.e. the callback will immediately be invoked with false).

<br />

|                                                                                                                                                                                                                 Details                                                                                                                                                                                                                 ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------------------|----------------------------------------------------------------------| | `achievementId`             | The ID of the achievement to increment.                              | | `steps`                     | The number of steps to increment by.                                 | | `successOrFailureCalllback` | Callback used to indicate whether the operation succeeded or failed. | |

### IsAuthenticated

```c#
bool IsAuthenticated()
```  
Returns whether or not user is authenticated.

<br />

|                               Details                               ||
|-------------|--------------------------------------------------------|
| **Returns** | `true`if the user is authenticated; otherwise,`false`. |

### LeaderboardMaxResults

```c#
int LeaderboardMaxResults()
```  
Returns the max number of scores returned per call.

<br />

|            Details            ||
|-------------|------------------|
| **Returns** | The max results. |

### LoadAchievements

```c#
void LoadAchievements(
  Action< Achievement[]> callback
)
```  
Loads the achievements for the current signed in user and invokes the callback.  

### LoadFriends

```c#
void LoadFriends(
  Action< bool > callback
)
```  
Loads friends of the authenticated user.

This loads the entire list of friends.

<br />

|                                                                                     Details                                                                                     ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|------------------------------------------------------------------| | `callback` | Callback invoked when complete. bool argument indicates success. | |

### LoadFriends

```c#
void LoadFriends(
  int pageSize,
  bool forceReload,
  Action< LoadFriendsStatus > callback
)
```  
Loads the first page of the user's friends

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `pageSize`    | The number of entries to request for this initial page. Note that if cached data already exists, the returned buffer may contain more than this size, but it is guaranteed to contain at least this many if the collection contains enough records.            | | `forceReload` | If true, this call will clear any locally cached data and attempt to fetch the latest data from the server. This would commonly be used for something like a user-initiated refresh. Normally, this should be set to`false`to gain advantages of data caching. | | `callback`    | Callback invoked upon completion.                                                                                                                                                                                                                              | |

### LoadMoreFriends

```c#
void LoadMoreFriends(
  int pageSize,
  Action< LoadFriendsStatus > callback
)
```  
Loads the friends list page

<br />

|                                                                                                                                                                                                                                                                                                                                                                                              Details                                                                                                                                                                                                                                                                                                                                                                                               ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `pageSize` | The number of entries to request for this page. Note that if cached data already exists, the returned buffer may contain more than this size, but it is guaranteed to contain at least this many if the collection contains enough records. | | `callback` |                                                                                                                                                                                                                                             | |

### LoadMoreScores

```c#
void LoadMoreScores(
  ScorePageToken token,
  int rowCount,
  Action< LeaderboardScoreData > callback
)
```  
Loads the more scores for the leaderboard.

The token is accessed by calling[LoadScores()](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/i-play-games-client#interface_google_play_games_1_1_basic_api_1_1_i_play_games_client_1ac2f86d3ff84fede458823a521d896ae0)with a positive row count.

<br />

|                                                                                                                                                                     Details                                                                                                                                                                     ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-----------------------------------------------------------------| | `token`    | Token for tracking the score loading.                           | | `rowCount` | max number of scores to return. This can be limited by the SDK. | | `callback` | Callback.                                                       | |

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
Loads the score data for the given leaderboard.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ||
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `leaderboardId` | Leaderboard identifier.                                                                                                                                            | | `start`         | Start indicating the top scores or player centric                                                                                                                  | | `rowCount`      | max number of scores to return. non-positive indicates no rows should be returned. This causes only the summary info to be loaded. This can be limited by the SDK. | | `collection`    | leaderboard collection: public or social                                                                                                                           | | `timeSpan`      | leaderboard timespan                                                                                                                                               | | `callback`      | callback with the scores, and a page token. The token can be used to load next/prev pages.                                                                         | |

### LoadUsers

```c#
void LoadUsers(
  string[] userIds,
  Action< IUserProfile[]> callback
)
```  
Loads the users specified.

This is mainly used by the leaderboard APIs to get the information of a high scorer.

<br />

|                                                       Details                                                        ||
|------------|----------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-------------------| | `userIds`  | User identifiers. | | `callback` | Callback.         | |

### ManuallyAuthenticate

```c#
void ManuallyAuthenticate(
  Action< SignInStatus > callback
)
```  
Manually requests that your game performs sign in with Play Games Services.

Note that a sign-in attempt will be made automatically when your game's application started. For this reason most games will not need to manually request to perform sign-in unless the automatic sign-in attempt failed and your game requires access to Play Games Services.

<br />

|                      Details                      ||
|------------|---------------------------------------|
| Parameters | |------------|---| | `callback` |   | |

### RequestRecallAccessToken

```c#
void RequestRecallAccessToken(
  Action< RecallAccess > callback
)
```  
Requests Recall Access to[Player](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player#class_google_play_games_1_1_basic_api_1_1_player)Games Services for the currently signed in account

When requested a session id is returned that can be used by your game-server to use Recall Access APIs like LinkPerson , UnlinkPersona and get Details about Recall Tokens and corresponding personas. See<https://developer.android.com/games/pgs/recall?hl=en>.

<br />

|                      Details                      ||
|------------|---------------------------------------|
| Parameters | |------------|---| | `callback` |   | |

### RequestServerSideAccess

```c#
void RequestServerSideAccess(
  bool forceRefreshToken,
  Action< string > callback
)
```  
Requests server-side access to[Player](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player#class_google_play_games_1_1_basic_api_1_1_player)Games Services for the currently signed in player.

When requested an authorization code is returned that can be used by your game-server to exchange for an access token and conditionally a refresh token (when`forceRefreshToken`is true). The access token may then be used by your game-server to access the Play Games Services web APIs. This is commonly used to complete a sign-in flow by verifying the Play Games Services player id.

If`forceRefreshToken`is true, when exchanging the authorization code a refresh token will be returned in addition to the access token. The refresh token allows the game-server to request additional access tokens, allowing your game-server to continue accesses Play Games Services while the user is not actively playing your app.

|                                                                                                                                                                                                                                  Details                                                                                                                                                                                                                                   ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------|----------------------------------------------------------------------------------------------------------------------------| | `forceRefreshToken` | If`true`when the returned authorization code is exchanged a refresh token will be included in addition to an access token. | | `callback`          |                                                                                                                            | |

### RequestServerSideAccess

```c#
void RequestServerSideAccess(
  bool forceRefreshToken,
  List< AuthScope > scopes,
  Action< AuthResponse > callback
)
```  
Requests server-side access to Play Games Services for the currently signed in player.

An authorization code is returned when requested. Your server can then exchange this code for an access token (and conditionally a refresh token when`forceRefreshToken`is`true`). The access token allows your server to access the Play Games Services web APIs, which is often used to complete sign-in by verifying the Play Games Services player ID.

When`forceRefreshToken`is`true`during authorization code exchange, a refresh token is provided along with the access token. This refresh token enables your server to obtain new access tokens and continue accessing Play Games Services even when the user isn't actively playing. Note that refresh tokens are only generated for players who have auto sign-in setting enabled.

Scopes represent the[AuthScope](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1ab5415b6b4ad0724108f447b203380e44)values requested such as`AuthScope.EMAIL`,`AuthScope.PROFILE`,`AuthScope.OPEN_ID`. For new permissions, users will see a consent screen upon the first request. Granting consent (or if permissions were already granted) results in the[AuthResponse](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/auth-response#class_google_play_games_1_1_basic_api_1_1_auth_response)listing the effectively granted[AuthScope](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1ab5415b6b4ad0724108f447b203380e44). Declining permission results in an empty list of granted[AuthScope](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1ab5415b6b4ad0724108f447b203380e44)in the[AuthResponse](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/auth-response#class_google_play_games_1_1_basic_api_1_1_auth_response). Regardless of granted permissions, a successful request will always return the authorization code. param name="scopes"\>A list of[AuthScope](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1ab5415b6b4ad0724108f447b203380e44)values representing the OAuth 2.0 permissions being requested, such as`AuthScope.EMAIL`,`AuthScope.PROFILE`and`AuthScope.OPEN_ID`.

|                                                                                                                                                        Details                                                                                                                                                        ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------|----------------------------------------------------------------------------------------------------------------------------| | `forceRefreshToken` | If`true`when the returned authorization code is exchanged a refresh token will be included in addition to an access token. | |

A[Task](https://developer.android.com/games/services/unity/v2/api/other/)that completes with an[AuthResponse](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/auth-response#class_google_play_games_1_1_basic_api_1_1_auth_response)containing the OAuth 2.0 authorization code as a string and a list of the[AuthScope](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1ab5415b6b4ad0724108f447b203380e44)s that were effectively granted by the user (see description for details on consent). This authorization code can be exchanged by your server for an access token (and conditionally a refresh token) that can be used to access the Play Games Services web APIs and other Google Identity APIs.

|                      Details                      ||
|------------|---------------------------------------|
| Parameters | |------------|---| | `callback` |   | |

### RevealAchievement

```c#
void RevealAchievement(
  string achievementId,
  Action< bool > successOrFailureCalllback
)
```  
Reveals the achievement with the passed identifier.

If the operation succeeds, the callback will be invoked on the game thread with true. If the operation fails, the callback will be invoked with false. This operation will immediately fail if the user is not authenticated (i.e. the callback will immediately be invoked with false). If the achievement is already in a revealed state, this call will succeed immediately.

<br />

|                                                                                                                                                             Details                                                                                                                                                              ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------------------|----------------------------------------------------------------------| | `achievementId`             | The ID of the achievement to reveal.                                 | | `successOrFailureCalllback` | Callback used to indicate whether the operation succeeded or failed. | |

### SetStepsAtLeast

```c#
void SetStepsAtLeast(
  string achId,
  int steps,
  Action< bool > callback
)
```  
Set an achievement to have at least the given number of steps completed.

Calling this method while the achievement already has more steps than the provided value is a no-op. Once the achievement reaches the maximum number of steps, the achievement is automatically unlocked, and any further mutation operations are ignored.

<br />

|                                                                     Details                                                                     ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-----------------| | `achId`    | Ach identifier. | | `steps`    | Steps.          | | `callback` | Callback.       | |

### ShowAchievementsUI

```c#
void ShowAchievementsUI(
  Action< UIStatus > callback
)
```  
Shows the appropriate platform-specific achievements UI.

<br />

|                                                                                          Details                                                                                          ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-----------------------------------------------------------------------| | `callback` | The callback to invoke when complete. If null, no callback is called. | |

### ShowCompareProfileWithAlternativeNameHintsUI

```c#
void ShowCompareProfileWithAlternativeNameHintsUI(
  string otherUserId,
  string otherPlayerInGameName,
  string currentPlayerInGameName,
  Action< UIStatus > callback
)
```  
Shows the Play Games[Player](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player#class_google_play_games_1_1_basic_api_1_1_player)Profile UI for a specific user identifier.

<br />

|                                                                                                                                                                                                                                                     Details                                                                                                                                                                                                                                                      ||
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------------|------------------------------------------------------------------| | `otherUserId`             | User Identifier.                                                 | | `otherPlayerInGameName`   | The game's own display name of the player referred to by userId. | | `currentPlayerInGameName` | The game's own display name of the current player.               | | `callback`                | Callback invoked upon completion.                                | |

### ShowLeaderboardUI

```c#
void ShowLeaderboardUI(
  string leaderboardId,
  LeaderboardTimeSpan span,
  Action< UIStatus > callback
)
```  
Shows the leaderboard UI for a specific leaderboard.

If the passed ID is null, all leaderboards are displayed.

<br />

|                                                                                                                                                                                             Details                                                                                                                                                                                             ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------|------------------------------------------------------------------------| | `leaderboardId` | The leaderboard to display. null to display all.                       | | `span`          | Timespan to display for the leaderboard                                | | `callback`      | If non-null, the callback to invoke when the leaderboard is dismissed. | |

### SubmitScore

```c#
void SubmitScore(
  string leaderboardId,
  long score,
  Action< bool > successOrFailureCalllback
)
```  
Submits the passed score to the passed leaderboard.

This operation will immediately fail if the user is not authenticated (i.e. the callback will immediately be invoked with false).

<br />

|                                                                                                                                                                                                                 Details                                                                                                                                                                                                                 ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------------------|----------------------------------------------------------------------| | `leaderboardId`             | Leaderboard identifier.                                              | | `score`                     | Score.                                                               | | `successOrFailureCalllback` | Callback used to indicate whether the operation succeeded or failed. | |

### SubmitScore

```c#
void SubmitScore(
  string leaderboardId,
  long score,
  string metadata,
  Action< bool > successOrFailureCalllback
)
```  
Submits the score for the currently signed-in player.

<br />

|                                                                                                                                                         Details                                                                                                                                                         ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------------------|---------------------------| | `score`                     | Score.                    | | `leaderboardId`             | leaderboard id.           | | `metadata`                  | metadata about the score. | | `successOrFailureCalllback` | Callback upon completion. | |

### UnlockAchievement

```c#
void UnlockAchievement(
  string achievementId,
  Action< bool > successOrFailureCalllback
)
```  
Unlocks the achievement with the passed identifier.

If the operation succeeds, the callback will be invoked on the game thread with true. If the operation fails, the callback will be invoked with false. This operation will immediately fail if the user is not authenticated (i.e. the callback will immediately be invoked with false). If the achievement is already unlocked, this call will succeed immediately.

<br />

|                                                                                                                                                             Details                                                                                                                                                              ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------------------|----------------------------------------------------------------------| | `achievementId`             | The ID of the achievement to unlock.                                 | | `successOrFailureCalllback` | Callback used to indicate whether the operation succeeded or failed. | |