---
title: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-local-user
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-local-user
source: md.txt
---

# GooglePlayGames.PlayGamesLocalUser Class Reference

# GooglePlayGames.PlayGamesLocalUser

Represents the Google Play Games local user, providing access to authentication and user-specific functionality.

## Summary

Implements Unity's`ILocalUser`interface.

### Inheritance

Inherits from:[GooglePlayGames.PlayGamesUserProfile](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-user-profile), ILocalUser

|                                                                                                                                               ### Properties                                                                                                                                                ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [AvatarURL](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-local-user#class_google_play_games_1_1_play_games_local_user_1a51150662cbd4c2955afb1898ffdf1d4a)     | `new string` Gets the URL of the user's avatar image.                                        |
| [authenticated](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-local-user#class_google_play_games_1_1_play_games_local_user_1ab8f1d6fbe6b60c79b500fb41f1839653) | `bool` Gets a value indicating whether the local user is authenticated to Google Play Games. |
| [friends](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-local-user#class_google_play_games_1_1_play_games_local_user_1a23c63e5a2954c705c16e1ddff2a9c14a)       | `IUserProfile[]` Gets the local user's friends.                                              |
| [id](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-local-user#class_google_play_games_1_1_play_games_local_user_1abccc69bf41e6181740dcf8b26a92b291)            | `new string` Gets the user's Google ID (Player ID).                                          |
| [isFriend](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-local-user#class_google_play_games_1_1_play_games_local_user_1aeaeb7d54b3b73451961ba9b8aaf72737)      | `new bool` Gets a value indicating whether this user is a friend of the local user.          |
| [state](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-local-user#class_google_play_games_1_1_play_games_local_user_1a3aee9494d5963d525f461f461302123d)         | `new UserState` Gets the user's state.                                                       |
| [underage](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-local-user#class_google_play_games_1_1_play_games_local_user_1a75290a932e7ed6234007261daed390dd)      | `bool` Gets a value indicating whether the user is underage.                                 |
| [userName](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-local-user#class_google_play_games_1_1_play_games_local_user_1ab7fe26ead243bd1e93710e66b4271453)      | `new string` Gets the display name of the local user.                                        |

|                                                                                                                                                                                                                                                                                                                                                   ### Public functions                                                                                                                                                                                                                                                                                                                                                    ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [Authenticate](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-local-user#class_google_play_games_1_1_play_games_local_user_1a3f4ec65ac968e23d25dc6c0a64a57745)`(Action< bool > callback)`                                                                                                                                                                                                                                                                                                                                                                              | `void` Authenticates the local user.                                                                |
| [Authenticate](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-local-user#class_google_play_games_1_1_play_games_local_user_1a15df75fef3908ed578f3bf516d320b56)`(Action< bool, string > callback)`                                                                                                                                                                                                                                                                                                                                                                      | `void` Authenticates the local user with an extended callback that includes the reason for failure. |
| [GetStats](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-local-user#class_google_play_games_1_1_play_games_local_user_1a8e8748009744baaa1b3209c575158466)`(Action< `[CommonStatusCodes](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1abaf59665136d25cef9ddd68d2069c603)`, `[PlayerStats](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats#class_google_play_games_1_1_basic_api_1_1_player_stats)` > callback)` | `void` Gets the player's stats from the server.                                                     |
| [LoadFriends](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-local-user#class_google_play_games_1_1_play_games_local_user_1a0b13f862b89657444f3cabf95db52c1c)`(Action< bool > callback)`                                                                                                                                                                                                                                                                                                                                                                               | `void` Loads the friends of the authenticated user.                                                 |

## Properties

### AvatarURL

```c#
new string AvatarURL
```  
Gets the URL of the user's avatar image.

The avatar image URL.  

### authenticated

```c#
bool authenticated
```  
Gets a value indicating whether the local user is authenticated to Google Play Games.

`true`if authenticated; otherwise,`false`.  

### friends

```c#
IUserProfile[] friends
```  
Gets the local user's friends.

This will be null until[LoadFriends](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-local-user#class_google_play_games_1_1_play_games_local_user_1a0b13f862b89657444f3cabf95db52c1c)completes.

An array of the user's friends, or null if not yet loaded.  

### id

```c#
new string id
```  
Gets the user's Google ID (Player ID).

This ID is persistent and uniquely identifies the user across all games. It is the preferred way to identify a player.

The user's Google ID.  

### isFriend

```c#
new bool isFriend
```  
Gets a value indicating whether this user is a friend of the local user.

Always returns`true`.  

### state

```c#
new UserState state
```  
Gets the user's state.

For the local user, this is always`UserState.Online`.  

### underage

```c#
bool underage
```  
Gets a value indicating whether the user is underage.

This is not implemented and returns`true`as a placeholder.  

### userName

```c#
new string userName
```  
Gets the display name of the local user.

The user's display name.

## Public functions

### Authenticate

```c#
void Authenticate(
  Action< bool > callback
)
```  
Authenticates the local user.

This is equivalent to calling PlayGamesPlatform.Authenticate(Action{SignInStatus}).

<br />

|                                                                            Details                                                                            ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|---------------------------------------------------------| | `callback` | A callback to invoke with a boolean indicating success. | |

### Authenticate

```c#
void Authenticate(
  Action< bool, string > callback
)
```  
Authenticates the local user with an extended callback that includes the reason for failure.

This is equivalent to calling PlayGamesPlatform.Authenticate(Action{SignInStatus}).

<br />

|                                                                                                               Details                                                                                                               ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|--------------------------------------------------------------------------------------------| | `callback` | A callback to invoke with a boolean indicating success and a string containing the status. | |

### GetStats

```c#
void GetStats(
  Action< CommonStatusCodes, PlayerStats > callback
)
```  
Gets the player's stats from the server.

<br />

|                                                                                                                                        Details                                                                                                                                        ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|---------------------------------------------------------------------------------------------------------------------| | `callback` | A callback to be invoked with the status code and the player's stats. The stats may be cached from a previous call. | |

### LoadFriends

```c#
void LoadFriends(
  Action< bool > callback
)
```  
Loads the friends of the authenticated user.

<br />

|                                                                            Details                                                                            ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|---------------------------------------------------------| | `callback` | A callback to invoke with a boolean indicating success. | |