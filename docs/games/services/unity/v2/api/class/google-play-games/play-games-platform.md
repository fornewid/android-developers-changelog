---
title: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform
source: md.txt
---

# GooglePlayGames.PlayGamesPlatform Class Reference

# GooglePlayGames.PlayGamesPlatform

Provides access to the Google Play Games platform.

## Summary

This is an implementation of UnityEngine.SocialPlatforms.ISocialPlatform. Activate this platform by calling the[Activate](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1afc68980eb29743625ae7ea74c1e99327)method, then authenticate by calling the[Authenticate](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a2743441943ae1a4f5916c47c6a93b0df)method. After authentication completes, you may call the other methods of this class. This is not a complete implementation of the ISocialPlatform interface. Methods lacking an implementation or whose behavior is at variance with the standard are noted as such.

### Inheritance

Inherits from: ISocialPlatform

|                                                                                                                                                                                                                                              ### Properties                                                                                                                                                                                                                                               ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [DebugLogEnabled](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a850e7ad93813230a847878b7e1d2de5c) | `static bool` Gets or sets a value indicating whether debug logs are enabled.                                                                                                                                                                                                                |
| [Events](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1addfe8a623f55d673d6f10a162636e9d1)          | [IEventsClient](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/events/i-events-client#interface_google_play_games_1_1_basic_api_1_1_events_1_1_i_events_client) Gets the events client object.                                              |
| [Instance](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a4895a06cafea42728ff73cb0435c136e)        | `static `[PlayGamesPlatform](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform) Gets the singleton instance of the Play Games platform.                                                  |
| [Nearby](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1ab9959795aee74bcec2f4849cfb3b7c7f)          | `static `[INearbyConnectionClient](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_nearby_connection_client) Gets the nearby connection client. |
| [SavedGame](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a8b73a196abc5f5ac682bafb92d8dad9c)       | [ISavedGameClient](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-saved-game-client#interface_google_play_games_1_1_basic_api_1_1_saved_game_1_1_i_saved_game_client) Gets the saved game client object.                       |
| [localUser](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1aa3f7c587a65e1fd099bb0bdbfe0014c5)       | `ILocalUser` Gets the local user.                                                                                                                                                                                                                                                            |

|                                                                                                                                                                                                                                                                                                                                                         ### Public static functions                                                                                                                                                                                                                                                                                                                                                         ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Activate](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1afc68980eb29743625ae7ea74c1e99327)`()`                                                                                                                                                                                                                                                                              | [PlayGamesPlatform](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform) Activates the Play Games platform as the implementation of Social.Active. |
| [InitializeNearby](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a31a54a14f96b74e06872a320d66e84ee)`(Action< `[INearbyConnectionClient](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-nearby-connection-client#interface_google_play_games_1_1_basic_api_1_1_nearby_1_1_i_nearby_connection_client)` > callback)` | `void` Initializes the nearby connection platform.                                                                                                                                                                                                   |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AddIdMapping](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a5f3b14568fa25fb25f2012549540b835)`(string fromId, string toId)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `void` Specifies that the ID`fromId`should be implicitly replaced by`toId`on any calls that take a leaderboard or achievement ID.                                                                                                               |
| [AskForLoadFriendsResolution](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1afc87ca34be206a64fe6ce9a0969f295c)`(Action< `[UIStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1aab0aa7dedba9c8167fff3a0deafaae52)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `void` Shows the appropriate platform-specific friends sharing UI.                                                                                                                                                                              |
| [Authenticate](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a2743441943ae1a4f5916c47c6a93b0df)`(Action< `[SignInStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1a7ac5abd21359fbbe3ea826b40143e5c6)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `void` Returns the result of the automatic sign-in attempt.                                                                                                                                                                                     |
| [Authenticate](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a31cf269d1386341275d2033fe2bdd2a9)`(ILocalUser unused, Action< bool > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `void` Provided for compatibility with ISocialPlatform.                                                                                                                                                                                         |
| [Authenticate](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1abd903cd223c5d8576bb8275625d143b3)`(ILocalUser unused, Action< bool, string > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `void` Provided for compatibility with ISocialPlatform.                                                                                                                                                                                         |
| [CreateAchievement](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a5a3c8132294dfa17c965377292ef3131)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `IAchievement` Creates an achievement object which may be subsequently used to report an achievement.                                                                                                                                           |
| [CreateLeaderboard](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a3f61a6cd7ed0864955972c76d346180d)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `ILeaderboard` Returns a leaderboard object that can be configured to load scores.                                                                                                                                                              |
| [GetFriendsListVisibility](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a41e52fabedb62822f1dcbdc791ef512c)`(bool forceReload, Action< `[FriendsListVisibilityStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1ae51eb6918fd8949e31a7d7888c93e664)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `void` Returns if the user has allowed permission for the game to access the friends list.                                                                                                                                                      |
| [GetLastLoadFriendsStatus](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a7dcacf4ca7cff4d9e7388c90689b1c86)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | [LoadFriendsStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1ac4592ce0c250daf4bf07792776f63708) Gets status of the last call to load friends. |
| [GetLoading](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a9555dc92333723ab50047f37687919f6)`(ILeaderboard board)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `bool` Check if the leaderboard is currently loading.                                                                                                                                                                                           |
| [GetPlayerStats](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a7d0d430e05e849a394b6d2cf5f90f02a)`(Action< `[CommonStatusCodes](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1abaf59665136d25cef9ddd68d2069c603)`, `[PlayerStats](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `void` Gets the player stats.                                                                                                                                                                                                                   |
| [GetUserDisplayName](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1ad33a89088ff06798207be4a1f808dc6c)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `string` Returns the user's display name.                                                                                                                                                                                                       |
| [GetUserId](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1ad2c68f0709dd3e2201e42ffa195b25b3)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `string` Returns the user's Google ID.                                                                                                                                                                                                          |
| [GetUserImageUrl](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1ae3c5daf64dfb3c59aa81e8e308b115c7)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `string` Returns the user's avatar URL if they have one.                                                                                                                                                                                        |
| [IncrementAchievement](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a00118ca719d9b61a9e62154ca9a99899)`(string achievementID, int steps, Action< bool > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `void` Increments an achievement.                                                                                                                                                                                                               |
| [IsAuthenticated](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1ae1ba863528f49f91e63a6ca9d7428765)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `bool` Determines whether the user is authenticated.                                                                                                                                                                                            |
| [LoadAchievementDescriptions](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a8c471dcd2d8aa2f1b753e7b65506e4d3)`(Action< IAchievementDescription[]> callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `void` Loads the Achievement descriptions.                                                                                                                                                                                                      |
| [LoadAchievements](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1aa36955e56367f489520edc16ba7994be)`(Action< IAchievement[]> callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `void` Loads the achievement state for the current user.                                                                                                                                                                                        |
| [LoadFriends](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a3d77eb44d7af0e75b84b76e05a19093b)`(ILocalUser user, Action< bool > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `void` Loads the friends that also play this game.                                                                                                                                                                                              |
| [LoadFriends](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1af7ae7dc4eb1652bb391de7e4477bf67f)`(int pageSize, bool forceReload, Action< `[LoadFriendsStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1ac4592ce0c250daf4bf07792776f63708)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `void` Loads the first page of the user's friends.                                                                                                                                                                                              |
| [LoadMoreFriends](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a3c2b167a53b55ec0c01fb5fac1571991)`(int pageSize, Action< `[LoadFriendsStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1ac4592ce0c250daf4bf07792776f63708)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `void` Loads the friends list page                                                                                                                                                                                                              |
| [LoadMoreScores](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1ae791a3698a14efeec5d73463531eeb8d)`(`[ScorePageToken](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/score-page-token#class_google_play_games_1_1_basic_api_1_1_score_page_token)` token, int rowCount, Action< `[LeaderboardScoreData](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/leaderboard-score-data#class_google_play_games_1_1_basic_api_1_1_leaderboard_score_data)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `void` Loads more scores.                                                                                                                                                                                                                       |
| [LoadScores](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a5be808426a316ffd4c91b48af57e6661)`(string leaderboardId, Action< IScore[]> callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `void` Loads the scores relative the player.                                                                                                                                                                                                    |
| [LoadScores](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a9a6d340efb24fd9f33b06b6e7a11ddb3)`(string leaderboardId, `[LeaderboardStart](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1abccf096f9fcbe7a3e572b64290675d18)` start, int rowCount, `[LeaderboardCollection](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1a33fac2add308ad7414106822f66bc681)` collection, `[LeaderboardTimeSpan](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1a8d9a7be92fea2b7a31420b073558fbce)` timeSpan, Action< `[LeaderboardScoreData](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/leaderboard-score-data#class_google_play_games_1_1_basic_api_1_1_leaderboard_score_data)` > callback)` | `void` Loads the scores using the provided parameters.                                                                                                                                                                                          |
| [LoadScores](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a38cef749ebfe965b2df84817be34fb86)`(ILeaderboard board, Action< bool > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `void` Loads the leaderboard based on the constraints in the leaderboard object.                                                                                                                                                                |
| [LoadUsers](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1adac2a3fe7f29a08c8077ab5234e4526c)`(string[] userIds, Action< IUserProfile[]> callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `void` Loads the users.                                                                                                                                                                                                                         |
| [ManuallyAuthenticate](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1aea04653464bdc830efc81882c60e4858)`(Action< `[SignInStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1a7ac5abd21359fbbe3ea826b40143e5c6)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `void` Manually requests that your game performs sign in with Play Games Services.                                                                                                                                                              |
| [ReportProgress](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a64dff72e31b512bdd15169c08852fb6d)`(string achievementID, double progress, Action< bool > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `void` Reports the progress of an achievement (reveal, unlock or increment).                                                                                                                                                                    |
| [ReportScore](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a9a51e50e3de344ec7c896d89ca600b1d)`(long score, string board, Action< bool > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `void` Reports a score to a leaderboard.                                                                                                                                                                                                        |
| [ReportScore](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a7188afce9744624359b5891f35ed927e)`(long score, string board, string metadata, Action< bool > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `void` Submits the score for the currently signed-in player to the leaderboard associated with a specific id and metadata (such as something the player did to earn the score).                                                                 |
| [RequestRecallAccess](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a330264f1e8c58a37bbf65bd3b2207531)`(Action< `[RecallAccess](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/recall-access#class_google_play_games_1_1_basic_api_1_1_recall_access)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `void` Requests access to the recall API.                                                                                                                                                                                                       |
| [RequestServerSideAccess](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1aed10805cf9f61c90d9f2a0e290c31fc5)`(bool forceRefreshToken, Action< string > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `void` Requests server-side access to Player Games Services for the currently signed in player.                                                                                                                                                 |
| [RequestServerSideAccess](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1ad073478e2601d6dab89ffc89f3fe71d8)`(bool forceRefreshToken, List< `[AuthScope](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1ab5415b6b4ad0724108f447b203380e44)` > scopes, Action< `[AuthResponse](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/auth-response#class_google_play_games_1_1_basic_api_1_1_auth_response)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `void` Requests server-side access to Player Games Services for the currently signed in player.                                                                                                                                                 |
| [RevealAchievement](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a41d1b992c9fcc83562fc14f889000afb)`(string achievementID, Action< bool > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `void` Reveals the achievement with the passed identifier.                                                                                                                                                                                      |
| [SetDefaultLeaderboardForUI](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1afc9822ee9fee41d589a7ef79933d6408)`(string lbid)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `void` Sets the default leaderboard for the leaderboard UI.                                                                                                                                                                                     |
| [SetStepsAtLeast](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1ac453088bb201e1d24609ff81383faad4)`(string achievementID, int steps, Action< bool > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `void` Set an achievement to have at least the given number of steps completed.                                                                                                                                                                 |
| [ShowAchievementsUI](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a2c6db5bcb3d813d12667c83f22eaecbf)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `void` Shows the standard Google Play Games achievements user interface, which allows the player to browse their achievements.                                                                                                                  |
| [ShowAchievementsUI](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a58fe1b549f297c67d35dc206f9192d1a)`(Action< `[UIStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1aab0aa7dedba9c8167fff3a0deafaae52)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `void` Shows the standard Google Play Games achievements user interface, which allows the player to browse their achievements.                                                                                                                  |
| [ShowCompareProfileWithAlternativeNameHintsUI](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a81ff4e3efe041eba297c69827f982107)`(string userId, string otherPlayerInGameName, string currentPlayerInGameName, Action< `[UIStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1aab0aa7dedba9c8167fff3a0deafaae52)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `void` Shows the Player Profile UI for the given user identifier.                                                                                                                                                                               |
| [ShowLeaderboardUI](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a89d9409cc48dadfa19ba73df80e8db4d)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `void` Shows the standard Google Play Games leaderboards user interface, which allows the player to browse their leaderboards.                                                                                                                  |
| [ShowLeaderboardUI](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a8abedaa65a3c5a6af0863b19f73cd36a)`(string leaderboardId)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `void` Shows the standard Google Play Games leaderboard UI for the given leaderboard.                                                                                                                                                           |
| [ShowLeaderboardUI](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a21f38c4dcdbb5881579878e6b43bf191)`(string leaderboardId, Action< `[UIStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1aab0aa7dedba9c8167fff3a0deafaae52)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `void` Shows the leaderboard UI and calls the specified callback upon completion.                                                                                                                                                               |
| [ShowLeaderboardUI](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1ab25ffb2515af8cb190ab0c03e654e01b)`(string leaderboardId, `[LeaderboardTimeSpan](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1a8d9a7be92fea2b7a31420b073558fbce)` span, Action< `[UIStatus](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1aab0aa7dedba9c8167fff3a0deafaae52)` > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `void` Shows the leaderboard UI and calls the specified callback upon completion.                                                                                                                                                               |
| [UnlockAchievement](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1aad8f51e28cd76102410c4b82b0bdc76e)`(string achievementID, Action< bool > callback)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `void` Unlocks the achievement with the passed identifier.                                                                                                                                                                                      |

## Properties

### DebugLogEnabled

```c#
static bool DebugLogEnabled
```  
Gets or sets a value indicating whether debug logs are enabled.

This property may be set before calling[Activate](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1afc68980eb29743625ae7ea74c1e99327)method.

<br />

|                           Details                           ||
|-------------|------------------------------------------------|
| **Returns** | `true`if debug log enabled; otherwise,`false`. |

### Events

```c#
IEventsClient Events
```  
Gets the events client object.

The events client.  

### Instance

```c#
static PlayGamesPlatform Instance
```  
Gets the singleton instance of the Play Games platform.

<br />

|          Details           ||
|-------------|---------------|
| **Returns** | The instance. |

### Nearby

```c#
static INearbyConnectionClient Nearby
```  
Gets the nearby connection client.

NOTE: Can be null until the nearby client is initialized. Call InitializeNearby to use callback to be notified when initialization is complete.

The nearby.  

### SavedGame

```c#
ISavedGameClient SavedGame
```  
Gets the saved game client object.

The saved game client.  

### localUser

```c#
ILocalUser localUser
```  
Gets the local user.

<br />

|           Details            ||
|-------------|-----------------|
| **Returns** | The local user. |

## Public static functions

### Activate

```c#
PlayGamesPlatform Activate()
```  
Activates the Play Games platform as the implementation of Social.Active.

After calling this method, you can call methods on Social.Active. For example,`Social.Active.Authenticate()`.

<br />

|                                                                                                    Details                                                                                                    ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The singleton[PlayGamesPlatform](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform)instance. |

### InitializeNearby

```c#
void InitializeNearby(
  Action< INearbyConnectionClient > callback
)
```  
Initializes the nearby connection platform.

This call initializes the nearby connection platform. This is independent of the Play Game Services initialization. Multiple calls to this method are ignored.

<br />

|                                                    Details                                                    ||
|------------|---------------------------------------------------------------------------------------------------|
| Parameters | |------------|---------------------------------| | `callback` | Callback invoked when complete. | |

## Public functions

### AddIdMapping

```c#
void AddIdMapping(
  string fromId,
  string toId
)
```  
Specifies that the ID`fromId`should be implicitly replaced by`toId`on any calls that take a leaderboard or achievement ID.

After a mapping is registered, you can use`fromId`instead of`toId`when making a call. For example, the following two snippets are equivalent:`ReportProgress("Cfiwjew894_AQ", 100.0, callback);`is equivalent to:`AddIdMapping("super-combo", "Cfiwjew894_AQ");``ReportProgress("super-combo", 100.0, callback);`

<br />

|                                                                                              Details                                                                                               ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |----------|-----------------------------------------------| | `fromId` | The identifier to map.                        | | `toId`   | The identifier that`fromId`will be mapped to. | |

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

Play Games SDK automatically prompts users to sign in when the game is started. This API is useful for understanding if your game has access to Play Games Services and should be used when your game is started in order to conditionally enable or disable your Play Games Services integration.

<br />

|                                                                       Details                                                                       ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|----------------------------------------------------| | `callback` | The callback to call when authentication finishes. | |

### Authenticate

```c#
void Authenticate(
  ILocalUser unused,
  Action< bool > callback
)
```  
Provided for compatibility with ISocialPlatform.

**See also:**Authenticate(Action\<bool\>,bool)

|                                                                                           Details                                                                                            ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-------------------------------------------| | `unused`   | Unused parameter for this implementation. | | `callback` | Callback invoked when complete.           | |

### Authenticate

```c#
void Authenticate(
  ILocalUser unused,
  Action< bool, string > callback
)
```  
Provided for compatibility with ISocialPlatform.

**See also:**Authenticate(Action\<bool\>,bool)

|                                                                                           Details                                                                                            ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-------------------------------------------| | `unused`   | Unused parameter for this implementation. | | `callback` | Callback invoked when complete.           | |

### CreateAchievement

```c#
IAchievement CreateAchievement()
```  
Creates an achievement object which may be subsequently used to report an achievement.

<br />

|               Details                ||
|-------------|-------------------------|
| **Returns** | The achievement object. |

### CreateLeaderboard

```c#
ILeaderboard CreateLeaderboard()
```  
Returns a leaderboard object that can be configured to load scores.

<br />

|               Details                ||
|-------------|-------------------------|
| **Returns** | The leaderboard object. |

### GetFriendsListVisibility

```c#
void GetFriendsListVisibility(
  bool forceReload,
  Action< FriendsListVisibilityStatus > callback
)
```  
Returns if the user has allowed permission for the game to access the friends list.

<br />

|                                                                                                                                                                                                                                                                                                                   Details                                                                                                                                                                                                                                                                                                                    ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `forceReload` | If`true`, this call will clear any locally cached data and attempt to fetch the latest data from the server. Normally, this should be set to`false`to gain advantages of data caching. | | `callback`    | Callback invoked upon completion.                                                                                                                                                      | |

### GetLastLoadFriendsStatus

```c#
LoadFriendsStatus GetLastLoadFriendsStatus()
```  
Gets status of the last call to load friends.  

### GetLoading

```c#
bool GetLoading(
  ILeaderboard board
)
```  
Check if the leaderboard is currently loading.

<br />

|                                                                  Details                                                                   ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|--------------------------------------------------| | `board` | The leaderboard to check for loading in progress | |
| **Returns** | `true`, if loading was gotten,`false`otherwise.                                                                               |

### GetPlayerStats

```c#
void GetPlayerStats(
  Action< CommonStatusCodes, PlayerStats > callback
)
```  
Gets the player stats.

<br />

|                                                     Details                                                     ||
|------------|-----------------------------------------------------------------------------------------------------|
| Parameters | |------------|----------------------------------| | `callback` | Callback invoked when completed. | |

### GetUserDisplayName

```c#
string GetUserDisplayName()
```  
Returns the user's display name.

<br />

|                              Details                              ||
|-------------|------------------------------------------------------|
| **Returns** | The user display name. For example, "Bruno Oliveira" |

### GetUserId

```c#
string GetUserId()
```  
Returns the user's Google ID.

<br />

|                                                                             Details                                                                             ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The user's Google ID. No guarantees are made as to the meaning or format of this identifier except that it is unique to the user who is signed in. |

### GetUserImageUrl

```c#
string GetUserImageUrl()
```  
Returns the user's avatar URL if they have one.

<br />

|                                          Details                                           ||
|-------------|-------------------------------------------------------------------------------|
| **Returns** | The URL, or null if the user is not authenticated or does not have an avatar. |

### IncrementAchievement

```c#
void IncrementAchievement(
  string achievementID,
  int steps,
  Action< bool > callback
)
```  
Increments an achievement.

This is a Play Games extension of the ISocialPlatform API.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `achievementID` | The ID of the achievement to increment. This can be a raw Google Play Games achievement ID (alphanumeric string), or an alias that was previously configured by a call to[AddIdMapping](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a5f3b14568fa25fb25f2012549540b835). | | `steps`         | The number of steps to increment the achievement by.                                                                                                                                                                                                                                                                                                                               | | `callback`      | The callback to call to report the success or failure of the operation. The callback will be called with`true`to indicate success or`false`for failure.                                                                                                                                                                                                                            | |

### IsAuthenticated

```c#
bool IsAuthenticated()
```  
Determines whether the user is authenticated.

<br />

|                               Details                               ||
|-------------|--------------------------------------------------------|
| **Returns** | `true`if the user is authenticated; otherwise,`false`. |

### LoadAchievementDescriptions

```c#
void LoadAchievementDescriptions(
  Action< IAchievementDescription[]> callback
)
```  
Loads the Achievement descriptions.

<br />

|                                                             Details                                                             ||
|------------|---------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|------------------------------------------| | `callback` | The callback to receive the descriptions | |

### LoadAchievements

```c#
void LoadAchievements(
  Action< IAchievement[]> callback
)
```  
Loads the achievement state for the current user.

<br />

|                                                             Details                                                             ||
|------------|---------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|------------------------------------------| | `callback` | The callback to receive the achievements | |

### LoadFriends

```c#
void LoadFriends(
  ILocalUser user,
  Action< bool > callback
)
```  
Loads the friends that also play this game.

See loadConnectedPlayers.

This is a callback variant of LoadFriends. When completed, the friends list set in the user object, so they can accessed via the friends property as needed.

<br />

|                                                                            Details                                                                             ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|---------------------------------| | `user`     | The current local user          | | `callback` | Callback invoked when complete. | |

### LoadFriends

```c#
void LoadFriends(
  int pageSize,
  bool forceReload,
  Action< LoadFriendsStatus > callback
)
```  
Loads the first page of the user's friends.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `pageSize`    | The number of entries to request for this initial page. Note that if cached data already exists, the returned buffer may contain more than this size, but it is guaranteed to contain at least this many if the collection contains enough records.            | | `forceReload` | If true, this call will clear any locally cached data and attempt to fetch the latest data from the server. This would commonly be used for something like a user-initiated refresh. Normally, this should be set to`false`to gain advantages of data caching. | | `callback`    | Callback invoked upon completion with the status.                                                                                                                                                                                                              | |

### LoadMoreFriends

```c#
void LoadMoreFriends(
  int pageSize,
  Action< LoadFriendsStatus > callback
)
```  
Loads the friends list page

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                          Details                                                                                                                                                                                                                                                                                                                                                                                                           ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `pageSize` | The number of entries to request for this initial page. Note that if cached data already exists, the returned buffer may contain more than this size, but it is guaranteed to contain at least this many if the collection contains enough records. | | `callback` |                                                                                                                                                                                                                                                     | |

### LoadMoreScores

```c#
void LoadMoreScores(
  ScorePageToken token,
  int rowCount,
  Action< LeaderboardScoreData > callback
)
```  
Loads more scores.

This call may fail when trying to load friends with ResponseCode.ResolutionRequired if the user has not share the friends list with the game. In this case, use AskForLoadFriendsResolution to request access.

This is used to load the next "page" of scores.

<br />

|                                                                                                               Details                                                                                                               ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|--------------------------------------| | `token`    | Token used to recording the loading. | | `rowCount` | Row count.                           | | `callback` | Callback invoked when complete.      | |

### LoadScores

```c#
void LoadScores(
  string leaderboardId,
  Action< IScore[]> callback
)
```  
Loads the scores relative the player.

This returns the 25 (which is the max results returned by the SDK per call) scores that are around the player's score on the Public, all time leaderboard. Use the overloaded methods which are specific to GPGS to modify these parameters.

<br />

|                                                                                        Details                                                                                         ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------|------------------------------------| | `leaderboardId` | Leaderboard Id                     | | `callback`      | Callback to invoke when completed. | |

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
Loads the scores using the provided parameters.

This call may fail when trying to load friends with ResponseCode.ResolutionRequired if the user has not share the friends list with the game. In this case, use AskForLoadFriendsResolution to request access.

<br />

|                                                                                                                                                                                                                                             Details                                                                                                                                                                                                                                              ||
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------|----------------------------------------------| | `leaderboardId` | Leaderboard identifier.                      | | `start`         | Start either top scores, or player centered. | | `rowCount`      | Row count. the number of rows to return.     | | `collection`    | Collection. social or public                 | | `timeSpan`      | Time span. daily, weekly, all-time           | | `callback`      | Callback to invoke when completed.           | |

### LoadScores

```c#
void LoadScores(
  ILeaderboard board,
  Action< bool > callback
)
```  
Loads the leaderboard based on the constraints in the leaderboard object.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `board`    | The leaderboard object. This is created by calling[CreateLeaderboard()](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a3f61a6cd7ed0864955972c76d346180d), and then initialized appropriately. | | `callback` | Callback invoked when complete.                                                                                                                                                                                                                                                                        | |

### LoadUsers

```c#
void LoadUsers(
  string[] userIds,
  Action< IUserProfile[]> callback
)
```  
Loads the users.

<br />

|                                                                            Details                                                                             ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|---------------------------------| | `userIds`  | User identifiers.               | | `callback` | Callback invoked when complete. | |

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

### ReportProgress

```c#
void ReportProgress(
  string achievementID,
  double progress,
  Action< bool > callback
)
```  
Reports the progress of an achievement (reveal, unlock or increment).

This method attempts to implement the expected behavior of`ISocialPlatform.ReportProgress`as closely as possible, as described below. Although this method works with incremental achievements for compatibility purposes, calling this method for incremental achievements is not recommended, since the Play Games API exposes incremental achievements in a very different way than the interface presented by`ISocialPlatform.ReportProgress`. The implementation of this method for incremental achievements attempts to produce the correct result, but may be imprecise. If possible, call[IncrementAchievement](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a00118ca719d9b61a9e62154ca9a99899)instead.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `achievementID` | The ID of the achievement to unlock, reveal or increment. This can be a raw Google Play Games achievement ID (alphanumeric string), or an alias that was previously configured by a call to[AddIdMapping](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a5f3b14568fa25fb25f2012549540b835).                                                                                                                                             | | `progress`      | Progress of the achievement. If the achievement is standard (not incremental), then a progress of 0.0 will reveal the achievement and 100.0 will unlock it. Behavior of other values is undefined. If the achievement is incremental, then this value is interpreted as the total percentage of the achievement's progress that the player should have as a result of this call (regardless of the progress they had before). So if the player's previous progress was 30% and this call specifies 50.0, the new progress will be 50% (not 80%). | | `callback`      | Callback that will be called to report the result of the operation:`true`on success,`false`otherwise.                                                                                                                                                                                                                                                                                                                                                                                                                                            | |

### ReportScore

```c#
void ReportScore(
  long score,
  string board,
  Action< bool > callback
)
```  
Reports a score to a leaderboard.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `score`    | The score to report.                                                                                                                                                                                                                                                                                                                                               | | `board`    | The ID of the leaderboard on which the score is to be posted. This may be a raw Google Play Games leaderboard ID or an alias configured through a call to[AddIdMapping](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a5f3b14568fa25fb25f2012549540b835). | | `callback` | The callback to call to report the success or failure of the operation. The callback will be called with`true`to indicate success or`false`for failure.                                                                                                                                                                                                            | |

### ReportScore

```c#
void ReportScore(
  long score,
  string board,
  string metadata,
  Action< bool > callback
)
```  
Submits the score for the currently signed-in player to the leaderboard associated with a specific id and metadata (such as something the player did to earn the score).

<br />

|                                                                                                                                  Details                                                                                                                                   ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-----------------------------------| | `score`    | Score to report.                  | | `board`    | leaderboard id.                   | | `metadata` | metadata about the score.         | | `callback` | Callback invoked upon completion. | |

### RequestRecallAccess

```c#
void RequestRecallAccess(
  Action< RecallAccess > callback
)
```  
Requests access to the recall API.

<br />

|                                                                   Details                                                                   ||
|------------|---------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|------------------------------------------------| | `callback` | The callback to invoke with the recall access. | |

### RequestServerSideAccess

```c#
void RequestServerSideAccess(
  bool forceRefreshToken,
  Action< string > callback
)
```  
Requests server-side access to Player Games Services for the currently signed in player.

When requested an authorization code is returned that can be used by your game-server to exchange for an access token and conditionally a refresh token (when`forceRefreshToken`is true). The access token may then be used by your game-server to access the Play Games Services web APIs. This is commonly used to complete a sign-in flow by verifying the Play Games Services player id.

If`forceRefreshToken`is true, when exchanging the authorization code a refresh token will be returned in addition to the access token. The refresh token allows the game-server to request additional access tokens, allowing your game-server to continue accesses Play Games Services while the user is not actively playing your app.

<br />

|                                                                                                                                                                Details                                                                                                                                                                 ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------|--------------------------------------------------------------------------------| | `forceRefreshToken` | If set to`true`, a refresh token will be returned along with the access token. | | `callback`          | The callback to invoke with the server authorization code.                     | |

### RequestServerSideAccess

```c#
void RequestServerSideAccess(
  bool forceRefreshToken,
  List< AuthScope > scopes,
  Action< AuthResponse > callback
)
```  
Requests server-side access to Player Games Services for the currently signed in player.

When requested an authorization code is returned that can be used by your game-server to exchange for an access token and conditionally a refresh token (when`forceRefreshToken`is true). The access token may then be used by your game-server to access the Play Games Services web APIs. This is commonly used to complete a sign-in flow by verifying the Play Games Services player id.

If`forceRefreshToken`is true, when exchanging the authorization code a refresh token will be returned in addition to the access token. The refresh token allows the game-server to request additional access tokens, allowing your game-server to continue accesses Play Games Services while the user is not actively playing your app.

<br />

|                                                                                                                                                                                                                     Details                                                                                                                                                                                                                     ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------|--------------------------------------------------------------------------------| | `forceRefreshToken` | If set to`true`, a refresh token will be returned along with the access token. | | `scopes`            | The OAuth 2.0 scopes to request access to.                                     | | `callback`          | The callback to invoke with the AuthResponse.                                  | |

### RevealAchievement

```c#
void RevealAchievement(
  string achievementID,
  Action< bool > callback
)
```  
Reveals the achievement with the passed identifier.

This is a Play Games extension of the ISocialPlatform API.

If the operation succeeds, the callback will be invoked on the game thread with`true`. If the operation fails, the callback will be invoked with`false`. This operation will immediately fail if the user is not authenticated (the callback will immediately be invoked with false). If the achievement is already in a revealed state, this call will succeed immediately.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `achievementID` | The ID of the achievement to increment. This can be a raw Google Play Games achievement ID (alphanumeric string), or an alias that was previously configured by a call to[AddIdMapping](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a5f3b14568fa25fb25f2012549540b835). | | `callback`      | The callback to call to report the success or failure of the operation. The callback will be called with`true`to indicate success or`false`for failure.                                                                                                                                                                                                                            | |

### SetDefaultLeaderboardForUI

```c#
void SetDefaultLeaderboardForUI(
  string lbid
)
```  
Sets the default leaderboard for the leaderboard UI.

After calling this method, a call to[ShowLeaderboardUI](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a89d9409cc48dadfa19ba73df80e8db4d)will show only the specified leaderboard instead of showing the list of all leaderboards.

<br />

|                                                                                                                                                                                                                                                                                                                                                                             Details                                                                                                                                                                                                                                                                                                                                                                             ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `lbid` | The ID of the leaderboard to display on the default UI. This may be a raw Google Play Games leaderboard ID or an alias configured through a call to[AddIdMapping](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a5f3b14568fa25fb25f2012549540b835). | |

### SetStepsAtLeast

```c#
void SetStepsAtLeast(
  string achievementID,
  int steps,
  Action< bool > callback
)
```  
Set an achievement to have at least the given number of steps completed.

Calling this method while the achievement already has more steps than the provided value is a no-op. Once the achievement reaches the maximum number of steps, the achievement is automatically unlocked, and any further mutation operations are ignored.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `achievementID` | The ID of the achievement to increment. This can be a raw Google Play Games achievement ID (alphanumeric string), or an alias that was previously configured by a call to[AddIdMapping](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a5f3b14568fa25fb25f2012549540b835). | | `steps`         | The number of steps to increment the achievement by.                                                                                                                                                                                                                                                                                                                               | | `callback`      | The callback to call to report the success or failure of the operation. The callback will be called with`true`to indicate success or`false`for failure.                                                                                                                                                                                                                            | |

### ShowAchievementsUI

```c#
void ShowAchievementsUI()
```  
Shows the standard Google Play Games achievements user interface, which allows the player to browse their achievements.  

### ShowAchievementsUI

```c#
void ShowAchievementsUI(
  Action< UIStatus > callback
)
```  
Shows the standard Google Play Games achievements user interface, which allows the player to browse their achievements.

<br />

|                                                                                              Details                                                                                              ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|---------------------------------------------------------------------------| | `callback` | If non-null, the callback is invoked when the achievement UI is dismissed | |

### ShowCompareProfileWithAlternativeNameHintsUI

```c#
void ShowCompareProfileWithAlternativeNameHintsUI(
  string userId,
  string otherPlayerInGameName,
  string currentPlayerInGameName,
  Action< UIStatus > callback
)
```  
Shows the Player Profile UI for the given user identifier.

<br />

|                                                                                                                                                                                                                                                     Details                                                                                                                                                                                                                                                      ||
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------------|------------------------------------------------------------------| | `userId`                  | User Identifier.                                                 | | `otherPlayerInGameName`   | The game's own display name of the player referred to by userId. | | `currentPlayerInGameName` | The game's own display name of the current player.               | | `callback`                | Callback invoked upon completion.                                | |

### ShowLeaderboardUI

```c#
void ShowLeaderboardUI()
```  
Shows the standard Google Play Games leaderboards user interface, which allows the player to browse their leaderboards.

If you have configured a specific leaderboard as the default through a call to[SetDefaultLeaderboardForUI](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1afc9822ee9fee41d589a7ef79933d6408), the UI will show that specific leaderboard only. Otherwise, a list of all the leaderboards will be shown.  

### ShowLeaderboardUI

```c#
void ShowLeaderboardUI(
  string leaderboardId
)
```  
Shows the standard Google Play Games leaderboard UI for the given leaderboard.

<br />

|                                                                                                                                                                                                                                                                                                                                                                    Details                                                                                                                                                                                                                                                                                                                                                                    ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `leaderboardId` | The ID of the leaderboard to display. This may be a raw Google Play Games leaderboard ID or an alias configured through a call to[AddIdMapping](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a5f3b14568fa25fb25f2012549540b835). | |

### ShowLeaderboardUI

```c#
void ShowLeaderboardUI(
  string leaderboardId,
  Action< UIStatus > callback
)
```  
Shows the leaderboard UI and calls the specified callback upon completion.

<br />

|                                                                                                                     Details                                                                                                                     ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------|-------------------------------------------------------| | `leaderboardId` | leaderboard ID, can be null meaning all leaderboards. | | `callback`      | Callback to call. If null, nothing is called.         | |

### ShowLeaderboardUI

```c#
void ShowLeaderboardUI(
  string leaderboardId,
  LeaderboardTimeSpan span,
  Action< UIStatus > callback
)
```  
Shows the leaderboard UI and calls the specified callback upon completion.

<br />

|                                                                                                                                                           Details                                                                                                                                                           ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------|-------------------------------------------------------| | `leaderboardId` | leaderboard ID, can be null meaning all leaderboards. | | `span`          | Timespan to display scores in the leaderboard.        | | `callback`      | Callback to call. If null, nothing is called.         | |

### UnlockAchievement

```c#
void UnlockAchievement(
  string achievementID,
  Action< bool > callback
)
```  
Unlocks the achievement with the passed identifier.

This is a Play Games extension of the ISocialPlatform API.

If the operation succeeds, the callback will be invoked on the game thread with`true`. If the operation fails, the callback will be invoked with false. This operation will immediately fail if the user is not authenticated (the callback will immediately be invoked with`false`). If the achievement is already unlocked, this call will succeed immediately.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `achievementID` | The ID of the achievement to increment. This can be a raw Google Play Games achievement ID (alphanumeric string), or an alias that was previously configured by a call to[AddIdMapping](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-platform#class_google_play_games_1_1_play_games_platform_1a5f3b14568fa25fb25f2012549540b835). | | `callback`      | The callback to call to report the success or failure of the operation. The callback will be called with`true`to indicate success or`false`for failure.                                                                                                                                                                                                                            | |