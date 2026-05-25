---
title: https://developer.android.com/games/services/cpp/v2/api/struct/pgs-score-submission-data
url: https://developer.android.com/games/services/cpp/v2/api/struct/pgs-score-submission-data
source: md.txt
---

# PgsScoreSubmissionData

Play Games Services score submission data.

## Summary

| ### Public attributes ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-score-submission-data#struct_pgs_score_submission_data_1a8de2297bbeb75daa07b0ddf07946798e` | `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-score-submission-result#struct_pgs_score_submission_result *` Result for all-time timespan. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-score-submission-data#struct_pgs_score_submission_data_1a48a478b65534bdfa7aea7aa44817c1c9` | `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-score-submission-result#struct_pgs_score_submission_result *` Result for daily timespan. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-score-submission-data#struct_pgs_score_submission_data_1a7e06bab110a95464c6d309be0df84600` | `char *` The leaderboard ID that the score was submitted to. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-score-submission-data#struct_pgs_score_submission_data_1a28fa24d5d159893e9730f901f9c111b8` | `char *` The player ID submitting the score. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-score-submission-data#struct_pgs_score_submission_data_1aeb366ad17e0199c50c48b8a84ee52b57` | `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-score-submission-result#struct_pgs_score_submission_result *` Result for weekly timespan. |

## Public attributes

### all_time_result

```c++
PgsScoreSubmissionResult * PgsScoreSubmissionData::all_time_result
```
Result for all-time timespan.

### daily_result

```c++
PgsScoreSubmissionResult * PgsScoreSubmissionData::daily_result
```
Result for daily timespan.

### leaderboard_id

```c++
char * PgsScoreSubmissionData::leaderboard_id
```
The leaderboard ID that the score was submitted to.

### player_id

```c++
char * PgsScoreSubmissionData::player_id
```
The player ID submitting the score.

### weekly_result

```c++
PgsScoreSubmissionResult * PgsScoreSubmissionData::weekly_result
```
Result for weekly timespan.