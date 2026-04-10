---
title: https://developer.android.com/games/pgs/branding
url: https://developer.android.com/games/pgs/branding
source: md.txt
---

This page describes the design guidelines for Google Play Games Services branding elements.
You can use these elements in your app without pre-approval provided you follow
these guidelines. Use of Google brands in ways not expressly covered by these
guidelines is not allowed without prior written consent from Google. For more
information, see the
[Guidelines for Third Party Use of Google Brand Features](https://developers.google.com/identity/branding-guidelines).

## Games and Google Play branding

You are encouraged to create a great end-to-end experience
when integrating games services. It is also important to show to your players
how Google Play Games is used for the most intuitive experience.
This document describes the minimum requirements to use Google Play Games
branding in a game and to officially be recognized as supporting Google
Play Games.

## Guideline summary

To use Google Play Games branding elements in a game and to officially
support Google Play games services, your game must meet these requirements:

- **Minimum features**
  - Meet all required tasks in the [Google Play games services quality checklist](https://developer.android.com/games/pgs/quality).
- **Required iconography**
  - Provide a way to invoke Google Play Games default UI with user interface entry points for Achievements or Leaderboards. Developers are still encouraged to implement their own UI for these features. See the [FAQ](https://developer.android.com/games/pgs/branding#faq) for details.
  - Always use the Google Play game controller icon when labeling entry points. In instances where there are many entry points on one screen, use the guidelines below to best match your game's experience.
- **Game feature terminology**
  - When describing any game feature in-game, you may use the "Google Play", "Google Play Games" or "Play Games" brands nominatively to refer to those services. For reference usage, see the examples on this page.
- **What not to do**
  - Do not suppress or interrupt any pop-ups or overlays invoked by game services on Android.
  - Do not use "Google", "Google Play", "Google Play Games" or any other Google trademarks in your game title. You may use Google trademarks nominatively, as described in these branding guidelines, in your game description.
  - Do not use Google provided iconography, Google logos, or anything closely similar to those icons or logos in your game's icon.

<br />

## Game iconography

### General guidelines

- Do not obfuscate icons with other elements in your game.
- Icons should be easy to see and free from "busy" backgrounds.
- Ensure there's adequate space when using multiple icons, so they don't touch or overlap with other iconography.
- You are free to modify the color and texture of icons to match the style of your game. Make sure to follow the guidelines on [what not
  to do](https://developer.android.com/games/pgs/branding#icon-avoid).

### Applying the Google Play game controller icon

Use the Google Play game controller to represent the use of Google Play Games
services.

|---|---|---|
| ![Green game controller badge](https://developer.android.com/static/images/games/pgs/branding/ic_play_games_badge_green.png) | ![Gray game controller badge](https://developer.android.com/static/images/games/pgs/branding/ic_play_games_badge_gray.png) | ![White game controller badge](https://developer.android.com/static/images/games/pgs/branding/ic_play_games_badge_white.png) |

- Use the game controller icon in buttons or other user interface elements that launch default game service UI.
- Avoid using the controller icon repetitively on one screen. If a screen has multiple buttons or elements that would cause repetition, use the game controller icon once per area that visually groups together those elements.
- You may alter the color and texture of Google Play Games iconography to match your game's style. See the examples and guidelines below.

<br />

### Showcase implementations

You are encouraged to perform visual treatments on iconography
to match the style of their game. Since every game is unique, here are some
examples on how to apply Google Play Games icons to your user
interfaces.

**Example** The Google Play Games controller icon is
inset with other games services feature icons to visually tie these features
together. In this example, buttons for achievements and leaderboards are
shown on the same screen using Play Games iconography. When multiple feature
icons are shown, the Play Games controller is shown in a way that creates
affinity with the feature icons.
![example screenshot](https://developer.android.com/static/images/games/pgs/branding/branding-example3.png)

<br />

<br />

### Optional: Game feature icons

Optionally, the iconography below can be used when creating UI
elements that launch default UI for Google Play games services features. These
icons are not a replacement for the game controller icon requirement.

|---|---|---|---|
| Achievements | ![Green game achievements badge](https://developer.android.com/static/images/games/pgs/branding/ic_play_games_badge_achievements_green.png) | ![Gray game achievements badge](https://developer.android.com/static/images/games/pgs/branding/ic_play_games_badge_achievements_gray.png) | ![White game achievements badge](https://developer.android.com/static/images/games/pgs/branding/ic_play_games_badge_achievements_white.png) |
| Leaderboards | ![Green game leaderboards badge](https://developer.android.com/static/images/games/pgs/branding/ic_play_games_badge_leaderboards_green.png) | ![Gray game leaderboards badge](https://developer.android.com/static/images/games/pgs/branding/ic_play_games_badge_leaderboards_gray.png) | ![White game leaderboards badge](https://developer.android.com/static/images/games/pgs/branding/ic_play_games_badge_leaderboards_white.png) |
| Saved Games | ![Green saved games badge](https://developer.android.com/static/images/games/pgs/branding/ic_play_games_badge_savedgames_green.png) | ![Gray saved games badge](https://developer.android.com/static/images/games/pgs/branding/ic_play_games_badge_savedgames_gray.png) | ![White saved games badge](https://developer.android.com/static/images/games/pgs/branding/ic_play_games_badge_savedgames_white.png) |

### What not to do

- Do not obfuscate icons with other elements. For example:

  ![overlay controller icon with achievements icon](https://developer.android.com/static/images/games/pgs/branding/overlay_controller.png)
- Do not substantially modify icons. For example:

  ![distorted game controller icon](https://developer.android.com/static/images/games/pgs/branding/distort_controller.png)
- Show the icon on a busy background. For example:

  ![obfuscated game controller icon](https://developer.android.com/static/images/games/pgs/branding/busy_obfuscated.png)
- Do not use the Google provided iconography in your game's icon.

## Game feature terminology

When describing any game feature in-game, you may use
**"Google Play"** , **"Google Play Games"** , or
**"Play Games"** to nominatively refer to the use of Google Play
Games services. This applies to Achievements, Leaderboards, and
Saved Games.

Example usage:

- Google Play Games
- Google Play Leaderboards
- Achievements from Google Play Games
- Your game progress is being saved online with Google Play
- Finding players with Google Play

### What not to do

- Do not use "Google", "Google Play", "Google Play Games" or any other Google trademarks in your game title. You may use Google trademarks nominatively, as described in these branding guidelines, in your game description.

<br />

<br />

## FAQ

This section frequently asked questions about the branding guidelines.

### What methods invoke the default UI (Intents) for game features?

Android
:
    - Achievements UI: [`getAchievementsIntent()`](https://developers.google.com/android/reference/com/google/android/gms/games/AchievementsClient#public-abstract-taskintent-getachievementsintent)
    - Leaderboards UI: [`getLeaderboardIntent()`](https://developers.google.com/android/reference/com/google/android/gms/games/LeaderboardsClient#public-abstract-taskintent-getallleaderboardsintent)
    - Saved Games selection UI: [`Snapshots.getSelectSnapshotIntent()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient#public-abstract-taskintent-getselectsnapshotintent-string-title,-boolean-allowaddbutton,-boolean-allowdelete,-int-maxsnapshots)

### Which pop-ups should I ensure are shown in my game?

Android
:
    - Ensure the 'Welcome back' pop-up is shown after sign-in and never interrupted by other game or player activities.
    - Ensure the Achievement pop-up shows up when unlocking an achievement through unlockAchievement, increment or equivalent method.

### What are the Google Sign-In branding guidelines?

See
[Google Sign-In branding guidelines](https://developers.google.com/identity/branding-guidelines)
for details.

### When should I use Google Sign-In branding?

Follow Google Sign-In branding guidelines for sign-in scenarios only. For game features,
follow the iconography requirements and use the Google Play game controller.

### Can I change the look of the Google Play icons to better match my game?

In general, yes. Change the color, texture and size to suit your game.
Follow the general guidelines so that the icon is visible and recognizable.

### My game has multiple buttons to show achievements and leaderboards, does
the game controller icon need to be in each UI element?

No. In this case, use the controller once in a header or next to a
collection of buttons. This way the game controller is meant to show that a
set of buttons use Google Play games services.

### Do my game feature buttons need to use feature icons?

The only required icon is the Google Play game controller, displayed on a
UI element or the screen invoking Google Play Games features.

If you are displaying many buttons for Google Play games services, such as 5
different leaderboard buttons, the Google Play game feature icons for
achievements and leaderboards are available for your use. The
Google Play game controller must still be shown on the same screen

## Download files

You can download the image files for Play Games Services branding on the
[downloads](https://developer.android.com/games/pgs/downloads#graphics) page.