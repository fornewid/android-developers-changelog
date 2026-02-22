---
title: https://developer.android.com/games/pgs/next-gen-player-ids
url: https://developer.android.com/games/pgs/next-gen-player-ids
source: md.txt
---

To further enhance the privacy of users, we are introducing PGS next generation
Player IDs. With next generation Player IDs, users will be assigned a different
[Player ID](https://developers.google.com/android/reference/com/google/android/gms/games/PlayersClient#public-abstract-taskstring-getcurrentplayerid)
for each game they play. However, the
Player ID remains consistent for a given game
([PGS Project](https://developer.android.com/games/pgs/console/setup)) across devices.

Next generation Player IDs will only apply to users who have never authenticated
for your game with PGS. **Existing users who have already logged into your game
will continue to get the same Player ID.**

Next generation Player IDs will be rolled out gradually and will eventually be a
requirement for all PGS projects starting August 2025. For a detailed timeline
of the rollout plan, review this [blog post](https://android-developers.googleblog.com/2023/02/enable-next-generation-ids-for-better-play-games-services-support-for-all-google-accounts.html).
| **Note:** Next generation Player IDs enable better Play Games Services support for all accounts, including those [under supervision](https://support.google.com/families/answer/9499456).

## Use next generation Player IDs

To support next generation Player IDs, do the following:

1. In the [Google Play Console](https://play.google.com/apps/publish/), select a game.
2. Navigate to **Grow users \> Play Games Services \> Setup and management \> Configuration**.
3. On the configuration page, select **Edit properties**. This page includes the settings to enable next generation Player IDs, as shown in the following image:

![Play Games Services Next Generation ID Config](https://developer.android.com/static/images/games/pgs/pgs-next-gen-id-config.png)

Prior to publishing the change to enable next generation Player IDs, we
recommend using [tester accounts](https://developer.android.com/games/pgs/console/setup#test) to verify that
next generation Player IDs won't cause issues with your identity system.

To do this, set the radio button to "On" but don't publish the change. Once the
radio button is set to "On", the tester accounts will return next generation
Player IDs for you to test with. **This setting will apply to all the games
linked to this PGS project.**
| **Note:** Existing tester accounts will need to recreate their PGS profile in order to receive next generation Player IDs.

Once you have completed testing, [publish the change with your PGS project in
the Play Console](https://developer.android.com/games/pgs/console/publish)
(under **Play Games Services \> Setup and
management \> Publishing**) so the change goes into effect and all new users
start receiving next generation IDs.
| **Note:** If issues arise in production, you can choose to temporarily disable next generation IDs by selecting "Off" and [publishing the new change](https://developer.android.com/games/pgs/console/publish).

## Test next generation Player IDs

If your game doesn't make the assumption that a Player ID will be consistent
across different titles, then we expect that you will be able to enable next
generation Player IDs without issues. However, we still recommend testing to
confirm there won't be any issues.

A few tests we would recommend running:

- Ensuring tester accounts (receiving next generation Player IDs) are able to authenticate and link their PGS profile with game progresses.
- (If applicable) Tester accounts are able to authenticate to the same identity system with the same PGS profile across separate games, and have their progress tracked.

| **Note:** Next generation Player IDs are supported on devices running GMS Core versions 22.30.12 or higher. More info on how to check the GMS Core version can be found [here](https://developer.android.com/games/playgames/faq#q_why_does_v2_auto_sign-in_fail_on_a_mobile_device). For all devices running versions older than this, next generation IDs won't be supported.

## Use the developer player key

If you need a way to identify a user across your titles to offer cross-game
users experiences, you can use the *developer player key* . The *developer
player key* is only accessible through the REST Web APIs. To retrieve the ID:

1. [Create a server-side web app](https://developer.android.com/games/pgs/android/server-access#create_a_server-side_web_app).
2. Make the following HTTP request:

   `GET https://www.googleapis.com/games/v1/players/me/scopedIds`

The response will have one field:

`developer_player_key (string)` - The user's ID which will be the same
across a developer's applications in their Google Play Console.
| **Warning:** If a game transfers developer accounts, then the *developer player key* will change. **Therefore, you should not consider this as a stable
| identifier, nor as a primary key to access progress.** This also should not be considered a Player ID when interacting with the PGS API. The developer player key should only be user to enable cross-game capabilities, as needed.

## Retrieve a list of Player IDs across your applications

You can also retrieve a list of your user's Player IDs across the list of
applications that are owned by your developer account. Please note that a user
will only have an ID for the games that they have been signed into with PGS.

1. [Create a server-side web app](https://developer.android.com/games/pgs/android/server-access#create_a_server-side_web_app).
2. Make [the following HTTP request](https://developer.android.com/games/services/web/api/rest/v1/players/getMultipleApplicationPlayerIds):

   `GET https://www.googleapis.com/games/v1/players/me/multipleApplicationPlayerIds`