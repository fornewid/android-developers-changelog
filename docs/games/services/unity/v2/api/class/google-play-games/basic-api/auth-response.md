---
title: GooglePlayGames.BasicApi.AuthResponse Class Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/class/google-play-games/basic-api/auth-response
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# GooglePlayGames.BasicApi.AuthResponse

Represents the response received from Play Games Services when requesting a server-side OAuth 2.0 authorization code for the signed-in player.

## Summary

| Constructors and Destructors | |
| --- | --- |
| `AuthResponse(string authCode, List< AuthScope > grantedScopes)`   Constructs an `AuthResponse` with the provided granted scopes and authentication code. | |

| Public functions | |
| --- | --- |
| `Equals(object obj)` | `override bool` |
| `GetAuthCode()` | `string`  Gets the OAuth 2.0 authorization code. |
| `GetGrantedScopes()` | `List< AuthScope >`  Gets the list of `AuthScope` permissions that the user has granted. |
| `GetHashCode()` | `override int` |
| `ToString()` | `override string` |

## Public functions

### AuthResponse

```
 AuthResponse(
  string authCode,
  List< AuthScope > grantedScopes
)
```

Constructs an `AuthResponse` with the provided granted scopes and authentication code.

Details | || Parameters | |  |  | | --- | --- | | `authCode` | The authentication code. | | `grantedScopes` | A list of `AuthScope` objects representing the granted scopes. | |
| Exceptions | |  |  | | --- | --- | | `ArgumentNullException` | If `grantedScopes` is null. | |

### Equals

```
override bool Equals(
  object obj
)
```

### GetAuthCode

```
string GetAuthCode()
```

Gets the OAuth 2.0 authorization code.

This code is a short-lived credential that should be sent securely to your server to be exchanged for an access token and conditionally a refresh token.

Details | || **Returns** | A string containing the OAuth 2.0 authorization code. |

### GetGrantedScopes

```
List< AuthScope > GetGrantedScopes()
```

Gets the list of `AuthScope` permissions that the user has granted.

A list of the `AuthScope` permissions the user explicitly granted consent for (or previously approved). The list will be empty if the user declines consent and none of the requested `AuthScope` were previously granted.

Details | || **Returns** | A `List` of `AuthScope` objects, representing the granted permissions. |

### GetHashCode

```
override int GetHashCode()
```

### ToString

```
override string ToString()
```