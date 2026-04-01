---
title: GooglePlayGames.BasicApi.AuthScopeExtensions Class Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/auth-scope-extensions
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# GooglePlayGames.BasicApi.AuthScopeExtensions

Extensions for the AuthScope enum.

## Summary

These extensions are used to converting between the AuthScope enum and its string representation.

| Public static functions | |
| --- | --- |
| `FromValue(string value)` | `AuthScope`  Returns the AuthScope enum value corresponding to the provided string. |
| `GetValue(this AuthScope authScope)` | `string`  Returns the standard string representation of this OAuth 2.0 scope. |

## Public static functions

### FromValue

```
AuthScope FromValue(
  string value
)
```

Returns the AuthScope enum value corresponding to the provided string.

Details | || Parameters | |  |  | | --- | --- | | `value` | The string value used to represent the scope. | |
| Exceptions | |  |  | | --- | --- | | `ArgumentException` | If the provided string is not a valid AuthScope. | |
| **Returns** | The AuthScope enum value corresponding to the provided string. |

### GetValue

```
string GetValue(
  this AuthScope authScope
)
```

Returns the standard string representation of this OAuth 2.0 scope.

Details | || Parameters | |  |  | | --- | --- | | `authScope` | The AuthScope enum value. | |
| Exceptions | |  |  | | --- | --- | | `ArgumentException` | If the provided AuthScope is not valid. | |
| **Returns** | The string value used to represent this scope. |