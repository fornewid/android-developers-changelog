---
title: https://developer.android.com/games/pgs/android/leaderboards
url: https://developer.android.com/games/pgs/android/leaderboards
source: md.txt
---

> [!NOTE]
> **Note:** This guide is for the Play Games Services v2 SDK. For information on the previous version of this SDK, see the [Play Games Services v1
> documentation](https://developer.android.com/games/pgs/v1/android/leaderboards).

This guide shows you how to use leaderboards APIs in an Android app
to create visual leaderboards, record a player's score, and compare the score
against the player's score from previous game sessions. The APIs can be found
in the [`com.google.android.gms.games`](https://developers.google.com/android/reference/com/google/android/gms/games/package-summary)
and [`com.google.android.gms.games.leaderboards`](https://developers.google.com/android/reference/com/google/android/gms/games/leaderboard/package-summary) packages.

## Before you begin

If you haven't already done so, you might find it helpful to review the
[leaderboards game concepts](https://developer.android.com/games/pgs/leaderboards).

Before you start to code using the leaderboards APIs:

- Follow the instructions for installing and setting up your app to use
  Google Play Games Services in the
  [Set Up Google Play Services SDK](https://developers.google.com/android/guides/setup) guide.

- Define the leaderboards that you want your game to display or update, by
  following the instructions in the
  [Google Play Console guide](https://developer.android.com/games/pgs/leaderboards#creating_a_leaderboard).

- Download and review the leaderboards code samples in the
  [Android samples page](https://github.com/playgameservices/android-basic-samples) on GiHub.

- Familiarize yourself with the recommendations described in
  [Quality Checklist](https://developer.android.com/games/pgs/quality).

## Get the leaderboards client

To start using the leaderboards API, your game must first obtain a
[`LeaderboardsClient`](https://developers.google.com/android/reference/com/google/android/gms/games/LeaderboardsClient) object.
You can do this by calling the [`PlayGames.getLeadeboardsClient()`](https://developers.google.com/android/reference/com/google/android/gms/games/PlayGames#public-static-leaderboardsclient-getleaderboardsclient-activity-activity)
method and passing in the activity.

> [!NOTE]
> **Note:** The [`LeaderboardsClient`](https://developers.google.com/android/reference/com/google/android/gms/games/LeaderboardsClient) class makes use of the Google Play services Task class to return results asynchronously. To learn more about using tasks to manage threaded work, see the [Tasks API developer guide](https://developers.google.com/android/guides/tasks).

## Update the player's score

When the player's score changes (for example, when the player finishes the game), your
game can update their score on the leaderboard by calling
[`LeaderboardsClient.submitScore()`](https://developers.google.com/android/reference/com/google/android/gms/games/LeaderboardsClient#submitScore),
and passing in the leaderboard ID and the raw score value.

The following code snippet shows how your app can update the player's score:

```
PlayGames.getLeaderboardsClient(this)
    .submitScore(getString(R.string.leaderboard_id), 1337);
```

A good practice is to define the leaderboard ID in your `strings.xml` file, so
your game can reference the leaderboards by resource ID. When making calls to
update and load player scores, make sure to also follow these
[best practices](https://developer.android.com/games/pgs/quality) to avoid exceeding your API quota.

## Display a leaderboard

To display leaderboard, call
[`LeaderboardsClient.getLeaderboardIntent()`](https://developers.google.com/android/reference/com/google/android/gms/games/LeaderboardsClient#getLeaderboardIntent(java.lang.String)) to get an
[`Intent`](https://developer.android.com/reference/android/content/Intent) to
create the default leaderboard user interface. Your game can then bring up the
UI by calling
[`startActivityForResult`](https://developer.android.com/reference/android/app/Activity#startActivityForResult).

The following code snippet shows how your app can update the player's score. In the
code snippet, `RC_LEADERBOARD_UI` is an arbitrary integer for the request code.

```
private static final int RC_LEADERBOARD_UI = 9004;

private void showLeaderboard() {
  PlayGames.getLeaderboardsClient(this)
      .getLeaderboardIntent(getString(R.string.leaderboard_id))
      .addOnSuccessListener(new OnSuccessListener<Intent>() {
        @Override
        public void onSuccess(Intent intent) {
          startActivityForResult(intent, RC_LEADERBOARD_UI);
        }
      });
}
```

Even though no result is returned, you have to use
[`startActivityForResult`](https://developer.android.com/reference/android/app/Activity#startActivityForResult)
so that the API can obtain the identity of the calling package. An example of
the default leaderboard UI is shown below.
![](https://developer.android.com/static/images/games/pgs/leaderboard_android.png)