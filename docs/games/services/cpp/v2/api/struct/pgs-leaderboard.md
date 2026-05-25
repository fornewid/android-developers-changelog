---
title: https://developer.android.com/games/services/cpp/v2/api/struct/pgs-leaderboard
url: https://developer.android.com/games/services/cpp/v2/api/struct/pgs-leaderboard
source: md.txt
---

# PgsLeaderboard

Represents a single leaderboard.

## Summary

| ### Public attributes ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-leaderboard#struct_pgs_leaderboard_1a2be26f663e66d8057acca9474238efef` | `const char *` The display name of this leaderboard. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-leaderboard#struct_pgs_leaderboard_1a40b19b8c5e45973edfb000de9894c846` | `const char *` The URI for the icon of this leaderboard. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-leaderboard#struct_pgs_leaderboard_1a550446b43c6f957caef408a538f48c78` | `const char *` The ID of this leaderboard. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-leaderboard#struct_pgs_leaderboard_1ad8e7a782a77141e4d6ffc1c323b9ec48` | `https://developer.android.com/games/services/cpp/v2/api/group/pgs-leaderboard#group__pgs__leaderboard_1gae0d0de21aaba5741e4acbbb976a2abe2` The score order of this leaderboard. |

## Public attributes

### display_name

```c++
const char * PgsLeaderboard::display_name
```
The display name of this leaderboard.

### icon_image_uri

```c++
const char * PgsLeaderboard::icon_image_uri
```
The URI for the icon of this leaderboard.

### leaderboard_id

```c++
const char * PgsLeaderboard::leaderboard_id
```
The ID of this leaderboard.

### score_order

```c++
PgsLeaderboardScoreOrder PgsLeaderboard::score_order
```
The score order of this leaderboard.