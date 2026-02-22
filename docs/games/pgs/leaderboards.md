---
title: https://developer.android.com/games/pgs/leaderboards
url: https://developer.android.com/games/pgs/leaderboards
source: md.txt
---

Leaderboards can be a fun way to drive competition among your players, both for
your most hardcore fans (who will be fighting for the top spot in a public
leaderboard) and for your more casual players (who will be interested in
comparing their progress to their friends').

To learn how to implement leaderboards for your platform, see [Client
implementations](https://developer.android.com/games/pgs/leaderboards#client-implementations).

## Understand leaderboards

When you create a leaderboard, Play Games Services will take care of managing
most aspects of this leaderboard for you. The typical process works like this:

1. At the end of a game (or at an appropriate moment that you've determined), the game submits the player's score to one or more leaderboards you've created for the game.
2. Play Games Services checks if this score is better than the player's current leaderboard entry for the daily, weekly, or all-time score. If it is, Play Games Services updates the corresponding leaderboards with the new score.
3. Play Games Services sends a score report back to the game client. This report tells the client whether this is a new daily, weekly, or all-time high score. If it isn't, Play Games Services will tell the client what the current daily, weekly, or all-time high score is for this player.
4. To retrieve a player's results for a leaderboard, you can request a timeframe (daily, weekly, or all-time), and specify whether or not the user wants to see a social or public leaderboard. Play Games Services performs all the necessary filtering, and then sends the results back to the client.
5. In cases where there are a lot of scores to report, Play Games Services sends back only the data for the top leaderboard scores. You can also retrieve raw score data for the top scores or the scores adjacent to the player's.

### Multiple leaderboards

Games can have multiple leaderboards, up to a maximum of 70. For example, a
multi-level game might provide a different leaderboard for each level, and a
racing game might have a separate leaderboard for each track.

### Leaderboard timeframes

The Play Games SDK automatically creates daily, weekly, and all-time
versions of every leaderboard that you create. There's no need for you to create
separate leaderboards for each timeframe.

Daily leaderboards reset at UTC-7 (that is, "midnight Pacific Daylight Time")
all year long.

Weekly leaderboards reset at midnight between Saturday and Sunday, in the same
timezone as daily leaderboards (UTC-7).

### Public and social leaderboards

The Play Games SDK can display two different versions of each
leaderboard to the player:

The **social** leaderboard is a leaderboard made up of people in the user's
circles (or, more accurately, members of the circles that the user has chosen to
share with your application) who have decided to share their gameplay activity
to the user.

The **public** leaderboard is a leaderboard made up of players who have chosen
to share their gameplay activity publicly. If your player has not chosen to
share their gameplay activity publicly, they won't appear in this leaderboard.
| **Note:** Social leaderboards will initially be empty until you publish the corresponding leaderboard by using Google Play Console. To learn how to publish your leaderboard, see [Publishing your game
| changes](https://developer.android.com/games/pgs/console/publish#publish_game_changes).

### Display leaderboards

In the mobile client libraries, the libraries take care of all the formatting
and displaying of leaderboards. You can specify whether a player can see a
specific leaderboard, or see a list of all of your leaderboards that they can
choose from.

You can also implement your own versions of the leaderboards by accessing the
data directly from the client libraries.
| **Warning:** Player names that you retrieve directly using the client libraries may contain Unicode characters (for example, if the name has non-English characters). If you are implementing your own version of a leaderboard UI that uses decorative fonts, make sure that your UI can display these names correctly.

## Attributes

To create and manage leaderboards, you'll want to be familiar with these
leaderboard attributes:

### The basics

These basic elements are associated with every leaderboard:

- **ID** is a unique string that Google Play Console will generate for you. You'll use this unique ID to refer to the leaderboard in your game clients.
- **Name** is a short name of the leaderboard (for example, "High Scores" or "Level 3"). This can be up to 100 characters.
- **Icon** is a square icon that will be associated with your leaderboard. For best practices when creating your leaderboard icons, see [Icon
  Guidelines](https://developer.android.com/games/pgs/leaderboards#icon-guidelines).
- **List order** is the order in which the leaderboard will appear when a player views the leaderboards associated with your game.
- **Limits** are optional values that define the lower and upper limits of scores that are allowed in the leaderboard. This can help you discard score submissions that are clearly fraudulent. You can also use [`Players.hide`](https://developer.android.com/games/services/management/api/players/hide) to hide players that you believe have submitted fraudulent scores from all leaderboards in your app.

### Order leaderboards

Leaderboards can have one of two ordering types:

- **Larger is better** leaderboards are the default. This is typically what you would see in most games where players earn points.
- **Smaller is better** leaderboards are occasionally used in cases where a smaller score would be better. The most common examples of this type of leaderboard are in racing games, where the score represents the player's time to finish the race.

| **Note:** Once a leaderboard is published, its ordering type ('Larger is better' or 'Smaller is better') is fixed and cannot be changed. You can still change a leaderboard's list order after it is published.

## Score formatting

While all scores are submitted to leaderboards and stored internally as long
integers, Play Games Services can present them to the user in a number of
different formats:

- **Numeric** leaderboards present scores as numbers. These can be displayed
  as integers or as real numbers with a fixed number of decimal places. You
  submit the score as integers and the decimal point is inserted in the
  specified location. A score of `314159`, for example, would be displayed as
  `3.14159`, `3141.59`, or `314159`, depending on the decimal place you
  specified.

- **Time** leaderboards present scores in hours / minutes / seconds /
  hundredths of a second format. You must submit scores as milliseconds, so
  `66032` would be interpreted as `1:06.03`.

- **Currency** leaderboards present scores in a currency format. You submit
  scores as 1/1,000,000th of the main currency unit. For example, a score of
  19,950,000 would be interpreted as `$19.95`, assuming you specified your
  currency as USD.

Numeric leaderboards also support custom units. For instance, if your game
measures high scores in meters, you can specify "meters" as the default unit for
your leaderboard.

### Translations and score formatting

When the mobile client libraries request leaderboard data from
Play Games Services, they specify a language and locale in which to display these
scores. The [REST
API](https://developer.android.com/games/services/web/api/rest/v1/scores/list) lets you
to specify a locale-based language as well. Play Games Services returns
formatted leaderboard scores appropriate for that language and locale. These
formatted scores will appear whether or not you have added
[translations](https://developer.android.com/games/pgs/console/enable-features#add_translations) for your
leaderboard.

For **Numeric** leaderboards, the number format is displayed differently per
language. (For example, `12,345.78` in the US, and `12 345,78` in France.) If
you are using custom units and have added
[translations](https://developer.android.com/games/pgs/console/enable-features#add_translations) to your
game, you must supply translated units for every language you have added. The
service then displays these translated units where appropriate.

Depending on the language you choose, you might need to supply different
versions of the names of your units. In English you'll need a version for one
item, and another for everything else (for instance, "meter" and "meters"). In
Polish, on the other hand, you would need to provide a version for one unit, a
few units, many units, and everything else. To learn more about plural rules,
see [Quantity
Strings(Plurals)](http://developer.android.com/guide/topics/resources/string-resource.html#Plurals).

For **Time** leaderboards, the time format is displayed according to the
player's language and locale. This will mainly be noticeable if you are using
fractions of a second or have an hours value with more than 3 digits (for
example, `4,815:16:23.42` in the US and `4.815:16:23,42` in Germany).

For **Currency** leaderboards, the currency format will be displayed according
to the player's language and locale. However, you cannot change the unit of
currency. For example, if you specify your currency in USD, the game will
display `$19.95` in the US and `19,95 $` in France. But you cannot specify that
your game shows dollars in the US and Euros in France.

## Icon guidelines

Icons should be created as 512 x 512 PNG or JPEG files. Your icons will be
scaled down in most game clients, so you should avoid creating icons with too
much fine detail. You can submit icons with an alpha channel, and the
transparency will be retained. The leaderboard icon will be shown against a
darker gray background on Android devices, so choose an icon that can work well
in this situation.

The same icon is used in all locales, so we recommend against including any text
or localized content in an icon.

## Create a leaderboard

This section tells you how to create leaderboards for new or existing games.

### Create a leaderboard for a new game

To create a leaderboard for a new and unpublished game, go to
Google Play Console entry for your game, and navigate to **Grow users \> Play Games
Services \> Setup and management \> Leaderboards** , then click the
**Create leaderboard** button.
![The 'Add Leaderboard' button on the main Leaderboards Panel](https://developer.android.com/static/images/games/pgs/leaderboardAddNew.png) The 'Add Leaderboard' button on the main Leaderboards Panel

Then, simply fill out the information required for this leaderboard.
![A filled-out form for the 'Best round' leaderboard.](https://developer.android.com/static/images/games/pgs/leaderboardSampleForm.png) A filled-out form for the 'Best round' leaderboard.

Click **Save as draft**, and your leaderboard will be available in the "Draft"
state. Once you publish your game, all of your game's leaderboards are published
with it.

### Create a leaderboard for a published game

To create an additional leaderboard for a game that has already been published,
follow the same steps as above. For more information on testing an updated
version of a game, see [Publishing Your Game
Changes](https://developer.android.com/games/pgs/console/publish#publish_game_changes).

Once you've tested your leaderboard and are happy with it, you can republish
your game with the new leaderboards, and they will be pushed out to the world.

## Edit a leaderboard

To edit a leaderboard that you've already created, click the leaderboard in the
**Leaderboards** tab of Google Play Console. At this point, you will see the
same form you used when first creating the leaderboard, and you will be able to
edit any of the fields as you need.

When you're done editing a leaderboard, click the **Save as draft** button. The
newly edited leaderboard will be in the "Draft" state, which lets you to test it
out.

If it's working correctly, select **Publish the changes** from the box at the
top of the leaderboard form, and you'll be able to republish your game, along
with all your updated leaderboards, to the public.

### Undo an edit

If you decide you don't like your newly-edited leaderboard and want to go back
to the previous iteration, simply select **Revert** from the box at the top of
the Leaderboard form. Your leaderboard reverts back to the already published
version.

### Delete a leaderboard

You can delete leaderboards that are in the "Draft" state or that have been
published. To delete a leaderboard in Google Play Console, go to the form
for the leaderboard, and click **Delete leaderboard** at the top of the form.

Alternatively, you can call [`Players.hide`](https://developer.android.com/games/services/management/api/players/hide) to
hide a player's leaderboard in the app.

### Reset a leaderboard

You can only reset player progress data for your draft leaderboards.

- To reset leaderboards in Google Play Console, click **Reset progress** at the top of the form for that event.
- To reset leaderboard data programmatically, call the [Management API
  `Scores`methods](https://developer.android.com/games/services/management/api/scores).

## Add translations for leaderboards

You can specify your own translations for leaderboards that are associated with
your game. Before you do so, first make sure to complete the steps described in
[Adding translations for your
game](https://developer.android.com/games/pgs/console/enable-features#add_translations). You must also have
created one or more leaderboards for your game.

To add your own translations for leaderboards, open the **Leaderboards** tab for
your game in Google Play Console, then select an existing leaderboard. On
the leaderboard details page, click the tab for a language that you previously
added in the **Game details** tab. In the leaderboard details page for that
language, edit the form with your translations for that leaderboard. Click
**Save** to store your translated leaderboard details.

## Hide leaderboard scores

Google Play Games Services provides a leaderboard tamper protection feature that checks for
suspected tampered scores and hides them automatically. This feature is
available for Android games only.

Tamper protection is enabled by default for new leaderboards that you create for
your Android game, but is disabled for existing leaderboards. To enable tamper
protection for your existing leaderboards that are already published, follow
these steps:

1. In Google Play Console, open the **Games services** tab, then select your game from the list.
2. Open the **Leaderboards** tab, then select the leaderboard instance for which you want to enable tamper protection.
3. Turn the **Enable leaderboard tamper protection** option to ON.
4. Click **Save** and continue.
5. Publish your game.

Once tamper protection is enabled for a leaderboard in Google Play Console,
it may take up to 24 hours before this feature takes effect. Scores submitted
before you enabled tamper protection are not retroactively hidden.

In some situations, you may want to disable tamper protection (for example, if
your game also runs on the web in addition to Android, and shares leaderboards
across these platforms).

## Client implementations

To learn how to implement leaderboards for your platform, see the following
resources:

- [Android](https://developer.android.com/games/pgs/android/leaderboards)
- [Web](https://developer.android.com/games/services/web/api/rest/v1/leaderboards)
- [C++ API](https://developer.android.com/games/pgs/cpp/cpp-start)
- [Best practices for implementing leaderboards](https://developer.android.com/games/pgs/quality#leaderboards)