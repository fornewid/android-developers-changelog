---
title: https://developer.android.com/games/pgs/play-games-sidekick
url: https://developer.android.com/games/pgs/play-games-sidekick
source: md.txt
---

Play Games Sidekick is an overlay that helps players stay in your game by
delivering relevant content and offers directly to players.

- **User retention** with Gemini Live and tips, so players don't need to leave the game for help or advice.
- **Increased monetization** with in-the-moment Points exchange, Play-funded offers, and Pass coupons.
- **Rewarded gameplay** with integrated streaks, quests, and profile interactions.
- **Deeper engagement** with content and videos.

[![Play Games Sidekick with available features.](https://developer.android.com/static/images/games/pgs/Sidekick.gif)](https://developer.android.com/static/images/games/pgs/Sidekick.gif) Play Games Sidekick (click to enlarge).

## Features

Available features on Sidekick will vary by game, depending on
your Google Play Games Services integration status and Play Points enrollment. Players can
expect the following features:

- **Gaming utilities:** Screenshot, screen record, YouTube Livestream, and Do Not Disturb.
- **Achievements:** Requires implementation of [achievements](https://developer.android.com/games/pgs/achievements).
- **Gaming streaks:** [Gaming streaks](https://support.google.com/googleplay/answer/16562031).
- **Play Points credit exchange.**
- **Play Points boosters and coupons:** Available to enrolled Play Points developers.
- **Play Pass benefits and offers.**
- **Quests:** [Quests](https://support.google.com/googleplay/answer/11534416) are available to enrolled Quest developers.
- **Official and Creator Videos:** Sidekick shows the videos that you add. For more information about how to add videos on Play Store and Sidekick, see [Showcase your app with YouTube videos on
  Google Play](https://support.google.com/googleplay/android-developer/answer/15501235).

Some features are being tested with Early Access Partners:

- **Gemini Live:** Only available to Early Access Partners (EAP). If your game is not an EAP title, Gemini Live won't appear on your game. There will be a minimum of 3 months notice for any changes from this EAP program to move to the General Availability (GA) phase. Use our EAP program to test for performance in your test tracks.
- **Game Tips:** Available in select languages in an Early Access Program (EAP). If your game is not an EAP title, Game Tips won't appear on your game. There will be a minimum of 3 months notice for any changes from this EAP program to move to the General Availability (GA) phase. Use our EAP program to test for performance in your test tracks.

## Software and hardware requirements

To access Sidekick, players need the following:

- A mobile phone running Android 13 or higher.

  > [!NOTE]
  > **Note:** Sidekick is available to devices with 4 GB RAM or higher. Performance testing continues on to enable more devices. Minimum hardware specifications will be published in July 2026.

- Players must have one [Gamer profile](https://play.google.com/games/profile).

- The game must be installed from the Play Store.

## Try Sidekick

To enable Sidekick for your game, follow these steps:

### Make Sidekick default on for your game

Create an internal or closed testing release in Play Console to test pre-release
versions of your game with Sidekick and gather targeted feedback.

Once you've tested with a smaller group of colleagues or trusted users, you can
expand your test to an open release.

1. In the Play Console, [set up an internal or a closed testing](https://support.google.com/googleplay/android-developer/answer/9845334) release.
2. To add Play Games Sidekick to your app bundle, select **Sidekick is on by default**.
3. Conduct your testing.
4. Once ready, release the build to production. For more information, see [Prepare and roll out a release](https://support.google.com/googleplay/android-developer/answer/9859348).

Players can manage the visibility of Sidekick at any time through
the user settings in the Play Store.
[![Sidekick is on by default](https://developer.android.com/static/images/games/pgs/sidekickon.png)](https://developer.android.com/static/images/games/pgs/sidekickon.png) Add Play Games Sidekick to your game.

### Manage Sidekick visibility on your device for testing

Once the release is available to your testers in the Play Console, follow these
steps to enable Play Store developer options on the device:

1. Open Google Play Store app.
2. Tap your profile icon and then tap **Settings**.
3. Tap the **About** menu.
4. Tap the **Play Store version** 7 times until you see the message `You are
   now a developer!`. This enables developer options on your device.
5. Tap **General** and then tap **Developer options**.
6. Turn on **Play Games Sidekick**.
7. Go to your game to see Sidekick appear.

[![The toggle to turn on Play Games Sidekick on the Google Play
Store app.](https://developer.android.com/static/images/games/pgs/playstoresidekick.png)](https://developer.android.com/static/images/games/pgs/playstoresidekick.png) The toggle to turn on Play Games Sidekick on the Google Play Store app (click to enlarge).

## Automatically add Sidekick to all bundle uploads

When you create a release and make Sidekick default on for your game,
Sidekick is added to all of your future app bundles.

To change if Sidekick is on by default for all new app bundles
you upload, follow these steps:

1. Open [Play Console](https://play.google.com/console).
2. Select a game.
3. Go to **Testing** \> **Advanced settings**.
4. On the **Play Games Sidekick** tab, select either
   - Automatically make Sidekick is on by default for new app bundles you upload.
   - Don't automatically make Sidekick default on for new app bundles you upload.
5. Select **Save changes**.

If your app updates are infrequent, we may periodically update the
Sidekick for you. You can opt out of Sidekick
using the advanced settings in the Google Play Console at any time.

## Promote Sidekick to production

If you promote a release containing Sidekick to production,
players will see Sidekick. Players can manage the visibility
of Sidekick at any time through the user settings in the
Play Store app.

Games that promote a release with Sidekick satisfy the [Level Up
guidelines](https://play.google.com/console/about/levelup/#user-experience-guidelines).

## Give feedback

For any feedback on Sidekick, use the [feedback form](https://docs.google.com/forms/d/e/1FAIpQLScDNLDrD7a6ldsqnh5bafj-aID6rfIJsP4I4xt5dUSGo3_-1A/viewform).

## Frequently asked questions

#### Can you add Sidekick to your game using the Publishing API?

You can add Sidekick to your game even if you publish using
the [Google Play Developer Publishing API](https://developers.google.com/android-publisher#publishing).
First, [automatically
add Sidekick to all bundle uploads](https://developer.android.com/games/pgs/play-games-sidekick#add-sidekick),
and then continue your normal release process. Sidekick will be
added to your Android App Bundle.

#### My game does not use Android App Bundles (AAB), what should I do?

Sidekick is added to games when you upload a new
[Android App Bundle](https://developer.android.com/guide/app-bundle).

If you are using APKs, add the
[Sidekick SDK](https://developer.android.com/games/pgs/play-games-sidekick-sdk) as a dependency.

#### My game uses an anti-tampering product. Is Sidekick compatible with my solution?

We have been working with leading companies to ensure Sidekick
compatibility.

If you are using an incompatible anti-tampering product, add the
[Sidekick SDK](https://developer.android.com/games/pgs/play-games-sidekick-sdk) as a dependency to your
APK.
If you have other questions,
[request support](https://docs.google.com/forms/d/1NPmZ04tyT97tb8q-NbElU_HJ3YuPWOkXvhwJB3mTmB8/viewform).

#### Why are achievements not appearing in Sidekick?

If achievements aren't appearing as expected, check the following:

- **Draft status:** Achievements in "Draft" state aren't shown in the Sidekick.
- **Achievement badge:** Locked achievements are only visible to all players if the game has earned an achievements badge. This requires at least 100 unique players to have made calls to the achievements API within the last 30 days.
- **Unlocked:** If the game hasn't earned a badge, players see achievements they have already unlocked.