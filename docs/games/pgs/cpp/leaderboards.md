---
title: https://developer.android.com/games/pgs/cpp/leaderboards
url: https://developer.android.com/games/pgs/cpp/leaderboards
source: md.txt
---

This guide shows you how to use the Play Games Services c++ SDK Leaderboards
APIs to create visual leaderboards, record a player's score, and compare the
score against the player's score from previous game sessions. The APIs can be
found in [`LeaderboardsClient`](https://developer.android.com/games/services/cpp/v2/api/group/play-games#pgsleaderboardsclient).

## Before you begin

If you haven't already done so, you might find it helpful to review the
[leaderboards game concepts](https://developer.android.com/games/pgs/leaderboards).

Before you start to code using the leaderboards APIs:

- Follow the instructions for installing and setting up your app to use
  Google Play Games Services in the
  [Set Up Google Play services SDK](https://developers.google.com/android/guides/setup) guide.

- Define the leaderboards that you want your game to display or update, by
  following the instructions in the
  [Google Play Console guide](https://developer.android.com/games/pgs/leaderboards#creating_a_leaderboard).

- Familiarize yourself with the recommendations described in
  [Quality Checklist](https://developer.android.com/games/pgs/quality).

## Get the leaderboards client

To start using the leaderboards API, your game must first obtain a
[`LeaderboardsClient`](https://developer.android.com/games/services/cpp/v2/api/group/play-games#pgsleaderboardsclient) object.
You can do this by calling the [`PgsLeaderboardsClient_create()`](https://developer.android.com/games/services/cpp/v2/api/group/play-games#pgsleaderboardsclient_create)
method and passing in the activity.

> [!NOTE]
> **Note:** The c++ SDK functions often return results asynchronously using callbacks. You'll provide function pointers to handle the results of operations.

## Update the player's score

When the player's score changes (for example, when the player finishes the
game), your game can update their score on the leaderboard by calling
[`PgsLeaderboardsClient_submitScoreImmediate`](https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#pgsleaderboardsclient_submitscoreimmediate). You need to pass the
leaderboard ID, the raw score value, an optional score tag, and a callback
function.

```c++
// Callback function to handle the result of submitting the score
void OnScoreSubmitted(PgsStatusCode status_code,
                      PgsScoreSubmissionData* score_submission_data,
                      void* user_data) {
  if (status_code == PGS_STATUS_SUCCESS) {
    // Score submitted successfully
    // You can inspect score_submission_data for details
    // Remember to release the data when done:
    PgsScoreSubmissionData_Release(score_submission_data);
  } else {
    // Handle error
  }
}

// Function to submit the score
void SubmitScore(PgsLeaderboardsClient* client, const char* leaderboard_id, int64_t score) {
  const char* score_tag = NULL; // Optional tag

  PgsLeaderboardsClient_submitScoreImmediate(
      client,
      leaderboard_id,
      score,
      score_tag,
      OnScoreSubmitted,
      NULL // user_data - optional context pointer
  );
}

// Example usage:
// Assuming 'my_leaderboard_id' is defined elsewhere, e.g., fetched from resources
// SubmitScore(leaderboards_client, my_leaderboard_id, 1337);
```

A good practice is to manage your leaderboard IDs as constants or resources
within your c++ code.

## Display a leaderboard

To display the default leaderboard user interface for a specific leaderboard, call [`PgsLeaderboardsClient_showLeaderboardUI`](https://developer.android.com/games/services/cpp/v2/api/group/leaderboards#pgsleaderboardsclient_showleaderboardui). This function requires the client
handle, the activity, the leaderboard ID, the time span and collection,
and a callback.

```c++
// Callback function to handle the result of showing the UI
void OnShowLeaderboardUI(PgsStatusCode status_code, bool success, void* user_data) {
  if (status_code == PGS_STATUS_SUCCESS && success) {
    // UI was shown successfully
  } else {
    // Handle error or failure to show UI
  }
}

// Function to show a specific leaderboard UI
void ShowLeaderboard(PgsLeaderboardsClient* client, jobject activity, const char* leaderboard_id) {
  PgsLeaderboardsClient_showLeaderboardUI(
      client,
      activity,
      leaderboard_id,
      PGS_LEADERBOARD_TIME_SPAN_ALL_TIME, // Or PGS_LEADERBOARD_TIME_SPAN_DAILY, PGS_LEADERBOARD_TIME_SPAN_WEEKLY
      PGS_LEADERBOARD_COLLECTION_PUBLIC,  // Or PGS_LEADERBOARD_COLLECTION_FRIENDS
      OnShowLeaderboardUI,
      NULL // user_data - optional context pointer
  );
}

// Example usage:
// ShowLeaderboard(leaderboards_client, android_activity, my_leaderboard_id);
```

This function displays the UI. The `activity` object provides the context for
displaying the UI.