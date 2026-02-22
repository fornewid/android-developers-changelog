---
title: https://developer.android.com/games/pgs/console/publish
url: https://developer.android.com/games/pgs/console/publish
source: md.txt
---

To ensure that Google Play Games Services are functioning correctly in your application, you
should test your Play Games Services before publishing your game changes on Google
Play.

## Enable accounts for testing

If your game is in an unpublished state, you must allowlist the user accounts
that you want to grant access for testing. Otherwise, your testers will
encounter OAuth and 404 errors when attempting to access the Play Games Services
endpoints such as [platform authentication](https://developer.android.com/games/pgs/signin).
| **Warning:** Remember to add **yourself** as a tester, or the Play Games SDK won't work for your user account.

There are two ways to enable testers to use PGS APIs for your game:

- At an individual level, by adding individual email addresses.
- At a group level, by enabling Play Games Services for a Play Console release track.

To add individual testers to your game project:

1. In the [Google Play Console](https://play.google.com/apps/publish/), select a game.
2. Open the **Testers** tab for your game in the Google Play Console (**Grow users \>
   Play Games Services \> Setup and
   management \> Testers**).
3. Click the **Add testers** button.
4. In the dialog that appears, enter the email addresses of the Google Accounts that you want to add as testers (separated with commas or one email address per line).
5. Click **Add** to save the users as testers. The tester accounts you added should be able to access your Play Games Services within a couple of hours.

To give testing access to a group, enable a release track to access PGS:

Google Play distributes pre-release versions of your app to
controlled groups of trusted users with the release track features. See
[Set up an open, closed, or internal test](https://support.google.com/googleplay/android-developer/answer/9845334)
to learn more about testing with release tracks.

You can grant access to test your game to all users who have access to test APKs
on a given release track. This works the same as if you had added them to the
tester list individually. To do this, follow these steps:

1. In the [Google Play Console](https://play.google.com/apps/publish/), select a game.
2. Open the **PGS Testers** section (**Grow users \> Play Games Services \>
   Setup and management \> Testers** ) and select the **Release tracks** tab. On this page, you can also see the list of tracks that are already enabled for PGS testing.
3. Click **Add tracks**.
4. Select one or more tracks to enable for PGS testing.
5. Click **Add Tracks**.

The selected release tracks now appears on the list of tracks enabled for
PGS testing.
| **Note:** This feature is only available if you have an Android app linked to your game in Google Play Console.

## Publish game changes

Once you are ready to share your latest game changes with players, it's time to
publish them. Publishing your game changes makes the Play Games Services that you
have configured available to public users of your game. This is different from
publishing your game APK and won't display any information about your game on
the Play Store. Instead, it means that all users with your game APK will be able
to access Play Games Services features, such as authentication,
without needing to be added individually as a tester or be given access to a
release track.

It can take up to 2 hours for Play Games Services changes made in
Play Console to be ready for end users. Ensure that your
Play Games Services game project is published at least 2 hours before your game
goes live on the Play Store, or users may have trouble using Play Games Services
features (including authentication). Publishing your
Play Games Services game project enables Play Games Services for your game.
However, it does not make your game available or visible on the Play Store.

To publish your Play Games Services changes:

1. In the [Google Play Console](https://play.google.com/apps/publish/), select a game.
2. Open the **Publishing** section for your game in the Play Console (**Grow users \> Play Games
   Services \> Setup and
   management \> Publishing**), then follow the instructions on that screen to publish your game.
3. If there are missing or incorrectly configured items that are preventing you from publishing your game, the **Publishing** section will tell you what those items are so that you can fix them.

The data for listed testers for the game is not automatically deleted when you
publish the game changes. To delete data for testers, use the
[Play Games Services Management APIs](https://developer.android.com/games/pgs/management).
| **Note:** If you are using leaderboards and achievements in your game, these game features may not be immediately reflected under your game's listing in the Google Play Store until your users start earning achievements and posting scores.