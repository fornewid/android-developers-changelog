---
title: https://developer.android.com/games/pgs/quality
url: https://developer.android.com/games/pgs/quality
source: md.txt
---

| **Note:** This guide is for the Play Games Services v2 SDK. For information on the previous SDK, see the [Play Games Services v1 documentation](https://developers.google.com/games/services/v1/checklist).

The quality of your game influences the long-term success of your game -- in
terms of installs, player rating and reviews, engagement and player retention.
Before publishing your game, it's important to make sure that your game meets
the basic expectations of game players through compelling features and an
intuitive, well-designed UI.

This document guides you through key aspects of game development that
significantly impact your game's success. It focuses on quality, feature set,
and user interface (UI).

For each focus area, this document provides:

- Checklists detailing minimum requirements.
- Best practices to enhance your game.

Follow these recommendations to the greatest extent possible to publish a
high-quality game and deliver the best possible product to your players.
| **Note:** To help prioritize your development efforts, take note of the level of importance indicated for each checklist item.
|
| - **Required**. Minimum requirements that must be implemented for your game to be considered Google Play Games Services-compatible.
| - **Best practices**. Strongly recommended implementation guidelines.

## 1. Platform authentication

The following checklist tasks apply to implementing player authentication
functionality in your game. Learn more about how authentication works and how
you should implement it in [Platform authentication](https://developer.android.com/games/pgs/signin). For code examples
of how to implement authentication on mobile games, see [Platform authentication on Android](https://developer.android.com/games/pgs/android/android-signin).

| ID | Importance | Description |
|---|---|---|
| 1.1 | Required | **Authenticate players with Google Play Games Services.** 1.1.1. Initialize the Google Play Games Services SDK and check if the player is authenticated. If the player is not automatically authenticated then provide a manual sign-in option. :   Automatic authentication will get players quickly authenticated and authorized to use the full set of features provided by the Google Play Games Services. If the user declines, your game should offer the opportunity for them to authenticate later (e.g. with a button in the game menu, etc.). The sign-in button should be easy for players to find; for example, it should be accessible from your main screen or located in the Settings screen. This button shouldn't be buried multiple levels deep in your game menu. |
| 1.2 | Best practices | **Follow Google branding guidelines.** To provide players with an end-to-end experience that is attractive and consistent, implement the [Google Play Games Services branding guidelines](https://developer.android.com/games/pgs/branding). |
| 1.3 | Best practices | **Remind players that they are authenticated.** Give authenticated players an appropriate reminder or cue when your game performs some action on their behalf. For example, when a authenticated player finishes a level, you can provide a message like this to indicate that the player's score and achievements are being automatically uploaded: *"You are authenticated with Google. Your achievements and scores will be saved automatically."* |
| 1.4 | Required | **Back up player progress using the Play Games Services ID.** To ensure players do not lose their progress when switching or resetting devices, or if they play on multiple devices, ensure their progress is backed up to a Cloud Save solution, and use the Play Games Services ID as a key, [securely](https://developer.android.com/games/pgs/signin#secure-access) if using your own backend game server. When players authenticate with their Play Games Services ID, check whether progress exists for that account and if it does, allow the player to pick up where they left off. You can use your own cloud save solution or Play Games Services saved games. If the user is not authenticated, try to maintain the player's progress locally, then sync that progress when the player eventually authenticates. This helps to prevent losing any of the player's progress if the player postpones to authenticate your game. |

## 2. Achievements

The following checklist tasks apply to implementing the
[Achievements](https://developer.android.com/games/pgs/achievements) feature in your game.

| ID | Importance | Description |
|---|---|---|
| 2.1 | Required | **Minimum of ten visible achievements spread across the lifetime of the game.** At least 10 visible achievements must be in a revealed state. |
| 2.2 | Required | **At least four achievements should be reasonably and reliably achievable within an hour of gameplay by everyone who plays.** <br /> |
| 2.3 | Required | **All achievements should have unique names and descriptions. These should make clear to users what they need to do to get the achievement.** <br /> |
| 2.4 | Required | **All achievements should have unique icons.** Icons should be created as 512 x 512 PNG, JPEG, or JPG files on transparent background. For more information, see the [icon guidelines](https://developer.android.com/games/pgs/integrate-achievements#icon-guidelines). |
| 2.5 | Required | **Ensure that all achievements are attainable.** Players must be able to unlock all achievements you create. |
| 2.6 | Best practice | **Use [incremental achievements](https://developer.android.com/games/pgs/achievements#incremental-achievements) to show progress.** Incremental achievements are cumulative across game sessions. ![A sample incremental achievement showing the player's progress at 23%.](https://developer.android.com/static/images/games/pgs/achievementIncremental.png) Incremental achievement showing the player's progress at 23%. |
| 2.7 | Best practice | **At least forty or more achievements spread across the lifetime of the game including ones that surprise and delight, recognise milestones, and capture player progress.** At least forty achievements in any state spread across the lifetime of the game. |
| 2.9 | Best practice | **Use [hidden achievements](https://developer.android.com/games/pgs/achievements#incremental-achievements) for element of surprise and delight.** Hidden achievements means that details about the achievement are hidden from the player. |
| 2.10 | Best practice | **Add new achievements when new levels or episodes are added to the game.** For more information, see [Points and experience](https://developer.android.com/games/pgs/achievements#points-experience). |
| 2.11 | Best practice | **Score achievements proportionately.** Achievement points should be proportional to the amount of time or skill required to earn that achievement. |
| 2.12 | Best practice | **Design achievements for a variety of difficulty levels.** Include some easy achievements that a player could earn through casual gameplay, a number of intermediate difficulty achievements that require more skill or player dedication to earn, and one or two very difficult achievements for the most dedicated players. For example, the following screenshot shows a hard-to-earn achievement that helps to motivate and retain fans of the title. ![hard to earn achievement that requires earning 5K gems](https://developer.android.com/static/images/games/pgs/achievement-difficulty-example.png) Hard to earn achievement that requires earning 5K gems. |
| 2.13 | Best practice | **Don't frontload achievements.** Avoid awarding more than one achievement in the first 5 minutes of gameplay, since players who are new to your game won't be deeply invested enough to care. Don't define your achievements such that they are unintentionally granted too early in gameplay. For example, watch out for achievements that are likely to be trivially earned at the start of the game, like *"Complete a level without taking damage"*. |
| 2.14 | Best practice | **Define achievements around compelling in-game activities.** Select metrics to build achievements that make your game more compelling and replayable (for example, *"number of zombies killed"* is a more interesting metric than *"number of miles your character walked"*). |
| 2.15 | Best practice | **Use color achievement icons.** Play Games Services uses grayscale versions of achievement icons to show if they're earned or unearned. If you are restricted to using all black (or all white) achievement icons, display them on a colored background. |
| 2.16 | Best practice | **Minimize the use of hidden achievements.** Hidden achievements should only be used to avoid in-game spoilers; they shouldn't be the norm. |
| 2.17 | Best practice | **Avoid achievements that are too reliant on chance.** *"Find 100 treasure chests"* is a better achievement than *"Find an item that has a 1% chance of appearing in a treasure chest."* |
| 2.18 | Best practice | **Think like an \`Achievement Hunter\`.** Some players will attempt to earn every achievement you create. Try to provide achievements that cater to this category of players. Avoid creating achievements that rely too much on elements beyond the player's control or cannot be earned once the player has made a decision in the game. |

### Examples

A few examples to help you design high quality achievements:

#### Good example

The following screenshot shows good examples of achievements. Achievements with
unique *names* , *icons* , and *descriptions*. The descriptions inform
what you need to do to get the achievement.
[![Good achievements with unique names, icons, and descriptions.](https://developer.android.com/static/images/games/pgs/Goodachievements.png)](https://developer.android.com/static/images/games/pgs/Goodachievements.png) Good achievements with unique names, icons, and descriptions (click to enlarge).

#### Bad example

The following screenshot shows bad examples of achievements.
[![Bad achievements with duplicate names, icons, and descriptions.](https://developer.android.com/static/images/games/pgs/Badachievements.png)](https://developer.android.com/static/images/games/pgs/Badachievements.png) Bad achievements with duplicate names, icons, and descriptions (click to enlarge).

## 3. Leaderboards

The following checklist tasks apply to implementing the [Leaderboards](https://developer.android.com/games/pgs/leaderboards) feature in your game.

| ID | Importance | Description |
|---|---|---|
| 3.1 | Best practice | **Make leaderboards visible in your main menu and after key transitions.** Leaderboards should be readily accessible on the loading of a game. After critical transitions in a game (for example, at the end of a level, or when the player dies), players should immediately see links to the relevant leaderboards. |
| 3.2 | Best practice | **Define upper limits for scores that can be submitted.** If possible, add limits when defining your leaderboards so that obviously fake scores are discarded. |
| 3.3 | Best practice | **Use custom icons.** Create a custom icon for each leaderboard you define; don't just use your game's icon, as it will display poorly in the Google Play Games app. |
| 3.4 | Best practice | **Keep the frequency of score submissions appropriate.** Submit scores after critical transitions in the game, such as at the end of a level or when a player's game character dies. For games without critical transitions (for example, an "endless runner" type game), use good judgment on how frequently to submit scores. Scores should not be submitted continuously or every second. |
| 3.5 | Best practices | **Make use of scoretags.** Scoretags are extra bits of data that can be sent with your score submission. For instance, you can implement a scoretag as a flag to confirm that a player's submitted score is valid. Custom leaderboards can also read this tag data. If the scoretag consisted of an ID for a YouTube video containing that player's gameplay, for instance, your game could create a link to view that video within your leaderboard. |
| 3.6 | Best practices | **Creatively design your own leaderboard UI** If you have the resources, build your own custom leaderboard view on top of the social leaderboard data. Social leaderboards typically create a more engaging experience than public leaderboards. Check first to determine if there are any entries in the social leaderboard. If not, use the public leaderboard instead. |
| 3.7 | Best practices | **Show players how they stack up against the competition.** The leaderboards API supports showing score windows (for example, a player's rank within +/-10 spots). If you are creating a custom view, this can be a powerful way to motivate engagement. This could be shown right after a critical transition in the game (for example, at the end of a level or when a player's game character dies). Avoid putting unnecessary clicks between your players and their ranking information. |

## 4. Friends

The following checklist tasks apply to implementing the
[Friends service](https://developer.android.com/games/pgs/friends) in your game.

| ID | Importance | Description |
|---|---|---|
| 4.1 | Required | **When players are displayed in a list, show the Play Games Services icon next to users who have a Play Games profile.** This list could be an existing friends list, a recently-played friends list, or other list of friends. 4.1.1. The Play Games Services icon must be clickable. : If the user presses the icon, the game should call [`getCompareProfileIntent()`](https://developers.google.com/android/reference/com/google/android/gms/games/PlayersClient.html#getCompareProfileIntent(com.google.android.gms.games.Player)) or [`getCompareProfileIntentWithAlternativeNameHints()`](https://developers.google.com/android/reference/com/google/android/gms/games/PlayersClient#public-abstract-taskintent-getcompareprofileintentwithalternativenamehints-string-otherplayerid,-string-otherplayeringamename,-string-currentplayeringamename) to show the UI where the user can compare themselves against another player's profile. 4.1.2. Player profiles and friend invitations support, for customizable in-game player names. :   If a player sets a different name within the game (and doesn't use their Play Games profile name), use [`getCompareProfileIntentWithAlternativeNameHints()`](https://developers.google.com/android/reference/com/google/android/gms/games/PlayersClient#public-abstract-taskintent-getcompareprofileintentwithalternativenamehints-string-otherplayerid,-string-otherplayeringamename,-string-currentplayeringamename) to provide that alternative in-game name for both the current player and the player they're viewing, as context for the profile view and any friend invitation sent from it. Pass only persistent, global player names for the values and not arbitrary user content. This requirement means that friend invitations sent from within the game will provide context to both players: - The recipient will see the in-game name of the invitation sender, along with the game name. - When viewing the friendship, the sender will still see the in-game name of the recipient, as well as the game they initiated it from. |
| 4.2 | Best practice | Use different icons to show which Play Games users are already friends, and which are not yet Play Games friends but have authenticated with Play Games. Use two icons for Play Games users, one for "Friends" and one for "Not friends" (or when the friendship status is unknown). ![](https://developer.android.com/static/games/pgs/download-files/signed-in-friend.png) Friends icon ![](https://developer.android.com/static/games/pgs/download-files/not-yet-friends.svg) Not Friends icon |
| 4.3 | Best practice | Call [`loadFriends()`](https://developers.google.com/android/reference/com/google/android/gms/games/PlayersClient#loadFriends(int,%20boolean)) every time you authenticate and display the list of friends to ensure the friends list is up-to-date. Make sure players see the updated list. |
| 4.4 | Best practice | If your game already contains in-game friends, use the Friends service to increase the list of friends by adding the Play Games friends. If a player is in the in-game friends list and they are also a Play Games friend, show the icon for "Friends". |
| 4.5 | Best practice | If a player has denied the request to access their friends list, don't show the dialog asking for access again unless the user has taken an action to indicate they want to give access (for example, pressing an \*\*Import Play Games Friends\*\* button). |
| 4.6 | Best practice | If a player has denied access to the friends list, give them a way to grant friends list access in the future (for example, after pressing an \*\*Import Play Games Friends\*\* button). |
| 4.7 | Best practice | If you use the player ID or friends list with a backend server, you must access the ID or list [securely](https://developer.android.com/games/pgs/signin#secure-access). In addition, for some older games and players, the player ID returned by the *Android* SDK for a player may not be the same ID that other players see when viewing that player in the same game; this is particularly relevant when using the friends list. However, the `player_id` returned within the REST API is always consistent and is always the ID that is visible to other players. |

## 5. Quota and rate limiting

The following checklist tasks apply to managing the quota and rate limiting in
your game. To learn how to manage your game's quota and detect when its rate
limit is exceeded, see [Managing Quota and Rate Limiting](https://developer.android.com/games/pgs/quota).

| ID | Importance | Description |
|---|---|---|
| 5.1 | Best practice | **Use the client libraries.** The mobile client libraries employ a number of strategies to reduce the calls you make to the service. For instance, data for achievements and leaderboards is cached, so players can view their achievements as often as they like without requiring the service to make multiple calls. The Android client library will not to send a player's score to the server if your score isn't as good as one you recently submitted. The Android library also automatically combines frequent achievement increment calls when it detects that you are being rate limited. |
| 5.2 | Best practices | **Combine frequent calls to incremental achievements.** If you're making a fighting game and you have a 'Throw 5000 punches' achievement, don't send an achievement increment call every time somebody throws a punch. Wait until the end of the round, and then send one `increment(xxx)` call (where xxx is the total number of punches thrown that round), or wait until 50 punches are thrown before sending a single `increment(50)` call. |
| 5.3 | Best practices | **Be aware of your usage.** Be conscious of the number of calls you make to Google Play Games Services. Even if you avoid hitting rate limits, frequent calls can lead to high network traffic, and cause the device's battery to drain more rapidly. To avoid this, you can use these techniques: - When performing saved games, keep the frequency to once every few minutes, not on every button click. - Wait until the player's game is over before submitting a high score. - Review your app's daily quota by going to your project dashboard in the Google Cloud Platform. |

## 6. Saved games

The following checklist tasks apply to implementing the
[Saved Games](https://developer.android.com/games/pgs/savedgames) feature in your game.

| ID | Importance | Description |
|---|---|---|
| 6.1 | Required | **Add metadata to provide additional context for saved games.** At minimum, you must include the following metadata when committing a saved game: - Cover image - A screenshot that captures game progress and reminds players of where they left the game. - Description - Short description that provides additional context for the cover image. - Time stamp - Indicates how long the player has been playing this saved game. |
| 6.2 | Required | **Allow players to load saved games.** Load the correct saved game when players make a selection from either the [Play Games app](https://play.google.com/store/apps/details?id=com.google.android.play.games) or the default Saved Games selection UI. |