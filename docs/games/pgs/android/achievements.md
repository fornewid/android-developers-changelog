---
title: https://developer.android.com/games/pgs/android/achievements
url: https://developer.android.com/games/pgs/android/achievements
source: md.txt
---

| **Note:** This guide is for the Play Games Services v2 SDK. For information about the previous version of this SDK, see the [Play Games Services v1
| documentation](https://developer.android.com/games/pgs/v1/android/achievements).

This guide shows you how to use the achievements APIs in an Android application
to unlock and display achievements in your game. The APIs can be found
in the [`com.google.android.gms.games`](https://developers.google.com//android/reference/com/google/android/gms/games/package-summary)
and [`com.google.android.gms.games.achievements`](https://developers.google.com//android/reference/com/google/android/gms/games/achievement/package-summary)
packages.

## Before you begin

If you haven't already done so, you might find it helpful to review the
[achievements game concepts](https://developer.android.com/games/pgs/achievements).

Before you start to code using the achievements API:

- Follow the instructions for installing and setting up your app to use
  Google Play Games Services in the
  [Set Up Google Play Services SDK](https://developers.google.com/android/guides/setup) guide.

- Define the achievements that you want your game to unlock or display, by
  following the instructions in the [Google Play Console guide](https://developer.android.com/games/pgs/achievements#creating_an_achievement).

- Download and review the achievements code samples in the
  [Android samples page](https://github.com/playgameservices/android-basic-samples).

- Familiarize yourself with the recommendations described in
  [Quality Checklist](https://developer.android.com/games/pgs/quality).

## Get an achievements client

To start using the achievements API, your game must first obtain an
[`AchievementsClient`](https://developers.google.com/android/reference/com/google/android/gms/games/AchievementsClient)
object. You can do this by calling the
[`Games.getAchievementClient()`](https://developers.google.com/android/reference/com/google/android/gms/games/AchievementsClient#public-abstract-taskintent-getachievementsintent)
method and passing in the activity.
| **Note:** The [`AchievementsClient`](https://developers.google.com/android/reference/com/google/android/gms/games/AchievementsClient) class makes use of the Google Play services [`Task`](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task) class to return results asynchronously. To learn more about using tasks to manage threaded work, see the [Tasks API developer guide](https://developers.google.com/android/guides/tasks).

## Unlock achievements

To unlock an achievement, call the
[`AchievementsClient.unlock()`](https://developers.google.com/android/reference/com/google/android/gms/games/AchievementsClient#unlock(java.lang.String))
method and pass in the achievement ID.

The following code snippet shows how your app can unlock achievements:

```scdoc
PlayGames.getAchievementsClient(this).unlock(getString(R.string.my_achievement_id));
```

If the achievement is of the *incremental* type (that is, several steps are
required to unlock it), call [`AchievementsClient.increment()`](https://developers.google.com/android/reference/com/google/android/gms/games/AchievementsClient#increment(java.lang.String,%20int))
instead.

The following code snippet shows how your app can increment the player's
achievement:

```scdoc
PlayGames.getAchievementsClient(this).increment(getString(R.string.my_achievement_id), 1);
```

You don't need to write additional code to unlock the achievement; Google Play Games Services
automatically unlocks the achievement once it reaches its required number of
steps.

A good practice is to define the achievement IDs in the `strings.xml` file, so
your game can reference the achievements by resource ID. When making calls to
update and load achievements, make sure to also follow these
[best practices](https://developer.android.com/games/pgs/quality) to avoid exceeding your API
quota.

## Display achievements

To show a player's achievements, call
[`AchievementsClient.getAchievementsIntent()`](https://developers.google.com/android/reference/com/google/android/gms/games/AchievementsClient#public-abstract-taskintent-getachievementsintent)
to get an
[`Intent`](http://developer.android.com/reference/android/content/Intent.html)
to create the default achievements user interface. Your game can then bring up
the UI by calling
[`startActivityForResult`](http://developer.android.com/reference/android/app/Activity#startActivityForResult(android.content.Intent,%20int)).

The following code snippet shows how your app can display the default
achievement user interface. In the snippet, `RC_ACHIEVEMENT_UI` is an arbitrary
integer that the game uses as the request code.

```transact-sql
private static final int RC_ACHIEVEMENT_UI = 9003;

private void showAchievements() {
  PlayGames.getAchievementsClient(this)
      .getAchievementsIntent()
      .addOnSuccessListener(new OnSuccessListener<Intent>() {
        @Override
        public void onSuccess(Intent intent) {
          startActivityForResult(intent, RC_ACHIEVEMENT_UI);
        }
      });
}
```

The following image shows an example of the default achievements UI.

The **Suggested** row shows the most common revealed achievement, which is the
one
the player hasn't unlocked yet but the highest percentage of other players have.
![](https://developer.android.com/static/images/games/pgs/achievements_android.png)