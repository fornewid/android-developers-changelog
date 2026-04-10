---
title: https://developer.android.com/games/pgs/console/enable-features
url: https://developer.android.com/games/pgs/console/enable-features
source: md.txt
---

This page describes how to enable Google Play Games Services features for your
game in Google Play Console.

## Before you begin

- [Set up Play Games Services](https://developer.android.com/games/pgs/console/setup).

- Integrate Play Games Services [platform authentication]() in your game project.

  - For Java games, see
    [Platform authentication for Android games](https://developer.android.com/games/pgs/android/android-signin).

  - For Unity games, see
    [Platform authentication for Unity](https://developer.android.com/games/pgs/unity/unity-start#signin).

  - The C API V2 for Play Games Services is coming soon.

## Define and manage achievements, leaderboards, and events

You can create, edit, and delete achievements, leaderboards, and events in
Google Play Console. For more information, see the following guides:

- [Achievements](https://developer.android.com/games/pgs/achievements)

- [Leaderboards](https://developer.android.com/games/pgs/leaderboards)

- [Events](https://developer.android.com/games/pgs/events)

## Enable Saved Games

To enable the Saved Games service, complete these steps in
Play Console:

1. In the [Google Play Console](https://play.google.com/apps/publish/), select a game.
2. In the **Play Games Services - Configuration** page (**Grow users \>
   Play Games Services \> Setup and
   management \> Configuration** ), select **Edit properties**.
3. Turn the **Saved Games** option to **ON**.
4. Click **Save**.

After performing the steps, it may take up to 24 hours for Google Play Games Services to
activate the Saved Games service for your game. If you want to test the Saved
Games service immediately, manually clear the data in the Google Play Services
app on your test device.

To clear the cached data on Android, open
**Settings \> Apps \> Google Play services** , click on **Manage Space** , then
click **Clear All Data**.

For more information about the Saved Games service, see the
[Saved Games game guide](https://developer.android.com/games/pgs/savedgames).

## Add translations

You can set your own translations for game details, including the display name,
game description, and graphic assets. You can also specify your own translations
for achievements and leaderboards that are associated with your game.

To add your own translations for game details:

1. In the [Google Play Console](https://play.google.com/apps/publish/), select a game.
2. Navigate to the **Play Games Services - Configuration** page (**Grow users \> Play Games
   Services \> Setup and
   management \> Configuration**).
3. Select **Edit properties**.
4. Select **Manage translations \> Manage
   your own translations**.
5. Select the languages that you will provide translations for, then click **Apply** to confirm your selection. On the **Properties** page, the languages that you selected become available in the language selector.
6. Select the language that you want to edit from the language selector, then edit the form with your translations for the display name, the description, and the graphic assets.
7. Click **Save changes** to store your translated game details.

For more information on adding translations for achievements and leaderboards,
see the [achievements](https://developer.android.com/games/pgs/achievements) and
[leaderboards](https://developer.android.com/games/pgs/leaderboards) guides.

When displaying game detail, leaderboard, and achievement strings,
Play Games Services uses the game-supported language that is closest to the
user-requested language. For example, if the user's device language preference
is set to French (Canada) (fr-CA), but the game supports only English
(United States) (en-US) and French (France) (fr-FR), Play Games Services selects
the fr-FR strings to display since this is the closest matching language.

## Grant edit permissions to users

To edit Play Games Services settings within Play Console, you must ensure that
your team has the right permissions to manage Play Game Services. See
[Add developer account users and manage permissions](https://support.google.com/googleplay/android-developer/answer/9844686)
for more information about permissions in Play Console.