---
title: Player statistics in Unity games  |  Android game development  |  Android Developers
url: https://developer.android.com/games/pgs/unity/stats
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Games dev center](https://developer.android.com/games)
* [Guides](https://developer.android.com/games/guides)

Send feedback

# Player statistics in Unity games Stay organized with collections Save and categorize content based on your preferences.



The Player Stats API let you tailor game experiences to specific segments
of players and different stages of the player lifecycle. You can build
tailored experiences for each player segment based on how players are
progressing, spending, and engaging. For example, you can use this API to
take proactive actions to encourage a less active player to re-engage with
your game, such as by displaying and promoting new in-game items when the
player signs in.

The callback takes two parameters:

1. The result code. A value of 0 or less indicates success. See [`CommonStatusCodes`](/games/services/unity/v2/api/namespace/google-play-games/basic-api#commonstatuscodes) for all values.
2. The [`PlayerStats`](/games/services/unity/v2/api/class/google-play-games/basic-api/player-stats) object from the [`PlayGamesLocalUser.GetStats`](/games/services/unity/v2/api/class/google-play-games/play-games-local-user#getstats) method.

The player stats are available after authenticating:

```
    ((PlayGamesLocalUser)Social.localUser).GetStats((rc, stats) =>
        {
            // -1 means cached stats, 0 is success
            // see  CommonStatusCodes for all values.
            if (rc <= 0 && stats.HasDaysSinceLastPlayed()) {
                Debug.Log("It has been " + stats.DaysSinceLastPlayed + " days");
            }
        });
```




Send feedback