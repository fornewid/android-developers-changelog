---
title: GooglePlayGames.PlayGamesUserProfile Class Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-user-profile
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.




# GooglePlayGames.PlayGamesUserProfile

Represents a Google Play Games user profile.

## Summary

Implements the Unity's `IUserProfile` interface and is used as a base class for [PlayGamesLocalUser](/games/services/unity/v2/api/class/google-play-games/play-games-local-user#class_google_play_games_1_1_play_games_local_user).

### Inheritance

Inherits from: IUserProfile  
Direct Known Subclasses:[GooglePlayGames.BasicApi.Player](/games/services/unity/v2/api/class/google-play-games/basic-api/player), [GooglePlayGames.BasicApi.PlayerProfile](/games/services/unity/v2/api/class/google-play-games/basic-api/player-profile), [GooglePlayGames.PlayGamesLocalUser](/games/services/unity/v2/api/class/google-play-games/play-games-local-user)

| Properties | |
| --- | --- |
| `AvatarURL` | `string`  Gets the URL of the user's avatar. |
| `gameId` | `string`  Gets the user's game-specific identifier. |
| `id` | `string`  Gets the user's unique player ID. |
| `image` | `Texture2D`  Gets the user's avatar image as a Texture2D. |
| `isFriend` | `bool`  Gets a value indicating whether this user is a friend of the local user. |
| `state` | `UserState`  Gets the user's current state. |
| `userName` | `string`  Gets the user's display name. |

| Protected functions | |
| --- | --- |
| `ResetIdentity(string displayName, string playerId, string avatarUrl)` | `void`  Resets the user's identity with new information. |

| Public functions | |
| --- | --- |
| `Equals(object obj)` | `override bool`  Determines whether the specified System.Object is equal to the current [PlayGamesUserProfile](/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile). |
| `GetHashCode()` | `override int`  Serves as a hash function for a [PlayGamesUserProfile](/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile) object. |
| `ToString()` | `override string`  Returns a System.String that represents the current [PlayGamesUserProfile](/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile). |

## Properties

### AvatarURL

```
string AvatarURL
```

Gets the URL of the user's avatar.

### gameId

```
string gameId
```

Gets the user's game-specific identifier.

In this implementation, it is the same as the player ID.

### id

```
string id
```

Gets the user's unique player ID.

The player ID.

### image

```
Texture2D image
```

Gets the user's avatar image as a Texture2D.

The image is loaded asynchronously. Returns null until the image has been loaded.

The user's avatar image.

### isFriend

```
bool isFriend
```

Gets a value indicating whether this user is a friend of the local user.

`true` if this user is a friend; otherwise, `false`.

### state

```
UserState state
```

Gets the user's current state.

In this implementation, it always returns 'Online'.

### userName

```
string userName
```

Gets the user's display name.

The name of the user.

## Protected functions

### ResetIdentity

```
void ResetIdentity(
  string displayName,
  string playerId,
  string avatarUrl
)
```

Resets the user's identity with new information.

If the avatar URL has changed, the old image is discarded.

Details | || Parameters | |  |  | | --- | --- | | `displayName` | The new display name. | | `playerId` | The new player ID. | | `avatarUrl` | The new avatar URL. | |

## Public functions

### Equals

```
override bool Equals(
  object obj
)
```

Determines whether the specified System.Object is equal to the current [PlayGamesUserProfile](/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile).

Equality is based on the player ID.

Details | || Parameters | |  |  | | --- | --- | | `obj` | The System.Object to compare with the current [PlayGamesUserProfile](/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile). | |
| **Returns** | `true` if the specified object is equal to the current object; otherwise, `false`. |

### GetHashCode

```
override int GetHashCode()
```

Serves as a hash function for a [PlayGamesUserProfile](/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile) object.

Details | || **Returns** | A hash code for this instance that is suitable for use in hashing algorithms and data structures such as a hash table. |

### ToString

```
override string ToString()
```

Returns a System.String that represents the current [PlayGamesUserProfile](/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile).

Details | || **Returns** | A string representation of the object. |