---
title: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/auth-response
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/auth-response
source: md.txt
---

# GooglePlayGames.BasicApi.AuthResponse

Represents the response received from Play Games Services when requesting a server-side OAuth 2.0 authorization code for the signed-in player.

## Summary

| ### Constructors and Destructors ||
|---|---|
| [AuthResponse](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/auth-response#class_google_play_games_1_1_basic_api_1_1_auth_response_1a5c4d958ab85760c1ac31ab45507f88f4)`(string authCode, List< `[AuthScope](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1ab5415b6b4ad0724108f447b203380e44)` > grantedScopes)` Constructs an [AuthResponse](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/auth-response#class_google_play_games_1_1_basic_api_1_1_auth_response) with the provided granted scopes and authentication code. ||

| ### Public functions ||
|---|---|
| [Equals](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/auth-response#class_google_play_games_1_1_basic_api_1_1_auth_response_1a39a2403f5f1dcc8de41d6402b3d9af08)`(object obj)` | `override bool` |
| [GetAuthCode](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/auth-response#class_google_play_games_1_1_basic_api_1_1_auth_response_1af868a26d44d39e244eb16418595a43dc)`()` | `string` Gets the OAuth 2.0 authorization code. |
| [GetGrantedScopes](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/auth-response#class_google_play_games_1_1_basic_api_1_1_auth_response_1ae07475d535461a7ae0f36b74e9ffc494)`()` | `List< `[AuthScope](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1ab5415b6b4ad0724108f447b203380e44)` >` Gets the list of `AuthScope` permissions that the user has granted. |
| [GetHashCode](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/auth-response#class_google_play_games_1_1_basic_api_1_1_auth_response_1a70626483d8759bf5f9598f06be206f32)`()` | `override int` |
| [ToString](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/auth-response#class_google_play_games_1_1_basic_api_1_1_auth_response_1a316944d8587f98fce033736bd129a2bb)`()` | `override string` |

## Public functions

### AuthResponse

```c#
 AuthResponse(
  string authCode,
  List< AuthScope > grantedScopes
)
```  
Constructs an [AuthResponse](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/auth-response#class_google_play_games_1_1_basic_api_1_1_auth_response) with the provided granted scopes and authentication code.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `authCode` | The authentication code. | | `grantedScopes` | A list of `AuthScope` objects representing the granted scopes. | |
| Exceptions | |---|---| | `ArgumentNullException` | If `grantedScopes` is null. | |

### Equals

```c#
override bool Equals(
  object obj
)
```  

### GetAuthCode

```c#
string GetAuthCode()
```  
Gets the OAuth 2.0 authorization code.

This code is a short-lived credential that should be sent securely to your server to be exchanged for an access token and conditionally a refresh token.

<br />

| Details ||
|---|---|
| **Returns** | A string containing the OAuth 2.0 authorization code. |

### GetGrantedScopes

```c#
List< AuthScope > GetGrantedScopes()
```  
Gets the list of `AuthScope` permissions that the user has granted.

A list of the `AuthScope` permissions the user explicitly granted consent for (or previously approved). The list will be empty if the user declines consent and none of the requested `AuthScope` were previously granted.

<br />

| Details ||
|---|---|
| **Returns** | A `List` of `AuthScope` objects, representing the granted permissions. |

### GetHashCode

```c#
override int GetHashCode()
```  

### ToString

```c#
override string ToString()
```