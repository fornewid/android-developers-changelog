---
title: https://developer.android.com/games/services/cpp/v2/api/struct/pgs-score-submission-result
url: https://developer.android.com/games/services/cpp/v2/api/struct/pgs-score-submission-result
source: md.txt
---

# PgsScoreSubmissionResult

A Play Games Services score submission result.

## Summary

| ### Public attributes ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-score-submission-result#struct_pgs_score_submission_result_1a2442b89d96053b7e467824c5baa63d8c` | `char *` The score data in a display-appropriate format. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-score-submission-result#struct_pgs_score_submission_result_1a046965e2504ea2c071c960dea75c4d99` | `bool` Whether or not this score was the player's new best score for this time span. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-score-submission-result#struct_pgs_score_submission_result_1af3692658dc682bc7e0068d4ed1366ecc` | `int64_t` The raw score. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-score-submission-result#struct_pgs_score_submission_result_1a9fd073dc84b6f3d563ae9e0a8f9b1c79` | `char *` The score tag associated with this result, if any. |

## Public attributes

### formatted_score

```c++
char * PgsScoreSubmissionResult::formatted_score
```
The score data in a display-appropriate format.

### new_best

```c++
bool PgsScoreSubmissionResult::new_best
```
Whether or not this score was the player's new best score for this time span.

### raw_score

```c++
int64_t PgsScoreSubmissionResult::raw_score
```
The raw score.

### score_tag

```c++
char * PgsScoreSubmissionResult::score_tag
```
The score tag associated with this result, if any.