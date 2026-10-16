---
title: https://developer.android.com/games/services/cpp/v2/api/group/status
url: https://developer.android.com/games/services/cpp/v2/api/group/status
source: md.txt
---

# Play Games Services Status

Status codes for Play Games Services native SDK.

## Summary

| ### Enumerations ||
|---|---|
| [PgsStatusCode](https://developer.android.com/games/services/cpp/v2/api/group/status#group__status_1gae0ce80601ab657304037a67d7d41be7d)`{` ` `[PGS_STATUS_SUCCESS](https://developer.android.com/games/services/cpp/v2/api/group/status#group__status_1ggae0ce80601ab657304037a67d7d41be7daebd1119ccf7e110b054cd5c02cc47446)` = 0,` ` `[PGS_STATUS_NOT_AUTHENTICATED](https://developer.android.com/games/services/cpp/v2/api/group/status#group__status_1ggae0ce80601ab657304037a67d7d41be7dae83e054d56c917d9edc644fd53c36825)` = 1,` ` `[PGS_STATUS_NETWORK_ERROR](https://developer.android.com/games/services/cpp/v2/api/group/status#group__status_1ggae0ce80601ab657304037a67d7d41be7da14c94969a9cd675e5403fbb733bb5b0a)` = 2,` ` `[PGS_STATUS_CANCELED](https://developer.android.com/games/services/cpp/v2/api/group/status#group__status_1ggae0ce80601ab657304037a67d7d41be7da646c1e1e2de323db65ce7d47d5d56efb)` = 3,` ` `[PGS_STATUS_TIMEOUT](https://developer.android.com/games/services/cpp/v2/api/group/status#group__status_1ggae0ce80601ab657304037a67d7d41be7dac908d1d5f757808854a86e2af4408ec3)` = 4,` ` `[PGS_STATUS_INVALID_ARGUMENT](https://developer.android.com/games/services/cpp/v2/api/group/status#group__status_1ggae0ce80601ab657304037a67d7d41be7da0fa7bfb9f08a8ed093928de350feef43)` = 5,` ` `[PGS_STATUS_INTERNAL_ERROR](https://developer.android.com/games/services/cpp/v2/api/group/status#group__status_1ggae0ce80601ab657304037a67d7d41be7da2eb0bd15fe86a88da6516e44a2423a45)` = 6` `}` | enum Represents status codes for asynchronous operations across all PGS clients. |

## Enumerations

### PgsStatusCode

```c++
 PgsStatusCode
```  
Represents status codes for asynchronous operations across all PGS clients.

| Properties ||
|---|---|
| `PGS_STATUS_CANCELED` | The operation was canceled by the user (e.g., backing out of a UI). |
| `PGS_STATUS_INTERNAL_ERROR` | An unexpected internal error occurred within the SDK or service. |
| `PGS_STATUS_INVALID_ARGUMENT` | An invalid argument was provided to the function (e.g., a null pointer). |
| `PGS_STATUS_NETWORK_ERROR` | A network error occurred (e.g., no internet connection). |
| `PGS_STATUS_NOT_AUTHENTICATED` | The user is not signed in and needs to authenticate. |
| `PGS_STATUS_SUCCESS` | The operation was successful. |
| `PGS_STATUS_TIMEOUT` | The request to the server timed out. |