---
title: https://developer.android.com/games/services/cpp/v2/api/group/leaderboards
url: https://developer.android.com/games/services/cpp/v2/api/group/leaderboards
source: md.txt
---

# Play Games Services Leaderboards

Native API for Play Games Services Leaderboards.

## Summary

| ### Enumerations ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1ga5bd4c49e881aeef339962a2e43de8ef0{ https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gga5bd4c49e881aeef339962a2e43de8ef0a614e01f7fdb8a0600092bf5bb492783c = 0, https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gga5bd4c49e881aeef339962a2e43de8ef0ac2e80f775d4303d7c2452b5adb064cf6 = 3 }` | enumRepresents the collection type for a leaderboard. |
| `https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gac19c727982519552366071770c1fc716{ https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1ggac19c727982519552366071770c1fc716a086a9ce2f60c01f764dd39b89e14fb2a = 0, https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1ggac19c727982519552366071770c1fc716a9f299bc495a37daeacdc85f1c2f67bb8 = 1, https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1ggac19c727982519552366071770c1fc716a79497671578f90bf352305385f1384af = 2 }` | enumRepresents the time span for a leaderboard. |

| ### Typedefs ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gac169a92c1afc06567d54621cbebe3bea` | typedef `struct https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gac169a92c1afc06567d54621cbebe3bea` An opaque handle to a leaderboard score buffer. |
| `https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1ga3452aaf991dcd1bd1151a6c7fe5bf61d)(PgsStatusCode status_code, PgsLeaderboardScore *score, void *user_data)` | typedef `void(*` Callback for PgsLeaderboardsClient_loadCurrentPlayerLeaderboardScore. |
| `https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1ga53b40b220af7d70ac4d6851fd0dcee27)(PgsStatusCode status_code, const PgsLeaderboard *leaderboards, size_t leaderboard_count, void *user_data)` | typedef `void(*` Callback for PgsLeaderboardsClient_loadLeaderboardMetadata. |
| `https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gaa8ffc35d9f9778b4adb7c158dbc062c8)(PgsStatusCode status_code, const PgsLeaderboard *leaderboard, void *user_data)` | typedef `void(*` Callback for PgsLeaderboardsClient_loadLeaderboardMetadataWithId. |
| `https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1ga0d8dd14d539e16a07a591c9e1e0286b3)(PgsStatusCode status_code, PgsLeaderboardScoreBuffer *leaderboard_score_buffer, PgsLeaderboardScore *scores, size_t scores_count, void *user_data)` | typedef `void(*` Callback for PgsLeaderboardsClient_loadMoreScores. |
| `https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gaaf561834a65bde5d19421c0b31e8661c)(PgsStatusCode status_code, PgsLeaderboardScoreBuffer *leaderboard_score_buffer, PgsLeaderboardScore *scores, size_t scores_count, void *user_data)` | typedef `void(*` Callback for PgsLeaderboardsClient_loadPlayerCenteredScores. |
| `https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gaeb8514e75432684c1e1d8a501e8efa09)(PgsStatusCode status_code, PgsLeaderboardScoreBuffer *leaderboard_score_buffer, PgsLeaderboardScore *scores, size_t scores_count, void *user_data)` | typedef `void(*` Callback for PgsLeaderboardsClient_loadTopScores. |
| `https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gaaa7976dcb801bd3fc02683897a5161a7)(PgsStatusCode status_code, bool success, void *user_data)` | typedef `void(*` Callback for PgsLeaderboardsClient_showAllLeaderboardsUI. |
| `https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gafb9612e9481f9e89baa5b02f21259267)(PgsStatusCode status_code, bool success, void *user_data)` | typedef `void(*` Callback for PgsLeaderboardsClient_showLeaderboardUI. |
| `https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gafcf975b94a51f932578f2717cc344c15)(PgsStatusCode status_code, PgsScoreSubmissionData *score_submission_data, void *user_data)` | typedef `void(*` Callback for PgsLeaderboardsClient_submitScoreImmediate. |

| ### Functions ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gafc73c6a8a9f1f8f45d8da7db52bb85af(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga2f1a423a29ca48ef4134c788e623ff0f *leaderboards_client, const char *leaderboard_id, https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gac19c727982519552366071770c1fc716 time_span, https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1ga5bd4c49e881aeef339962a2e43de8ef0 collection, https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1ga3452aaf991dcd1bd1151a6c7fe5bf61d callback, void *user_data)` | `void` Asynchronously loads the current player's score for a specific leaderboard with time span and collection. |
| `https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1ga7627000d33e2a57ce6725172dd16c9aa(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga2f1a423a29ca48ef4134c788e623ff0f *leaderboards_client, bool force_reload, https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1ga53b40b220af7d70ac4d6851fd0dcee27 callback, void *user_data)` | `void` Asynchronously loads leaderboard metadata. |
| `https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gac7ed86b140475c14f3ab7a7f91432c0d(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga2f1a423a29ca48ef4134c788e623ff0f *leaderboards_client, const char *leaderboard_id, bool force_reload, https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gaa8ffc35d9f9778b4adb7c158dbc062c8 callback, void *user_data)` | `void` Asynchronously loads metadata for a specific leaderboard. |
| `https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1ga51b1b2d4eb7e67bd8a51768353652a6c(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga2f1a423a29ca48ef4134c788e623ff0f *leaderboards_client, https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gac169a92c1afc06567d54621cbebe3bea *leaderboard_score_buffer, int32_t max_results, int32_t page_direction, https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1ga0d8dd14d539e16a07a591c9e1e0286b3 callback, void *user_data)` | `void` Asynchronously loads more scores for a given leaderboard score buffer. |
| `https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1ga6b64d7221abf5a40fa2b3637ec213bb2(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga2f1a423a29ca48ef4134c788e623ff0f *leaderboards_client, const char *leaderboard_id, int32_t span, int32_t collection, int32_t max_results, bool force_reload, https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gaaf561834a65bde5d19421c0b31e8661c callback, void *user_data)` | `void` Asynchronously loads player-centered scores for a specific leaderboard. |
| `https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gad7fc8914637f80ffa3063e50f3cd2ef7(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga2f1a423a29ca48ef4134c788e623ff0f *leaderboards_client, const char *leaderboard_id, https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gac19c727982519552366071770c1fc716 time_span, https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1ga5bd4c49e881aeef339962a2e43de8ef0 collection, int32_t max_results, bool force_reload, https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gaeb8514e75432684c1e1d8a501e8efa09 callback, void *user_data)` | `void` Asynchronously loads top scores for a specific leaderboard. |
| `https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gab3dd36e7fa30705f89c424fd64427a71(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga2f1a423a29ca48ef4134c788e623ff0f *leaderboards_client, jobject activity, https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gaaa7976dcb801bd3fc02683897a5161a7 callback, void *user_data)` | `void` Asynchronously loads and displays the standard leaderboards UI. |
| `https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1ga68ec1f583f2ee2b7debad33cf6fbcf4e(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga2f1a423a29ca48ef4134c788e623ff0f *leaderboards_client, jobject activity, const char *leaderboard_id, https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gac19c727982519552366071770c1fc716 time_span, https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1ga5bd4c49e881aeef339962a2e43de8ef0 collection, https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gafb9612e9481f9e89baa5b02f21259267 callback, void *user_data)` | `void` Asynchronously loads and displays the UI for a specific leaderboard with time span and collection. |
| `https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gad5072ee76c7448e2f619761341808b36(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga2f1a423a29ca48ef4134c788e623ff0f *leaderboards_client, const char *leaderboard_id, int64_t score, const char *score_tag, https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#group__leaderboards_1gafcf975b94a51f932578f2717cc344c15 callback, void *user_data)` | `void` Submits a score to a leaderboard. |

## Enumerations

### PgsLeaderboardCollection

```c++
 PgsLeaderboardCollection
```
Represents the collection type for a leaderboard.

| Properties ||
|---|---|
| `PGS_LEADERBOARD_COLLECTION_FRIENDS` | Friends leaderboards. |
| `PGS_LEADERBOARD_COLLECTION_PUBLIC` | Public leaderboards. |

### PgsLeaderboardTimeSpan

```c++
 PgsLeaderboardTimeSpan
```
Represents the time span for a leaderboard.

| Properties ||
|---|---|
| `PGS_LEADERBOARD_TIME_SPAN_ALL_TIME` | Scores are never reset. |
| `PGS_LEADERBOARD_TIME_SPAN_DAILY` | Scores are reset every day. |
| `PGS_LEADERBOARD_TIME_SPAN_WEEKLY` | Scores are reset once per week. |

## Typedefs

### PgsLeaderboardScoreBuffer

```c++
struct PgsLeaderboardScoreBuffer PgsLeaderboardScoreBuffer
```
An opaque handle to a leaderboard score buffer.

### PgsLeaderboardsClient_LoadCurrentPlayerLeaderboardScoreCallback

```c++
void(* PgsLeaderboardsClient_LoadCurrentPlayerLeaderboardScoreCallback)(PgsStatusCode status_code, PgsLeaderboardScore *score, void *user_data)
```
Callback for PgsLeaderboardsClient_loadCurrentPlayerLeaderboardScore.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. | | `score` | Pointer to a leaderboard score. This may be NULL if status_code is not PGS_STATUS_SUCCESS, or if the player has no score on this leaderboard. The caller must call PgsLeaderboardScore_Release on the score when it is no longer needed. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsLeaderboardsClient_LoadLeaderboardMetadataCallback

```c++
void(* PgsLeaderboardsClient_LoadLeaderboardMetadataCallback)(PgsStatusCode status_code, const PgsLeaderboard *leaderboards, size_t leaderboard_count, void *user_data)
```
Callback for PgsLeaderboardsClient_loadLeaderboardMetadata.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. | | `leaderboards` | Pointer to an array of leaderboards, or NULL if status is not PGS_STATUS_SUCCESS. | | `leaderboard_count` | The number of leaderboards in the array. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsLeaderboardsClient_LoadLeaderboardMetadataWithIdCallback

```c++
void(* PgsLeaderboardsClient_LoadLeaderboardMetadataWithIdCallback)(PgsStatusCode status_code, const PgsLeaderboard *leaderboard, void *user_data)
```
Callback for PgsLeaderboardsClient_loadLeaderboardMetadataWithId.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. | | `leaderboard` | Pointer to the leaderboard, or NULL if status is not PGS_STATUS_SUCCESS. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsLeaderboardsClient_LoadMoreScoresCallback

```c++
void(* PgsLeaderboardsClient_LoadMoreScoresCallback)(PgsStatusCode status_code, PgsLeaderboardScoreBuffer *leaderboard_score_buffer, PgsLeaderboardScore *scores, size_t scores_count, void *user_data)
```
Callback for PgsLeaderboardsClient_loadMoreScores.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. | | `leaderboard_score_buffer` | The leaderboard score buffer, or NULL if status is not PGS_STATUS_SUCCESS. The caller must call PgsLeaderboardScoreBuffer_Release on this object when it is no longer needed. | | `scores` | The leaderboard scores result, or NULL if status is not PGS_STATUS_SUCCESS. | | `scores_count` | The number of scores in the array. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsLeaderboardsClient_LoadPlayerCenteredScoresCallback

```c++
void(* PgsLeaderboardsClient_LoadPlayerCenteredScoresCallback)(PgsStatusCode status_code, PgsLeaderboardScoreBuffer *leaderboard_score_buffer, PgsLeaderboardScore *scores, size_t scores_count, void *user_data)
```
Callback for PgsLeaderboardsClient_loadPlayerCenteredScores.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. | | `leaderboard_score_buffer` | The leaderboard score buffer, or NULL if status is not PGS_STATUS_SUCCESS. The caller must call PgsLeaderboardScoreBuffer_Release on this object when it is no longer needed. | | `scores` | The leaderboard scores result, or NULL if status is not PGS_STATUS_SUCCESS. | | `scores_count` | The number of scores in the array. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsLeaderboardsClient_LoadTopScoresCallback

```c++
void(* PgsLeaderboardsClient_LoadTopScoresCallback)(PgsStatusCode status_code, PgsLeaderboardScoreBuffer *leaderboard_score_buffer, PgsLeaderboardScore *scores, size_t scores_count, void *user_data)
```
Callback for PgsLeaderboardsClient_loadTopScores.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. | | `scores` | The leaderboard scores result, or NULL if status is not PGS_STATUS_SUCCESS. The caller must call PgsLeaderboardScores_Release on this object when it is no longer needed. | | `leaderboard_score_buffer` | The leaderboard score buffer, or NULL if status is not PGS_STATUS_SUCCESS. The caller must call PgsLeaderboardScoreBuffer_Release on this object when it is no longer needed. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsLeaderboardsClient_ShowAllLeaderboardsUICallback

```c++
void(* PgsLeaderboardsClient_ShowAllLeaderboardsUICallback)(PgsStatusCode status_code, bool success, void *user_data)
```
Callback for PgsLeaderboardsClient_showAllLeaderboardsUI.

This is invoked after the attempt to load and display the UI.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. | | `success` | True if the UI was successfully launched, false otherwise. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsLeaderboardsClient_ShowLeaderboardUICallback

```c++
void(* PgsLeaderboardsClient_ShowLeaderboardUICallback)(PgsStatusCode status_code, bool success, void *user_data)
```
Callback for PgsLeaderboardsClient_showLeaderboardUI.

This is invoked after the attempt to load and display the UI.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. | | `success` | True if the UI was successfully launched, false otherwise. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsLeaderboardsClient_SubmitScoreImmediateCallback

```c++
void(* PgsLeaderboardsClient_SubmitScoreImmediateCallback)(PgsStatusCode status_code, PgsScoreSubmissionData *score_submission_data, void *user_data)
```
Callback for PgsLeaderboardsClient_submitScoreImmediate.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. | | `score_submission_data` | The score submission data, or NULL if status is not PGS_STATUS_SUCCESS. The caller must call PgsScoreSubmissionData_Release on the data when it is no longer needed. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

## Functions

### PgsLeaderboardsClient_loadCurrentPlayerLeaderboardScore

```c++
void PgsLeaderboardsClient_loadCurrentPlayerLeaderboardScore(
  PgsLeaderboardsClient *leaderboards_client,
  const char *leaderboard_id,
  PgsLeaderboardTimeSpan time_span,
  PgsLeaderboardCollection collection,
  PgsLeaderboardsClient_LoadCurrentPlayerLeaderboardScoreCallback callback,
  void *user_data
)
```
Asynchronously loads the current player's score for a specific leaderboard with time span and collection.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `leaderboards_client` | The client handle. | | `leaderboard_id` | The ID of the leaderboard to load score for. | | `time_span` | The time span for the leaderboard. Valid values are `PGS_LEADERBOARD_TIME_SPAN_DAILY`, `PGS_LEADERBOARD_TIME_SPAN_WEEKLY`, or `PGS_LEADERBOARD_TIME_SPAN_ALL_TIME`. | | `collection` | The collection for the leaderboard. Valid values are `PGS_LEADERBOARD_COLLECTION_PUBLIC` or `PGS_LEADERBOARD_COLLECTION_FRIENDS`. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsLeaderboardsClient_loadLeaderboardMetadata

```c++
void PgsLeaderboardsClient_loadLeaderboardMetadata(
  PgsLeaderboardsClient *leaderboards_client,
  bool force_reload,
  PgsLeaderboardsClient_LoadLeaderboardMetadataCallback callback,
  void *user_data
)
```
Asynchronously loads leaderboard metadata.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `leaderboards_client` | The client handle. | | `force_reload` | If true, this call will clear any locally cached data and attempt to fetch the latest data from the server. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsLeaderboardsClient_loadLeaderboardMetadataWithId

```c++
void PgsLeaderboardsClient_loadLeaderboardMetadataWithId(
  PgsLeaderboardsClient *leaderboards_client,
  const char *leaderboard_id,
  bool force_reload,
  PgsLeaderboardsClient_LoadLeaderboardMetadataWithIdCallback callback,
  void *user_data
)
```
Asynchronously loads metadata for a specific leaderboard.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `leaderboards_client` | The client handle. | | `leaderboard_id` | ID of the leaderboard to load metadata for. | | `force_reload` | If true, this call will clear any locally cached data and attempt to fetch the latest data from the server. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsLeaderboardsClient_loadMoreScores

```c++
void PgsLeaderboardsClient_loadMoreScores(
  PgsLeaderboardsClient *leaderboards_client,
  PgsLeaderboardScoreBuffer *leaderboard_score_buffer,
  int32_t max_results,
  int32_t page_direction,
  PgsLeaderboardsClient_LoadMoreScoresCallback callback,
  void *user_data
)
```
Asynchronously loads more scores for a given leaderboard score buffer.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `leaderboards_client` | The client handle. | | `leaderboard_score_buffer` | The buffer to load more scores from. This buffer must be obtained from a previous call to loadTopScores or loadPlayerCenteredScores. | | `max_results` | The maximum number of scores to return. | | `page_direction` | The direction to load scores from. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsLeaderboardsClient_loadPlayerCenteredScores

```c++
void PgsLeaderboardsClient_loadPlayerCenteredScores(
  PgsLeaderboardsClient *leaderboards_client,
  const char *leaderboard_id,
  int32_t span,
  int32_t collection,
  int32_t max_results,
  bool force_reload,
  PgsLeaderboardsClient_LoadPlayerCenteredScoresCallback callback,
  void *user_data
)
```
Asynchronously loads player-centered scores for a specific leaderboard.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `leaderboards_client` | The client handle. | | `leaderboard_id` | The ID of the leaderboard to load scores for. | | `span` | The time span for the leaderboard scores. | | `collection` | The score collection for the leaderboard. | | `max_results` | The maximum number of scores to return. | | `force_reload` | If true, this call will clear any locally cached data and attempt to fetch the latest data from the server. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsLeaderboardsClient_loadTopScores

```c++
void PgsLeaderboardsClient_loadTopScores(
  PgsLeaderboardsClient *leaderboards_client,
  const char *leaderboard_id,
  PgsLeaderboardTimeSpan time_span,
  PgsLeaderboardCollection collection,
  int32_t max_results,
  bool force_reload,
  PgsLeaderboardsClient_LoadTopScoresCallback callback,
  void *user_data
)
```
Asynchronously loads top scores for a specific leaderboard.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `leaderboards_client` | The client handle. | | `leaderboard_id` | The ID of the leaderboard to load scores for. | | `time_span` | The time span for the leaderboard scores. | | `collection` | The score collection for the leaderboard. | | `max_results` | The maximum number of scores to return. | | `force_reload` | If true, this call will clear any locally cached data and attempt to fetch the latest data from the server. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsLeaderboardsClient_showAllLeaderboardsUI

```c++
void PgsLeaderboardsClient_showAllLeaderboardsUI(
  PgsLeaderboardsClient *leaderboards_client,
  jobject activity,
  PgsLeaderboardsClient_ShowAllLeaderboardsUICallback callback,
  void *user_data
)
```
Asynchronously loads and displays the standard leaderboards UI.

This function asynchronously loads the necessary components and then presents the leaderboards screen to the player.

The callback is invoked to report the success or failure of the operation to load and display the UI.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `leaderboards_client` | The client handle. | | `activity` | A JNI reference to the Android Activity to use for launching the new UI. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsLeaderboardsClient_showLeaderboardUI

```c++
void PgsLeaderboardsClient_showLeaderboardUI(
  PgsLeaderboardsClient *leaderboards_client,
  jobject activity,
  const char *leaderboard_id,
  PgsLeaderboardTimeSpan time_span,
  PgsLeaderboardCollection collection,
  PgsLeaderboardsClient_ShowLeaderboardUICallback callback,
  void *user_data
)
```
Asynchronously loads and displays the UI for a specific leaderboard with time span and collection.

This function asynchronously loads the necessary components and then presents the leaderboard screen to the player.

The callback is invoked to report the success or failure of the operation to load and display the UI.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `leaderboards_client` | The client handle. | | `activity` | A JNI reference to the Android Activity to use for launching the new UI. | | `leaderboard_id` | The ID of the leaderboard to display. | | `time_span` | The time span for the leaderboard. | | `collection` | The collection for the leaderboard. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsLeaderboardsClient_submitScoreImmediate

```c++
void PgsLeaderboardsClient_submitScoreImmediate(
  PgsLeaderboardsClient *leaderboards_client,
  const char *leaderboard_id,
  int64_t score,
  const char *score_tag,
  PgsLeaderboardsClient_SubmitScoreImmediateCallback callback,
  void *user_data
)
```
Submits a score to a leaderboard.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `leaderboards_client` | The client handle. | | `leaderboard_id` | The ID of the leaderboard to submit to. | | `score` | The score to submit. | | `score_tag` | An optional score tag. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |