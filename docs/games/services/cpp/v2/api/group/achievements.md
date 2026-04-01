---
title: https://developer.android.com/games/services/cpp/v2/api/group/achievements
url: https://developer.android.com/games/services/cpp/v2/api/group/achievements
source: md.txt
---

# Play Games Services Achievements

Native API for Play Games Services Achievements.

## Summary

| ### Typedefs ||
|---|---|
| [PgsAchievementsClient_IncrementImmediateCallback](https://developer.android.com/games/services/cpp/v2/api/group/achievements#group__achievements_1ga55a48d23fdce2d27a003f11c8ee75bda)`)(PgsStatusCode status_code, bool is_unlocked, void *user_data)` | typedef `void(*` Callback for PgsAchievementsClient_incrementImmediate. |
| [PgsAchievementsClient_LoadCallback](https://developer.android.com/games/services/cpp/v2/api/group/achievements#group__achievements_1ga00c7b2ae5bc564cb31b851d042e25ffd)`)(PgsStatusCode status_code, PgsAchievement *achievements_array, size_t achievements_count, void *user_data)` | typedef `void(*` Callback for PgsAchievementsClient_load. |
| [PgsAchievementsClient_RevealImmediateCallback](https://developer.android.com/games/services/cpp/v2/api/group/achievements#group__achievements_1gad0abbccf53c48d217d5b4b246b35296f)`)(PgsStatusCode status_code, void *user_data)` | typedef `void(*` Callback for PgsAchievementsClient_revealImmediate. |
| [PgsAchievementsClient_SetStepsImmediateCallback](https://developer.android.com/games/services/cpp/v2/api/group/achievements#group__achievements_1ga2fc87bba8bc8609411dec5378f8ccee1)`)(PgsStatusCode status_code, bool is_unlocked, void *user_data)` | typedef `void(*` Callback for PgsAchievementsClient_setStepsImmediate. |
| [PgsAchievementsClient_ShowAchievementsUICallback](https://developer.android.com/games/services/cpp/v2/api/group/achievements#group__achievements_1ga5533749ecd76d83a4d83f39d5d42cdb6)`)(PgsStatusCode status_code, bool success, void *user_data)` | typedef `void(*` Callback for PgsAchievementsClient_showAchievementsUI. |
| [PgsAchievementsClient_UnlockImmediateCallback](https://developer.android.com/games/services/cpp/v2/api/group/achievements#group__achievements_1gadb81d1b4144753c3a2221509b9b6eeb5)`)(PgsStatusCode status_code, void *user_data)` | typedef `void(*` Callback for PgsAchievementsClient_unlockImmediate. |

| ### Functions ||
|---|---|
| [PgsAchievementsClient_increment](https://developer.android.com/games/services/cpp/v2/api/group/achievements#group__achievements_1gae2ed1943942c80c59eee9a1354d86493)`(`[PgsAchievementsClient](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga1658f46313e5cebcd72479f1e8c45287)` *achievements_client, const char *achievement_id, int32_t num_steps)` | `void` Increments an achievement by the given number of steps. |
| [PgsAchievementsClient_incrementImmediate](https://developer.android.com/games/services/cpp/v2/api/group/achievements#group__achievements_1gaba97d40b2003186603d39524bbd96da0)`(`[PgsAchievementsClient](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga1658f46313e5cebcd72479f1e8c45287)` *achievements_client, const char *achievement_id, int32_t num_steps, `[PgsAchievementsClient_IncrementImmediateCallback](https://developer.android.com/games/services/cpp/v2/api/group/achievements#group__achievements_1ga55a48d23fdce2d27a003f11c8ee75bda)` callback, void *user_data)` | `void` Asynchronously increments an achievement by the given number of steps, invoking a callback upon completion. |
| [PgsAchievementsClient_load](https://developer.android.com/games/services/cpp/v2/api/group/achievements#group__achievements_1ga375060be3e89b23797585692af53f7d3)`(`[PgsAchievementsClient](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga1658f46313e5cebcd72479f1e8c45287)` *achievements_client, bool force_reload, `[PgsAchievementsClient_LoadCallback](https://developer.android.com/games/services/cpp/v2/api/group/achievements#group__achievements_1ga00c7b2ae5bc564cb31b851d042e25ffd)` callback, void *user_data)` | `void` Asynchronously loads achievement data for the currently signed-in player for this application, invoking a callback upon completion. |
| [PgsAchievementsClient_reveal](https://developer.android.com/games/services/cpp/v2/api/group/achievements#group__achievements_1ga4d1f32cd511c576771cd095eb4768bc0)`(`[PgsAchievementsClient](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga1658f46313e5cebcd72479f1e8c45287)` *achievements_client, const char *achievement_id)` | `void` Reveals a hidden achievement to the currently signed-in player. |
| [PgsAchievementsClient_revealImmediate](https://developer.android.com/games/services/cpp/v2/api/group/achievements#group__achievements_1ga66d96137f533d5ff73e5642e92a1c3f9)`(`[PgsAchievementsClient](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga1658f46313e5cebcd72479f1e8c45287)` *achievements_client, const char *achievement_id, `[PgsAchievementsClient_RevealImmediateCallback](https://developer.android.com/games/services/cpp/v2/api/group/achievements#group__achievements_1gad0abbccf53c48d217d5b4b246b35296f)` callback, void *user_data)` | `void` Asynchronously reveals a hidden achievement to the currently signed-in player, invoking a callback upon completion. |
| [PgsAchievementsClient_setSteps](https://developer.android.com/games/services/cpp/v2/api/group/achievements#group__achievements_1gaa48f4d7670e9ef5e696be1e7ef807e0c)`(`[PgsAchievementsClient](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga1658f46313e5cebcd72479f1e8c45287)` *achievements_client, const char *achievement_id, int32_t num_steps)` | `void` Sets an achievement to have at least the given number of steps completed. |
| [PgsAchievementsClient_setStepsImmediate](https://developer.android.com/games/services/cpp/v2/api/group/achievements#group__achievements_1gafccfb443fd6585865ba4ccfd64faf349)`(`[PgsAchievementsClient](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga1658f46313e5cebcd72479f1e8c45287)` *achievements_client, const char *achievement_id, int32_t num_steps, `[PgsAchievementsClient_SetStepsImmediateCallback](https://developer.android.com/games/services/cpp/v2/api/group/achievements#group__achievements_1ga2fc87bba8bc8609411dec5378f8ccee1)` callback, void *user_data)` | `void` Asynchronously sets an achievement to have at least the given number of steps completed, invoking a callback upon completion. |
| [PgsAchievementsClient_showAchievementsUI](https://developer.android.com/games/services/cpp/v2/api/group/achievements#group__achievements_1gaf8c336d80a410b121644d72df3dac2f7)`(`[PgsAchievementsClient](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga1658f46313e5cebcd72479f1e8c45287)` *achievements_client, jobject activity, `[PgsAchievementsClient_ShowAchievementsUICallback](https://developer.android.com/games/services/cpp/v2/api/group/achievements#group__achievements_1ga5533749ecd76d83a4d83f39d5d42cdb6)` callback, void *user_data)` | `void` Asynchronously loads and displays the standard achievements UI. |
| [PgsAchievementsClient_unlock](https://developer.android.com/games/services/cpp/v2/api/group/achievements#group__achievements_1ga2a2d23bc283992fa491033a954be7264)`(`[PgsAchievementsClient](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga1658f46313e5cebcd72479f1e8c45287)` *achievements_client, const char *achievement_id)` | `void` Unlocks an achievement for the currently signed-in player. |
| [PgsAchievementsClient_unlockImmediate](https://developer.android.com/games/services/cpp/v2/api/group/achievements#group__achievements_1gac121cad089ff430ac0fcb5043163551e)`(`[PgsAchievementsClient](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga1658f46313e5cebcd72479f1e8c45287)` *achievements_client, const char *achievement_id, `[PgsAchievementsClient_UnlockImmediateCallback](https://developer.android.com/games/services/cpp/v2/api/group/achievements#group__achievements_1gadb81d1b4144753c3a2221509b9b6eeb5)` callback, void *user_data)` | `void` Asynchronously unlocks an achievement for the currently signed-in player, invoking a callback upon completion. |

## Typedefs

### PgsAchievementsClient_IncrementImmediateCallback

```c++
void(* PgsAchievementsClient_IncrementImmediateCallback)(PgsStatusCode status_code, bool is_unlocked, void *user_data)
```  
Callback for PgsAchievementsClient_incrementImmediate.

This is invoked after the asynchronous operation to increment the achievement and update the server completes or fails.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. PGS_STATUS_SUCCESS on success. | | `is_unlocked` | Whether the achievement is now unlocked as a result of this increment. This is only meaningful if status_code is PGS_STATUS_SUCCESS. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsAchievementsClient_LoadCallback

```c++
void(* PgsAchievementsClient_LoadCallback)(PgsStatusCode status_code, PgsAchievement *achievements_array, size_t achievements_count, void *user_data)
```  
Callback for PgsAchievementsClient_load.

This is invoked after the asynchronous operation to load achievements completes or fails.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. PGS_STATUS_SUCCESS on success. | | `achievements_array` | Pointer to an array of [PgsAchievement](https://developer.android.com/games/services/cpp/v2/api/struct/pgs-achievement#struct_pgs_achievement) objects, or NULL if status_code is not PGS_STATUS_SUCCESS. | | `achievements_count` | The number of achievements in achievements_array. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsAchievementsClient_RevealImmediateCallback

```c++
void(* PgsAchievementsClient_RevealImmediateCallback)(PgsStatusCode status_code, void *user_data)
```  
Callback for PgsAchievementsClient_revealImmediate.

This is invoked after the asynchronous operation to reveal the achievement and update the server completes or fails.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. PGS_STATUS_SUCCESS on success. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsAchievementsClient_SetStepsImmediateCallback

```c++
void(* PgsAchievementsClient_SetStepsImmediateCallback)(PgsStatusCode status_code, bool is_unlocked, void *user_data)
```  
Callback for PgsAchievementsClient_setStepsImmediate.

This is invoked after the asynchronous operation to set the achievement steps and update the server completes or fails.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. PGS_STATUS_SUCCESS on success. | | `is_unlocked` | Whether the achievement is now unlocked as a result of this operation. This is only meaningful if status_code is PGS_STATUS_SUCCESS. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsAchievementsClient_ShowAchievementsUICallback

```c++
void(* PgsAchievementsClient_ShowAchievementsUICallback)(PgsStatusCode status_code, bool success, void *user_data)
```  
Callback for PgsAchievementsClient_showAchievementsUI.

This is invoked after the attempt to load and display the UI.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. | | `success` | True if the UI was successfully launched, false otherwise. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsAchievementsClient_UnlockImmediateCallback

```c++
void(* PgsAchievementsClient_UnlockImmediateCallback)(PgsStatusCode status_code, void *user_data)
```  
Callback for PgsAchievementsClient_unlockImmediate.

This is invoked after the asynchronous operation to unlock the achievement and update the server completes or fails.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. PGS_STATUS_SUCCESS on success. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

## Functions

### PgsAchievementsClient_increment

```c++
void PgsAchievementsClient_increment(
  PgsAchievementsClient *achievements_client,
  const char *achievement_id,
  int32_t num_steps
)
```  
Increments an achievement by the given number of steps.

The achievement must be an incremental achievement. Once an achievement reaches at least the maximum number of steps, it will be unlocked automatically. Any further increments will be ignored.

This is the fire-and-forget form of the API. Use this form if you don't need to know the status of the operation immediately. For most applications, this will be the preferred API to use, though note that the update may not be sent to the server until the next sync. See the "Immediate" version if you need the operation to attempt to communicate to the server immediately or need to have the status code delivered to your application.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `achievements_client` | The client handle. | | `achievement_id` | The achievement ID to increment. | | `num_steps` | The number of steps to increment by. Must be greater than 0. | |

### PgsAchievementsClient_incrementImmediate

```c++
void PgsAchievementsClient_incrementImmediate(
  PgsAchievementsClient *achievements_client,
  const char *achievement_id,
  int32_t num_steps,
  PgsAchievementsClient_IncrementImmediateCallback callback,
  void *user_data
)
```  
Asynchronously increments an achievement by the given number of steps, invoking a callback upon completion.

The achievement must be an incremental achievement. Once an achievement reaches at least the maximum number of steps, it will be unlocked automatically. Any further increments will be ignored.

This form of the API will attempt to update the user's achievement on the server immediately. The callback is invoked with the status and a boolean indicating whether the achievement is now unlocked.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `achievements_client` | The client handle. | | `achievement_id` | The ID of the achievement to increment. | | `num_steps` | The number of steps to increment by. Must be greater than 0. | | `callback` | Function to be called with the result of the asynchronous operation. See PgsAchievementsClient_IncrementImmediateCallback. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsAchievementsClient_load

```c++
void PgsAchievementsClient_load(
  PgsAchievementsClient *achievements_client,
  bool force_reload,
  PgsAchievementsClient_LoadCallback callback,
  void *user_data
)
```  
Asynchronously loads achievement data for the currently signed-in player for this application, invoking a callback upon completion.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `achievements_client` | The client handle. | | `force_reload` | If true, this call will clear any locally cached data and attempt to fetch the latest data from the server. This would commonly be used for something like a user-initiated refresh. Normally, this should be set to false to gain advantages of data caching. | | `callback` | Function to be called with the result of the asynchronous operation. See PgsAchievementsClient_LoadCallback. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsAchievementsClient_reveal

```c++
void PgsAchievementsClient_reveal(
  PgsAchievementsClient *achievements_client,
  const char *achievement_id
)
```  
Reveals a hidden achievement to the currently signed-in player.

If the achievement has already been unlocked, this will have no effect.

This is the "fire-and-forget" form of the API. Use this form if you do not need to know the status of the operation immediately.

Note that the update may not be sent to the server until the next sync. See the "Immediate" version if you need the operation to attempt to communicate to the server immediately or need to have the status code delivered to your application.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `achievements_client` | The client handle. | | `achievement_id` | The ID of the achievement to reveal. | |

### PgsAchievementsClient_revealImmediate

```c++
void PgsAchievementsClient_revealImmediate(
  PgsAchievementsClient *achievements_client,
  const char *achievement_id,
  PgsAchievementsClient_RevealImmediateCallback callback,
  void *user_data
)
```  
Asynchronously reveals a hidden achievement to the currently signed-in player, invoking a callback upon completion.

If the achievement is already visible, this will have no effect.

This form of the API will attempt to update the user's achievement on the server immediately. The callback is invoked with the status when the server has been updated or the operation fails.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `achievements_client` | The client handle. | | `achievement_id` | The ID of the achievement to reveal. | | `callback` | Function to be called with the result of the asynchronous operation. See PgsAchievementsClient_RevealImmediateCallback. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsAchievementsClient_setSteps

```c++
void PgsAchievementsClient_setSteps(
  PgsAchievementsClient *achievements_client,
  const char *achievement_id,
  int32_t num_steps
)
```  
Sets an achievement to have at least the given number of steps completed.

Calling this method while the achievement already has more steps than the provided value is a no-op. Once the achievement reaches the maximum number of steps, the achievement will automatically be unlocked, and any further mutation operations will be ignored.

This is the fire-and-forget form of the API. Use this form if you don't need to know the status of the operation immediately. For most applications, this will be the preferred API to use, though note that the update may not be sent to the server until the next sync. See the "Immediate" version if you need the operation to attempt to communicate to the server immediately or need to have the status code delivered to your application.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `achievements_client` | The client handle. | | `achievement_id` | The ID of the achievement to modify. | | `num_steps` | The number of steps to set the achievement to. Must be greater than 0. | |

### PgsAchievementsClient_setStepsImmediate

```c++
void PgsAchievementsClient_setStepsImmediate(
  PgsAchievementsClient *achievements_client,
  const char *achievement_id,
  int32_t num_steps,
  PgsAchievementsClient_SetStepsImmediateCallback callback,
  void *user_data
)
```  
Asynchronously sets an achievement to have at least the given number of steps completed, invoking a callback upon completion.

Calling this method while the achievement already has more steps than the provided value is a no-op. Once the achievement reaches the maximum number of steps, the achievement will automatically be unlocked, and any further mutation operations will be ignored.

This form of the API will attempt to update the user's achievement on the server immediately. The callback is invoked with the status and a boolean indicating whether the achievement is now unlocked.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `achievements_client` | The client handle. | | `achievement_id` | The ID of the achievement to set steps on. | | `num_steps` | The number of steps to set for the achievement. Must be greater than 0. | | `callback` | Function to be called with the result of the asynchronous operation. See PgsAchievementsClient_SetStepsImmediateCallback. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsAchievementsClient_showAchievementsUI

```c++
void PgsAchievementsClient_showAchievementsUI(
  PgsAchievementsClient *achievements_client,
  jobject activity,
  PgsAchievementsClient_ShowAchievementsUICallback callback,
  void *user_data
)
```  
Asynchronously loads and displays the standard achievements UI.

This function asynchronously loads the necessary components and then presents the achievements screen to the player.

The callback is invoked to report the success or failure of the operation to load and display the UI.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `achievements_client` | The client handle. | | `activity` | A JNI reference to the Android Activity to use for launching the new UI. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsAchievementsClient_unlock

```c++
void PgsAchievementsClient_unlock(
  PgsAchievementsClient *achievements_client,
  const char *achievement_id
)
```  
Unlocks an achievement for the currently signed-in player.

If the achievement is hidden, this will reveal it to the player.

This is the "fire-and-forget" form of the API. Use this form if you do not need to know the status of the operation immediately.

Note that the update may not be sent to the server until the next sync. If you need the operation to attempt to communicate to the server immediately or need to have the status code delivered, please use the "Immediate" version of this function.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `achievements_client` | The client handle. | | `achievement_id` | The ID of the achievement to unlock. | |

### PgsAchievementsClient_unlockImmediate

```c++
void PgsAchievementsClient_unlockImmediate(
  PgsAchievementsClient *achievements_client,
  const char *achievement_id,
  PgsAchievementsClient_UnlockImmediateCallback callback,
  void *user_data
)
```  
Asynchronously unlocks an achievement for the currently signed-in player, invoking a callback upon completion.

If the achievement is hidden, this will reveal it to the player.

This form of the API will attempt to update the user's achievement on the server immediately. The callback is invoked with the status when the server has been updated or the operation fails.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `achievements_client` | The client handle. | | `achievement_id` | The ID of the achievement to unlock. | | `callback` | Function to be called with the result of the asynchronous operation. See PgsAchievementsClient_UnlockImmediateCallback. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |