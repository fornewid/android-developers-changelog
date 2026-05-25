---
title: https://developer.android.com/games/services/cpp/v2/api/struct/pgs-achievement
url: https://developer.android.com/games/services/cpp/v2/api/struct/pgs-achievement
source: md.txt
---

# PgsAchievement

Represents a single achievement.

## Summary

| ### Public attributes ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-achievement#struct_pgs_achievement_1a09d3f26b66b38e51fa15bd952cb0ecb9` | `const char *` The ID of this achievement. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-achievement#struct_pgs_achievement_1ac5dab9cb5fc52fcb62a432a7d17b3e85` | `int32_t` The number of steps completed if this is an incremental achievement, 0 otherwise. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-achievement#struct_pgs_achievement_1ada3686eb4af4519261cb4ee6f36cb08e` | `const char *` The description of this achievement. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-achievement#struct_pgs_achievement_1aaf0f42875be821896c6a57b79f2c7771` | `int64_t` The timestamp (in milliseconds since epoch) at which this achievement was last updated. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-achievement#struct_pgs_achievement_1ac08ae91704cf7bee33f5d6b740e6b1b7` | `const char *` The name of this achievement. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-achievement#struct_pgs_achievement_1a88e82332f059e45e6347f52be259c424` | `const char *` The URI for the revealed image of this achievement. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-achievement#struct_pgs_achievement_1ab3adad4e37c598d0674fb4de5808683c` | `https://developer.android.com/games/services/cpp/v2/api/group/pgs-achievement#group__pgs__achievement_1ga16b4ae8d19986cc35563db0d0302ca29` The state of this achievement. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-achievement#struct_pgs_achievement_1a39721ecc552ed7e5c2a7d83916ba96f6` | `int32_t` The total number of steps if this is an incremental achievement, 0 otherwise. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-achievement#struct_pgs_achievement_1ab947a2e578295de5f8d1b3628a00322a` | `https://developer.android.com/games/services/cpp/v2/api/group/pgs-achievement#group__pgs__achievement_1ga3808f49f6a713a92fe4c2399c2097fc7` The type of this achievement. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-achievement#struct_pgs_achievement_1a2fc64764b696db918480535c72cff929` | `const char *` The URI for the unlocked image of this achievement. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-achievement#struct_pgs_achievement_1a38b4d6dfed02aaed4d9463e6dc92a9d6` | `int64_t` The XP value of this achievement. |

## Public attributes

### achievement_id

```c++
const char * PgsAchievement::achievement_id
```
The ID of this achievement.

### current_steps

```c++
int32_t PgsAchievement::current_steps
```
The number of steps completed if this is an incremental achievement, 0 otherwise.

### description

```c++
const char * PgsAchievement::description
```
The description of this achievement.

### last_updated_timestamp

```c++
int64_t PgsAchievement::last_updated_timestamp
```
The timestamp (in milliseconds since epoch) at which this achievement was last updated.

### name

```c++
const char * PgsAchievement::name
```
The name of this achievement.

### revealed_image_uri

```c++
const char * PgsAchievement::revealed_image_uri
```
The URI for the revealed image of this achievement.

### state

```c++
PgsAchievementState PgsAchievement::state
```
The state of this achievement.

### total_steps

```c++
int32_t PgsAchievement::total_steps
```
The total number of steps if this is an incremental achievement, 0 otherwise.

### type

```c++
PgsAchievementType PgsAchievement::type
```
The type of this achievement.

### unlocked_image_uri

```c++
const char * PgsAchievement::unlocked_image_uri
```
The URI for the unlocked image of this achievement.

### xp_value

```c++
int64_t PgsAchievement::xp_value
```
The XP value of this achievement.