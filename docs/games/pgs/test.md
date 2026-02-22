---
title: https://developer.android.com/games/pgs/test
url: https://developer.android.com/games/pgs/test
source: md.txt
---

To check that Google Play Games Services (PGS) are functioning correctly in your application,
test your Google Play Games Services before publishing your game changes on Google Play.

If your game is in an unpublished state, you must allowlist the user accounts
that you want to grant access for testing. Otherwise, your testers
encounter OAuth and 404 errors when attempting to access the Google Play Games Services
endpoints such as [sign-in](https://developer.android.com/games/pgs/android/android-signin).
| **Warning:** Remember to add **yourself** as a tester so that the Play Games SDK works for your user account, too.

There are two ways to enable testers to use PGS APIs for your game:

- At an individual level, by adding individual email addresses.
- At a group level, by enabling Play Games Services for a Play Console release track.

To add individual testers to your game project, complete these steps:

1. Open the **Testers** tab for your game in the Google Play Console (**Grow users \>
   Play Games Services \> Setup and
   management \> Testers**).
2. Click the **Add testers** button.
3. In the dialog that appears, enter the email addresses of the Google Accounts that you wish to add as testers (separated with commas or one email address per line).
4. Click **Add** to save the users as testers. The owners of the tester accounts that you added should be able to access your Google Play Games Services within a couple of hours.

![](https://developer.android.com/static/images/games/pgs/consoleAddTesters.png)

To give testing access to a group, enable a release track to access PGS.

Google Play makes it easy to distribute pre-release versions of your app to
controlled groups of trusted users with the release track features. Learn more
about [testing with release
tracks](https://support.google.com/googleplay/android-developer/answer/9845334).

You can grant access to test your game to all users who have access to test APKs
on a given release track. This works the same as if you had added each user to
the tester list individually. To do this, follow these steps:

1. Open the **PGS Testers** section (**Grow users \> Play Games Services \>
   Setup and management \> Testers** ) and select the **Release tracks** tab. On this page, you can also see the list of tracks that are already enabled for PGS testing.
2. Click **Add tracks**.
3. Select one or more tracks to enable for PGS testing.
4. Click **Add Tracks**.

The selected release tracks appear in the list of tracks enabled for PGS
testing.
| **Note:** This feature is only available if you have an Android app linked to your game in Google Play Console.

## Configure the production testing track

If you are testing in the [Production](https://play.google.com/console/u/0/developers/app/tracks/production)
**(Test and release \> Production)** testing track using a [personal testing
account](https://support.google.com/googleplay/android-developer/answer/14151465),
you must have also configured your OAuth audience setting in Google Cloud as
**External** . For more information, see
[Manage App audience](https://support.google.com/cloud/answer/15549945).