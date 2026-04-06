---
title: Play Games Services Recall  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/cpp/v2/api/group/recall
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# Play Games Services Recall

Native API for Play Games Services Recall.

## Summary

| Typedefs | |
| --- | --- |
| `PgsRecallClient_RequestRecallAccessCallback)(PgsStatusCode status_code, const char *session_id, void *user_data)` | typedef `void(*`  Callback for the requestRecallAccess operation. |

| Functions | |
| --- | --- |
| `PgsRecallClient_requestRecallAccess(PgsRecallClient *client, PgsRecallClient_RequestRecallAccessCallback callback, void *user_data)` | `void`  Requests a recall access token. |

## Typedefs

### PgsRecallClient\_RequestRecallAccessCallback

```
void(* PgsRecallClient_RequestRecallAccessCallback)(PgsStatusCode status_code, const char *session_id, void *user_data)
```

Callback for the requestRecallAccess operation.

Details | || Parameters | |  |  | | --- | --- | | `status_code` | The result of the operation. PGS\_STATUS\_SUCCESS on success. | | `session_id` | The recall session ID, or NULL if an error occurred. The caller is responsible for freeing this string using free(). | | `user_data` | User-provided data passed to the original function call. | |

## Functions

### PgsRecallClient\_requestRecallAccess

```
void PgsRecallClient_requestRecallAccess(
  PgsRecallClient *client,
  PgsRecallClient_RequestRecallAccessCallback callback,
  void *user_data
)
```

Requests a recall access token.

This function is asynchronous. The result will be provided in the PgsRecallClient\_RequestRecallAccessCallback.

Details | || Parameters | |  |  | | --- | --- | | `client` | The Recall Client instance. | | `callback` | The callback to invoke with the result. | | `user_data` | Arbitrary data to be passed to the callback. | |