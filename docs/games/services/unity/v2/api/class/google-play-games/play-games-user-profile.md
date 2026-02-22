---
title: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-user-profile
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-user-profile
source: md.txt
---

# GooglePlayGames.PlayGamesUserProfile Class Reference

# GooglePlayGames.PlayGamesUserProfile

Represents a Google Play Games user profile.

## Summary

Implements the Unity's`IUserProfile`interface and is used as a base class for[PlayGamesLocalUser](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-local-user#class_google_play_games_1_1_play_games_local_user).

### Inheritance

Inherits from: IUserProfile  
Direct Known Subclasses:[GooglePlayGames.BasicApi.Player](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player),[GooglePlayGames.BasicApi.PlayerProfile](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/player-profile),[GooglePlayGames.PlayGamesLocalUser](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-local-user)

|                                                                                                                                         ### Properties                                                                                                                                         ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [AvatarURL](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile_1a71d39715173c138166e268a494ec52f2) | `string` Gets the URL of the user's avatar.                                     |
| [gameId](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile_1a0996268384dbaea0b6c00d21acec5bf1)    | `string` Gets the user's game-specific identifier.                              |
| [id](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile_1ab820dee129b6a7fe2fc576030a711f18)        | `string` Gets the user's unique player ID.                                      |
| [image](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile_1aad98593bbb94b66094fd42039b57f8b4)     | `Texture2D` Gets the user's avatar image as a Texture2D.                        |
| [isFriend](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile_1ade393e3e3c3f7c3ece086c1bcc7efd1d)  | `bool` Gets a value indicating whether this user is a friend of the local user. |
| [state](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile_1a5e31dd6d1d8e7b62c469d7ffcfbe5503)     | `UserState` Gets the user's current state.                                      |
| [userName](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile_1af55c5392ac08e0387b47927fc4e9b1c3)  | `string` Gets the user's display name.                                          |

|                                                                                                                                                       ### Protected functions                                                                                                                                                       ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| [ResetIdentity](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile_1a78ab519b9474193dc0989dd16f931693)`(string displayName, string playerId, string avatarUrl)` | `void` Resets the user's identity with new information. |

|                                                                                                                                                                                                                                          ### Public functions                                                                                                                                                                                                                                          ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Equals](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile_1acfe2689b25bcbd7bf0a5d6fde380de3f)`(object obj)` | `override bool` Determines whether the specified System.Object is equal to the current[PlayGamesUserProfile](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile). |
| [GetHashCode](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile_1a30acefa44308b433ee352ba16e4029dd)`()`      | `override int` Serves as a hash function for a[PlayGamesUserProfile](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile)object.                                   |
| [ToString](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile_1adf64a14193feef41a37d554d2599a03a)`()`         | `override string` Returns a System.String that represents the current[PlayGamesUserProfile](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile).                  |

## Properties

### AvatarURL

```c#
string AvatarURL
```  
Gets the URL of the user's avatar.  

### gameId

```c#
string gameId
```  
Gets the user's game-specific identifier.

In this implementation, it is the same as the player ID.  

### id

```c#
string id
```  
Gets the user's unique player ID.

The player ID.  

### image

```c#
Texture2D image
```  
Gets the user's avatar image as a Texture2D.

The image is loaded asynchronously. Returns null until the image has been loaded.

The user's avatar image.  

### isFriend

```c#
bool isFriend
```  
Gets a value indicating whether this user is a friend of the local user.

`true`if this user is a friend; otherwise,`false`.  

### state

```c#
UserState state
```  
Gets the user's current state.

In this implementation, it always returns 'Online'.  

### userName

```c#
string userName
```  
Gets the user's display name.

The name of the user.

## Protected functions

### ResetIdentity

```c#
void ResetIdentity(
  string displayName,
  string playerId,
  string avatarUrl
)
```  
Resets the user's identity with new information.

If the avatar URL has changed, the old image is discarded.

<br />

|                                                                                       Details                                                                                       ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------|-----------------------| | `displayName` | The new display name. | | `playerId`    | The new player ID.    | | `avatarUrl`   | The new avatar URL.   | |

## Public functions

### Equals

```c#
override bool Equals(
  object obj
)
```  
Determines whether the specified System.Object is equal to the current[PlayGamesUserProfile](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile).

Equality is based on the player ID.

<br />

|                                                                                                                                                                                                                                                   Details                                                                                                                                                                                                                                                    ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `obj` | The System.Object to compare with the current[PlayGamesUserProfile](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile). | |
| **Returns** | `true`if the specified object is equal to the current object; otherwise,`false`.                                                                                                                                                                                                                                                                                                                                                                                                                |

### GetHashCode

```c#
override int GetHashCode()
```  
Serves as a hash function for a[PlayGamesUserProfile](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile)object.

<br />

|                                                               Details                                                               ||
|-------------|------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A hash code for this instance that is suitable for use in hashing algorithms and data structures such as a hash table. |

### ToString

```c#
override string ToString()
```  
Returns a System.String that represents the current[PlayGamesUserProfile](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/play-games-user-profile#class_google_play_games_1_1_play_games_user_profile).

<br />

|                       Details                       ||
|-------------|----------------------------------------|
| **Returns** | A string representation of the object. |