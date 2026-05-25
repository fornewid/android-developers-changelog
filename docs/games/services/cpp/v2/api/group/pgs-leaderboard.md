---
title: https://developer.android.com/games/services/cpp/v2/api/group/pgs-leaderboard
url: https://developer.android.com/games/services/cpp/v2/api/group/pgs-leaderboard
source: md.txt
---

# Play Games Services Leaderboard

Data interface for retrieving leaderboard information.

## Summary

| ### Enumerations ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/group/pgs-leaderboard#group__pgs__leaderboard_1gae0d0de21aaba5741e4acbbb976a2abe2{ https://developer.android.com/games/services/cpp/v2/api/group/pgs-leaderboard#group__pgs__leaderboard_1ggae0d0de21aaba5741e4acbbb976a2abe2a51cc7caf15d8d3c717616d57089d4ae3 = 0, https://developer.android.com/games/services/cpp/v2/api/group/pgs-leaderboard#group__pgs__leaderboard_1ggae0d0de21aaba5741e4acbbb976a2abe2a9b7c4744dfdc00a2251e045716643e1f = 1 }` | enumRepresents the sort order of scores for a leaderboard. |

| ### Typedefs ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/group/pgs-leaderboard#group__pgs__leaderboard_1gaab0deb8287e8522b0ee41e2d71fe7e2c` | typedef `struct https://developer.android.com/games/services/cpp/v2/api/struct/pgs-leaderboard#struct_pgs_leaderboard` Represents a single leaderboard. |

| ### Functions ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/group/pgs-leaderboard#group__pgs__leaderboard_1ga1101b0040324557f6a9f5d5e9e293b23(const https://developer.android.com/games/services/cpp/v2/api/struct/pgs-leaderboard#struct_pgs_leaderboard *leaderboard)` | `void` Releases memory held by [PgsLeaderboard](https://developer.android.com/games/services/cpp/v2/api/struct/pgs-leaderboard#struct_pgs_leaderboard), including its fields. |

| ### Structs ||
|---|---|
| [PgsLeaderboard](https://developer.android.com/games/services/cpp/v2/api/struct/pgs-leaderboard) | Represents a single leaderboard. |

## Enumerations

### PgsLeaderboardScoreOrder

```c++
 PgsLeaderboardScoreOrder
```
Represents the sort order of scores for a leaderboard.

| Properties ||
|---|---|
| `kPgsLeaderboardScoreOrderLargerIsBetter` | Scores are sorted in descending order (larger is better). |
| `kPgsLeaderboardScoreOrderSmallerIsBetter` | Scores are sorted in ascending order (smaller is better). |

## Typedefs

### PgsLeaderboard

```c++
struct PgsLeaderboard PgsLeaderboard
```
Represents a single leaderboard.

## Functions

### PgsLeaderboard_Release

```c++
void PgsLeaderboard_Release(
  const PgsLeaderboard *leaderboard
)
```
Releases memory held by [PgsLeaderboard](https://developer.android.com/games/services/cpp/v2/api/struct/pgs-leaderboard#struct_pgs_leaderboard), including its fields.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `leaderboard` | The leaderboard to release. | |