---
title: https://developer.android.com/games/services/cpp/v2/api/group/play-games
url: https://developer.android.com/games/services/cpp/v2/api/group/play-games
source: md.txt
---

# Play Games Services

Native API for Play Games Services.

## Summary

| ### Typedefs ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga1658f46313e5cebcd72479f1e8c45287` | typedef `struct https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga1658f46313e5cebcd72479f1e8c45287` An opaque handle to the Achievements Client. |
| `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gae227514075dc58e0ea306477ee91ded6` | typedef `struct https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gae227514075dc58e0ea306477ee91ded6` An opaque handle to the GamesSignIn Client. |
| `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga2f1a423a29ca48ef4134c788e623ff0f` | typedef `struct https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga2f1a423a29ca48ef4134c788e623ff0f` An opaque handle to the Leaderboards Client. |
| `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gaf679f412e36ebfbb36af030d17279c61` | typedef `struct https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gaf679f412e36ebfbb36af030d17279c61` An opaque handle to the Recall Client. |
| `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gac5f98c3af7334d48b0346bbee83b5553` | typedef `struct https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gac5f98c3af7334d48b0346bbee83b5553` An opaque handle to the Snapshots Client. |

| ### Functions ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga5d8cfd0eccc93f20a7ff3be03b255c60(jobject activity)` | `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga1658f46313e5cebcd72479f1e8c45287 *` Creates a new Achievements Client instance. |
| `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga3ab2b8387edbfe3768119f94fd3ca358(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga1658f46313e5cebcd72479f1e8c45287 *achievements_client)` | `void` Destroys an Achievements Client instance. |
| `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga52107378b624161b0f320335fab9d001(jobject activity)` | `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga7a0f58b5967954ea578f2c9523949067 *` Creates a new GameStats Client instance. |
| `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga7cf1239c0035ff7f90748e29d5331bfa(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga7a0f58b5967954ea578f2c9523949067 *game_stats_client)` | `void` Destroys a GameStats Client instance. |
| `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga15085249c5c4b1c35823176dbea45dae(jobject activity)` | `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gae227514075dc58e0ea306477ee91ded6 *` Creates a new GamesSignIn Client instance. |
| `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga9cba93bc35798c2bb4491a23dc9d3287(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gae227514075dc58e0ea306477ee91ded6 *games_sign_in_client)` | `void` Destroys a GamesSignIn Client instance. |
| `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga14a218057a4bee88d384aa4f559342ee(jobject activity)` | `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga2f1a423a29ca48ef4134c788e623ff0f *` Creates a new Leaderboards Client instance. |
| `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga9e0468b2dc577647903becf99dc43103(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga2f1a423a29ca48ef4134c788e623ff0f *leaderboards_client)` | `void` Destroys a Leaderboards Client instance. |
| `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga95b2518215ca5e163e585198ea9b1ae4(jobject activity)` | `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gaf679f412e36ebfbb36af030d17279c61 *` Creates a new Recall Client instance. |
| `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gaf6a9487b7684d715d789c263bc14ad26(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gaf679f412e36ebfbb36af030d17279c61 *recall_client)` | `void` Destroys a Recall Client instance. |
| `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga70b489f0ceda1e265fb238f2a2600be8(jobject activity)` | `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gac5f98c3af7334d48b0346bbee83b5553 *` Creates a new Snapshots Client instance. |
| `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga61b4877cdfae489eebe20353b75fa4d1(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gac5f98c3af7334d48b0346bbee83b5553 *snapshots_client)` | `void` Destroys a Snapshots Client instance. |
| `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga8de2848a742f4abba86e1053c51acdc7()` | `void` Shuts down the Play Games Services native SDK. |
| `https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gabd7ce01192b396374b8726af3abe6976(JavaVM *vm, jobject context)` | `jint` Initializes the Play Games Services native SDK. |

## Typedefs

### PgsAchievementsClient

```c++
struct PgsAchievementsClient PgsAchievementsClient
```
An opaque handle to the Achievements Client.

### PgsGameStatsClient

```c++
struct PgsGameStatsClient PgsGameStatsClient
```
An opaque handle to the GameStats Client.

### PgsGamesSignInClient

```c++
struct PgsGamesSignInClient PgsGamesSignInClient
```
An opaque handle to the GamesSignIn Client.

### PgsLeaderboardsClient

```c++
struct PgsLeaderboardsClient PgsLeaderboardsClient
```
An opaque handle to the Leaderboards Client.

### PgsRecallClient

```c++
struct PgsRecallClient PgsRecallClient
```
An opaque handle to the Recall Client.

### PgsSnapshotsClient

```c++
struct PgsSnapshotsClient PgsSnapshotsClient
```
An opaque handle to the Snapshots Client.

## Functions

### PgsAchievementsClient_create

```c++
PgsAchievementsClient * PgsAchievementsClient_create(
  jobject activity
)
```
Creates a new Achievements Client instance.

This function creates a client handle for interacting with the achievements API.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `activity` | A JNI reference to a valid Android Activity. | |
| **Returns** | A new PgsAchievementsClient handle, or NULL on failure. This handle must be released with [PgsAchievementsClient_destroy()](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga3ab2b8387edbfe3768119f94fd3ca358). |

### PgsAchievementsClient_destroy

```c++
void PgsAchievementsClient_destroy(
  PgsAchievementsClient *achievements_client
)
```
Destroys an Achievements Client instance.

This function releases all resources associated with the client handle. The handle becomes invalid after this call.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `achievements_client` | The client handle to destroy. | |

### PgsGameStatsClient_create

```c++
PgsGameStatsClient * PgsGameStatsClient_create(
  jobject activity
)
```
Creates a new GameStats Client instance.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `activity` | A JNI reference to a valid Android Activity. | |
| **Returns** | A new PgsGameStatsClient handle, or NULL on failure. This handle must be released with [PgsGameStatsClient_destroy()](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga7cf1239c0035ff7f90748e29d5331bfa). |

### PgsGameStatsClient_destroy

```c++
void PgsGameStatsClient_destroy(
  PgsGameStatsClient *game_stats_client
)
```
Destroys a GameStats Client instance.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `game_stats_client` | The client handle to destroy. | |

### PgsGamesSignInClient_create

```c++
PgsGamesSignInClient * PgsGamesSignInClient_create(
  jobject activity
)
```
Creates a new GamesSignIn Client instance.

This function creates a client handle for interacting with the GamesSignIn API.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `activity` | A JNI reference to a valid Android Activity. | |
| **Returns** | A new PgsGamesSignInClient handle, or NULL on failure. This handle must be released with [PgsGamesSignInClient_destroy()](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga9cba93bc35798c2bb4491a23dc9d3287). |

### PgsGamesSignInClient_destroy

```c++
void PgsGamesSignInClient_destroy(
  PgsGamesSignInClient *games_sign_in_client
)
```
Destroys a GamesSignIn Client instance.

This function releases all resources associated with the client handle. The handle becomes invalid after this call.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `games_sign_in_client` | The client handle to destroy. | |

### PgsLeaderboardsClient_create

```c++
PgsLeaderboardsClient * PgsLeaderboardsClient_create(
  jobject activity
)
```
Creates a new Leaderboards Client instance.

This function creates a client handle for interacting with the Leaderboards API.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `activity` | A JNI reference to a valid Android Activity. | |
| **Returns** | A new PgsLeaderboardsClient handle, or NULL on failure. This handle must be released with [PgsLeaderboardsClient_destroy()](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga9e0468b2dc577647903becf99dc43103). |

### PgsLeaderboardsClient_destroy

```c++
void PgsLeaderboardsClient_destroy(
  PgsLeaderboardsClient *leaderboards_client
)
```
Destroys a Leaderboards Client instance.

This function releases all resources associated with the client handle. The handle becomes invalid after this call.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `leaderboards_client` | The client handle to destroy. | |

### PgsRecallClient_create

```c++
PgsRecallClient * PgsRecallClient_create(
  jobject activity
)
```
Creates a new Recall Client instance.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `activity` | A JNI reference to a valid Android Activity. | |
| **Returns** | A new PgsRecallClient handle, or NULL on failure. This handle must be released with [PgsRecallClient_destroy()](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gaf6a9487b7684d715d789c263bc14ad26). |

### PgsRecallClient_destroy

```c++
void PgsRecallClient_destroy(
  PgsRecallClient *recall_client
)
```
Destroys a Recall Client instance.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `recall_client` | The client handle to destroy. | |

### PgsSnapshotsClient_create

```c++
PgsSnapshotsClient * PgsSnapshotsClient_create(
  jobject activity
)
```
Creates a new Snapshots Client instance.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `activity` | A JNI reference to a valid Android Activity. | |
| **Returns** | A new PgsSnapshotsClient handle, or NULL on failure. This handle must be released with [PgsSnapshotsClient_destroy()](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga61b4877cdfae489eebe20353b75fa4d1). |

### PgsSnapshotsClient_destroy

```c++
void PgsSnapshotsClient_destroy(
  PgsSnapshotsClient *snapshots_client
)
```
Destroys a Snapshots Client instance.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshots_client` | The client handle to destroy. | |

### Pgs_destroy

```c++
void Pgs_destroy()
```
Shuts down the Play Games Services native SDK.

This should be called once when the application is closing to clean up all global references.

### Pgs_initialize

```c++
jint Pgs_initialize(
  JavaVM *vm,
  jobject context
)
```
Initializes the Play Games Services native SDK.

This must be called once at application startup before any other SDK functions.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `vm` | The `JavaVM` pointer obtained. | | `context` | An Android `Activity` object. | |
| **Returns** | `JNI_OK` on success, or `JNI_ERR` on failure. |