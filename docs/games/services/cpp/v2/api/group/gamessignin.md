---
title: https://developer.android.com/games/services/cpp/v2/api/group/gamessignin
url: https://developer.android.com/games/services/cpp/v2/api/group/gamessignin
source: md.txt
---

# Play Games Services Sign-In

Native API for Play Games Services Sign-In.

## Summary

| ### Typedefs ||
|---|---|
| [PgsGamesSignInClient_IsAuthenticatedCallback](https://developer.android.com/games/services/cpp/v2/api/group/gamessignin#group__gamessignin_1ga9583ea136216ddc173c54afb53ba710a)`)(PgsStatusCode status_code, bool is_authenticated, void *user_data)` | typedef `void(*` Callback for PgsGamesSignInClient_isAuthenticated. |
| [PgsGamesSignInClient_RequestServerSideAccessCallback](https://developer.android.com/games/services/cpp/v2/api/group/gamessignin#group__gamessignin_1ga548656c14918159576f0aa621e90d096)`)(PgsStatusCode status_code, const char *auth_code, void *user_data)` | typedef `void(*` Callback for PgsGamesSignInClient_requestServerSideAccess. |
| [PgsGamesSignInClient_RequestServerSideAccessWithScopesCallback](https://developer.android.com/games/services/cpp/v2/api/group/gamessignin#group__gamessignin_1ga52e652f05f8a86494464f68f9e4b3c9d)`)(PgsStatusCode status_code, const char *auth_code, PgsAuthScope *granted_scopes, int32_t granted_scopes_count, void *user_data)` | typedef `void(*` Callback for PgsGamesSignInClient_requestServerSideAccessWithScopes. |
| [PgsGamesSignInClient_SignInCallback](https://developer.android.com/games/services/cpp/v2/api/group/gamessignin#group__gamessignin_1ga94817f87d51beb34a22d49c8f916ce7a)`)(PgsStatusCode status_code, bool is_authenticated, void *user_data)` | typedef `void(*` Callback for PgsGamesSignInClient_signIn. |

| ### Functions ||
|---|---|
| [PgsGamesSignInClient_isAuthenticated](https://developer.android.com/games/services/cpp/v2/api/group/gamessignin#group__gamessignin_1ga437c28c879ed29902231606444d1b192)`(`[PgsGamesSignInClient](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gae227514075dc58e0ea306477ee91ded6)` *client, `[PgsGamesSignInClient_IsAuthenticatedCallback](https://developer.android.com/games/services/cpp/v2/api/group/gamessignin#group__gamessignin_1ga9583ea136216ddc173c54afb53ba710a)` callback, void *user_data)` | `void` Checks if the player is currently authenticated with Play Games Services. |
| [PgsGamesSignInClient_requestServerSideAccess](https://developer.android.com/games/services/cpp/v2/api/group/gamessignin#group__gamessignin_1gab74587336628109f8c7af2f7a294a05f)`(`[PgsGamesSignInClient](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gae227514075dc58e0ea306477ee91ded6)` *client, const char *server_client_id, bool force_refresh_token, `[PgsGamesSignInClient_RequestServerSideAccessCallback](https://developer.android.com/games/services/cpp/v2/api/group/gamessignin#group__gamessignin_1ga548656c14918159576f0aa621e90d096)` callback, void *user_data)` | `void` Retrieves the OAuth 2.0 server-side access code for the client ID specified in the Google Play Console. |
| [PgsGamesSignInClient_requestServerSideAccessWithScopes](https://developer.android.com/games/services/cpp/v2/api/group/gamessignin#group__gamessignin_1ga94e91f01714b2deb40d2eafcd41214ac)`(`[PgsGamesSignInClient](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gae227514075dc58e0ea306477ee91ded6)` *client, const char *server_client_id, bool force_refresh_token, const `[PgsAuthScope](https://developer.android.com/games/services/cpp/v2/api/group/auth#group__auth_1gadbee6c0835f25f7fd555e47e7873d197)` *scopes, int32_t scopes_count, `[PgsGamesSignInClient_RequestServerSideAccessWithScopesCallback](https://developer.android.com/games/services/cpp/v2/api/group/gamessignin#group__gamessignin_1ga52e652f05f8a86494464f68f9e4b3c9d)` callback, void *user_data)` | `void` Retrieves the OAuth 2.0 server-side access code for the client ID specified in the Google Play Console, with additional OAuth scopes. |
| [PgsGamesSignInClient_signIn](https://developer.android.com/games/services/cpp/v2/api/group/gamessignin#group__gamessignin_1ga34becbb52b7d12ddf83729ced54134d7)`(`[PgsGamesSignInClient](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gae227514075dc58e0ea306477ee91ded6)` *client, `[PgsGamesSignInClient_SignInCallback](https://developer.android.com/games/services/cpp/v2/api/group/gamessignin#group__gamessignin_1ga94817f87d51beb34a22d49c8f916ce7a)` callback, void *user_data)` | `void` Manually requests that your game sign in with Play Games Services. |

## Typedefs

### PgsGamesSignInClient_IsAuthenticatedCallback

```c++
void(* PgsGamesSignInClient_IsAuthenticatedCallback)(PgsStatusCode status_code, bool is_authenticated, void *user_data)
```  
Callback for PgsGamesSignInClient_isAuthenticated.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. PGS_STATUS_SUCCESS on success. | | `is_authenticated` | True if the player is currently authenticated, false otherwise. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsGamesSignInClient_RequestServerSideAccessCallback

```c++
void(* PgsGamesSignInClient_RequestServerSideAccessCallback)(PgsStatusCode status_code, const char *auth_code, void *user_data)
```  
Callback for PgsGamesSignInClient_requestServerSideAccess.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. PGS_STATUS_SUCCESS on success. | | `auth_code` | The server auth code if successful, otherwise NULL. The caller is responsible for managing the memory of this string if needed beyond the callback. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsGamesSignInClient_RequestServerSideAccessWithScopesCallback

```c++
void(* PgsGamesSignInClient_RequestServerSideAccessWithScopesCallback)(PgsStatusCode status_code, const char *auth_code, PgsAuthScope *granted_scopes, int32_t granted_scopes_count, void *user_data)
```  
Callback for PgsGamesSignInClient_requestServerSideAccessWithScopes.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. PGS_STATUS_SUCCESS on success. | | `auth_code` | The server auth code if successful, otherwise NULL. The caller is responsible for managing the memory of this string if needed beyond the callback. | | `granted_scopes` | The granted scopes if successful, otherwise NULL. The caller is responsible for managing the memory of this array if needed beyond the callback. | | `granted_scopes_count` | The number of scopes in the granted_scopes array. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsGamesSignInClient_SignInCallback

```c++
void(* PgsGamesSignInClient_SignInCallback)(PgsStatusCode status_code, bool is_authenticated, void *user_data)
```  
Callback for PgsGamesSignInClient_signIn.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the sign-in operation. PGS_STATUS_SUCCESS on success. | | `is_authenticated` | True if the player is now authenticated, false otherwise. This is the result from AuthenticationResult.isAuthenticated(). | | `user_data` | Pointer to the user-provided data passed in the original call. | |

## Functions

### PgsGamesSignInClient_isAuthenticated

```c++
void PgsGamesSignInClient_isAuthenticated(
  PgsGamesSignInClient *client,
  PgsGamesSignInClient_IsAuthenticatedCallback callback,
  void *user_data
)
```  
Checks if the player is currently authenticated with Play Games Services.

The result is provided asynchronously via the callback.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `client` | The GamesSignInClient handle. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsGamesSignInClient_requestServerSideAccess

```c++
void PgsGamesSignInClient_requestServerSideAccess(
  PgsGamesSignInClient *client,
  const char *server_client_id,
  bool force_refresh_token,
  PgsGamesSignInClient_RequestServerSideAccessCallback callback,
  void *user_data
)
```  
Retrieves the OAuth 2.0 server-side access code for the client ID specified in the Google Play Console.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `client` | The GamesSignInClient handle. | | `server_client_id` | The server client ID. | | `force_refresh_token` | Whether to force a refresh of the access token. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsGamesSignInClient_requestServerSideAccessWithScopes

```c++
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

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `client` | The GamesSignInClient handle. | | `server_client_id` | The server client ID. | | `force_refresh_token` | Whether to force a refresh of the access token. | | `scopes` | Array of PgsAuthScope values to request. | | `scopes_count` | Number of scopes in scopes array. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsGamesSignInClient_signIn

```c++
void PgsGamesSignInClient_signIn(
  PgsGamesSignInClient *client,
  PgsGamesSignInClient_SignInCallback callback,
  void *user_data
)
```  
Manually requests that your game sign in with Play Games Services.

Note that a sign-in attempt will be made automatically when your game starts. Games will only need to manually request to sign in if the automatic sign-in attempt failed.

The result, including whether the user is authenticated, is provided asynchronously via the callback.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `client` | The GamesSignInClient handle. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |