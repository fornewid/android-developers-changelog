---
title: GooglePlayGames.PlayGamesLocalUser Class Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-local-user
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.




# GooglePlayGames.PlayGamesLocalUser

Represents the Google Play Games local user, providing access to authentication and user-specific functionality.

## Summary

Implements Unity's `ILocalUser` interface.

### Inheritance

Inherits from: [GooglePlayGames.PlayGamesUserProfile](/games/services/unity/v2/api/class/google-play-games/play-games-user-profile), ILocalUser

| Properties | |
| --- | --- |
| `AvatarURL` | `new string`  Gets the URL of the user's avatar image. |
| `authenticated` | `bool`  Gets a value indicating whether the local user is authenticated to Google Play Games. |
| `friends` | `IUserProfile[]`  Gets the local user's friends. |
| `id` | `new string`  Gets the user's Google ID (Player ID). |
| `isFriend` | `new bool`  Gets a value indicating whether this user is a friend of the local user. |
| `state` | `new UserState`  Gets the user's state. |
| `underage` | `bool`  Gets a value indicating whether the user is underage. |
| `userName` | `new string`  Gets the display name of the local user. |

| Public functions | |
| --- | --- |
| `Authenticate(Action< bool > callback)` | `void`  Authenticates the local user. |
| `Authenticate(Action< bool, string > callback)` | `void`  Authenticates the local user with an extended callback that includes the reason for failure. |
| `GetStats(Action< CommonStatusCodes, PlayerStats > callback)` | `void`  Gets the player's stats from the server. |
| `LoadFriends(Action< bool > callback)` | `void`  Loads the friends of the authenticated user. |

## Properties

### AvatarURL

```
new string AvatarURL
```

Gets the URL of the user's avatar image.

The avatar image URL.

### authenticated

```
bool authenticated
```

Gets a value indicating whether the local user is authenticated to Google Play Games.

`true` if authenticated; otherwise, `false`.

### friends

```
IUserProfile[] friends
```

Gets the local user's friends.

This will be null until [LoadFriends](/games/services/unity/v2/api/class/google-play-games/play-games-local-user#class_google_play_games_1_1_play_games_local_user_1a0b13f862b89657444f3cabf95db52c1c) completes.

An array of the user's friends, or null if not yet loaded.

### id

```
new string id
```

Gets the user's Google ID (Player ID).

This ID is persistent and uniquely identifies the user across all games. It is the preferred way to identify a player.

The user's Google ID.

### isFriend

```
new bool isFriend
```

Gets a value indicating whether this user is a friend of the local user.

Always returns `true`.

### state

```
new UserState state
```

Gets the user's state.

For the local user, this is always `UserState.Online`.

### underage

```
bool underage
```

Gets a value indicating whether the user is underage.

This is not implemented and returns `true` as a placeholder.

### userName

```
new string userName
```

Gets the display name of the local user.

The user's display name.

## Public functions

### Authenticate

```
void Authenticate(
  Action< bool > callback
)
```

Authenticates the local user.

This is equivalent to calling PlayGamesPlatform.Authenticate(Action{SignInStatus}).

Details | || Parameters | |  |  | | --- | --- | | `callback` | A callback to invoke with a boolean indicating success. | |

### Authenticate

```
void Authenticate(
  Action< bool, string > callback
)
```

Authenticates the local user with an extended callback that includes the reason for failure.

This is equivalent to calling PlayGamesPlatform.Authenticate(Action{SignInStatus}).

Details | || Parameters | |  |  | | --- | --- | | `callback` | A callback to invoke with a boolean indicating success and a string containing the status. | |

### GetStats

```
void GetStats(
  Action< CommonStatusCodes, PlayerStats > callback
)
```

Gets the player's stats from the server.

Details | || Parameters | |  |  | | --- | --- | | `callback` | A callback to be invoked with the status code and the player's stats. The stats may be cached from a previous call. | |

### LoadFriends

```
void LoadFriends(
  Action< bool > callback
)
```

Loads the friends of the authenticated user.

Details | || Parameters | |  |  | | --- | --- | | `callback` | A callback to invoke with a boolean indicating success. | |