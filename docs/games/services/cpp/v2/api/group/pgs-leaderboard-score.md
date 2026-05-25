---
title: https://developer.android.com/games/services/cpp/v2/api/group/pgs-leaderboard-score
url: https://developer.android.com/games/services/cpp/v2/api/group/pgs-leaderboard-score
source: md.txt
---

# Play Games Services LeaderboardScore

Data interface for retrieving leaderboard score information.

## Summary

| ### Typedefs ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/group/pgs-leaderboard-score#group__pgs__leaderboard__score_1ga229064b09c09913b6892214b91836a76` | typedef `struct https://developer.android.com/games/services/cpp/v2/api/struct/pgs-leaderboard-score#struct_pgs_leaderboard_score` Represents a single leaderboard score. |

| ### Functions ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/group/pgs-leaderboard-score#group__pgs__leaderboard__score_1ga717115a9eef051b6e2c53267cf966273(https://developer.android.com/games/services/cpp/v2/api/struct/pgs-leaderboard-score#struct_pgs_leaderboard_score *leaderboard_score)` | `void` Releases memory held by [PgsLeaderboardScore](https://developer.android.com/games/services/cpp/v2/api/struct/pgs-leaderboard-score#struct_pgs_leaderboard_score), including its fields. |

| ### Structs ||
|---|---|
| [PgsLeaderboardScore](https://developer.android.com/games/services/cpp/v2/api/struct/pgs-leaderboard-score) | Represents a single leaderboard score. |

## Typedefs

### PgsLeaderboardScore

```c++
struct PgsLeaderboardScore PgsLeaderboardScore
```
Represents a single leaderboard score.

## Functions

### PgsLeaderboardScore_Release

```c++
void PgsLeaderboardScore_Release(
  PgsLeaderboardScore *leaderboard_score
)
```
Releases memory held by [PgsLeaderboardScore](https://developer.android.com/games/services/cpp/v2/api/struct/pgs-leaderboard-score#struct_pgs_leaderboard_score), including its fields.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `leaderboard_score` | The leaderboard score to release. | |