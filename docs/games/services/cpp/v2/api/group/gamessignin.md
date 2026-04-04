---
title: Play Games Services Sign-In  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/cpp/v2/api/group/gamessignin
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.




# Play Games Services Sign-In

Native API for Play Games Services Sign-In.

## Summary

| Typedefs | |
| --- | --- |
| `PgsGamesSignInClient_IsAuthenticatedCallback)(PgsStatusCode status_code, bool is_authenticated, void *user_data)` | typedef `void(*`  Callback for PgsGamesSignInClient\_isAuthenticated. |
| `PgsGamesSignInClient_RequestServerSideAccessCallback)(PgsStatusCode status_code, const char *auth_code, void *user_data)` | typedef `void(*`  Callback for PgsGamesSignInClient\_requestServerSideAccess. |
| `PgsGamesSignInClient_RequestServerSideAccessWithScopesCallback)(PgsStatusCode status_code, const char *auth_code, PgsAuthScope *granted_scopes, int32_t granted_scopes_count, void *user_data)` | typedef `void(*`  Callback for PgsGamesSignInClient\_requestServerSideAccessWithScopes. |
| `PgsGamesSignInClient_SignInCallback)(PgsStatusCode status_code, bool is_authenticated, void *user_data)` | typedef `void(*`  Callback for PgsGamesSignInClient\_signIn. |

| Functions | |
| --- | --- |
| `PgsGamesSignInClient_isAuthenticated(PgsGamesSignInClient *client, PgsGamesSignInClient_IsAuthenticatedCallback callback, void *user_data)` | `void`  Checks if the player is currently authenticated with Play Games Services. |
| `PgsGamesSignInClient_requestServerSideAccess(PgsGamesSignInClient *client, const char *server_client_id, bool force_refresh_token, PgsGamesSignInClient_RequestServerSideAccessCallback callback, void *user_data)` | `void`  Retrieves the OAuth 2.0 server-side access code for the client ID specified in the Google Play Console. |
| `PgsGamesSignInClient_requestServerSideAccessWithScopes(PgsGamesSignInClient *client, const char *server_client_id, bool force_refresh_token, const PgsAuthScope *scopes, int32_t scopes_count, PgsGamesSignInClient_RequestServerSideAccessWithScopesCallback callback, void *user_data)` | `void`  Retrieves the OAuth 2.0 server-side access code for the client ID specified in the Google Play Console, with additional OAuth scopes. |
| `PgsGamesSignInClient_signIn(PgsGamesSignInClient *client, PgsGamesSignInClient_SignInCallback callback, void *user_data)` | `void`  Manually requests that your game sign in with Play Games Services. |

## Typedefs

### PgsGamesSignInClient\_IsAuthenticatedCallback

```
void(* PgsGamesSignInClient_IsAuthenticatedCallback)(PgsStatusCode status_code, bool is_authenticated, void *user_data)
```

Callback for PgsGamesSignInClient\_isAuthenticated.

Details | || Parameters | |  |  | | --- | --- | | `status_code` | Result of the operation. PGS\_STATUS\_SUCCESS on success. | | `is_authenticated` | True if the player is currently authenticated, false otherwise. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsGamesSignInClient\_RequestServerSideAccessCallback

```
void(* PgsGamesSignInClient_RequestServerSideAccessCallback)(PgsStatusCode status_code, const char *auth_code, void *user_data)
```

Callback for PgsGamesSignInClient\_requestServerSideAccess.

Details | || Parameters | |  |  | | --- | --- | | `status_code` | Result of the operation. PGS\_STATUS\_SUCCESS on success. | | `auth_code` | The server auth code if successful, otherwise NULL. The caller is responsible for managing the memory of this string if needed beyond the callback. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsGamesSignInClient\_RequestServerSideAccessWithScopesCallback

```
void(* PgsGamesSignInClient_RequestServerSideAccessWithScopesCallback)(PgsStatusCode status_code, const char *auth_code, PgsAuthScope *granted_scopes, int32_t granted_scopes_count, void *user_data)
```

Callback for PgsGamesSignInClient\_requestServerSideAccessWithScopes.

Details | || Parameters | |  |  | | --- | --- | | `status_code` | Result of the operation. PGS\_STATUS\_SUCCESS on success. | | `auth_code` | The server auth code if successful, otherwise NULL. The caller is responsible for managing the memory of this string if needed beyond the callback. | | `granted_scopes` | The granted scopes if successful, otherwise NULL. The caller is responsible for managing the memory of this array if needed beyond the callback. | | `granted_scopes_count` | The number of scopes in the granted\_scopes array. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsGamesSignInClient\_SignInCallback

```
void(* PgsGamesSignInClient_SignInCallback)(PgsStatusCode status_code, bool is_authenticated, void *user_data)
```

Callback for PgsGamesSignInClient\_signIn.

Details | || Parameters | |  |  | | --- | --- | | `status_code` | Result of the sign-in operation. PGS\_STATUS\_SUCCESS on success. | | `is_authenticated` | True if the player is now authenticated, false otherwise. This is the result from AuthenticationResult.isAuthenticated(). | | `user_data` | Pointer to the user-provided data passed in the original call. | |

## Functions

### PgsGamesSignInClient\_isAuthenticated

```
void PgsGamesSignInClient_isAuthenticated(
  PgsGamesSignInClient *client,
  PgsGamesSignInClient_IsAuthenticatedCallback callback,
  void *user_data
)
```

Checks if the player is currently authenticated with Play Games Services.

The result is provided asynchronously via the callback.

Details | || Parameters | |  |  | | --- | --- | | `client` | The GamesSignInClient handle. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsGamesSignInClient\_requestServerSideAccess

```
void PgsGamesSignInClient_requestServerSideAccess(
  PgsGamesSignInClient *client,
  const char *server_client_id,
  bool force_refresh_token,
  PgsGamesSignInClient_RequestServerSideAccessCallback callback,
  void *user_data
)
```

Retrieves the OAuth 2.0 server-side access code for the client ID specified in the Google Play Console.

Details | || Parameters | |  |  | | --- | --- | | `client` | The GamesSignInClient handle. | | `server_client_id` | The server client ID. | | `force_refresh_token` | Whether to force a refresh of the access token. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsGamesSignInClient\_requestServerSideAccessWithScopes

```
void PgsGamesSignInClient_requestServerSideAccessWithScopes(
  PgsGamesSignInClient *client,
  const char *server_client_id,
  bool force_refresh_token,
  const PgsAuthScope *scopes,
  int32_t scopes_count,
  PgsGamesSignInClient_RequestServerSideAccessWithScopesCallback callback,
  void *user_data
)
```

Retrieves the OAuth 2.0 server-side access code for the client ID specified in the Google Play Console, with additional OAuth scopes.

Details | || Parameters | |  |  | | --- | --- | | `client` | The GamesSignInClient handle. | | `server_client_id` | The server client ID. | | `force_refresh_token` | Whether to force a refresh of the access token. | | `scopes` | Array of PgsAuthScope values to request. | | `scopes_count` | Number of scopes in scopes array. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsGamesSignInClient\_signIn

```
void PgsGamesSignInClient_signIn(
  PgsGamesSignInClient *client,
  PgsGamesSignInClient_SignInCallback callback,
  void *user_data
)
```

Manually requests that your game sign in with Play Games Services.

Note that a sign-in attempt will be made automatically when your game starts. Games will only need to manually request to sign in if the automatic sign-in attempt failed.

The result, including whether the user is authenticated, is provided asynchronously via the callback.

Details | || Parameters | |  |  | | --- | --- | | `client` | The GamesSignInClient handle. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |