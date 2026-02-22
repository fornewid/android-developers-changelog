---
title: https://developer.android.com/games/services/cpp/v2/api/group/recall
url: https://developer.android.com/games/services/cpp/v2/api/group/recall
source: md.txt
---

# Play Games Services Recall

Native API for Play Games Services Recall.

## Summary

| ### Typedefs ||
|---|---|
| [PgsRecallClient_RequestRecallAccessCallback](https://developer.android.com/games/services/cpp/v2/api/group/recall#group__recall_1ga9becd35dbe994d6ed179f5a64d004b7f)`)(PgsStatusCode status_code, const char *session_id, void *user_data)` | typedef `void(*` Callback for the requestRecallAccess operation. |

| ### Functions ||
|---|---|
| [PgsRecallClient_requestRecallAccess](https://developer.android.com/games/services/cpp/v2/api/group/recall#group__recall_1gaf91c2204ecbf285aa72bffc25b983c6d)`(`[PgsRecallClient](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gaf679f412e36ebfbb36af030d17279c61)` *client, `[PgsRecallClient_RequestRecallAccessCallback](https://developer.android.com/games/services/cpp/v2/api/group/recall#group__recall_1ga9becd35dbe994d6ed179f5a64d004b7f)` callback, void *user_data)` | `void` Requests a recall access token. |

## Typedefs

### PgsRecallClient_RequestRecallAccessCallback

```c++
void(* PgsRecallClient_RequestRecallAccessCallback)(PgsStatusCode status_code, const char *session_id, void *user_data)
```  
Callback for the requestRecallAccess operation.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | The result of the operation. PGS_STATUS_SUCCESS on success. | | `session_id` | The recall session ID, or NULL if an error occurred. The caller is responsible for freeing this string using free(). | | `user_data` | User-provided data passed to the original function call. | |

## Functions

### PgsRecallClient_requestRecallAccess

```c++
void PgsRecallClient_requestRecallAccess(
  PgsRecallClient *client,
  PgsRecallClient_RequestRecallAccessCallback callback,
  void *user_data
)
```  
Requests a recall access token.

This function is asynchronous. The result will be provided in the PgsRecallClient_RequestRecallAccessCallback.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `client` | The Recall Client instance. | | `callback` | The callback to invoke with the result. | | `user_data` | Arbitrary data to be passed to the callback. | |