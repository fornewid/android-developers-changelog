---
title: Play Games Services Achievements  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/cpp/v2/api/group/achievements
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# Play Games Services Achievements

Native API for Play Games Services Achievements.

## Summary

| Typedefs | |
| --- | --- |
| `PgsAchievementsClient_IncrementImmediateCallback)(PgsStatusCode status_code, bool is_unlocked, void *user_data)` | typedef `void(*`  Callback for PgsAchievementsClient\_incrementImmediate. |
| `PgsAchievementsClient_LoadCallback)(PgsStatusCode status_code, PgsAchievement *achievements_array, size_t achievements_count, void *user_data)` | typedef `void(*`  Callback for PgsAchievementsClient\_load. |
| `PgsAchievementsClient_RevealImmediateCallback)(PgsStatusCode status_code, void *user_data)` | typedef `void(*`  Callback for PgsAchievementsClient\_revealImmediate. |
| `PgsAchievementsClient_SetStepsImmediateCallback)(PgsStatusCode status_code, bool is_unlocked, void *user_data)` | typedef `void(*`  Callback for PgsAchievementsClient\_setStepsImmediate. |
| `PgsAchievementsClient_ShowAchievementsUICallback)(PgsStatusCode status_code, bool success, void *user_data)` | typedef `void(*`  Callback for PgsAchievementsClient\_showAchievementsUI. |
| `PgsAchievementsClient_UnlockImmediateCallback)(PgsStatusCode status_code, void *user_data)` | typedef `void(*`  Callback for PgsAchievementsClient\_unlockImmediate. |

| Functions | |
| --- | --- |
| `PgsAchievementsClient_increment(PgsAchievementsClient *achievements_client, const char *achievement_id, int32_t num_steps)` | `void`  Increments an achievement by the given number of steps. |
| `PgsAchievementsClient_incrementImmediate(PgsAchievementsClient *achievements_client, const char *achievement_id, int32_t num_steps, PgsAchievementsClient_IncrementImmediateCallback callback, void *user_data)` | `void`  Asynchronously increments an achievement by the given number of steps, invoking a callback upon completion. |
| `PgsAchievementsClient_load(PgsAchievementsClient *achievements_client, bool force_reload, PgsAchievementsClient_LoadCallback callback, void *user_data)` | `void`  Asynchronously loads achievement data for the currently signed-in player for this application, invoking a callback upon completion. |
| `PgsAchievementsClient_reveal(PgsAchievementsClient *achievements_client, const char *achievement_id)` | `void`  Reveals a hidden achievement to the currently signed-in player. |
| `PgsAchievementsClient_revealImmediate(PgsAchievementsClient *achievements_client, const char *achievement_id, PgsAchievementsClient_RevealImmediateCallback callback, void *user_data)` | `void`  Asynchronously reveals a hidden achievement to the currently signed-in player, invoking a callback upon completion. |
| `PgsAchievementsClient_setSteps(PgsAchievementsClient *achievements_client, const char *achievement_id, int32_t num_steps)` | `void`  Sets an achievement to have at least the given number of steps completed. |
| `PgsAchievementsClient_setStepsImmediate(PgsAchievementsClient *achievements_client, const char *achievement_id, int32_t num_steps, PgsAchievementsClient_SetStepsImmediateCallback callback, void *user_data)` | `void`  Asynchronously sets an achievement to have at least the given number of steps completed, invoking a callback upon completion. |
| `PgsAchievementsClient_showAchievementsUI(PgsAchievementsClient *achievements_client, jobject activity, PgsAchievementsClient_ShowAchievementsUICallback callback, void *user_data)` | `void`  Asynchronously loads and displays the standard achievements UI. |
| `PgsAchievementsClient_unlock(PgsAchievementsClient *achievements_client, const char *achievement_id)` | `void`  Unlocks an achievement for the currently signed-in player. |
| `PgsAchievementsClient_unlockImmediate(PgsAchievementsClient *achievements_client, const char *achievement_id, PgsAchievementsClient_UnlockImmediateCallback callback, void *user_data)` | `void`  Asynchronously unlocks an achievement for the currently signed-in player, invoking a callback upon completion. |

## Typedefs

### PgsAchievementsClient\_IncrementImmediateCallback

```
void(* PgsAchievementsClient_IncrementImmediateCallback)(PgsStatusCode status_code, bool is_unlocked, void *user_data)
```

Callback for PgsAchievementsClient\_incrementImmediate.

This is invoked after the asynchronous operation to increment the achievement and update the server completes or fails.

Details | || Parameters | |  |  | | --- | --- | | `status_code` | Result of the operation. PGS\_STATUS\_SUCCESS on success. | | `is_unlocked` | Whether the achievement is now unlocked as a result of this increment. This is only meaningful if status\_code is PGS\_STATUS\_SUCCESS. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsAchievementsClient\_LoadCallback

```
void(* PgsAchievementsClient_LoadCallback)(PgsStatusCode status_code, PgsAchievement *achievements_array, size_t achievements_count, void *user_data)
```

Callback for PgsAchievementsClient\_load.

This is invoked after the asynchronous operation to load achievements completes or fails.

Details | || Parameters | |  |  | | --- | --- | | `status_code` | Result of the operation. PGS\_STATUS\_SUCCESS on success. | | `achievements_array` | Pointer to an array of [PgsAchievement](/games/services/cpp/v2/api/struct/pgs-achievement#struct_pgs_achievement) objects, or NULL if status\_code is not PGS\_STATUS\_SUCCESS. | | `achievements_count` | The number of achievements in achievements\_array. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsAchievementsClient\_RevealImmediateCallback

```
void(* PgsAchievementsClient_RevealImmediateCallback)(PgsStatusCode status_code, void *user_data)
```

Callback for PgsAchievementsClient\_revealImmediate.

This is invoked after the asynchronous operation to reveal the achievement and update the server completes or fails.

Details | || Parameters | |  |  | | --- | --- | | `status_code` | Result of the operation. PGS\_STATUS\_SUCCESS on success. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsAchievementsClient\_SetStepsImmediateCallback

```
void(* PgsAchievementsClient_SetStepsImmediateCallback)(PgsStatusCode status_code, bool is_unlocked, void *user_data)
```

Callback for PgsAchievementsClient\_setStepsImmediate.

This is invoked after the asynchronous operation to set the achievement steps and update the server completes or fails.

Details | || Parameters | |  |  | | --- | --- | | `status_code` | Result of the operation. PGS\_STATUS\_SUCCESS on success. | | `is_unlocked` | Whether the achievement is now unlocked as a result of this operation. This is only meaningful if status\_code is PGS\_STATUS\_SUCCESS. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsAchievementsClient\_ShowAchievementsUICallback

```
void(* PgsAchievementsClient_ShowAchievementsUICallback)(PgsStatusCode status_code, bool success, void *user_data)
```

Callback for PgsAchievementsClient\_showAchievementsUI.

This is invoked after the attempt to load and display the UI.

Details | || Parameters | |  |  | | --- | --- | | `status_code` | Result of the operation. | | `success` | True if the UI was successfully launched, false otherwise. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsAchievementsClient\_UnlockImmediateCallback

```
void(* PgsAchievementsClient_UnlockImmediateCallback)(PgsStatusCode status_code, void *user_data)
```

Callback for PgsAchievementsClient\_unlockImmediate.

This is invoked after the asynchronous operation to unlock the achievement and update the server completes or fails.

Details | || Parameters | |  |  | | --- | --- | | `status_code` | Result of the operation. PGS\_STATUS\_SUCCESS on success. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

## Functions

### PgsAchievementsClient\_increment

```
void PgsAchievementsClient_increment(
  PgsAchievementsClient *achievements_client,
  const char *achievement_id,
  int32_t num_steps
)
```

Increments an achievement by the given number of steps.

The achievement must be an incremental achievement. Once an achievement reaches at least the maximum number of steps, it will be unlocked automatically. Any further increments will be ignored.

This is the fire-and-forget form of the API. Use this form if you don't need to know the status of the operation immediately. For most applications, this will be the preferred API to use, though note that the update may not be sent to the server until the next sync. See the "Immediate" version if you need the operation to attempt to communicate to the server immediately or need to have the status code delivered to your application.

Details | || Parameters | |  |  | | --- | --- | | `achievements_client` | The client handle. | | `achievement_id` | The achievement ID to increment. | | `num_steps` | The number of steps to increment by. Must be greater than 0. | |

### PgsAchievementsClient\_incrementImmediate

```
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

Details | || Parameters | |  |  | | --- | --- | | `achievements_client` | The client handle. | | `achievement_id` | The ID of the achievement to increment. | | `num_steps` | The number of steps to increment by. Must be greater than 0. | | `callback` | Function to be called with the result of the asynchronous operation. See PgsAchievementsClient\_IncrementImmediateCallback. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsAchievementsClient\_load

```
void PgsAchievementsClient_load(
  PgsAchievementsClient *achievements_client,
  bool force_reload,
  PgsAchievementsClient_LoadCallback callback,
  void *user_data
)
```

Asynchronously loads achievement data for the currently signed-in player for this application, invoking a callback upon completion.

Details | || Parameters | |  |  | | --- | --- | | `achievements_client` | The client handle. | | `force_reload` | If true, this call will clear any locally cached data and attempt to fetch the latest data from the server. This would commonly be used for something like a user-initiated refresh. Normally, this should be set to false to gain advantages of data caching. | | `callback` | Function to be called with the result of the asynchronous operation. See PgsAchievementsClient\_LoadCallback. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsAchievementsClient\_reveal

```
void PgsAchievementsClient_reveal(
  PgsAchievementsClient *achievements_client,
  const char *achievement_id
)
```

Reveals a hidden achievement to the currently signed-in player.

If the achievement has already been unlocked, this will have no effect.

This is the "fire-and-forget" form of the API. Use this form if you do not need to know the status of the operation immediately.

Note that the update may not be sent to the server until the next sync. See the "Immediate" version if you need the operation to attempt to communicate to the server immediately or need to have the status code delivered to your application.

Details | || Parameters | |  |  | | --- | --- | | `achievements_client` | The client handle. | | `achievement_id` | The ID of the achievement to reveal. | |

### PgsAchievementsClient\_revealImmediate

```
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

Details | || Parameters | |  |  | | --- | --- | | `achievements_client` | The client handle. | | `achievement_id` | The ID of the achievement to reveal. | | `callback` | Function to be called with the result of the asynchronous operation. See PgsAchievementsClient\_RevealImmediateCallback. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsAchievementsClient\_setSteps

```
void PgsAchievementsClient_setSteps(
  PgsAchievementsClient *achievements_client,
  const char *achievement_id,
  int32_t num_steps
)
```

Sets an achievement to have at least the given number of steps completed.

Calling this method while the achievement already has more steps than the provided value is a no-op. Once the achievement reaches the maximum number of steps, the achievement will automatically be unlocked, and any further mutation operations will be ignored.

This is the fire-and-forget form of the API. Use this form if you don't need to know the status of the operation immediately. For most applications, this will be the preferred API to use, though note that the update may not be sent to the server until the next sync. See the "Immediate" version if you need the operation to attempt to communicate to the server immediately or need to have the status code delivered to your application.

Details | || Parameters | |  |  | | --- | --- | | `achievements_client` | The client handle. | | `achievement_id` | The ID of the achievement to modify. | | `num_steps` | The number of steps to set the achievement to. Must be greater than 0. | |

### PgsAchievementsClient\_setStepsImmediate

```
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

Details | || Parameters | |  |  | | --- | --- | | `achievements_client` | The client handle. | | `achievement_id` | The ID of the achievement to set steps on. | | `num_steps` | The number of steps to set for the achievement. Must be greater than 0. | | `callback` | Function to be called with the result of the asynchronous operation. See PgsAchievementsClient\_SetStepsImmediateCallback. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsAchievementsClient\_showAchievementsUI

```
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

Details | || Parameters | |  |  | | --- | --- | | `achievements_client` | The client handle. | | `activity` | A JNI reference to the Android Activity to use for launching the new UI. | | `callback` | Function to be called with the result. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsAchievementsClient\_unlock

```
void PgsAchievementsClient_unlock(
  PgsAchievementsClient *achievements_client,
  const char *achievement_id
)
```

Unlocks an achievement for the currently signed-in player.

If the achievement is hidden, this will reveal it to the player.

This is the "fire-and-forget" form of the API. Use this form if you do not need to know the status of the operation immediately.

Note that the update may not be sent to the server until the next sync. If you need the operation to attempt to communicate to the server immediately or need to have the status code delivered, please use the "Immediate" version of this function.

Details | || Parameters | |  |  | | --- | --- | | `achievements_client` | The client handle. | | `achievement_id` | The ID of the achievement to unlock. | |

### PgsAchievementsClient\_unlockImmediate

```
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

Details | || Parameters | |  |  | | --- | --- | | `achievements_client` | The client handle. | | `achievement_id` | The ID of the achievement to unlock. | | `callback` | Function to be called with the result of the asynchronous operation. See PgsAchievementsClient\_UnlockImmediateCallback. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |