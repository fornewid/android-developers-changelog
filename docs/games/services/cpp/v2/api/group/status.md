---
title: Play Games Services Status  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/cpp/v2/api/group/status
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.




# Play Games Services Status

Status codes for Play Games Services native SDK.

## Summary

| Enumerations | |
| --- | --- |
| `PgsStatusCode{   PGS_STATUS_SUCCESS = 0,   PGS_STATUS_NOT_AUTHENTICATED = 1,   PGS_STATUS_NETWORK_ERROR = 2,   PGS_STATUS_CANCELED = 3,   PGS_STATUS_TIMEOUT = 4,   PGS_STATUS_INVALID_ARGUMENT = 5,   PGS_STATUS_INTERNAL_ERROR = 6 }` | enum Represents status codes for asynchronous operations across all PGS clients. |

## Enumerations

### PgsStatusCode

```
 PgsStatusCode
```

Represents status codes for asynchronous operations across all PGS clients.

| Properties | |
| --- | --- |
| `PGS_STATUS_CANCELED` | The operation was canceled by the user (e.g., backing out of a UI). |
| `PGS_STATUS_INTERNAL_ERROR` | An unexpected internal error occurred within the SDK or service. |
| `PGS_STATUS_INVALID_ARGUMENT` | An invalid argument was provided to the function (e.g., a null pointer). |
| `PGS_STATUS_NETWORK_ERROR` | A network error occurred (e.g., no internet connection). |
| `PGS_STATUS_NOT_AUTHENTICATED` | The user is not signed in and needs to authenticate. |
| `PGS_STATUS_SUCCESS` | The operation was successful. |
| `PGS_STATUS_TIMEOUT` | The request to the server timed out. |