---
title: https://developer.android.com/games/pgs/android/anti-piracy
url: https://developer.android.com/games/pgs/android/anti-piracy
source: md.txt
---

This guide describes how to use the anti-piracy feature to secure your
Android games.

The anti-piracy feature is available for Android games only. If anti-piracy is
turned on for your game, the Google Play Games Services checks if the
authenticated user or any other user account on the same device is licensed to
play your game. If none of the user accounts on the device are licensed for your
game, the Play Games Services calls sent by your game fail and return a
`LICENSE_CHECK_FAILED` status code.

To be licensed for your game, users must install it from Google Play. The
license checking takes place regardless of whether your game is a free or paid
app. The checking is only performed if the game is published. If the
authenticated user is a test account, they can play the game without purchasing
it.

## Enable anti-piracy

To turn on the anti-piracy feature for your Android game:

1. Follow the steps described in
   [Set Up Your Game](https://developer.android.com/games/pgs/console/enable-features) to add your Android game
   to the Google Play Console, if you have not done so already.

2. In the [Google Play Console](https://play.google.com/console/), open the **Settings** tab, click
   **Game projects** and select your Game Project from the list.
   Select your game to manage Play Games Services settings.

3. In the **Play Games Services configuration** page, go to the
   **Credentials** section. Then, select an existing Android credential or add
   a new one.

4. Turn on the **Enable anti-piracy** option.

5. Click **Save changes**.

6. Publish your game in order for license checking to be
   activated.