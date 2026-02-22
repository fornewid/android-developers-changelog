---
title: https://developer.android.com/games/pgs/android/stats
url: https://developer.android.com/games/pgs/android/stats
source: md.txt
---

| **Note:** This guide is for the Play Games Services v2 SDK. For information on the previous version of this SDK, see the [Play Games Services v1
| documentation](https://developer.android.com/games/pgs/v1/android/stats).

This guide shows you how to use the player stats API for Google Play Games Services. You can
use the player stats API to retrieve data about a player's in-game activity.
| **Important:** Based on results from experiments with this API, we've stopped populating the following endpoints: Churn probability, Spend probability, Total spend next 28 days, and High spender probability. Each of these endpoints now always returns an unset value constant. This value is the same as the one that the Player Stats system uses to indicate when it doesn't have sufficient data to compute a given endpoint.

The player stats API let you tailor game experiences to specific segments of
players and different stages of the player lifecycle. You can build tailored
experiences for each player segment based on how players are progressing, spending,
and engaging. For example, you can use this API to take proactive actions to
encourage a less active player to re-engage with your game, such as by
displaying and promoting new in-game items when the player authenticates.

The APIs can be found in the
[`com.google.android.gms.games.stats`](https://developers.google.com/android/reference/com/google/android/gms/games/stats/package-summary)
and [`com.google.android.gms.games`](https://developers.google.com/android/reference/com/google/android/gms/games/package-summary) packages.

## Before you begin

Before you start to use the player stats API:

- Download and review the [code sample](https://github.com/playgameservices/android-basic-samples).
- Familiarize yourself with the recommendations described in the [Quality Checklist](https://developer.android.com/games/pgs/quality).

## Get the player stats client

To start using the player stats API, your game must first obtain a
[`PlayerStatsClient`](https://developers.google.com/android/reference/com/google/android/gms/games/PlayerStatsClient) object. You can do this by calling the
[`PlayerStatsClient.getPlayersClient()`](https://developers.google.com/android/reference/com/google/android/gms/games/PlayGames#public-static-playerstatsclient-getplayerstatsclient-activity-activity)
method and passing in the activity.

The
[`PlayerStatsClient`](https://developers.google.com/android/reference/com/google/android/gms/games/PlayerStatsClient)
class makes use of the Google Play services
[`Task`](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task)
class to return results asynchronously. To learn more about
using tasks to manage threaded work, see the
[Tasks API developer guide](https://developers.google.com/android/guides/tasks).

## Player stats basics

You can use the player stats API to retrieve data about a player's in-game
activity. The types of player data you can retrieve include:

- **Average session length**: The average session length of the player in
  minutes. Session length is determined by the time that a player is authenticated
  by Google Play Games services.

- **Days since last played**: The approximate number of days since the player
  last played.

- **Number of purchases**: The approximate number of in-app purchases for the
  player.

- **Number of sessions**: The approximate number of sessions of the player.
  Sessions are determined by the number of times that a player authenticated by
  Google Play Games services.

- **Session percentile**: The approximation of sessions percentile for the
  player, given as a decimal value between 0 to 1 inclusive. This value indicates how many
  sessions the current player has played in comparison to the rest of this game's player
  base. Higher numbers indicate that this player has played more sessions.

- **Spend percentile**: The approximate spend percentile of the player, given
  as a decimal value between 0 to 1 inclusive. This value indicates how much
  the current player has spent in comparison to the rest of this game's player
  base. Higher numbers indicate that this player has spent more.

The following types of player data are deprecated and always return an unset
value constant:
- **Churn probability**: The prediction of whether a player will churn in the next day, given as a decimal value between 0 (low probability of churn) to 1 (high probability of churn) inclusive. Churn is defined as 7 days of inactivity.
- **Spend probability**: The approximate probability of the player choosing to spend in this game, given as a decimal value between 0 (low probability of spend) to 1 (high probability of spend) inclusive.
- **Total spend next 28 days**: The approximate total expected player spend over the next 28 days in this game.
- **High spender probability**: The approximate probability that over the next 28 days a player will spend an amount that is in the 95th percentile or higher of this game's player base. This is given as a decimal value between 0 (low probability of becoming a high spender) to 1 (high probability of become a high spender).

## Retrieve player stats data

To retrieve player stats data for the authenticated player, follow these
steps:

1. Call the
   [`PlayerStatsClient.loadPlayerStats()`](https://developers.google.com/android/reference/com/google/android/gms/games/PlayerStatsClient#loadPlayerStats)
   method.

2. If the call is successful, Google Play games services returns a
   [`Task`](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task)
   object which asynchronously loads a
   [`PlayerStats`](https://developers.google.com/android/reference/com/google/android/gms/games/stats/PlayerStats)
   object. Use the methods of this object to retrieve data about the authenticated
   player's activities in your app.

Here's an example:

```gdscript
public void checkPlayerStats() {
  PlayGames.getPlayerStatsClient(this)
      .loadPlayerStats(true)
      .addOnCompleteListener(new OnCompleteListener<AnnotatedData<PlayerStats>>() {
        @Override
        public void onComplete(@NonNull Task<AnnotatedData<PlayerStats>> task) {
          if (task.isSuccessful()) {
            // Check for cached data.
            if (task.getResult().isStale()) {
              Log.d(TAG, "using cached data");
            }
            PlayerStats stats = task.getResult().get();
            if (stats != null) {
              Log.d(TAG, "Player stats loaded");
              if (stats.getDaysSinceLastPlayed() > 7) {
                Log.d(TAG, "It's been longer than a week");
              }
              if (stats.getNumberOfSessions() > 1000) {
                Log.d(TAG, "Veteran player");
              }
              if (stats.getChurnProbability() == 1) {
                Log.d(TAG, "Player is at high risk of churn");
              }
            }
          } else {
            int status = CommonStatusCodes.DEVELOPER_ERROR;
            if (task.getException() instanceof ApiException) {
              status = ((ApiException) task.getException()).getStatusCode();
            }
            Log.d(TAG, "Failed to fetch Stats Data status: "
                + status + ": " + task.getException());
          }
        }
      });
}
```

## Tips for using player stats data

The Play Stats API lets you identify various types of players, based on
their engagement and spending behavior, and apply appropriate strategies to
enhance their game experience.

The following table lists some example player segments and recommended
engagement strategies:

| Player Segment | Engagement Strategy |
|---|---|
| Frequent players with a high number of sessions and good spend percentile, but have not played for the last week or more. | - Send a notification about a discount or special bonus available upon their return to play. - Show a welcome back message that acknowledges impressive accomplishments, and award a badge designed to encourage return play. |
| Highly engaged players in a low spend percentile. | - Tailor bonuses to incentivize them to invite their friends to install and join your game. This approach builds on the player's demonstrated enjoyment of the game to recruit new players. |
| High spending players showing signs of having peaked and starting to play less frequently. | - Tailor bonuses to freshen their interest, such as by offering high-value, short-duration tools, weapons, or discounts. - The next time the player authenticates, show a video that directs them to community features, like clan attacks, that drive more frequent and longer engagement. |
| Players with very high or very low spend probability. | - Unlikely to spend: Give the option to watch an advertisement video. Show lower-priced items for purchase. - Likely to spend: Direct them to the in-game store early, and provide special promotions to incentivize them to buy. |