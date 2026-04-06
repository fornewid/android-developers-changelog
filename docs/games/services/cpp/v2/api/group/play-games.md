---
title: Play Games Services  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/cpp/v2/api/group/play-games
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# Play Games Services

Native API for Play Games Services.

## Summary

| Typedefs | |
| --- | --- |
| `PgsAchievementsClient` | typedef `struct PgsAchievementsClient`  An opaque handle to the Achievements Client. |
| `PgsGamesSignInClient` | typedef `struct PgsGamesSignInClient`  An opaque handle to the GamesSignIn Client. |
| `PgsRecallClient` | typedef `struct PgsRecallClient`  An opaque handle to the Recall Client. |

| Functions | |
| --- | --- |
| `PgsAchievementsClient_create(jobject activity)` | `PgsAchievementsClient *`  Creates a new Achievements Client instance. |
| `PgsAchievementsClient_destroy(PgsAchievementsClient *achievements_client)` | `void`  Destroys an Achievements Client instance. |
| `PgsGamesSignInClient_create(jobject activity)` | `PgsGamesSignInClient *`  Creates a new GamesSignIn Client instance. |
| `PgsGamesSignInClient_destroy(PgsGamesSignInClient *games_sign_in_client)` | `void`  Destroys a GamesSignIn Client instance. |
| `PgsRecallClient_create(jobject activity)` | `PgsRecallClient *`  Creates a new Recall Client instance. |
| `PgsRecallClient_destroy(PgsRecallClient *recall_client)` | `void`  Destroys a Recall Client instance. |
| `Pgs_destroy()` | `void`  Shuts down the Play Games Services native SDK. |
| `Pgs_initialize(JavaVM *vm, jobject context)` | `jint`  Initializes the Play Games Services native SDK. |

## Typedefs

### PgsAchievementsClient

```
struct PgsAchievementsClient PgsAchievementsClient
```

An opaque handle to the Achievements Client.

### PgsGamesSignInClient

```
struct PgsGamesSignInClient PgsGamesSignInClient
```

An opaque handle to the GamesSignIn Client.

### PgsRecallClient

```
struct PgsRecallClient PgsRecallClient
```

An opaque handle to the Recall Client.

## Functions

### PgsAchievementsClient\_create

```
PgsAchievementsClient * PgsAchievementsClient_create(
  jobject activity
)
```

Creates a new Achievements Client instance.

This function creates a client handle for interacting with the achievements API.

Details | || Parameters | |  |  | | --- | --- | | `activity` | A JNI reference to a valid Android Activity. | |
| **Returns** | A new PgsAchievementsClient handle, or NULL on failure. This handle must be released with [PgsAchievementsClient\_destroy()](/games/services/cpp/v2/api/group/play-games#group__play__games_1ga3ab2b8387edbfe3768119f94fd3ca358). |

### PgsAchievementsClient\_destroy

```
void PgsAchievementsClient_destroy(
  PgsAchievementsClient *achievements_client
)
```

Destroys an Achievements Client instance.

This function releases all resources associated with the client handle. The handle becomes invalid after this call.

Details | || Parameters | |  |  | | --- | --- | | `achievements_client` | The client handle to destroy. | |

### PgsGamesSignInClient\_create

```
PgsGamesSignInClient * PgsGamesSignInClient_create(
  jobject activity
)
```

Creates a new GamesSignIn Client instance.

This function creates a client handle for interacting with the GamesSignIn API.

Details | || Parameters | |  |  | | --- | --- | | `activity` | A JNI reference to a valid Android Activity. | |
| **Returns** | A new PgsGamesSignInClient handle, or NULL on failure. This handle must be released with [PgsGamesSignInClient\_destroy()](/games/services/cpp/v2/api/group/play-games#group__play__games_1ga9cba93bc35798c2bb4491a23dc9d3287). |

### PgsGamesSignInClient\_destroy

```
void PgsGamesSignInClient_destroy(
  PgsGamesSignInClient *games_sign_in_client
)
```

Destroys a GamesSignIn Client instance.

This function releases all resources associated with the client handle. The handle becomes invalid after this call.

Details | || Parameters | |  |  | | --- | --- | | `games_sign_in_client` | The client handle to destroy. | |

### PgsRecallClient\_create

```
PgsRecallClient * PgsRecallClient_create(
  jobject activity
)
```

Creates a new Recall Client instance.

Details | || Parameters | |  |  | | --- | --- | | `activity` | A JNI reference to a valid Android Activity. | |
| **Returns** | A new PgsRecallClient handle, or NULL on failure. This handle must be released with [PgsRecallClient\_destroy()](/games/services/cpp/v2/api/group/play-games#group__play__games_1gaf6a9487b7684d715d789c263bc14ad26). |

### PgsRecallClient\_destroy

```
void PgsRecallClient_destroy(
  PgsRecallClient *recall_client
)
```

Destroys a Recall Client instance.

Details | || Parameters | |  |  | | --- | --- | | `recall_client` | The client handle to destroy. | |

### Pgs\_destroy

```
void Pgs_destroy()
```

Shuts down the Play Games Services native SDK.

This should be called once when the application is closing to clean up all global references.

### Pgs\_initialize

```
jint Pgs_initialize(
  JavaVM *vm,
  jobject context
)
```

Initializes the Play Games Services native SDK.

This must be called once at application startup before any other SDK functions.

Details | || Parameters | |  |  | | --- | --- | | `vm` | The JavaVM pointer obtained. | | `context` | An Android Activity object. | |
| **Returns** | JNI\_OK on success, or JNI\_ERR on failure. |