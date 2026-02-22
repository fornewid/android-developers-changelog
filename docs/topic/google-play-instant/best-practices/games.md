---
title: https://developer.android.com/topic/google-play-instant/best-practices/games
url: https://developer.android.com/topic/google-play-instant/best-practices/games
source: md.txt
---

**Warning:** Google Play Instant will no longer be available. Starting December 2025, Instant Apps cannot be published through Google Play, and all[Google Play services Instant APIs](https://developers.google.com/android/reference/com/google/android/gms/instantapps/package-summary)will no longer work. Users will no longer be served Instant Apps by Play using any mechanism.

We're making this change based on developer feedback and our continuous investments to improve the ecosystem since the introduction of Google Play Instant.

To continue optimizing for user growth, we encourage developers to refer users to their regular app or game, using[deeplinks](https://support.google.com/googleplay/android-developer/answer/12463044)to redirect them to specific journeys or features when relevant.

Games on Google Play Instant are a great way to remove friction for your players and increase your reach. This guide expands upon the[UX best practices for apps on Google Play Instant](https://developer.android.com/topic/google-play-instant/best-practices/apps)and presents best practices specific to games.

## Identify your target user experience

When designing your gaming experience using Google Play Instant, consider how you'd like players to interact with it.

You can make your entire game available without installation, which is a great way for players to enjoy your game with the least amount of friction. These types of full instant experience games are called Instant play and are[eligible for featuring on the homepage of the](https://developer.android.com/topic/google-play-instant/instant-play-games)[Google Play Games app](https://play.google.com/store/apps/details?id=com.google.android.play.games).

If you aren't able to make the entire game available, you can also create one of the types of trial experiences described in this section.

Be deliberate when building out your instant experience. In doing so, you'll increase your reach by providing value to your gamers.

### Preregistration

You can deploy a Google Play Instant experience as part of a preregistration campaign for an upcoming release. You can use this experience to help generate signups, perform A/B testing of features, and share teaser content to prospective players.

Players launch this experience from the Play Store details page, which is also where they preregister for the game.

### Introductory gameplay

This type of Google Play Instant experience is built around the first few levels of the game, or the game's tutorial, with minimal changes to the player's experience. When players install the game from the instant experience, you can transfer their current progression.

### Core gameplay

This type of Google Play Instant experience provides a preview of what players see*after*they complete the tutorial and introductory levels. This pattern is particularly effective when combined with the best practice of saving players' progress after they install the full game.

### New gameplay types or levels

Games can experience player abandonment as they mature. These players may have either finished the current game, exhausted all the current features, or dropped off for a variety of other reasons. Google Play Instant is a great way to re-engage these players by showing them what more they can experience with your game. These new experiences might include new levels or changed game mechanics.

### Minigame

The Google Play Instant experience complements the installed version of your game. This experience often contains different gameplay elements and might be more simplistic.

### Cross-promotion and ads

Several types of campaigns---including ad campaigns and cross-promotional ad campaigns---can launch players directly into the Google Play Instant experience instead of the static Google Play Store details page.

These experiences include the following:

- Ad campaigns.
- Cross-promotional ad campaigns: Advertising one of your games within one of your other games.
- Re-engagement ad campaigns: Ads that target churned players of your game.

## Polish the end-to-end experience

This section provides some suggestions for optimizing the end-to-end experience for players who interact with your game on Google Play Instant. You should make sure that your instant experience starts quickly from a variety of entry points, and if you have built a trial experience, you should encourage players to graduate out of the experience by installing a full version of your game.

### Give players several entry points

Players may find your game using any of the following methods:

- An ad
- The[Google Play Games app](https://play.google.com/store/apps/details?id=com.google.android.play.games)
- The**Try Now**button in the Play Store

Provide at least a few of these methods for bringing players into your game.

The screenshots in Figure 1 show examples of these game discovery methods:  
![](https://developer.android.com/static/topic/google-play-instant/best-practices/images/gpi-entry-point-1.png)  
![](https://developer.android.com/static/topic/google-play-instant/images/play-instant-games.png)  
![](https://developer.android.com/static/topic/google-play-instant/best-practices/images/gpi-entry-point-4.png)**Figure 1.**Several possible ways players might find your game (left to right, from top: ad campaign, Google Play Games app, Play Store)

### Start the experience quickly

![Device showing a game loading](https://developer.android.com/static/topic/google-play-instant/best-practices/images/gpi-game-loading.gif)**Figure 2.**Animation shown when a game loads on Google Play Instant

Games on Google Play Instant use an immersive, arcade-like animation as a loading screen to keep players engaged while the game loads, as shown in Figure 2:

If you must display an additional loading screen in the game, try to show it for as short a time period as possible.

### Keep the back button enabled

![](https://developer.android.com/static/topic/google-play-instant/best-practices/images/gpi-back-button-warning.png)**Figure 3.**Back button warning dialog (Bubble Witch 3 Saga)

Don't disable the Android back button at the bottom of the screen. Instead, show a warning when it's pressed to alert players they're about to exit the game, as shown in Figure 3. It's a good practice to not disrupt established navigational patterns.

### Provide an installation prompt

If you have built a trial experience, you should provide a way for players to install the full game. Note that this isn't required for[Instant play games that are featured in the Google Play Games app](https://developer.android.com/topic/google-play-instant/instant-play-games).

For trial Google Play Instant experiences, you would typically use an**Install**button. You can show this button in a variety of locations:

- On screen permanently.
- Between levels.
- As part of the main menu.

The screenshots in Figure 4 present examples of possible**Install** button locations. The screenshot in Figure 5 demonstrates the in-app installation experience that occurs after players tap a given**Install**button.  
![](https://developer.android.com/static/topic/google-play-instant/best-practices/images/gpi-install-invite-1.png)  
![](https://developer.android.com/static/topic/google-play-instant/best-practices/images/gpi-install-invite-2.png)**Figure 4.**Several possible ways of inviting players to install a game (Clash Royale, left; Bubble Witch 3 Saga, right)  
![](https://developer.android.com/static/topic/google-play-instant/best-practices/images/gpi-inline-app-install.png)**Figure 5.**Inline app installation experience (Panda Pop)

### Preserve user state after installation

Ensure players' progress and achievements are saved and available after installation. They should be able to continue playing where they left off when they decided to install.

## Make your game viral

Some of the best players are acquired organically through recommendations from existing players. Google Play Instant can bridge the installation gap between one friend recommending a game and another friend trying it out for the first time.