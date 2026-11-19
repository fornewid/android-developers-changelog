---
title: https://developer.android.com/games/services/cpp/v2/api/group/players
url: https://developer.android.com/games/services/cpp/v2/api/group/players
source: md.txt
---

> Documentation index: https://developer.android.com/games/services/cpp/v2/api/llms.txt

# Play Games Services Players

Native API for Play Games Services Players.

## Summary

| ### Typedefs ||
|---|---|
| `PgsPlayersClient_GetCurrentPlayerIdCallback)(PgsStatusCode status_code, const char *player_id, void *user_data)` | typedef `void(*` Callback for PgsPlayersClient_getCurrentPlayerId. |

| ### Functions ||
|---|---|
| `PgsPlayersClient_getCurrentPlayerId(PgsPlayersClient *client, PgsPlayersClient_GetCurrentPlayerIdCallback callback, void *user_data)` | `void` Asynchronously retrieves the player ID of the currently signed-in player. |

## Typedefs

### PgsPlayersClient_GetCurrentPlayerIdCallback

```c++
void(* PgsPlayersClient_GetCurrentPlayerIdCallback)(PgsStatusCode status_code, const char *player_id, void *user_data)
```
Callback for PgsPlayersClient_getCurrentPlayerId.

This is invoked after the asynchronous operation to get the player ID completes or fails.


Details Parameters `status_code` Result of the operation. PGS_STATUS_SUCCESS on success. `player_id` The player ID if successful, otherwise NULL. The caller is responsible for managing the memory of this string if needed beyond the callback. `user_data` Pointer to the user-provided data passed in the original call.

## Functions

### PgsPlayersClient_getCurrentPlayerId

```c++
void PgsPlayersClient_getCurrentPlayerId(
  PgsPlayersClient *client,
  PgsPlayersClient_GetCurrentPlayerIdCallback callback,
  void *user_data
)
```
Asynchronously retrieves the player ID of the currently signed-in player.

The result is provided asynchronously via the callback.


Details Parameters `client` The Players Client instance. `callback` Function to be called with the result. `user_data` Arbitrary data pointer to be passed back to the callback.