---
title: https://developer.android.com/games/services/cpp/v2/api/group/score-submission-data
url: https://developer.android.com/games/services/cpp/v2/api/group/score-submission-data
source: md.txt
---

# Score Submission Data

Native API for Play Games Services Score Submission Data.

## Summary

| ### Typedefs ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/group/score-submission-data#group___score_submission_data_1gaacaf0e8a0afd4fc092563e6af8008205` | typedef `struct https://developer.android.com/games/services/cpp/v2/api/struct/pgs-score-submission-data#struct_pgs_score_submission_data` Play Games Services score submission data. |
| `https://developer.android.com/games/services/cpp/v2/api/group/score-submission-data#group___score_submission_data_1ga4d6321c2e8375c841015e244345d8e54` | typedef `struct https://developer.android.com/games/services/cpp/v2/api/struct/pgs-score-submission-result#struct_pgs_score_submission_result` A Play Games Services score submission result. |

| ### Functions ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/group/score-submission-data#group___score_submission_data_1ga074ab4873e72545441f439b53cf4838c(https://developer.android.com/games/services/cpp/v2/api/struct/pgs-score-submission-data#struct_pgs_score_submission_data *data)` | `void` Releases memory used by score submission data. |

| ### Structs ||
|---|---|
| [PgsScoreSubmissionData](https://developer.android.com/games/services/cpp/v2/api/struct/pgs-score-submission-data) | Play Games Services score submission data. |
| [PgsScoreSubmissionResult](https://developer.android.com/games/services/cpp/v2/api/struct/pgs-score-submission-result) | A Play Games Services score submission result. |

## Typedefs

### PgsScoreSubmissionData

```c++
struct PgsScoreSubmissionData PgsScoreSubmissionData
```
Play Games Services score submission data.

### PgsScoreSubmissionResult

```c++
struct PgsScoreSubmissionResult PgsScoreSubmissionResult
```
A Play Games Services score submission result.

## Functions

### PgsScoreSubmissionData_Release

```c++
void PgsScoreSubmissionData_Release(
  PgsScoreSubmissionData *data
)
```
Releases memory used by score submission data.