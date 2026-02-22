---
title: https://developer.android.com/games/pgs/play-games-sidekick
url: https://developer.android.com/games/pgs/play-games-sidekick
source: md.txt
---

Play Games Sidekick (beta) is an overlay that helps you stay in your game
by delivering relevant content and offers directly to you.

- **User retention** with Gemini Live and tips, so you don't need to leave the game for help or advice.
- **Increased monetization** with in-the-moment Points exchange, Play-funded offers, and Pass coupons.
- **Rewarded gameplay** with integrated streaks, quests, and profile interactions
- **Deeper engagement** with your content and videos

[![The Play Games Sidekick (beta) with available features.](https://developer.android.com/static/images/games/pgs/Sidekick.gif)](https://developer.android.com/static/images/games/pgs/Sidekick.gif) The Play Games Sidekick (beta) (click to enlarge).

## Features available for testing

Sidekick (beta) is ready for you to test. Available features
vary by game, depending on your Google Play Games Services integration status and Play Points
enrollment. Because Sidekick is in beta, some features are only available to
Early Access Partners (EAP). You can test the following features:

- **Gaming utilities:** Screenshot, screen record, YouTube Livestream, and Do Not Disturb.
- **Achievements:** Requires implementation of [achievements](https://developer.android.com/games/pgs/achievements).
- **Gaming streaks:** [Gaming streaks](https://support.google.com/googleplay/answer/16562031).
- **Play Points credit exchange.**
- **Play Points boosters and coupons:** Available to enrolled Play Points developers.
- **Quests:** [Quests](https://support.google.com/googleplay/answer/11534416) are available to enrolled Quest developers.
- **Game Tips:** Will be available in Q1 2026.
- **Gemini Live:** Available only to Sidekick EAP members.

More features will be available for testing in Q1 2026. To join the Early Access
Program (EAP), request access here: [Join the Early Access Program
(EAP)](http://goo.gle/sidekick-eap).

## Software and hardware requirements

To access the Sidekick (beta), you need the following:

- An Android mobile phone operating on Android 13 or higher.
- You must have one [Gamer profile](https://play.google.com/games/profile).
- The game must be installed from the Play Store.

## Try Sidekick (beta)

To enable Sidekick (beta) for your game, follow these steps.

### Add Sidekick to your game

Create an internal or closed testing release in Play Console to test pre-release
versions of your game with Sidekick and gather targeted feedback.

Once you've tested with a smaller group of colleagues or trusted users, you can
expand your test to an open release.

1. In the Play Console, [set up an internal or a closed testing](https://support.google.com/googleplay/android-developer/answer/9845334) release.
2. To add Play Games Sidekick (beta) to your app bundle, select **Add Play
   Games Sidekick to app bundles you upload** . For more information, see [Prepare and roll out a release](https://support.google.com/googleplay/android-developer/answer/9859348).

[![The Add Play Games Sidekick to app bundles you upload checkbox in the Play Console.](https://developer.android.com/static/images/games/pgs/closed_testing.png)](https://developer.android.com/static/images/games/pgs/closed_testing.png) The **Add Play Games Sidekick to app bundles you upload** checkbox (click to enlarge).

### Switch on Sidekick for your device

Once the release is available to your testers in the Play Console, follow these
steps to enable Play Store developer options on the device:

1. Open Google Play Store app.
2. Tap your profile icon and then tap **Settings**.
3. Tap the **About** menu.
4. Tap the **Play Store version** 7 times until you see the message `You
   are now a developer!`. This enables developer options on your device.
5. Tap **General** and then tap **Developer options**.
6. Turn on **Play Games Sidekick (beta)**.
7. Go to your game to see Sidekick appear.

[![The toggle to turn on Play Games Sidekick (beta) on the Google Play
Store app.](https://developer.android.com/static/images/games/pgs/playstoresidekick.png)](https://developer.android.com/static/images/games/pgs/playstoresidekick.png) The toggle to turn on Play Games Sidekick (beta) on the Google Play Store app (click to enlarge).

## Automatically add Sidekick to all bundle uploads

When you create a release, Sidekick (beta) isn't added to your app
bundles by default.

To automatically add Sidekick (beta) to the new app bundles you upload,
follow these steps:

1. Open [Play Console](https://play.google.com/console).
2. Select a game.
3. Go to **Testing** \> **Advanced settings**.
4. On the **Play Games Sidekick** tab, select **Automatically add Sidekick to
   new app bundles you upload**.
5. Select **Save changes**.

## Promote Sidekick to production

If you promote a release containing Sidekick (beta) to production, your
players won't yet see Sidekick. Players gain access to Sidekick only when the
product is Generally Available (GA) from Google, or if they manually enable it
from the **Developer options**.

Games that promote a release with Sidekick satisfy the [Level Up
guidelines](https://play.google.com/console/about/levelup/#user-experience-guidelines).

## Give feedback

For any feedback on the Sidekick, use the [feedback
form](https://docs.google.com/forms/d/e/1FAIpQLScDNLDrD7a6ldsqnh5bafj-aID6rfIJsP4I4xt5dUSGo3_-1A/viewform).

## Frequently asked questions

#### My game does not use Android App Bundles (AAB), what should I do?

Sidekick (beta) is added to games when you upload a new
[Android App Bundle](https://developer.android.com/guide/app-bundle).
If you are uploading APKs and cannot enable AAB,
[request support](https://docs.google.com/forms/d/1NPmZ04tyT97tb8q-NbElU_HJ3YuPWOkXvhwJB3mTmB8/viewform).

#### My game uses an anti-tampering product. Is Sidekick compatible with my solution?

We have been working with leading companies to ensure Sidekick (beta)
compatibility.
Integrating Sidekick introduces new native libraries that can create issues with
anti-tampering features. While we've collaborated with security providers,
thorough testing is essential, and we recommend working with your solution
provider. If you have other questions,
[request support](https://docs.google.com/forms/d/1NPmZ04tyT97tb8q-NbElU_HJ3YuPWOkXvhwJB3mTmB8/viewform).