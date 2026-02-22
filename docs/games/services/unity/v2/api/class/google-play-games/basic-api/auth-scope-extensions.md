---
title: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/auth-scope-extensions
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/auth-scope-extensions
source: md.txt
---

# GooglePlayGames.BasicApi.AuthScopeExtensions Class Reference

# GooglePlayGames.BasicApi.AuthScopeExtensions

Extensions for the AuthScope enum.

## Summary

These extensions are used to converting between the AuthScope enum and its string representation.

|                                                                                                                                                                                                                                                                                                                                           ### Public static functions                                                                                                                                                                                                                                                                                                                                            ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FromValue](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/auth-scope-extensions#class_google_play_games_1_1_basic_api_1_1_auth_scope_extensions_1a839f18d9a6eca8c850daaa62dae84e11)`(string value)`                                                                                                                                                                                              | [AuthScope](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1ab5415b6b4ad0724108f447b203380e44) Returns the AuthScope enum value corresponding to the provided string. |
| [GetValue](https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/auth-scope-extensions#class_google_play_games_1_1_basic_api_1_1_auth_scope_extensions_1accc57cce519a20b8923eb2abd8a3ef58)`(this `[AuthScope](https://developer.android.com/games/services/unity/v2/api/namespace/google-play-games/basic-api#namespace_google_play_games_1_1_basic_api_1ab5415b6b4ad0724108f447b203380e44)` authScope)` | `string` Returns the standard string representation of this OAuth 2.0 scope.                                                                                                                                                                                     |

## Public static functions

### FromValue

```c#
AuthScope FromValue(
  string value
)
```  
Returns the AuthScope enum value corresponding to the provided string.

<br />

|                                                                              Details                                                                               ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|-----------------------------------------------| | `value` | The string value used to represent the scope. |                               |
| Exceptions  | |---------------------|--------------------------------------------------| | `ArgumentException` | If the provided string is not a valid AuthScope. | |
| **Returns** | The AuthScope enum value corresponding to the provided string.                                                                                        |

### GetValue

```c#
string GetValue(
  this AuthScope authScope
)
```  
Returns the standard string representation of this OAuth 2.0 scope.

<br />

|                                                                     Details                                                                      ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------------|---------------------------| | `authScope` | The AuthScope enum value. |                                             |
| Exceptions  | |---------------------|-----------------------------------------| | `ArgumentException` | If the provided AuthScope is not valid. | |
| **Returns** | The string value used to represent this scope.                                                                                      |