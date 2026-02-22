---
title: https://developer.android.com/games/playgames/development-test
url: https://developer.android.com/games/playgames/development-test
source: md.txt
---

This guide describes how to test your game for distribution on
Google Play Games on PC. This lets you to test your games before users
are able to play on desktop.

## Add the Google Play Games on PC form factor

Enabling the form factor is required if it is not activated for your game.
To enable the form factor:

1. In the [Google Play Console](https://play.google.com/console/u/0/developers/app/advanced-distribution), go to **Release \> Advanced settings**.
2. In the **Form factors** tab, add *Google Play Games on PC* from the **+ Add form factor** list.
3. In the **Google Play Games on PC** page, for **Releases** select one of the following options:
   - **Use the same release track and artifacts as your mobile app**. Indicates that all PC users (including testers and end users) download the same binary that mobile users receive.
   - **Use a dedicated track for Google Play Games on PC**. Indicates that you can distribute a separate binary to only PC users.
4. Click **Save**.

For example, say you have a game that is already launched on mobile, and you
want to restrict PC users from being able to download the game (from the
standard mobile track) until you have had a chance to test the game. Create a
dedicated testing track. This lets you designate testers who will have
access to your game on PC. You can then release the game to the public after
testing is complete.

During testing, use the dedicated release track for Google Play Games on PC;
this lets only your testers download the game on desktop during testing. Upload
the same build to the closed test track.

### Opt in to Google Play Games on PC distribution

1. In the [Google Play Console](https://play.google.com/console/u/0/developers/app/advanced-distribution), go to **Release \> Advanced settings**.
2. In the **Form factors** tab, click **Manage** to open the settings for **Google Play Games on PC**.
3. Select **Opt-in to Google Play Games on PC** and save the settings.

> [!NOTE]
> **Note:** To finish activating the PC form factor [publish your changes](https://support.google.com/googleplay/android-developer/answer/9859654).

## Create and configure your closed test track

To distribute a build to your testers, create a track:

1. In the [Google Play Console](https://play.google.com/console/u/0/developers/app/closed-testing), go to **Release \> Test \> Closed testing**.
2. Select **Google Play Games on PC only** from the **form factors** list.
3. Create a new closed testing track:
   1. Click **Create track** in the top right corner.
   2. On successful creation, the site directs you to the track page for your new track. This is also located on the closed testing page for the release type.
4. Click **Manage track** for the track.
5. On the **Testers** tab:
   1. Create and configure the groups you want to test.
   2. Make a note of the opt-in URL provided for the test track. Your testers need to opt in using this link.

### Release on the dedicated track

Create a new Google Play Games on PC release on the closed track and upload
your game.

1. Go back to the track page for your new track. See [Create and configure your Play multiplatform users track](https://developer.android.com/games/playgames/development-submit#users-tracks) to manage the track.
2. Click **Create release** , which opens the **Prepare release** page for the new release.
3. Follow the on-screen instructions to prepare your release:
   - Add your app bundles or APKs.
   - Name your release.
   - Enter release notes for the version of your release.
4. Click **Save**.
5. Click **Review release**.
6. On the **Review** page, ensure that all the information you have entered is correct.
   - Validation errors and warnings appear at the top of the screen. Errors need to be resolved before you can proceed.
   - Review the information on the page to ensure that you have uploaded correct artifacts and entered your release details.
7. Click **Start roll-out** at the bottom of the page to complete rolling out your release.

For more information, see [Prepare and roll out a release](https://support.google.com/googleplay/android-developer/answer/9859348).

### Test your game

Once the published changes are live, your testers should be able to test your
game.

1. Download and install [Google Play Games for PC](https://play.google.com/googleplaygames) (Using the developer emulator is not required).
2. Sign in using one of the test accounts listed on your closed test track.
3. Click the search icon, and search for your game by package name.
4. Install and test the game.

### Release your game to Google Play Games on PC

Once your game has been satisfactorily tested, you can release your game to the
public. This can be done in one of two ways:

- You can release your mobile version of the game to all desktop users.

  1. In the [Google Play Console](https://play.google.com/console/u/0/developers/app/advanced-distribution), go to **Release \> Advanced settings**.
  2. Switch from **Use dedicated release track for Google Play Games on PC** to **Use the same release track and artifacts as your mobile app**.
  3. Submit changes for review.
  4. After approval, users can install the same game version on their PCs.
- To create a separate build for Google Play Games on PC users, keep the
  dedicated release track. Upload a binary to its dedicated production track.

> [!NOTE]
> **Note:** Ensure that the dedicated track is kept up to date with the mobile track to ensure that updates are delivered to Google Play Games on PC users.

## Use Vitals with Google Play Games on PC

You can use [Android vitals](https://developer.android.com/topic/performance/vitals) to monitor the crash and
ANR rates for your game after you have rolled it out to production on
Google Play Games on PC, just as you would with the mobile version.
Filter with the **Form factor** and select `Google Play Games on PC` to see the
crash and ANR rates on Google Play Games on PC.